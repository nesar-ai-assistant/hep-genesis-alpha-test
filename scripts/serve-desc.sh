#!/bin/bash
# Serve the desc_mcp_server for hep-genesis-agent CLI testing.
# Env built via micromamba from tools/env/environment.yml (repo conda-lock
# ships linux-64 + osx-arm64 only; this host is osx-64).
# Reference clones live in ~/github-integration (not as repo siblings).
set -euo pipefail
DIR="$HOME/github-integration/desc_mcp_server"
export DESC_AUGUR_DIR="$HOME/github-integration/augur"
export DESC_EXTERNAL_DIR="$HOME/github-integration/external-Smokescreen"
export DESC_TXPIPE_DIR="$HOME/github-integration/TXPipe"
export DESC_CCL_DIR="$HOME/github-integration/CCL"
export DESC_CCLX_DIR="$HOME/github-integration/CCLX"
export DESC_FIRECROWN_DIR="$HOME/github-integration/firecrown"
exec "$DIR/.mcp-env/bin/python" -m mcp_server
