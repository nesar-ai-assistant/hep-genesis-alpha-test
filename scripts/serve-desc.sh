#!/bin/bash
# Serve the desc_mcp_server for hep-genesis-agent CLI testing.
# Uses the osx-64 env built from a platform-correct conda-lock solve
# (repo lock ships linux-64 + osx-arm64 only; this host is osx-64).
# Reference clones live in ~/github-integration (augur, external-Smokescreen).
set -euo pipefail
DIR="$HOME/github-integration/desc_mcp_server"
export DESC_AUGUR_DIR="$HOME/github-integration/augur"
export DESC_EXTERNAL_DIR="$HOME/github-integration/external-Smokescreen"
exec "$DIR/.mcp-env/bin/python" -m mcp_server
