# HEP-Genesis-Agent test session — 2026-11-02-spark-deep-1030-research

- Version under test: v0.4.4 (published 2026-10-30T22:32:35Z)
- Profile: research
- Backend: https://inference-api.alcf.anl.gov/resource_server/minerva/api/v1 / muse-spark-bf16
- Cases: 3 total, 2 pass, 1 flagged
- Storage: test tree 0.54 GB (free 106.0 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | R1-sterile-bbn-xray | research | ✅ PASS | 815.2s | exit 0 with substantive output |
| 2 | R2-sterile-bbn-xray-followup | research | ✅ PASS | 717.1s | exit 0 with substantive output |
| 3 | R3-report | cli | 🚩 FLAG | 14.7s | rc=1, output=12263 chars |

## Flagged issues

### R3-report — Generate PDF report for the research run
- rc=1, duration=14.7s
- note: rc=1, output=12263 chars
- transcript: cases/R3-report.out
