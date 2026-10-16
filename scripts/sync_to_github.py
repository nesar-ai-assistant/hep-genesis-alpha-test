#!/usr/bin/env python3
"""Sync the HEP-Genesis testing tree to the private GitHub repo.

Pushes: docs, ISSUES.md, SCOPE.md, research-results, run summaries +
per-case transcripts (small text), and small project metadata (boards,
findings, tex sources). Excludes: binary PDFs of arXiv papers, venvs,
downloads, any .env / key material.

Run from anywhere:  python3 scripts/sync_to_github.py [--dry]
"""
import subprocess
import sys
from pathlib import Path

BASE = Path.home() / "hep-genesis-testing"
REPO_URL = "git@github.com:nesar-ai-assistant/hep-genesis-alpha-test.git"
REPO_NAME = "hep-genesis-alpha-test"

DRY = "--dry" in sys.argv


def sh(cmd, cwd=None, capture=True, check=True):
    print(f"  $ {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    r = subprocess.run(cmd, cwd=cwd, text=True, capture_output=capture, shell=isinstance(cmd, str))
    if check and r.returncode != 0:
        print(r.stdout or "")
        print(r.stderr or "", file=sys.stderr)
        raise SystemExit(f"command failed: {cmd}")
    return r


def main():
    if not (BASE / ".git").exists():
        print("[sync] initializing repo")
        sh(["git", "init"])
        sh(["git", "remote", "add", "origin", REPO_URL])
        sh(["git", "branch", "-M", "main"])
    # ensure remote exists & is ours
    r = sh(["git", "remote", "get-url", "origin"], capture=True)
    if REPO_URL not in r.stdout:
        raise SystemExit("origin remote is not the expected repo — aborting")

    # stage everything per .gitignore, letting git apply the rules
    print("[sync] staging (git add -A)")
    sh(["git", "add", "-A"])
    staged = sh(["git", "diff", "--cached", "--name-only"], capture=True).stdout.strip().splitlines()
    if not staged:
        print("[sync] nothing to sync")
        return
    print(f"[sync] {len(staged)} files staged")
    # safety: refuse to commit any file that looks like a secret
    bad = [f for f in staged if f.endswith((".env", ".env.")) or "secret" in f.lower() or "token" in f.lower()]
    if bad:
        raise SystemExit(f"REFUSING: suspicious files staged: {bad}")
    sizes = []
    for f in staged:
        try:
            if (BASE / f).stat().st_size > 3_000_000:
                sizes.append(f)
        except OSError:
            pass
    if sizes:
        print("[sync] large files (>3MB) staged:", sizes)
    if DRY:
        print("[sync] dry run — stopping before commit")
        return
    msg = f"testing update {__import__('datetime').date.today().isoformat()}"
    sh(["git", "commit", "-m", msg, "--quiet"])
    sh(["git", "push", "-u", "origin", "main"])
    print(f"[sync] pushed {len(staged)} files -> {REPO_URL}")


if __name__ == "__main__":
    main()
