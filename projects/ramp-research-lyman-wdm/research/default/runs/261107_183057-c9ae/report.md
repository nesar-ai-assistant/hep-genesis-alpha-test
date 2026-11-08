# Lyman-alpha forest limits on warm dark matter and Dodelson-Widrow sterile neutrinos

## Abstract
Recent Lyman-alpha forest (absorption by neutral hydrogen in quasar spectra) 1D flux power spectrum measurements imply a thermal-relic warm dark matter (WDM, a light thermal particle that erases small-scale structure) lower bound of $m_{\rm WDM} > 5.3\,\mathrm{keV}$ to $m_{\rm WDM} > 5.7\,\mathrm{keV}$ at $95\%$ confidence, not independently verified beyond web-search snippets in this run. Mapped to Dodelson-Widrow (DW, non-resonant oscillation production) sterile neutrinos via $m_{s,{\rm DW}} \approx 4.43\,\mathrm{keV}\,(m_{\rm WDM}/1\,\mathrm{keV})^{4/3}$, this corresponds to $m_s \approx 20\,\mathrm{keV}$ to $45\,\mathrm{keV}$ for $100\%$ dark matter. Sterile-neutrino tool grids run locally show DW relic density scales linearly with mixing, $\Omega_s h^2 \propto \sin^2 2\theta$, and that keV DW candidates contribute negligible extra radiation at Big Bang Nucleosynthesis (BBN, light-element formation), $\Delta N_{\rm eff} < 0.003$, while an eV-scale short-baseline anomaly benchmark is excluded by BBN and Planck. X-ray decay line predictions for DW $f_s=1$ points are flagged excluded by NuSTAR M31 and XMM blank-sky limits, but numerical X-ray limit curves were not digitized and the binding Lyman-alpha versus X-ray comparison remains incomplete.

## Background
The Lyman-alpha forest 1D flux power spectrum probes suppression of the matter power spectrum from WDM free-streaming (erasure of structure by particle motion). High-resolution high-redshift HIRES/UVES data at $z = 4.2$ to $5.0$ combined with hydrodynamical simulations give the strongest thermal-relic limits, typically $m_{\rm WDM} > 3$ to $5\,\mathrm{keV}$ at $95\%$ CL depending on thermal history and reionization priors, with the most stringent published bound $m_{\rm WDM} > 5.3\,\mathrm{keV}$.

Key literature in the record is:

* arXiv:2309.04533 (high-$z$ HIRES/UVES Bayesian inference, $z = 4.2$ to $5.0$, updates Irsic et al. methodology, current benchmark $m_{\rm WDM}$ lower bound).
* arXiv:1702.01764 (combined XQ-100 X-shooter $z = 3$ to $4.2$ plus HIRES/MIKE $z = 4.2$ to $5.4$, canonical $m_{\rm WDM} > 5.3\,\mathrm{keV}$ at $2\sigma$, reference for conversion to DW sterile neutrino mass $m_s > 20$ to $30\,\mathrm{keV}$).
* arXiv:1911.09073 (SDSS DR14 BOSS/eBOSS 1D flux power plus Planck, large-scale complement, neutrino mass bounds, framework for joint CMB-Lyman-alpha tension).

For sterile neutrinos produced non-resonantly via Dodelson-Widrow oscillations, the mass-mixing relation required for $\Omega_s = \Omega_{\rm DM}$ is excluded as $100\%$ dark matter by the combination of Lyman-alpha free-streaming limits mapped via $m_{s,{\rm DW}} \sim 4$ to $5\,\mathrm{keV}\,(m_{\rm WDM}/1\,\mathrm{keV})^{4/3}$ and X-ray decay line non-detections. Resonant Shi-Fuller (lepton-asymmetry-enhanced production with cooler momentum distribution) or other non-thermal production remains viable. The Viel et al. transfer function $T(k) = [1+(\alpha k)^{2\nu}]^{-5/\nu}$ with $\nu = 1.12$ calibrates the WDM suppression, and the half-mode scale $k_{1/2} = 0.325/\alpha$ links $m_{\rm WDM}$ to the cutoff.

## Results

### Lyman-alpha thermal-relic WDM limits and systematics
Web-search snippets corroborate, but do not quote-verify, the two benchmark limits. arXiv:1702.01764 reports $m_{\rm WDM} > 5.3\,\mathrm{keV}$ at $2\sigma$ from combined XQ-100 plus HIRES/MIKE flux power. arXiv:2309.04533 reports $m_{\rm WDM} > 5.7\,\mathrm{keV}$ at $2\sigma$ from high-resolution high-redshift HIRES/UVES Bayesian inference including thermal history and inhomogeneous reionization. Both rely on a proxy mapping and are not independently verified at full-text quote level in this run.

No citable quotes were extracted for $k_{\rm max}$ cuts ($0.2$ versus $<0.1\,\mathrm{s\,km^{-1}}$), $T(z)$ power-law versus free-floating versus $5000\,\mathrm{K}$ jump priors, peculiar velocities, or patchy reionization. SDSS DR14 BOSS/eBOSS plus Planck results from arXiv:1911.09073 and Rogers and Poulin re-analyses highlighting intergalactic medium thermal modeling sensitivity and Planck tension remain unverified. Mixed dark matter fraction versus mass curves from arXiv:2504.06367 and arXiv:0812.0010 were not extracted.

What ran was web search and literature-research skill loading locally; read_arxiv_chunk, get_paper_figures for limit curves, and cite were not executed before the tool budget of $80$ calls was exhausted. The run directory $261107\_183057$ contains only sterile-neutrino grids, no Lyman-alpha systematics verification outputs.

### Thermal-relic to DW sterile mass mapping and free-streaming scales
The Viel 2005 mapping $m_s = 4.43\,\mathrm{keV}\,(m_{\rm WDM}/1\,\mathrm{keV})^{4/3}$ was used without primary-source quote verification. It gives DW floors that match board floors within $1$ to $2\%$.

| $m_{\rm WDM}$ ($\mathrm{keV}$) | $m_{s,{\rm DW}}$ Viel ($\mathrm{keV}$) | Board floor ($\mathrm{keV}$) |
|---|---|---|
| $3.1$ | $20.0$ | $20.2$ |
| $3.3$ | $21.8$ | $21.9$ |
| $4.1$ | $29.1$ | $29.3$ |
| $5.7$ | $45.0$ | $45.4$ |

A conservative $4.1\,\mathrm{keV}$ prior relaxes the DW floor by $\sim 15\,\mathrm{keV}$ ($33\%$) versus the $5.7\,\mathrm{keV}$ benchmark, but all remain above the $7.1\,\mathrm{keV}$ $3.5\,\mathrm{keV}$-line mass. Alternative prescriptions (half-mode matching, Bozek/Murgia, Abazajian) were not retrieved, so the spread is not quantified beyond this analytic estimate.

Sterile-neutrino tool free-streaming lengths (distance particles stream and erase structure) at $\sin^2 2\theta = 1\times10^{-10}$ are $53.2\,\mathrm{kpc}$ at $20.2\,\mathrm{keV}$, $36.7\,\mathrm{kpc}$ at $29.3\,\mathrm{keV}$, and $23.7\,\mathrm{kpc}$ at $45.4\,\mathrm{keV}$, scaling as $1/m_s$, all in the warm dark matter regime with BBN treatment valid (relativistic at BBN). Analytic half-mode scale from $T(k)$ with $\alpha = 0.049\,(m_{\rm WDM}/1\,\mathrm{keV})^{-1.11}\,h^{-1}\mathrm{Mpc}$ gives $k_{1/2} = 23.4\,h\,\mathrm{Mpc}^{-1}$ for $3.1\,\mathrm{keV}$ and $46.0\,h\,\mathrm{Mpc}^{-1}$ for $5.7\,\mathrm{keV}$, corresponding to $\lambda \sim 0.27$ and $0.14\,h^{-1}\mathrm{Mpc}$, consistent in trend with tool $\lambda_{\rm fs}$ but offset by a factor $2$ to $3$ due to different definitions.

[[FIGURE 28]]
Figure 28. WDM transfer function $T(k)$ for thermal masses $92$ to $1441\,\mathrm{eV}$ with analytic fits, showing calibration used for Lyman-alpha mapping.

[[FIGURE 30]]
Figure 30. Fractional flux power suppression for thermal WDM masses $0.5$ to $8\,\mathrm{keV}$ at $z = 2.5$ to $4$, illustrating small-scale suppression probed by the forest.

[[FIGURE 31]]
Figure 31. Bias between flux power and linear matter power for CDM versus $1\,\mathrm{keV}$ WDM, with shaded $k$-range used in analysis.

### DW relic density grid and $f_s=1$ line
The sterile-neutrino server models pure DW production, relativistic at BBN, with $\Delta N_{\rm eff}$ (effective extra radiation) from relic density and BBN fit valid for $N_{\rm eff} = 2.044$ to $6.044$ and $m_s < 100\,\mathrm{keV}$. All computations ran locally or on the hosted sterile-neutrino server; no facility dispatch was used.

A $5$-point grid at $\sin^2 2\theta = 1\times10^{-12}$ gives:

| $m_s$ ($\mathrm{keV}$) | $\Omega_s h^2$ | $\Delta N_{\rm eff}$ |
|---|---|---|
| $7.1$ | $0.0004715$ | $6.2\times10^{-6}$ |
| $20$ | $0.003041$ | $1.4\times10^{-4}$ |
| $22$ | $0.00361$ | $1.7\times10^{-4}$ |
| $29$ | $0.005936$ | $2.8\times10^{-4}$ |
| $45$ | $0.01309$ | $6.2\times10^{-4}$ |

Linear scaling was verified: at $\sin^2 2\theta = 1\times10^{-11}$ values are exactly $10$ times larger ($0.004715$ at $7.1\,\mathrm{keV}$, $0.03041$ at $20\,\mathrm{keV}$, $0.1309$ at $45\,\mathrm{keV}$), confirming $\Omega_s h^2 \propto \sin^2 2\theta$ at low mixing. This anchors the $f_s = 1$ ($100\%$ of dark matter, $\Omega_s h^2 = 0.12$) mixings:

| $m_s$ ($\mathrm{keV}$) | $\sin^2 2\theta$ for $f_s=1$ |
|---|---|
| $7.1$ | $2.55\times10^{-10}$ |
| $20$ | $3.95\times10^{-11}$ |
| $22$ | $3.32\times10^{-11}$ |
| $29$ | $2.02\times10^{-11}$ |
| $45$ | $9.17\times10^{-12}$ |

A $35$-point grid ($7.1$, $20$, $22$, $29$, $45\,\mathrm{keV}$ times $1\times10^{-12}$ to $1\times10^{-8}$) gives $\Delta N_{\rm eff} = 6\times10^{-6}$ to $0.27$ and $\Omega_s h^2 = 0.00047$ to $131$; none are BBN-excluded at $95\%$ ($\Delta\chi^2$ versus Standard Model $-0.002$ to $-1.15$, limit $\Delta\chi^2 > 3.84$), $28$ of $35$ overclose ($\Omega_s h^2 > 0.12$). A $5$-point $f_s \approx 1$ zip grid gives $\Delta N_{\rm eff} = 0.00017$ to $0.00155$ and $\Omega_s h^2 = 0.083$ to $0.118$ ($f_s = 0.69$ to $0.98$), all BBN-allowed. Files are $sterile\_nu\_grid\_DW\_bc0526.csv$, $sterile\_nu\_grid\_DW\_230529.csv$, $sterile\_nu\_grid\_DW\_c49937.csv$, and $sterile\_nu\_grid\_DW\_59815e.csv$ in $runs/261107\_183057$.

At the $3.5\,\mathrm{keV}$ line benchmark ($m_s = 7.1\,\mathrm{keV}$, $\sin^2 2\theta = 7\times10^{-11}$) the tool gives $\Omega_s h^2 = 0.033$ ($27.5\%$ of observed $0.12$), $\Delta N_{\rm eff} = 0.00043$, $Y_p = 0.24682$, $D/H = 2.44\times10^{-5}$, lifetime $\tau = 5.8\times10^{27}\,\mathrm{s}$, free-streaming $151\,\mathrm{kpc}$, BBN allowed ($\Delta\chi^2 = -0.01$).

### BBN and CMB $\Delta N_{\rm eff}$ and $Y_p$/$D/H$ shifts
For DW masses at Lyman-alpha floors ($20.2$ to $45.4\,\mathrm{keV}$) at $\sin^2 2\theta = 1\times10^{-10}$, BBN impact is negligible: $\Delta N_{\rm eff} = 0.0014$ to $0.0027$ ($N_{\rm eff} = 3.045$ to $3.047$ versus Standard Model $3.044$), $Y_p = 0.24683$ to $0.24685$ (observed $0.2449 \pm 0.004$) and $D/H \times10^5 = 2.4438$ to $2.4442$ (observed $2.547 \pm 0.025$), $\Delta\chi^2 = -0.02$ to $-0.04$, allowed at $95\%$. BBN does not constrain these DW masses.

The BBN impact plot quantifies the lever arm:

[[FIGURE 27]]
Figure 27. BBN $Y_p$ and $D/H$ versus $N_{\rm eff}$, showing Standard Model at $N_{\rm eff}=3.044$ and fully thermalized sterile at $N_{\rm eff}=4.044$.

Key numbers from the plot are Standard Model $Y_p = 0.2468$, $D/H = 2.44\times10^{-5}$ at $N_{\rm eff} = 3.044$ and fully thermalized sterile $Y_p = 0.2596$, $D/H = 2.78\times10^{-5}$ at $N_{\rm eff} = 4.044$ ($3.7\sigma$ above observed $Y_p$). BBN alone limits $\Delta N_{\rm eff} < 0.55$ at $95\%$, with slopes $dY_p/dN_{\rm eff} = 0.0135$ and $d(D/H)/dN_{\rm eff} = 0.33\times10^{-5}$. Files are $bbn\_vs\_neff.png$ and $bbn\_vs\_neff.pdf$.

### X-ray decay line predictions and exclusion flags
Radiative decay gives photon energy $E_\gamma = m_s/2$ and rate $\Gamma \propto m_s^5 \sin^2 2\theta$. Tool predictions assume whole-halo $f_{\rm DM}=1$ with no field-of-view cut.

* $m_s = 7.1\,\mathrm{keV}$, $\sin^2 2\theta = 7\times10^{-11}$: $E_\gamma = 3.55\,\mathrm{keV}$, $\Gamma = 1.72\times10^{-28}\,\mathrm{s}^{-1}$, $\tau = 5.82\times10^{27}\,\mathrm{s}$, fluxes $3.28\,\mathrm{ph\,s^{-1}\,cm^{-2}}$ (Milky Way center), $4.8\times10^{-4}$ (M31), $2.5\times10^{-5}$ (Perseus), flagged excluded by NuSTAR M31 (Roach et al. 2020) and XMM blank sky (Dessert et al. 2020), not independently verified with a citable quote.
* $m_s = 20\,\mathrm{keV}$, $\sin^2 2\theta = 2.8\times10^{-11}$ ($f_s \approx 1$): $E_\gamma = 10\,\mathrm{keV}$, $\Gamma = 1.22\times10^{-26}\,\mathrm{s}^{-1}$, $\tau = 8.2\times10^{25}\,\mathrm{s}$, fluxes $82.6$ (Milky Way center), $0.012$ (M31), $6.3\times10^{-4}$ (Perseus), flagged excluded by NuSTAR M31.
* $m_s = 20\,\mathrm{keV}$, $\sin^2 2\theta = 3.95\times10^{-11}$ ($f_s=1$): $E_\gamma = 10\,\mathrm{keV}$, $\tau = 5.8\times10^{25}\,\mathrm{s}$, fluxes $116$ (Milky Way center), $0.017$ (M31), $8.8\times10^{-4}$ (Perseus).

All three $f_s=1$ points at $20.2$, $29.3$, $45.4\,\mathrm{keV}$ require $\sin^2 2\theta = 3.95\times10^{-11}$, $2.02\times10^{-11}$, $9.17\times10^{-12}$ with $\Delta N_{\rm eff} = 0.00025$ to $0.00056$ and lifetimes $5.5\times10^{25}$, $1.7\times10^{25}$, $4.2\times10^{24}\,\mathrm{s}$ respectively, BBN-allowed but overclosing if taken as $100\%$ dark matter.

No numerical X-ray $\sin^2 2\theta$ limit curves were digitized. arXiv:2207.04572 has no usable HTML rendering; arXiv:1908.09037 and arXiv:1609.00667 returned only sky-map and aperture figures, not limit curves, because limit curves are PDF-only tikz/pgfplots dropped by LaTeXML.

[[FIGURE 26]]
Figure 26. Sky map of Galactic bulge $17$ to $60\,\mathrm{keV}$ flux with NuSTAR 0-bounce fields of view, illustrating X-ray search geometry.

[[FIGURE 32]]
Figure 32. NuSTAR aperture area for 0-bounce photons, showing vignetting and Pac-Man shape from optical bench obscuration.

[[FIGURE 33]]
Figure 33. Sky coverage of 0-bounce photons overlaid on INTEGRAL $17$ to $60\,\mathrm{keV}$ image, indicating stellar mass tracer.

### eV-scale short-baseline anomaly control
The short-baseline anomaly benchmark ($\Delta m^2 = 1.3\,\mathrm{eV}^2$, $\sin^2 2\theta = 0.42$, $m_s \approx 1.14\,\mathrm{eV}$) predicts $\Delta N_{\rm eff} = 1.0$ ($N_{\rm eff} = 4.044$), excluded by BBN at $\Delta\chi^2 = 23.1$ versus Standard Model and in $6.2\sigma$ tension with Planck $N_{\rm eff} = 2.99 \pm 0.17$ (CMB-S4 would see at $33\sigma$), and overcloses with $\Omega_s h^2 = 29.3$. This control confirms the tool correctly flags a fully thermalized eV sterile as excluded, while keV DW dark matter is not BBN-excluded.

### Mixed dark matter and resonant production loophole
Mixed dark matter fraction limits in arXiv:2504.06367 and arXiv:0812.0010 are derived for thermal-relic WDM and require the Viel mapping to apply to DW sterile neutrinos; direct application without mapping overstates DW exclusion. This caveat is not quantified with quote-verified curves in this run.

[[FIGURE 34]]
Figure 34. Slice through $20\,h^{-1}\mathrm{Mpc}$ Sherwood-Relics simulation at $z=4.2$, comparing CDM to $1$ and $3\,\mathrm{keV}$ WDM dark matter distributions.

[[FIGURE 35]]
Figure 35. Emulator building process with $k$-fold cross-validation and neural network, used for Lyman-alpha flux power inference.

Resonant Shi-Fuller production produces a cooler momentum distribution $\langle p/T \rangle \sim 1$ to $2$ versus DW $3.15$, relaxing the Lyman-alpha free-streaming bound by a factor $\sim 2$ in mass. DW $100\%$ dark matter is excluded by the Lyman-alpha plus X-ray combination in the board brief, but resonant remains viable. No verbatim $\langle p/T \rangle$ quotes were retrieved.

## Discussion
The results imply that non-resonant DW sterile neutrinos cannot make up all dark matter if the Lyman-alpha thermal-relic bound $m_{\rm WDM} > 5.3$ to $5.7\,\mathrm{keV}$ holds, because the mapped DW mass $20$ to $45\,\mathrm{keV}$ requires mixings $10^{-11}$ to $10^{-10}$ that are flagged by X-ray decay searches and that give the correct relic density only at those mixings. BBN and CMB $N_{\rm eff}$ do not add constraining power for keV DW masses, as $\Delta N_{\rm eff} < 0.003$ shifts $Y_p$ and $D/H$ by $<0.1\%$, well within observed $Y_p = 0.2449 \pm 0.004$ and $D/H = (2.547 \pm 0.025)\times10^{-5}$.

Agreement with literature is at the level of the mapping coefficient $4.43\,\mathrm{keV}$ and the $m_{\rm WDM}$ to $m_s$ scaling $m_s \propto m_{\rm WDM}^{4/3}$ within $1$ to $2\%$ of board floors, and the linear $\Omega_s h^2 \propto \sin^2 2\theta$ scaling verified locally at $7.1$, $20$, and $45\,\mathrm{keV}$.

The BBN impact plot slope $dY_p/dN_{\rm eff} = 0.0135$ matches standard BBN expectations, and the eV-scale control correctly reproduces full thermalization at $\Delta N_{\rm eff} = 1.0$. The keV DW points cluster at $\Delta N_{\rm eff} < 0.003$, so BBN and Planck $N_{\rm eff} = 2.99 \pm 0.17$ add no constraining power for DW dark matter, while they exclude the eV sterile at $\Delta\chi^2 = 23.1$.

Tensions with literature are not resolved in this run. The reported Lyman-alpha limits $m_{\rm WDM} > 5.3\,\mathrm{keV}$ and $m_{\rm WDM} > 5.7\,\mathrm{keV}$ are not independently verified beyond web-search snippets, and their dependence on $k_{\rm max}$, $T(z)$ priors, peculiar velocities, and patchy reionization is not quote-verified. The SDSS DR14 BOSS/eBOSS plus Planck complement and the Rogers and Poulin tension claim remain unverified. The X-ray exclusion flags for $7.1$ and $20\,\mathrm{keV}$ rely on the tool's internal NuSTAR M31 and XMM blank-sky proxy, not on digitized limit curves.

Dead ends explain why the binding constraint is incomplete:

* X-ray limit curves are PDF-only tikz/pgfplots dropped by LaTeXML, so get_paper_figures on arXiv:2207.04572 returned no figures and on arXiv:1908.09037 and arXiv:1609.00667 returned only sky-map and aperture figures, requiring manual PDF digitization outside the tool budget.
* Full-text quote verification for Viel 2005 Eq.5 coefficient $4.43\,\mathrm{keV}$, $\alpha(m_{\rm WDM})$, $T(k)$ with $\nu = 1.12$, and $k_{1/2} = 0.325/\alpha$ was blocked by tool budget exhaustion before read_arxiv_chunk could run, leaving only figure captions.
* Alternative DW mappings (half-mode, Bozek/Murgia, Abazajian) were not retrieved due to DNS failures and budget limits, so the $10$ to $20\%$ spread from extrapolation beyond $k < 5\,h\,\mathrm{Mpc}^{-1}$ is not quantified.
* Lyman-alpha systematics hierarchy and mixed dark matter fraction curves from arXiv:2504.06367 and arXiv:0812.0010 were not extracted, and no citable X-ray $\sin^2 2\theta$ limits at $E_\gamma = m_s/2$ were obtained for $7.1$, $20$, $22$, $29$, $45\,\mathrm{keV}$.
* Resonant Shi-Fuller $\langle p/T \rangle \sim 1$ to $2$ versus DW $3.15$ and the factor $\sim 2$ relaxation in mass were confirmed only by web search, without verbatim quotes.

All computations ran locally or on the hosted sterile-neutrino server, with no facility dispatch, and the $80$ of $80$ tool-call budget was exhausted.

## Limitations
What could not be established and why:

* No citable Lyman-alpha thermal-relic bound: $m_{\rm WDM} > 5.3$ and $5.7\,\mathrm{keV}$ remain at snippet level, with no verification of $k_{\rm max} = 0.2$ versus $<0.1\,\mathrm{s\,km^{-1}}$, $T(z)$ power-law versus free-floating versus $5000\,\mathrm{K}$ jump priors, or inhomogeneous reionization modeling, due to DNS failures and budget exhaustion before read_arxiv_chunk and cite.
* No quantitative DW exclusion plane: $f_{s,{\rm max,Xray}} = \sin^2_{\rm Xray}/\sin^2(f_s=1)$ and the binding Lyman-alpha versus X-ray table per mass were not built because numerical X-ray $\sin^2 2\theta$ limits were not digitized and no exclusion plot was produced.
* No mapping uncertainty: the Viel $4.43\,\mathrm{keV}\,(m_{\rm WDM}/1\,\mathrm{keV})^{4/3}$ coefficient is not quote-verified from the primary source, and alternative prescriptions were not tabulated, so the $20$ versus $45\,\mathrm{keV}$ floor robustness is not quantified.
* No mixed dark matter or resonant loophole quantification: thermal-relic mixed fraction limits and Shi-Fuller cooler momentum distribution were not extracted, so direct application to DW without mapping remains unquantified.
* No independent X-ray background limit quote: Dessert 2020 and Roach 2020/2022 were identified by web search but no verbatim quote or references.bib entry was created.

## Open directions
* Build the final quantitative DW exclusion with digitized X-ray $\sin^2 2\theta$ limits at $7.1$, $20$, $22$, $29$, $45\,\mathrm{keV}$ and compute $f_{s,{\rm max}}$ and binding constraint per mass for tool versus Abazajian normalisations.
* Quote-verify Viel 2005 Eq.5 and $\alpha(m_{\rm WDM})$ from full text and tabulate alternative DW mappings to quantify floor spread in $\mathrm{keV}$ and percent.
* Verify Lyman-alpha WDM systematics hierarchy ($k_{\rm max}$, $T(z)$ prior, patchy reionization, peculiar velocities) and SDSS DR14 plus Planck tension with citable quotes from arXiv:2309.04533, arXiv:1702.01764, and arXiv:1911.09073.
* Extract mixed dark matter fraction versus $m_{\rm WDM}$ curves and Shi-Fuller $\langle p/T \rangle$ values to test DW $100\%$ exclusion robustness and resonant viability.
* Produce the full $(m_s, \sin^2 2\theta)$ exclusion plane overlaying Lyman-alpha mapped floors, X-ray decay limits, and BBN $\Delta N_{\rm eff}$ contours for DW production.
