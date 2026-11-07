#!/bin/bash
# Wrapper: launch sn-mcp-server (cosmo-mcp family) with its own venv, correct cwd
cd "/Users/nramachandra/github-integration/sn-mcp-server" || exit 1
export MPLBACKEND=Agg
exec .venv/bin/python -m mcp_server "$@"
