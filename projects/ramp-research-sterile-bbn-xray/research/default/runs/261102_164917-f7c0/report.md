# Sterile neutrino DM: BBN + X-ray joint constraints — updated report

## Abstract
This run attempted to deepen the two weakest claims from prior work: the X-ray decay-line limit table and the production-mechanism / structure-formation mapping. Two contrasting X-ray emulator points and a six-point BBN grid at 40–50 keV were computed locally, and literature figures were extracted for NuSTAR stray-light limits, Abazajian review detections, and Viel et al. WDM transfer functions. Tool budget was exhausted after four calls per direction, so no primary-source verbatim quotes, no numerically read NuSTAR Fig.3 or XRISM limits, no SPI primary fetch, no DW-normalization settlement, and no BBN robustness reruns were completed. The joint BBN+X-ray exclusion therefore remains anchored to prior-run scans and server heuristics with explicit caveats.

## Background
Literature describes keV sterile neutrino dark matter constrained jointly by BBN and X-ray decay searches. BBN constraints arise from thermalization via active-sterile oscillations increasing N_eff and altering n/p freeze-out, with relaxation possible via large lepton asymmetry or secret interactions. X-ray constraints come from non-observation of decay lines at E = m_s/2 in stacked clusters, M31, Galactic Center/Bulge and diffuse background with NuSTAR, Chandra and XMM-Newton. The 3.55 keV / 7.1 keV candidate has been extensively tested and largely excluded as DM decay. Production mechanism determines the relic density vs mixing relation and maps to the joint exclusion plane with Lyman-alpha free-streaming limits.

Key literature for this task:
- arXiv:1402.4119 — 7.1 keV sterile neutrino decay interpretation of the 3.55 keV line; defines X-ray line flux vs mass/mixing target.
- arXiv:1402.2301 — independent detection claim for the 3.55 keV line; motivates X-ray line search methodology.
- arXiv:1904.05710 — NuSTAR M31 / Galactic bulge X-ray line search with focused+unfocused FOV treatment.
- arXiv:1602.04816 — NuSTAR Galactic Center constraints closing the Dodelson-Widrow window.
- arXiv:1408.3503 — joint CMB/BBN N_eff and mass constraints vs short-baseline anomalies.
- arXiv:1103.4570 — comprehensive BBN+CMB+LSS constraints on sterile thermalization and Delta N_eff.

Additional papers referenced in this wave: arXiv:1705.01837 (Abazajian review), arXiv:2405.17861 (NuSTAR 11-yr stray-light), arXiv:2510.24560 (XRISM Resolve 3.75 Ms stacked clusters), arXiv:2507.18752 (Vogel Shi-Fuller with large L), astro-ph/0501562 (Viel et al. WDM/Lyman-alpha), astro-ph/0602028 (galaxy surface photometry, not directly relevant).

## Results

### BBN baseline and validity range
The sterile-neutrino server reports BBN baselines as Yp = 0.2449 ± 0.004 (Aver, Olive & Skillman JCAP 07 2021 029), D/H = 2.547 ± 0.025e-5 (Cooke, Pettini & Steidel ApJ 855 2018 102), Planck N_eff = 2.99 ± 0.17 (TT,TE,EE+lowE+lensing+BAO), with CMB-S4 forecast N_eff = 3.044 ± 0.03. The BBN fit validity range is N_eff 2.044–6.044, omega_b h2 0.019–0.0257, tau_n 866.4–890.4 s, 95% exclusion at Delta chi2 > 3.84 (1 dof), m_s < ~100 keV (relativistic at BBN), PRyMordial-calibrated <0.3%. This provenance was captured verbatim from the server description and has not been independently verified against primary observational papers; the brief’s alternative baselines Yp = 0.245 ± 0.003 and D/H = (2.53 ± 0.03)e-5 were not reconciled, and the impact of the Planck N_eff prior on the Delta N_eff < 0.5 vs 0.6 bound was not quantified.

### Prior-run artifacts and current-run inventory
Prior run 261021_110150 produced a DW scan CSV/NPZ (scan_DW_dc7743.csv/.npz), BBN vs N_eff plot (bbn_vs_neff.png), exclusion plane (exclusion_scan_DW_dc7743.png), six sterile_nu_grid CSVs (DW and SF mechanisms), and references.bib with five papers, plus six paper PDF/TXT pairs (1702.08430, 1705.01837, 2405.17861, 2507.18752, 2510.24560, astro-ph/0501562). Current run 261102_164917 contains three grid CSVs (sterile_nu_grid_DW_44fa64.csv, sterile_nu_grid_DW_5d6c37.csv, sterile_nu_grid_SF_d58c80.csv) and four figure directories (figures_1705.01837, figures_2405.17861, figures_astro-ph_0501562, figures_astro-ph_0602028). The out/ directory is empty (0 files); no updated joint report was written in this wave.

File inventory verified by directory listing:
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261021_110150/scan_DW_dc7743.csv
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261021_110150/scan_DW_dc7743.npz
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261021_110150/bbn_vs_neff.png
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261021_110150/exclusion_scan_DW_dc7743.png
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261102_164917/sterile_nu_grid_DW_44fa64.csv
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261102_164917/sterile_nu_grid_DW_5d6c37.csv
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261102_164917/sterile_nu_grid_SF_d58c80.csv

### X-ray decay-line emulator at contrasting masses
Two contrasting X-ray line predictions were computed with the server’s whole-halo, f_DM = 1, no FOV cut model (10 tabulated limits). This model assumption means the “not excluded” verdicts are not directly comparable to NuSTAR unfocused stray-light or SPI diffuse limits without primary-paper J-factor/profile and sin^2 2theta normalization.

- m_s = 40 keV, sin^2 2theta = 3e-14: E_gamma = 20 keV, Gamma = 4.18e-28 s^-1, tau = 2.39e27 s (7.58e19 yr), not excluded by built-in limits. Fluxes: Milky Way center (M = 1e12 Msun, d = 0.0083 Mpc) 1.42 ph/s/cm2; M31 (1.3e12 Msun, 0.78 Mpc) 0.000208 ph/s/cm2; Coma (1.2e15 Msun, 99.0 Mpc) 1.19e-05 ph/s/cm2; Perseus (6.6e14 Msun, 77.7 Mpc) 1.07e-05 ph/s/cm2.
- m_s = 10 keV, sin^2 2theta = 1e-12: E_gamma = 5 keV, Gamma = 1.36e-29 s^-1, tau = 7.35e28 s (2.33e21 yr), not excluded. Fluxes: Milky Way center 0.184 ph/s/cm2; M31 2.71e-05 ph/s/cm2; Coma 1.55e-06 ph/s/cm2; Perseus 1.4e-06 ph/s/cm2.

The analytic decay rate Gamma = 1.38e-29 s^-1 (m_s/1 keV)^5 sin^2 2theta matches the tool within 3% at these points. These two points are the only masses in the intended 5-row table (7.1/10/20/40/50 keV) with tool Gamma/tau in this wave; the 7.1 keV and 20 keV entries from prior waves were not rerun here, and the 50 keV SPI-dominated entry remains without primary-source provenance.

### BBN impact at high-mass, low-mixing (SPI-dominated) regime
A six-point DW grid at m_s = 40 and 50 keV with sin^2 2theta = 1e-12, 3e-14, 1e-14 was computed. All points are BBN-allowed (Delta chi2_BBN ~ 0, bbn_excluded_95 = 0) and not overclosing (Omega_s h2 < 0.12), confirming BBN is negligible at these low mixings where X-ray/SPI dominates. This result relies on the server’s BBN mapping and has not been independently verified with a full Boltzmann code.

CSV: /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261102_164917/sterile_nu_grid_DW_5d6c37.csv

- 40 keV, 1e-12: Delta N_eff = 2.47e-05 (2.46585e-05), Omega_s h2 = 0.0106 (0.0105898), tau = 7.18e25 s (7.17533e25 s), Yp = 0.246815, D/H = 2.44334e-5, chi2_bbn = 2.7711, Delta chi2 = -0.0003, free-streaming = 26.87 kpc
- 40 keV, 3e-14: Delta N_eff = 7.40e-07 (7.39754e-07), Omega_s h2 = 0.00032 (0.000317695), tau = 2.39e27 s (2.39178e27 s)
- 40 keV, 1e-14: Delta N_eff = 2.47e-07 (2.46585e-07), Omega_s h2 = 0.00011 (0.000105898), tau = 7.18e27 s (7.17533e27 s)
- 50 keV, 1e-12: Delta N_eff = 2.95e-05 (2.94777e-05), Omega_s h2 = 0.0158 (0.0158244), tau = 2.35e25 s (2.35121e25 s), free-streaming = 21.49 kpc
- 50 keV, 3e-14: Delta N_eff = 8.84e-07, Omega_s h2 = 0.00047, tau = 7.84e26 s
- 50 keV, 1e-14: Delta N_eff = 2.95e-07, Omega_s h2 = 0.00016, tau = 2.35e27 s

### Production mechanism comparison: Dodelson-Widrow vs Shi-Fuller
At m_s = 20 keV, sin^2 2theta = 1e-14: DW gives Delta N_eff = 1.42e-07 (1.416e-07), Omega_s h2 = 3.04e-05 (3.041e-05), Delta chi2_BBN = 0, BBN-allowed and not overclosing. The server’s SF model at L = 0.1 (heuristic 0.1×DW, no xi_e, no BR/T_RH physics) gives Delta N_eff = 1.42e-08 (1.416e-08), Omega_s h2 = 4.90 (4.898), BBN-allowed but overclosing by ~40×. At 50 keV, 1e-14: DW Omega_s h2 = 1.58e-04, SF Omega_s h2 = 30.6, overclosing by ~255×. This demonstrates the server SF implementation is unphysical at L = 0.1 and cannot test the literature L > 0.5 viable region (Vogel arXiv:2507.18752: m_s > 10 keV, sin^2 2theta < 1e-14). The DW normalization dispute (server 2.55e-10 vs Abazajian arXiv:1705.01837 Eq.37 3.0e-9 at 7.1 keV, factor 10–17×) remains unresolved; no verbatim Eq.37 quote with 0.527×erfc term and T_QCD 150–200 MeV uncertainty was captured.

CSVs:
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261102_164917/sterile_nu_grid_DW_44fa64.csv
- /Users/nramachandra/hep-genesis-testing/projects/ramp-research-sterile-bbn-xray/runs/261102_164917/sterile_nu_grid_SF_d58c80.csv

### Literature figure extraction
Four figure sets were extracted to the current run; no numeric digitization or verbatim quoting was performed due to budget exhaustion.

NuSTAR 11-yr stray-light paper arXiv:2405.17861 Fig.1 was extracted, showing 95% CL sin^2 2theta upper limits vs m_s from the unfocused stray-light spectrum (|b| > 3 deg, 117 Ms/FPM) with previous NuSTAR 2020/2023 and XMM 2021 constraints overplotted; the borderline excess at 40 keV is noted as an instrumental absorbed stray-light effect. This extraction has not been independently verified against a primary-source numeric table, and Fig.3 (observed vs expected limits at 7,10,20,40 keV) was not numerically read.

[[FIGURE 39]]
Figure 39 shows NuSTAR 95% upper limits on sin^2 2theta from the unfocused stray-light spectrum with previous constraints overplotted.

[[FIGURE 40]]
Figure 40 shows the NuSTAR FPMA+FPMB combined spectrum of the unfocused stray-light sky background at |b| > 3 deg.

[[FIGURE 41]]
Figure 41 shows the sky distribution of 3248 (FPMA) and 3139 (FPMB) NuSTAR observations in Galactic coordinates.

[[FIGURE 42]]
Figure 42 shows NuSTAR detector count rate vs time with a cubic polynomial outlier-resistant approximation and exclusion threshold.

Abazajian arXiv:1705.01837 Fig.7 was extracted, showing X-ray line detections consistent with 7.1 keV sterile neutrino DM (Bulbul et al. MOS/PN stacked clusters, Perseus core-removed, M31, Galactic Center) vs 90% constraints from Chandra M31, stacked dwarfs, Suzaku Perseus. Fig.2 (lepton asymmetry sign vs mass splitting and mixing) was also extracted.

[[FIGURE 43]]
Figure 43 shows the final sign of the lepton asymmetry vs mass splitting and mixing angle for nu_tau <-> nu_s mixing.

[[FIGURE 44]]
Figure 44 shows X-ray line detections consistent with sterile neutrino DM with 1,2,3 sigma regions from stacked clusters, Perseus, M31 and Galactic Center.

Viel et al. astro-ph/0501562 Figs.1–3 were extracted, showing WDM transfer function T(k) for thermal masses 92–1441 eV and mixed LambdaCWDM, flux power spectrum fractional difference for m_WDM = 0.5–8 keV at z = 2.5–4, and bias function b^2(k) for 1 keV WDM. The Viel coefficient m_s = 4.43 keV (m_th/1 keV)^{4/3} was not quoted verbatim, no m_th translation table at 7.1/10/20/50 keV was computed, and the half-mode vs free-streaming definition shift remains open.

[[FIGURE 45]]
Figure 45 shows the WDM transfer function T(k) for pure LambdaWDM models with T_x/T_nu = 0.5–0.2 corresponding to m_x = 92–1441 eV, with analytic fits.

[[FIGURE 47]]
Figure 47 shows fractional difference of flux power spectrum for LambdaWDM vs LambdaCDM for thermal WDM masses 0.5–8 keV at z = 4, 3, 2.5.

[[FIGURE 48]]
Figure 48 shows bias function b^2(k) between flux power spectrum and linear matter power spectrum for LambdaCDM vs LambdaWDM with
