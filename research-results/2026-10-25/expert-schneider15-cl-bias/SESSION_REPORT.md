# Session Report — Schneider15 BCM calibration & 3x2pt baryon-bias chain

**Date:** 2026-10-25
**Project:** `expert-schneider15-cl-bias`
**Chat(s):** `hydro-1025` (hydroemu-mcp-server, CLI-driven), plus direct-Python firecrown
work (see Methodology — the key measurement bypasses the MCP tool layer).
**LLM backend:** `gpt-5.6-luna@openai` on the MAG gateway (fallback; the
documented default `claude-opus-5-5` allocation `genesis-mission-october-2026-hackathon`
expired mid-session — HTTP 403 `amsc_allocation_expired` — see Blockers).

## Motivation

The 2026-10-24 `expert-baryon-lensing-bias` session set out to measure the
weak-lensing parameter bias induced by HACC's hydrodynamical baryonic
feedback (quantified via the `cosmohydro_emu`/`hydroemu-mcp-server` Pk-ratio
emulator) when a cosmic shear analysis assumes a baryon-free (or wrong-model)
matter power spectrum. That session got as far as building a real DES-Y1-like
firecrown likelihood and discovered the measurement **could not be made
through the MCP tool layer**: `firecrown_build_likelihood` generates
pure-CCL-mode YAML experiments that silently ignore `cosmology.baryons`
(desc_mcp_server#5), so two theory vectors built with
`baryons="none"` vs `baryons="schneider15"` came back byte-identical. The
recommended next step was to drive `pyccl`/`firecrown`'s Python API directly,
bypassing the broken YAML wiring, using a `PowerspectrumModifier` the way
firecrown's own shipped example (`_des_y1_cosmic_shear_pk_modifier_template.py`)
does for `BaryonsvanDaalen19`.

This session executes exactly that workaround, chaining two MCP servers'
worth of science (hydroemu-mcp-server for the HACC suppression curve,
desc_mcp_server/firecrown+pyccl for the cosmic shear likelihood) into one
pipeline, and gets the actual bias number the last session was blocked on.

## What ran

1. **hydroemu-mcp-server, via the CLI** (chat `hydro-1025`, `--quick`,
   `gpt-5.6-luna@openai`): asked for the Pk-ratio prediction at the
   emulator's fiducial design point at z=0.5, full 799-bin k-grid.
   - Output: `hydro-data/Pk-ratio_z0.5000_prediction.csv`
   - **Bug discovered and filed** (nesar-ai-assistant/hydroemu-mcp-server#1):
     `describe_parameters()` never surfaces `cosmohydro_emu.get_parameter_info()["fiducial"]`
     (`omega_m=0.14176, sigma_8=0.8102`, documented in the package README as
     `FIDUCIAL_COSMOLOGY`), even though the underlying package ships it. The
     agent in this session guessed `omega_m=0.143, sigma_8=0.82` (rounded
     range-midpoint-ish values); the *prior* session on 2026-10-24 guessed
     `omega_m=0.1375, sigma_8=0.8` for the identical "fiducial" request — two
     different wrong answers to the same question, because the tool gives no
     ground truth. **This session's downstream numbers (steps 2-5 below) use
     the agent's guessed `omega_m=0.143, sigma_8=0.82`, not the true fiducial
     — a known, documented limitation of this run** (see Caveats).

2. **Direct pyccl fit** (outside the MCP tool layer — no tool exposes BCM
   parameter fitting): fit `pyccl.BaryonsSchneider15(log10Mc, eta_b)` by
   least-squares to the HACC S(k)=P_hydro/P_grav curve from step 1 over
   k in [0.05, 10] h/Mpc (634 bins), holding `k_s=55.0` (CCL default) fixed
   and using a derived cosmology `h=0.6727`, `Omega_b=0.0492` consistent with
   the prior session's convention (h is not one of the emulator's 7 design
   parameters, so it must be assumed — another real gap, noted below).
   - **Result:** `log10Mc = 13.878`, `eta_b = 0.1707`, RMS residual in
     S(k) = 0.0105 (max |residual| = 0.0217) — a reasonable but not perfect
     fit; Schneider15's 2-parameter BCM cannot exactly reproduce a
     hydrodynamical simulation's feedback curve, and the residual is largest
     at the high-k end (k > 8 h/Mpc) where S(k) departs most from unity.
   - Files: `scripts/01_fit_schneider15_to_hacc.py`,
     `data/bcm_fit_vs_hacc_z0.5.csv`.

3. **Direct firecrown/pyccl likelihood build** (bypassing
   `firecrown_build_likelihood`'s broken YAML path entirely): reused the
   227-point DES-Y1-like shear-only sacc file + covariance from the prior
   session (`desy1_shear_only.hdf5`, src0-3, xi+/xi-, real space). Built a
   `ConstGaussian` likelihood directly in Python with a custom
   `PowerspectrumModifier` subclass wrapping the fitted `BaryonsSchneider15`,
   following firecrown's own example pattern.
   - At the DES-Y1 fiducial cosmology, evaluated chi2 with vs. without the
     baryon modifier: `chi2_no_baryons = 4622.87`, `chi2_with_baryons =
     4632.74`, raw delta = 9.87.
   - Files: `scripts/02_firecrown_chi2_comparison.py`, `data/chi2_comparison.json`.

4. **Sanity/diagnostic check** (self-correction moment, see below): decomposed
   the per-statistic theory-vector ratios (baryons/no-baryons). Confirmed the
   effect is physically sensible: xi+ is enhanced by up to +0.26% (projection
   of a real-space suppression concentrated at k>1 h/Mpc through the lensing
   kernel can produce either sign depending on scale weighting) and xi- is
   suppressed by up to -0.09%, consistently across all 10 src-pair
   combinations, with larger effects at smaller angular separations as
   expected for a small-scale-k effect.
   - Files: `scripts/03_diagnose_theory_vectors.py`.

5. **Fisher-bias propagation** (the actual target measurement): computed
   numerical derivatives dT/d(Omega_c), dT/d(sigma8) at the no-baryons
   fiducial model (step=0.01, central difference), built the 2x2 Fisher
   matrix, and propagated the baryon-induced delta-T into a parameter bias
   via the standard linear formalism (same equation as
   `augur.analyze.Analyze.get_fisher_bias`, computed independently here since
   augur's own fisher_bias tool is wired through the same broken YAML path).
   - **Result:** `sigma(Omega_c) = 0.0134`, `sigma(sigma8) = 0.0204` (shear-only,
     227 points, Omega_c+sigma8 jointly varied, all else fixed).
     Baryon-induced bias: `delta(Omega_c) = -0.0001 (-0.01 sigma)`,
     `delta(sigma8) = +0.0005 (+0.02 sigma)`.
   - Files: `scripts/04_fisher_bias_propagation.py`, `data/fisher_bias.json`.

6. **Self-correction (important):** my first framing treated the raw
   "delta_chi2 = 9.87" from step 3 as if it were the headline bias number.
   On inspection this is wrong: decomposing
   `chi2_biased - chi2_unbiased = 2*deltaT^T*Cinv*(T0-D) + deltaT^T*Cinv*deltaT`
   showed the quantity is 97% the **cross term** — i.e. dominated by how far
   the noiseless synthetic "data" vector in this particular sacc file already
   sits from the no-baryons theory, which has nothing to do with the size of
   the baryon effect itself. Only the quadratic term (0.024) is a property of
   the baryon modification alone, and even that isn't the right way to get a
   parameter bias — the correct quantity is the Fisher-bias propagation in
   step 5. This is logged in `scripts/05_sanity_check_chi2_decomposition.py`
   and was called out explicitly in the GitHub issue comment (see Bugs filed)
   so a future workaround doesn't repeat the mistake of reporting a raw chi2
   delta as "the bias."

## Numbers obtained (headline)

| Quantity | Value |
|---|---|
| HACC Pk-ratio(k, z=0.5) at (guessed, not true) fiducial | `hydro-data/Pk-ratio_z0.5000_prediction.csv` (799 bins) |
| Schneider15 BCM fit to HACC curve | log10Mc=13.878, eta_b=0.171 (k_s=55 fixed), RMS=0.0105 |
| DES-Y1-like shear-only sigma(Omega_c) | 0.0134 |
| DES-Y1-like shear-only sigma(sigma8) | 0.0204 |
| Baryon-induced bias, delta(Omega_c) | -0.0001 (-0.01 sigma) |
| Baryon-induced bias, delta(sigma8) | +0.0005 (+0.02 sigma) |

**Headline physics result:** for a Schneider15 BCM fit directly to this HACC
suite's own suppression curve, the induced bias on (Omega_c, sigma8) from a
DES-Y1-like **shear-only** (xi+/xi-, no galaxy clustering/galaxy-galaxy
lensing) analysis that ignores baryons entirely is sub-0.1-sigma — not a
dominant systematic at DES-Y1 statistical power. This is a real, if modest,
result and is plausible: DES-Y1 real-space shear correlation functions at
these scale cuts are not maximally sensitive to the k > 1 h/Mpc regime where
S(k) deviates most from unity.

## What failed / blockers

1. **MAG backend allocation expired mid-ramp-up** (`genesis-mission-october-2026-hackathon`,
   end date 2026-10-31 per the error payload, but returned 403
   `amsc_allocation_expired` already on 2026-10-25). `claude-opus-5-5` is
   unusable until reallocated; this session fell back to `gpt-5.6-luna@openai`
   (same gateway, verified tool-calling). **Action for Nesar:** check whether
   the MAG allocation needs manual renewal, or whether `scripts/test-env.sh`
   should be updated to a different default model going forward.
2. **hydroemu-mcp-server's `describe_parameters` fiducial gap** (filed,
   nesar-ai-assistant/hydroemu-mcp-server#1) means every "fiducial" query in
   every session to date (this one included) has used a slightly wrong
   cosmology. The emulator's 7 design parameters also don't include `h`,
   `Omega_b`, or `n_s` independently — those were assumed (h=0.6727,
   Omega_b=0.0492, consistent with the prior session) to convert `omega_m`
   (physical density) into `Omega_m`/`Omega_c` for pyccl. **This assumption
   is not verified against HACC's actual simulation parameter file** and is
   a second-order uncertainty in the BCM fit not propagated into the final
   error bars.
3. **desc_mcp_server#5 still open** (confirmed via `gh issue view` before
   starting) — this session's entire firecrown step required bypassing the
   MCP tool layer and hand-writing ~200 lines of direct-API Python. Flagged
   in the issue comment that this is a workable but repeat-every-session
   workaround, and (newly) that any official fix or future workaround should
   report the Fisher-bias vector as the headline number, not a bare chi2 delta.
4. `timeout`/`gtimeout` are not installed on this Mac (brew itself is broken:
   `unknown or unsupported macOS version`) — background+poll was used
   instead of a hard wall-clock cutoff for the CLI invocation.

## Bugs filed

- **nesar-ai-assistant/hydroemu-mcp-server#1** (new): `describe_parameters`
  drops `cosmohydro_emu`'s documented `FIDUCIAL_COSMOLOGY`
  (`omega_m=0.14176, sigma_8=0.8102`), forcing agents to guess the fiducial
  point — two sessions guessed two different wrong values for the same
  question. https://github.com/nesar-ai-assistant/hydroemu-mcp-server/issues/1
- **nesar/desc_mcp_server#5** (comment added, issue still open): confirmed
  still blocking; posted the validated direct-Python workaround, numbers, and
  a methodological caveat (don't report a raw chi2 delta as a parameter
  bias). https://github.com/nesar/desc_mcp_server/issues/5#issuecomment-6403684059

Logged in `~/hep-genesis-testing/ISSUES.md` as local observation #12 and an
update to #5's status.

## Verdict: publication-worthy?

**Not as a standalone result**, for the same reason flagged by the prior
session plus a new one:
1. The upstream fiducial-cosmology bug (hydroemu#1) means the "fiducial" Pk
   suppression curve used here is not actually at the true calibrated
   fiducial — the whole chain needs to be rerun once that's fixed or the
   agent is told the correct values directly, before any number here should
   be trusted as "the HACC fiducial bias."
2. The BCM fit itself is imperfect (RMS 0.0105 in S(k), worse at high-k) —
   a 2-parameter analytic model is not expected to perfectly reproduce a
   genuine hydro simulation's feedback signature; this should be reported as
   an approximation, not a measurement of HACC's "true" baryon bias.
3. `h`, `Omega_b` were assumed rather than matched to HACC's actual
   simulation parameters.

What **is** solid and reusable:
1. The workaround itself (custom `PowerspectrumModifier` injecting an
   externally-calibrated BCM into firecrown, bypassing the YAML layer) is a
   validated, general pattern — it should work for any hydro suite's S(k),
   not just this one, once run with the correct cosmology.
2. The self-correction on chi2-decomposition is a useful methodological note:
   anyone propagating a baryon (or any model) mismatch into a cosmology bias
   via firecrown should use Fisher-bias propagation, not a bare chi2
   difference at one point.
3. The DES-Y1 shear-only Fisher sensitivities (`sigma(Omega_c)=0.0134,
   sigma(sigma8)=0.0204`) are reusable sanity-scale numbers for future
   sessions on this same sacc file.

## Recommendation for next session

1. **First priority:** once hydroemu-mcp-server#1 lands (or in the meantime,
   hardcode the documented fiducial `omega_m=0.14176, sigma_8=0.8102` instead
   of guessing), rerun this exact Q1-Q5 chain with the true fiducial and
   with `h`/`Omega_b` verified against HACC's actual CosmoHydro suite
   parameters (check `cosmohydro_emu`'s source/docs for whether these are
   documented anywhere, or ask Nesar directly) rather than assumed values.
2. Extend the bias measurement to the full 3x2pt (not shear-only) sacc file
   from the prior session (`desy1_3x2pt_noiseless_0ccc86.yaml`/`.hdf5`) —
   galaxy-galaxy lensing and clustering may be more or less sensitive to the
   baryon suppression than cosmic shear alone; worth checking since this
   session only measured the shear-only piece.
3. If `--servers` chaining ever supports both hydroemu-mcp-server and
   desc_mcp_server live in the same CLI chat (currently this session, like
   the last one, had to do the firecrown half outside the CLI/MCP layer
   entirely), that would let the whole Q1-Q5 chain run as actual MCP tool
   calls instead of hand-written Python — worth testing once #5 is fixed
   upstream, since a real fix would presumably also expose this as a proper
   tool argument.
4. Check whether the MAG `claude-opus-5-5` allocation needs manual renewal
   before the next scheduled ramp-up cron jobs run — several are still
   configured to use it by default per `scripts/test-env.sh`.
