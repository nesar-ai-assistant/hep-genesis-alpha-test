# HEP-Genesis-Agent test session — 2026-10-21-eve-desc

- Version under test: v0.3.18 (published 2026-10-19T19:33:25Z)
- Profile: desc
- Backend: https://mag.genesis.americansciencecloud.org/v1 / claude-opus-5-5
- Cases: 10 total, 10 pass, 0 flagged
- Storage: test tree 0.36 GB (free 108.5 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | D1-meta | quick | ✅ PASS | 24.7s | exit 0 with substantive output |
| 2 | D2-ccl-theory | quick | ✅ PASS | 27.2s | exit 0 with substantive output |
| 3 | D3-datavector | quick | ✅ PASS | 48.2s | exit 0 with substantive output |
| 4 | D4-likelihood | quick | ✅ PASS | 111.2s | exit 0 with substantive output |
| 5 | D5-forecast | quick | ✅ PASS | 43.3s | exit 0 with substantive output |
| 6 | D6-txpipe | quick | ✅ PASS | 45.1s | exit 0 with substantive output |
| 7 | D7-namaster | quick | ✅ PASS | 36.3s | exit 0 with substantive output |
| 8 | D8-covariance | quick | ✅ PASS | 21.8s | exit 0 with substantive output |
| 9 | D9-skills-dispatch | quick | ✅ PASS | 30.5s | exit 0 with substantive output |
| 10 | D10-multi-desc | quick | ✅ PASS | 56.8s | exit 0 with substantive output |
## Post-run notes (manual review, 2026-10-21)

- **Fresh conversations**: run used `--chat-suffix -1021` (new harness option) so all
  10 cases started clean chats instead of resuming 10-19/10-20 conversations. This is
  the first DESC run testing chains built from scratch.
- **D8 caveat**: with fresh chats, D8's prompt ("the sacc you measured with NaMaster")
  had no prior context, so the agent correctly refused rather than fabricate. Harness
  fixed: D8 now continues D7's chat (`--chat nm`). A manual rerun on the continued chat
  (`D8-covariance-rerun.out`, `--chat nm-1021`) completed the full chain: sacc_inspect →
  namaster_mask_properties → sacc_prepare_for_firecrown → tjpcov_generate_config →
  sacc_attach_gaussian_covariance (Knox) → tjpcov_compute_covariance →
  tjpcov_compare_covariances → firecrown_build_likelihood → firecrown_compute_loglike.
  Result: TJPCov vs Knox agree to ~1%, χ² = 27.7 for 18 points (p ≈ 0.07),
  positive definite (min eigenvalue 1.11e-20). Cross-family chaining VERIFIED.
- **D6 truncation = upstream #11 recurrence**: txpipe_validate_pipeline returned 27
  dry-run commands; the tool result was cut at ~20k chars after ~8 commands. The model
  noticed and said so (did NOT misreport as fact this time). Adds a second known
  instance to HEP-KE/hep-genesis-releases#11.
- **Missing ccl family (desc_mcp_server#4, [local])**: 48/54 tools loaded; `tools.ccl`
  module absent from repo. D2 and the CCL steps of D9/D10 could not run; agent honestly
  reported "not computed" each time and suggested the fix. `conamaster` family also
  absent from `tools/` (never registered — "54 tools" counts only the 6 missing ccl_*).
- All other physics checks verified against artifacts on disk (D3 sacc 540 pts, D4
  closure χ²=0/300 after IA correction, D5 Fisher σ(σ8)=0.0062 σ(w0)=0.0165, D7
  bandpowers vs theory within cosmic variance, D10 DES Y1 test vector χ²/n=1.207).
