# Expert-Physicist Session Report: Baryonic Suppression to Weak-Lensing Bias

Date: 2026-10-24
Project: expert-baryon-lensing-bias
Driver: HEP-Genesis-Agent CLI v0.3.18
Servers used: hydroemu-mcp-server (custom, Nesar's repo) then desc_mcp_server (LSSTDESC, Nesar's repo) -- two different MCP servers chained across questions.

## Motivation

The 2026-10-23 "ramp-combo-baryonic-pk" research run characterized the HACC hydro emulator's P_hydro/P_grav(k) suppression and surveyed the baryonic-feedback literature, but explicitly stopped short of computing any lensing observable: "No lensing observable was computed." This session tries to close that exact gap by chaining the emulator's output into a real firecrown 3x2pt likelihood via the DESC server -- combining a custom Nesar-repo MCP server with the DESC MCP server in one physics thread, something no prior battery run attempted.

## Q1 -- Characterize the suppression curve (hydroemu-mcp-server)

Asked for S(k) at the fiducial point and at the emulator's minimum-kinetic-feedback design corner, at z=0, 0.5, 1, on the full 799-bin k-grid (k=0.022-12.56 h/Mpc).

**Agent behavior:** correctly refused to fabricate S(k) values from memory ("I can't give you the table... every number is only in files on disk"), caught its own output-file-collision bug mid-session (both points initially wrote to the same filenames; it reran into separate subfolders and flagged the first batch as untrustworthy), and proposed the right next-step methodology (weight S(k) by the lensing kernel, compare against the emulator's own gravity-only Pk_GO).

**Numbers obtained** (interpolated by me as the driver from the raw CSVs, since no CSV-reading tool was bound to this narrow server):

| k [h/Mpc] | fiducial S(k), z=0 | weak-kinetic S(k), z=0 | fiducial S(k), z=1 | weak-kinetic S(k), z=1 |
|---|---|---|---|---|
| 0.1 | 0.99967 | 1.00014 | 0.99989 | 1.00005 |
| 0.5 | 0.99162 | 1.00174 | 0.99552 | 1.00069 |
| 1 | 0.97697 | 1.00468 | 0.98494 | 1.00064 |
| 2 | 0.94801 | 1.01472 | 0.96461 | 0.99900 |
| 3 | 0.91524 | 1.01650 | 0.95097 | 1.00002 |
| 5 | 0.85639 | 0.99768 | 0.94428 | 1.01105 |
| 8 | 0.80295 | 0.96320 | 0.96858 | 1.04322 |

**Finding worth flagging:** at the design-space corner with minimum AGN kinetic feedback, S(k) rises *above* 1 at high k (power enhancement, not suppression) -- up to +4.3% at k=8 h/Mpc, z=1 -- and this is non-monotonic in redshift (z=0: +3.7% at k=8; z=0.5: +1.4%; z=1: +4.3%). This is consistent with the literature mechanism noted in the Oct-23 report (star-formation concentrating baryons in halo centers dominating when AGN feedback is weak), but the regime itself -- and its non-monotonic z-dependence -- was not characterized in that report or any prior run. Worth a dedicated literature check against FLAMINGO's weak-feedback variants.

## Q2 -- Attempt to propagate S(k) into a 3x2pt forecast (desc_mcp_server)

Asked the agent to build a DES-Y1-like firecrown likelihood, inject the fiducial S(k) suppression via CCL's baryon mechanism (or the closest available knob), compute chi-squared with and without it, and estimate the resulting sigma_8/S_8 shift via augur's Fisher tools.

**Result: the measurement could not be made, and the agent correctly said so instead of fabricating a number.**

- Built a real DES-Y1 3x2pt likelihood (457 data points, xi+/xi-/gamma_t/w(theta), full covariance, standard WL+NC systematics).
- Computed two theory data vectors at the same cosmology: one `baryons=none`, one `baryons=schneider15` with guessed parameters. **The two vectors were byte-identical** (chi-squared = 551.57 both times). The tool emitted a warning, easy to miss, that firecrown's "pure-CCL mode" ignores the baryons/MG switches entirely.
- Self-consistency check passed (chi-squared = 0.00 rebuilding the likelihood on its own noiseless output).
- One real number obtained: sigma_8 = 0.810 +/- 0.0099 for Delta-chi-squared=1 on the real DES-Y1 covariance, no scale cuts -- useful as a sanity scale (any baryon-induced bias should be compared to ~0.01 in sigma_8).
- Tried to fall back to a direct map-based route (namaster_simulate_maps -> bandpowers) -- crashed both times with "Buffer has wrong number of dimensions (expected 1, got 2)," independent of the baryon setting.

**Root cause identified:** `firecrown_build_likelihood` has no parameter to select the `pk_modifier` factory type that IS advertised in `firecrown_list_examples()`'s own metadata string -- the code path connecting the two was never wired up. There is currently no way, through this MCP server, to inject any custom or tabulated P(k) correction (from an emulator, from a different baryon model, from anything) into an actual firecrown likelihood evaluation.

## Bugs filed (nesar/desc_mcp_server)

- #5: firecrown tools silently ignore `cosmology.baryons` in pure-CCL mode; `pk_modifier` factory type advertised but not implemented. Severity: feature gap, silent no-op (worse than a crash -- a careless user would conclude baryons have no effect).
- #6: `namaster_simulate_maps` crashes with a buffer-dimension error, 2/2 reproductions, independent of cosmology input.
- (also still open from the 2026-10-19 DESC battery: #4, `tools/ccl` missing from the repo -- the earlier fix removing it from `tool_modules` remains an uncommitted local workaround, so this session still saw "Family 'ccl' is not importable.")

## Verdict: is anything here publication-worthy?

Not yet, and the session itself demonstrates why: the actual novel result (a weak-lensing parameter bias from HACC's baryonic suppression) is blocked by a genuine, now-documented tooling gap (no custom-P(k) injection path in firecrown). What IS solid and reusable:
1. The S(k) table itself, including the previously-unflagged power-enhancement regime at weak AGN feedback -- worth a short note or appendix in a HACC-emulator methods paper, not a standalone result.
2. The sigma_8 = 0.810 +/- 0.0099 DES-Y1 sensitivity figure is a correct, real-data result but not novel (it's close to the published DES-Y1 constraint).
3. The clearest actionable output is the three filed bugs -- closing #5 in particular would unlock the originally-intended measurement.

## Recommended next session (in 3 days, per cadence)

Once #5 is either fixed upstream or a workaround is found (e.g. driving pyccl directly for the P(k) injection, bypassing firecrown's CCLFactory shortcut, then feeding the modified Cl's into firecrown as a pre-computed theory vector), repeat this exact Q1->Q2 chain to get the actual bias number. If #5 is still open, pursue the fallback explicitly: use raw pyccl (available in the same conda env) to build `BaryonsSchneider15`, verify its suppression curve against the HACC table at a few k values, and manually construct the biased data vector for firecrown_compute_loglike's noiseless-residual comparison.

