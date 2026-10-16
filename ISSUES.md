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
- v0.3.16. All sub-agent PDF/TXT downloads fail:
  `RuntimeError: 'Search' object has no attribute 'results'` (python-arxiv API
  misuse). Degrades to abstract-level synthesis (honestly, to its credit).
  Direct `download_arxiv_paper` / `download_full_arxiv_paper` work fine.
- Evidence: tool-call tc-261015_2-w1-d-01-18; report Methods section.

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
- In runs 261016_083303 and 261015_223937, predict_observable writes the CSV
  and PNG but the tool response carries only file paths + a one-line message,
  so the CLI agent cannot quote amplitudes/ratios and falls back to
  qualitative interpretation ("check them against Figure 10"). Consider
  embedding a compact summary (bin centers/values or knee/endpoint stats) in
  the tool payload. (Nesar's server, not the app.)

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

