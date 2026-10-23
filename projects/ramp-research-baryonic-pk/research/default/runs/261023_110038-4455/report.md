# Baryonic suppression of the matter power spectrum: HACC emulator predictions at z = 0 and z = 1, and what they mean for weak lensing

## Abstract

This report combines a literature survey on how baryonic feedback suppresses the matter power spectrum with new predictions from a CRK-HACC hydrodynamics emulator. The survey brief said no emulator was available. That was wrong: a HACC hydro emulator was connected during the session and offers a `Pk-ratio` observable, S(k) = P_hydro/P_DMO.

The emulator was evaluated at z = 0 for three AGN-feedback settings, called weak, fiducial and strong:

- **Fiducial point.** S reaches 0.99 at k ≈ 0.59 h/Mpc and 0.95 at k ≈ 2.11 h/Mpc. S(k=1 h/Mpc) = 0.979 ± 0.001.
- **Fiducial, high k.** S keeps falling monotonically to 0.791 ± 0.006 at k = 11.27 h/Mpc, which is close to the emulator's maximum k. Neither a minimum nor a high-k upturn was found.
- **Strong point.** It adds only about 0.4% more suppression at k = 1.
- **Weak point.** It shows no suppression; S rises to about 1.011 near k ≈ 2.4 h/Mpc.

Two physical trends appear in the emulator:

- **Gas fraction.** A lower cluster gas fraction goes with stronger suppression at k ≈ 1 h/Mpc. This qualitatively matches the halo-baryon-fraction picture in the literature.
- **Redshift.** Suppression weakens and moves to higher k between z = 0 and z = 1.

For weak lensing, the assessment rests on sourced literature numbers only. KiDS-1000 S8 is about 9% below Planck. Matching Planck would require a nonlinear-power modulation A_mod ≈ 0.69. FLAMINGO concludes that baryons are unlikely to drive the required modification. No S8 bias was computed from the emulator curves.

## Background

**Shape of the response.** The survey brief summarises a consistent picture across several simulation suites: OWLS/cosmo-OWLS/BAHAMAS (arXiv:1105.1075, arXiv:2309.06479), Horizon-AGN (arXiv:1801.08559), IllustrisTNG/CAMELS (arXiv:2511.10634, arXiv:2301.02231) and FLAMINGO (arXiv:2410.17109). In that picture:

- there is a small boost at k < 0.1 h/Mpc;
- suppression begins at k ~ 0.1–0.3 h/Mpc;
- the minimum is roughly 10–30% deep at k ~ 5–20 h/Mpc;
- S(k) turns up at higher k, where stars and cooled gas concentrate matter.

**Physical mechanism.** AGN feedback, in thermal or kinetic/jet form, expels gas from groups and clusters of about 10^13–10^14.5 Msun/h beyond the virial radius. This lowers their baryon fractions and makes their profiles shallower. arXiv:2309.06479 identifies "group-sized haloes" as the important contributors. FLAMINGO arXiv:2410.17109 states that "lower gas fractions in groups and clusters lead to a stronger response".

This link to gas fractions underlies empirical predictors that work from cluster f_gas and f_star (arXiv:2309.02920, arXiv:2509.04552, arXiv:2409.05716). FLAMINGO's strongest-feedback response, which is compatible with some lensing-plus-external analyses, is "in strong tension with the X-ray inferred gas fractions" (arXiv:2410.17109). The Astrid simulation finds "no significant suppression at z = 0" and a suppression "weaker than in other state-of-the-art simulations" (arXiv:2605.04176).

**Weak lensing.** Amon and Efstathiou (arXiv:2206.11794) argue that KiDS-1000 can be reconciled with Planck if the matter power is "suppressed more strongly on non-linear scales than" usually assumed. Preston et al. (arXiv:2305.09827) find that for DES Y3 the required suppression "is not as strong as inferred using KiDS data". They also find it "is still more extreme than predictions from recent numerical simulations".

FLAMINGO (arXiv:2309.07959) concludes that some mechanism must slow late-time or nonlinear growth, "but that it is unlikely that baryon physics is driving this modification". Several other analyses point to relatively strong but still uncertain feedback:

- DES Y3 small-scale analyses (arXiv:2303.05537, arXiv:2206.08591);
- joint X-ray, tSZ and kSZ fits (arXiv:2110.02228, arXiv:2109.04458);
- kSZ + X-ray + galaxy-galaxy lensing work (arXiv:2512.02954).

For Stage IV surveys, the suppression must be modelled at the percent level up to k ~ 10 h/Mpc, or else marginalised over.

**Available emulators.** BACCO (arXiv:2011.15018), BCemu (arXiv:2108.08863) and syren-baryon (arXiv:2506.08783) were not available in this session.

## Results

### The emulator

The connected HACC emulator is a Gaussian process trained on CRK-HACC hydrodynamical runs. It has 7 parameters:

| Parameter | Description | Range |
|---|---|---|
| kappa_w | AGN wind coupling | 2–4 |
| e_w | AGN energy efficiency | 0.2–1.0 |
| M_seed | Black-hole seed mass | 0.6–2.0 × 10^6 Msun |
| v_kin | Kinetic AGN velocity | 0.1–1.2 × 10^4 km/s |
| eps_kin | Kinetic AGN efficiency | 0.02–1.2 × 10 |
| omega_m = Omega_m h^2 | Cosmology | 0.12–0.155 |
| sigma_8 | Cosmology | 0.7–0.9 |

Other properties:

- **Pk-ratio output.** 799 k bins starting at k = 0.022 h/Mpc, trained at z = 0, 0.1, 0.5, 1 and 2.
- **fGas output.** Gives M_gas/M500c within R500c in only 3 M500c bins.
- **No baryon-fraction parameter.** There is no Omega_b parameter, so the dependence of S(k) on Omega_b/Omega_m cannot be tested with this tool.

Two cosmologies were used:

- **Set A:** omega_m = 0.142, sigma_8 = 0.81.
- **Set B:** omega_m = 0.1375, sigma_8 = 0.80.

They are reported separately below. The fiducial S(3.7) differs between them, 0.901 in Set A versus 0.892 in Set B. This gives an informal sense of the size of the cosmology dependence.

All runs held kappa_w = 3 and M_seed = 1.3 fixed. The three AGN settings were:

| Setting | e_w | v_kin (km/s) | eps_kin | Location in design |
|---|---|---|---|---|
| Weak | 0.2 | 1000 | 0.2 | Lower edges |
| Fiducial | 0.6 | 6500 | 6.1 | Mid-design |
| Strong | 1.0 | 12000 | 12 | Upper edges |

### z = 0 suppression curves (cosmology Set A)

[[FIGURE 36]]

Figure 36 overlays the three z = 0 emulator curves.

On large scales all three are close to unity. At k = 0.086 h/Mpc the CSVs give:

- fiducial S = 0.99986;
- strong S = 0.99981;
- weak S = 1.00014.

The weak point therefore shows a boost of about 1.4 × 10^-4. This is the sign of boost that the literature describes, but it is negligible in size. Below 1% suppression persists out to k ≈ 0.5–0.6 h/Mpc for all points. In particular, k = 0.2 h/Mpc lies inside the sub-1% regime; no value at that k was read directly.

Each GP uncertainty below is 1σ.

| Point | k(1%) [h/Mpc] | k(5%) [h/Mpc] | S(k=1) | S(k=3.7) |
|---|---|---|---|---|
| Weak | — | — | 1.003 ± 0.003 | 1.004 ± 0.011 |
| Fiducial | 0.59 | 2.11 | 0.979 ± 0.001 | 0.901 ± 0.004 |
| Strong | 0.53 | 1.86 | 0.975 ± 0.002 | 0.892 ± 0.007 |

The weak point never drops below 1. It peaks at about 1.011 ± 0.007 near k ≈ 2.4 h/Mpc.

The response to the AGN parameters is strongly nonlinear. Almost all of the change happens between the weak and fiducial points. The strong point adds only about 0.4% at k = 1, which is roughly 2σ of the combined GP uncertainty.

The weak-point boost and the strong-point saturation both sit at corners of the design space. They may be edge or extrapolation artifacts. Inside-bound reruns were made to test this:

- weak-in: e_w = 0.24, v_kin = 1550 km/s, eps_kin = 0.8;
- strong-in: e_w = 0.96, v_kin = 11450 km/s, eps_kin = 11.4.

These reruns have not been read or compared.

### High-k behaviour of the fiducial curve

The full fiducial CSV extends well past the k ≈ 3.7 h/Mpc cut-off of the first file reader. Rows read from the file:

| k [h/Mpc] | S |
|---|---|
| 7.45 | 0.8214 ± 0.0055 |
| 9.006 | 0.8044 ± 0.0057 |
| 10.01 | 0.7970 ± 0.0058 |
| 11.27 | 0.7910 ± 0.0059 |

The curve falls steadily throughout this range. So within the emulator range, which ends at k_max ≈ 11.3 h/Mpc (the exact last row was not read), there is:

- no suppression minimum;
- no high-k upturn from cooling and star formation.

S_min and k_min can only be stated as limits: S_min < 0.791 and k_min > 11.27 h/Mpc for this point. S(k=5) was not extracted. The strong and weak curves were not read beyond k ≈ 3.7 h/Mpc.

### Gas fraction against suppression (cosmology Set B, z = 0)

This analysis uses the same three AGN settings as above.

| Point | f_gas at M500c = 7.94e13 Msun/h | f_gas at 1.26e14 | S(k=1.013 h/Mpc) |
|---|---|---|---|
| Weak | 0.1396 ± 0.0024 | 0.1438 | 1.0022 ± 0.0025 |
| Fiducial | 0.1099 ± 0.0011 | 0.1229 | 0.9766 ± 0.0010 |
| Strong | 0.1111 ± 0.0020 | 0.1237 | 0.9733 ± 0.0018 |

From weak to fiducial, f_gas at 7.94e13 Msun/h drops by about 0.03. Over the same step, 1 − S(1) moves from about −0.002 to about 0.024. This matches the literature's expectation that lower group and cluster gas fractions give a stronger response.

The relation fails between the fiducial and strong points. Their f_gas values agree within 1σ, and the strong point is actually slightly higher in every mass bin (for example 0.0985 versus 0.0956 at 5.0e13 Msun/h). Yet the strong point suppresses about 0.3% more. With only three points this is a trend direction, not a fitted slope. The non-monotonic f_gas also supports the concern that the strong corner may be GP-extrapolated.

### Redshift evolution, z = 0 to z = 1 (cosmology Set B)

| Point | z | S(k=1.013) | S(k=3.71) | k(1%) [h/Mpc] | k(5%) [h/Mpc] |
|---|---|---|---|---|---|
| Fiducial | 0 | 0.9766 | 0.8924 | ~0.55 | ~1.92 |
| Fiducial | 1 | 0.9848 ± 0.0010 | 0.9458 | ~0.78 | ~3.09 |
| Strong | 0 | 0.9733 | 0.8852 | ~0.51 | ~1.74 |
| Strong | 1 | 0.9881 ± 0.0016 | 0.9620 ± 0.0057 | ~0.90 | not reached for k < 3.73 |

Between z = 0 and z = 1, suppression weakens and its onset moves to higher k. At z = 1 the strong curve flattens near 0.962 over k = 3.4–3.7 h/Mpc. It then suppresses less than the fiducial curve, so the z = 0 ordering reverses.

The k crossings were read from neighbouring CSV rows, so they are approximate. z = 0.5 was not run, and no plots were made for this analysis.

### Weak-lensing numbers from the literature

These values were read from the paper texts; only the "about 9% lower than the Planck value" phrase passed citation validation.

| Quantity | Value | Source |
|---|---|---|
| KiDS-1000 cosmic-shear S8 | 0.759 (+0.024/−0.021) | arXiv:2206.11794 |
| Planck TTTEEE+Plens S8 | 0.829 ± 0.012 | arXiv:2206.11794 |
| Discrepancy | about 9%, ~2.4–2.7σ | arXiv:2206.11794 |
| DES Y3 cosmic-shear S8 | 0.772 (+0.018/−0.017) | arXiv:2305.09827 |
| Nonlinear-power modulation for Planck to fit KiDS shear | A_mod ≈ 0.69 | arXiv:2305.09827 eq. 1 |
| Extent of suppression needed for DES Y3 | to k ~ 0.2 h/Mpc | arXiv:2305.09827 |

These numbers bound how large a small-scale suppression would need to be to shift S8. They are not a direct "S8 bias from ignoring baryons", and no such number was extracted.

The FLAMINGO text (arXiv:2410.17109) gives no numerical S(k) values for its fiducial or fgas-8σ models; these appear only in its Fig. 11. The text does state:

- the fgas-8σ thermal and jet models resemble cosmo-OWLS with ΔT_AGN = 8.3 and 8.5;
- only Illustris and cosmo-OWLS 8.7 lie beyond the reach of its emulator;
- that emulator is accurate to better than 1% up to k = 10 h/Mpc;
- the cosmology dependence is about 1%.

## Discussion

**Agreement with the literature.**

- The fiducial and strong HACC curves agree qualitatively with the picture in the literature: negligible change at k < 0.1 h/Mpc, percent-level suppression from k ~ 0.5 h/Mpc, and roughly 20% suppression by k ~ 10 h/Mpc.
- The weak corner, with essentially no suppression, is qualitatively like the Astrid result (arXiv:2605.04176).
- The f_gas–suppression trend from weak to fiducial matches FLAMINGO's statement that lower gas fractions give a stronger response.
- The redshift trend (weaker, higher-k suppression at z = 1) is consistent with feedback effects building up at late times.

**Points of tension.**

- *Saturation at high feedback.* The strong point barely differs from the fiducial point, while f_gas does not decrease between them. This could be a real saturation of the CRK-HACC feedback model, or it could be GP behaviour at the edge of the design space. The pending inside-bound comparison is the deciding test.
- *Can HACC reach strong FLAMINGO-like responses?* If the saturation is real, it bears on whether HACC's AGN ranges can reproduce fgas-8σ-like responses. That question is still open, because no FLAMINGO numbers could be placed next to the HACC values.
- *Earlier qualitative comparisons.* Earlier comparisons to "OWLS AGN S(1) ~ 0.90" and to BCemu or FLAMINGO minima were not sourced from cited values. They should be treated as qualitative at most.
- *Mapping between models.* The HACC parameters do not map onto BACCO M_c or FLAMINGO variants. Any bracketing across models is qualitative.
- *Missing minimum and upturn.* Within k ≤ 11.3 h/Mpc the fiducial curve has neither a minimum nor an upturn. This is consistent with the literature placing the minimum at k ~ 5–20 h/Mpc. Within this range it cannot confirm the cooling upturn.

**Implications for weak lensing.** Without a projection code, the quantitative S8 statement rests on the literature. A_mod ≈ 0.69 for KiDS, and a suppression extending to k ~ 0.2 h/Mpc for DES Y3, are far stronger than any HACC point gives at k ≲ 0.5 h/Mpc, where all points stay within 1%. The HACC results therefore side with FLAMINGO and Preston et al.: within this model, baryonic feedback on its own does not look sufficient to remove the S8 tension.

This is a qualitative inference. It was not derived by combining the emulator S(k) with the quoted numbers.

**Dead ends.**

- **Table loading.** `load_table_data` cannot parse the emulator CSVs, which begin with `#` comment lines and an `x,y_mean,y_std` header. `read_text_file` truncates them at k ≈ 3.7 h/Mpc. Reading by character offset with `read_arxiv_chunk` works.
- **Citation validation.** Long quotes containing Greek letters, subscripts or special symbols failed validation, probably because of PDF ligatures and lost spaces. Short ASCII fragments passed.
- **Plots.** The gas-fraction and redshift-evolution comparison plots were never made before the budget ran out.

## Limitations

- **Budget.** The run stopped after two waves of its budget.
- **High-k gaps.** S(k=5) was not read for any point. The strong and weak curves were not read beyond k ≈ 3.7 h/Mpc. The exact k_max was not read.
- **Edge-artifact test incomplete.** The inside-bound runs exist but were not analysed, so the weak boost and strong saturation are not classified in units of GP σ.
- **Mixed cosmologies.** Two cosmology sets were used. The z = 0 table and the f_gas/redshift tables are therefore not strictly comparable.
- **No Omega_b dependence.** The Omega_b/Omega_m dependence cannot be studied with this emulator.
- **No lensing projection.** No Limber or C_ell code was available, so no S8 bias or fractional C_ell change was computed. None was extracted from arXiv:1105.1075, arXiv:2303.05537 or arXiv:2206.08591, because these were not read.
- **FLAMINGO curves not extracted.** Numerical FLAMINGO S(k) values were not obtained, since its Fig. 11 was not digitised.
- **Validation status.** The emulator results and several literature numbers were not independently verified beyond the tool outputs. The critic contested most quantitative findings pending these checks.
- **Execution.** No HPC facility was used.

## Open directions

1. Read the inside-bound weak and strong CSVs and the rest of the z = 0 curves by character offset to obtain S(k=5) and the exact k_max, and to decide whether the weak boost and strong saturation exceed the GP uncertainty.
2. Extract numerical fiducial and fgas-8σ S(k) values from Fig. 11 of arXiv:2410.17109, and read arXiv:2303.05537 and arXiv:2206.08591 for a quoted S8 shift from including small scales.
3. Add a coding tool to Limber-project the HACC S(k) into a cosmic-shear C_ell and estimate the S8 shift from ignoring baryons, in the spirit of arXiv:2206.11794.
4. Redo the f_gas, z = 0.5 and z = 1 runs in a single harmonised cosmology and produce the missing comparison plots.
5. Connect BACCO, BCemu or syren-baryon to test the Omega_b/Omega_m dependence that the HACC emulator cannot vary.

```json
{"open_directions": [
 {"direction_id": "d-10", "goal": "Read inside-bound d10 CSVs and remaining d07 rows (S(k=5), exact k_max, strong/weak high-k) via read_arxiv_chunk and classify weak boost / strong saturation in GP sigma", "why": "Corner points may be GP edge artifacts; S_min/k_min and S(k=5) remain unmeasured"},
