# The thermal pure higgsino (about 1.1 TeV) against Planck 2018, LZ 2024 and XENONnT: a literature survey

## Abstract

The task was to compute the pure-higgsino relic density at several masses with inelastic-DM tools, and to place the 1.0–1.2 TeV thermal higgsino against LZ, XENONnT and the Planck abundance. No relic-density or inelastic-DM compute tool was available in this environment. No input data were available either. **Every Omega h^2 value below therefore comes from the literature, or is a labelled rescaling of a literature value; none was computed.**

The main findings are these:

- **Relic density.** The one published pure-higgsino point found is Omega h^2 = 0.127 (perturbative) and 0.126 (Sommerfeld) in arXiv:1411.6930. The mass of about 1172 GeV attached to it is inferred from context, not stated. Rescaling that point as m^2 to the verbatim Planck 2018 value, Omega_c h^2 = 0.120 ± 0.001, gives a thermal mass of about 1.14 TeV.
- **Elastic scattering.** The most complete elastic calculation (arXiv:1912.07795) bounds the pure-higgsino spin-independent (SI) cross section below 1e-48 cm^2 at TeV masses, below the xenon neutrino floor. LZ 2024 is tightest at 40 GeV, with 2.2e-48 cm^2. A linear extrapolation to 1.1 TeV, which is an estimate and not a read value, puts the LZ limit at about 6e-47 cm^2. That is at least about 60 times above the higgsino bound.
- **Inelastic scattering.** The kinematic threshold for up-scattering on xenon is about 364–368 keV at 1.0–1.1 TeV. Recent one-loop benchmarks with splittings of 9–36 keV predict at most about one LZ event and are all allowed.

Net conclusion: a thermal pure higgsino is not excluded by current direct detection. It becomes visible only through gaugino mixing or very small neutral splittings.

## Background

A pure higgsino is an SU(2) doublet with Y = 1/2. The literature places its thermal-relic mass at roughly 1.0–1.2 TeV, with the exact value set by the Sommerfeld and coannihilation treatment:

- Beneke, Hellmann and Ruiz-Femenia, arXiv:1411.6930, give a Sommerfeld-enhanced coannihilation calculation.
- arXiv:2606.31013 quotes about 1 TeV.
- An earlier estimate, hep-ph/0610249, expected a Sommerfeld effect of about 10% for higgsinos, against about 50% for winos.
- A more recent independent framework includes bound-state formation as well as Sommerfeld enhancement (Bottaro et al., arXiv:2107.09688 and arXiv:2205.04486).
- The target abundance is from Planck 2018 (arXiv:1807.06209).

Pure-higgsino elastic scattering arises only at loop level and is suppressed by an accidental cancellation:

- Hisano et al. give the leading-order result in arXiv:1104.0228, with gluon contributions in arXiv:1007.2601.
- Chen and Hill, arXiv:1912.07795, refine it with power corrections, QCD corrections to NNNLO and chiral-EFT nuclear effects.
- arXiv:2607.20588 (2026) argues that NLO corrections can push the cross section lower, or make it vanish, in parts of MSSM parameter space.

The experimental references are:

- LZ, arXiv:2410.17036, with 4.2 tonne-years of exposure.
- XENONnT, arXiv:2303.14729.
- The ICRC 2025 review, arXiv:2510.17473, which notes that xenon experiments are entering the solar-neutrino-limited regime.

Two 2026 papers cover the visibility routes:

- **Mixing (arXiv:2606.31013).** Hamaguchi, Nagata and Osaki show that gaugino mixing raises the Higgs coupling.
- **Inelastic scattering (arXiv:2609.09830).** Chatterjee et al. compute inelastic higgsino scattering at one loop for LZ.

Both IDs were confirmed by metadata lookup.

## Results

### Planck target and the absence of a compute tool

Planck 2018 states verbatim, on page 1 of the abstract: "A combined analysis gives dark matter density Ωch2 = 0.120± 0.001" (68% CL, base ΛCDM). This value was read from the downloaded text but not added to the bibliography file.

A file listing returned an empty input set. The tool catalog contains only statistics/histogram, test-job and literature tools. The task's request to "compute the relic density" therefore could not be carried out.

### Relic density against mass

arXiv:1411.6930 (Sec. 3) reports the following:

- **Pure-higgsino model** (sfermions and heavy Higgses decoupled): Omega h^2 = 0.127 without and 0.126 with Sommerfeld enhancement, including off-diagonal rates. The net Sommerfeld effect is below 1%, because enhancement in the neutral channels cancels suppression in the neutral–charged channels.
- **Higgsino-like pMSSM point 1627006** (higgsino fraction 0.98, Δm+ = 1.8 GeV, Δm0 = 9.5 GeV): Omega h^2 = 0.108 perturbative and 0.100 with Sommerfeld, an 8% reduction.
- **Normalisation and accuracy.** The paper quotes about 5% Sommerfeld accuracy at best and normalises to Planck 2013 (0.1187 ± 0.0017).

The pure-higgsino mass of 1172.31 GeV is the mass of the pMSSM comparison point. Its attribution to the pure-higgsino numbers was inferred from context and is not stated in the paper. The critic flagged this, and it remains unconfirmed.

[[FIGURE 6]]

Figure 6 reproduces Fig. 7 of arXiv:1411.6930. It shows the yield ratio Y/Y_pert, Sommerfeld over perturbative, for the pMSSM higgsino-like point with and without off-diagonal rates, and for the pure-higgsino model. It shows the size of the Sommerfeld correction, not Omega h^2 against mass. No published Omega h^2(m) curve was found.

The table below is an m^2 rescaling of the single point (0.126 × (m/1172.31 GeV)^2). It is an interpolation, not published values, and it depends on the inferred mass.

| m (TeV) | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 |
|---|---|---|---|---|---|
| Omega h^2 (rescaled) | 0.074 | 0.092 | 0.111 | 0.132 | 0.155 |

Omega h^2 = 0.120 falls at about 1144 GeV (Sommerfeld) or 1139 GeV (perturbative), that is about 1.14 TeV.

A second, independent thermal mass was identified but not read: the doublet entry of arXiv:2205.04486. That paper also states that the Y = 1/2 doublet is the notable case that future direct detection cannot fully probe.

### Elastic SI cross section against LZ and XENONnT

**Prediction.** Hisano et al. (arXiv:1104.0228) find an SI cross section of O(1e-46–1e-48) cm^2 at leading order for pure electroweak multiplets, nearly mass-independent above about 1 TeV. The positive twist-2 terms cancel against the negative Higgs, gluon and scalar terms. The critic noted that the numeric range was not visible in the excerpts read. The calculation scans the Higgs mass and predates its measurement.

Chen and Hill (arXiv:1912.07795) state verbatim: "The upper limit for the pure doublet is less than 10^-48 cm2 in the TeV mass regime, consistent with the leading order estimate [18, 19], and lower than the estimated Xenon neutrino floor [26]." Sec. 4 adds that the bound "remains at or below 10^-48 cm2 for masses above a few hundred GeV". The same section says that with gaugino admixture c_H/g2^2 of about 0.1 the TeV rate comes within next-generation reach, and with about 0.01 it lies near the floor. These quotes were recorded, but the critic did not treat them as fully verified, and only the earlier citation entry is in the bibliography. Only an upper bound was obtained, not a central value with an uncertainty.

**Limits.** LZ 2024 gives its strongest SI exclusion as 2.2e-48 cm^2 (90% CL), with a best median sensitivity of 5.1e-48 cm^2, both at 40 GeV. No 1 TeV value was read.

**Comparison.** Comparing the 1e-48 cm^2 bound with the 40 GeV minimum gives a factor of only more than 2.2 (more than 0.34 decades). An earlier "two orders of magnitude" statement was wrong on this point and has been corrected.

At equal mass, scaling the LZ limit linearly gives 2.2e-48 × 1100/40 ≈ 6e-47 cm^2 at 1.1 TeV. That is a ratio of at least about 60 (at least about 1.8 decades) above the higgsino bound. This is an extrapolation. The XENONnT 1 TeV limit, the LZ 1 TeV curve value and a numeric neutrino-fog value were not obtained.

### Inelastic threshold and LZ inelastic sensitivity

**Threshold.** The threshold was worked out by hand:

- m_Xe = 131 × 0.9315 GeV = 122.0 GeV.
- μ_A = 108.7 GeV at 1.0 TeV and 109.8 GeV at 1.1 TeV.
- v_max = 544 + 232 = 776 km/s, so β^2 = 6.70e-6.
- δ_max = μ_A β^2/2 gives 364 keV at 1.0 TeV and 368 keV at 1.1 TeV.

The relation v_min = sqrt(2δ/μ_A) is Eq. A7 of arXiv:2609.09830. The result depends on the escape speed and Earth velocity assumed.

**Benchmarks.** arXiv:2609.09830 does not give an LZ-excluded δ_m0 range. Its five benchmarks are:

- Table III: μ = −739.63, −606.64, −814.26, 1282.11 and 1400.0 GeV; M1 = −7830, −6292, −5838, 11354 and 12875 GeV; M2 = 17055, 42000, 30925, 12627 and 12050 GeV; tan β = 10.88–26.46.
- One-loop on-shell δ = 36.37, 8.90, 16.39, 10.81 and 10.59 keV for BP1–BP5.

Table VII gives the NLO LZ event counts:

| | BP1 | BP2 | BP3 | BP4 | BP5 |
|---|---|---|---|---|---|
| Elastic | 1.0280 | 0.07729 | 0.1176 | 0.4127 | 0.5074 |
| Inelastic | 0.00022 | 0.07039 | 0.0518 | 0.1806 | 0.1661 |
| Combined | 1.02822 | 0.14768 | 0.1694 | 0.5933 | 0.6735 |
| Exposure needed (t-y) | 9.41 | 65.50 | 57.10 | 16.30 | 14.36 |

For comparison, LZ has 4.2 t-y, and the null-result criterion used is N < ln 10 ≈ 2.3. All benchmarks are consistent with LZ.

NLO vertex corrections can exceed 100%. For BP2, the NLO inelastic cross section is 0.507e-12 pb, against an LO elastic cross section of 0.284e-12 pb (ratio 1.785).

The critic noted that the table rows were not visible in the displayed excerpts, although the ranges read cover them. They are accepted on that basis.

### Splittings and mixing

**Charged–neutral splitting.** Eq. 13 of arXiv:2606.31013 gives the pure-limit radiative splitting as Δm+ ≈ (1/2) α2 MZ sin^2θW (1 − 3MZ/(2π M)). This tends to about 356 MeV for M ≫ MZ, rather than the 340 MeV in the brief.

**Higgs coupling.** Eq. 33 (approximate form of Eq. 32) gives f_q ≈ −(g^2/8M_h^2)[1/(M2−|μ|) + tan^2θW/(M1−|μ|)](1 + sgn(μ) sin 2β). This is suppressed at large gaugino mass, and at small tan β with μ < 0 through an accidental cancellation.

**Scan.** The scan in Eq. 37 covers 150 < |μ| < 1000 GeV, 1.6 < tan β < 50 and 0.5 < M1 < 10 TeV, with M2 = 2 M1. Rates are rescaled as σ_eff = (Omega_H h^2/0.12) σ (Eq. 38, micrOMEGAs v6.3.0). arXiv:2609.09830 likewise weakens its limits proportionally for sub-thermal fractions.

Direct detection is sensitive mainly where mixing produces sizable charged–neutral splittings, and in that region it reaches the about 1 TeV thermal mass. The reach figures of that paper were not extracted.

**Neutral splitting δ_m0.** The tree-level formula was not sourced. arXiv:2609.09830 refers only to "Eq. (9) of Ref. [28]" and states that the M_Z^2/M1 and M_Z^2/M2 terms can partially cancel. An earlier estimate, that same-sign M2 = 2 M1 needs M1 ≈ 1.4e7 GeV for δ < 364 keV, rests on that unsourced formula and should be disregarded. The critic noted that a same-sign tree-level splitting at about 12 TeV would be only about 0.5–0.7 MeV.

BP4 and BP5 reach about 10.6–10.8 keV with M1 and M2 both positive (about 11–13 TeV) and μ > 0. So the earlier claim that only opposite-sign gauginos give O(10) keV splittings was revised. On-shell one-loop corrections and the relative signs between μ and the gauginos also contribute.

## Discussion

The survey supports the brief's qualitative picture.

- **Thermal mass.** A thermal pure higgsino sits near 1.1 TeV. The single rescaled point gives about 1.14 TeV, inside the 1.0–1.2 TeV window. The Sommerfeld effect is negligible in the pure limit (below 1%), smaller than the earlier 10% expectation of hep-ph/0610249.
- **Elastic scattering.** The elastic SI rate is bounded below 1e-48 cm^2. By the extrapolation above, it lies roughly two decades below the current LZ reach at 1.1 TeV and below the xenon floor. Pure-higgsino elastic scattering is therefore not a viable discovery channel for current or, per arXiv:2205.04486 and arXiv:1912.07795, future xenon detectors.
- **Visibility routes.** The higgsino becomes visible through gaugino mixing, which raises f_q and the splittings (arXiv:2606.31013). It can also become visible through neutral splittings well below the about 365 keV kinematic limit. Even at 9–36 keV, however, the one-loop benchmarks of arXiv:2609.09830 give fewer than about 1.03 LZ events and need 9.4–65.5 t-y.

Two points of tension remain:

- **Splitting value.** The brief's 340 MeV charged–neutral splitting differs from the 356 MeV one-loop asymptote quoted here. The critic suggested that a two-loop value of about 341 MeV may reconcile them, but this was not read.
- **Robustness of the cancellation.** Whether the elastic cancellation is robust is unresolved. arXiv:2607.20588 suggests NLO effects can drive the rate lower still.

Dead ends:

- **Limit figures.** Figure extraction from arXiv:2410.17036 and arXiv:2303.14729 returned no limit plots, only data-distribution and calibration figures. The LZ text region read had no 1 TeV value.
- **Abstract search.** An abstract search for recent thermal-mass papers returned unrelated LEP notes. Direct arXiv-ID lookup proved more effective.

## Limitations

- **No computation.** No compute tool existed, so no relic density, event rate or reach map was computed. The m^2 table is an interpolation from one point with an inferred mass.
- **Thermal-mass spread.** Only one thermal-mass determination was available. The bound-state-inclusive value of arXiv:2205.04486 was not read, so the spread across calculations is unknown.
- **Direct-detection numbers not read.** The LZ and XENONnT limits at 1 TeV, the neutrino-fog value at 1 TeV, and next-generation projections (XLZD, arXiv:2410.17137) were not read. The headline ratio of about 60 or more remains an extrapolation.
- **δ_m0 formula.** The tree-level δ_m0 formula is unsourced.
- **Indirect detection.** Indirect detection was not addressed.
- **Bibliography.** Several quotes (Planck, the Chen and Hill passages, the Table III/VI/VII traces) are recorded on the board but not cited into references.bib.
- **Budget.** Both waves were used.

## Open directions

1. Read the Y = 1/2 doublet thermal mass and its uncertainty from arXiv:2205.04486, to give a second, bound-state-inclusive determination to compare with about 1.14 TeV.
2. Obtain the LZ 2024 and XENONnT SI limits at 1 TeV from HEPData or the remaining paper text, replacing the linear extrapolation.
3. Read the XLZD Design Book (arXiv:2410.17137) for the xenon neutrino-fog value and the projected SI sensitivity at about 1 TeV.
4. Confirm in the text of arXiv:1411.6930 which mass the pure-higgsino values 0.126/0.127 refer to.
5. Identify Ref. [28] of arXiv:2609.09830 and quote its Eq. (9), to map δ_m0 against (μ, M1, M2) with explicit sign dependence.
6. Add one sourced sentence on indirect-detection (for example H.E.S.S. Galactic Center) limits on TeV higgsinos.
7. Provide a relic-density compute tool (for example micrOMEGAs) so that Omega h^2(m) at 0.9–1.3 TeV can actually be computed.
