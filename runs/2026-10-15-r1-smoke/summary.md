# HEP-Genesis-Agent test session — 2026-10-15-r1-smoke

- Version under test: v0.3.16 (published 2026-10-15T03:57:35Z)
- Profile: smoke
- Backend: https://mag.genesis.americansciencecloud.org/v1 / claude-opus-5-5
- Cases: 4 total, 4 pass, 0 flagged
- Storage: test tree 0.03 GB (free 123.3 GB)

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | 01-help | cli | ✅ PASS | 0.2s | exit 0, output present |
| 2 | 02-quick-chat | quick | ✅ PASS | 7.0s | exit 0 with substantive output |
| 3 | 03-tool-discovery | quick | ✅ PASS | 10.9s | exit 0 with substantive output |
| 4 | 04-sbbn-ping | quick | ✅ PASS | 18.8s | exit 0 with substantive output |