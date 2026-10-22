# HEP-Genesis-Agent test session — 2026-10-22-pm-combo

- Version under test: v0.3.18 (published 2026-10-19T19:33:25Z)
- Profile: combo
- Backend: https://mag.genesis.americansciencecloud.org/v1 / claude-opus-5-5
- Cases: 3 total, 2 pass, 1 flagged
- Storage: test tree 0.4 GB (free 108.4 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | C1-multi-server-research | research | 🚩 FLAG | 1393.6s | traceback present (run may have continued) |
| 2 | C2-report | cli | ✅ PASS | 225.0s | exit 0, output present |
| 3 | C3-skills | cli | ✅ PASS | 0.2s | exit 0, output present |

## Flagged issues

### C1-multi-server-research — Research with 4 servers: Higgsino thermal target vs direct detection
- rc=0, duration=1393.6s
- note: traceback present (run may have continued)
- transcript: cases/C1-multi-server-research.out
