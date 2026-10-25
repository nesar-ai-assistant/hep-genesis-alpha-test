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
        super().__init__(); self.pk_to_modify = pk_to_modify
        self.bcm = pyccl.BaryonsSchneider15(log10Mc=BEST_LOG10MC, eta_b=BEST_ETA_B, k_s=K_S)
    def compute_p_of_k_z(self, tools):
        return self.bcm.include_baryonic_effects(cosmo=tools.get_ccl_cosmology(), pk=tools.get_pk(self.pk_to_modify))


def build_likelihood(with_baryons):
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
    ccl_factory = CCLFactory(require_nonlinear_pk=True, creation_mode=CCLCreationMode.DEFAULT, amplitude_parameter="sigma8")
    tools = ModelingTools(pk_modifiers=[Schneider15HACCBaryonfication()] if with_baryons else None, ccl_factory=ccl_factory)
    return likelihood, tools


def run(with_baryons):
    like, tools = build_likelihood(with_baryons)
    defaults = dict(get_default_params_map(tools, like))
    all_p = dict(COSMO0); all_p.update(NUISANCE)
    for k, v in all_p.items():
        if k in defaults: defaults[k] = v
    pm = ParamsMap({k: (float(v) if not isinstance(v, (list, tuple)) else v) for k, v in defaults.items()})
    tools.update(pm); tools.prepare(); like.update(pm)
    loglike = like.compute_loglike(tools)
    T = np.asarray(like.compute_theory_vector(tools))
    D = np.asarray(like.get_data_vector())
    cov = np.asarray(like.cov)
    like.reset(); tools.reset()
    return loglike, T, D, cov


ll0, T0, D, cov = run(False)
ll1, T1, D2, cov2 = run(True)
assert np.allclose(D, D2) and np.allclose(cov, cov2)
cinv = np.linalg.inv(cov)

chi2_0 = (T0 - D) @ cinv @ (T0 - D)
chi2_1 = (T1 - D) @ cinv @ (T1 - D)
print("chi2 via manual (T-D)^T Cinv (T-D), no baryons:", chi2_0)
print("chi2 via manual, with baryons:                 ", chi2_1)
print("delta chi2 (manual):", chi2_1 - chi2_0)
print("chi2 via -2*loglike, no baryons:", -2*ll0, " with baryons:", -2*ll1, " delta:", -2*ll1 - (-2*ll0))

delta_T = T1 - T0
quad = delta_T @ cinv @ delta_T
cross = 2 * delta_T @ cinv @ (T0 - D)
print(f"\nDecomposition check: delta_chi2 = cross-term + quadratic-term")
print(f"  cross term  2*deltaT^T Cinv (T0-D) = {cross:.4f}")
print(f"  quadratic term deltaT^T Cinv deltaT = {quad:.4f}")
print(f"  sum = {cross+quad:.4f}  (should equal delta chi2 manual = {chi2_1-chi2_0:.4f})")
print(f"\n==> The quadratic term alone (0.0244 reported earlier) is NOT delta_chi2;")
print(f"    delta_chi2 is dominated by the cross term, i.e. by how far the FIDUCIAL")
print(f"    theory (no baryons) already sits from the noiseless 'data' vector D in this")
print(f"    particular sacc file. This means the earlier 'delta_chi2=9.87' number is")
print(f"    sensitive to whatever cosmology/nuisance point was used to generate D,")
print(f"    NOT purely the baryon effect size. The clean, model-independent quantity")
print(f"    is the parameter bias from the Fisher-bias formalism (quadratic term only'")
print(f"    conflated in my chi2 framing) -- re-derive bias directly from delta_T, not chi2.")
