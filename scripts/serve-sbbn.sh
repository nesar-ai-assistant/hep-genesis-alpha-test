#!/bin/bash
# Wrapper: launch sterile-nu-bbn MCP server with its own venv, correct cwd
cd "/Users/nramachandra/github-integration/sterile-nu-bbn-server" || exit 1
exec .venv/bin/python -m mcp_server "$@"
