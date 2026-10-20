# HEP-Genesis-Agent test session — 2026-10-20-am-core

- Version under test: v0.3.18 (published 2026-10-19T19:33:25Z)
- Profile: core
- Backend: https://mag.genesis.americansciencecloud.org/v1 / claude-opus-5-5
- Cases: 10 total, 10 pass, 0 flagged
- Storage: test tree 0.27 GB (free 108.5 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | 01-help-version | cli | ✅ PASS | 0.3s | exit 0, output present |
| 2 | 02-list-projects | cli | ✅ PASS | 0.2s | exit 0, output present |
| 3 | 03-quick-reasoning | quick | ✅ PASS | 16.2s | exit 0 with substantive output |
| 4 | 04-sbbn-dw-scan | quick | ✅ PASS | 38.2s | exit 0 with substantive output |
| 5 | 05-sbbn-bbn-scan | quick | ✅ PASS | 23.7s | exit 0 with substantive output |
| 6 | 06-idm-freezeout | quick | ✅ PASS | 23.7s | exit 0 with substantive output |
| 7 | 07-hydro-gsmf | quick | ✅ PASS | 40.7s | exit 0 with substantive output |
| 8 | 08-hydro-cross | quick | ✅ PASS | 34.9s | exit 0 with substantive output |
| 9 | 09-dom-data | quick | ✅ PASS | 16.7s | exit 0 with substantive output |
| 10 | 10-multi-server | quick | ✅ PASS | 18.7s | exit 0 with substantive output |