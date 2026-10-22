# The thermal higgsino at 1.0–1.2 TeV: relic mass, inelastic LZ rates and neutrino limits

## Abstract

This run surveyed recent work on the pure-higgsino thermal relic, used the inelastic-DM tool server to compute relic densities and xenon recoil rates, and checked the 2026 reading of the LZ 248 keV nuclear-recoil event as higgsino inelastic scattering.

- **Relic mass from the tool.** The tool's perturbative freeze-out gives Omega h^2 = 0.120 at m_chi ≈ 1159 GeV (bracketed by 1150 and 1160 GeV). This is a calibration of the tool's built-in cross-section normalisation, not an independent calculation. The independent Sommerfeld plus bound-state value from the literature is 1.08 ± 0.02 TeV.
- **LZ event under the tool's halo.** With a standard halo cut off at 776 km/s, the tool predicts zero LZ events for every delta_m ≥ 380 keV at 1.0–1.2 TeV. LZ-compatible event counts appear only near delta_m ≈ 350 keV, which lies below both the 475 keV (IceCube) and 557 keV (Super-K + IceCube) solar-neutrino exclusions.
- **What the literature region requires.** Analytic kinematics show that the published preferred region (481–519 keV) needs Earth-frame dark-matter speeds of about 920–980 km/s, and clearing the 557 keV line needs about 950–1015 km/s. The higgsino reading of the event therefore depends entirely on the halo's high-velocity tail.
- **Not done.** The elastic spin-independent comparison against the LZ and XENONnT curves at 1.1 TeV was not completed.

## Background

The pure higgsino is an electroweak doublet whose neutral states are split by a small Majorana mass, delta_m. Its thermal mass is fixed by matching the Planck abundance, Omega h^2 ≈ 0.12. A precise value needs Sommerfeld enhancement and coannihilation with the charged state (arXiv:1411.6930; analytic method in arXiv:1008.2905). Bound-state formation is claimed to matter mainly above a few TeV (arXiv:1407.7874).

Bottaro et al. (arXiv:2205.04486, Table I) give M_DM = 1.08 ± 0.02 TeV for the Dirac Y=1/2 doublet. That value includes Sommerfeld enhancement and bound-state formation and is normalised to Omega_DM h^2 = 0.11933 ± 0.00091. The same paper states that the doublet's direct-detection cross section "lies well below the neutrino" floor. Chen and Hill (arXiv:1912.07795) state: "The direct detection signal in the pure Higgsino limit remains below neutrino backgrounds for WIMPs in the TeV mass range." The relic density also sets the upper mass limit relevant to collider disappearing-track searches (arXiv:1901.02987).

For elastic scattering, the higgsino lies below the LZ 4.2 tonne-year limits (arXiv:2410.17036; best SI limit 2.2e-48 cm^2 at 40 GeV) and the XENONnT limits (arXiv:2303.14729). Tree-level Z exchange is removed by the inelastic splitting.

**The LZ event.** LZ reported a nuclear-recoil candidate at E_R = 248 ± 23 stat ± 23 sys keV, with 3.4σ local and 2.6σ global significance, in a 2.84 tonne-year exposure (arXiv:2609.06890, arXiv:2609.02608).

**Papers interpreting or constraining the event:**
- Wu, Zhang and Zhu (arXiv:2609.01590) fit the event with a higgsino.
  - With a Milky Way plus Large Magellanic Cloud (LMC) velocity distribution ("Halo 13"), they find delta_m = 481–519 keV at 1σ and 475–529 keV at 2σ.
  - With a profiled Maxwellian halo they find 312–422 keV at 1σ and 280–457 keV at 2σ, with best fit 1.09 TeV and 366 keV.
  - The relic density fixes m_chi = 1000–1183 GeV at 1σ and 943–1230 GeV at 2σ.
- Solar-capture neutrino limits:
  - arXiv:2609.07807 excludes delta_m ≲ 557 keV, assuming captured higgsinos thermalise in a standard truncated Maxwellian halo.
  - arXiv:2609.01590 excludes delta_m ≲ 475 keV at 90% CL with IceCube when captured particles stay on extended orbits without elastic cooling. Loose inputs give 466 keV and the Fe nuclear-response uncertainty gives about 454 keV. Assuming equilibrium instead, the same paper finds about 553 keV.
- Freese and Theodosopoulos (arXiv:2610.03692) find the 1.1 TeV thermal higgsino only marginally compatible with the event and IceCube. Their compatible regions run from about 2 TeV to hundreds of TeV with delta ≈ 350–525 keV.
- arXiv:2609.09830 computes one-loop electroweak corrections to delta_m and to the scattering rates.
- arXiv:2609.06890 proposes boosted dark matter, which does not depend on the halo tail.

Several of these literature numbers were read directly in the full texts but could not be validated as verbatim quotes, because PDF extraction garbles math symbols and en-dash ranges. Treat them as read but not independently verified.

## Results

### Relic density versus mass (tool)

The tool's `compute_relic_density` uses perturbative Kolb–Turner freeze-out (x_f ≈ 24.4–24.8, g* = 86.25) with sigma_v = 2.5e-26 cm^3/s × (1100 GeV/m_chi)^2.

| m_chi (GeV) | Omega h^2 |
|---|---|
| 900 | 0.0731 |
| 1000 | 0.0898 |
| 1100 | 0.1083 |
| 1150 | 0.1181 |
| 1160 | 0.1202 |
| 1200 | 0.1285 |
| 1300 | 0.1503 |

The Planck crossing (0.120 ± 0.0012) is at about 1159 GeV.

- **Comparison with the literature.** This is about 1% below the 1172 GeV inferred, not quoted, from arXiv:1411.6930. It is about 7% above the 1.08 TeV of arXiv:2205.04486.
- **Why it is not a check.** The agreement follows from the hard-coded normalisation; it is not independent physics.
- **Missing inputs.** The tool has no Sommerfeld or coannihilation switch, no charged-splitting input and no delta_m dependence: Omega h^2 = 0.1202 at 1160 GeV for delta = 400, 500 and 600 keV. The "with and without Sommerfeld/coannihilation" and charged-splitting sensitivity items could not be run.
- **Unreliable flag.** The tool's `consistent_planck` flag reads True at 25σ tension and False at 39σ.

### Inelastic recoil kinematics and LZ event counts (tool)

The tool's halo is a standard halo with a hard cutoff at v_esc + v_E = 776 km/s. No call exposes halo parameters. Results at m_chi = 1100 GeV, sigma_n = 7.43e-39 cm^2:

| delta (keV) | E_R,peak (keV) | v_min at peak (km/s) | v_min at 248 keV (km/s) | N_LZ (2.84 t-yr) |
|---|---|---|---|---|
| 300 | 270 | 701 | 701 | 744.6 |
| 400 | 360 | 809 | 823 | 0.00 |
| 480 | 432 | 886 | 921 | 0.00 |
| 520 | 468 | 922 | 969 | 0.00 |
| 560 | 504 | 957 | 1018 | 0.00 |

Scaling by exposure gives about 1101 events at 4.2 t-yr for 300 keV and zero for the rest. The tool does not report a separate E_R,min or an integrated rate above 100 keV. The annual-modulation output at (1100 GeV, 500 keV, 248 keV) is identically zero, because the rate is zero.

Bracketing near the edge with `predict_recoil` (2.84 t-yr):

| delta (keV) | events at 1000 GeV | events at upper mass |
|---|---|---|
| 340 | 10.67 | 17.30 (1183 GeV) |
| 350 | 1.13 | 2.90 (1200 GeV) |
| 360 | 0.03 | 0.158 (1183 GeV) |
| 380 | 0.00 | 0.00 (1183 GeV) |

**Scans.**
- A 15×15 scan (900–1300 GeV, 300–650 keV) found 180 of 225 points passing all constraints. Only 12 points predict 0.3–5 LZ events, with best fit (986 GeV, 350 keV).
- A 16×16 scan (1000–1200 GeV, 330–480 keV) passed all 256 points. It placed 16 points in the 0.3–5 band, with best fit (1000 GeV, 350 keV).
- That those 16 points form the delta = 350 keV row is inferred from the bracketing above. The binary scan file could not be read, so this was not listed directly by the tool.
- The second scan overwrote the first scan's file (`.../inelastic-dm-server/output/scan_idm.npz`) and its summary plot (`constraint_summary.png`). A recoil-spectrum plot for 1100 GeV / 500 keV is at `.../output/recoil_spectrum.png`.
- No numbered figures were produced.

**Interpretation.** Under the truncated halo, no LZ-compatible point reaches delta ≥ 360 keV. In particular none reaches the 475 or 557 keV neutrino lines, so no tool point that reproduces the event survives the neutrino limits. The critic stressed that the band near 350 keV is an artefact of the hard cutoff, where N falls from 10.7 to 1.1 to 0.03 over 20 keV. It is not a physical preferred region.

### Analytic kinematic check

The maximum splitting that can produce a recoil at E_R = 248 keV for a given maximum speed is

delta_max = v_max·sqrt(2 m_N E_R) − m_N E_R/mu,

with m_N = 122.0 GeV (Xe-131) and sqrt(2 m_N E_R) = 0.8206 keV per km/s.

| v_max (km/s) | delta_max at 1000 GeV (keV) | at 1100 GeV | at 1183 GeV |
|---|---|---|---|
| 776 | 358.5 | 361.3 | 363.2 |
| 800 | 378 | 381 | 383 |
| 850 | 419 | 422 | 424 |
| 900 | 460 | 463 | 465 |

- **Agreement with the tool.** This reproduces the tool's v_min(248 keV) to within about 1 km/s.
- **Origin of the "about 365 keV" edge.** That figure is the endpoint with E_R left free, mu v_max^2/2 = 364–370 keV at 776 km/s, reached near E_R ≈ 330 keV rather than at 248 keV.

Inverting at 1100 GeV gives the Earth-frame v_max needed to reach a given splitting:

| delta (keV) | v_max with event at 248 keV (km/s) | v_max with E_R free (km/s) |
|---|---|---|
| 422 | — | 830 |
| 457 | 893 | 864 |
| 475 | 915 | 881 |
| 519 | 968 | 921 |
| 529 | 980 | 930 |
| 557 | 1015 | 954 |

At 1000 GeV these values shift by about +3 km/s, and at 1183 GeV by about −2 km/s.

What this implies:
- The profiled-Maxwellian edges of arXiv:2609.01590 (422/457 keV) imply an effective endpoint of about 830–890 km/s.
- The Halo 13 edges (519/529 keV) need an LMC-boosted tail reaching about 920–980 km/s.
- Clearing 475 keV needs at least about 880–915 km/s, and clearing 557 keV needs at least about 950–1015 km/s.

The critic noted two sources of uncertainty that make these thresholds uncertain by roughly ±10–20 km/s:
- The calculation assumes a single isotope. Natural xenon spans A = 124–136, and Xe-134 raises delta_max by about 7 keV at 776 km/s and 1.1 TeV.
- The ±23 keV statistical and systematic energy uncertainty also enters.

### Combined constraint check (tool)

At 1160 GeV, `check_all_constraints` returns "VIABLE" for delta = 400, 500 and 600 keV:

| Quantity | delta = 400 keV | 500 keV | 600 keV | Tool's limit |
|---|---|---|---|---|
| Omega h^2 | 0.1202 (0.1σ) | 0.1202 | 0.1202 | — |
| N_LZ (2.84 t-yr) | 0.00 | 0.00 | 0.00 | flagged inconsistent with 1 observed event |
| sigma_v today (cm^3/s) | 6.7e-42 | 1.04e-41 | 1.50e-41 | 2.48e-25 (Fermi) |
| CMB p_ann | 0.86e-45 | 1.35e-45 | 1.94e-45 | 3.2e-28 |

At (1100 GeV, 500 keV) the check gives Omega h^2 = 0.1083, N_LZ = 0 and sigma_v = 1.29e-41 against a Fermi limit of 2.3e-25.

Warning: these verdicts are not physically reliable. The tool treats annihilation today as p-wave and splitting-suppressed, whereas the higgsino annihilates s-wave to WW/ZZ at about 1e-26 cm^3/s. The "viable" label therefore means invisible, not allowed. The critic contested this finding, and no s-wave replacement was computed.

### Literature: why the two neutrino lines differ, and gamma-ray lines

The 475 vs 557 keV difference comes from how captured particles are treated in the Sun, not from the halo model (read in the full texts; not independently verified).

- **arXiv:2609.01590 (475 keV).** At 1.11 TeV it uses a non-thermal captured population on extended orbits, <sigma v>_eff ≈ 1.5e-26 cm^3/s with Sommerfeld, and ten years of IceCube data.
- **arXiv:2609.07807 (557 keV).** It assumes thermalisation, a truncated Maxwellian (u0 = 220, v_esc = 544, v_sun = 232 km/s; rho = 0.4 GeV/cm^3), sigma_chi_n = 7.4e-39 cm^2, <sigma v> = 1.3e-26 cm^3/s and m_chi = 1.08 TeV. It uses a 95% CL fit to IceCube nu_mu, IceCube nu_e and Super-K. It still allows rescue by an LMC tail or substructure.
- **arXiv:2610.03692.** It shows four 90% CL IceCube cooling treatments in its Fig. 2:
  - capture–annihilation equilibrium;
  - spin-independent (SI) inelastic cooling only;
  - SI inelastic plus spin-dependent (SD) elastic cooling;
  - SI inelastic plus SD plus SI elastic cooling, with sigma_SI,el = 4e-50 cm^2.

  Its other inputs are a standard halo with rho = 0.3 GeV/cm^3, sigma_Hn = 7.43e-39 cm^2 and an LMC tail cut at 950 km/s. It states the solar limits "remain unchanged by adding the effects of the LMC". The delta values at 1.1 TeV for each treatment appear only in the figure and were not quantified.

**Gamma-ray lines (arXiv:2609.01590).** The thermal line prediction is 0.815–0.900 of the H.E.S.S. 546 h limits, which the paper describes as close to but not excluded. The CTAO Alpha 500 h projection gives mu_gamma,95 = 1.69, which falls short of the thermal target. An Omega-configuration estimate of 0.85 would reach it, but it is unverified whether that number comes from the paper or from the agent's own 1.69/2 scaling. Dwarf, CMB and ATLAS disappearing-track limits do not exclude the region.

**Radiative corrections (arXiv:2609.09830).** Its benchmarks have one-loop on-shell splittings of 36.37, 8.90, 16.39, 10.81 and 10.59 keV at |mu| = 0.61–1.40 TeV, all with Omega h^2 < 0.12. It gives no delta_m shift in the 475–557 keV window. A tree-to-one-loop shift of order 0.1 GeV was read off its mass table by the agent; the paper does not state it. It therefore does not bear on rescuing the window.

## Discussion

**Relic mass.** The tool's 1159 GeV is a normalisation echo. The best independent anchor in the record is 1.08 ± 0.02 TeV (arXiv:2205.04486), which includes Sommerfeld enhancement and bound states. The 1172 GeV figure attributed to arXiv:1411.6930 is inferred rather than quoted. Which value to use as the headline remains open, since published thermal masses differ by roughly 10–20% depending on treatment.

**The LZ event.** Our computations and the literature agree on one point: the LZ reading requires a population of halo particles above roughly 880 km/s in the Earth frame. A standard halo truncated at 776 km/s caps the splitting at about 360 keV at 248 keV recoil. That is below every neutrino exclusion line. This is consistent with arXiv:2609.07807's statement that the reading is disfavoured for standard halo velocities, and with arXiv:2610.03692's "marginal" verdict.

What the run could not do is decide between the published analyses. They differ in the solar treatment (thermalised or not) and in how much LMC tail they assume. Our tool can vary neither.

**Current limits.** The task asked where the higgsino sits relative to current limits. Only qualitative literature statements are available for the elastic channel: below the LZ and XENONnT reach, and below the neutrino floor according to arXiv:1912.07795 and arXiv:2205.04486. No numerical limit at 1.1 TeV was read. For indirect detection, the only computed numbers come from the tool's unphysical p-wave treatment. The literature gamma-ray line ratio (0.815–0.900 of H.E.S.S.) suggests the thermal higgsino is close to current sensitivity, but that number is not independently verified.

**Dead ends.**
- No tool exposes halo parameters, so the dependence on v_esc and on an LMC tail could not be tested. A custom rate code is needed.
- `load_table_data` cannot read the binary scan file, so scan-band membership had to be inferred by bracketing.
- Verbatim quotes from arXiv:2609.01590 failed because of garbled math: the endpoint sentence, the H.E.S.S. ratio, the 553 keV bound, the Maxwellian best fit and the relic ranges.
- The Planck 2018 quote "0.120 \pm 0.001" was not found in the extracted text, so Planck is not yet cited in the reference file.
- The tool budget ran out before narrow re-reads of arXiv:2609.01590 and arXiv:2609.07807 and before an s-wave indirect-detection comparison.

## Limitations

- **Relic density.** The tool is perturbative only, with no Sommerfeld, coannihilation, charged-splitting or delta_m dependence. The relic mass is therefore not an independent computation.
- **Event counts.** Counts assume the tool's unstated LZ acceptance in its extended nuclear-recoil search and a single halo with a hard 776 km/s cutoff. There is no isotope averaging, and the critic noted thresholds carry about ±10–20 km/s.
- **Elastic SI comparison.** Not done: the LZ 4.2 t-yr and XENONnT 90% CL values near 1.1 TeV, the higgsino sigma_SI band and the neutrino-fog level were never read. The critic flagged this as the main missing piece.
- **Indirect and CMB.** These rest on an unphysical p-wave assumption. No s-wave comparison was made.
- **Unverified literature numbers.** Several literature numbers (preferred regions, 553 keV, the H.E.S.S. ratio, the CTAO Omega estimate, the doublet mass, the arXiv:2610.03692 and arXiv:2609.09830 details) were not independently verified. The critic contested them, mostly because of failed verbatim quotes or abstract-only reading.
- **Reproducibility.** The first scan's outputs were overwritten and cannot be reproduced from disk.
- **Compute.** All computation ran locally. No HPC facility was used.

## Open directions

1. Read the LZ 4.2 t-yr (arXiv:2410.17036) and XENONnT (arXiv:2303.14729) SI 90% CL limits near 1.1 TeV from text or HEPData and place the Chen–Hill higgsino band and the neutrino fog against them.
2. Write a custom inelastic rate code with variable v_esc and an LMC high-velocity tail to compute LZ event counts across delta_m = 400–600 keV and test the 481–519 keV region directly.
3. Replace the tool's p-wave indirect pass with an s-wave WW/ZZ (about 1e-26 cm^3/s) comparison against Fermi dwarf and H.E.S.S. continuum and line limits at 1.1 TeV.
4. Obtain an independent Sommerfeld-plus-coannihilation thermal mass (e.g. via the arXiv:1008.2905 method) and reconcile it with 1.08 ± 0.02 TeV and the inferred 1172 GeV.
5. Re-read narrow windows of arXiv:2609.01590 and arXiv:2609.07807 to validate the contested numbers, including whether the CTAO Omega 0.85 is the paper's own value.
6. Extract the per-treatment IceCube delta limits at 1.1 TeV from arXiv:2610.03692 Fig. 2.
7. Add isotope averaging over natural xenon and the ±23 keV energy uncert
