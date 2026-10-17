# Baryonic suppression of the matter power spectrum: literature survey, AGN feedback physics, and weak-lensing implications (no emulator evaluation was possible)

## Abstract

The task had three parts: predict the baryonic power-spectrum ratio S(k) = P_hydro/P_DMO at z=0 for at least two feedback settings using a hydrodynamics emulator, explain the AGN-feedback physics of the suppression, and assess its impact on weak-lensing cosmology.

**The emulator part could not be done.** No emulator was available in this session, and none could be installed. No S(k) value in this report was computed by us. Every number is a published value, quoted from paper text.

**Simulation bracket at z=0.** The quoted values span:
- The weak end: Astrid shows no significant suppression; Horizon-AGN shows less than 15% at k~10 h/Mpc.
- An intermediate case: OWLS AGN shows 1% at k~0.3, 10% at k~1 and 30% at k~10 h/Mpc.
- The strong end: the FLAMINGO jet and low-gas-fraction variants resemble cosmo-OWLS with log ΔT_AGN = 8.3 to 8.5.

An X-ray-calibrated BCemu fit gives a maximum suppression of 21-28% (68% CL) at k~7 h/Mpc.

**Physical mechanism.** AGN feedback ejects gas from group-scale haloes (M ~ 1e13-1e14 Msun/h) to beyond r200m. The amplitude of the suppression is set by the mean baryon fraction of groups.

**Weak lensing.** Reconciling KiDS-1000 or DES Y3 cosmic shear with Planck ΛCDM through baryons alone requires:
- A_mod = 0.69 ± 0.06 for KiDS;
- A_mod = 0.858 ± 0.052 for DES Y3;
- a suppression that reaches down to k~0.2 h/Mpc.

This is stronger than most simulations produce. FLAMINGO concludes that baryonic effects cannot remove the S8 tension. Ignoring feedback shifts S8 by roughly 1σ in the quoted KiDS and DES analyses.

## Background

**OWLS reference.** The OWLS result of van Daalen et al. (arXiv:1104.1174) established that AGN feedback suppresses the z=0 matter power by percent-to-tens-of-percent levels over the scales probed by cosmic shear. Radiative cooling raises the power only at very small scales.

**Baryon-fraction relations.** Two papers tie the suppression to halo baryon fractions:
- van Daalen et al. 2019 (arXiv:1906.00968) used a library of 92 OWLS, cosmo-OWLS and BAHAMAS power spectra. The mean baryon fraction in groups predicts the suppression to 1% for k < 1 h/Mpc.
- SP(k) (arXiv:2305.09710) extended this to a 400-run suite. It provides a public code (pyspk).

**Parameterised and emulated models.** The baryonic correction model (arXiv:1510.06034) expresses the mechanism in parametric form:
- the ejected gas fraction sets the amplitude;
- the ejection radius sets the scale where suppression begins.

This approach underlies the BCemu emulator (arXiv:2108.08863) and the BACCO emulator (arXiv:2011.15018). The FLAMINGO project has three relevant papers:
- a Gaussian-process emulator of its response (arXiv:2410.17109);
- an S8 analysis (arXiv:2309.07959);
- a study of how feedback couples to cosmology (arXiv:2403.12967).

**Halo-mass decomposition.** Two papers split the suppression by halo mass: arXiv:2309.06479 for cosmo-OWLS/BAHAMAS and arXiv:2511.10634 for IllustrisTNG.

**Weak-suppression simulations.** Horizon-AGN (arXiv:1801.08559) and Astrid (arXiv:2605.04176) predict weak suppression.

**S8 analyses.** The weak-lensing S8 question is addressed by:
- the "non-linear solution" papers (arXiv:2206.11794, arXiv:2305.09827);
- a DES Y3 + ACT kSZ joint fit (arXiv:2404.06098);
- KiDS × tSZ (arXiv:2109.04458);
- DES Y3 harmonic-space shear (arXiv:2203.07128);
- an early forecast of the dark-energy bias from neglecting baryons (arXiv:1105.1075).

**Search conditions.** The abstract-search tool was rate-limited (HTTP 429) on all three attempts. The survey was therefore built from a second search tool, followed by full-text downloads of the core papers.

## Results

### 1. Emulator evaluation: not possible

No tool in the session could evaluate P_hydro/P_DMO:
- The input-file and dataset lists were empty.
- Dispatch was local.
- The only job tool (run_test_job) draws random samples from a normal distribution. It does not evaluate any physics.

BCemu and pyspk could not be installed. Saved paper figures could not be used as a substitute either: the figure tool stores PNGs and captions, but no tool could view or digitise images.

Consequently:
- No named weak or strong parameter point (for example a low and a high BCemu log Mc) was evaluated.
- No S(k=1) or S(k=5) value exists for any named point.
- The SP(k) relation between f_b and S was not reproduced.

### 2. Literature S(k) at z=0: the simulation bracket

All values below are published, not computed. In the table, k(1%) is the k at which suppression first reaches 1%.

| Model | Ordering | Quoted z=0 behaviour | k(1%) | S at stated k | Minimum |
|---|---|---|---|---|---|
| Astrid (arXiv:2605.04176) | weak | "no significant suppression at z = 0"; mild suppression to k~1 h/Mpc at z=0.2, with the ratio rising back above unity at z=0 | not quoted | S(k=1) about 1 or above | none below 1 quoted |
| Horizon-AGN (arXiv:1801.08559) | weak | less than 15% at k~10 h/Mpc; enhancement by a factor of a few at smaller scales; non-monotonic evolution over z=0-5 | not quoted | S(10) > 0.85 | not quoted |
| FLAMINGO fiducial (arXiv:2410.17109) | moderate | departs from unity at k~0.1 h/Mpc; minimum moves from k=6 h/Mpc (z=2) to k=10 h/Mpc (z=0) | ~0.1 h/Mpc (departure) | not quoted | k_min = 10 h/Mpc |
| OWLS AGN (arXiv:1104.1174) | intermediate (provisional) | 1% at k~0.3, 10% at k~1, 30% at k~10 h/Mpc | ~0.3 h/Mpc | S(1)~0.90, S(10)~0.70 | at or beyond 10 h/Mpc |
| FLAMINGO fgas−8σ thermal / jet | strong | "closely resemble" cosmo-OWLS log ΔT = 8.3 (thermal) and 8.5 (jet); jet response exceeds thermal at fixed fgas | not quoted | not quoted | k_min 8-10 h/Mpc for thermal fgas variants |

Further details on the strong end, from the FLAMINGO paper:
- Below fgas−8σ the thermal response "reaches a saturation value".
- Only Illustris and cosmo-OWLS ΔT = 8.7 lie beyond the emulator's reach.
- The numerical amplitudes for these strong variants appear only in the paper's Figs. 5, 6, 11 and 13, which could not be read.

Astrid results on black-hole dynamics:
- Black-hole repositioning boosts kinetic AGN feedback, by a factor of 2 at z=1.5.
- At z=0 the repositioning run lies about 10% lower than the dynamical-friction run around k = 20 h/Mpc.
- Modelling choices for black-hole dynamics therefore shift the predicted ratio substantially.

Caveat on ordering: OWLS AGN is labelled stronger than FLAMINGO fiducial, but no quoted FLAMINGO-fiducial S(k=1) or S_min supports this. Its ordering relative to Horizon-AGN is only partly constrained: 30% versus less than 15% at k~10 h/Mpc. The ranking should be treated as provisional. An earlier pass called OWLS the "strong/fiducial" reference; that label was revised to "intermediate".

### 3. X-ray-calibrated BCemu constraint

Giri and Schneider (arXiv:2108.08863, Sec. 4.2) fit the 7-parameter BCemu model to X-ray group and cluster gas fractions. The fit assumes Planck cosmology and hydrostatic bias b_hse = 0.26 ± 0.07, and the posterior sits near log10 Mc ~ 12.6. The posterior prefers low δ: a slowly falling gas profile, with much of the gas ejected beyond the virial radius.

The resulting z=0 suppression:
- **68% CL:** suppression exceeds 1% between k~0.1 and 0.4 h/Mpc. It grows to a maximum of 21-28% (S_min ~0.72-0.79) at k~7 h/Mpc. The abstract rounds this to 20-28%.
- **99% CL:** k(1%) lies at 0.1-1.3 h/Mpc. The maximum is 14-38% (S_min ~0.62-0.86) beyond k~7 h/Mpc.

How the paper places simulations against this band:
- Only cosmo-OWLS 8.5 is fully consistent.
- cosmo-OWLS 8.0, BAHAMAS and OWLS lie between the 68% and 99% regions.
- Illustris-TNG and Horizon-AGN fall outside the 99% region, because their suppression is shifted to higher k.

The OWLS-AGN 30% at k~10 h/Mpc sits at or just beyond the strong edge of the 68% band. The FLAMINGO strongest variants are stated to be in strong tension with X-ray gas fractions.

BCemu coverage:
- Parameter ranges: log10 Mc ∈ [11, 15], θ_ej ∈ [2, 8], δ ∈ [3, 11], η ∈ [0.05, 0.4], f_b ∈ [0.10, 0.25].
- Wavenumber range: k ~ 0.03-12.5 h/Mpc.
- Emulation error: below 1% at 1σ.

[[FIGURE 1]]

Figure 1 is the BCemu emulator's percentage error on S(k) for its test set at several redshifts, with 1σ and 2σ bands. It documents the stated sub-percent emulation accuracy.

[[FIGURE 2]]

Figure 2 is the paper's comparison of S = P/P_N-body from the hydrodynamical simulations with best-fit baryonification curves at three redshifts. It was saved but not read numerically.

[[FIGURE 3]]

Figure 3 is one panel of the paper's Figure 3. It compares the baryonification model, fitted only to simulated gas and stellar fractions, with the S(k) measured in cosmo-OWLS, BAHAMAS, OWLS, Illustris-TNG and Horizon-AGN. The remaining panels are registered separately as Figures 4-8 and are not repeated here.

[[FIGURE 21]]

Figure 21 is the paper's Figure 8: the constraints on f_gas, f_star and S(k) from the X-ray observations. It is the figure behind the 21-28% band. No values were read from it; the numbers above come from the text.

### 4. Physics of the suppression

The physical picture rests on abstract-level and introductory quotes from the papers below. The critic noted that the stored evidence excerpts for these items show only file headers, so they are not independently verified at the verbatim level.

**Gas ejection.** Feedback heats gas and ejects it to large distances, which is needed to match X-ray groups (arXiv:1906.00968). In haloes with M500c ≳ 1e13 Msun/h, AGN feedback moves matter from inside r500c to r200m and possibly beyond (arXiv:2309.06479).

**Halo-mass dependence.**
- For k ≲ 3 h/Mpc, group-sized haloes (1e14±0.25 Msun/h) dominate the power spectrum. At smaller scales, the combined contribution of lower-mass haloes takes over.
- A lower AGN heating temperature damps the effect at k ≳ 4 h/Mpc for M500c ≥ 1e13.25 (arXiv:2309.06479).
- In IllustrisTNG, haloes with log M200m in [13, 14] are reported to dominate at k~2-30 h/Mpc (arXiv:2511.10634). This comes from the survey stage only; the full text was not read.

**Baryon fraction as the controlling variable.**
- The mean group baryon fraction alone predicts the z=0 suppression to 1% for k < 1 h/Mpc. Differences in group baryon fraction explain why simulations disagree (arXiv:1906.00968).
- A parameter-free model built on halo baryon fractions is accurate to the percent level down to k~10 h/Mpc (arXiv:2309.06479).

**Cooling.** Radiative cooling dominates only for k ≳ 70 h/Mpc in OWLS (arXiv:1104.1174). Horizon-AGN shows an enhancement of a factor of a few at scales smaller than k~10 h/Mpc (arXiv:1801.08559).

**Cosmology coupling.** Feedback strength depends on cosmology through f_b/(Ω_m σ8)^(1/4), which yields an accurate fitting formula. Combined baryonic and non-baryonic suppression (neutrinos, decaying dark matter) exceeds the sum of the two (arXiv:2403.12967).

The SP(k) figures shown below were saved but not read. The SP(k) full text was not read. No SP(k) result is drawn from them here.

[[FIGURE 23]]

Figure 23 is the SP(k) fractional baryonic impact on total matter power for all 400 models at z=0.125, colour-coded by the total baryon fraction of haloes of M200c = 1e14 Msun. It is the relation the task asked to reproduce.

[[FIGURE 25]]

Figure 25 is the SP(k) parameterisation of suppression as a function of the scaled baryon fraction (their Eq. 4), with the scale and redshift dependence of the fit parameters λ, μ and ν. These published coefficients are what a by-hand evaluation of SP(k) would use.

[[FIGURE 26]]

Figure 26 compares the SP(k) model with simulations for 8 randomly selected runs.

### 5. Impact on weak-lensing cosmology

**Required suppression in the A_mod model.** Amon and Efstathiou (arXiv:2206.11794) model the power spectrum as P = P_L + A_mod(P_NL − P_L).

For KiDS-1000, with the cosmology fixed to Planck TTTEEE ΛCDM, the ξ± fit gives "a mean Amod = 0.69 ± 0.06", with χ²_min = 265.5 for 225 data points. The authors note that this error is underestimated because it neglects the Planck cosmology uncertainty.

The same fit done with HMCode2020 needs Θ_AGN = 9.17 (+0.2, −0.8). This is well outside the BAHAMAS-calibrated range of 7.6-8.0. The paper calls the required suppression "more extreme than predicted by most of the hydrodynamic simulations".

The tension being addressed, against Planck S8 = 0.829 ± 0.012:
- KiDS shear S8 = 0.759 (+0.024, −0.021): about 9% (2.4-2.7σ) low.
- DES Y3 shear S8 = 0.772 (+0.018, −0.017): about 7% (2.3-2.6σ) low.

**DES Y3 refit.** Preston, Amon and Efstathiou (arXiv:2305.09827) give, with a Planck prior:

| Data | Scale cuts | A_mod | Significance |
|---|---|---|---|
| DES Y3 | none | 0.858 ± 0.052 | 2.7σ from 1 |
| KiDS, same prior | — | 0.748 ± 0.072 | — |
| DES Y3 + KiDS (naive combination) | — | 0.820 ± 0.042 | suppression required at about 4σ |

For comparison, BAHAMAS with log ΔT_heat = 8.0 "is well approximated by Amod = 0.9" for k ≲ 1 h/Mpc. The data require more suppression than that, closer to the C-OWLS 8.5/8.7 runs, and it must extend to k~0.2 h/Mpc. The paper names non-standard dark matter as an alternative explanation.

**S8 shift when feedback is ignored.**
- KiDS (arXiv:2206.11794, Table 1): S8 = 0.755 ± 0.016 with no feedback, against 0.774 ± 0.021 with the fiducial Θ_AGN 7.3-8.3 prior. The shift is about 0.02, roughly 1σ.
- DES Y3 (arXiv:2305.09827, Table 2):
  - All scales, no feedback: S8 = 0.793 ± 0.012, which is 1.8σ below Planck (0.828 ± 0.016).
  - With scale cuts: 0.805 ± 0.017, which is 0.9σ below Planck.
  - With A_mod and free cosmology: 0.831 ± 0.036.

  The DES difference of about 0.04 compares fits that differ in both the model and the treatment of cosmological freedom. It should therefore be read as an upper-bound-style estimate, not a controlled shift.

**FLAMINGO verdict (arXiv:2309.07959).** FLAMINGO compares its full suite, including extreme variants, with cosmic shear, CMB lensing, tSZ and their cross-spectra. Its conclusions:
- Baryonic effects are not large enough to remove the S8 tension.
- Current shear data are only marginally sensitive to baryons.
- Stronger feedback improves the fit to KiDS/DES in the D3A cosmology only slightly, and this preference largely disappears once a lower S8 is adopted.
- CMB lensing agrees well with Planck ΛCDM.
- The strongest tension comes from tSZ y-y, then shear × tSZ, then shear-shear.

This conclusion rests on abstract-level reading plus a body excerpt about the ordering of tensions. No verbatim conclusion quote was captured.

A companion FLAMINGO statement (arXiv:2410.17109) supports this. The Amon and Efstathiou response, and to a lesser extent the Preston et al. response, "are out of reach of our emulator and likely of what can be achieved using the FLAMINGO model without altering the sub-grid models".

**WL + kSZ (arXiv:2404.06098).** The DES Y3 WL + ACT DR5 kSZ fit uses BCEmu baryonification. Results:
- S8 = 0.823 (+0.019, −0.020), higher than WL alone.
- The fit prefers a mean feedback scenario more extreme than most simulations.
- The baryon fraction at M500 ~ 1e13
