# HEP-Genesis-Agent — Issues Log

All problems encountered during alpha testing, filed on GitHub or not.
Updated automatically by the test harness (flags appended per run) and
manually by the testing agent for broader observations.

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

