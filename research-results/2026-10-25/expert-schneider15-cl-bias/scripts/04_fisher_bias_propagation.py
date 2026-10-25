"""Propagate the baryon-induced DeltaT (biased - unbiased theory vector) into
a parameter-space bias on (Omega_c, sigma8) using the standard linear
Fisher-bias formalism (Amara & Refregier 2008, Eq. in augur's analyze.py
get_fisher_bias): bias_p = (F^-1)_pq B_q,  B_q = sum_ij dT_i/dtheta_q Cov^-1_ij DeltaT_j

This bypasses augur's own fisher_bias tool (which is wired through the same
broken firecrown_build_likelihood -> pure-CCL-mode YAML path that silently
drops the baryons switch, desc_mcp_server#5) by calling the same custom
likelihood object we already validated in firecrown_bias.py / diag_theory.py.
"""
import numpy as np
import pyccl

from firecrown.likelihood import ConstGaussian, TwoPoint
from firecrown.likelihood.factories import load_sacc_data
from firecrown.modeling_tools import CCLFactory, ModelingTools, PowerspectrumModifier
import firecrown.likelihood.weak_lensing as wl
from firecrown.ccl_factory import CCLCreationMode
from firecrown.updatable import get_default_params_map, ParamsMap

SACC_PATH = "/Users/nramachandra/hep-genesis-testing/projects/expert-baryon-lensing-bias-3/runs/261024_190326/desy1_shear_only.hdf5"
BEST_LOG10MC = 13.87825005
BEST_ETA_B = 0.17074722
K_S = 55.0

COSMO0 = dict(Omega_c=0.25, Omega_b=0.05, h=0.67, n_s=0.96, sigma8=0.81,
              Omega_k=0.0, Neff=3.044, m_nu=0.0, w0=-1.0, wa=0.0, T_CMB=2.7255)
NUISANCE = dict(ia_bias=0.5, alphaz=0.0, z_piv=0.5,
                 src0_delta_z=0.0, src1_delta_z=0.0, src2_delta_z=0.0, src3_delta_z=0.0,
                 src0_mult_bias=1.0, src1_mult_bias=1.0, src2_mult_bias=1.0, src3_mult_bias=1.0)


class Schneider15HACCBaryonfication(PowerspectrumModifier):
    name = "delta_matter_baryons:delta_matter_baryons"

    def __init__(self, pk_to_modify="delta_matter:delta_matter"):
        super().__init__()
        self.pk_to_modify = pk_to_modify
        self.bcm = pyccl.BaryonsSchneider15(log10Mc=BEST_LOG10MC, eta_b=BEST_ETA_B, k_s=K_S)

    def compute_p_of_k_z(self, tools):
        return self.bcm.include_baryonic_effects(
            cosmo=tools.get_ccl_cosmology(), pk=tools.get_pk(self.pk_to_modify)
        )


def build_likelihood(with_baryons: bool):
    sacc_data = load_sacc_data(SACC_PATH)
    sources = {}
    for i in range(4):
        tracer = f"src{i}"
        systs = [wl.MultiplicativeShearBias(sacc_tracer=tracer), wl.PhotoZShift(sacc_tracer=tracer)]
        if with_baryons:
            systs.append(wl.SelectField(field="delta_matter_baryons"))
        sources[tracer] = wl.WeakLensing(sacc_tracer=tracer, systematics=systs)
    stats = []
    names = list(sources)
    for i, t1 in enumerate(names):
        for t2 in names[i:]:
            for dt in ("galaxy_shear_xi_plus", "galaxy_shear_xi_minus"):
                stats.append(TwoPoint(dt, sources[t1], sources[t2]))
    likelihood = ConstGaussian(statistics=stats)
    likelihood.read(sacc_data)
    ccl_factory = CCLFactory(require_nonlinear_pk=True, creation_mode=CCLCreationMode.DEFAULT,
                              amplitude_parameter="sigma8")
    if with_baryons:
        tools = ModelingTools(pk_modifiers=[Schneider15HACCBaryonfication()], ccl_factory=ccl_factory)
    else:
        tools = ModelingTools(ccl_factory=ccl_factory)
    return likelihood, tools


def theory_vector(cosmo_overrides, with_baryons=False):
    like, tools = build_likelihood(with_baryons)
    defaults = dict(get_default_params_map(tools, like))
    all_p = dict(COSMO0); all_p.update(NUISANCE); all_p.update(cosmo_overrides)
    for k, v in all_p.items():
        if k in defaults:
            defaults[k] = v
    pm = ParamsMap({k: (float(v) if not isinstance(v, (list, tuple)) else v) for k, v in defaults.items()})
    tools.update(pm); tools.prepare(); like.update(pm)
    like.compute_loglike(tools)
    T = like.compute_theory_vector(tools)
    cov = like.cov  # covariance matrix (property on ConstGaussian/Gaussian likelihood)
    like.reset(); tools.reset()
    return np.asarray(T), cov


if __name__ == "__main__":
    # 1) Fiducial (no baryons) theory vector and covariance
    T0, cov = theory_vector({}, with_baryons=False)
    cov = np.asarray(cov)
    print("cov shape:", cov.shape)
    cov_inv = np.linalg.inv(cov)

    # 2) Biased theory vector (same cosmology, with HACC-calibrated Schneider15 baryons)
    T_biased, _ = theory_vector({}, with_baryons=True)
    delta_T = T_biased - T0
    chi2_check = delta_T @ cov_inv @ delta_T  # NOT the same as delta_chi2 from before (that compares loglike at the SAME params, this is the quadratic form)
    print(f"||delta_T^T Cinv delta_T|| = {chi2_check:.4f}  (cross-check vs earlier delta_chi2=9.8687)")

    # 3) Numerical derivatives dT/dtheta for (Omega_c, sigma8) at the no-baryons model
    step_Oc = 0.01
    step_s8 = 0.01
    Tp_Oc, _ = theory_vector({"Omega_c": COSMO0["Omega_c"] + step_Oc}, with_baryons=False)
    Tm_Oc, _ = theory_vector({"Omega_c": COSMO0["Omega_c"] - step_Oc}, with_baryons=False)
    dT_dOc = (Tp_Oc - Tm_Oc) / (2 * step_Oc)

    Tp_s8, _ = theory_vector({"sigma8": COSMO0["sigma8"] + step_s8}, with_baryons=False)
    Tm_s8, _ = theory_vector({"sigma8": COSMO0["sigma8"] - step_s8}, with_baryons=False)
    dT_ds8 = (Tp_s8 - Tm_s8) / (2 * step_s8)

    # Fisher matrix (2x2) for (Omega_c, sigma8), all else fixed
    J = np.vstack([dT_dOc, dT_ds8])  # (2, n_data)
    F = J @ cov_inv @ J.T
    F_inv = np.linalg.inv(F)
    sigma_Oc = np.sqrt(F_inv[0, 0])
    sigma_s8 = np.sqrt(F_inv[1, 1])
    print(f"Marginalized 1-sigma (Omega_c, sigma8 jointly varied, shear-only 227 pts): "
          f"sigma(Omega_c)={sigma_Oc:.5f}, sigma(sigma8)={sigma_s8:.5f}")

    # Fisher bias vector B_q = J Cinv deltaT ; bias = F^-1 B  (Amara & Refregier 2008)
    B = J @ cov_inv @ delta_T
    bias = F_inv @ B
    print(f"Bias from HACC-calibrated Schneider15 baryons (ignored in the fit): "
          f"delta(Omega_c)={bias[0]:+.5f} ({bias[0]/sigma_Oc:+.2f} sigma),  "
          f"delta(sigma8)={bias[1]:+.5f} ({bias[1]/sigma_s8:+.2f} sigma)")

    import json
    with open("/Users/nramachandra/hep-genesis-testing/projects/expert-schneider15-cl-bias/runs/pyfit/fisher_bias.json", "w") as f:
        json.dump({
            "sigma_Omega_c": float(sigma_Oc), "sigma_sigma8": float(sigma_s8),
            "bias_Omega_c": float(bias[0]), "bias_sigma8": float(bias[1]),
            "bias_Omega_c_sigma": float(bias[0]/sigma_Oc), "bias_sigma8_sigma": float(bias[1]/sigma_s8),
            "delta_T_quadratic_form": float(chi2_check),
            "step_Omega_c": step_Oc, "step_sigma8": step_s8,
            "bcm_params": {"log10Mc": BEST_LOG10MC, "eta_b": BEST_ETA_B, "k_s": K_S},
            "fiducial_cosmology": COSMO0,
        }, f, indent=2)
    print("Wrote fisher_bias.json")
