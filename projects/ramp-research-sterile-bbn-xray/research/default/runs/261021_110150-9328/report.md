# Sterile-neutrino dark matter in 2024-2026: combined BBN and X-ray viability of the (m_s, sin^2 2θ) plane

## Abstract

This study surveyed recent arXiv work on keV sterile-neutrino dark matter. It combined tool-computed BBN observables (Yp, D/H, ΔN_eff) with published X-ray decay-line limits to identify which (m_s, sin^2 2θ) regions remain viable.

**BBN is not a useful constraint on keV dark matter without a lepton asymmetry.**
- Along the non-resonant Dodelson-Widrow (DW) dark-matter line, ΔN_eff is between 1e-4 and 1.1e-2, and the BBN Δχ^2 relative to the Standard Model is below 0.15.
- The overclosure bound is 40 to about 5000 times stronger than BBN over 1-100 keV.

**DW production cannot supply all of the dark matter.**
- X-ray limits exclude it. These are NuSTAR, quoted as sin^2 2θ ≲ 1e-12 at 6-40 keV, and INTEGRAL/SPI, quoted as ≲ 3e-14 above 40 keV.
- Structure formation independently excludes the masses where DW could otherwise survive.
- At 7.1 keV the XRISM-only verdict depends on which DW relic normalization is used. The server's normalization differs from the published fit by a factor of 10-17 in mixing.

**What survives requires non-oscillation production or very small mixing.**
- Shi-Fuller resonant production with a lepton asymmetry L ≳ 0.5 at T > 20 MeV is quoted as viable at m_s ≳ 10 keV and sin^2 2θ ≲ 1e-14 (arXiv:2507.18752). The available server cannot test this: it caps L at 0.1.
- Flavor-dependent asymmetries and reheating production open further regions. Those claims rest on abstracts only.

## Background

The main recent combined analysis is Vogel, Garcia Escudero, Froustey and Abazajian (arXiv:2507.18752, 2025), who revisit Shi-Fuller resonant production. The full text was read, and states:
- "lepton asymmetries L≳0.5 at high temperatures open significant viable parameter space in the m_s≳10 keV and sin^2(2θ)≲10^-14 regime".
- That region is compatible with NuSTAR ("sin^2(2θ)≲10^-12 in the 6–40 keV mass range").
- It is also compatible with INTEGRAL/SPI ("exclude lifetimes below ∼10^20 s at 95% CL [corresponding to sin^2(2θ)≲3×10^-14] in the ≳40 keV mass regime").
- The structure-formation bounds used are m_th > 8.4 keV (galaxy counts, 95% CL) and m_th > 8.5 keV (counts plus strong lensing). The paper also cites a Lyman-alpha preference of m_th = 4.1 (+33.3/−1.5) keV.
- The paper states that "the original DW mechanism is ruled out as producing the entirety of the dark matter".

Three further papers were confirmed to exist by metadata lookup. Only their abstracts were read, so their claims are reported here as abstract-level statements without numerical ranges:
- **Gorbunov, Kalashnikov and Krugan (arXiv:2502.17374, 2025).** Lepton asymmetry spread unequally over flavors can mitigate BBN limits on mixing and mass, through cancellation of flavor asymmetries. The brief notes this works best with inverted ordering. It gives colder spectra that reopen lighter masses.
- **Gorbunov and Kalashnikov (arXiv:2609.31340, 2026).** A high lepton flavor asymmetry saturates resonant production. The board's summary of the abstract is that this leaves a window of about two decades in sin^2 2θ. The concern that this ID was hallucinated is resolved: the paper is real.
- **Cline and Xu (arXiv:2601.03346, 2026).** Cold sterile-neutrino dark matter can be produced by inflaton decays during reheating, with branching ratio ≲ 1e-4. This populates mixings too small for oscillation production and below current X-ray limits.

On the X-ray side, two recent papers were found:
- **XRISM Resolve (arXiv:2510.24560).** This stacked 3.75 Ms on ten clusters over 2.5-15 keV and found no unidentified lines.
- **NuSTAR stray-light analysis (Krivonos, Barinov, Mukhin and Gorbunov, arXiv:2405.17861).** This used 11 years of data and set 95% CL limits for m_s = 6-40 keV.

Baseline references used:
- The Abazajian review (arXiv:1705.01837), for the published DW relic fit.
- Viel et al. (astro-ph/0501562), for the DW-to-thermal mass mapping.
- Merle (arXiv:1702.08430), as a pre-2024 review.

No citable arXiv source was found for 2024-2026 eROSITA or INTEGRAL/SPI line limits. The eROSITA statement in the brief came from a non-citable web snippet.

## Results

### Tool capabilities and assumptions

The sterile-neutrino server computes Yp, D/H and Li7 from a fit to the PRyMordial BBN network, accurate to better than 0.3%. Its only BBN input is ΔN_eff.

| Item | Server setting |
|---|---|
| N_eff validity range | 2.044-6.044 |
| ω_b h^2 validity range | 0.019-0.0257 |
| τ_n validity range | 866.4-890.4 s |
| Mass validity | m_s below about 100 keV; at m_s ≥ 1 MeV decay injection is not modelled |
| Yp data | 0.2449 ± 0.004 (Aver+ 2021) |
| D/H data | (2.547 ± 0.025)e-5 (Cooke+ 2018) |
| N_eff data | Planck 2.99 ± 0.17 |
| Exclusion rule | Δχ^2 > 3.84 relative to the SM |

The server's data values differ from the brief's Yp = 0.245 ± 0.003 and D/H = (2.53 ± 0.03)e-5.

Two production modes are offered:
- **DW (non-resonant).**
- **Shi-Fuller (SF, resonant).** Its ΔN_eff is a heuristic set to 0.1 times the DW value, and its relic density is a fitting formula in L. The lepton asymmetry is not fed into the BBN network.

### BBN versus the DW plane

A 100 × 100 DW scan covered m_s = 1-100 keV and sin^2 2θ = 1e-15 to 1e-6. It showed that BBN excludes only large mixing.

| m_s | BBN exclusion starts above sin^2 2θ = |
|---|---|
| 1 keV | 3.5e-7 |
| 3.7 keV | 1.2e-7 |
| 7 keV | 8.1e-8 |
| 13.5 keV | 4.3e-8 |
| 50 keV | 1.5e-8 |
| 100 keV | 1e-8 |

The server's Ω_s h^2 = 0.12 contour lies far below these thresholds:

| m_s (keV) | 1 | 2 | 3 | 5 | 7.1 | 10 | 20 | 50 | 100 |
|---|---|---|---|---|---|---|---|---|---|
| sin^2 2θ on DM line | 8.7e-9 | 2.5e-9 | 1.2e-9 | 4.8e-10 | 2.55e-10 | 1.37e-10 | 3.9e-11 | 7.6e-12 | 2.2e-12 |

Along this line ΔN_eff is 1e-4 to 1.1e-2 and |Δχ^2_BBN| < 0.15. Overclosure is therefore 40 times (1 keV) to about 5000 times (100 keV) stronger than BBN. The entire DW dark-matter line and everything below it are BBN-allowed.

[[FIGURE 8]]

Figure 8 shows the DW exclusion plot from this scan: the BBN-excluded region at large mixing and the overclosure region, in the (m_s, sin^2 2θ) plane.

Representative points are listed below, with σ values relative to the brief's data.

| Point | ΔN_eff | Yp | D/H | Δχ^2 | Verdict |
|---|---|---|---|---|---|
| SM, N_eff = 3.044 | 0 | 0.246815 (+0.6σ) | 2.4433e-5 (−2.9σ) | 0 | baseline |
| 7.1 keV, 3e-10 | negligible | 0.24684 | 2.4440e-5 | −0.024 | allowed |
| 1 keV, 3e-7 | 0.387 | 0.25193 (+2.3σ) | 2.5718e-5 (+1.4σ) | 0.44 | allowed |
| 10 keV, 1e-7 | 0.813 | 0.25730 (+4.1σ) | 2.7145e-5 (+6.2σ) | 13.4 | excluded |
| 3 keV, 3e-7 | 0.931 | 0.25874 (+4.6σ) | 2.7540e-5 (+7.5σ) | 19.3 | excluded |

The 1 keV point is allowed despite Yp sitting at +2.3σ. The reason is that the SM D/H sits low, so extra radiation improves the D/H fit and offsets the Yp penalty.

[[FIGURE 6]]

Figure 6 shows the server's BBN response to N_eff. From it:
- BBN alone gives ΔN_eff < 0.548 at 95%.
- The slopes are dYp/dN_eff = 0.0135 and d(D/H × 1e5)/dN_eff = 0.331.

A separate server cross-check used the BEST short-baseline point (m_s = 1.14 eV, sin^2 2θ = 0.42). It gave:
- ΔN_eff = 1, Yp = 0.25956, D/H = 2.777e-5 and Δχ^2 = 23.1, so the point is excluded.
- 6.2σ tension with Planck N_eff, and 33σ at CMB-S4.

### BBN robustness: data baseline and lepton asymmetry

These are analytic results, not server runs. They linearize the slopes above about the server SM values. Bounds are 95% upper limits on ΔN_eff, with Δχ^2 = 3.84 against the SM; values in brackets are against the best fit.

| Data set | Yp only | D/H only | Combined |
|---|---|---|---|
| Brief's data | 0.32 | 0.58 [0.44] | 0.47 [0.37] |
| Server's data | 0.46 | 0.66 [0.46] | 0.61 [0.43] |

The server itself reports 0.548. Because the SM D/H is 2.9σ (brief) to 4.1σ (server) low, D/H alone prefers ΔN_eff ≈ 0.26-0.31. The bound therefore moves by 0.1-0.2 depending on the baseline.

The joint (ΔN_eff, ξ_e) bound used dYp/dξ_e = −0.25, assumed D/H independent of ξ_e, and applied 2-dof Δχ^2 = 5.99.

| Data set | Allowed ΔN_eff | Allowed ξ_e |
|---|---|---|
| Brief's data | [0.04, 0.48] | 0.0073 + 0.054 ΔN_eff ± 0.029 |
| Server's data | [0.13, 0.50] | 0.0077 + 0.054 ΔN_eff ± 0.039 |

Overall this gives |ξ_e| ≲ 0.03-0.06. A positive ξ_e of about 0.03 compensates a ΔN_eff of about 0.5 in Yp. Two caveats affect the ξ_e headroom available to Shi-Fuller scenarios:
- The SM D/H baseline depends on the choice of d(p,γ)3He rate.
- Neglecting dD/H/dξ_e biases the joint contour.

### Shi-Fuller tool tests

SF-mode runs at m_s = 10, 20 and 30 keV with sin^2 2θ = 1e-14 gave ΔN_eff ≈ 1e-8 and BBN Δχ^2 = 0. At 20 keV the outputs were Yp = 0.24682 and D/H = 2.4433e-5.

| L | Ω_s h^2 at 10 keV | at 20 keV | at 30 keV |
|---|---|---|---|
| 1e-3 | 0.122 | 0.490 | 1.10 |
| 0.1 | 1.22 | 4.90 | 11.0 |

All of these points are flagged as overclosing. None of this tests the claims of arXiv:2507.18752, for four reasons:
- The tool caps L at 0.1, while the paper needs L ≳ 0.5.
- Its SF ΔN_eff is a heuristic.
- ξ_e does not enter Yp.
- Its relic density is a fitting formula, not a Boltzmann calculation.

The "BBN-allowed" verdict is trivially true here and is not supporting evidence.

### X-ray decay rate and limits

The server's radiative decay rate agrees with Γ = 1.38e-32 s^-1 (sin^2 2θ/1e-10)(m_s/keV)^5 to within about 1.5%:
- At 7.1 keV and 1e-10 it gives 2.46e-28 s^-1 (formula 2.49e-28), with E = 3.55 keV and lifetime 4.07e27 s.
- At 20 keV and 1e-12 it gives 4.36e-28 s^-1 (formula 4.42e-28), with E = 10 keV.

Equation 2 of arXiv:2405.17861 gives 1.36×10^-22 (m_s/keV)^5 sin^2 2θ s^-1, which equals 1.36e-32 s^-1 at sin^2 2θ = 1e-10, consistent with the above. Whole-halo fluxes at 7.1 keV and 1e-10 are:
- 4.68 ph/s/cm^2 for the Milky Way centre.
- 6.89e-4 ph/s/cm^2 for M31.
- 3.55e-5 ph/s/cm^2 for Perseus.

The tool's built-in limits (NuSTAR M31 from Roach+2020, and XMM blank-sky from Dessert+2020) exclude both test points.

**XRISM and the 3.55 keV line.** The XRISM abstract gives a 3σ limit Γ ∼ 1.0e-27 s^-1 at m_s ∼ 7.1 keV. This is "3−4 times lower than the one derived by Hitomi ... but still 5 times higher than the XMM-Newton detection reported by Bulbul et al. (2014)". The line is therefore constrained but not ruled out. Scaling the rate gives sin^2 2θ ≲ 4e-10 at 7.1 keV. This is our conversion, not a quoted value.

**NuSTAR.** arXiv:2405.17861 sets 95% limits for 6-40 keV. Its observed limits are stronger than expected at 8-9 and 23-25 keV, and it reports a known instrumental excess at 40 keV. Two problems prevented reading numerical values from it:
- Fig. 3 was missing from the HTML rendering.
- The Fig. 1 image was downloaded but could not be digitized with the available tools.

Per-mass NuSTAR entries therefore rest on the secondary summary in arXiv:2507.18752 (≲ 1e-12 across 6-40 keV).

[[FIGURE 15]]

Figure 15 is the Fig. 1 image retrieved from arXiv:2405.17861. No numbers in this report are read from it.

The resulting limit table is below. It was cross-checked with the server's line tool, and is 95% CL unless noted.

| m_s | Limit on sin^2 2θ | Server check |
|---|---|---|
| 7.1 keV | XRISM ≲ 4e-10 (3σ, derived); NuSTAR ≲ 1e-12 | Built-in tables exclude 1e-10 |
| 10 keV | NuSTAR ≲ 1e-12 | At 1e-12: Γ = 1.36e-29 s^-1, E = 5 keV, lifetime 7.35e28 s; not excluded by the tool's tables |
| 20 keV | NuSTAR ≲ 1e-12 | Built-in tables exclude 1e-12, so the tool's table is stronger than the summary value here |
| 40 keV | NuSTAR upper edge (instrumental excess); SPI ≲ 3e-14 above it | none |
| 50 keV | SPI ≲ 3e-14 | At 3e-14: Γ = 1.28e-27 s^-1, E = 25 keV, lifetime 7.84e26 s (2.48e19 yr); not excluded |

Warning: the SPI quote equates "lifetimes below ∼10^20 s" with sin^2 2θ ≲ 3e-14. That is inconsistent with the computed lifetime of 7.84e26 s at that mixing. The tool's lifetime in years (2.48e19 yr) is close to 1e20, which suggests the quoted unit may be years. If so, the SPI ceiling tightens as m_s^-5 rather than staying flat. This is unresolved without the primary SPI paper.

### DW relic normalization and the thermal-equivalent mass

The server's DW relic density scales as Ω_s h^2 = 0.1 (sin^2 2θ/1e-9)(m_s/3 keV)^1.8. Spot checks:
- 3 keV at 1e-9 gives 0.100.
- 10 keV at 1e-9 gives 0.873, a ratio of 8.73, which equals (10/3)^1.8.
- 1 keV at 1e-8 gives 0.138.

The mass exponent matches the brief's formula, but the normalization is three times higher than the brief's.

The published fit in arXiv:1705.01837, Eq. 37, is

m_s ≈ 3.40 keV (sin^2 2θ/1e-8)^-0.615 (Ω_DM/0.26)^0.5 × 0.527 erfc[−1.15 (T_QCD/170 MeV)^2.15].

Inverted by hand, it places the DM line as follows.

| m_s (keV) | 3 | 7.1 | 10 | 20 | 50 |
|---|---|---|---|---|---|
| Published fit | 1.23e-8 | 3.0e-9 | 1.73e-9 | 5.6e-10 | 1.26e-10 |
| Server (Ω h^2 = 0.119-0.120) | 1.2e-9 | 2.55e-10 | 1.37e-10 | 3.9e-11 | 7.6e-12 |

The QCD-era uncertainty (T_QCD = 150-200 MeV) moves the published line by about +10%/−7%. The published line needs 10-17 times more mixing than the server and 3.4-5.5 times more than the brief's formula. It also differs in shape: Ω ∝ m^2 (sin^2 2θ)^1.23.

At 7.1 keV, measured against XRISM (≲ 4e-10):
- The server line (2.55e-10) survives.
- The brief's line (7.65e-10) is excluded.
- The published line (3.0e-9) is excluded, by about 7.5 times.

Taking the published fit as the reference, XRISM alone excludes DW dark matter at 7.1 keV. Server-based DW statements are not conservative.

**Thermal-equivalent mass.** Using m_s = 4.43 keV (m_th/keV)^(4/3) (Viel et al. 2005; not quoted verbatim from the downloaded text), the DW line maps as follows.

| m_s (keV) | 3 | 7.1 | 10 | 20 | 50 |
|---|---|---|---|---|---|
| m_th (keV) | 0.75 | 1.42 | 1.84 | 3.10 | 6.16 |

The structure-formation bounds then translate into mass requirements:
- Lyman-alpha m_th > 4 (6) keV requires m_s > 28 (48) keV.
- Satellite counts (m_th > 8.4 keV) require m_s > 76 keV.

At m_s ≥ 28 keV the DW line sits at about 3e-10 (published) or about 1e-11 (server). Both are far above the NuSTAR and SPI ceilings, so the surviving DW mass interval is empty under all three normalizations. This is robust to the 10-30% differ
