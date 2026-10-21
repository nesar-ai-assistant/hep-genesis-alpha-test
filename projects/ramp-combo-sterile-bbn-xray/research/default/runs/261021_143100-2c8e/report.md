# Sterile-neutrino dark matter in 2024-2026: combining BBN and X-ray constraints on the (m_s, sin^2 2theta) plane

## Abstract

This investigation combined sterile-neutrino tool calculations with a reading of recent arXiv papers to ask which (m_s, sin^2 2theta) regions remain viable for keV sterile-neutrino dark matter.

**BBN.** The tool's BBN module responds only to Delta N_eff. On the non-resonant (Dodelson-Widrow, DW) relic-density line it gives Delta N_eff between 2.2e-4 and 1.6e-3. The resulting abundance shifts are negligible (|Delta chi^2| of 0.02 or less). BBN begins to exclude only at mixing angles 180-3600 times above the relic line, under every error budget tested. BBN therefore does not constrain keV sterile-neutrino dark matter through Delta N_eff. Where BBN does matter is through the lepton asymmetry that resonant production requires, and the tool does not model that effect.

**X-rays.** The tool's decay rates agree with the standard radiative formula to within about 2%. Its tabulated limits exclude DW production as all of the dark matter for m_s = 7-20 keV. The newest XRISM cluster-stack limit is sin^2 2theta below about 4-5e-10 at 7.1 keV. That does not exclude the 3.5 keV line, which implies about 7e-11.

**What survives.** For sterile neutrinos to be all of the dark matter, the literature (Vogel et al., arXiv:2507.18752) gives a resonant (Shi-Fuller) window. It requires an initial lepton asymmetry L of about 0.5 or more, m_s of about 35 keV or more, and sin^2 2theta of about 1e-14 or less. Two other cases:
- A flavor-universal asymmetry of about 1e-3 is excluded for full dark matter across 15-60 keV.
- A zero-total-asymmetry flavor configuration (arXiv:2507.20659) widens the viable mixing range, but its edges could not be quantified here.

The quantitative upper (X-ray) and lower (asymmetry) edges at 30-60 keV remain open. They exist only as plots that could not be extracted.

**Correction to the brief.** The initial survey brief stated a low-mass edge of "m_s >~ 10 keV" and said that no BBN tools were available. Both statements are wrong. The edge is about 30-37 keV, and the sterile-neutrino tools were used throughout.

## Background

**X-ray searches.** The XRISM Collaboration stacked 3.75 Ms of Resolve data on ten galaxy clusters (arXiv:2510.24560) and found no unidentified lines. For a 7.1 keV particle, its 3-sigma decay-rate limit is Gamma < 0.97e-27 s^-1. The paper also gives a mixing-angle fit, valid for line energies of 2.5-15 keV:

sin^2 2theta / 1e-10 < 4.1 (E/3.55)^-4 f1(E)

The NuSTAR Galactic Center analysis (arXiv:1609.00667) improved earlier limits by about an order of magnitude near m_s = 20 keV and implied m_s <~ 16 keV in the nuMSM. It quotes the decay-rate normalization used throughout this report:

Gamma = 1.38e-32 s^-1 (sin^2 2theta/1e-10)(m/keV)^5

**Lepton asymmetries and BBN.** Froustey and Pitrou (arXiv:2405.06509) used full three-flavor neutrino transport with BBN. They find that the space of allowed initial lepton asymmetries is "generically unbound" with current abundance and CMB data, because flavors do not fully equilibrate. A tight bound of about 1e-3 holds only for a flavor-universal asymmetry. A quantum-kinetic study of flavor equilibration (arXiv:2502.14960) supports the same picture: large flavor asymmetries can evade BBN and CMB limits.

**Resonant-production windows.**
- Vogel et al. (arXiv:2507.18752) revive Shi-Fuller production with L of order 1 above about 20 MeV. They combine NuSTAR and INTEGRAL/SPI X-ray limits with structure-formation bounds and provide fitting functions for the thermal-equivalent mass m_th and for the required L.
- Akita, Hamaguchi and Ovchynnikov (arXiv:2507.20659) assume large flavor asymmetries with zero total asymmetry, washed out by oscillations at about 15 MeV. They find that the viable mixing range grows by up to two orders of magnitude for m_s up to 60 keV, and they release a public code (sterile-dm-lfa).
- Gorbunov et al. (arXiv:2502.17374) argue that unequal flavor asymmetries soften BBN limits and give colder spectra.
- Two further papers were listed in the survey but not checked. arXiv:2402.11902 (an Affleck-Dine source for the asymmetry) was not read. arXiv:2609.31340 (saturation of resonant production at high asymmetry) was never checked against arXiv metadata, and its identifier looks implausible. Neither is relied on below.

## Results

### What the sterile-neutrino tools can and cannot compute

**BBN module.** BBN is a PRyMordial-calibrated fit for Yp, D/H and Li7. It is driven only by Delta N_eff and is valid for m_s below about 100 keV. A point is excluded at Delta chi^2 > 3.84 against two measurements:
- Yp = 0.2449 +/- 0.004 (Aver+ 2021)
- D/H = 2.547 +/- 0.025 e-5 (Cooke+ 2018)

Earlier the criterion was described as also including Planck N_eff = 2.99 +/- 0.17. A later reconstruction shows the chi^2 actually uses Yp and D/H only (see the error-budget subsection below).

**Production mechanisms.** DW production is the only mechanism the tool models reliably. Its Shi-Fuller mode accepts a lepton_asymmetry argument, but:
- Its Delta N_eff is a labelled heuristic (0.1 times the DW value).
- At m_s = 7.1 keV, sin^2 2theta = 7e-11 and L = 1e-3 it returned Omega h^2 = 432, which is unphysical.
- The asymmetry's own effect on BBN (the shift in n/p from xi_e) is not modelled.

**Shi-Fuller benchmark check.** At the 2507.18752 benchmark (m_s = 37 keV, sin^2 2theta = 1.5e-14, L = 0.1, the tool's maximum) the tool gives:
- Delta N_eff = 3.5e-8
- Yp = 0.24682 and D/H = 2.443e-5, identical to the Standard Model values
- BBN Delta chi^2 = 0
- Decay rate 1.42e-28 s^-1 at E = 18.5 keV
- Omega_s h^2 = 25.1

That relic density is about 200 times the observed dark matter. The paper's fit instead places this point at the observed density for L of about 0.7. The tool therefore cannot test the published resonant windows, either on the BBN side or on the relic-density side.

### DW scan of the (m_s, sin^2 2theta) plane

The scan covered m_s = 1-100 keV and sin^2 2theta = 1e-14 to 1e-6 on a 60x60 grid (files scan_DW_9bfc3d.npz/.csv). Of the 3600 points, 546 are BBN-excluded and 1740 overclose.

The BBN 95% upper limits on sin^2 2theta, by mass, are:

| m_s (keV) | 1 | 7 | 13 | 26 | 50 | 100 |
|---|---|---|---|---|---|---|
| BBN limit on sin^2 2theta | 3.9e-7 | 8.2e-8 | 4.4e-8 | 2.4e-8 | 1.7e-8 | 9.3e-9 |

These limits are two or more orders of magnitude weaker than the overclosure boundary.

[[FIGURE 10]]

Figure 10 shows the DW exclusion plane. The Omega h^2 = 0.12 line runs from sin^2 2theta = 2.5e-10 at 7.1 keV down to 7.6e-12 at 50 keV, with overclosure above it. The BBN-excluded region lies only above about 1e-8 to 1e-7 and so never reaches the relic line.

The tool also tabulated BBN numbers at 84 points. The precise DW relic-line points, with their BBN output, are:

| m_s (keV) | sin^2 2theta | Delta N_eff | Delta chi^2_BBN |
|---|---|---|---|
| 7.1 | 2.545e-10 | 1.6e-3 | -0.020 |
| 10 | 1.374e-10 | 1.1e-3 | -0.014 |
| 20 | 3.946e-11 | 5.6e-4 | -0.007 |
| 50 | 7.583e-12 | 2.2e-4 | -0.003 |

At 7.1 keV and sin^2 2theta = 3e-10 the tool gives Yp = 0.246840 and D/H = 2.44395e-5. Both are indistinguishable from the Standard Model baseline (Yp = 0.246815, D/H = 2.4433e-5, N_eff = 3.044).

BBN starts to exclude only far above the relic line:
- At 7.1 keV, near sin^2 2theta of about 1e-7: Delta N_eff = 0.62, Yp = 0.2549, D/H = 2.649e-5, Delta chi^2 = 5.9.
- At 50 keV, near 3e-8: Delta N_eff = 0.88, Delta chi^2 = 16.8.

A second grid at m_s = 15, 20, 30, 40 and 60 keV, with sin^2 2theta from 1e-15 to 1e-11 (45 points), found no BBN exclusion anywhere: |Delta chi^2| was at most 0.0044 and Delta N_eff at most 3.4e-4. Only the point at 60 keV with sin^2 2theta = 1e-11 overcloses under DW (Omega h^2 = 0.22).

### BBN response to N_eff and robustness of the error budget

[[FIGURE 12]]

Figure 12 shows the tool's BBN predictions as a function of N_eff only; m_s does not enter. Its key numbers:
- Standard Model baseline: Yp = 0.24682, D/H = 2.4433e-5.
- Slopes near the Standard Model: dYp/dN_eff = 0.01351 and d(D/H x 1e5)/dN_eff = 0.3308.
- One fully thermalised sterile neutrino (N_eff = 4.044): Yp = 0.2596 and D/H = 2.777e-5.
- BBN-only limit: Delta N_eff < 0.548 (95%).

**Reconstructing the tool's error budget.** The tool's numbers are reproduced only if its chi^2 uses Yp and D/H, with a D/H theory error of about 0.060e-5 added in quadrature to the observational 0.025e-5. The baseline then splits as chi^2 = 0.23 (Yp) + 2.54 (D/H) = 2.77. This reconstruction matches the tool's Delta chi^2 at three points:
- Delta chi^2 = -1.14 at Delta N_eff = 0.161
- Delta chi^2 = 5.9 at Delta N_eff = 0.62
- Delta chi^2 = -0.367 at Delta N_eff = 0.031; adding Planck N_eff to the chi^2 would give about -0.21 instead

It follows that the Standard Model D/H offset is -1.6 sigma against the tool's own error budget. The earlier figure of -4.1 sigma holds only if the observational error is used alone.

**Alternative budgets.** These are my own linearized estimates, using the grid scaling Delta N_eff = 6.18e6 sin^2 2theta at 7.1 keV and 2.95e7 sin^2 2theta at 50 keV. The 95% limits on Delta N_eff are:

| Error budget | 95% limit on Delta N_eff |
|---|---|
| Yp only | < 0.455 |
| Tool default (Yp plus D/H with theory error) | < 0.548 |
| Yp plus D/H, observational error only | < 0.61 |
| D/H only, with theory error | < 0.81 |
| Planck N_eff (extreme check) | < 0.28 |

The Planck case is an extreme check only, because a keV sterile neutrino is non-relativistic at recombination.

In mixing angle, these limits correspond to:
- sin^2 2theta < 4.5e-8 to 1.3e-7 at 7.1 keV, which is 180-510 times above the relic line;
- sin^2 2theta < 9.5e-9 to 2.8e-8 at 50 keV, which is 1250-3600 times above the relic line.

A direct tool grid agrees. At 50 keV, sin^2 2theta = 2.6e-8 gives Delta N_eff = 0.766 and is excluded, while 1e-8 is allowed. At 7.1 keV, 7.5e-8 is allowed (Delta chi^2 = 1.83).

### Lepton-asymmetry shift of Yp (estimate only)

The tool omits the shift in Yp caused by the asymmetry itself. I estimated it by hand, using Delta Yp of about -0.23 xi_e and xi of about 1.46 L. These are low-confidence numbers, because the L-to-xi conversion is convention-dependent at the factor-of-4 level.

- **Flavor-universal L = 1e-3.** Delta Yp is about -3.4e-4, or 0.08 sigma. This is negligible.
- **Threshold for a visible shift.** A 2-sigma shift in Yp needs a residual xi_e of about 0.035.
- **2507.20659 benchmark (L_e = -L_mu = 0.1).** Without equilibration, Delta Yp would be about -0.034 (about 8 sigma).
- **2507.18752 benchmark.** If its asymmetry sat in nu_e, Delta Yp would be about -0.02 to -0.05 (6-12 sigma).

Both resonant windows are therefore BBN-safe only if the residual xi_e at about 1 MeV stays below about 0.03. This is what flavor equilibration (for zero total asymmetry) or keeping the asymmetry mostly in L_mu is meant to deliver. The tool cannot check it.

### X-ray constraints

**Normalization.** The tool's decay rates follow the standard formula with a 1.36e-29 prefactor:
- On the DW relic line they are 6.25e-28 s^-1 (7.1 keV), 1.87e-27 s^-1 (10 keV), 1.72e-26 s^-1 (20 keV) and 3.23e-25 s^-1 (50 keV), within about 1.5% of the analytic values.
- At 7.1 keV with sin^2 2theta = 4e-10 the tool gives 9.82e-28 s^-1, within 2% of the XRISM limit of 0.97e-27 s^-1.
- At 20 keV with sin^2 2theta = 1e-12 it gives 4.36e-28 s^-1, against 4.42e-28 s^-1 from the NuSTAR Eq. 2.

The tool's fluxes are whole-halo values with no field-of-view cut, so only decay rates, not fluxes, can be compared with published limits.

**XRISM limits.** Evaluating the XRISM fit by hand gives the following upper limits on sin^2 2theta:

| m_s (keV) | 6 | 7.1 | 8 | 10 | 14 |
|---|---|---|---|---|---|
| XRISM limit on sin^2 2theta | about 1.3e-9 | about 4-5e-10 | about 2.3e-10 | about 5.7e-11 | about 1.2e-11 |

At 7.1 keV the two routes differ slightly: the decay-rate limit gives 3.9e-10 and the polynomial fit gives 4.8e-10. The 3.5 keV line implies a rate of about 2e-28 s^-1 (sin^2 2theta of about 7e-11), a factor of about 5 below the XRISM limit, so XRISM does not exclude the line. These XRISM numbers were not re-verified verbatim in a second pass; that attempt hit the author-list chunk of the paper. They should be treated as single-read values.

**The tool's tabulated limits** (NuSTAR M31, Roach+ 2020; XMM blank sky, Dessert+ 2020):
- They exclude the DW relic points at 7.1 and 10 keV (both limits) and at 20 keV (NuSTAR M31). DW as all of the dark matter is therefore X-ray-excluded for 7-20 keV.
- At 7.1 keV they also exclude sin^2 2theta = 4e-10, so these limits are stronger than XRISM there.
- At 15 keV, sin^2 2theta = 1e-12 is excluded.
- At 20 keV the exclusion boundary lies between 1e-13 (allowed, Gamma = 4.36e-29 s^-1) and 1e-12.

Above m_s of about 25 keV (line energies above about 10-13 keV) the tool has no tabulated limits. Nothing is flagged at 30 keV even at sin^2 2theta = 1e-11 (Gamma = 3.31e-26 s^-1), nor at 40 or 60 keV with sin^2 2theta = 1e-14. The 50 keV DW relic point is "not excluded" only because of this gap. Published NuSTAR Galactic Center, INTEGRAL and Lyman-alpha limits exclude DW dark matter at 50 keV. These high-mass tool results describe the tool's coverage, not the physics.

**NuSTAR Galactic Center.** 1609.00667 gives its sin^2 2theta limits only as curves (Figs. 7-8). Extracting those figures failed, so no numerical NuSTAR or INTEGRAL edge is available at 30-60 keV.

### Resonant-production window from the literature

The following items from 2507.18752 were checked against the full text in a second pass:
- The window opens for L >~ 0.5 (given at T = 10 GeV), m_s >~ 35 keV and sin^2 2theta <~ 1e-14.
- It is excluded at much more than 95% CL for L < 0.1.
- Structure
