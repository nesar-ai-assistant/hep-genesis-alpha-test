#!/bin/bash
# Wrapper: launch inelastic-dm MCP server with its own venv, correct cwd
cd "/Users/nramachandra/github-integration/inelastic-dm-server" || exit 1
exec .venv/bin/python -m mcp_server "$@"
