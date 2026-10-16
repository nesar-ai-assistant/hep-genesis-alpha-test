# HEP-Genesis-Agent test session — 2026-10-15-r1-features

- Version under test: v0.3.16 (published 2026-10-15T03:57:35Z)
- Profile: features
- Backend: https://mag.genesis.americansciencecloud.org/v1 / claude-opus-5-5
- Cases: 9 total, 8 pass, 1 flagged
- Storage: test tree 0.03 GB (free 123.2 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | F1-list-chats | cli | ✅ PASS | 0.2s | exit 0, output present |
| 2 | F2-board | cli | ✅ PASS | 1.5s | exit 0, output present |
| 3 | F3-list-runs | cli | 🚩 FLAG | 1.2s | rc=0, output=0 chars |
| 4 | F4-temperature | quick | ✅ PASS | 23.5s | exit 0 with substantive output |
| 5 | F5-table | quick | ✅ PASS | 17.9s | exit 0 with substantive output |
| 6 | F6-quick-report | quick | ✅ PASS | 90.2s | exit 0 with substantive output |
| 7 | F7-memory | quick | ✅ PASS | 9.6s | exit 0 with substantive output |
| 8 | F8-skill | quick | ✅ PASS | 14.4s | exit 0 with substantive output |
| 9 | F9-research-noservers | research | ✅ PASS | 322.6s | exit 0 with substantive output |

## Flagged issues

### F3-list-runs — List research runs
- rc=0, duration=1.2s
- note: rc=0, output=0 chars
- transcript: cases/F3-list-runs.out
