import numpy as np, pandas as pd, pyccl as ccl
from scipy.optimize import least_squares

omega_m_phys = 0.14176
sigma8_hacc  = 0.8102
h = 0.6727
Omega_m = omega_m_phys / h**2
Omega_b = 0.0492
Omega_c = Omega_m - Omega_b
print(f"Derived cosmology: Omega_m={Omega_m:.5f}, Omega_c={Omega_c:.5f}, Omega_b={Omega_b:.5f}, h={h}, sigma8={sigma8_hacc}")

cosmo_nobar = ccl.Cosmology(Omega_c=Omega_c, Omega_b=Omega_b, h=h, n_s=0.9649,
                             sigma8=sigma8_hacc, matter_power_spectrum='halofit')

z = 0.5
a = 1/(1+z)

path = "/Users/nramachandra/hep-genesis-testing/projects/expert-schneider15-cl-bias/runs/261025_162428/Pk-ratio_z0.5000_prediction.csv"
df = pd.read_csv(path, comment="#")
k_hacc = df['x'].values
S_hacc = df['y_mean'].values

mask = (k_hacc > 0.05) & (k_hacc < 10.0)
k_fit = k_hacc[mask]
S_fit = S_hacc[mask]
print(f"Fitting over {mask.sum()} k-bins in [{k_fit.min():.3f}, {k_fit.max():.3f}] h/Mpc")

def model_S(params):
    log10Mc, eta_b = params
    bar = ccl.BaryonsSchneider15(log10Mc=log10Mc, eta_b=eta_b, k_s=55.0)
    boost = bar.boost_factor(cosmo_nobar, k_fit, a)
    return boost

def resid(params):
    return model_S(params) - S_fit

x0 = np.array([13.5, 0.5])
res = least_squares(resid, x0, bounds=([11.0, 0.05], [15.5, 2.0]))
print("Fit result:", res.x, "cost:", res.cost, "success:", res.success)
rms = np.sqrt(np.mean(res.fun**2))
print(f"RMS residual in S(k): {rms:.5f}  (max |resid| = {np.max(np.abs(res.fun)):.5f})")

best_log10Mc, best_eta_b = res.x
np.save('/tmp/bcm_fit/best_fit.npy', res.x)
df_out = pd.DataFrame({'k': k_fit, 'S_hacc': S_fit, 'S_bcm_fit': model_S(res.x)})
df_out.to_csv('/tmp/bcm_fit/bcm_vs_hacc_z0.5.csv', index=False)
print(df_out.head(10))
print(df_out.tail(10))
