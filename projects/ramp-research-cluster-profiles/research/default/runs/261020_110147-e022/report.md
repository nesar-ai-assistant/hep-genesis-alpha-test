# Shape evolution of emulated cluster gas profiles and its effect on hydrostatic mass bias, z = 0 to z = 0.5

## Abstract

We surveyed recent work on hydrostatic-equilibrium (HSE) mass bias in galaxy clusters. We then used the HACC hydrodynamics emulator to predict scaled gas-density (CGD) and temperature (CTP) profiles at z = 0 and z = 0.4987. The task asked for z = 1, but the emulator's CGD and CTP profiles only run to z = 0.4987.

Because the profiles are already scaled, any difference between the two redshifts is shape evolution alone. Using finite-difference slopes across the bins either side of R500, the thermal-only HSE mass at fixed true mass is:

| | z = 0 | z = 0.4987 |
|---|---|---|
| M_HSE,500c/M500 | 0.925 | 0.840 |
| b_HSE (FLAMINGO sign convention) | -0.075 | -0.160 |

The shape-only shift in M_HSE,500c is -9.2%. Its significance lies between 1.3 sigma and 4.3 sigma, depending on the unknown correlation of emulator errors between bins. The shift is driven by a 12.4% drop in scaled temperature at R500, partly offset by a 3.7% steepening of the slope sum. Its sign matches FLAMINGO's cluster-scale trend.

The redshift drop in scaled temperature is robust to the kinetic-AGN parameters. The resulting mass shift, however, is of the same size as the kinetic-AGN spread. A Nelson et al. non-thermal pressure correction overcorrects the masses, and its redshift dependence comes entirely from an assumed radius conversion.

All derived quantities were computed by hand from tool-returned emulator values, not by a script. The absolute bias values also depend on an unconfirmed T500 convention.

## Background

**Size and trends of the bias in simulations.** FLAMINGO (arXiv:2409.07849) defines b_HSE = (M_HSE,500c - M500c)/M500c. It finds a median b_HSE of about -0.1 for groups and about -0.2 for clusters. The scatter is smallest, about 0.1, at M500c ~ 1e14 Msun. The paper also states: "At a fixed true mass, the hydrostatic masses increase (decrease) with redshift on group (cluster) scales, and the scatter increases". The bias is insensitive to the analytic profile form but sensitive to goodness of fit and to feedback strength. The verbatim quote on the redshift trend is stored in the bibliography. The -0.1/-0.2 amplitudes come from the abstract and have no verbatim quote.

**Methods.** Lau, Nagai and Nelson (arXiv:1306.3993) show that the summation and averaging (Euler/Jeans) methods of computing the bias are equivalent. The gas-acceleration term is small in the interior but not negligible in the outskirts of massive, accreting clusters.

**Non-thermal pressure.** Nelson, Lau and Nagai (arXiv:1404.4636) is the only paper read in full text. It gives a redshift-universal fit for the non-thermal pressure fraction:

f_nth = P_rand/P_tot = 1 - A{1 + exp[-((r/r200m)/B)^gamma]}

- Parameters: A = 0.452 +/- 0.001, B = 0.841 +/- 0.008, gamma = 1.628 +/- 0.019.
- Accuracy: about 10% over 0.1-1.5 r200m, valid out to z = 1.5.
- Behaviour: f_nth is about 10% in the core and about 50% near r200m. There is no systematic mass dependence for M200m >= 6e14 Msun/h. Rapidly accreting clusters lie 5-15% higher.
- The redshift dependence seen with r200c scaling "has completely disappeared" when radius is scaled by r200m.

Other papers in the survey brief were not read and are cited here only as the brief's pointers: arXiv:1308.6589, arXiv:1112.3659, arXiv:2511.10730 and arXiv:1507.04338 on merger and non-thermal origins of the bias; arXiv:1411.5361 on accretion-driven steepening of outskirt slopes.

**Observations.**
- X-COP (arXiv:1805.00034, abstract only) finds median f_nth of about 6% at R500 and about 10% at R200, with 1-b = 0.85 +/- 0.05 for Planck SZ masses. It excludes the B of about 0.6 required by CMB plus cluster counts. Its verbatim quote is "We find that hydrostatic masses require little correction".
- Wicker et al. (arXiv:2204.12823) find 3.8 sigma evidence for a redshift-dependent B under a Planck Omega_m prior. The trend is sample-dependent and degenerate with Omega_m, and the amplitude is B of about 0.8.
- SPT (arXiv:1404.6250) finds that clusters at 0.6 < z < 1.2 are "slightly (~40%) cooler" in scaled temperature, both inside 0.1 R500 and beyond R500, than clusters at 0.3 < z < 0.6. Pressure evolves little outside the core.

## Results

### Emulator configuration

The CGD and CTP outputs are already scaled: rho_gas/rho_crit(z) and T/T500. They are given on 19 log-spaced bins in r/R500c from 0.0154 to 2.74, with log spacing dln r = 0.2878. Each bin has a GP mean and standard deviation (y_std).

The emulator has seven inputs:
- Five subgrid parameters, all described by the tool as AGN controls:
  - wind: kappa_w (2-4), e_w (0.2-1);
  - black-hole seed mass: M_seed (0.6-2, in units of 10^6 Msun);
  - kinetic feedback: v_kin (0.1-1.2, in units of 10^4 km/s), eps_kin (0.02-1.2, in units of 10).
- Two cosmology parameters: omega_m and sigma_8.

Halo mass is not an input. There is no separate stellar or SN feedback parameter. The tool reports neither the halo mass selection nor the T500 definition.

The fiducial run uses kappa_w = 3, e_w = 0.6, M_seed = 1.3, v_kin = 0.65, eps_kin = 0.61, omega_m = 0.1375 and sigma_8 = 0.8. One check could not be made: the critic noted that the tool excerpts shown display only the stellar mass function's redshift list, which extends to about z = 1.75. The z = 0.4987 ceiling for CGD and CTP is therefore not directly visible in the quoted output.

The prediction files are in `runs/261020_110147/` under the project directory, named `C{GD,TP}_z{0.0000,0.4987}_prediction.csv`.

### Profile comparison between redshifts

[[FIGURE 6]]

Figure 6 compares the fiducial scaled gas density at z = 0 and z = 0.4987. The two agree within about 2% over 0.2-0.9 R500. At 1.54 R500 the density is about 13% lower at z = 0.4987, so the outskirts are steeper at higher redshift.

[[FIGURE 7]]

Figure 7 compares the fiducial scaled temperature. It is lower at z = 0.4987 at all radii above 0.03 R500: by 12% at R500 and by 30% at 2.7 R500.

The GP uncertainty is much larger at z = 0.4987 in the inner density bins: y_std/mean is about 0.68 at z = 0.4987 against about 0.12 at z = 0 in the innermost bin.

### Logarithmic slopes and HSE mass

Slopes are finite differences in ln y versus ln r. The HSE mass is

M_HSE(<x R500)/M500 = -(x t/2)(s_n + s_T)

where t = T/T500 and s_n, s_T are the density and temperature slopes. This assumes kT500 = G mu m_p M500/(2 R500) with mu = 0.59, and it treats the density slope as the n slope (constant mu).

All four fiducial files were read in full. The numbers below were then recomputed by hand from those values.

| r/R500 | Bins used | z | dln rho/dln r | dln T/dln r | t | M_HSE/M500 |
|---|---|---|---|---|---|---|
| 0.487 | central, 0.365-0.649 | 0 | -1.863 | -0.271 | – | 0.408 |
| 0.487 | central, 0.365-0.649 | 0.4987 | -1.872 | -0.345 | – | 0.382 |
| 1.000 | 0.866-1.155 | 0 | -2.545 | -0.583 | 0.592 | 0.925 |
| 1.000 | 0.866-1.155 | 0.4987 | -2.738 | -0.505 | 0.518 | 0.840 |
| 1.54 (taken as R200) | central, 1.155-2.054 | 0 | -2.929 | -0.912 | 0.430 | 1.272 |
| 1.54 (taken as R200) | central, 1.155-2.054 | 0.4987 | -3.097 | -1.072 | 0.380 | 1.221 |

An earlier value of -1.98 for the density slope "at 0.5 R500" was a one-sided difference over the 0.487-0.649 pair. It therefore measures the slope at 0.562 R500. The 0.365-0.487 pair gives -1.745. With the bin pair stated, the discrepancy is resolved.

The density slope steepens with redshift at R500 and beyond. At R500 the temperature slope flattens with redshift, while at 1.54 R500 it steepens.

Treating 1.54 R500 as R200 assumes an NFW profile with concentration about 4.

### Implied bias, shape-only shift and error bracket

If the true mass is taken as M500, the uncorrected bias is b_HSE = -0.075 at z = 0 and -0.160 at z = 0.4987. These absolute values depend on the T500 convention. The ratio between redshifts depends only on self-similar T500 scaling at fixed M500, because the profiles are already scaled.

The shape-only change is M_HSE,500c(z = 0.4987)/M_HSE,500c(z = 0) - 1 = -9.2%. It breaks down as:
- the scaled temperature at R500 falls from 0.592 to 0.518 (-12.4%);
- the slope sum steepens from -3.128 to -3.243 (+3.7%).

The errors come from linear propagation of the GP y_std, bracketed two ways:

| Assumption about adjacent bins | M_HSE/M500, z = 0 | M_HSE/M500, z = 0.4987 | Error on the -9.2% shift | Significance |
|---|---|---|---|---|
| Independent (upper bound) | 0.925 +/- 0.049 | 0.840 +/- 0.047 | +/- 7.0% | 1.3 sigma |
| Fully correlated (lower bound) | 0.925 +/- 0.010 | 0.840 +/- 0.018 | +/- 2.1% | 4.3 sigma |

Under the independent-bin assumption, the R500 slope errors are:
- z = 0: +/- 0.155 (density) and +/- 0.055 (temperature);
- z = 0.4987: +/- 0.100 and +/- 0.135.

The true GP covariance between bins is unknown, so the true significance lies inside this bracket.

An earlier error of +/- 0.15 M500 (+/- 0.3 in units of k_B T500 R500/(G mu m_p)) overstated the uncertainty. The independent-bin value is +/- 0.05 M500 (+/- 0.10 in those units).

### Kinetic-AGN feedback robustness

The CTP predictions were read at the kinetic-AGN extremes, with all other parameters at fiducial values:

| Variant | z | t(R500) | dln T/dln r |
|---|---|---|---|
| AGN-min (v_kin = 0.1, eps_kin = 0.02) | 0 | 0.565 | -0.617 |
| AGN-min | 0.4987 | 0.490 | -0.589 |
| AGN-max (v_kin = 1.2, eps_kin = 1.2) | 0 | 0.600 | -0.573 |
| AGN-max | 0.4987 | 0.526 | -0.621 |

At fixed redshift:
- The AGN spread in t(R500) is 6.0% at z = 0 and 7.1% at z = 0.4987. The GP y_std on t(R500) is about 1% at z = 0 and 2-3% at z = 0.4987, so this spread is about 4 sigma and about 2 sigma respectively.
- The spread in temperature slope is only 0.03-0.04, and its sign reverses between the two redshifts.

The redshift change in ln t(R500) is -0.144 for AGN-min and -0.132 for AGN-max, against -0.134 for the fiducial run. This is about twice the AGN spread at fixed redshift (0.060 and 0.071 in ln t). The scaled-temperature cooling with redshift is therefore robust to kinetic-AGN feedback.

The mass comparison is weaker. It was contested by the critic because the variant density profiles were not read: the density slope was held at the fiducial values of -2.54 (z = 0) and -2.74 (z = 0.4987) for both variants.
- On that basis, the shape-only shift in ln M_HSE,500c is -9.0% for AGN-min and -5.6% for AGN-max.
- The AGN-max minus AGN-min difference at fixed redshift is +4.6% at z = 0 and +8.1% at z = 0.4987.
- To first order, the M_HSE redshift shift is the same size as the kinetic-AGN spread and cannot be cleanly separated from it.

### Non-thermal pressure correction

The Nelson et al. (arXiv:1404.4636) f_nth was applied with P_tot = P_th/(1 - f_nth), giving

M_tot/M500 = (t/2)/(1-f) * [-(s_n+s_T) + dln(1-f)/dln r].

Converting R500c to r200m required assumptions not supplied by the emulator: an NFW profile with c200c = 4 and Omega_m = 0.3. These give R500c = 0.652 R200c and R200m/R500c = 2.60 at z = 0 and 1.94 at z = 0.4987.

| | z = 0 | z = 0.4987 |
|---|---|---|
| f_nth at R500 | 0.207 | 0.260 |
| dln(1-f)/dln r | -0.196 | -0.285 |
| M_tot/M500 | 1.093 | 1.035 |
| Corrected b_HSE | +0.09 | +0.035 |
| Correction factor M_tot/M_th | 1.18 | 1.23 |

The correction overshoots: the corrected masses exceed M500. The implied f_nth of 21-26% at R500 is well above the X-COP median of about 6%. The corrected redshift shift is -5.3%. If R200m/R500c is held at 2.60 at both redshifts, the shift stays at -9.2%. The redshift dependence of the correction therefore comes entirely from the assumed radius conversion.

## Discussion

The main result is that profile shape alone, at fixed scaled normalisation, lowers the thermal HSE mass at R500 by about 9% between z = 0 and z = 0.5. The effect enters mainly through the lower scaled temperature at R500, rather than through the logarithmic slopes. The slopes do steepen in the outskirts at higher redshift. This is qualitatively what arXiv:1411.5361 attributes to higher accretion rates, but here it only partly offsets the temperature drop.

**Agreement with FLAMINGO.** The emulated mass decreases with redshift, matching the sign of FLAMINGO's cluster-scale trend. The uncorrected z = 0.4987 bias of -0.16 is close to FLAMINGO's cluster median of about -0.2, and the z = 0 value of -0.075 is closer to its group value of about -0.1. The emulator's mass bin is unknown, however, so it cannot be placed on FLAMINGO's group or cluster scale. The absolute bias values also depend on the unconfirmed T500 convention. FLAMINGO's sensitivity to feedback is mirrored here: the kinetic-AGN spread in M_HSE is comparable to the redshift shift.

**Comparison with SPT.** The emulated cooling of 12% at R500 and 30% at 2.7 R500 points the same way as SPT's roughly 40% cooler high-redshift clusters. The redshift ranges do not overlap, so the comparison is only qualitative.

**Non-thermal correction.** Adding the Nelson f_nth moves the bias from negative to positive, which suggests the correction is too strong for this emulator. The critic noted two caveats:
- the Nelson sample is restricted to massive clusters (M200m >= 6e14 Msun/h) and uses a random-gas-motion definition;
- the fixed-concentration radius conversion ignores the decline of concentration with redshift and does not use the emulator's own cosmology.

An X-COP-calibrated f_nth (arXiv:2112.07554 or arXiv:1805.00034) should be tested before concluding that the correction overcorrects. The emulated profiles are thermal-only, so the uncorrected bias reflects shape effects and the mass convention, not non-thermal support.

**Dead ends.**
- Halo-mass dependence (groups versus clusters) cannot be tested, because mass is not an emulator input and the profiles are stacked in r/R500 for one fixed selection.
- The table loader failed on the CSV header row "x,y_mean,y_std" ("could not convert string 'x' to float64"). This forced plain-text reads and hand arithmetic.
- Citing the numerical benchmarks verbatim and comparing with X-COP profiles were blocked when the budget ran out. The bibliography has no verbatim quotes for FLAMINGO -0.1/-0.2, X-COP f_nth 6% and 1-b = 0.85, or the Planck B values. No X-COP profile values were ever quoted.

## Limitations

- **No scripted arithmetic.** Every slope, mass and error was computed by hand from tool-returned bin values. The critic also noted that the excerpts recorded in evidence stop at the 0.0866 R500 bin, so the outer-bin values used were read but are not reproduced in the quoted output.
- **Unknown bin covariance.** The GP covariance between bins is unknown, so the significance of the -9.2% shift is bracketed (1.3-4.3 sigma) rather than measured. A Monte Carlo would need a Python tool.
- **Unconfirmed emulator conventions.** The T500 definition, the temperature weighting and the halo mass selection were not confirmed. This affects all absolute b_HSE values.
- **Assumed radii.** R200 was taken as 1.54 R500, and the R200m/R500c conversion assumed c200c = 4 and Omega_m = 0.3.
- **Incomplete feedback test.**
  - The wind variants were generated but never read; they were the stand-in for SN feedback, which the emulator does not parametrise separately.
  - The kinetic-AGN density profiles were not read, so the AGN mass comparison holds the density slope fixed.
  - M_seed was not varied.
  - No feedback comparison plots were made.
- **No fit-based comparison.** No analytic-form fits (Vikhlinin density, generalized temperature model) and no fitted-versus-direct-gradient comparison were done. The tools cannot do nonlinear fitting.
- **Thin literature coverage.** Only arXiv:1404.4636 was read in full; the other five cited papers are abstract-only. The 2023-2025 search, including arXiv:2511.10730, was not run. arXiv:1805.00035, arXiv:1308.6589, arXiv:1411.5361 and arXiv:1507.04338 were not read. No paper figures were extracted.
- **Redshift range.** The high-redshift point is z = 0.4987, not z = 1.

## Open directions

1. Script the slope and HSE-mass calculation with Monte Carlo sampling of the GP profiles, or the GP covariance if available, to pin down the significance of the -9.2% shape-only shift.
2. Read the existing wind-variant and kinetic-AGN CGD files to complete the feedback test with real density slopes, and compare the feedback spread in M_HSE with the redshift shift at both redshifts.
3. Establish the emulator's T500 definition, temperature weighting and halo mass selection from the HACC emulator documentation, so that absolute b_HSE values can be compared with FLAMINGO's group and cluster medians.
4. Redo the non-thermal correction with a redshift-dependent concentration and the emulator cosmology, and compare it against an X-COP-calibrated f_nth (arXiv:2112.07554, arXiv:1805.00034).
5. Compare finite-difference slopes with slopes from analytic-profile fits or wider-baseline smoothed slopes, to test FLAMINGO's goodness-of-fit sensitivity and the method dependence in arXiv:1306.3993.
6. Read FLAMINGO in full text to verify the bias amplitudes and the redshift trend for the matching mass range, and add arXiv:2511.10730, arXiv:1411.5361 and arXiv:1805.00035 with verbatim quotes.

```json
{"open_directions": [
{"direction_id": "new", "goal": "Script the slope and HSE-mass calculation with Mon
