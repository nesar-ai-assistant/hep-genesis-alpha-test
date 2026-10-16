# The 1.0–1.2 TeV thermal higgsino against LZ, XENONnT, Planck and gamma-ray limits: toy-model calculations and an abstract-level literature survey

## Abstract

This investigation asked where the pure higgsino thermal relic, at about 1.0–1.2 TeV, sits relative to current limits.

**Tool calculations.** An inelastic-dark-matter (inelastic-DM) server was used for relic and recoil calculations.

- **Relic density.** The server's relic model is a single-channel freeze-out scaling calibrated near 1.1 TeV. It reaches the Planck abundance at about 1158 GeV. This lies inside the 1.08–1.2 TeV literature range, but it is a calibration result, not a Sommerfeld/coannihilation prediction.
- **LZ inelastic events.** The server's Z-exchange higgsino predicts these LZ counts at 1.1 TeV for the 2.84 tonne-year extended nuclear-recoil window:

| Mass splitting delta (keV) | Expected LZ events |
|---|---|
| 300 | 744.6 (excluded) |
| 350 | about 2 |
| 380 and above | 0 |

- **Kinematic edge and one-event window.** The cutoff sits at about 368 keV for the tool's 776 km/s halo cutoff. It would sit at about 385 keV for 794 km/s. The "about one event" window is only about 4 keV wide, at 352–356 keV.

**Literature, from abstracts only.** None of the following could be verified against full texts.

- Solar-capture limits from IceCube require delta > 566 keV.
- That puts every solar-capture-allowed thermal higgsino beyond the inelastic reach of xenon.
- The pure-higgsino elastic cross section is described as lying below the neutrino floor.
- The higgsino is not excluded by current gamma-ray line searches, and the Cherenkov Telescope Array Observatory (CTAO) is identified as the decisive future test.

**Bottom line.** The full-abundance thermal higgsino at about 1.1 TeV is not excluded. Its interpretation as the source of the sub-MeV-splitting LZ 248 keV event is disfavoured. With splittings of order an MeV it is effectively invisible to current xenon detectors.

## Background

**Thermal mass.** With Sommerfeld enhancement and coannihilation included, a pure higgsino gives the full Planck abundance at roughly 1.0–1.2 TeV. Quoted values are:

- about 1.08–1.1 TeV (arXiv:2609.02775, arXiv:2609.02608);
- "~1.2 TeV" (arXiv:2410.15733);
- an upper end of about 1150 GeV, with the thermal higgsino-like mass required to lie "between about 100 GeV and 1150 GeV" (arXiv:2403.19598).

Lighter thermal higgsinos are under-abundant by a factor of 5–20 in natural SUSY (arXiv:1803.11210).

**Direct detection.** The pure higgsino is inelastic dark matter. Z-mediated scattering requires the neutral-state splitting delta to be no more than a few hundred keV. If delta lies beyond the kinematic reach of xenon, only loop-level elastic scattering remains, and that rate sits near or below the neutrino fog (arXiv:2609.01504, arXiv:2410.02723). One 2026 abstract states that next-to-leading-order corrections push the pure-higgsino nucleon cross section "below the neutrino floor" (arXiv:2607.20588). Higgsino–gaugino mixing raises the elastic rate (arXiv:2606.31013).

**The 2026 LZ result.** LZ reported a 2.84 tonne-year search with a recoil window extended to about 270 keV (arXiv:2609.02823). It found one event at 248 ± 23 (stat) ± 23 (sys) keV, with 2.6σ global and 3.4σ local significance.

Interpretations of that event as a higgsino give these preferred splittings:

| Assumption or method | Preferred delta | Source |
|---|---|---|
| Standard Halo Model | about 350 keV | arXiv:2609.01504 |
| Standard Halo Model | 377 keV | arXiv:2609.02608 |
| Sideband optimum at 1 TeV | 339 keV, about 1.9σ tension | arXiv:2609.26698 |
| Including the Large Magellanic Cloud (LMC) | about 480–520 keV | arXiv:2609.01504; 481–519 keV in arXiv:2609.01590 |

**Tensions with the event interpretation.**

- **Solar capture.** IceCube non-observation requires delta > 566 keV (arXiv:2609.02775). This is supported by arXiv:2609.11833 and arXiv:2609.07807. arXiv:2609.06760 quotes 0.51–0.56 MeV.
- **Empty sideband.** The absence of events above 350 keV is in tension with the thermal-mass fit (arXiv:2609.09385, arXiv:2609.26698).
- **Halo uncertainties.** These cannot close the gap (arXiv:2609.15321). Under the Standard Halo Model, delta > 566 keV would need v0 > 240 km/s. With the LMC included, the largest workable splitting is 514 keV.

**Surviving branch.** A Planck-compatible thermal branch survives at delta of about 0.85–1.34 MeV (arXiv:2610.00226). arXiv:2609.09136 proposes a non-higgsino alternative.

**Caveat on sources.** All 2026-dated identifiers came from an OpenAlex-backed search and could not be resolved through the arXiv API. They should be checked on arxiv.org before anyone cites them.

## Results

### Relic density from the inelastic-DM server (toy model)

The relic tool was run with the higgsino flag set. This flag sets σv = 2.5×10⁻²⁶ cm³/s × (1100 GeV/m)² and feeds it into a Kolb–Turner freeze-out estimate, with x_f about 24.5 and g* = 86.25. The tool has no Sommerfeld or coannihilation switch.

| m_χ (GeV) | Ω h² |
|---|---|
| 900 | 0.0731 |
| 1000 | 0.0898 |
| 1100 | 0.1083 |
| 1200 | 0.1285 |
| 1300 | 0.1503 |

- **Planck crossing.** Linear interpolation reaches Ω h² = 0.120 at about 1158 GeV. The server's ±0.0012 band gives ±6 GeV; the ±0.001 band gives about ±5 GeV. A direct call at 1159 GeV returns 0.120.
- **Comparison with the literature.** This crossing is inside the 1.08–1.2 TeV range. It is about 60–80 GeV above the 1.08–1.1 TeV values and close to the ~1.2 TeV value of arXiv:2410.15733.
- **Interpretation.** The agreement reflects how the tool's cross section is normalized. It should be read as a toy-model crossing, not a higgsino prediction.
- **Tests not run.** The with/without-Sommerfeld comparison and splitting-dependence tests could not be done.
- **Pass flag.** The tool marks results as "consistent" with Planck even at 7–25σ tension; for example, 1100 GeV carries 9.8σ tension. This looks like a bug.

### LZ inelastic event counts and the kinematic reach of xenon

The recoil tool uses:

- Z exchange, with σ_n = 7.43×10⁻³⁹ cm² per nucleon;
- the LZ 2.84 tonne-year extended nuclear-recoil window;
- a hard halo cutoff at v_esc + v_E = 776 km/s.

Expected LZ counts at m_χ = 1100 GeV:

| delta (keV) | Expected LZ events | Spectrum peak (keV) | Notes |
|---|---|---|---|
| 300 | 744.6 | not recorded | Grossly excluded against 1 observed event |
| 350 | 1.97 | 315 | P(N ≥ 1) = 0.86; the 248 keV event needs v_min = 762 km/s, which is accessible |
| 380 | 0.00 | 342 | The 248 keV event needs v_min = 799 km/s, which is inaccessible |
| 500 | 0.00 | 450 | |
| 566 | 0.00 | 510 | |
| 700 | 0.00 | 630 | |

**Hand check of the edge.** The maximum splitting is δ_max = μ v_max²/2. With m_Xe of about 122 GeV, the reduced mass is μ = 109.8 GeV.

- For v_max = 776 km/s, δ_max is about 368 keV.
- For v_max = 794 km/s (544 + 250 km/s), δ_max is about 385 keV.

This matches the tool, which gives events at 350 keV and none at 380 keV.

**Mass dependence.** The edge depends only weakly on mass. At delta = 380 keV, v_min for the 248 keV event is 802, 799 and 796 km/s at 1000, 1100 and 1200 GeV, all above 776 km/s.

**Consequence.** The solar-capture bound of delta > 566 keV from the literature therefore puts every solar-capture-allowed thermal higgsino beyond LZ's inelastic reach under the Standard Halo Model.

**Annual modulation.** At 1100 GeV, 350 keV and E_R = 248 keV, the tool gives:
- a fractional amplitude of 98.5%, peaking on June 2;
- 22.5% of the peak rate on the event date of September 1.

A recoil-spectrum plot for 1100 GeV and 380 keV was written to `/Users/nramachandra/github-integration/inelastic-dm-server/output/recoil_spectrum.png`. No numbered figure was produced for this report.

### The one-event splitting window

A finer scan at 1100 GeV gives:

| delta (keV) | Expected LZ events | Spectrum peak (keV) |
|---|---|---|
| 350 | 1.97 | 315 |
| 355 | 0.494 | 320 |
| 360 | 0.085 | 324 |
| 365 | 0.009 | 329 |
| 370 | 0.00 | 333 |
| 375 | 0.00 | 338 |

- **Window location.** Log-linear interpolation gives delta(N=1) = 352.5 keV and delta(N=0.3) = 356.4 keV. The window is therefore about 4 keV wide, and N falls by about 4–6 times per 5 keV.
- **Where the event becomes inaccessible.** The 248 keV event drops out between 360 and 365 keV, where v_min rises from 774 to 781 km/s.
- **Thermal mass.** At the tool's thermal mass of 1159 GeV, delta = 360 keV gives N = 0.135, against 0.085 at 1100 GeV. This moves delta(N=1) up by only about 1–2 keV.
- **Cause of the zero counts.** The zero counts at delta ≥ 370 keV come from the hard 776 km/s cutoff, not the energy window.
- **Halo dependence (not computed).** The recoil tool has no halo inputs, so halo dependence could not be computed. An analytic rescaling by (794/776)² = 1.047 would move the window to about 369–373 keV. This is a heuristic: near the edge, the count depends on how the velocity tail is populated, not only on where the edge sits.

Comparison with literature fits:

- **350 keV (arXiv:2609.01504).** Agrees with the tool directly.
- **377 keV (arXiv:2609.02608).** The offset is 24.5 keV. About 17 keV of it would be explained if that paper used a 794 km/s cutoff, but this is an assumption, not a sourced fact. The remaining roughly 5–8 keV is unexplained. Possible causes are the halo tail shape, v_E at the event date, and cross-section or efficiency normalization; none was tested.
- **339 keV (arXiv:2609.26698).** This is a normalization-free sideband-ratio optimum. With the tool's normalization, splittings this low give hundreds of events, so it is not a like-for-like comparison.

The tool therefore does not by itself account for the spread among literature fits.

### Parameter scan and constraint checker

A 17 × 17 scan covered m_χ = 800–1400 GeV and delta = 0–800 keV. It reported 144 of 289 points "viable" and 9 points predicting 0.3–5 LZ events. The best-fit point is m_χ = 988 GeV, delta = 350 keV. Output files are:

- `/Users/nramachandra/github-integration/inelastic-dm-server/output/scan_idm.npz`
- `/Users/nramachandra/github-integration/inelastic-dm-server/output/constraint_summary.png`

These numbers should not be taken as physics, for three reasons:

- The viable count uses the relic pass flag that stays true at 7–25σ.
- It uses an indirect-detection model that is wrong for a higgsino (see below).
- The best fit fits the LZ event, not the relic. At 988 GeV the tool's own relic curve gives Ω h² of about 0.087, so this point is under-abundant.

The constraint checker rated four points VIABLE: 1100 GeV with delta = 400, 566 and 1000 keV, and 1159 GeV with 400 keV. All four have N_LZ = 0.00 and no Fermi-LAT or CMB exclusion. Its present-day σv of about 7×10⁻⁴² to 5×10⁻⁴¹ cm³/s is labelled "p-wave + mass-splitting suppressed". That is inappropriate for an s-wave, Sommerfeld-enhanced higgsino, whose cross section is about 10⁻²⁶ cm³/s.

### Elastic scattering (literature only)

The XENONnT 3.1 tonne-year search (arXiv:2502.18005) reports:
- a minimum spin-independent limit of 1.7×10⁻⁴⁷ cm² at 30 GeV (90% CL);
- a best median sensitivity of 1.4×10⁻⁴⁷ cm² at 41 GeV.

The earlier 1.09 tonne-year result (arXiv:2303.14729) reached 2.58×10⁻⁴⁷ cm² at 28 GeV.

Neither abstract gives the limit at 1 TeV. The figure of about 10⁻⁴⁵ cm² is only an extrapolation using linear high-mass scaling.

XLZD (arXiv:2410.17137) reaches the neutrino fog, with 3σ evidence potential down to 3×10⁻⁴⁹ cm² at 40 GeV.

The pure-higgsino loop-level elastic cross section of about 10⁻⁴⁸–10⁻⁴⁹ cm² was not sourced. arXiv:2607.20588 places it qualitatively below the neutrino floor without giving a number.

### Indirect detection (literature only)

These findings are based on abstracts only. The full text of arXiv:2405.13104 could not be downloaded.

- **Fermi-LAT.** A 15-year line-like search comes "within an order one factor" of the sensitivity needed to detect the higgsino, for some simulated Milky Way profiles. In the same analysis, H.E.S.S. is subleading to Fermi (arXiv:2405.13104).
- **Current imaging Cherenkov telescopes.** At their ultimate sensitivity, H.E.S.S.-like instruments leave the higgsino "out of reach by at least a factor of a few". The dominant systematic is the dark-matter density in the inner Galaxy (arXiv:2210.03140).
- **H.E.S.S. Inner Galaxy Survey.** This 2026-dated, unverified paper used 546 h of data (arXiv:2608.07234). It quotes a line limit of 2.3×10⁻²⁸ cm³/s at 1 TeV for an Einasto profile and says the thermal higgsino is "probed" for the first time. Its abstract does not say whether, or for which profiles, the higgsino is excluded.
- **MAGIC.** No MAGIC-specific limit surfaced.
- **Future instruments.**
  - CTA could be the first experiment with sensitivity to the thermal higgsino (arXiv:2008.00692).
  - CTA and SWGO could detect it "at high significance" for all but the most pessimistic profiles (arXiv:2405.13104).
  - CTAO-North could reach the required sensitivity within a decade (arXiv:2506.08084).

The predicted line cross section at 1.1 TeV, and its ratio to current limits, could not be extracted.

### Literature verification status

Every arXiv-API-backed tool failed: metadata lookup, both download tools, and the metadata check inside the citation tool. They returned "not found", HTTP 429 or timeouts, even for the Planck 2018 parameters paper (1807.06209). No quote could be validated and no bibliography entry was made.

Abstract-level text was obtained through OpenAlex for:
- the LZ result (arXiv:2609.02823);
- arXiv:2403.19598;
- arXiv:2410.15733;
- arXiv:2607.20588;
- arXiv:2410.17137.

Planck overview and likelihood papers (1807.06205, 1907.12875) were found. The parameters abstract was not, so Ω_c h² = 0.120 ± 0.001 is used here as the standard value but remains unquoted.

## Discussion

Answering "where does the higgsino sit?" requires assembling three pieces.

**First, the relic target.** This is set by the literature at about 1.1 TeV, give or take about 0.1 TeV. The tool's crossing at about 1158 GeV is consistent with that only because the tool is calibrated there.

**Second, inelastic direct detection.** The xenon kinematics are robust and do not depend on the toy model. At the thermal mass, δ_max is about 368–385 keV depending on the velocity cutoff, nearly independent of mass. The sub-MeV LZ interpretation therefore requires a splitting in a narrow band just below this edge. In the tool, that band is 352–356 keV for one to 0.3 events, and lower splittings are grossly excluded.

The solar-capture bound reported in the literature (delta > 566 keV, or 0.51–0.56 MeV) lies far above this edge under the Standard Halo Model. It also lies above the roughly 480–520 keV LMC-tail values. This is why the LZ interpretation is disfavoured while the higgsino itself survives at delta of order an MeV (arXiv:2610.00226). In that regime, inelastic scattering is closed in xenon. The elastic rate is described as below the neutrino floor, although no number was sourced here.

**Third, indirect detection.** The literature consensus from abstracts is that the higgsino is within an order-one factor of current Fermi-LAT line sensitivity and is not excluded, with strong dependence on the halo profile. CTAO is the decisive future test.

The results agree with the literature on:
- the location of the xenon edge;
- the roughly 350 keV preferred splitting under a Standard-Halo-like cutoff.

They are in tension, or at least unreconciled, with:
- the 377 keV fit of arXiv:2609.02608, where 5–8 keV is unexplained even after the assumed cutoff correction;
- the 339 keV sideband optimum, which is not a comparable quantity.

Dead ends:

- **Verbatim citations.** Verbatim citation of Planck 2018 VI, arXiv:2410.15733, arXiv:2609.02823 and arXiv:2609.02775 was tried twice. Each time, the arXiv API layer returned "not found", 429 errors or internal errors, even for long-established papers. A "not found" result therefore says nothing about whether a paper exists.
- **Tool-based Sommerfeld, halo and indirect-detection studies.** These were impossible because the server has no Sommerfeld switch and no halo parameters, and its indirect-detection model is p-wave.

## Limitations

- **Relic model.** The relic calculation is a toy single-channel scaling. No Sommerfeld or coannihilation physics was computed, and no tool for it was available.
- **Halo model.** Recoil predictions use a single hard 776 km/s cutoff. Halo sensitivity, including v0, v_esc, a smooth tail and the LMC, was only estimated by an analytic rescaling. The Standard Halo Model v0 scan of arXiv:2609.15321 and the sideband analysis of arXiv:2609.26698 were not reproduced.
- **Binned counts.** Counts in the [14,225), [225,271] and (271,800] keV bins were not obtained. The tool returns integrated rates only.
- **Constraint checker.** Its relic pass flag and its indirect-detection model are unreliable. Its viability counts and "no Fermi-LAT exclusion" verdicts should be disregarded.
- **
