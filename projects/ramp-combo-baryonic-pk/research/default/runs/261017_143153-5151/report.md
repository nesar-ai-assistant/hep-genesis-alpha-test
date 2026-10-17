# Baryonic suppression of the matter power spectrum: HACC emulator predictions at z=0 and a literature assessment of AGN feedback and weak-lensing impact

## Abstract

We used the HACC hydrodynamics emulator to predict the z=0 ratio P_hydro/P_grav at six parameter points, holding cosmology fixed at omega_m=0.14 and sigma_8=0.8.

- **Suppression at k=1 h/Mpc.** It runs from an enhancement of 0.2% at the weakest AGN point to 2.9% suppression at the lowest wind coupling (kappa_w=2).
- **Suppression at k=3 h/Mpc.** The largest sampled value is 10.9%.
- **Comparison with observations.** Every sampled point is consistent with the HSC-XXL gas-fraction constraint of 5+/-4% at k=1. All of them fall well short of the eROSITA+kSZ preference of 10+/-2%. At k=3 they also fall short of the cluster-calibrated 18.4% from arXiv:2309.02920.
- **Unresolved curve shape.** The emulator curves are still deepening at k≈3.7 h/Mpc, the furthest point we could read. The suppression minimum and the high-k upturn are therefore not resolved.

From the literature, AGN feedback in groups and clusters ejects gas and drives the suppression. Lower cluster gas fractions and jet-mode feedback strengthen it. For weak lensing, reconciling KiDS or DES shear with Planck through baryons alone requires suppression stronger and reaching larger scales than current simulations predict. FLAMINGO concludes that baryons are unlikely to drive the S8 tension.

We computed no lensing observable.

## Background

The effect of galaxy formation on the total matter power spectrum was established with the OWLS simulations (arXiv:1104.1174). A library of 92 simulation power spectra provides benchmark ratios (arXiv:1906.00968). The commonly quoted shape is a 10–30% minimum at k≈5–20 h/Mpc followed by a high-k upturn. That shape was flagged in the survey as general knowledge and was not sourced from these papers during the run.

Within the texts that were read, the mechanism is as follows:

- **Gas redistribution.** Energy injected by AGN redistributes gas relative to the dark matter. This suppresses small-scale power by tens of percent relative to dark-matter-only runs (arXiv:2512.02954).
- **Outward and inward baryon motion.** Below about 10 Mpc, AGN push baryons outward. On smaller scales, star formation concentrates baryons in halo centres (arXiv:2309.02920).
- **What strengthens the response in FLAMINGO** (arXiv:2410.17109):
  - lower gas fractions in groups and clusters;
  - collimated jets in place of thermal AGN feedback;
  - lower stellar mass at fixed gas fraction.
- **Redshift dependence in FLAMINGO.** The response grows as redshift falls.
  - The fiducial minimum moves from k=6 h/Mpc at z=2 to k=10 h/Mpc at z=0.
  - The departure from unity begins at k≈1 h/Mpc at z=2 and at k≈0.1 h/Mpc at z=0.
- **Gas-fraction variants in FLAMINGO.** Thermal-AGN variants spanning fgas −10σ to +4σ keep the z=0 minimum at k=8–10 h/Mpc. These variants mainly change the amplitude of the response.
  - The response saturates below fgas−8σ, which is an emulator extrapolation.
  - The jet model has a similar k-range and minimum position.
- **Cosmology dependence and accuracy in FLAMINGO.** The cosmology dependence is about 1% at k<10 h/Mpc, and the emulator is accurate to better than 1% up to k=10 h/Mpc and z=3.
- **Depth of the FLAMINGO z=0 minimum.** The text states no number. It is shown only graphically, in Figs. 2, 5 and 6 of that paper.

Observational benchmarks at k=1 h/Mpc, for haloes with 13<log10 M500<14 at 0<z<1 (arXiv:2512.02954):

| Constraint | Suppression at k=1 h/Mpc | Agreement with simulations |
|---|---|---|
| eROSITA+kSZ | 10+/-2% | Only the strong-feedback runs BAHAMAS 8.0 and FLAMINGO fgas−8σ agree |
| HSC-XXL | 5+/-4% | — |

The same paper notes that the simulations differ from each other by more than 10% at k=1 h/Mpc.

Grandis et al. (arXiv:2309.02920) derive cluster-based baryon-correction results:

| Model | Suppression at k=1 h/Mpc | Suppression at k=3 h/Mpc |
|---|---|---|
| Fiducial | 0.042 (+0.012/−0.014) | 0.184 (+0.026/−0.031) |
| Alternative | 0.049 | 0.179 |

At 97.5% credibility they find an impact below 1% for k<0.37 h/Mpc. They state that some hydrodynamical simulations have feedback that is either too strong or too weak.

For weak lensing, the relevant results are:

- **KiDS-1000.** Amon & Efstathiou (arXiv:2206.11794) show that KiDS-1000 shear, with S8 = 0.759 (+0.024/−0.021), can be reconciled with Planck ΛCDM if the non-linear power is suppressed with A_mod≈0.69. This is a sufficient route, not shown to be the only one. The suppression must extend to k≈0.2 h/Mpc, outside the BAHAMAS range.
- **DES Y3.** Preston, Amon & Efstathiou (arXiv:2305.09827) find that DES Y3 requires a weaker suppression than KiDS. It is still more extreme than recent hydrodynamic simulations predict. They note that underestimating baryonic effects is not the only possible interpretation.
- **FLAMINGO.** FLAMINGO (arXiv:2309.07959) finds that "it is unlikely that baryon physics is driving this modification."
- **Mitigation by gas calibration.** Siegel et al. (arXiv:2512.02954) use an LSST-Y1-like mock.
  - Ignoring baryons biases S8 significantly.
  - An uninformed baryonification model removes the bias but roughly doubles the S8 uncertainty.
  - A kSZ+eROSITA-calibrated prior recovers about half of the lost precision.
  - The bias is shown only graphically.
- **Mitigation by theoretical-error covariance.** Maraio, Hall & Taylor (arXiv:2410.12500) replace scale cuts with a theoretical-error covariance in P(k). For a Euclid-like survey with ell_max=5000, this reduces the bias in Ω_m and S8 to acceptable levels with a modest increase in variance. This statement rests on that paper's abstract and was not independently verified by the critic.

Other relevant tools named in the survey are BCemu (arXiv:2108.08863), the baryonic correction model (arXiv:1810.08629) and the analytic model of arXiv:2504.15633. None of these was available to run.

## Results

### HACC emulator: fiducial, strong and weak AGN points

The HACC Pk-ratio emulator has a 7-parameter design built from 110 simulations in 400 Mpc/h boxes. Its parameters and ranges are:

| Parameter | Meaning | Range |
|---|---|---|
| kappa_w | AGN wind coupling | [2, 4] |
| e_w | AGN energy efficiency | [0.2, 1] |
| M_seed | Black-hole seed mass, in 10^6 Msun | [0.6, 2] |
| v_kin | Kinetic feedback velocity, in 10^4 km/s | [0.1, 1.2] |
| eps_kin | Kinetic efficiency, in units of 10 | [0.02, 1.2] |
| omega_m | Ω_m h² | [0.12, 0.155] |
| sigma_8 | — | [0.7, 0.9] |

The reference spectrum is the emulator's P_grav, not a matched dark-matter-only run.

All runs are at z=0 with omega_m=0.14 and sigma_8=0.8. The "fiducial" point is the centre of the parameter ranges, not a calibrated model. The three points are:

- **Fiducial:** e_w=0.6, v_kin=0.65, eps_kin=0.61.
- **Strong:** e_w=1.0, v_kin=1.2, eps_kin=1.2.
- **Weak:** e_w=0.2, v_kin=0.1, eps_kin=0.02.

All three use kappa_w=3 and M_seed=1.3.

| k [h/Mpc] | Fiducial | Strong | Weak |
|---|---|---|---|
| 0.10 | 0.99968 | 0.99962 | 1.00009 |
| 0.51 | 0.99197 | 0.99062 | 1.00096 |
| 1.00 | 0.97832+/-0.00096 | 0.97506+/-0.00175 | 1.0023+/-0.0025 |
| 2.00 | 0.95104+/-0.00229 | 0.94463+/-0.00405 | 1.0089 |
| 3.0 | 0.91968+/-0.00346 | 0.91207+/-0.00596 | 1.0074 |
| 3.71 | 0.8979 | 0.8904 | 1.0012+/-0.0105 |

Expressed as suppression at k=1 h/Mpc, the values are 2.2% (fiducial), 2.5% (strong) and −0.2% (weak). The negative value means the weak point is enhanced.

The weak point shows no suppression anywhere in the readable range. Its ratio peaks at about 1.0097+/-0.0072 near k≈2.4 h/Mpc. We do not have a sourced physical explanation for this enhancement in the emulator.

Moving e_w, v_kin and eps_kin together to their upper bounds changes the k=1 suppression by only about 0.3 percentage points relative to the fiducial. That shift is comparable to the emulator 1σ at k=1, which is 0.1–0.25%. The weak-to-fiducial difference of 2.4 pp is well resolved.

The suppression in the fiducial and strong runs is still deepening at k=3.71 h/Mpc. Their minimum therefore lies at higher k and was not measured.

Figure 8 overlays the three z=0 ratio curves (fiducial, strong, weak) produced by the emulator plotting tool:

[[FIGURE 8]]

Figure 9 shows the fiducial prediction with its emulator uncertainty band:

[[FIGURE 9]]

Warning: the board's quoted CSV excerpts stop near k≈0.12 h/Mpc. Every value at k≥0.5 h/Mpc is therefore taken from the run summaries and could not be checked against the quoted tool output.

The original statement that the full AGN design range spans only −0.2% to +2.5% at k=1 was contested. It is contradicted by the kappa_w=2 run below. That statement is superseded by the six-point summary given later in this section.

### One-at-a-time sensitivity: kappa_w and M_seed

Each run below varies one parameter and keeps all others at the fiducial values. Suppression is 1−P_hydro/P_grav, with the emulator 1σ in brackets.

| Run | k=0.997 | k=3.007 | k=3.714 h/Mpc |
|---|---|---|---|
| Fiducial | 2.17% (0.10%) | 8.03% (0.35%) | 10.2% |
| kappa_w=2 | 2.92% (0.15%) | 10.93% (0.54%) | 13.66% (0.64%) |
| kappa_w=4 | 1.31% (0.13%) | 4.95% (0.46%) | 6.60% (0.54%) |
| M_seed=2.0 | 2.42% (0.14%) | 9.03% (0.49%) | 11.40% (0.57%) |

Lower wind coupling kappa_w strengthens the suppression.

Ranking the shifts from the fiducial gives the following.

- **At k=1:** the joint lowering of e_w, v_kin and eps_kin (−2.4 pp) is the largest. It is followed by kappa_w across its range (1.6 pp spread: +0.75 pp at kappa_w=2, −0.86 pp at kappa_w=4). Next is the joint raising of e_w, v_kin and eps_kin (+0.33 pp), and last is M_seed from 1.3 to 2.0 (+0.25 pp).
- **At k=3:** the joint lowering of e_w, v_kin and eps_kin (about −8.8 pp) is again the largest shift sampled. It is followed by kappa_w (5.98 pp spread; +2.9 pp at kappa_w=2), then M_seed (+1.0 pp), then the joint raising (+0.76 pp).

Of the parameters varied singly, kappa_w has the largest one-at-a-time effect. However, it is not the largest shift sampled, because the joint move of the three AGN energy and kinetic parameters toward their lower bounds is larger.

At k=3 every shift exceeds the emulator 1σ of 0.35–0.54%. At k=1 the M_seed shift and the joint-raising shift are only about 2σ.

e_w, v_kin and eps_kin were only ever moved together, so their individual sensitivities are unknown. omega_m and sigma_8 were never varied. As a result, the roughly 1% cosmology independence reported by FLAMINGO has not been checked for HACC.

For the kappa_w and M_seed runs, no values at k=0.1 or 0.5 h/Mpc are on the board. For the fiducial and strong points only, the large-scale suppression is about 0.03–0.04% at k=0.1 h/Mpc and about 0.8–0.9% at k=0.5 h/Mpc. The weak point is slightly enhanced at these k.

No comparison plot was produced for these runs.

### Comparison with observational and calibrated benchmarks

This is a range-of-model check, not a calibration. The cosmology and halo-mass weighting differ between HACC and the observational analyses, and HACC parameters do not map onto FLAMINGO fgas, FLAMINGO jet or BCemu parameters.

**At k=1 h/Mpc.** Across the six sampled points (fiducial, strong, weak, kappa_w=2, kappa_w=4, M_seed=2), the suppression spans −0.2% to 2.9%. None reaches 5% or 10%. The most suppressed point, kappa_w=2 at 2.92+/-0.15%:

- is about 0.5σ from HSC-XXL;
- falls short of eROSITA+kSZ by about 3.5σ, using the observational error only;
- relative to Grandis et al., the fiducial and strong points sit about 1.2–1.4σ below their 4.2%.

**At k=3 h/Mpc.** The fiducial and strong HACC points give 8.0% and 8.8%. These are a factor of about 2.1–2.3 below the 18.4% of arXiv:2309.02920, or about 3.1–3.4σ against that paper's lower error bar. The largest sampled value, 10.9+/-0.5% at kappa_w=2, is still about 2.4σ low.

This k=3 gap is unexplained, and the critic contested the comparison. Possible contributors are:

- HACC's minimum lies beyond k=3.7 h/Mpc, while FLAMINGO's lies at 8–10 h/Mpc, so the curve shapes may differ.
- The cosmologies and halo-mass ranges differ. arXiv:2309.02920 is calibrated on haloes above about 3e13 Msun.
- HACC uses P_grav as its reference spectrum.
- Combined extremes were not sampled, for example kappa_w=2 together with high e_w, v_kin, eps_kin and M_seed.

### Weak-lensing implications

No C_ell, xi_+ or S8 shift was computed, because no tool provides them. All lensing statements in this report come from the literature.

The A_mod-type suppression required by Amon & Efstathiou and Preston et al. scales the whole non-linear part of P(k), with A_mod≈0.69 for KiDS. It reaches down to k≈0.2 h/Mpc. The HACC fiducial and strong points suppress P(k) by less than 1% at k≤0.5 h/Mpc and by at most 2.5% at k=1 h/Mpc.

Within the sampled range, the emulator is far from the suppression needed to reconcile shear with Planck. This comparison is approximate and was contested by the critic as a rough mapping between different parameterisations.

FLAMINGO likewise reports that the Amon–Efstathiou response lies outside the reach of the FLAMINGO emulator (arXiv:2410.17109). Both of its fgas−8σ models, thermal and jet, fall inside the Bigwood et al. 2024 ranges, with or without kSZ.

The only sourced multipole range is that the baryon-sensitive shear extends to ell≈5000 (arXiv:2410.12500). The DES Y3 numerical A_mod was not read.

## Discussion

The emulator results agree qualitatively with the literature on two points:

- Suppression grows with k through the readable range.
- Suppression is weak on linear scales, below 1% at k<0.5 h/Mpc for the suppressed points. This is consistent with the <1% bound at k<0.37 h/Mpc from arXiv:2309.02920.

Quantitatively, the sampled HACC models are mild-feedback models. At k=1 they sit at the low end of the HSC-XXL range. They cannot reproduce the strong feedback preferred by eROSITA+kSZ (arXiv:2512.02954) or the k=3 cluster-calibrated amplitude (arXiv:2309.02920).

The weak-AGN corner even shows a net enhancement of about 1% near k≈2.4 h/Mpc. The sensitivity scan suggests that the amplitude is controlled more by kappa_w and by moving the energy and kinetic parameters toward their lower bounds than by raising them. Raising e_w, v_kin and eps_kin together to their maximum adds only 0.3–0.8 pp. This saturation is reminiscent of FLAMINGO's reported saturation below fgas−8σ. However, the two parameterisations are not comparable, and this resemblance is not a demonstrated link.

There is an unresolved tension at k=3 that cannot be settled without the curve beyond k=3.7 h/Mpc. If HACC's minimum sits at k≈8–10 h/Mpc like FLAMINGO's, the k=3 deficit reflects a genuinely weaker amplitude. If the shape differs, the comparison at a single k is misleading.

For weak lensing, the evidence assembled supports the FLAMINGO conclusion. Feedback consistent with X-ray gas fractions is not strong enough, nor large-scale enough, to remove the S8 tension. The KiDS and DES A_mod solutions require suppression extending to k≈0.2 h/Mpc, which is well beyond any of our sampled emulator points. The eROSITA+kSZ results favour stronger feedback than the fiducial simulations, which reopens part of this question. Even so, that paper's mitigation analysis treats baryons as a nuisance to calibrate, not as a resolution of the tension.

Dead ends:

- **Reading the CSVs beyond k≈3.73 h/Mpc.** The plain-text reader has no offset parameter and truncates each 799-bin CSV near k≈3.73 h/Mpc. The table loader rejects the header row, and no file-writing tool was available to make a header-free copy. As a result, values at k=5 and 10 h/Mpc, the minimum and any upturn were never extracted.
- **Running other baryonic emulators.** No BCemu, BACCO or FLAMINGO emulator was available. Every computed number is from HACC.

## Limitations

- **Truncated k range.** The k range effectively stops at 3.7 h/Mpc in our readout. The depth and position of the suppression minimum, which is a central quantity in the task, are not delivered. Whether the emulator itself reaches 10 h/Mpc is also not established.
- **Unverified mid- and high-k values.** The quoted evidence for every CSV ends near k≈0.12 h/Mpc. Values at k≥0.5 h/Mpc rest on run summaries.
- **Limited sampling.** Only six points were sampled, all at z=0 and at a single cosmology. There is no redshift scan, which matters because the lensing-weighted redshift is about 0.3–0.5. There is no cosmology variation, no fGas link and no combined-extreme points.
- **Missing literature numbers.** The FLAMINGO z=0 minimum depth and the DES Y3 A_mod are unsourced. arXiv:2305.09827 and arXiv:2410.12500 were not added to the bibliography. The 1104.1174 claims about the minimum and upturn were never verified.
- **No lensing calculation.** No projected lensing calculation was possible.
- **Budget.** The two-wave budget was exhausted. The planned robustness and cosmology cross-checks were replaced by the limited sensitivity scan reported above.

## Open directions

1. Re-read the 799-bin HACC Pk-ratio CSVs with a proper CSV reader to get the ratio at k=5 and 10 h/Mpc, the
