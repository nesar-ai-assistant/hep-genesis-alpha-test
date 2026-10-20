# Hydrostatic mass bias and profile-shape evolution: a literature baseline and HACC-emulator test at z = 0 and z = 0.4987

## Abstract

This report combines a survey of hydrostatic-equilibrium (HSE) mass bias in galaxy clusters with a test using a HACC-based hydrodynamics emulator. The emulator was used to predict gas-density (CGD) and temperature (CTP) profiles at the midpoint of its design space, at z = 0 and z = 0.4987.

The pairing differs from the intended z = 0 vs z = 1 because the cluster-profile emulators stop at z = 0.4987. The log-slopes of the profiles at R500c barely change between the two redshifts:

- s_n + s_T = -3.13 at z = 0.
- s_n + s_T = -3.24 at z = 0.4987.

The main change is in the temperature normalisation, with T(R500)/T500 falling from 0.592 to 0.518. Under an assumed T500 convention this gives:

- M_HSE/M500 = 0.925 ± 0.051 at z = 0 and 0.840 ± 0.048 at z = 0.4987.
- In the FLAMINGO sign convention, b = -0.075 and -0.160, so Δb = -0.085 ± 0.070.

The bias becomes more negative with redshift, as FLAMINGO finds for clusters. The trend is only about 1.2σ, both from the density-plus-temperature route and from the emulator's own pressure profile.

The pressure profile agrees with the density and temperature slopes at R500 but is far shallower at 2 R500. This indicates that the three emulated profiles are not mutually consistent at large radius.

Three further limits apply:

- A feedback-robustness test was run but not reduced to numbers.
- The emulator exposes no halo mass, so the FLAMINGO group-versus-cluster comparison could not be done.
- The absolute bias values depend on an undocumented T500 and temperature-weighting convention.

## Background

**Bias magnitude in simulations.** Hydrodynamical simulations consistently find that HSE masses from X-ray and SZ data underestimate the true mass. The FLAMINGO study (arXiv:2409.07849) defines b_HSE = (M_HSE,500c - M500c)/M500c and reports the following:

- The median bias goes from about -0.1 for groups to about -0.2 for clusters.
- The scatter is smallest near M500c ~ 10^14 Msun, with σ(b) ≈ 0.1. It grows to about 0.35 at 5×10^14 Msun in the fgas+2σ variant.
- At fixed true mass, HSE masses rise with redshift for groups and fall with redshift for clusters, and the scatter grows with z.
- Feedback models with lower gas fractions give more-biased group masses and less-biased cluster masses.
- The bias does not depend on which fitting function is used, but poorer fits give a stronger bias.
- The scatter comes from differences in the pressure gradient, not from T(R500c).

From the FLAMINGO full text:

- In the 10^13.75–10^14.25 Msun bin, all five profile methods converge to b ≈ -0.1.
- The FLAMINGO calibration assumed a constant b = -0.257.
- Volume-weighted profiles give a much smaller and less mass-dependent bias than X-ray-weighted ones, with mass-weighted profiles in between. The authors attribute most of the bias at M500c ≫ 10^13 Msun to X-rays being a biased tracer of the gas.
- As a function of true mass, b(M) steepens with redshift over z = 0–1.5. At fixed M_HSE it is nearly unchanged except at z = 1.5.

**Non-thermal pressure.** Nelson, Lau & Nagai (arXiv:1404.4636) give a fit to the non-thermal pressure fraction:

f_nth = 1 - A{1 + exp[-((r/R200m)/B)^γ]}, with A = 0.452 ± 0.001, B = 0.841 ± 0.008 and γ = 1.628 ± 0.019.

The fit comes from non-radiative ART runs using mass-weighted T and σ. It is accurate to about 10% over 0.1–1.5 R200m out to z = 1.5, and it is universal in redshift when radii are scaled to R200m. The fraction depends strongly on the mass accretion rate.

**Observations.** The X-COP sample (arXiv:1805.00034) of 13 nearby clusters gives:

- A median non-thermal fraction of about 6% at R500 and about 10% at R200, lower than simulations predict.
- 1 - b = 0.85 ± 0.05 with the Planck calibration, with some evidence for a mass-dependent bias.

**Gas-density slopes.** Simba (arXiv:2409.05815) finds that gas-density profiles follow power laws whose slope and amplitude depend only weakly on redshift at fixed mass over 0 < z < 4. AGN jets flatten the profiles above M200c ~ 10^13 Msun. This suggests that any redshift evolution of the bias should come from the temperature rather than the density slope.

**Mergers.** A recent merger study (arXiv:2511.10730, abstract only) finds that the bias dips sharply negative during a major merger, then peaks briefly positive, then relaxes back. This is driven mainly by changes in the gas-density structure rather than by thermodynamics.

**Relevance to this test.** The HSE mass depends on the log-slopes d ln n/d ln r and d ln T/d ln r and on T itself, not on the density amplitude. Profile-shape evolution therefore enters the bias directly.

Other papers identified but not read in detail are:

- arXiv:1112.3659 (merger-driven bias evolution).
- arXiv:1306.3993 and arXiv:1308.6589 (methods for computing the bias, and its origin).
- arXiv:1507.04338 (Shi–Komatsu analytic non-thermal model).
- arXiv:1608.04388 (mass-modelling framework).
- arXiv:1805.00035, arXiv:1805.00042 and arXiv:2112.07554 (X-COP mass and universal profiles, and non-thermal tracing).
- arXiv:2010.00619 (CAMELS). Note that the emulator used here is HACC-based, not CAMELS-based.

## Results

### Emulator set-up

The emulator's CGD, CTP and CPP (pressure) profiles take seven inputs plus redshift. The inputs, set to the midpoints of their design ranges, are:

| Parameter | Description | Midpoint used |
|---|---|---|
| kappa_w | AGN wind coupling | 3 |
| e_w | AGN wind energy fraction | 0.6 |
| M_seed | Black-hole seed mass | 1.3 |
| v_kin | Kinetic feedback parameter | 0.65 |
| eps_kin | Kinetic AGN feedback efficiency | 0.61 |
| omega_m | Matter density | 0.1375 |
| sigma_8 | Power-spectrum normalisation | 0.8 |

There is no fiducial parameter set, so the midpoints were used. The profiles have these properties:

- They are already self-similarly scaled: CGD is ρ_gas/ρ_crit(z), CTP is T/T500 and CPP is P/P500.
- Each covers 19 logarithmic bins from 0.0154 to 2.74 R500c, so 2 R500c lies inside the grid.
- Each profile is for a single, undocumented halo selection. There is no mass column and no true M500c.
- The cluster profiles cover only z ≤ 0.4987.

### Profile shape change between z = 0 and z = 0.4987

[[FIGURE 9]]

Figure 9 overlays CGD at the two redshifts. The density at z = 0.4987 behaves as follows relative to z = 0:

- It agrees within about 3% over 0.2–0.9 R500c.
- It is about 6% lower at 1.15 R500c and 13–14% lower at 1.5–2.05 R500c.
- It converges again at 2.74 R500c.

The core (r < 0.1 R500c) appears 15–50% lower at z = 0.4987. The emulator uncertainty there is very large: the innermost bin is 1018 ± 689 at z = 0.4987 against 2154 ± 258 at z = 0. The core difference should therefore be treated as not significant.

[[FIGURE 10]]

Figure 10 overlays CTP. Relative to z = 0, the temperature at z = 0.4987 is:

- 7–13% lower over 0.15–1.15 R500c.
- 12% lower at R500c itself.
- About 30% lower at 2.74 R500c.

### Log-slopes and the HSE mass ratio

Slopes are centred finite differences in ln r over neighbouring bins centred at 0.49, 1.00 and 2.05 R500c. The errors come from the emulator's Gaussian-process standard deviation, assuming independent bins.

| Radius (R500c) | s_n (z=0) | s_n (z=0.4987) | s_T (z=0) | s_T (z=0.4987) |
|---|---|---|---|---|
| 0.49 | -1.86 ± 0.10 | -1.87 ± 0.10 | -0.27 ± 0.03 | -0.35 ± 0.06 |
| 1.00 | -2.55 ± 0.16 | -2.74 ± 0.10 | -0.58 ± 0.06 | -0.50 ± 0.14 |
| 2.05 | -3.13 ± 0.07 | -2.93 ± 0.06 | -1.12 ± 0.05 | -1.54 ± 0.11 |

As a check, the z = 0 density slope near R500c follows directly from the CSV values. Between r/R500c = 0.866 (35.08) and 1.155 (16.86), ln(16.862/35.076)/ln(1.1548/0.8660) ≈ -2.55.

At R500c the slopes barely change with redshift:

- s_n + s_T = -3.13 ± 0.17 at z = 0 and -3.24 ± 0.17 at z = 0.4987, consistent within errors.
- The density slope does not evolve significantly at any of the three radii, in line with the Simba expectation.
- The clearest shape change is the steepening of the temperature slope at 2 R500c, nominally about 3.6σ. This rests on finite differences of emulator means with independent errors and has not been checked against a smooth fit.

**Mass ratio.** T(R500)/T500 was taken as the geometric mean of the 0.866 and 1.155 R500c bins, giving 0.5916 ± 0.0047 at z = 0 and 0.5181 ± 0.0101 at z = 0.4987. The HSE mass ratio uses μ = 0.59 and the convention kT500 = G μ m_p M500/(2 R500), so that M_HSE(R500)/M500 = -(T/T500)(s_n + s_T)/2. This gives:

| Quantity | z = 0 | z = 0.4987 |
|---|---|---|
| M_HSE/M500 | 0.925 ± 0.051 | 0.840 ± 0.048 |
| b (FLAMINGO convention) | -0.075 ± 0.051 | -0.160 ± 0.048 |

The ratio between redshifts is 0.91. Because the slope sum barely changes, the larger bias at z = 0.4987 comes mainly from the 12% lower temperature at R500, not from profile shape. The absolute b values depend on the assumed T500 convention. The critic flagged two problems with this result: the significance had to be tested, and the sign convention initially differed from FLAMINGO's. Both are addressed in the next subsection.

### Pressure-profile cross-check and significance

The emulator's own pressure profile gives an independent slope s_P, compared here with s_n + s_T over the same bin pairs.

| Radius | z | s_P (CPP) | s_n + s_T | Difference |
|---|---|---|---|---|
| 0.49 R500 | 0 | -1.981 ± 0.042 | -2.133 ± 0.104 | 1.3σ |
| 0.49 R500 | 0.4987 | -1.874 ± 0.088 | -2.218 ± 0.117 | 2.4σ |
| 1.00 R500 | 0 | -3.052 ± 0.113 | -3.128 ± 0.171 | 0.37σ |
| 1.00 R500 | 0.4987 | -3.232 ± 0.154 | -3.243 ± 0.172 | 0.05σ |
| 2.05 R500 | 0 | -2.877 ± 0.042 | -4.249 ± 0.086 | 14.4σ |
| 2.05 R500 | 0.4987 | -1.815 ± 0.207 | -4.463 ± 0.125 | 10.9σ |

The routes agree at R500, so the R500 mass estimate is robust to which route is used. Beyond R500 the pressure profile is not the product of the density and temperature profiles.

With the T(R500)/T500 error propagated, the two routes give:

| Slope used | z=0 M_HSE/M500 | z=0.4987 M_HSE/M500 | Difference | Δb (FLAMINGO convention) | Significance |
|---|---|---|---|---|---|
| s_n + s_T | 0.925 ± 0.051 | 0.840 ± 0.048 | 0.085 ± 0.070 | -0.085 ± 0.070 | 1.2σ |
| s_P (CPP) | 0.903 ± 0.034 | 0.837 ± 0.043 | 0.066 ± 0.055 | -0.066 ± 0.055 | 1.2σ |

From the pressure route, b = -0.097 ± 0.034 at z = 0 and -0.163 ± 0.043 at z = 0.4987. Both routes give a bias that becomes more negative with redshift, the same direction as FLAMINGO for clusters, but neither is statistically significant.

The quoted errors treat bins and redshifts as independent. Correlated emulator errors could move the significance in either direction.

### Feedback sensitivity (incomplete)

The feedback test used kinetic AGN efficiency eps_kin, varied to the ends of its range (0.02 and 1.2) with the other parameters held at their midpoints. Choosing eps_kin was a judgement call, because the emulator does not indicate which parameter controls the slopes. CGD and CTP were predicted at both redshifts for both values.

[[FIGURE 21]]

[[FIGURE 22]]

Figures 21 (CGD) and 22 (CTP) each overlay five profiles: the midpoint (eps_kin = 0.61) at z = 0, and eps_kin = 0.02 and 1.2 at both redshifts. The slopes, T/T500 and M_HSE/M500 for these runs were not extracted. It therefore cannot yet be said whether feedback moves the bias more or less than the redshift change does. The fGas observable was not run.

### Non-thermal correction

The Nelson et al. fit was evaluated at R500c assuming R500c ≈ 0.5–0.6 R200m (about 0.5 at z = 0 and 0.55–0.6 at z = 0.5). This conversion and the evaluation were done by hand, not with a tool. The results are:

| x = r/R200m | f_nth | Correction factor 1/(1 - f_nth) |
|---|---|---|
| 0.50 | 0.254 | 1.34 |
| 0.55 | 0.274 | 1.38 |
| 0.60 | 0.294 | 1.42 |

Applying these factors to the emulator ratios gives 1.24–1.31 at z = 0 and 1.16–1.19 at z = 0.4987, an overcorrection of 16–31%.

Reconciling the emulator directly would need f_nth ≈ 1 - M_HSE/M500 ≈ 0.075 at z = 0 and 0.16 at z = 0.4987. These are closer to the X-COP value of about 6% than to the non-radiative Nelson fit. This conclusion relies on the hand-derived R500c–R200m mapping and on the assumed T500 convention, so it is low confidence and has not been independently verified.

## Discussion

**Where profile shape matters.** Profile-shape evolution between z = 0 and z ≈ 0.5 has little effect on the HSE mass reconstruction at R500c:

- The density slope is stable, as Simba (arXiv:2409.05815) predicts.
- The total slope changes by only about 0.1.
- The apparent increase in bias with redshift is carried by the temperature normalisation, T(R500)/T500.

Shape evolution does matter at 2 R500c, where the temperature slope steepens. At that radius, however, the emulated pressure profile disagrees with density times temperature by more than 10σ. Any outskirts mass reconstruction from these emulators is therefore currently unreliable. Possible causes include:

- ⟨P⟩ ≠ ⟨ρ⟩⟨T⟩ under halo-to-halo scatter or clumping.
- Different halo samples or weightings behind each emulator.
- Edge effects near the 2.74 R500c grid boundary.

The flattening of the pressure slope with redshift at 2.05 R500c, from -2.88 to -1.82, deserves caution for the same reasons.

**Comparison with FLAMINGO.** The direction of Δb matches FLAMINGO's cluster-scale trend (arXiv:2409.07849). The magnitude cannot be compared quantitatively, for three reasons:

- The halo mass behind the emulated profiles is unknown.
- The temperature weighting (mass-weighted or spectroscopic-like) is undocumented.
- The subgrid models in HACC, FLAMINGO and Simba differ.

FLAMINGO's weighting result offers one possible reconciliation. If CTP is mass-weighted, FLAMINGO would predict a bias smaller in magnitude than -0.2, compatible with the emulator's -0.075 to -0.16.

**Possible confounds.** Two effects could mimic or distort the redshift trend:

- **Selection.** If the emulator's stack uses a fixed mass threshold, the mean mass is lower at z = 0.4987, and part of the trend could be a selection effect.
- **Normalisation.** The critic noted that T(R500)/T500 ≈ 0.59 is low compared with observed universal profiles, which the critic put at roughly 0.8–0.9 at R500 for X-COP. This hints that the emulator's T500 normalisation differs from the assumed convention, which would shift every absolute b.

**Non-thermal pressure.** The non-radiative Nelson et al. fraction overcorrects the emulator masses. The implied required fraction is closer to the X-COP observation (arXiv:1805.00034). Possible explanations are:

- The emulator's convention or weighting already absorbs part of the bias.
- HACC haloes carry less non-thermal support than non-radiative ART runs.

These cannot be distinguished without the emulator documentation.

**Dead ends.**

- **Group versus cluster mass dependence.** The emulator has no mass input and returns one profile per call, so group-scale and cluster-scale profiles could not be produced. The z ≈ 1 comparison was also impossible.
- **Documentation search and X-COP benchmark.** The search for HACC mass-selection and temperature-weighting documentation, and the X-COP universal-profile slope benchmark (arXiv:1805.00042), were not attempted because the tool budget ran out. They are not intrinsically blocked.

## Limitations

**What the emulator does not provide.**

- There is no true M500c and no mass selection, so absolute biases rest on an assumed kT500 convention. Only the redshift ratio (0.91) is relatively convention-independent.
- The temperature weighting is unknown. This matters because FLAMINGO shows the bias depends strongly on weighting.
- Redshift coverage stops at z = 0.4987, so z = 1 was not tested.

**How slopes and errors were computed.**

- Slopes are finite differences of emulator means with independent-bin errors.
- No smooth-function fit (for example a Vikhlinin-type model) was tried.
- Correlated emulator errors were not modelled.
- The 3.6σ temperature-slope change and the 1.2σ bias change are therefore uncertain in significance.

**Incomplete analyses.** The feedback runs exist but were not analysed, and fGas was never predicted. No plots with uncertainty bands were made for individual predictions.

**Literature coverage.**

- The baseline rests on four papers recorded with verbatim quotes, short of the six targeted.
- The FLAMINGO numbers taken from the full text were not recorded with quotes, and its per-mass-bin b(z) values are only plotted, not tabulated.
- The merger result is from the abstract only.
- arXiv:1805.00035, arXiv:1805.00042, arXiv:1507.04338 and the Simba fit coefficients were not extracted.

**Non-thermal correction.** The R500c-to-R200m conversion used for it was assumed and computed by hand.

## Open directions

1. Extract s_n + s_T, T/T500 and M_HSE/M500 at R500c from the existing eps_kin = 0.02 and 1.2 profiles to test whether the feedback-induced shift exceeds the 0.085 redshift change.
2. Search for HACC profile documentation (halo-mass selection, T500 definition, temperature weighting) to turn the relative bias into an absolute one and to test the selection explanation.
3. Diagnose why the emulated pressure profile is much shallower than density times temperature beyond R500, and decide which is the correct input for outskirts HSE masses.
4. Refit the profiles with smooth analytic models and propagate correlated emulator errors to re-assess the significance of the temperature-slope steep
