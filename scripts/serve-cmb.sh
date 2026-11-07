#!/bin/bash
# Wrapper: launch cmb-data-mcp-server (cosmo-mcp family) with its own venv, correct cwd
cd "/Users/nramachandra/github-integration/cmb-data-mcp-server" || exit 1
export MPLBACKEND=Agg
exec .venv/bin/python -m mcp_server "$@"
