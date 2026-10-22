# The thermal higgsino (1.0-1.2 TeV) relative to Planck, LZ and XENONnT: relic target, elastic limits and the inelastic window

## Abstract

This study places a pure higgsino at its thermal-relic mass against current xenon direct-detection limits. It combines a literature survey with calculations from an inelastic-dark-matter tool server.

**Relic mass.** The cited literature puts the thermal mass between about 1.08 and 1.2 TeV, so a central value near 1.1 TeV is reasonable. The Planck 2018 value used is Ω_c h² = 0.120 ± 0.001. In the tool's own higgsino normalization, Ω h² reaches 0.120 at about 1159-1160 GeV.

**Elastic scattering.** The pure higgsino's loop-level spin-independent (SI) cross section is only bounded, at σ_SI ≲ 1e-48 cm². At 1.1 TeV that is at least about 33 times below the LZ 4.2 tonne-year observed limit (about 3.3e-47 cm²). It is at least about 400 times below the XENONnT 3.1 tonne-year limit (about 4.1e-46 cm²). It is also at least about 5.5 times below the xenon neutrino floor, which places it inside the neutrino fog.

**Inelastic scattering.** Z-mediated elastic scattering at zero splitting is excluded by about 7 orders of magnitude. A neutral mass splitting is therefore required. With its fixed halo, the tool gives about one LZ event only in a narrow window near δ ≈ 352 keV, and the rate closes completely by 370 keV.

**Gaugino scale.** Tree-level splittings in that window need gauginos at roughly 2 × 10⁴ TeV. At that scale, Higgs-exchange elastic scattering is negligible. On an estimate the reviewer contested, the inelastic and Higgs-exchange elastic signals appear mutually exclusive.

## Background

**Relic abundance.** A pure higgsino is an electroweak doublet. Its thermal relic abundance includes coannihilation with the charged state and the second neutral state, and Sommerfeld enhancement of the annihilation rate. The relevant literature includes:

- a pMSSM study of heavy higgsino and wino relic abundance with Sommerfeld effects (arXiv:1411.6930);
- analytic and numerical treatments of Sommerfeld-enhanced freeze-out (arXiv:1008.2905, arXiv:0910.5221).

**Cosmological reference.** The abundance is taken from Planck 2018 (arXiv:1807.06209), whose abstract gives Ω_c h² = 0.120 ± 0.001. The planning review recommended quoting the more precise form 0.1200 ± 0.0012 (TT,TE,EE+lowE+lensing). The inelastic-DM tool uses 0.12 ± 0.0012.

**Recent thermal-mass estimates (cited verbatim from their abstracts):**

| Source | Thermal mass | Notes |
|---|---|---|
| arXiv:2410.15733 | about 1.2 TeV | Abstract states that coannihilation and Sommerfeld effects are included |
| arXiv:2609.02775 (Pospelov and Ramani) | about 1.08 TeV ("cosmologically preferred") | Also derives a solar-capture bound δ > 566 keV |
| arXiv:2609.02608 (Di Mauro) | near 1.1 TeV | δ ≈ 377 keV reproduces the 248 keV LZ nuclear-recoil candidate |
| arXiv:2403.19598 (Martin) | about 100-1150 GeV | Range for higgsino-like thermal dark matter |

The solar-capture bound in arXiv:2609.02775 rests on these assumptions, as stated in its abstract:
- solar-core speeds up to about 1400 km/s;
- inelastic scattering on heavy elements;
- annihilation to WW and ZZ;
- IceCube's non-observation of high-energy neutrinos from the Sun.

A model-building context in which a roughly 1 TeV higgsino lightest supersymmetric particle saturates the relic density is given in arXiv:2302.02905.

**Direct detection: pure higgsino.** At tree level a pure higgsino's elastic SI scattering is suppressed, and it reaches xenon only through electroweak loops. Hill and Solon's heavy-WIMP effective theory (arXiv:1309.4092, arXiv:1409.8290) gives an upper bound rather than a central value. Further results:
- Chen and Hill (arXiv:1912.07795) place it below 1e-48 cm² at TeV masses.
- An NLO MSSM study (arXiv:2607.20588) finds regions where cancellations take it below 1e-50 cm².

**Direct detection: mixing and splittings.** Gaugino mixing adds Higgs exchange. The neutral splitting scales inversely with the gaugino masses (Nagata and Shirai, arXiv:1410.4549). A 2026 paper (arXiv:2609.09830) computes loop-corrected splittings and the resulting elastic and inelastic LZ rates.

**Current limits and floor.** The current xenon limits are LZ 4.2 tonne-years (arXiv:2410.17036) and XENONnT 3.1 tonne-years (arXiv:2502.18005), preceded by the first runs (arXiv:2207.03764, arXiv:2303.14729). The xenon neutrino floor is taken from O'Hare (arXiv:2109.03116), consistent with the XLZD design book (arXiv:2410.17137).

## Results

No figure in the registered list shows a computed result or a limit curve. The four extracted figures are LZ and XENONnT event-distribution and calibration plots, which add nothing to this analysis. The tool's scan figure was written to the server's output directory and was not registered.

### Relic density from the tool, and the mass target

With the higgsino option and δ = 350 keV, the tool's constraint check gives these relic densities (tension computed against 0.12 ± 0.0012):

| m (GeV) | Ω h² | Tension |
|---|---|---|
| 1080 | 0.1045 | 12.9σ |
| 1100 | 0.1083 | 9.8σ |
| 1160 | 0.1202 | 0.1σ |
| 1200 | 0.1285 | 7.1σ |

The tool's built-in higgsino cross section is ⟨σv⟩ = 2.5e-26 × (1100/m)² cm³/s, and it crosses Ω h² = 0.120 at 1159 GeV.

With the higgsino option on, the tool ignored an explicitly supplied ⟨σv⟩ and echoed its built-in value every time. The reviewer noted that this rests partly on the agent's account of what was passed, though the echoed value supports it. The cross section was therefore varied with the generic-WIMP option at m = 1100 GeV:

| ⟨σv⟩ (cm³/s) | Ω h² |
|---|---|
| 2.0e-26 | 0.1342 |
| 2.25e-26 | 0.1199 |
| 3.0e-26 | 0.0909 |

Ω scales almost exactly as 1/⟨σv⟩ (Ω × ⟨σv⟩ ≈ 0.27e-26), so Ω h² = 0.120 at 1.1 TeV needs ⟨σv⟩ = 2.25e-26 cm³/s. Under the built-in scaling Ω grows roughly as m². Consequences:

- A 10% change in ⟨σv⟩ moves the crossing mass by about 5%, or 55-60 GeV.
- Reproducing the literature masses of 1.08, 1.10 and 1.20 TeV would need effective factors of about 0.87, 0.90 and 1.07 on the tool's rate. These are relative to the tool's own normalization and are not physical Sommerfeld or coannihilation factors.
- The planning review estimated that the Planck uncertainty shifts the mass by only about ±6 GeV. That is negligible next to the 1.08-1.2 TeV spread in the literature.

Only arXiv:2410.15733 states its treatment (Sommerfeld plus coannihilation) in its abstract. The cause of the 1.08 versus 1.2 TeV spread was therefore not established. The 1.08-1.2 TeV band with a central value near 1.1 TeV is an inference from the spread of cited values, not a published result.

### Current elastic SI limits at 1.1 TeV

**LZ 4.2 tonne-years.** The paper's text gives no value at 1 TeV. The HEPData record 155182, table t1 (the data behind its Fig. 5), gives at 1008 GeV:
- an observed 90% CL limit of 3.056e-47 cm²;
- a median sensitivity of 6.834e-47 cm²;
- a scaling of roughly m^0.985 above 1 TeV.

Scaled to 1.1 TeV, these become about 3.3e-47 cm² (observed) and about 7.5e-47 cm² (median). The HEPData units were not checked against the figure.

**XENONnT 3.1 tonne-years.** The text states 3.7e-46 cm² × (M/1 TeV) above 200 GeV, which gives about 4.1e-46 cm² at 1.1 TeV.

**Time evolution.**
- XENONnT: the first run gave 6.08e-47 cm² × (M/100 GeV), about 6.7e-46 cm² at 1.1 TeV, under a more conservative median power constraint. The improvement to the current result is about 1.6 times.
- LZ: the minimum limit improved from 9.2e-48 cm² at 36 GeV to 2.2e-48 cm² at 40 GeV, about 4.2 times. The first-run LZ value at 1 TeV was not obtained.

### Higgsino cross section relative to limits and to the neutrino fog

The pure higgsino is bounded at σ_SI ≲ 1e-48 cm² at 95% CL. This bound is independent of mass in the heavy-WIMP limit (arXiv:1309.4092 Eq. 5; arXiv:1409.8290 Eq. 122). No central value exists because of strong destructive interference between the spin-0 and spin-2 amplitudes. For comparison, the pure wino is 8(+6/−3)(+3/−3)e-48 cm².

Taking the xenon SI floor as 5.0e-48 cm² at 1 TeV (about 5.5e-48 cm² at 1.1 TeV, from the O'Hare data file Xe_SI.txt), the higgsino lies at 1.1 TeV:
- at least about 33 times below the LZ observed limit;
- at least about 75 times below the LZ median sensitivity;
- at least about 400 times below the XENONnT limit;
- at least about 5.5 times below the neutrino floor.

The LZ limit itself is only about 6 times above the floor at 1 TeV. All of these ratios are lower bounds, because the higgsino cross section is itself an upper bound.

### Elastic Z exchange and the inelastic window (tool)

At δ = 0 the tool uses the higgsino Z coupling (σ_n = 7.43e-39 cm²) and predicts about 1.1e7 events in the LZ extended nuclear-recoil search, against 1 observed. The same point also fails indirect detection:
- ⟨σv⟩ today is 2.5e-24 cm³/s, against a Fermi-LAT limit of 2.3e-25 cm³/s;
- p_ann is 3.4e-28, against a CMB limit of 3.2e-28.

Expected LZ counts at m = 1100 GeV from the recoil predictor, which uses a fixed halo with v_esc + v_E = 776 km/s:

| δ (keV) | N_LZ |
|---|---|
| 200 | 5.1e4 |
| 330 | 57.7 |
| 350 | 1.97 |
| 355 | 0.49 |
| 360 | 0.085 |
| 370 | 0 |
| 390 | 0 |
| 566 | 0 |

At 370 keV the tool marks the 248 keV event as inaccessible, because v_min = 787 km/s exceeds 776 km/s. At m = 1160 GeV, N_LZ = 2.52 at 350 keV and 0.136 at 360 keV.

Log-linear interpolation puts N_LZ = 1 at δ ≈ 352 keV for 1100 GeV and about 353 keV for 1160 GeV. The window is roughly 15 keV wide and sits below the literature's 377 keV.

At δ = 350 keV the four masses give N_LZ = 1.79, 1.97, 2.52 and 2.90, all compatible with the single observed event. At those points the present-day annihilation rate is about 5e-42 cm³/s, so Fermi-LAT and CMB checks pass. The annual modulation at 1100 GeV and 350 keV has a 98.5% fractional amplitude and peaks on June 2.

A 15 × 15 scan over 1000-1200 GeV and 0-700 keV finds 210 of 225 points passing the tool's overall flag, which ignores direct detection. Fifteen points predict 0.3-5 LZ events, apparently one splitting row near 350 keV. The reported best fit (1000 GeV, 350 keV) sits on the mass edge of the scan. The scan file and figure are at /Users/nramachandra/github-integration/inelastic-dm-server/output/.

### Halo sensitivity of the window (analytic estimate, not tool output)

The kinematic endpoint is δ_max ≈ μ_N v_max²/2, with μ ≈ 110 GeV for 1.1 TeV on xenon. This gives about 368 keV at 776 km/s, consistent with the tool's closure between 360 and 370 keV. Because the endpoint scales as v_max², setting v_esc to 500 or 600 km/s would move it to about 327 or 423 keV.

The reviewer pointed out that the relevant quantity is v_min at the 248 keV event, not the overall endpoint. On that basis, 377 keV needs v_max ≳ 795 km/s, about 2.5% above the tool's value. That corresponds to v_esc ≈ 563 km/s for an assumed v_E ≈ 232 km/s, rather than the 1-2% and 555 km/s first estimated. Producing about one event, rather than a merely nonzero rate, needs more margin still. The v0 dependence was not quantified.

The conclusion that halo uncertainty can plausibly bridge 352 versus 377 keV is therefore plausible but not demonstrated. Every halo choice considered stays well below the 566 keV solar bound.

### Gaugino scale implied by the splitting

The tree-level relation is δ₀ ≈ m_Z²(s_W²/M1 + c_W²/M2) (arXiv:1410.4549 Eqs. 15 and 34). Setting M1 = M2 = M gives:

| δ (keV) | Required M (GeV) |
|---|---|
| 350 | 2.38e7 |
| 370 | 2.25e7 |
| 385 | 2.16e7 |
| 566 | 1.47e7 |

The xenon window therefore needs gauginos at about 2.2-2.4 × 10⁴ TeV, about three orders of magnitude above the 10-30 TeV initially assumed in planning. The solar bound requires M below about 1.5 × 10⁴ TeV. With wino exchange only, these values are about 22% lower. Renormalization-group running and on-shell loop corrections (arXiv:1410.4549 Eq. 35; arXiv:2609.09830 Eqs. 19-20) change them by tens of percent; the exact amount was not extracted.

### Higgs-exchange elastic scattering versus the inelastic window

Warning: the reviewer contested this result; it relies on an unverified normalization.

From the higgsino-limit coupling (arXiv:2606.31013 Eqs. 30-33; arXiv:1410.4549 Eqs. 46-49), the estimate is σ_SI ≈ 5e-46 cm² × (1 TeV/M)² × (1 + sgn μ sin 2β)². This normalization is an estimate made in this study, not a quoted value. On it:

- σ_SI reaches the LZ limit of about 3.3e-47 cm² at M ≈ 4 TeV. At that scale the splitting is about 2 GeV, so inelastic scattering is closed.
- In the inelastic window (M ≈ 2.3 × 10⁴ TeV), σ_SI is about 1e-54 cm², 7-8 orders below LZ.

The reviewer raised two objections:
- Keeping 1/(M − |μ|) rather than 1/M changes σ_SI by about a factor of 2 at M = 4 TeV.
- The tan β factor ranges from 0 to 4, which moves the LZ-reach scale anywhere from 0 to about 8 TeV.

The normalization has not been checked against a published σ_SI-versus-M curve. The qualitative conclusion is robust to these factors, because the gap is many orders of magnitude: the two signals cannot both appear.

### Tool reliability

- The tool's overall pass verdict ignores the LZ result. It reports a viable point at δ = 200 keV with N_LZ = 51158.
- The relic flag reads "consistent with Planck" even at 12.9σ and 24.2σ tension.
- The LZ check only compares expected counts with the single 248 keV event in 2.84 tonne-years.
- There is no published LZ σ_SI limit curve and no XENONnT data, so the tool's LZ treatment could not be cross-checked against arXiv:2410.17036.

None of the tool's pass flags should be read as physical viability.

## Discussion

The answer to the task is as follows. A thermal pure higgsino at about 1.1 TeV is out of reach of elastic SI searches. It sits at least an order of magnitude below the best LZ limit and inside the xenon neutrino fog. Elastic scattering will not become accessible to xenon detectors simply through more exposure. This agrees with the expectation in the survey brief and with Chen and Hill (arXiv:1912.07795).

Xenon detectors can see a higgsino in two ways:
- **Inelastic scattering**, if the neutral splitting falls within a narrow window just below the kinematic endpoint. The window is about 350-370 keV in the tool's halo, and the literature prefers about 377 keV.
- **Higgs exchange**, if gauginos are light, around a few TeV. This option is contested and normalization-dependent.

The splitting relation makes these two routes mutually exclusive.

The tool's inelastic window sits about 25 keV below the 377 keV of arXiv:2609.02608. The analytic estimate suggests that a few-percent increase in the halo's maximum speed could account for this. The reviewer's refined estimate puts the required v_max about 2.5% above the tool's value, and v0 and the shape of the distribution's tail could shift the window by several keV. The tension is therefore plausibly a halo-modelling difference, but this was not shown with a calculation.

The brief's assumed 100-200 keV cutoff for inelastic scattering is inconsistent with the computed endpoint near 370-400 keV. In the tool, δ = 200 keV gives about 5e4 events and is strongly excluded. The tool's 1160 GeV relic crossing lies within the literature band, but toward its upper end. Because the tool's relic calculation is a simple freeze-out with a fixed normalization, its crossing mass should be treated as model-dependent, not as a check of the Sommerfeld literature.

Several approaches did not work:
- **Reading the limit curves from figures.** Figure extraction returned only two non-limit figures per experiment, so the limits came from HEPData and from scaling formulas in the papers' text.
- **Citing the LZ 4.2 tonne-year paper.** The quote check failed, so its provenance rests on the arXiv ID and HEPData record 155182.
- **Testing halo variations with the tool.** The server exposes no halo parameters, so this direction was blocked.

## Limitations

- **No independent relic calculation.** No calculation with Sommerfeld effects or coannihilation was run. The tool's internal physics, such as whether it implements chargino coannihilation, is not documented, and its explicit ⟨σv⟩ input is ignored in higgsino mode.
- **Unresolved mass spread.** The 1.08-1.2 TeV spread could not be explained, because the full texts of the mass papers were not read.
- **Indirect LZ limit.** The LZ limit at 1.1 TeV comes from a HEPData point at 1008 GeV with linear scaling, and its units were not cross-checked against the pa
