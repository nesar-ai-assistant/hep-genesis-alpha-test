# Lyman-alpha forest constraints on warm dark matter compared with non-resonant (Dodelson-Widrow) sterile-neutrino production

## Abstract

We checked the recent high-redshift Lyman-alpha forest lower limits on the thermal-relic warm dark matter (WDM) mass against the papers. The values are 3.1, 3.3 and 5.7 keV (95% CL), and 4.1 keV for the scale-restricted variant of the strongest analysis. We converted them to non-resonant (Dodelson-Widrow, DW) sterile-neutrino mass floors with the Viel et al. 2005 relation, now verified against its full text. The floors are about 20, 22, 29 and 45 keV.

A sterile-neutrino tool server computed the DW relic abundance Omega_s h^2 as a function of (m_s, sin^2 2theta). From this we obtained the mixing at which DW sterile neutrinos make up all of the dark matter (f_s = 1) at each floor:

| m_s | sin^2 2theta at f_s = 1 |
|---|---|
| 20 keV | 3.95e-11 |
| 22 keV | 3.32e-11 |
| 29 keV | 2.02e-11 |
| 45 keV | 9.17e-12 |

The tool's normalisation produces 3 to 16 times more DW dark matter per unit mixing than two published yield fits. This makes the production fraction uncertain by that factor. At the 3.5 keV line point the fraction is f_s = 0.275 (tool), 0.089 or 0.023 (published fits).

The tool's coarse X-ray check excludes f_s = 1 at 20 keV. At 29 and 45 keV it has no coverage and cannot decide. Numerical X-ray limits on sin^2 2theta were not obtained, so the central comparison is incomplete: the maximum DW fraction allowed by X-rays at each Lyman-alpha floor could not be computed. On the evidence gathered here, we cannot show that 100% DW dark matter is excluded once Lyman-alpha and X-ray constraints are combined.

## Background

The Lyman-alpha flux power spectrum at z ~ 4-5 probes the small-scale suppression caused by WDM free-streaming. The limits have tightened over time:

- **Narayanan et al. 2000 (arXiv:astro-ph/0005095):** m_WDM > 750 eV, the historical baseline.
- **Viel et al. 2013 (arXiv:1306.2314):** benchmark limit of m_WDM > 3.3 keV (2 sigma) from 25 HIRES/MIKE quasars at z > 4.
- **Irsic et al. 2017 (arXiv:1702.01764):** combined XQ-100 with HIRES/MIKE.
- **Villasenor et al. 2022 (arXiv:2209.14220):** independent analysis using 1080 Cholla simulations.
- **Irsic et al. 2023 (arXiv:2309.04533):** the current strongest bound. It names IGM peculiar velocities and inhomogeneous reionization as the leading small-scale systematics.

These are thermal-relic limits. Applying them to DW sterile neutrinos needs a mass mapping. The standard one is from Viel et al. 2005 (arXiv:astro-ph/0501562). Emulator frameworks for general non-cold spectra exist (arXiv:2007.13751) but do not supply a DW-specific relation.

Mixed cold-plus-warm models are constrained as a function of the warm fraction:

- Boyarsky et al. 2008 (arXiv:0812.0010), stated in the DW mass itself.
- Garcia-Gallego et al. 2025 (arXiv:2504.06367), stated in thermal-relic mass.

On the particle side, Merle's 2017 review (arXiv:1702.08430) describes DW production as excluded by observations. arXiv:1512.05369 treats DW on top of other production channels. NuSTAR line searches set the leading X-ray limits over roughly 10-50 keV:

- Perez et al., arXiv:1609.00667.
- Roach et al. 2020, arXiv:1908.09037.
- Roach et al. 2022, arXiv:2207.04572.

## Results

### Thermal-relic Lyman-alpha limits

The limits were checked against the full text for arXiv:2309.04533 and against the abstracts for the others.

- **Irsic et al. 2023 (arXiv:2309.04533):** m_WDM > 5.7 keV (95% CL). It uses HIRES+UVES data at z = 4.2-5.0 with k_max = 0.2 s/km. Restricting to k_max < 0.1 s/km with earlier thermal-history priors gives 4.1 keV. The main small-scale modelling systematics are IGM peculiar velocities and inhomogeneous reionization. The paper says the thermal-history uncertainty now matters less.
- **Villasenor et al. 2022 (arXiv:2209.14220):** m_WDM > 3.1 keV, with a likelihood peak at 4.5 keV. It uses Boera et al. 2019 data at 4.0 < z < 5.2. The suppression saturates at k > 0.1 s/km because of peculiar-velocity smearing.
- **Viel et al. 2013 (arXiv:1306.2314):** m_WDM > 3.3 keV from 25 HIRES/MIKE quasars at z > 4.
- **Irsic et al. 2017 (arXiv:1702.01764):**
  - XQ-100 alone (z = 3-4.2) gives 1.4 keV.
  - Re-analysed HIRES/MIKE gives 4.1 keV.
  - The combination gives 5.3 keV, assuming a power-law T(z).
  - Allowing sudden temperature jumps of up to 5000 K lowers the combined limit to 3.5 keV.

The k_max and prior details of the three abstract-only papers were not checked against their full texts.

### Mapping thermal-relic limits to DW mass

Eq. (5) of Viel et al. 2005 was verified in the full text:

m_sterile = 4.43 keV (m_thermal / 1 keV)^{4/3} (0.25 (0.7)^2 / omega_x)^{1/3}

The normalisation 0.25 x 0.49 = 0.1225 matches the brief. The relation follows from equating omega_x and m_x/T_x for a thermal relic and a sterile neutrino "which share the same phase-space distribution but with an overall suppression factor chi". The DW spectrum is therefore treated as a rescaled Fermi-Dirac distribution, and the thermal and DW transfer functions are identical by construction.

DW floors from our own arithmetic:

| Thermal-relic limit | DW floor, omega_dm = 0.12 | DW floor, omega_dm = 0.1225 |
|---|---|---|
| 3.1 keV | 20.2 keV | 20.0 keV |
| 3.3 keV | 21.9 keV | 21.8 keV |
| 4.1 keV | 29.3 keV | 29.1 keV |
| 5.7 keV | 45.4 keV | 45.1 keV |

These confirm the brief's rough values to within 1%. Using the 4.1 keV variant instead of 5.7 keV lowers the DW floor from about 45 keV to about 29 keV. This is the size of the effect of restricting scales and priors.

**Transfer-function fit.** Viel 2005 fits T(k) = [1 + (alpha k)^{2nu}]^{-5/nu}, with nu = 1.12, for k < 5 h/Mpc. For thermal relics, alpha = 0.049 (m_x/keV)^{-1.11} (Omega_x/0.25)^{0.11} (h/0.7)^{1.22} h^-1 Mpc. Setting T^2 = 1/2 gives k_hm = 0.325/alpha (our arithmetic). For 3.1, 3.3, 4.1 and 5.7 keV this gives:

| Thermal-relic limit | alpha (h^-1 Mpc) | k_hm (h/Mpc) |
|---|---|---|
| 3.1 keV | 0.01396 | about 23.3 |
| 3.3 keV | 0.01302 | about 25.0 |
| 4.1 keV | 0.01024 | about 31.8 |
| 5.7 keV | 0.00710 | about 45.8 |

These lie far outside the k < 5 h/Mpc range on which the fit was calibrated. The critic did not consider the k_hm values settled, because they are an extrapolation and were not recomputed against the half-mode mass of about 2x10^8 Msun/h quoted in arXiv:1306.2314. Under Viel's mapping the DW k_hm is identical by construction, so this calculation does not test the mapping itself.

**The arXiv:2007.13751 framework.** It uses T(k) = [1 + (alpha k)^beta]^gamma. This reduces to the Viel form for beta = 2nu and gamma = -5/nu. A 2 keV WDM is fitted by [alpha, beta, gamma] = [0.02, 2.2, -4.5]. In the sections read, it gives no DW relation. Using it for DW would require fitting these parameters to a Boltzmann-code DW transfer function, which was not possible without CLASS/CAMB.

No second, independent mapping was verified, so the spread between mappings is unknown.

### DW abundance from the sterile-neutrino tool

The server models pure DW production, with Shi-Fuller resonant production available as a separate option. It returns:

- Omega_s h^2
- Delta N_eff
- BBN observables
- lifetime
- free-streaming length

It does not return k_hm. Contrary to the brief's warning, the tool does return relic abundances, so f_s = Omega_s h^2 / 0.12 is tool-derived. The rescaling to f_s = 1 below is our own arithmetic.

Omega_s h^2 scales linearly with sin^2 2theta; a 374-point grid confirmed this. At sin^2 2theta = 1e-12 the tool gives the values below, and linear scaling gives the f_s = 1 mixings:

| m_s | Omega_s h^2 at sin^2 2theta = 1e-12 | sin^2 2theta at f_s = 1 |
|---|---|---|
| 7.1 keV | 0.000471462 | 2.55e-10 |
| 20 keV | 0.00304114 | 3.95e-11 |
| 22 keV | 0.00361029 | 3.32e-11 |
| 29 keV | 0.00593606 | 2.02e-11 |
| 45 keV | 0.0130907 | 9.17e-12 |

As a direct check at the 3.5 keV line point (7.1 keV, sin^2 2theta = 7e-11), the tool returns Omega_s h^2 = 0.033, so f_s = 0.275.

### Cross-check of the DW normalisation

Two published DW yield fits were read in full text. They are quoted in the findings, but the citation step that validates quotes was not run for them.

- **Abazajian 2006 (astro-ph/0511630), Eq. 7:** m_s = 3.40 keV (sin^2 2theta / 1e-8)^-0.615 (Omega_DM / 0.26)^0.5, for T_QCD = 170 MeV and electron flavour.
- **Asaka-Laine-Shaposhnikov (hep-ph/0612182, Sec. 7.1):** the "most conservative" line, log10 sin^2 2theta = -7.6195 - 1.7428 log10(M/keV). The paper states this fit for M <= 4 keV, so using it here is an extrapolation. It is an overclosure upper line, so its ratio to the tool is a lower limit on the discrepancy.

Inverted to give the f_s = 1 mixing at the five masses:

| m_s | Tool | Abazajian 2006 (ratio to tool) | Asaka-Laine-Shaposhnikov (ratio to tool) |
|---|---|---|---|
| 7.1 keV | 2.55e-10 | 3.02e-9 (11.9) | 7.88e-10 (3.10) |
| 20 keV | 3.95e-11 | 5.61e-10 (14.2) | 1.30e-10 (3.29) |
| 22 keV | 3.32e-11 | 4.80e-10 (14.4) | 1.10e-10 (3.31) |
| 29 keV | 2.02e-11 | 3.06e-10 (15.2) | 6.79e-11 (3.36) |
| 45 keV | 9.17e-12 | 1.50e-10 (16.4) | 3.16e-11 (3.44) |

The tool therefore produces about 3 to 16 times more DW dark matter per unit mixing than these fits. At the 3.5 keV line point, f_s is:

- 0.275 with the tool,
- 0.089 with the Asaka-Laine-Shaposhnikov line,
- 0.023 with Abazajian 2006.

The tool is the most generous of the three. Its X-ray exclusion of f_s = 1 at 20 keV can therefore only get stronger under the published normalisations. Both the factor and its consequences were contested by the critic. The critic asks that the factor be settled with a modern DW calculation valid at 10-50 keV, rather than fits extrapolated from lower masses.

### X-ray status of the f_s = 1 points

The tool's X-ray check returns only an excluded/not-excluded flag based on sparse tabulated points. It gives no numerical limit on sin^2 2theta.

- **20 keV, sin^2 2theta = 3.95e-11:** excluded by the tool's tabulated NuSTAR M31 point, which the tool attributes to Roach et al. 2020.
- **29 keV (2.02e-11) and 45 keV (9.17e-12):** reported "not excluded", but only because no tabulated limit lies within 30% in mass. This means no coverage, not allowed.
- **22 keV:** not run.

The critic marked this result as needing independent confirmation, because it rests on the tool's coarse tabulation.

From the literature, with quotes verified:

- **Perez et al. (arXiv:1609.00667):** "In most of the mass range 10–50 keV, these are now the strongest limits". The curves are plotted on a sin^2 2theta axis from 1e-15 to 1e-7.
- **Roach et al. 2020 (arXiv:1908.09037):** find no anomalous lines at 5-20 keV, corresponding to m_s = 10-40 keV. Their limits are given on the decay rate Gamma, plotted on a 1e-29 to 1e-27 s^-1 axis. They are about 2x better than earlier limits at 10-12 keV, and weaker near 16 keV and 30-40 keV, where the background fit shows excesses. This reading was contested by the critic and is not independently verified.
- **Roach et al. 2022 (arXiv:2207.04572):** use about 7 Ms per detector of blank-sky data plus about 20 Ms per detector of stacked data. They "strongly disfavor a ~7-keV sterile neutrino" and give leading limits at about 15-18 and 25-40 keV, "reaching or extending below the big bang nucleosynthesis limit". They also state that this "does not fully rule out sterile neutrinos as the only DM component", only that "the simple and elegant mixing production mechanism … may be insufficient". Their statement that the parameter space is "mostly covered" includes satellite-counting bounds.

No numerical sin^2 2theta limits were extracted at 7, 20, 22, 29 or 45 keV, because the papers give them only as figure curves. NuSTAR coverage ends at 40 keV, so 45 keV would need INTEGRAL/SPI or Fermi-GBM limits.

### BBN in the DW plane

A 6400-point DW scan covered m_s = 1-100 keV and sin^2 2theta = 1e-14 to 1e-6. It found 3092 overclosing points (Omega_s h^2 > 0.12) and 968 points excluded by BBN at 95%.

[[FIGURE 25]]

Figure 25 shows the resulting exclusion map. The largest BBN-allowed mixing is 3.03e-8 at 26.2 keV and 1.5e-8 at 49.7 keV. This is about three orders of magnitude above the f_s = 1 line and deep in the overclosed region. BBN therefore does not constrain DW dark matter, but only trivially so; the relevant constraints are X-ray and Lyman-alpha. The two maximum-mixing values are not visible in the quoted tool output excerpt.

### Mixed cold-plus-warm bounds and the combined fraction table

**Garcia-Gallego et al. 2025 (arXiv:2504.06367).** This uses Sherwood-Relics simulations with a neural-network emulator and UVES+HIRES data at z = 4.2-5.0. It gives f_WDM < 0.16, 0.35, 0.50 and 0.67 (2 sigma) for thermal-relic masses of 1, 2, 3 and 4 keV.

**Boyarsky et al. 2008 (arXiv:0812.0010).** This is stated directly in the DW mass m_nrp:

- Pure WDM: m_nrp >= 8 keV (frequentist 99.7%) or 12.1 keV (Bayesian 95%).
- For any m_nrp above 5 keV, the model is allowed if F_wdm < 0.6 (99.7%) or F_wdm < 0.35 (Bayesian 95%).

Mapping the arXiv:2504.06367 masses through Viel's relation gives roughly 4.4, 11, 18 and 28 keV in DW mass. This is our own estimate. It applies a thermal-relic mixed-DM bound to DW spectra, which the critic regards as not justified.

Combined Lyman-alpha picture (low confidence; contested):

- **7.1 keV:** below the 12.1 keV pure-DW floor of arXiv:0812.0010. The mixed-DM bound binds, f_s ≲ 0.2-0.35.
- **20 and 22 keV:** the mapped bound gives f ≲ 0.5-0.67. These masses are below the 29 and 45 keV floors. The tool's X-ray flag excludes f_s = 1 at 20 keV.
- **29 keV:** f = 1 is allowed by Lyman-alpha only for the 4.1 keV variant. For the 5.7 keV variant, f ≲ 0.67 or somewhat more.
- **45 keV:** f = 1 is allowed by Lyman-alpha even for the 5.7 keV variant.
- **29 and 45 keV, X-ray side:** the X-ray constraint is presumably the binding one, but no numerical value exists, so the X-ray-allowed f_s,max is undetermined. For fractional DW the X-ray limit applies to f_s x Gamma, and f_s is itself proportional to sin^2 2theta. This step was not carried out.

The 0812.0010 figure files were downloaded, but none was analysed or digitised for this report. The extracted 2504.06367 figures are a simulation slice and an emulator schematic, not constraint plots, so they are not shown.

## Discussion

The Lyman-alpha side is now well characterised for thermal relics, and the Viel 2005 conversion to DW mass is confirmed in form and coefficient. The DW floors of roughly 20-45 keV are therefore reproducible under that convention.

The main uncertainty in the DW floor is not the conversion arithmetic. It is the analysis cho
