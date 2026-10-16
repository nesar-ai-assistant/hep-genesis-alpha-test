# HEP-Genesis-Agent test session — 2026-10-15

- Version under test: v0.3.16 (published 2026-10-15T03:57:35Z)
- Cases: 10 total, 9 pass, 1 flagged
- Endpoint: https://mag.genesis.americansciencecloud.org/v1 / gpt-5.6-luna@openai

## Results

| # | Case | Mode | Status | Time | Note |
|---|------|------|--------|------|------|
| 1 | 01-help-version | cli | ✅ PASS | 0.2s | exit 0, output present |
| 2 | 02-list-projects | cli | ✅ PASS | 0.2s | exit 0, output present |
| 3 | 03-quick-no-servers | quick | ✅ PASS | 6.8s | exit 0 with substantive output |
| 4 | 04-quick-domain-list | quick | ✅ PASS | 11.1s | exit 0 with substantive output |
| 5 | 05-quick-sbbn-physics | quick | ✅ PASS | 13.0s | exit 0 with substantive output |
| 6 | 06-quick-sbbn-bbn | quick | ✅ PASS | 56.3s | exit 0 with substantive output |
| 7 | 07-quick-idm-relic | quick | ✅ PASS | 12.5s | exit 0 with substantive output |
| 8 | 08-quick-hydro-list | quick | ✅ PASS | 107.9s | exit 0 with substantive output |
| 9 | 09-research-arxiv | research | 🚩 FLAG | 300.6s | traceback present (but run may have continued) |
| 10 | 10-report | cli | ✅ PASS | 53.0s | exit 0, output present |

## Flagged issues

### 09-research-arxiv — Research mode: arXiv survey on sterile neutrino DM (bounded)
- rc=0, duration=300.6s
- note: traceback present (but run may have continued)
