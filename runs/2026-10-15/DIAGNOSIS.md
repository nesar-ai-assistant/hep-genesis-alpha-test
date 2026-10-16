# Session 2026-10-15 — Diagnosis & Feedback

Version: v0.3.16 (published 2026-10-15T03:57:35Z) — first test session.
Endpoint: mag.genesis gateway, gpt-5.6-luna@openai.
Result: 9 PASS / 1 FLAG (flag = bundled-server bugs, run itself completed).

## Case 09 FLAG diagnosis — two real bugs in bundled `hep-research-aid`

The research run itself COMPLETED (survey → plan → critic → wave 1 (2 workers)
→ critic → report; 7 directions, 10 findings, report + supplement + transcript
PDFs generated). The flag is for protocol noise + a broken sub-tool, both in
the bundled hep-research-aid server (hep_genesis.domain.mcp_server):

### BUG 1 — Rich banner pollutes the MCP stdio channel (HIGH)
The `arxiv_agent` tool (smolagents-based sub-agent) prints Rich panels
(`╭───...───╮`, the "You're a helpful agent named 'arxiv_agent'" banner) to
STDOUT of the stdio MCP server. Stdout must carry only JSON-RPC; every banner
line produces:
  Failed to parse JSONRPC message from server
  pydantic ValidationError: Invalid JSON ... input_value='╭───────...──────╮'
Count in this run: 1663 occurrences. The client survives (logs and continues),
but this is protocol pollution and risks desync/confusion in stricter clients.
Fix: smolagents Console output must go to stderr (or be disabled) when running
under the MCP stdio server.

Evidence: runs/2026-10-15/cases/09-research-arxiv.out lines 287–330.

### BUG 2 — arxiv_agent full-text extraction broken (MEDIUM)
Inside the autonomous arxiv_agent, every full-text download failed with:
  RuntimeError: 'Search' object has no attribute 'results'
(python 'arxiv' package API mismatch — the Search object is passed where
results are expected, or an outdated call pattern). The agent degraded
gracefully to abstract-level synthesis and SAID SO honestly (good!), but its
PDF/TXT extraction produced zero files. Direct `download_arxiv_paper` /
`download_full_arxiv_paper` tool calls (non-autonomous path) worked fine —
8 papers downloaded and text-extracted.

Evidence: projects/hep-testing-research/research/default/tool-calls.jsonl
(tc-261015_2-w1-d-01-18), and the run report itself documents it.

### Pre-existing known bug (from setup, not this run) — CLI --servers path/git spec
`--servers <path-or-git-url>` pip-installs the repo then execs a console
script named after the package dir (`sterile_nu_bbn_server`). Repos that use
`python -m mcp_server` with no [project.scripts] crash with FileNotFoundError.
Workaround used: command: specs → scripts/serve-*.sh wrappers (per-server venv).

## Quality spot-checks (physics correctness)

- 05 sbbn: τ_γ(1 keV, sin²2θ=1e-8) = 7.35e29 s — matches tool value at 1 eV
  (7.35e44 s) with the correct m⁻⁵ scaling. ✓
- 06 sbbn BBN: Yp(3.044)=0.2468, D/H=2.443e-5; both increase with Neff. ✓
  (PRyMordial-consistent).
- 07 idm: Ωh²(1.1 TeV higgsino)=0.108 vs Planck 0.120 — agent correctly called
  it "below" and even flagged that the server's own "consistent" label is
  internally inconsistent (9.8σ). Agent critical-thinking: ✓ (also a note for
  the inelastic-dm-server repo itself).
- 08 hydro: all 14 observables + Pk_GO enumerated correctly. ✓
- 09 report: honest about failed extraction, no fabricated contours. ✓

## Artifacts

- Full PDF report: reports/2026-10-15/261015_205632/report.pdf (+ supplement,
  transcript)
- Research board: projects/hep-testing-research/research/default/board.json
- All case transcripts: runs/2026-10-15/cases/*.out
