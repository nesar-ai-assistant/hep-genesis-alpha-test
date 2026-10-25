# HEP-Genesis-Agent — Issues Log

All problems encountered during alpha testing, filed on GitHub or not.
Updated automatically by the test harness (flags appended per run) and
manually by the testing agent for broader observations.

| Date | Finding |
|---|---|
| 2026-10-24 | [local] **CLI `--project NAME` silently auto-suffixes on dir collision** — if a project directory is pre-created on disk (e.g. by `mkdir` before the first `--quick` call) the CLI does not reuse it; it creates `NAME-2`, then `NAME-3` on the next invocation with the same `--project` name, rather than treating the existing empty dir as the project. Minor but confusing for scripted/cron-driven sessions that pre-stage directories. Workaround: let the CLI create the project dir itself, never `mkdir` it first. |
| 2026-10-24 | [nesar/desc_mcp_server#5] **firecrown silently ignores `cosmology.baryons` in pure-CCL mode** — `firecrown_theory_data_vector` gave byte-identical output for `baryons=none` vs `baryons=schneider15`; only a metadata warning (easy to miss) flags this. `pk_modifier` factory type is advertised in `firecrown_list_examples()` metadata but not implemented in `firecrown_build_likelihood`'s actual parameters — no way to inject any custom/tabulated P(k) correction into a real likelihood evaluation. Blocks baryon/MG/emulator-bias forecasting workflows entirely. |
| 2026-10-24 | [nesar/desc_mcp_server#6] **`namaster_simulate_maps` crashes**: "Buffer has wrong number of dimensions (expected 1, got 2)" — 2/2 reproductions, independent of `cosmology.baryons` setting. Blocks the simulate-from-scratch entry point of the NaMaster map->bandpower->covariance chain. |

Format legend: **[GH#n]** = also filed at github.com/HEP-KE/hep-genesis-releases/issues/n
**[local]** = observation not (yet) filed upstream. Status: open / fixed-in-vX / wontfix / monitoring.

---

## App bugs

### 1. `--servers <path/git>` fails for servers without `[project.scripts]` **[GH#1]** — open
- v0.3.16. CLI pip-installs the repo, then execs a console script named after
  the package dir. Servers run via `python -m mcp_server` (common HEP-KE
  pattern) crash with `FileNotFoundError`.
- Workaround: `command:` specs + wrapper scripts (`scripts/serve-*.sh`).

### 2. `arxiv_agent` Rich banner pollutes MCP stdio stdout **[GH#2]** — open
- v0.3.16. smolagents console output goes to stdout of the stdio MCP server:
  1,663 `Failed to parse JSONRPC message` pydantic errors in one 5-min
  research run. Client survives; protocol pollution; real errors hard to spot.
- Evidence: runs/2026-10-15/cases/09-research-arxiv.out lines ~287–330.
- **Reproduced 2026-10-22 pm-combo on v0.3.18** — first reproduction since
  10-15 and first in combo mode: 9,877 JSONRPC parse errors in C1
  (transcript 8.9 MB, vs 92–104 KB / 0 errors in the three prior combo
  runs). Trigger is deterministic: this run's workers made 6 `arxiv_agent`
  sub-agent calls (first combo run to do so); the same-day midday research
  run with 0 arxiv_agent calls had 0 errors. #3's failures compound inside
  the flood (`'1912.07795 error Object ...has no attribute search'` lines
  in the pydantic input_value). Corrected the "not reproducing" note on
  GH#2 with the full table. Also worth noting: 4/6 arxiv_agent calls
  partially succeeded via arXiv-HTML reads, so #3 is softer than "always
  fails" — the `'Search'.results` crash hits the PDF download path only.

### 3. `arxiv_agent` full-text extraction broken **[GH#3]** — open
- v0.3.16. Sub-agent PDF/TXT downloads fail:
  `RuntimeError: 'Search' object has no attribute 'results'` (python-arxiv API
  misuse). Degrades to abstract-level synthesis (honestly, to its credit).
- 2026-10-16 correction: `download_full_arxiv_paper` ALSO crashes with the
  same 'Search'.results error (pm-combo tc-261016_1-w1-d-04-53,
  tc-261016_1-w2-d-03-81). `download_arxiv_full_text` itself works — 8/8
  succeeded in the midday run (files on disk) — so the bug is confined to
  the sub-agent extraction path. Commented on GH#3.

## Environment / packaging notes **[local]**

### 4. Wheel install requires Python ≥3.10; macOS system python is 3.8
- Not a bug, but a setup trap: use conda/venv python 3.10+.

### 5. `pip install cryptography` tries to build v50.0.2 from source on this Mac
- Environment quirk: fresh venvs on this machine resolve cryptography 50.0.2
  (no compatible wheel) → Rust/OpenSSL build fails. Pre-install
  `cryptography<49` in new venvs before anything that pulls it transitively.

### 6. All three HEP-KE MCP server repos share the top-level package name `mcp_server`
- Installing more than one into the same environment collides. Per-server
  venvs + `command:` wrappers are the robust pattern (also sidesteps #1).

### 7. hydroemu server pins `scipy<1.11` → needs Python ≤3.11
- Its venv must be 3.11, not 3.12 (scipy<1.11 has no 3.12 wheels).

## Behavior observations (not bugs, worth watching) **[local]**

### 11. `--board` auto-creates missing projects **[local → GH#4]**
- v0.3.16 (found 2026-10-15, features battery F2/F3). Running `--board
  --project <name>` on a NONEXISTENT project silently creates the project
  directory, then prints "No board for chat 'default'...". Read-only info
  commands should not have filesystem side effects.

### 12. `--list-runs` on empty project prints nothing **[local → GH#4]**
- v0.3.16. Exit 0, zero output — indistinguishable from success-with-runs in
  scripts. Should print "no runs yet" (and `--list-projects` similarly prints
  nothing when empty).

### 8. Research-mode tool budget consumed quickly by full-text reading
- In run 261015_205132-26af, direction d-01 closed with "Tool budget was
  exhausted before full-text chunk reading, figure extraction…". Bounded runs
  (--max-tool-calls 25) are too tight for literature work with chunked
  reading; 50–60 is more usable. Consider a budget hint in docs.

### 9. IDM server labels 9.8σ deviations "consistent" (Nesar's server, not the app)
- inelastic-dm-server's consistency labeling is too lenient vs its own quoted
  uncertainties (1.1 TeV higgsino: Ωh²=0.108 vs Planck 0.120±0.0012 labeled
  "consistent"). Flagged for the inelastic-dm-server repo.

### 10. Research report figure dir empty when no figures extracted
- reports/<ts>/figures/ exists but empty when the run produced no plots —
  harmless, but the report PDF then has no figures; consider omitting.

### 13. hydroemu predict_observable returns files but no bin values inline
- In runs 261016_083303 and 20261015_223937, predict_observable writes the CSV
  and PNG but the tool response carries only file paths + a one-line message,
  so the CLI agent cannot quote amplitudes/ratios and falls back to
  qualitative interpretation ("check them against Figure 10"). Consider
  embedding a compact summary (bin centers/values or knee/endpoint stats) in
  the tool payload. (Nesar's server, not the app.)

### 14. arXiv API transient failures (HTTP 429/503) reported as "Paper not found" **[GH#5]** — open
- v0.3.16 (found 2026-10-16 pm-combo). `get_arxiv_metadata`,
  `download_arxiv_full_text` and `cite()` surface arXiv export-API rate
  limits (HTTP 429) and outages (HTTP 503) as the message "Paper <id> not
  found" — with no HTTP status, no retry, and no hint the paper exists.
  Consequences in one run: research direction d-03 closed as **blocked**
  ("no full text could be read and no quote could be validated with cite()"),
  and the board asserted "these results say nothing about whether the papers
  exist". The agent even flagged the OpenAlex mirror returned June-Oct 2026
  "papers" that should be verified on arxiv.org before citing.
- Proof it is masking, not truth: arXiv:1807.06209 (Planck 2018) downloaded
  fine at 11:08 (442 KB on disk, midday run) and returned "not found" at
  14:35 in the pm-combo run — same wheel v0.3.16, same machine, same day.
  Meanwhile `search_arxiv_abstracts` in the same failing calls returned the
  real "Search failed: Page request resulted in HTTP 503/429 (export.arxiv.org)"
  errors, proving the underlying API was rate-limiting.
- Fix suggestion: propagate the HTTP status ("arXiv API returned 429 Too Many
  Requests — transient, retry with backoff"), add retry/backoff, and have
  `cite()` fall back to OpenAlex metadata instead of hard-failing.
- Evidence: runs/2026-10-16-pm-combo/cases/C1-multi-server-research.out
  lines 599-608, 822-836; runs/2026-10-16-midday-research (8/8 downloads OK).

### 15. Token-usage line prints "82K in (701 cached)" — units bug **[local]** — open
- v0.3.16 (found 2026-10-16 pm-combo). The per-phase token summary line
  prints the cached-token figure for the report phase as "(701 cached)"
  instead of e.g. "(701K cached)" or "(701,000 cached)" — inconsistent with
  every other phase, which uses K-scaled values ("813K cached"). Compare:
  pm-combo: "report 82K in (701 cached) · 16K out"; midday: "report 46K in ·
  8.0K out · 1 call" (no cached figure at all when the value is small).
- Cosmetic but confusing: a human skimming the line reads "701 cached" as
  701 tokens (or 701K?) and cannot tell which. Likely a missing `K` suffix or
  a division slip in the report-phase token formatter.
- Evidence: runs/2026-10-16-pm-combo/cases/C1-multi-server-research.out
  line 858; runs/2026-10-16-midday-research/cases/R1-higgsino-dd.out line 802.

### 16. Quick `--report` + query asking for a report → report generated twice **[GH#6]** — open
- v0.3.16 (found 2026-10-15, confirmed 2026-10-16). When the `--quick` query
  asks for a report in natural language AND `--report` is passed, the report is
  built twice: once by the in-turn `write_report` tool call, once by the
  post-turn `--report` pass. Two full report folders (~580 KB each) 39 s
  apart, same title/conversation_id, double report-model cost + pdflatex.
- Reproduced 3/3 (runs/2026-10-15-r1-features, 2026-10-16-eve-features and
  2026-10-17-eve-features, case F6). Latest: folders 261017_170213 (tool) and
  261017_170253 (flag pass), 40 s apart.
- Filed upstream: https://github.com/HEP-KE/hep-genesis-releases/issues/6

### 17. Invalid `--servers` spec → raw pip traceback, no usage hint **[GH#7]** — open
- v0.3.16 (found 2026-10-16, ad-hoc verification). `--servers sbbn` (bare
  name) makes the CLI run `pip install git+sbbn`, which fails with
  `ERROR: Invalid requirement: 'git+sbbn'` and an uncaught RuntimeError
  traceback, exit 1. No indication of the accepted spec formats
  (`command:`, `module:`, path, git URL, https …/mcp|/sse).
- Root cause: ServerPool._install (mcp.py) prepends `git+` to any non-module,
  non-command, non-URL token and lets pip validate it.
- Filed upstream: https://github.com/HEP-KE/hep-genesis-releases/issues/7

### 18. Workspace skills require `name:` frontmatter — silently skipped otherwise **[local, docs]** — open
- v0.3.16 (found 2026-10-16, F8 follow-up). `workspace_skills()` only lists
  `.md` files whose YAML frontmatter has a `name:` key; files without it are
  silently dropped from `--list-skills` and `load_skill` ("Available:
  (none)") with no warning. Not a crash, but easy to hit: a plain markdown
  recipe in `$HEP_WORKSPACE_DIR/skills/` looks ignored.
- The CLI `--help` and the releases-page docs don't mention the frontmatter
  requirement either — worth a doc line upstream (not filed; low priority).
- Verified the positive path after adding frontmatter: `--list-skills` lists
  the skill and `load_skill` returns its full text. `remember`/MEMORY.md
  persistence across invocations also verified working (single entry, no
  duplicates; F7 agent correctly refused to re-save an existing lesson).
- Test-env fix: `workspace/skills/statistical-analysis.md` now exists with
  proper frontmatter so F8 exercises the real load path in future batteries.

### 19. Board findings store evidence as bare tool-call IDs — no excerpt text **[local, app quality]** — open

Observed 2026-10-17-midday-research (baryonic-pk, v0.3.16): all 21/21 board
findings have `evidence: [{tool_call_id: ...}]` with **empty** `note` fields,
and no claim text/quotation is stored in the finding record itself. The run's
own wave-2 critic flagged exactly this ("Future findings should store the
exact matching snippet as the excerpt") and had to accept claims on the
plausibility of chunk ranges rather than verbatim quotes. Consequence: the
final report says "issues" trace only to tool-call IDs, and report-time
re-verification can't see what the worker actually read. Spot-checking
claims against downloaded full texts still verified them (OWLS AGN
1%/10%/30% at k≈0.3/1/10 h/Mpc and Amon & Efstathiou A_mod=0.69±0.06 both
verbatim in sources), but the board itself carries no reproducible quote.
Suggested upstream: persist the exact matched text snippet (chars offset +
length, or the first ~300 chars) in each evidence entry at finding-creation
time.

### 20. `load_table_data` cannot parse CSVs with a column-name header row **[GH#8]** — open

- v0.3.16 (found 2026-10-17-pm-combo, baryonic-pk, 4-server combo). The
  bundled DOM tool `load_table_data` fails on its sibling HYD server's own
  prediction CSVs: `Error: could not convert string 'x' to float64 at row 0,
  column 1.` The CSV is 5 `#` comment lines + `x,y_mean,y_std` header + 799
  numeric rows — the exact format the emulator's `predict_observable` writes.
- Root cause: `load_table_data()` = `np.loadtxt(path)` with fallback
  `np.loadtxt(path, delimiter=",")` — no header-row skipping; docstring
  claims `#`-comment support but not header support. Verified: both calls
  fail; `skiprows=6` works (799×3, k_max=12.56 vs 3.7 reachable via
  read_text_file fallback).
- Consequence in run: agent fell back to `read_text_file`, which truncated
  near k≈3.7 h/Mpc, so the suppression minimum was never resolved; agent
  posted question q-06 about it on the board; final report says suppression
  "is still deepening at k≈3.7 h/Mpc, the largest wavenumber that could be
  read from the output".
- Filed upstream: https://github.com/HEP-KE/hep-genesis-releases/issues/8

### 21. Direction closed with `result: null` — board loses that direction's summary **[local, app quality]** — open

- v0.3.16 (found 2026-10-17-eve-features, F2 `--board` on
  ramp-combo-baryonic-pk, run 261017_143153-5151). Direction d-03
  (per-parameter sensitivity + redshift evolution of the Pk-ratio
  suppression, wave 0) has `status: "closed"` but `result: null` in
  board.json — the only one of 23 closed directions across all six boards
  with no result text. All other closed directions carry multi-paragraph
  results.
- Consequence: `--board` renders `d-03 [closed] <goal>` with no
  `-- result:` clause, and the report/`--board` consumer cannot say what
  d-03 actually established. The underlying work was evidently done
  (critique c-03 and dead-end x-01 reference the kappa_w=2/4, M_seed=2
  runs, and f-014 carries the sensitivity numbers) — likely the planner
  closed d-03 as superseded by d-05 without writing a result.
- Suggested upstream: when closing a direction, require a non-empty result
  (or persist an explicit `closed_as_superseded_by: d-05` marker) so no
  closed direction is silent. One occurrence so far — monitoring; will file
  upstream if it recurs.

### 22. Plan-phase brief falsely claims MCP server tools are unavailable **[GH#9]** — open

- v0.3.16 (found 2026-10-17-pm-combo, reproduced 2026-10-19-pm-combo; 4-server
  research mode, 2/2 occurrences). The `[brief]` produced after the survey phase
  warns that domain-server tools "are not among the available tools" / "Only
  arXiv and web search tools were provided" — even though the same transcript
  shows the survey agent successfully probing those very tools seconds earlier,
  and the brief's own next line says "52 tools on 5 servers".
- 2026-10-17: brief said "none of my tools is a hydrodynamics or
  baryonic-emulator tool"; workers then called `predict_observable` /
  `describe_parameters` 10×.
- 2026-10-19: brief said sterile-nu tools are absent; workers then made ~19
  sterile-nu tool calls (predict_sterile_nu_grid, predict_sterile_nu_xray_line,
  scan_sterile_nu_parameters, …). The final report had to issue a correction:
  "The brief stated that no sterile-neutrino production tools were available.
  In fact a sterile-neutrino server was reachable and was used."
- Self-healing but costly: in both runs the plan critic caught the false claim
  and redirected ("The survey wrongly said these tools are absent"), wasting
  critic revisions; and in the 10-17 run the survey's claimed tool absence
  shaped the initial direction set.
- Likely cause: the brief/survey summarizer sees only arXiv/web tool results in
  its context (survey probes of domain tools may not be passed to it, or the
  summarizer prompt asks only about literature tools). Survey inventory should
  be grounded in the ListTools output it already collects.

### 23. sterile-nu server DW yield normalization 10–16× low vs literature **[Nesar's server, not the app]**

- Found 2026-10-19-pm-combo (ramp-combo-lyman-wdm). Against the Abazajian 2005
  DW fit (Ω_s h² ∝ (sin²2θ)^1.23 m_s², valid 135 < T_QCD < 300 MeV), the
  server's DW relic curve sits 10–16× too low in mixing angle at fixed mass:
  server scaling is linear in sin²2θ and ~m^1.8, literature is (sin²2θ)^1.23
  and ~m². Consequence: server production fractions f = Ω_s h²/0.12 are
  overstated by 1.5–2 orders of magnitude at the X-ray-allowed mixings.
- Secondary: at the server's own relic curve (Ω_s h² = 0.12) the tool labels
  3 of 5 points "overcloses" despite Ω_s h² = 0.12 exactly — strict/rounded
  inequality in the threshold check.
- Also noted by the agent: tool's built-in X-ray limits have no coverage at
  29–46 keV (gap reads as "allowed" in plot_sterile_nu_exclusion), and
  exclusion verdicts return no limit values.
- Flagged for the sterile-nu-bbn server repo; report has full details
  (research-results/2026-10-19/ramp-combo-lyman-wdm/).
- 2026-10-20-am-core (v0.3.18) reconfirmation: 6-point DW grid scan
  (1–50 keV, sin²2θ=3×10⁻⁹) shows f ∝ m_s^0.80 exactly (constant to 4
  digits across the QCD transition) and Ω_s h² ∝ m_s^1.8, linear in
  sin²2θ — consistent with the fitted-power-law diagnosis above. The
  agent itself noted the constant exponent implies a fitted power law
  rather than a production-equation solve.

### 24. DESC MCP server: `tools.ccl` module listed in pyproject.toml but never created **[local, Nesar's server]** — open

- Found 2026-10-19-eve-desc. `pyproject.toml [tool.mcp-server].tool_modules`
  lists `"tools.ccl"` and `tools/meta/registry.py` FAMILIES maps
  `ccl → tools.ccl`, but no `tools/ccl/` package exists in the repo
  (git history: never committed). Server crashes on startup with
  `ModuleNotFoundError: No module named 'tools.ccl'`.
- Workaround: commented out `tools.ccl` in pyproject.toml; server starts
  with 48 of 54 tools (6 CCL-family tools absent). `describe_desc_tool_family("ccl")`
  returns "not importable" but doesn't crash.
- Impact: the CCL-family tools (background distances, P(k), angular C_ell,
  correlation functions, halo model, SRD n(z)) are the foundation for most
  cross-family chains. Without them, agents use augur/firecrown tools as
  workarounds (which internally call pyccl but don't expose raw CCL).
- Action: create `tools/ccl/__init__.py` implementing the 6 tools
  referenced by the registry (ccl_* prefix). The pyccl import path works
  fine in the env (pyccl 3.3.6 installed).
- **Added 2026-10-23-eve-desc**: `list_desc_packages` still advertises ccl
  as an *active* package with a full description ("pyccl theory predictions:
  background, P(k), C_ell, xi, halo model, SRD n(z)") even though the family
  is not importable. Registry metadata should probe importability and mark
  the family unavailable/degraded instead of "active" — agents (and the
  D1/D2/D10 cases) burn calls discovering the mismatch at runtime.

### 25. DESC MCP server env: osx-64 conda-lock not shipped; classic conda solver hangs **[local, setup]** — fixed

- Found 2026-10-19. The repo's `conda-lock.yml` ships only linux-64 and
  osx-arm64 platforms. This host (macOS x86_64 / osx-64) requires a platform-
  specific re-solve. The prior attempt used `uvx conda-lock lock --conda conda`
  where `conda` was version 4.7.12 (pre-libmamba) — the solver ran for 2.5h
  at 100% CPU / 8.4 GB RSS without converging.
- Fix applied: killed the stuck solver; used the repo's embedded micromamba
  2.9.0 to solve directly from `environment.yml` (libmamba solver, ~2 min),
  then `pip install --no-deps -e .` for the server + pip-only deps. The
  repo's `scripts/env.sh` was not used because it requires `uvx` for
  `--relock` (available via `~/.hermes/bin/uv`) and its default path uses
  the shipped lock (which lacks osx-64).
- Also fixed: `serve-desc.sh` lacked the executable bit (chmod +x applied).

### 26. Research mode: final tool-call count exceeds `--max-tool-calls` in every run **[GH#10]** — open

- Found 2026-10-20 (pm-combo, v0.3.18). The final `[run] done (..., tool
  calls F, ...)` line exceeds the `--max-tool-calls B` budget in 11 of 12
  research runs on record (v0.3.16 + v0.3.18, both backends): overages +1
  to +8, never under. Today's combo: B=50, F=53 (+3 = exactly the 3
  parallel workers).
- Mechanism: check-then-call race — workers check remaining budget before
  dispatching, so up to `--workers` in-flight calls land after the counter
  crosses the limit. Wave 2 today started at 29 calls with 21 remaining and
  consumed 24.
- Low severity (cost-control softening, not correctness). Filed as
  HEP-KE/hep-genesis-releases#10 with the full 12-run evidence table.

### 27. Quick mode: MCP tool results silently truncated at 20,000 chars, no marker **[GH#11]** — open

- Found 2026-10-20 (eve-desc, v0.3.18; also present in 2026-10-19-eve-desc
  case D6). `txpipe_validate_pipeline` returns 27 per-stage dry-run commands;
  the model sees only the first ~7 and reports "the response was cut off
  partway through the eighth". Server-side result is complete — verified in
  desc_mcp_server source (full list in tool metadata, no server truncation).
- Hard evidence from the persisted chat record
  (`projects/ramp-desc/chats/txp.json`): `raw` length exactly 20,000, ends
  mid-token inside command 8, no truncation marker.
- Root cause: `hep_genesis/agent/quick.py` `_execute()` → `"raw":
  text[:20_000]` fed to the model via `ToolMessage(content=rec["raw"][:40_000])`
  with no marker. Research mode appends `[... N more chars in the ledger]`
  (nodes.py:199); quick mode has no equivalent. Same unmarked slice in
  `agent/research/tools.py:147` (compensated downstream, but the stored
  `raw` is still silently clipped).
- Consequence: the model misreports tool output as fact ("only 7 of 27
  commands") or believes data doesn't exist. Caught twice in DESC battery D6;
  judge heuristic can't see it (rc=0, substantive output → PASS).
- Filed upstream: https://github.com/HEP-KE/hep-genesis-releases/issues/11
  with the exact code lines and both run transcripts as evidence.

### 28. Fixed `--chat` names make repeat core batteries resume stale conversations — no fresh tool chains **[local, harness design]** — open

- Found 2026-10-21 (am-core, v0.3.18). Cases 04/05 (sbbn chat) answered
"this is the fifth/sixth time you've asked" and made **zero new tool calls**
(token line: `1 call` = the ListToolsRequest only); case 07 (hydro chat)
likewise "sixth time you've asked for this". The agent correctly reasoned
results were deterministic and replayed earlier grids instead of re-chaining.
- Cause: harness uses fixed chat names (`--chat sbbn`, `idm`, `hydro`, `dom`,
`multi`) in `build_cases()` core profile; at 4-6 batteries/day during ramp-up
each run resumes the previous conversation in that chat file. Same caveat the
skill documents for the DESC battery — it applies to ALL profiles.
- Consequence: core battery loses its fresh-chain signal for tool use /
multi-server orchestration; passing is still meaningful (CLI, reasoning,
replay path), but "PASS" no longer exercises the tool-call path from scratch.
Judge heuristic can't see this (rc=0, substantive output → PASS).
- Fix (harness-side, no app bug): rotate chat names per run — append the
  run_id date suffix to chat names in `build_cases()`, e.g. `--chat sbbn-1021`.
  For DESC battery, same: `--chat meta-1021` etc. Not filed upstream —
  harness design, not an app defect.
- Follow-up 2026-10-21: chat names still fixed; am-core 10-21 cases again
  replayed prior results. Rotate before the next core battery.

### 29. `--report`: first-pass LaTeX compile failure, silently auto-recovered — seen in 7 of 18 report runs (~39%) **[local observation, app quality]** — open

- Seen 2026-10-21 pm-combo (v0.3.18). C2 report build printed
  `LaTeX failed to compile — asking the report model to fix its markup…`
  then compiled successfully on retry. All three PDFs valid (report 10 pp /
  3,850 words, supplement, transcript).
- **CORRECTION 2026-10-23 (pm-combo): the "first occurrence" claim above was
  wrong.** Re-grepping all `runs/*/cases/*report*.out` shows the failure in
  2026-10-16-midday, 2026-10-17-midday and 2026-10-20-midday as well —
  identical `Compiling PDF… / LaTeX failed to compile… / Compiling the
  supplement and the transcript…` sequence. The earlier note's "not seen in
  any prior report run" was a record-keeping miss, not reality.
- **Actual pattern as of 2026-10-23: 7 of 18 report runs (~39%) hit a
  first-pass LaTeX compile failure; every one auto-recovered on the report
  model's retry and produced three valid PDFs.** Occurrences: 10-16-midday,
  10-17-midday, 10-20-midday, 10-21-pm-combo, 10-22-pm-combo,
  10-23-midday-research, 10-23-pm-combo (today: report 10 pp / supplement
  59 pp / transcript 39 pp, all valid after retry).
- **Filed upstream 2026-10-23 as HEP-KE/hep-genesis-releases#13** after the
  re-grep revealed the real frequency (7/18, ~39%) — the systematic-rate
  evidence plus the invisible-failure-cause problem (first-pass report.log
  is overwritten by the retry) justified it. Recovery path works every
  time; ask is: retain failure artifacts + deterministic .tex sanitizer
  pass. All 7 occurrence logs offered to upstream.
- **Second occurrence 2026-10-22 pm-combo** (v0.3.18, C2 for the higgsino-dd
  combo run): same `LaTeX failed to compile — asking the report model to fix
  its markup…` → successful retry. All three PDFs valid (report 307 KB,
  supplement 950 KB, transcript 352 KB; 4 figures). Two occurrences in two
  consecutive pm-combo runs, both on long multi-figure research boards —
  still auto-recovered both times, but the pattern is now real, not a
  one-off.

 ---

 ## Run log (auto-appended by harness)


## 2026-10-15-r1-core — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-15-r1-features — 8 pass / 1 flagged

### F3-list-runs — List research runs

- rc=0, duration=1.2s, note: rc=0, output=0 chars

- transcript: runs/2026-10-15-r1-features/cases/F3-list-runs.out


## 2026-10-16-am-core — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-16-midday-research — 2 pass / 0 flagged

Clean run — no flags.


## 2026-10-16-pm-combo — 3 pass / 0 flagged

Clean run — no flags.


## 2026-10-16-eve-features — 9 pass / 0 flagged

Clean run — no flags.


## 2026-10-17-am-core — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-17-midday-research — 2 pass / 0 flagged

Clean run — no flags.


## 2026-10-17-pm-combo — 3 pass / 0 flagged

Clean run — no flags.


## 2026-10-17-eve-features — 9 pass / 0 flagged

Clean run — no flags.


## 2026-10-19-am-core — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-19-midday-research — 2 pass / 0 flagged

Clean run — no flags.


## 2026-10-19-pm-combo — 3 pass / 0 flagged

Clean run — no flags.


## 2026-10-19-eve-desc — 10 pass / 0 flagged

Clean run (after fixing two setup issues; see #24, #25).
First DESC battery: all 10 cases passed, including multi-family chains
D3 (CCL→sacc→augur→sacc_inspect), D4 (augur→sacc→firecrown, χ²=0.00),
D7 (namaster simulate→compute_cls→sacc), D10 (meta→firecrown→convert_cosmology).
v0.3.18 on claude-opus-5-5. 48 of 54 tools loaded (6 CCL tools absent, see #24).


## 2026-10-20-am-core — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-20-midday-research — 2 pass / 0 flagged

Clean run — no flags.


## 2026-10-20-pm-combo — 3 pass / 0 flagged

Clean run — no flags.


## 2026-10-20-eve-desc — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-21-am-core — 10 pass / 0 flagged

Clean run — no flags.


## 2026-10-21-midday-research — 2 pass / 0 flagged

Clean run — no flags.


## 2026-10-21-pm-combo — 3 pass / 0 flagged

Clean run — no flags.


## 2026-10-21-eve-desc — 10 pass / 0 flagged

Clean run — no flags.


Notes (manual review):
- **Fresh-chat run** (new harness `--chat-suffix -1021`): first DESC battery where all
  chains were built from scratch rather than resumed. 10/10 pass.
- **[local] D8 test-design flaw (fixed)**: D8's prompt assumed a NaMaster sacc from a
  prior turn; with fresh chats the agent correctly refused instead of fabricating.
  Harness fixed: D8 now continues D7's chat (`--chat nm`). Manual rerun on the
  continued chat completed the full 9-tool cross-family chain (sacc → mask →
  prepare_for_firecrown → tjpcov config/cov/compare → Knox → firecrown loglike):
  TJPCov↔Knox agree ~1%, χ²=27.7/18 (p≈0.07), positive definite. Chaining verified.
- **upstream #11, 3rd recurrence (D6)**: txpipe_validate_pipeline tool result again
  truncated at 20k chars (~8 of 27 dry-run commands). Difference from prior runs: this
  time the model NOTICED and disclosed the cut-off ("output was cut off after about 8
  of them") instead of misreporting — with the fresh chat there was no prior-run
  memory to anchor a wrong belief. Still silent truncation server-side; comment added
  to HEP-KE/hep-genesis-releases#11.
- **[local] desc_mcp_server#4 persists**: 48/54 tools; `tools.ccl` module missing.
  D2/D9/D10 CCL steps ran as honest "not computed" refusals. Also confirmed
  `conamaster` family is absent from `tools/` entirely (never registered).

## 2026-10-22-am-core — 10 pass / 0 flagged

Clean run — no flags.

Notes (manual review):
- **[harness, fixed] Core battery was resuming week-old chats**: every quick case
  opened `chats/<name>.json` in `ramp-core` that has been resumed daily since
  10-16. The agent said so outright ("sixth/seventh time you've asked", "Figure
  45", "nothing was recomputed"). Cases 04 and 10 made **zero new tool calls**,
  answering purely from prior context — so today's PASSes test conversation
  memory, not fresh tool use. Same flaw the 10-21 DESC run fixed with
  `--chat-suffix -1021`, but core/research/combo never passed the flag.
  **Fix applied in harness.py**: fresh chats are now the DEFAULT — every run
  auto-appends a `-MMDD` date suffix to all `--chat` names (pass
  `--resume-chats` to restore old behaviour). Within-run continuations
  (D7→D8 `--chat nm`) keep working since all cases share the same suffix.
  Effect verified for today's run: it ran BEFORE the fix, so its PASSes reflect
  resumed context. Tomorrow's batteries will be the first fresh-chat core run.
- **Physics quality on resumed chats still strong** (case 04): DW production
  f ∝ m_s^0.8 / Ω_s h² ∝ m_s^1.8 scaling derived correctly across 1–50 keV,
  with honest caveats (suspects the tool's power-law fit; flags both points
  overclose; notes ΔN_eff far below BBN limit). Case 05 correctly solved
  Y_p +1% at N_eff ≈ 3.229 via DW mixing scan. Case 06: Ω_χ h² = 0.0823,
  x_f = 22.4, T_f = 4.46 GeV for 100 GeV WIMP, σ=31 tension vs Planck — all
  consistent with prior runs and textbook expectations.
- **Recurring pattern [local, #13]**: hydroemu cases (07, 08) again returned
  files+plot but no inline bin values, so the agent correctly refused to quote
  amplitudes and narrated expected physics instead — right behaviour for a
  truncated tool response, but it means hydro cases still can't verify numeric
  predictions end-to-end (ISSUES.md #13).
- No new upstream-worthy bugs: truncation (#11) not triggered today (no
  >20k-char tool results); #10 budget overrun is research-mode-only.


## 2026-10-22-midday-research — 2 pass / 0 flagged

Clean run — no flags.


## 2026-10-22-pm-combo — 2 pass / 1 flagged

**Diagnosis: known GH#2 reproducing in combo mode for the first time — no
new bug.** C1's research run completed cleanly (status `done`, 47/50 tool
calls, 2 waves, 28 findings: 17 supported / 11 contested, 0 tool errors);
the flag is purely traceback noise from 9,877 `Failed to parse JSONRPC
message` errors (vs 0 in the three prior combo runs). Trigger: the workers
made 6 `arxiv_agent` sub-agent calls — first combo run to do so — and each
spews the smolagents Rich banner on the stdio server's stdout (GH#2).
Correlation is deterministic: same-day midday research run (same wheel,
backend, topic) made 0 arxiv_agent calls → 0 errors. GH#3 also visibly
compounded inside the flood (`input_value='1912.07795 error Object ...has
no attribute search'` lines). Notably 4 of the 6 arxiv_agent calls
*partially succeeded* via arXiv-HTML reads (LZ 1 TeV limit ≈ 3.1e-47 cm²,
Hill & Solon bounds) — better than #3's "always fails" title suggests;
the 2 failures are the known `'Search' object has no attribute` path.

4-server orchestration worked: 26 calls routed to serve-idm.sh (relic
density, recoil, constraints), 14 to hep-research-aid (arXiv), 18 board
ops, 1 each to sbbn/hydro (topic-appropriate restraint — DM topic didn't
need hydro predictions; the agent still listed hydro's tools/datasets to
check applicability). Budget respected this run (47/50) — GH#10 did NOT
reproduce. Report: first-pass LaTeX failure again auto-recovered (#29,
second occurrence).

### C1-multi-server-research — Research with 4 servers: Higgsino thermal target vs direct detection

- rc=0, duration=1393.6s, note: traceback present (run may have continued)

- transcript: runs/2026-10-22-pm-combo/cases/C1-multi-server-research.out


## 2026-10-22-eve-desc — 10 pass / 0 flagged

Clean run — no flags. First DESC battery where all 10 cases ran fresh chats
AND the D8 harness fix (continue D7's chat) worked with no manual rerun.

- **Cross-family chains: all verified.** D3 augur→sacc_inspect (540-pt sacc,
  10 tracers, PD covariance); D4 augur→sacc_attach_gaussian_covariance→
  firecrown closure test — first eval χ²≈2×10⁶ on augur's datavector, agent
  self-diagnosed the model mismatch, regenerated a firecrown-theory sacc and
  got χ²=0.00/300 (honest failure+recovery, no fabrication); D7→D8 same-chat
  chain namaster→sacc_prepare_for_firecrown→tjpcov config+compute→Knox
  comparison (agree ~1%)→firecrown χ²=27.7/18, p≈0.07, PD; D10 firecrown DES
  Y1 test vector χ²/n=1.207 (matches 10-21 run exactly). D5 augur Fisher:
  σ(σ8)=0.0062, σ(w0)=0.0165 (matches 10-21).
- **[local] desc_mcp_server#4 persists**: 48/54 tools, `tools.ccl` still
  missing. D2/D9 tour step 2/D10 step 1 all blocked; agent honestly refused
  to quote numbers each time (correct behaviour). D9 auth_status: local
  dispatch.
- **GH#11 third instance (D6)**: `txpipe_validate_pipeline` returned 27
  dry-run commands, tool result cut at ~20k chars after ~8 commands — same
  tool as the 10-21 instance, deterministic repro. Model NOTICED and
  disclosed ("assembled, not copied") — no misreporting this time. Comment
  added to HEP-KE/hep-genesis-releases#11.
- No new upstream-worthy bugs; #10 (budget) N/A — quick mode only.


## 2026-10-23-am-core — 10 pass / 0 flagged

Clean run — no flags. Fresh chats (suffix `-1023`, 8 chats rotated). No
GH#2 banner noise (no arxiv_agent calls — quick mode only), no GH#11
truncation hits, GH#10 N/A (quick mode).

- **[local] inelastic-dm server: `consistent_planck` flag contradicts the
  tension it ships next to.** Case 10 (multi-server) raw tool output:
  `compute_relic_density(m_chi=1000 GeV, higgsino)` → Ωh² = 0.0898 with
  `tension_sigma` = 25.1σ (Planck-only) yet `consistent_planck: true`.
  Root cause is in our server, not the CLI:
  `inelastic-dm-server/tools/cosmology.py:171` defines the flag as
  `tension_with_theory_err < 2.0` where the theory error is a 15%
  systematic (≈0.018) — the 0.0898 point is 1.67σ in that metric, so the
  flag is True. Physics is defensible (semi-analytic freeze-out has
  O(15-20%) systematics) but the name + adjacency invites the CLI agent
  (and any consumer) to read "consistent with Planck" as a 25σ agreement.
  The v0.3.18 agent correctly caught the contradiction and warned the
  user — good model behaviour, confusing server semantics. Fix suggestion
  (our repo): rename to `consistent_within_theory_err` or emit both
  `consistent_planck` (Planck-only) and `consistent_theory`. Local issue
  filed: nesar-ai-assistant/inelastic-dm-server#1.
- Physics quality strong: case 05 asked for N_eff = 3.0, but the
  sterile-nu server parameterizes extra radiation as ΔN_eff ≥ 0, so no
  tool call can reach below the SM value 3.044 (fit itself is valid over
  [2.044, 6.044]). The agent disclosed this, then estimated the point
  from fit slopes (dYp/dN_eff = 0.01351, d(D/H×10⁵)/dN_eff = 0.3308) and
  labelled it a linear extrapolation, not a tool evaluation — honest
  method disclosure, no fabrication. Case 10: D/H = 2.443e-5 at
  N_eff = 3.044 (PRyMordial fit) correctly identified as the SM BBN
  prediction, not a sterile-neutrino result — an epistemically careful
  distinction the model got right unprompted.
- Times: all 10 cases 0.2–70s; total ~7 min wall clock.


## 2026-10-23-midday-research — 2 pass / 0 flagged

Clean run — no flags. Topic rotation landed on baryonic-pk (same as 10-17),
so the board now accumulates two research runs (33 findings / 11 directions
total; today's run 261023_110038-4455 added 11 findings across d-07..d-11).
Report PDF + supplement + transcript generated (report-261023_111024); the
known first-pass LaTeX failure auto-recovered again (local #29, third time).
No GH#2 banner noise (0 JSONRPC parse errors — no arxiv_agent sub-agent
calls this run).

- **GH#10 reproduced: 67/60 tool calls (+7)** — worst observed yet (prior
  band +1..+4 single-server). Amplifier: d-08 and d-10 each burned their
  remaining budget on the GH#8 workaround (reading prediction CSVs via
  read_arxiv_chunk char offsets; dead-end x-06 logged). Both directions
  ended "blocked (budget)" but the wave-2 reopen logic worked as designed.
  Comment posted to #10.
- **GH#8 third occurrence** — load_table_data rejects hydroemu CSV header
  row; agent workaround notable. Comment posted to #8.
- **Physics quality: verified independently.** Spot-checked 3 computed
  findings against a direct cosmohydro_emu run in the server venv:
  f-033 (fiducial z=0/z=1: S(1.013)=0.9766/0.9848, S(3.71)=0.8924/0.9458)
  and f-023 (k(1%)=0.59→0.60, k(5%)=2.11→2.13) reproduce to 3-4 decimals.
  This is the first research run where the agent chained Pk-ratio + fGas
  emulator predictions into a physics narrative (weak-AGN boost S>1 peak
  ~1.011 at k~2.4 from cooled baryons in halos; suppression deepens toward
  z=0 consistent with FLAMINGO literature findings f-002/f-019) — the
  emulation + literature bracket reads coherently.
- Agent honestly declared the Omega_b/Omega_m Elbers+2024 comparison
  impossible (emulator has no baryon-fraction parameter) instead of forcing
  it — good epistemic behaviour (f-024).


## 2026-10-23-pm-combo — 3 pass / 0 flagged

Clean run — no flags. Topic (rotation): baryonic suppression of the matter
power spectrum — HACC emulator S(k) predictions vs published feedback
levels (eROSITA+kSZ, HSC-XXL, Grandis), 4 servers (SBBN+IDM+HYD+DOM, 52
tools/5 server-instances incl. arxiv), 2 waves, 3 workers.

Notables:
- **GH#10 (budget overrun) reproduced**: 53 calls vs `--max-tool-calls 50`
  (+3). First combo-profile occurrence (midday research runs showed +7).
  Two wave-2 directions (d-12, d-13) were blocked mid-direction when the
  budget ran out — run stopped cleanly on the 2/2-wave limit regardless.
- **GH#2 (arxiv banner) did NOT reproduce**: 0 JSONRPC parse errors despite
  18 `read_arxiv_chunk` + 7 `download_arxiv_full_text` calls this run
  (Oct 22 combo run had 1,663). No banner text in transcript.
- **#29 (LaTeX first-pass failure) recurred — and the #29 record was wrong**:
  re-grep found the failure also in 10-16/10-17/10-20 midday runs, so it's
  7 of 18 report runs (~39%), not "first seen 10-21". #29 entry corrected
  and **filed upstream as GH#13**. Today: auto-recovered, report 10 pp /
  supplement 59 pp / transcript 39 pp, all valid.
- **4-server orchestration worked well**: 48 model calls total routed
  cleanly across servers — hydro emulator (9× predict_observable for
  Pk-ratio/fGas at fiducial + 5 extreme-corner points, 2× comparison
  plots), SBBN (list_sterile_nu_skills), DOM (get_dispatch, list_datasets,
  list_input_files/agent_files), arxiv survey (10× search, 7× download, 18×
  read chunks). No cross-server confusion; each direction picked the right
  server for its sub-question.
- Report flags contested findings honestly ("the significances quoted are
  contested", wave-2 restatements marked unverified vs wave-1 verbatim
  quotes) — the critic-wave mechanism is doing its job.
- Tokens: 1.5M in (1.1M cached) / 85K out for the research case.



## 2026-10-25-expert-schneider15-cl-bias — expert-physicist session

Deep multi-server chain, not a battery run. See
`research-results/2026-10-25/expert-schneider15-cl-bias/SESSION_REPORT.md`
for full writeup. Headline: chained hydroemu-mcp-server (HACC Pk-ratio
suppression curve) → direct pyccl `BaryonsSchneider15` fit → direct
firecrown/pyccl Python API (bypassing the broken YAML `pk_modifier` path,
#5) → Fisher-bias propagation on a DES-Y1-like shear-only sacc file. Result:
baryon-induced bias on (Omega_c, sigma8) is sub-0.1-sigma at DES-Y1
shear-only statistical power (delta(Omega_c)=-0.0001=-0.01σ,
delta(sigma8)=+0.0005=+0.02σ), with sigma(Omega_c)=0.0134,
sigma(sigma8)=0.0204. Caveat: this run's "fiducial" cosmology
(omega_m=0.143, sigma_8=0.82) is a guess, not the true HACC fiducial — see
#12 below.

**MAG backend note:** `claude-opus-5-5` returned HTTP 403
`amsc_allocation_expired` on 2026-10-25 (allocation
`genesis-mission-october-2026-hackathon`) — fell back to
`gpt-5.6-luna@openai` for this session. Needs a check/renewal before the
next ramp-up cron batteries run, or `scripts/test-env.sh`'s default should
change.

**#12 (new, local)**: `hydroemu-mcp-server::describe_parameters` never
surfaces `cosmohydro_emu.get_parameter_info()["fiducial"]`
(`omega_m=0.14176, sigma_8=0.8102`, documented in the package as
`FIDUCIAL_COSMOLOGY`) even though the package ships it — agents are forced
to guess the fiducial design point from the min/max range, and two sessions
(2026-10-24 and 2026-10-25) guessed two *different* wrong values for the
identical "predict at the fiducial point" request. Filed upstream:
https://github.com/nesar-ai-assistant/hydroemu-mcp-server/issues/1

**#5 status**: still open (confirmed via `gh issue view` before this
session). Added a comment with the validated direct-Python workaround,
numbers, and a methodological warning not to report a bare chi2 delta as a
parameter bias (self-caught mid-session: delta_chi2=9.87 at one point is
97% a cross-term artifact of the synthetic data vector's generation, not the
baryon effect size — the Fisher-bias vector is the correct quantity).
https://github.com/nesar/desc_mcp_server/issues/5#issuecomment-6403684059

## 2026-10-23-eve-desc — 10 pass / 0 flagged

Clean run — no flags. v0.3.18, claude-opus-5-5@MAG, ~11 min wall, 48/54 tools loaded.
Harness now auto-applies a `-1023` chat-name suffix → all 10 conversations fresh
(mitigates #28 without manual rotation); D7→D8 continuation chain intact within
the run (D8 correctly cited D7's "7–9% low clustering/lensing amplitudes").

**Cross-family chains (the point of this profile) all worked with real numbers:**
- **D3**: augur config → synthetic datavector (540 pts, S/N 1574) → sacc_inspect
  (10 tracers, cov 540×540 PD, cond 1e13). Tried `describe_desc_tool_family(ccl)`
  first, hit `No module named 'tools.ccl'` (#24), adapted via augur without
  fabricating — stated plainly the SRD n(z) came from augur files, not CCL.
- **D4**: augur datavector → sacc_attach_gaussian_covariance (300×300 PD,
  cond 8.2e9) → firecrown likelihood → chi². First attempt chi²≈2e6 (augur vs
  firecrown IA-model mismatch, ~74σ pulls); agent diagnosed honestly, then did
  a proper closure test (theory-replaced data) → chi²=0 exactly, with a correct
  explanation of why (t=d ⇒ cov irrelevant) and why chi²≈n_data≈300 is the
  noisy-case expectation.
- **D7→D8**: namaster simulate (nside 64, f_sky 0.2995) → bandpowers (6 bands,
  EE/TE/TT ratios 1.02/0.91/0.93 vs theory) → D8 TJPCov FourierGaussianFsky
  vs Knox (agree ~1%; chi²=27.7/18, TJPCov, PD) with correct cross-turn continuity.
- **D10**: 3-step chain — step 1 (CCL halofit Pk) blocked by #24; step 2 skill
  plan (pk-ccl-vs-emulators) loaded and reasoned; step 3 firecrown DES Y1
  3x2pt loglike −275.785 (chi²/n 1.207, matches tool docs).

**#24 recurrence (expected, Nesar's server, not the app)**: tools.ccl absent in
D1/D2/D3/D9/D10, same as 10-22. NEW detail: `list_desc_packages` advertises ccl
as "active" (full description: background, P(k), C_ell, xi, halo model, SRD n(z))
even though the family is not importable — package-registry metadata should
mark it unavailable. Noted under #24; candidate for nesar/desc_mcp_server#4
follow-up (creating tools/ccl remains the real fix).

**Honesty checks passed**: D2 refused to fabricate CCL values, gave a labeled
hand-check (chi(z=1)≈3450 Mpc for h=0.67, noting the user's ~3300 expectation
fits h≈0.70) and suggested checking the reference value. No truncation markers
(see #11) observed; token-units quirk #15 still present (e.g. "116K in (56K
cached)"). D6 pipeline validated but not runnable (missing TXPipe input files +
DESC_TXPIPE_ENV unset — environmental, expected on this host).

