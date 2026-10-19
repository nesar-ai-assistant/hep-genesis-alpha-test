# Lyman-alpha forest limits on warm dark matter and what they imply for non-resonant (Dodelson-Widrow) sterile neutrinos

## Abstract

This report collects recent Lyman-alpha forest lower limits on the thermal-relic warm dark matter (WDM) mass and checks them against the papers. It converts those limits to non-resonantly produced (Dodelson-Widrow, DW) sterile-neutrino masses and compares the result with DW production yields and X-ray decay limits.

**Lyman-alpha limits.** The verified 95% CL (2 sigma) limits run from m_x > 3.1 keV (Villasenor+2022) to m_x > 5.7 keV (Irsic+2023). Choices of IGM thermal history and k_max weaken them to 3.5–4.1 keV.

**Mass mapping.** The Viel+2005 relation was checked against its text and maps these limits to m_s(DW) ≈ 20–45 keV. An alternative Bozek-type relation, whose source was not confirmed, gives 17–37 keV.

**Production yields.** A sterile-neutrino production server was available and was used to compute DW relic densities and fractions. Its yield normalization disagrees with the Abazajian 2005 fit by a factor of 10–16 in relic mixing angle. The server-based fractions are therefore overstated by 1.5–2 orders of magnitude.

**X-ray side.** The server's tabulated X-ray limits exclude pure DW dark matter at 7.1 and 20 keV and have no coverage at 29–46 keV. The text of the NuSTAR Galactic Center analysis (Perez+2017) implies exclusion above about 16 keV. This conclusion is reached by inference from the paper's wording, without numerical mixing-angle limits.

**Overall.** Pure DW sterile neutrinos as all of the dark matter appear excluded: Lyman-alpha forces m_s ≳ 17–20 keV, and X-ray data exclude DW above about 16 keV. The quantitative X-ray-allowed fraction could not be tabulated.

## Background

### Thermal-relic limits from the Lyman-alpha flux power spectrum

Flux-power-spectrum analyses constrain the free-streaming of WDM, usually quoted as a lower limit on the mass m_x of a thermal relic. The papers covered here are:

- **Viel+2013** (arXiv:1306.2314): m_x > 3.3 keV (2 sigma) from HIRES/MIKE spectra at z > 4.
- **Irsic+2017** (arXiv:1702.01764): combines XQ-100 with HIRES/MIKE.
- **Palanque-Delabrouille+2019** (arXiv:1911.09073): uses SDSS DR14 BOSS/eBOSS together with XQ-100.
- **Villasenor+2022** (arXiv:2209.14220): an independent suite of 1080 Cholla simulations applied to the Boera+2019 data.
- **Irsic+2023** (arXiv:2309.04533): pushes to smaller scales with HIRES/UVES data at z = 4.2–5.0.

### From thermal-relic mass to sterile-neutrino mass

For non-resonantly produced sterile neutrinos, the standard mapping from m_x to m_s comes from Viel+2005 (arXiv:astro-ph/0501562). It assumes the DW momentum spectrum is a rescaled Fermi-Dirac distribution.

Two papers provide alternatives to that mapping:

- **Boyarsky+2009** (arXiv:0812.0010) give Lyman-alpha bounds for mixed cold-plus-warm models, expressed directly in non-resonant-production (NRP) masses.
- **Rogers & Peiris** (arXiv:2007.13751) give an emulator framework that applies Lyman-alpha bounds to arbitrary transfer functions without going through the thermal-relic mapping.

### Production and X-ray constraints

On the production side, the following papers were consulted:

- **Abazajian 2005** (arXiv:astro-ph/0511630) provides a fitting formula for the DW yield that includes the QCD transition.
- **Asaka, Laine & Shaposhnikov** (arXiv:hep-ph/0612182) find moderately different yields.
- **arXiv:1512.05369** states that DW production cannot meet the relic abundance and the structure-formation bounds at the same time.
- The reviews arXiv:1702.08430 and arXiv:1705.01837, and arXiv:2006.09553 on thermalization, are relevant background but were not read.

On the X-ray side, NuSTAR Galactic Center observations (Perez+2017, arXiv:1609.00667) give, by the abstract's own description, the strongest line limits over most of the 10–50 keV mass range. They improve earlier limits by up to about 10x at some masses.

### A note on the survey brief

The brief stated that no sterile-neutrino production tools were available. In fact a sterile-neutrino server was reachable and was used. It provides DW relic density, Delta N_eff, BBN, X-ray line and free-streaming outputs.

## Results

### Verified Lyman-alpha thermal-relic limits

The limits below were checked against paper text where full text was read (Irsic+2017, Irsic+2023) and against arXiv abstracts otherwise (Viel+2013, Palanque-Delabrouille+2019, Villasenor+2022).

| Analysis | Data | m_x limit | Systematic variation |
|---|---|---|---|
| Viel+2013 (1306.2314) | HIRES/MIKE, z > 4 | > 3.3 keV (2 sigma) | 1, 2, 2.5 keV disfavoured at about 9, 4, 3 sigma |
| Irsic+2017 (1702.01764) | XQ-100 alone / HIRES/MIKE alone / combined | 1.4 / 4.1 / 5.3 keV (2 sigma) | Combined limit falls to 3.5 keV if temperature jumps of up to 5000 K are allowed |
| Palanque-Delabrouille+2019 (1911.09073) | SDSS DR14 z < 4.5 + XQ-100 | > 5.3 keV (95% CL) | — |
| Villasenor+2022 (2209.14220) | 1080 Cholla runs, Boera+2019 data, z = 4.0–5.2 | > 3.1 keV (95% CL) | Likelihood peaks at 4.5 keV; flux-power suppression saturates at k ≳ 0.1 s/km because of peculiar-velocity smearing |
| Irsic+2023 (2309.04533) | HIRES/UVES, z = 4.2–5.0, k_max = 0.2 s/km | > 5.7 keV (95% CL) | 4.1 keV for k_max < 0.1 s/km with earlier thermal priors; peculiar velocities and inhomogeneous reionization are the main small-scale systematics |

The spread among the recent limits (3.1 to 5.7 keV) is comparable to the shifts from thermal-history and k_max choices (5.3 to 3.5 keV, and 5.7 to 4.1 keV). The modelling of small scales is therefore the dominant uncertainty.

Three searches for post-2023 limits found nothing: one query targeting DESI, and two targeting the one-dimensional flux power spectrum (P1D), eBOSS and emulator re-analyses. All returned only DESI BAO papers or unrelated results.

### Mapping thermal-relic limits to DW sterile-neutrino masses

**The Viel+2005 relation.** Eq. 5 of Viel+2005, read in the paper text, is

m_s(DW) = 4.43 keV (m_x/1 keV)^{4/3} (0.25·0.7²/omega_x)^{1/3},

normalized at omega_x = 0.1225. The paper describes the correspondence as one-to-one when the transfer functions match.

The 4.46 keV prefactor quoted in the survey brief does not appear in the paper. It equals 4.43 keV rescaled to omega_dm = 0.12, since 4.43 × (0.1225/0.12)^{1/3} = 4.461 keV. The brief's range of 20–46 keV holds to within 0.6 keV.

**Comparison with a Bozek-type relation.** The table also gives a Bozek+2016-type relation, 3.9 keV (m_x/keV)^{1.294}. Its coefficients came from the planning notes and could not be confirmed in any paper text: a targeted abstract search found nothing, and the Rogers & Peiris abstract quotes no such relation. All conversions below are hand arithmetic, not tool output. The critic marked the two-relation comparison as contested.

| m_x (keV) | Viel+2005, omega = 0.1225 (keV) | Viel+2005, omega = 0.12 (keV) | Bozek-type, unverified (keV) |
|---|---|---|---|
| 3.1 | 20.0 | 20.2 | 16.9 |
| 3.3 | 21.8 | 21.9 | 18.3 |
| 3.5 | 23.5 | 23.7 | 19.7 |
| 4.1 | 29.1 | 29.3 | 24.2 |
| 4.5 (Villasenor peak) | 32.9 | 33.1 | — |
| 5.3 | 40.9 | 41.2 | 33.8 |
| 5.7 | 45.1 | 45.4 | 37.1 |

The alternative relation lowers the DW-equivalent masses by 3.1–8.0 keV, moving the range from 20–45 keV to 17–37 keV.

**Papers that quote NRP masses directly.** Of the abstracts checked, only Boyarsky+2009 does so: m_NRP > 8 keV (99.7%, frequentist) and > 12.1 keV (Bayesian 95%). Inverting Viel+2005 by hand, these correspond to m_x ≈ 1.56 and 2.12 keV, which is weaker than the modern limits.

The Irsic+2017 and Palanque-Delabrouille+2019 abstracts quote only thermal-relic masses. Their DW-equivalent values therefore rest entirely on a mapping relation. It was not checked whether Villasenor+2022 or Viel+2013 quote their own NRP masses.

### DW production on the sterile-neutrino server

**Scans run.** Several separate runs were made on the server:

- A 15-mass × 13-mixing DW grid spanning 1–50 keV and sin²2θ = 1e-13 to 1e-7 (file `sterile_nu_grid_DW_8d35ed.csv`).
- A follow-up grid at 22, 29, 41, 46 and 50 keV with sin²2θ = 1e-12 and 1e-11 (`sterile_nu_grid_DW_10ad91.csv`).
- A five-point run on the derived relic curve at 7.1, 20, 29, 41 and 46 keV (`sterile_nu_grid_DW_e67bfc.csv`).
- An 80 × 80 scan, described with Figure 10 below.

**Relic curve.** On this server, Omega_s h² is exactly linear in sin²2θ and grows roughly as m_s^1.8. Setting Omega_s h² = 0.12 gives the server's DW relic curve:

| m_s (keV) | 1 | 2 | 3 | 5 | 7.1 | 10 | 15 | 20 | 22 | 29 | 41 | 46 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sin²2θ (relic, server) | 8.7e-9 | 2.5e-9 | 1.2e-9 | 4.8e-10 | 2.5e-10 | 1.4e-10 | 6.6e-11 | 3.9e-11 | 3.3e-11 | 2.0e-11 | 1.08e-11 | 8.8e-12 | 7.6e-12 |

**Points on the relic curve.** The five-point run used sin²2θ = 2.545e-10, 3.946e-11, 2.022e-11, 1.084e-11 and 8.81e-12 at m_s = 7.1, 20, 29, 41 and 46 keV. The radiative lifetimes are 1.6e27, 5.82e25, 1.77e25, 5.85e24 and 4.05e24 s. The tool labels three of these five points "overcloses" even though Omega_s h² = 0.12. This appears to be a strict or rounded inequality in its threshold, not physical overclosure.

**Fractions at fixed mixing (server).** The fractions f = Omega_s h²/0.12 are:

- At 7.1 keV and sin²2θ = 5e-11: f = 0.196 (Omega_s h² = 0.0236).
- At sin²2θ = 1e-12: f = 0.025 (20 keV), 0.030 (22 keV), 0.049 (29 keV), 0.092 (41 keV) and 0.114 (46 keV).
- At sin²2θ = 1e-11: ten times these values, with 46 and 50 keV overclosing (Omega_s h² = 0.136 and 0.158).

**Other outputs.** The free-streaming lengths are 151 kpc at 7.1 keV, 107 kpc at 10 keV and 53.7 kpc at 20 keV. The server provides no momentum distribution or ⟨p/T⟩, and no per-point Lyman-alpha flag.

[[FIGURE 10]]

Figure 10 is the server's DW exclusion plot from the 80 × 80 scan over m_s = 1–100 keV and sin²2θ = 1e-14 to 1e-6 (6400 points). Of these, 3092 points overclose and 968 are BBN-excluded. The plot overlays:

- the overclosure region,
- the Omega_DM line,
- NuSTAR/XMM limits,
- a Lyman-alpha thermal-WDM bound,
- the 3.5 keV point.

Two cautions apply when reading it. First, the provenance of the overlaid X-ray and Lyman-alpha curves is not documented by the tool. Second, the tool's built-in X-ray limits have no coverage at 29–46 keV, so the absence of an X-ray boundary there is a gap in coverage, not an allowed region. The relic line drawn is also the server's normalization, which the next subsection shows sits 10–16x too low in mixing.

### Cross-check of the DW yield against the literature

**The literature fit.** Abazajian 2005, Eq. 7 (read in the text), gives

m_s = 3.40 keV (sin²2θ/1e-8)^{-0.615} (Omega_DM/0.26)^{0.5} × {0.527 erfc[−1.15 (T_QCD/170 MeV)^{2.15}]}.

The braced factor equals 1 at T_QCD = 170 MeV, and the fit is valid for 135 < T_QCD < 300 MeV. Inverted, it gives Omega_s ∝ (sin²2θ)^{1.23} m_s². The server instead scales linearly in mixing and roughly as m^1.8. The peak production temperature is T_peak ~ 130 MeV (m_s/3 keV)^{1/3}. The critic marked this finding as contested.

**Relic mixings compared.** The fit gives the relic mixings below (hand arithmetic, Omega_DM = 0.26, T_QCD = 170 MeV). Using Omega_DM = 0.264 changes them by about 1%.

| m_s (keV) | Literature relic sin²2θ | Server relic sin²2θ | Ratio (literature / server) |
|---|---|---|---|
| 3 | 1.23e-8 | 1.2e-9 | 10.2 |
| 7.1 | 3.02e-9 | 2.5e-10 | 12.1 |
| 20 | 5.61e-10 | 3.9e-11 | 14.4 |
| 29 | 3.06e-10 | 2.0e-11 | 15.3 |
| 41 | 1.75e-10 | 1.08e-11 | 16.1 |
| 46 | 1.45e-10 | 8.8e-12 | 16.4 |

So the server overproduces DW sterile neutrinos at fixed mixing. Its relic mixings should be raised by about 10–16 to match this fit. An earlier critic estimate of a 2.5x discrepancy understated the gap.

**Revised fractions.** Scaling as f = (sin²2θ/sin²2θ_relic)^{1.23} (hand arithmetic) gives:

- At 7.1 keV: f = 0.0064 for sin²2θ = 5e-11 and 0.0098 for 7e-11. This is consistent with the literature statement that DW at the 3.5 keV-line mixing makes about 1% of the dark matter. The server gives 0.196 and 0.27.
- At sin²2θ = 1e-12: f = 4.2e-4 (20 keV), 8.8e-4 (29 keV), 1.75e-3 (41 keV) and 2.2e-3 (46 keV). These are 50–60x below the server values.
- At 1e-11: f = 7e-3 (20 keV) to 0.037 (46 keV), so nothing overcloses.

These revised fractions are contested. The critic pointed out that at fixed mass the fraction should scale linearly with mixing relative to the literature relic mixing. Applying the 1.23 exponent to the mixing ratio biases f low by a factor of about 2.6–4. The direction of the conclusion is unchanged either way: the server's fractions are far too high.

The fit was also checked only against the 2005 result. Asaka, Laine & Shaposhnikov (abstract only) find yields that "differ moderately" and allow DW as all of the dark matter only below 3.5 keV (6 keV at most). The updated yields in arXiv:1705.01837 and Venumadhav+2016 were not read.

**Delta N_eff.** On the relic curve, the sterile number density is fixed by Omega_s h²/m_s, whatever yield normalization is used. A hand estimate, assuming one Weyl species, gives Delta N_eff ≈ 11.3 eV/m_s while the sterile neutrinos are relativistic:

- 1.6e-3 at 7.1 keV (the server's on-curve value there is 1.574e-3),
- 5.6e-4 at 20 keV,
- 2.5e-4 at 46 keV.

The earlier server-based statement that Delta N_eff is "at most 3e-4" therefore holds only above about 40 keV. All of these values are 2–3 orders of magnitude below BBN and Planck sensitivity (about 0.2–0.3), so BBN does not constrain keV DW dark matter. A ⟨p/T⟩ factor of about 0.9 would change the estimate by about 10%, which does not affect this conclusion.

### X-ray constraints at the DW-equivalent masses

**Server predictions.** At the server's relic mixings, the predicted line energies are E = 3.55, 10, 14.5, 20.5 and 23 keV for m_s = 7.1, 20, 29, 41 and 46 keV. The whole-halo M31 fluxes are 1.75e-3, 1.71e-2, 3.88e-2, 8.31e-2 and 0.107 ph/s/cm².

The tool returns exclusion verdicts but never the limit values themselves:

- At 7.1 keV it reports exclusion by NuSTAR M31 (Roach+2020) and XMM blank sky (Dessert+2020).
- At 20 keV and sin²2θ = 3.946e-11 it reports "EXCLUDED by: NuSTAR M31 (Roach+ 2020)", with an M31 flux of 0.0171 ph/s/cm².
- At 29 keV and sin²2θ = 2.022e-11 it reports "Not excluded by tabulated X-ray limits (within 30% in mass)" with no excluding limits listed. That point has τ = 1.77e25 s and a Milky Way centre whole-halo flux of 264 ph/s/cm².

The 29 keV result is a coverage gap, not an allowed region. The server-based exclusion statements are contested and rest on verdict strings alone.

The critic also flagged the tool's label. Roach+2020 (arXiv:1908.09037) is a Galactic-bulge analysis, while the NuS
