"""Diagnostic: verify the baryon-induced chi2 shift is driven by physically
sensible small-scale suppression, not a modeling artifact. Dumps per-point
theory vectors with/without baryons and the data vector for comparison.
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

COSMO = dict(Omega_c=0.25, Omega_b=0.05, h=0.67, n_s=0.96, sigma8=0.81,
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

    stats, keys = [], []
    names = list(sources)
    for i, t1 in enumerate(names):
        for t2 in names[i:]:
            for dt in ("galaxy_shear_xi_plus", "galaxy_shear_xi_minus"):
                stats.append(TwoPoint(dt, sources[t1], sources[t2]))
                keys.append((dt, t1, t2))

    likelihood = ConstGaussian(statistics=stats)
    likelihood.read(sacc_data)
    ccl_factory = CCLFactory(require_nonlinear_pk=True, creation_mode=CCLCreationMode.DEFAULT,
                              amplitude_parameter="sigma8")
    if with_baryons:
        tools = ModelingTools(pk_modifiers=[Schneider15HACCBaryonfication()], ccl_factory=ccl_factory)
    else:
        tools = ModelingTools(ccl_factory=ccl_factory)
    return likelihood, tools, keys


def get_theory_vector(with_baryons: bool):
    like, tools, keys = build_likelihood(with_baryons)
    defaults = dict(get_default_params_map(tools, like))
    all_params = dict(COSMO); all_params.update(NUISANCE)
    for k, v in all_params.items():
        if k in defaults:
            defaults[k] = v
    pm = ParamsMap({k: (float(v) if not isinstance(v, (list, tuple)) else v) for k, v in defaults.items()})
    tools.update(pm); tools.prepare(); like.update(pm)
    like.compute_loglike(tools)  # populates .statistics with computed theory
    theory_concat, theta_concat, stat_labels = [], [], []
    for gs in like.statistics:
        st = getattr(gs, "statistic", gs)
        theory = np.asarray(st.get_statistic_results()[0]) if hasattr(st, "get_statistic_results") else None
    # fallback: use likelihood's cached predicted data vector directly
    pred = like.get_data_vector() if hasattr(like, "get_data_vector") else None
    computed = like.compute_theory_vector(tools) if hasattr(like, "compute_theory_vector") else None
    like.reset(); tools.reset()
    return computed, like


if __name__ == "__main__":
    theory_nobar, like_nobar = get_theory_vector(False)
    theory_bar, like_bar = get_theory_vector(True)
    data_vec = like_nobar.get_data_vector()
    print("n_data:", len(data_vec))
    print("theory (no baryons) first 5:", theory_nobar[:5])
    print("theory (baryons)    first 5:", theory_bar[:5])
    ratio = theory_bar / theory_nobar
    print("ratio theory_baryons/theory_nobaryons: min={:.5f} max={:.5f} mean={:.5f}".format(
        ratio.min(), ratio.max(), ratio.mean()))
    # Suppression should be < 1 everywhere for xi+ (power suppressed at small scales)
    frac_below_1 = (ratio < 1.0).mean()
    print(f"fraction of points with ratio<1 (suppression): {frac_below_1:.3f}")
    # Per-statistic breakdown
    idx = 0
    print("\nPer-statistic suppression summary (xi_plus/xi_minus pairs):")
    for gs in like_nobar.statistics:
        st = getattr(gs, "statistic", gs)
        n = len(np.asarray(st.sacc_indices))
        r = ratio[idx:idx+n]
        print(f"  {st.sacc_data_type:28s} {st.sacc_tracers.name1:6s}-{st.sacc_tracers.name2:6s}  n={n:3d}  "
              f"ratio range [{r.min():.5f}, {r.max():.5f}]  mean={r.mean():.5f}")
        idx += n
