# HEP-Genesis-Agent test session — 2026-10-17-eve-features

- Version under test: v0.3.16 (published 2026-10-15T03:57:35Z)
- Profile: features
- Backend: https://mag.genesis.americansciencecloud.org/v1 / claude-opus-5-5
- Cases: 9 total, 9 pass, 0 flagged
- Storage: test tree 0.18 GB (free 123.1 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | F1-list-chats | cli | ✅ PASS | 0.2s | exit 0, output present |
| 2 | F2-board | cli | ✅ PASS | 1.4s | exit 0, output present |
| 3 | F3-list-runs | cli | ✅ PASS | 1.2s | exit 0, output present |
| 4 | F4-temperature | quick | ✅ PASS | 22.2s | exit 0 with substantive output |
| 5 | F5-table | quick | ✅ PASS | 19.1s | exit 0 with substantive output |
| 6 | F6-quick-report | quick | ✅ PASS | 90.0s | exit 0 with substantive output |
| 7 | F7-memory | quick | ✅ PASS | 13.0s | exit 0 with substantive output |
| 8 | F8-skill | quick | ✅ PASS | 14.3s | exit 0 with substantive output |
| 9 | F9-research-noservers | research | ✅ PASS | 370.4s | exit 0 with substantive output |