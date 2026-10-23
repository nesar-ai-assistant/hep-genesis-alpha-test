# Baryonic suppression of the matter power spectrum: HACC emulator predictions at z = 0, AGN-feedback physics and weak-lensing impact

## Abstract

This report combines a literature survey of baryonic suppression of the matter power spectrum with predictions from a HACC-based hydrodynamics emulator. The emulator returns the ratio S(k) = P_hydro/P_grav, together with cluster gas fractions, over a 7-parameter design space: five AGN and black-hole parameters plus omega_m and sigma_8.

Main results from the emulator:

- At z = 0 the strongest suppression among the points sampled is 4.4 ± 0.3% at k = 1 h/Mpc and 14.8 ± 0.9% at k = 3 h/Mpc. It comes from maximal kinetic feedback, maximal e_w, kappa_w = 2 and the lowest seed mass.
- Kinetic AGN feedback produces almost all of the suppression. With the kinetic parameters set low, S(k) stays within about 1% of unity up to k = 3.7 h/Mpc.
- The suppression weakens substantially between z = 0 and z = 1. For the one point measured, it drops from 13.0% to 7.0% at k = 3 h/Mpc.
- The emulator's k-grid ends at about 12.6 h/Mpc, so the suppression minimum and any high-k upturn are not resolved.
- None of the points sampled reaches the 10 ± 2% suppression at k = 1 h/Mpc reported from eROSITA plus kSZ data. The shortfall is about 2.8 to 3.2 sigma, but this rests on literature values that have not been verified verbatim.
- Two points with very different S(k) have the same gas fraction at M500c ≈ 1.26e14 Msun/h, so the van Daalen-type relation between gas fraction and suppression is not reproduced by the pair tested.

For weak lensing, the evidence is taken from the literature rather than our own forecast:

- An Omega_m bias of -5.7 sigma arises for a Euclid-like survey when Illustris-like feedback is fitted with a one-parameter HMCode model. A theoretical-error covariance removes most of this bias.
- Reconciling DES Y3 with Planck needs A_mod = 0.858 ± 0.052. The suppression this implies at k ≈ 0.2 h/Mpc appears much larger than anything the emulator produces there.

## Background

**Physics of the suppression.** AGN feedback, with stellar feedback in lower-mass haloes, drives gas out of group- and cluster-mass haloes (about 1e13 to 1e14.5 Msun). This lowers their baryon fractions and flattens their inner mass profiles. The result is a suppression of P(k) relative to dark-matter-only runs at k ≈ 0.1–10 h/Mpc. At higher k, cooling and star formation push the ratio back up.

**Link to halo baryon fractions.** Several studies find that the suppression is set mainly by the baryon fraction of group-scale haloes:

- the van Daalen et al. library of 92 simulation power-spectrum ratios (arXiv:1906.00968);
- halo-model work tying observed gas profiles to P(k) (arXiv:1908.05765);
- a BAHAMAS/cosmo-OWLS breakdown by halo mass (arXiv:2309.06479);
- an IllustrisTNG study of which halo masses and radii matter at k > 1 h/Mpc (arXiv:2511.10634);
- the FLAMINGO resummation model, which predicts suppression from observed halo baryon fractions (arXiv:2509.04552).

FLAMINGO also studies the baryon response across feedback variants calibrated to cluster gas fractions (arXiv:2410.17109). This link makes X-ray, tSZ and kSZ observations direct probes of the suppression.

**Public modelling tools.** These include the BACCO baryonification emulator (arXiv:2011.15018), BCemu (arXiv:2108.08863), HMcode-2020 with its log10 T_AGN parameter (arXiv:2009.01858), an analytic redshift-independent formulation (arXiv:2504.15633), and the CAMELS simulation suite (arXiv:2010.00619).

**Observational constraints.**

- Siegel et al. (arXiv:2512.02954) combine eROSITA gas fractions with kSZ profiles and infer 10 ± 2% suppression at k = 1 h/Mpc. This is stronger than fiducial FLAMINGO and BAHAMAS. HSC-XXL gas fractions give 5 ± 4%.
- Grandis et al. (arXiv:2309.02920) infer 0.042 (+0.012/−0.014) at k = 1 h/Mpc and 0.184 (+0.026/−0.031) at k = 3 h/Mpc from cluster gas and stellar fractions. They predict a change of less than 1% for k < 0.37 h/Mpc at 97.5% credibility.

Neither set of numbers has yet been checked against the full text; both come from abstract-level reading.

**Weak lensing.** Ignoring these scale-dependent changes biases S8 (arXiv:1105.1075). Feedback is also degenerate with neutrino mass (arXiv:1407.4301). Amon and Efstathiou (arXiv:2206.11794) and Preston, Amon and Efstathiou (arXiv:2305.09827) model P_m = P_L + A_mod (P_NL − P_L). They argue that stronger-than-standard nonlinear suppression can reconcile cosmic shear with Planck. Further evidence for strong feedback is cited in arXiv:2602.02484.

Mitigation strategies in the literature are:

- scale cuts;
- marginalising over baryonic parameters;
- theoretical-error covariances (arXiv:2410.12500);
- external SZ, kSZ or FRB constraints (arXiv:2301.02186, arXiv:2401.03510, arXiv:2501.17922).

## Results

### Emulator configuration

The Pk-ratio emulator has these properties:

- **Redshifts:** trained at z = 0, 0.1, 0.5, 1.0 and 2.0.
- **k-grid:** 799 bins from 0.022 to about 12.6 h/Mpc. The k units are h/Mpc according to the file headers.
- **Parameter bounds:**

| Parameter | Range |
|---|---|
| kappa_w | 2–4 |
| e_w | 0.2–1.0 |
| M_seed | 0.6–2.0 (units of 1e6 Msun) |
| v_kin | 0.1–1.2 |
| eps_kin | 0.02–1.2 |
| omega_m | 0.12–0.155 |
| sigma_8 | 0.7–0.9 |

- **Reference spectrum:** the ratio is taken relative to P_grav, a gravity-only run. Whether this is equivalent to the P_DMO used in the literature has not been checked.

All parameter points below lie within these bounds. Their full parameter labels, read from the prediction-file headers, are:

| Point | kappa_w | e_w | M_seed | v_kin | eps_kin |
|---|---|---|---|---|---|
| fiducial | 3 | 0.6 | 1.3 | 0.65 | 0.61 |
| strongAGN | 3 | 1.0 | 1.3 | 1.2 | 1.2 |
| weakAGN | 3 | 0.2 | 1.3 | 0.1 | 0.02 |
| maxsupp | 2 | 1.0 | 2.0 | 1.2 | 1.2 |
| maxsupp_lowkin | 2 | 1.0 | 2.0 | 0.1 | 0.02 |
| maxsupp_lowM | 2 | 1.0 | 0.6 | 1.2 | 1.2 |

Every file header lists omega_m = 0.14 and sigma_8 = 0.8, so the cosmology axes were never varied.

### Pk-ratio at z = 0 for the sampled feedback points

**maxsupp (combined extreme corner).** S(k) at z = 0:

| k (h/Mpc) | S(k) |
|---|---|
| 0.101 | 0.99944 ± 0.00003 |
| 0.510 | 0.9868 ± 0.0008 |
| 1.013 | 0.9638 ± 0.0020 |
| 2.002 | 0.9179 ± 0.0045 |
| 3.007 | 0.8698 ± 0.0065 |
| 3.698 | 0.8400 ± 0.0076 |
| 4.00 | 0.8284 ± 0.0079 |
| 5.00 | 0.7942 ± 0.0089 |
| 6.0 | 0.7680 ± 0.0095 |
| 7.01 | 0.7479 ± 0.0100 |
| 7.84 | 0.7356 |

This is 3.6 ± 0.2% suppression at k = 1 and 13.0 ± 0.7% at k = 3 h/Mpc.

**maxsupp_lowM (M_seed = 0.6).** Lowering the seed mass from 2.0 to 0.6 deepens the suppression:

| k (h/Mpc) | S(k) |
|---|---|
| 0.212 | 0.9967 |
| 0.510 | 0.9835 ± 0.0011 |
| 1.013 | 0.9557 ± 0.0029 |
| 2.002 | 0.9026 ± 0.0064 |
| 3.007 | 0.8521 ± 0.0094 |
| 3.698 | 0.8228 ± 0.0109 |

This is 4.4 ± 0.3% at k = 1 and 14.8 ± 0.9% at k = 3 h/Mpc, the largest suppression among the sampled points. It is not shown to be the maximum over the design range.

**maxsupp_lowkin (kinetic parameters at minimum).** This point shows essentially no suppression:

| k (h/Mpc) | S(k) |
|---|---|
| 0.212 | 1.0002 |
| 0.510 | 1.0004 ± 0.0007 |
| 1.013 | 1.0006 ± 0.0019 |
| 2.002 | 1.0033 ± 0.0042 |
| 3.007 | 0.9972 ± 0.0062 |
| 3.698 | 0.9883 ± 0.0071 |

In this emulator, v_kin and eps_kin therefore drive almost all the suppression up to k ≈ 3.7 h/Mpc, even with e_w at its maximum.

**fiducial versus strongAGN.** The S(k) values are:

| Point | k = 1.01 | k = 3.01 | k = 3.70 |
|---|---|---|---|
| fiducial | 0.9779 | 0.9197 | 0.8984 (std 0.004) |
| strongAGN | 0.9746 | 0.9121 | 0.8909 |

Raising the kinetic parameters and e_w at kappa_w = 3 therefore adds only about 0.3–0.8 percentage points of suppression over this range. These values come from an earlier run on this thread and were not independently re-verified in the present run.

**strongAGN beyond k = 3.7 h/Mpc.** S(k) continues to fall:

| k (h/Mpc) | S(k) |
|---|---|
| 5.25 | 0.851 |
| 7.01 | 0.8205 |
| 10.01 | 0.7946 (std 0.0098) |
| 12.55 | 0.7893 |

Between about 11.6 and 12.6 h/Mpc it flattens to a plateau of about 0.789–0.790, falling by less than 0.001 per 0.1 h/Mpc at the edge.

Two cautions apply to the high-k behaviour:

- The ratio has no upturn within the grid. The minimum is at or beyond k_max ≈ 12.6 h/Mpc, with a depth of about 21% for strongAGN.
- maxsupp is already at 0.7356 by k = 7.84, deeper than the strongAGN plateau. Its minimum is unresolved.

The k_max and plateau values come from byte offsets, and the final rows of the file were not quoted verbatim. They should be treated as approximate.

### Redshift evolution, z = 0 to z = 1

For maxsupp the suppression weakens strongly towards z = 1:

| k (h/Mpc) | S at z = 0 | S at z = 1 | Suppression, z = 0 to z = 1 |
|---|---|---|---|
| 1.013 | 0.9638 ± 0.0020 | 0.9781 ± 0.0018 | 3.6% to 2.2% |
| 3.007 | 0.8698 ± 0.0065 | 0.9299 ± 0.0055 | 13.0% to 7.0% |
| 3.70 | 0.8400 ± 0.0076 | 0.9214 ± 0.0064 | 16.0% to 7.9% |

Qualitatively, this matches the FLAMINGO statement that the response grows as z falls (arXiv:2410.17109). That comparison has not been checked against the FLAMINGO text. The ratio is still falling at k = 3.7 at both redshifts, so any shift of the minimum with redshift could not be measured.

[[FIGURE 28]]

Figure 28 plots the emulator Pk-ratio at z = 0 and z = 1 for the fiducial and maxsupp points. Only the maxsupp values in the table above were read out numerically. The fiducial z = 1 prediction was written but not read, so no quantitative z-trend is claimed for the fiducial point.

A planned companion plot of the four z = 0 variants was overwritten by this one, because the two plotting calls shared an output path.

### Gas fraction versus suppression

The fGas emulator gives M_gas/M500c inside R500c at z = 0 in three M500c bins: 5.01e13, 7.94e13 and 1.26e14 Msun/h.

| Point | f_gas at 1.26e14 Msun/h | f_gas at 7.94e13 Msun/h |
|---|---|---|
| fiducial | 0.1214 ± 0.0010 | 0.1090 |
| strongAGN | 0.1221 ± 0.0019 | 0.1098 |
| weakAGN | 0.1414 ± 0.0023 | 0.1375 |

Only fiducial and strongAGN have S(k) values to pair with these gas fractions. Their f_gas values agree within errors, with strongAGN nominally higher, yet strongAGN is 0.3–0.8 points more suppressed. This pair therefore shows no resolvable van Daalen-type relation (arXiv:1906.00968), and the nominal trend runs the wrong way.

The comparison has two weaknesses:

- It is confounded, because e_w changes together with the kinetic parameters.
- It is limited, because the weakAGN S(k) was never read. weakAGN has a markedly higher gas fraction, so it is the point that would make a three-point test meaningful.

One physical reading of the pair is that the emulator's suppression is driven by gas removed beyond R500c, or by haloes of other masses, rather than by the R500c gas fraction. This is untested.

### Comparison with observational suppression estimates

Errors are combined in quadrature, taking the published error on the side facing the emulator value. For maxsupp:

| Constraint | Gap |
|---|---|
| Grandis et al., k = 1 | 0.4 sigma (4.2% vs 3.6%) |
| Grandis et al., k = 3 | 1.7 sigma (18.4% vs 13.0%) |
| eROSITA + kSZ, k = 1 | 3.2 sigma short (10% vs 3.6%) |
| HSC-XXL, k = 1 | 0.35 sigma |

An earlier pass quoted about 3 and 8 sigma against Grandis et al. Those figures used emulator error alone and are superseded.

The strongest point, maxsupp_lowM, is:

- about 2.8 sigma short of eROSITA + kSZ;
- consistent with HSC-XXL and with Grandis et al. at k = 1;
- 3.6 points below Grandis et al. at k = 3.

All of these significances depend on literature values that have not been confirmed verbatim. They are also tested only at the kappa_w = 2, e_w = 1 corners with fixed cosmology.

### Weak-lensing impact (literature-based)

**Omega_m bias from ignoring or mis-modelling baryons.** Maraio, Hall and Taylor (arXiv:2410.12500, Table 3, read verbatim) consider an idealised Euclid-like Stage-IV cosmic-shear survey with ell_max = 5000:

| Ground truth | Model | 100 ΔΩ_m | Significance |
|---|---|---|---|
| Illustris | one-parameter HMCode, no theory error | −1.317 | −5.69 sigma |
| Illustris | same, with theoretical-error covariance | 0.128 | 0.249 sigma |
| Bahamas | one-parameter HMCode | 0.057 | 0.258 sigma |
| Eagle | six-parameter model, with theory error | 0.573 | 1.459 sigma |

The text adds two statements:

- The one-parameter model without theory error gives "at least a 3 sigma offset in either Omega_m or S8 for all hydro-sims excluding Bahamas".
- With Simba as ground truth, even ell_max = 1000 is biased by more than 2 sigma in all parameters.

The ΔS8 values are in that paper's Table 4, which was not read. This bias is therefore an Omega_m bias, not an S8 bias.

**Suppression needed to reconcile lensing with Planck.**

- For DES Y3, A_mod = 0.858 ± 0.052, with no scale cuts and a Planck prior (arXiv:2305.09827, Eq. 3). The suppression must extend to k ~ 0.2 h/Mpc.
- For KiDS-1000, A_mod ≈ 0.69 (arXiv:2206.11794).
- Without A_mod, DES Y3 S8 lies 0.9–1.8 sigma below Planck S8 = 0.828 ± 0.016, depending on analysis variant.

**Comparison with the emulator.** For maxsupp, S(k) is 0.9994 at k = 0.10 and 0.987 at k = 0.51 h/Mpc. The value at k ≈ 0.2 h/Mpc was not read but presumably lies below a 1% effect. For maxsupp_lowM the read value at k = 0.212 is 0.9967.

Emulator-level feedback therefore agrees with the Grandis et al. bound of less than 1% for k < 0.37 h/Mpc. It appears far weaker than A_mod = 0.86 or 0.69 would require at these scales. This is a qualitative comparison, because no A_mod-equivalent number was computed for any emulator point.

### Bibliographic and data products

Validated citation entries for arXiv:2305.09827, arXiv:2410.12500, arXiv:2512.02954 and arXiv:2309.02920, each with a verbatim abstract quote, were written to `runs/261023_143127/references.bib`.

Full texts of FLAMINGO (arXiv:2410.17109), Siegel et al. (arXiv:2512.02954) and Grandis et al. (arXiv:2309.02920) were downloaded to `runs/261023_143127/` as `.txt` files. They have not yet been read.

## Discussion

**Feedback physics in the emulator.** Within this emulator, the kinetic AGN mode is the lever on S(k). Switching it off removes almost all suppression even at maximum e_w. Lowering the seed mass, and plausibly lowering kappa_w (not isolated, because M_seed also changed), deepens it.

This is consistent with the general picture of AGN-driven gas expulsion from group-scale haloes. However, the emulator does not show the expected anti-correlation between the gas fraction inside R500c at about 1e14 Msun/h and the suppression. Possible reasons:

- the relevant gas is pushed beyond R500c;
- other halo masses dominate;
- the two-point comparison is simply too confounded to show it.

The literature (arXiv:1906.00968, arXiv:2509.04552, arXiv:2309.06479) predicts a clear relation, so this is a real tension worth resolving with the unread weakAGN curve and single-parameter sweeps.

**Size of the suppression.** The emulator's largest sampled suppression at k = 1 h/Mpc, 4.4%, agrees with HSC-XXL and Grandis et al. It falls short of the strong-feedback eROSITA + kSZ inference. At k = 3 h/Mpc it is below Grandis et al.

Three explanations are open:

- the design range may not span the strongest feedback now favoured observationally;
- the cosmology axes, untouched here, may shift the response through the baryon fraction and halo abundance;
- the P_grav reference may differ from P_DMO.

**Weak lensing.** The literature
