# HEP-Genesis-Agent — Scope Document (Long-Horizon)

Living document: features the system could grow into, gathered from alpha
testing + reading the v0.3.16 codebase. Not a roadmap commitment — a menu of
directions with rationale. Updated as testing continues.

Last updated: 2026-10-15 (after first full battery, v0.3.16)

---

## A. Ecosystem & extensibility

### A1. Plugin system
Today the CLI hardcodes its bundled servers and tool taxonomy. A plugin
architecture (discoverable entry points, e.g. `[project.entry-points."hep_genesis.plugins"]`)
would let third parties ship:
- new MCP server bundles with one-command registration (`hep-genesis-agent plugin add X`);
- tool post-processors (e.g. auto-plotting for any tabular tool result);
- report templates (journal styles, conference proceedings).
*Why it matters:* the HEP-KE org already has 6+ MCP servers; friction to wire
them in is the single biggest adoption cost we observed (see ISSUES.md #1, #6).

### A2. Server registry / manifest
A shared TOML/JSON manifest (org-hosted) listing available MCP servers, their
tool summaries, and launch specs. `--servers @registry:sbbn` resolves without
local paths. Enables teams to share server configs without git clones.

### A3. Skills marketplace semantics
`--list-skills` + `load_skill` exist. Natural extension: skills versioned and
shareable across projects and users (workspace git remote), with the agent
suggesting relevant skills based on query content.

## B. Research engine

### B1. Hierarchical research (research-on-research)
The board (findings + critiques) is already structured. Let a follow-up run
consume a previous board: "continue from board X, resolve the open directions"
is partially there (`--continue d-04`); full board-level resumption with
inheritance of findings would enable week-long campaigns.

### B2. Uncertainty & provenance ledger
Findings carry claims; adding per-claim confidence, source (which tool call /
paper / parameter), and a machine-readable evidence chain would let reports
print an uncertainty table and let downstream agents cite precisely.

### B3. Steering UX
`--steer` exists but requires watching events.jsonl. A `--follow RUN_ID` mode
printing a live digest (phase, tokens, findings so far) would make supervision
practical. Optionally a `--watch-board` that pretty-prints new findings as
they post.

### B4. Budget semantics
Waves/tool-calls/wall-clock exist; a **token budget** (--max-tokens) with
per-stage attribution (usage lines already exist) would help on metered
gateways like MAG.

## C. Tools & science capabilities

### C1. Plotting as a first-class tool
The hydroemu server ships predict+plot heads; the bundled server lacks a
generic plotting tool (histogram outputs exist but no figure export). A
`plot_dataset` tool (matplotlib via the deployment head) with caption support
would make quick-mode answers publication-adjacent.

### C2. Table interop
`load_table_data` handles CSV/text. Parquet/FITS/HDF5 inputs and a
`save_table` output would close the loop with HACC/DESC data formats.

### C3. HPC dispatch guardrails
`set_dispatch polaris/perlmutter` exists. Pre-flight validation (queue depth,
allocation status, projected cost) surfaced to the agent would prevent wasted
submissions. Also `--allow-hpc` gating is global; per-tool dispatch policy
would be safer.

### C4. Coding mode parity
`--coding` shells to the pi harness. Bundling a minimal default harness (or
auto-detecting uv/venv) would make the flag usable out of the box — on this
machine `pi` is absent, so the flag is dead weight unless installed.

## D. CLI & UX

### D1. `--version` flag
Missing! `hep-genesis-agent --version` errors; version only via pip. Trivial
fix, high value for scripting and test automation.

### D2. Machine-readable output
`--events jsonl` exists for research runs. A global `--json` wrapper (results,
usage, errors as one JSON object per line) would make the CLI automatable from
other agents — this is exactly how our test harness would prefer to consume it.

### D3. Config file
Env vars are fine for one endpoint; a `~/.hep-genesis/config.toml` with
profiles (endpoints, models per stage, default servers, projects dir) would
reduce boilerplate. CLI flags > env > config precedence.

### D4. Chat management
`--list-chats` exists; `--delete-chat`, `--export-chat` (markdown/JSON) would
round it out.

## E. Reliability (from observed bugs)

### E1. MCP stdio hygiene
Bundled tools must never print to stdout (GH#2). A server-side wrapper that
redirects any stray stdout of tool subprocesses to stderr would make the whole
class of bugs impossible. Also consider validating JSON-RPC framing in CI with
a strict client.

### E2. arxiv tool regression tests
GH#3 shows sub-agent code paths rotting while direct tools work. One
end-to-end test per bundled tool (search → download → extract) in the release
pipeline would catch this before shipping.

### E3. Path/git server spec contract
GH#1: define + test the contract (entry point discovery, fallback to
`python -m mcp_server`, clear error message when neither exists).

---

## Priorities if we were advising the team (Oct 2026)

1. **D1 `--version`** — trivial, unblocks automation.
2. **E1 stdio hygiene + E2 tool regression tests** — trust in every research run.
3. **A1/A2 plugin & registry story** — the org's server fleet is the moat; wiring friction is the bottleneck.
4. **C1 plotting tool** — biggest perceived-capability jump per effort.
5. **D2 `--json` output** — makes the CLI a building block for agent-to-agent workflows.
