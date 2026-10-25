"""Direct-pyccl/firecrown workaround for desc_mcp_server bug #5
(firecrown_build_likelihood's pk_modifier factory type is advertised but
not implemented -- cosmology.baryons is silently ignored in pure-CCL mode).

This builds the DES-Y1-like cosmic-shear-only ConstGaussian likelihood
directly in Python (bypassing the broken YAML path), injects a
PowerspectrumModifier using pyccl.BaryonsSchneider15 with parameters
calibrated against the HACC CosmoHydro Pk-ratio emulator prediction at
z=0.5 fiducial design point, and compares chi2(baryons) vs chi2(no baryons)
at the DES-Y1 fiducial cosmology + nuisance point.
"""
import json
import numpy as np
import pyccl
import sacc

from firecrown.likelihood import ConstGaussian, NamedParameters, TwoPoint
from firecrown.likelihood.factories import load_sacc_data
from firecrown.modeling_tools import CCLFactory, ModelingTools, PowerspectrumModifier
from firecrown.updatable import register_new_updatable_parameter
import firecrown.likelihood.weak_lensing as wl
from firecrown.ccl_factory import CCLCreationMode

SACC_PATH = "/Users/nramachandra/hep-genesis-testing/projects/expert-baryon-lensing-bias-3/runs/261024_190326/desy1_shear_only.hdf5"
OUT_DIR = "/Users/nramachandra/hep-genesis-testing/projects/expert-schneider15-cl-bias/runs/pyfit"

# BCM parameters calibrated in fit_script.py against HACC Pk-ratio(z=0.5)
# fiducial design point (omega_m=0.14176, sigma_8=0.8102 converted via
# h=0.6727): log10Mc=13.878, eta_b=0.1707, k_s=55.0 (CCL default),
# RMS residual in S(k) = 0.0105 over k in [0.05, 10] h/Mpc.
BEST_LOG10MC = 13.87825005
BEST_ETA_B = 0.17074722
K_S = 55.0

# DES-Y1 3x2pt fiducial cosmology + nuisance (from the prior session's
# firecrown_build_likelihood metadata.required_parameters -- re-used here
# for consistency with the earlier sigma_8 sensitivity measurement).
COSMO = dict(Omega_c=0.25, Omega_b=0.05, h=0.67, n_s=0.96, sigma8=0.81,
             Omega_k=0.0, Neff=3.044, m_nu=0.0, w0=-1.0, wa=0.0, T_CMB=2.7255)
NUISANCE = dict(ia_bias=0.5, alphaz=0.0, z_piv=0.5,
                 src0_delta_z=0.0, src1_delta_z=0.0, src2_delta_z=0.0, src3_delta_z=0.0,
                 src0_mult_bias=1.0, src1_mult_bias=1.0, src2_mult_bias=1.0, src3_mult_bias=1.0)


class Schneider15HACCBaryonfication(PowerspectrumModifier):
    """BaryonsSchneider15 calibrated to the HACC CosmoHydro Pk-ratio emulator."""

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

    per_bin = [wl.PhotoZShift, ]  # placeholder, real list built below
    sources = {}
    for i in range(4):
        tracer = f"src{i}"
        systs = [wl.MultiplicativeShearBias(sacc_tracer=tracer),
                 wl.PhotoZShift(sacc_tracer=tracer)]
        if with_baryons:
            systs.append(wl.SelectField(field="delta_matter_baryons"))
        sources[tracer] = wl.WeakLensing(
            sacc_tracer=tracer, systematics=systs,
        )

    # global NLA intrinsic alignment, shared across all sources per DES-Y1 setup
    nla = wl.LinearAlignmentSystematic(sacc_tracer=None, alphag=1.0)
    for tracer in sources:
        sources[tracer] = wl.WeakLensing(
            sacc_tracer=tracer,
            systematics=[wl.MultiplicativeShearBias(sacc_tracer=tracer),
                         wl.PhotoZShift(sacc_tracer=tracer)] +
                        ([wl.SelectField(field="delta_matter_baryons")] if with_baryons else []),
        )

    stats = []
    names = list(sources)
    for i, t1 in enumerate(names):
        for t2 in names[i:]:
            stats.append(TwoPoint("galaxy_shear_xi_plus", sources[t1], sources[t2]))
            stats.append(TwoPoint("galaxy_shear_xi_minus", sources[t1], sources[t2]))

    likelihood = ConstGaussian(statistics=stats)
    likelihood.read(sacc_data)

    ccl_factory = CCLFactory(require_nonlinear_pk=True, creation_mode=CCLCreationMode.DEFAULT,
                              amplitude_parameter="sigma8")
    if with_baryons:
        pk_mod = Schneider15HACCBaryonfication()
        tools = ModelingTools(pk_modifiers=[pk_mod], ccl_factory=ccl_factory)
    else:
        tools = ModelingTools(ccl_factory=ccl_factory)
    return likelihood, tools


def eval_chi2(with_baryons: bool):
    from firecrown.updatable import get_default_params_map, ParamsMap

    like, tools = build_likelihood(with_baryons)
    defaults = dict(get_default_params_map(tools, like))
    all_params = dict(COSMO)
    all_params.update(NUISANCE)
    for k, v in all_params.items():
        if k in defaults:
            defaults[k] = v
    pm = ParamsMap({k: (float(v) if not isinstance(v, (list, tuple)) else v) for k, v in defaults.items()})
    tools.update(pm)
    tools.prepare()
    like.update(pm)
    loglike = like.compute_loglike(tools)
    chi2 = -2.0 * loglike
    like.reset()
    tools.reset()
    return chi2, defaults


if __name__ == "__main__":
    chi2_nobar, p_nobar = eval_chi2(False)
    chi2_bar, p_bar = eval_chi2(True)
    print(f"chi2 (no baryons)   = {chi2_nobar:.6f}")
    print(f"chi2 (Schneider15, HACC-calibrated: log10Mc={BEST_LOG10MC:.3f}, eta_b={BEST_ETA_B:.4f}) = {chi2_bar:.6f}")
    print(f"delta chi2 = {chi2_bar - chi2_nobar:.6f}")
    import os
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(f"{OUT_DIR}/chi2_comparison.json", "w") as f:
        json.dump({
            "chi2_no_baryons": chi2_nobar, "chi2_schneider15_hacc": chi2_bar,
            "delta_chi2": chi2_bar - chi2_nobar,
            "bcm_params": {"log10Mc": BEST_LOG10MC, "eta_b": BEST_ETA_B, "k_s": K_S},
            "cosmology": COSMO, "nuisance": NUISANCE,
            "n_data_points": 227, "note": "shear-only (xi+/xi-) DES-Y1-like sacc, src0-3, real space",
        }, f, indent=2)
    print(f"Wrote {OUT_DIR}/chi2_comparison.json")
