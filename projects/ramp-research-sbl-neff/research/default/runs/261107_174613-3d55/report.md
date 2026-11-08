# Short-baseline eV sterile neutrinos versus $N_{\rm eff}$ constraints: standard thermalization excluded, loopholes not quantified

## Abstract
The task was to test whether an eV-scale sterile neutrino explaining short-baseline anomalies survives cosmology. The answer is no in the standard case. At the BEST gallium best fit ($m_s = 1.14\,\mathrm{eV}$, $\Delta m^2_{41} = 1.3\,\mathrm{eV}^2$, $\sin^2 2\theta = 0.42$) Dodelson-Widrow production (collision-driven thermalization without new physics) gives $\Delta N_{\rm eff} = 1.0$ for total $N_{\rm eff} = 4.044$, which is $6.2\sigma$ above Planck 2018 $N_{\rm eff} = 2.99 \pm 0.17$ and excluded by Big Bang Nucleosynthesis (BBN, light-element formation) at $\Delta \chi^2 = 23.1$. The two weakest claims flagged by the board — the current status of appearance versus disappearance anomalies and the viability of non-standard suppression — were deepened with emulator grids and scans, but verbatim literature hardening and a suppressed-thermalization contrast were blocked by tool budget exhaustion.

## Background
The literature consensus is that a fully thermalized eV sterile neutrino contributes $\Delta N_{\rm eff} \sim 1$ (extra relativistic species beyond the Standard Model $N_{\rm eff} = 3.044$), which is excluded by Planck and BBN unless non-standard suppression is invoked.

* arXiv:1807.06209 (Planck 2018 results. VI. Cosmological parameters) reports $N_{\rm eff} = 2.99 \pm 0.17$ from temperature, polarization, lensing and baryon acoustic oscillations, with $95\%$ limit $N_{\rm eff} < 3.30$ ($\Delta N_{\rm eff} < 0.28$) and $m_{\rm eff, sterile} < 0.65\,\mathrm{eV}$. This defines the benchmark for exclusion of a fully thermalized eV sterile.
* arXiv:1606.04886 (joint cosmology and laboratory analysis) shows standard thermalization for short-baseline (SBL, meter-to-kilometer baseline neutrino experiments) mixing parameters gives $\Delta N_{\rm eff} \sim 1$ and is excluded, quantifying thermalization fraction versus mass and mixing.
* arXiv:1406.3208 (sterile neutrinos with secret interactions) proposes secret gauge interactions mediated by a light boson to generate a matter potential and suppress thermalization. This is the key loophole claim to test.
* arXiv:2201.07327 (reactor antineutrino anomaly in light of recent flux models) re-evaluates inverse beta decay yields with Huber-Mueller and summation models and finds the reactor anomaly significance drops from $\sim 3\sigma$ to $<1$–$2\sigma$ depending on flux model.
* arXiv:2210.10216 (MicroBooNE search for electron neutrino excess) finds no evidence for light sterile oscillations in $6.37 \times 10^{20}$ protons on target and sets $95\%$ exclusion contours in $\Delta m^2_{41}$ versus mixing, constraining muon-to-electron appearance but leaving electron disappearance relevant to reactor and gallium anomalies less directly excluded.
* arXiv:2504.16590 (testing the gallium anomaly with electron-neutrino scattering) notes the gallium deficit $R = 0.803 \pm 0.035$ in GALLEX, SAGE and BEST $^{51}$Cr calibrations persists, while sterile parameter space is strongly excluded by null experiments and the reactor anomaly is now attributed to flux error. One verbatim citation from this paper was secured; other required citations remain open.

The brief notes LSND at $3.8\sigma$ and MiniBooNE low-energy excess motivate eV sterile mixing $\Delta m^2 \sim 1.3\,\mathrm{eV}^2$, $\sin^2 2\theta \sim 0.01$–$0.4$, while MicroBooNE liquid argon (LAr) data disfavors simple $\nu_\mu \to \nu_e$ oscillations and BEST gallium persists at $\sim 5\sigma$.

## Results

All emulator calculations ran locally on the hosted sterile-neutrino to BBN bridge server in run 261107_174613, with no facility dispatch. Outputs are saved as CSV, NPZ, PNG and PDF in that run directory.

### Planck and BBN benchmarks for extra radiation
$N_{\rm eff}$ (effective number of relativistic species at recombination) counts light relics. Planck 2018 measures $N_{\rm eff} = 2.99 \pm 0.17$, consistent with Standard Model $N_{\rm eff} = 3.044$–$3.046$, with $95\%$ limit $N_{\rm eff} < 3.30$ corresponding to $\Delta N_{\rm eff} < 0.28$. A fully thermalized sterile neutrino predicts $\Delta N_{\rm eff} = 1.0$ and $N_{\rm eff} = 4.044$, which is $6.2\sigma$ high. This finding relies on the published Planck value and was not independently re-derived from cosmic microwave background data in this run.

BBN predicts primordial helium mass fraction $Y_p$ and deuterium $D/H$ as functions of $N_{\rm eff}$ and baryon density. The emulator reproduces:

* Standard Model $N_{\rm eff} = 3.044$ gives $Y_p = 0.2468$ and $D/H \times 10^5 = 2.443$.
* One thermalized sterile $N_{\rm eff} = 4.044$ gives $Y_p = 0.2596$ and $D/H \times 10^5 = 2.777$.

Observed values are $Y_p = 0.2449 \pm 0.004$ and $D/H = 2.547 \pm 0.025 \times 10^{-5}$ (brief quotes $Y_p = 0.245 \pm 0.003$, $D/H \sim 2.5 \times 10^{-5}$). The thermalized case is $3.7\sigma$ high in $Y_p$ alone. Near the Standard Model the slopes are $dY_p/dN_{\rm eff} = 0.0135$ and $d(D/H \times 10^5)/dN_{\rm eff} = 0.331$, though these slope values are derived from the two endpoint predictions and were flagged as not independently verified by direct fit excerpts. BBN alone limits $\Delta N_{\rm eff} < 0.55$ at $95\%$ ($\Delta \chi^2 > 3.84$ versus Standard Model).

[[FIGURE 3]]
Figure 3. BBN helium and deuterium versus $N_{\rm eff}$ showing Standard Model and fully thermalized sterile predictions and the BBN $95\%$ limit.

### Standard thermalization at the SBL best fit
The BEST best fit ($m_s = 1.14\,\mathrm{eV}$, $\Delta m^2_{41} = 1.3\,\mathrm{eV}^2$, $\sin^2 2\theta = 0.42$ for electron disappearance) was evaluated with Dodelson-Widrow production.

* It fully thermalizes to $\Delta N_{\rm eff} = 1.0$ and $N_{\rm eff} = 4.044$.
* BBN gives $Y_p = 0.2596$ versus $0.2449 \pm 0.004$ and $D/H = 2.78 \times 10^{-5}$ versus $2.547 \pm 0.025 \times 10^{-5}$, with $\Delta \chi^2 = 23.1$ versus Standard Model, excluded at $95\%$ where the threshold is $3.84$.
* Relic density is $\Omega_s h^2 = 29.3$ versus observed dark matter $\Omega_c h^2 = 0.12 \pm 0.001$, overclosing by more than two orders of magnitude.

This result was reproduced by both single-point and grid tools and is the core exclusion. The mixing definition in the emulator does not distinguish appearance ($\sin^2 2\theta_{\mu e}$, muon to electron) from disappearance ($\sin^2 2\theta_{ee}$, electron to electron) flavors, so the mapping to SBL channels relies on a proxy and was flagged as not independently verified.

### Mixing dependence and required suppression
A grid at fixed $m_s = 1.14\,\mathrm{eV}$ varying $\sin^2 2\theta$ shows:

| $\sin^2 2\theta$ (dimensionless) | $\Delta N_{\rm eff}$ (dimensionless) | $N_{\rm eff}$ (dimensionless) | $\Delta \chi^2_{\rm BBN}$ (dimensionless) | $\Omega_s h^2$ (dimensionless) | Status versus Planck $\Delta N_{\rm eff} < 0.28$ |
|---|---|---|---|---|---|
| $0.42$ | $1.0$ | $4.044$ | $23.1$ | $29.3$ | Excluded |
| $0.01$ | $1.0$ | $4.044$ | $23.1$ | $0.70$ | Excluded |
| $0.001$ | $0.40$ | $3.44$ | $0.62$ | $0.07$ | Excluded |
| $0.0001$ | $0.04$ | $3.08$ | $-1.1$ | $0.007$ | Allowed |
| $1 \times 10^{-6}$ | $0.0004$ | $3.044$ | $-0.01$ | $7 \times 10^{-5}$ | Allowed |

Full thermalization persists down to $\sin^2 2\theta = 0.01$. Planck requires suppression factor $>3.6$ ($1.0/0.28$) from the canonical value, implying allowed mixing $<5 \times 10^{-4}$. This is more than $20$ times below LSND appearance best fit $\sim 0.01$ and $\sim 800$ times below BEST disappearance $0.42$. The file sterile_nu_grid_DW_fd1398.csv contains this scan.

### 3600-point exclusion plane and statistical validation
A scan over $m_s = 0.1$–$10\,\mathrm{eV}$ and $\sin^2 2\theta = 1 \times 10^{-4}$ to $0.5$ with $3600$ points (Dodelson-Widrow) yields:

* $2479/3600$ ($68.9\%$) BBN-excluded at $95\%$ ($\Delta \chi^2 > 3.84$).
* $2258/3600$ ($62.7\%$) overclose the universe ($\Omega_s h^2 > 0.12$).
* Maximum BBN-allowed mixing is $\sin^2 2\theta_{\rm max} = 0.00134$ across $0.1$–$5\,\mathrm{eV}$ (null at $10\,\mathrm{eV}$), though this maximum value was flagged as lacking a direct tool quote in excerpts.

Independent validation via table load and statistics gives $\Delta \chi^2_{\rm BBN}$ mean $15.10$, standard deviation $10.83$, range $-1.15$ to $23.10$, median $23.10$, with $5$th percentile $-1.07$ and $16$th percentile $-0.74$. $N_{\rm eff}$ mean is $3.78 \pm 0.38$, range $3.08$ to $4.04$. The median at the maximum excluded value confirms a bimodal population split between allowed ($\Delta N_{\rm eff} \sim 0$) and fully thermalized ($\Delta N_{\rm eff} = 1.0$) points. Files scan_DW_aa8803.csv and scan_DW_aa8803.npz store the scan.

[[FIGURE 4]]
Figure 4. Exclusion plane in sterile mass versus mixing from the 3600-point scan showing BBN, overclosure, X-ray and Lyman-alpha limits.

SBL preferred regions exceed the BBN-allowed maximum by large factors:

| Anomaly (channel) | $\sin^2 2\theta$ (dimensionless) | Factor above $0.00134$ (dimensionless) | $\Delta N_{\rm eff}$ (dimensionless) | $\Delta \chi^2_{\rm BBN}$ (dimensionless) | $\Omega_s h^2$ (dimensionless) |
|---|---|---|---|---|---|
| BEST gallium (disappearance) | $0.42$ | $313$ | $1.0$ | $23.1$ | $29.3$ |
| Reactor (disappearance) | $0.09$ | $67$ | $1.0$ | $23.1$ | $6.3$ |
| LSND appearance | $0.01$ | $7.5$ | $1.0$ | $23.1$ | $0.70$ |
| Test point | $0.001$ | $0.75$ | $0.40$ | $0.62$ | $0.07$ |

Only $\sin^2 2\theta = 0.001$ is allowed. The numerical factors are computed, but graphical overlay of SBL contours on the exclusion plane was not produced.

### Appearance versus disappearance contrast
A contrasting emulator at $m_s = 1.14\,\mathrm{eV}$ evaluated appearance mixing $\sin^2 2\theta_{\mu e} = 0.01$ (relevant to LSND and MiniBooNE muon to electron) and disappearance mixing $\sin^2 2\theta_{ee} = 0.1$ and $0.42$ (relevant to BEST, gallium and reactor electron disappearance). All three fully thermalize to $\Delta N_{\rm eff} = 1.0$, $N_{\rm eff} = 4.044$, $\Delta \chi^2 = 23.1$, with $\Omega_s h^2 = 0.70$, $6.98$ and $29.3$ respectively versus $0.12$. MicroBooNE exclusion of appearance therefore does not relieve cosmology tension for disappearance parameter space. The $0.1$ mixing point with $\Omega_s h^2 = 6.98$ is present in the CSV but was flagged as not shown in quoted excerpts, so it is not independently verified in the text record.

## Discussion
The results imply standard eV sterile neutrinos motivated by SBL anomalies are in strong tension with cosmology. Planck $N_{\rm eff} = 2.99 \pm 0.17$ and BBN $Y_p$ and $D/H$ both disfavor $\Delta N_{\rm eff} = 1.0$ at $>3\sigma$, and the relic density overcloses dark matter for all SBL best fits. This agrees with arXiv:1606.04886 and the Planck 2018 baseline, and with the brief's statement that standard thermalization is unavoidable for $\Delta m^2 \sim 1.3\,\mathrm{eV}^2$, $\sin^2 2\theta \sim 0.01$–$0.4$.

Tensions with the literature are limited to the loophole domain. Secret interactions (arXiv:1406.3208), large lepton asymmetry $L \sim 10^{-2}$, and low reheating temperature $T_{\rm RH} \ll 100\,\mathrm{MeV}$ have been proposed to suppress thermalization, but this run did not quantify their thresholds or independent BBN and cosmic microwave background free-streaming constraints. The reactor anomaly weakening (arXiv:2201.07327) and MicroBooNE appearance exclusion (arXiv:2210.10216) reduce motivation for appearance-driven sterile, yet BEST gallium persistence keeps disappearance motivation alive, and cosmology excludes both channels equally in the standard case.

Dead ends encountered:

* Quantitative per-loophole thresholds for $L \sim 10^{-2}$, secret coupling $G_X$, and $T_{\rm RH}$ with verbatim citations were blocked when tool budget was exhausted after three emulator calls; web search identified candidate papers but read and cite could not run.
* Graphical overlay of SBL contours on the exclusion plane is not supported by the hosted plot tool and would require custom code; quantification was done numerically instead.
* Initial table load failed with relative filename because the server input directory was empty; absolute path to the run output directory was required.
* Published figure extraction for arXiv:2210.10216 and arXiv:2504.16590 failed due to no usable HTML rendering; LaTeXML dropped figures.
* Verbatim citation for arXiv:1807.06209 and arXiv:2210.10216 failed because web search snippets are not exact source quotes; exact chunk extraction is required before cite validation.
* In the final wave, tool budget was exhausted on entry, so no new citations or figures could be attempted and only prior-wave emulator evidence remains.

## Limitations
What could not be established and why:

* Non-standard loophole viability was not established. No verbatim quantitative thresholds for large lepton asymmetry, secret interaction coupling, or low reheating temperature, and no independent BBN or free-streaming limits, were extracted due to budget exhaustion before read and cite could run. No contrasting suppressed-thermalization grid (illustrative $\Delta N_{\rm eff} = 0.2$–$0.3$) was run.
* Literature hardening for SBL status is incomplete. Only one of three required verbatim citations (gallium test arXiv:2504.16590) is secured; Planck $N_{\rm eff} = 2.99 \pm 0.17$, MicroBooNE exclusion, and reactor flux re-evaluation citations remain open, and no published figure was extracted.
* Mixing flavor distinction is not modeled. The emulator uses a single $\sin^2 2\theta$ without separating $\sin^2 2\theta_{\mu e}$ from $\sin^2 2\theta_{ee}$, so appearance versus disappearance tension quantification relies on a proxy mapping.
* Visual SBL overlay on the exclusion plane was not produced due to tool limitation; only numerical factors above the allowed maximum are available.
* Baryon density degeneracy in BBN limits was not explored; the quoted BBN limit $\Delta N_{\rm eff} < 0.55$ assumes fixed baryon density and the emulator's PRyMordial-calibrated fit.

## Open directions
* Quantify suppression thresholds for large lepton asymmetry $L \sim 10^{-2}$, secret interaction $G_X$, and low $T_{\rm RH}$ and test each against independent BBN $Y_p$/$D/H$ and CMB free-streaming constraints with a suppressed-thermalization emulator grid.
* Secure verbatim citations and one published figure for Planck 2018 $N_{\rm eff}$, MicroBooNE appearance exclusion, and reactor flux re-evaluation to harden the SBL status claim.
* Produce a custom overlay of BEST, reactor and LSND $95\%$ contours on the 3600-point exclusion plane to visually quantify the $7$–$313\times$ tension with allowed mixing.
* Perform a global $3+1$ fit including 2024–2026 gallium re-analyses and STEREO and PROSPECT nulls to compute parameter goodness-of-fit for the gallium anomaly versus nulls.
