#!/usr/bin/env python3
"""Build augur + smokescreen into .mcp-env from the reference clones.

Per ENVIRONMENT.md: pip-installing from the clone would write egg-info into
the read-only reference, so build from a temporary copy.
"""
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO = Path.home() / "github-integration/desc_mcp_server"
PIP = REPO / ".mcp-env/bin/python"

for src, pkg in [(Path.home() / "github-integration/augur", "augur"),
                 (Path.home() / "github-integration/external-Smokescreen", "smokescreen")]:
    tmp = Path(tempfile.mkdtemp()) / pkg
    shutil.copytree(src, tmp)
    r = subprocess.run([str(PIP), "-m", "pip", "install", "--quiet", "--no-deps", str(tmp)],
                       cwd=REPO)
    print(pkg, "install rc =", r.returncode)
