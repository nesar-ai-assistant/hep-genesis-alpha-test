#!/bin/bash
# Wrapper: launch hydroemu MCP server with its own venv (py3.11, scipy<1.11), correct cwd
cd "/Users/nramachandra/github-integration/hydroemu-mcp-server" || exit 1
exec .venv/bin/python -m mcp_server "$@"
