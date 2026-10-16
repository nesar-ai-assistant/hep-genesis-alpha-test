# Research Results Archive

Autonomous research runs executed by the HEP-Genesis-Agent CLI during alpha
testing, archived by the test harness.

Layout: `YYYY-MM-DD/<project>/` containing:
- `board-*.json` — machine-readable findings (claims + evidence + critiques)
- `findings.json` — digest of all findings
- `report/` — latest generated PDF report (+ supplement, transcript, .tex)
- `manifest.json` — provenance (which harness run archived this)

The archive is append-only; nothing is deleted. Kept for later inspection —
not surfaced to Nesar unless requested.
