#!/usr/bin/env python3
"""Storage watchdog for the HEP-Genesis ramp-up week.

Prints a compact alert ONLY when action is needed; stays silent otherwise
(silent = nothing sent to Nesar). Checks:
- hep-genesis-testing tree size > 15 GB (soft limit)
- disk free < 20 GB
- any single run dir > 2 GB (likely runaway downloads)
Exit 1 on alert so delivery is guaranteed even if stdout plumbing changes.
"""
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path.home() / "hep-genesis-testing"
TREE_LIMIT_GB = 15.0
DISK_FREE_LIMIT_GB = 20.0
RUN_DIR_LIMIT_GB = 2.0


def du_gb(path: Path) -> float:
    try:
        out = subprocess.run(["du", "-sk", str(path)], capture_output=True,
                             text=True, timeout=120)
        return int(out.stdout.split()[0]) / 1_048_576
    except Exception:
        return 0.0


def main() -> int:
    alerts = []
    tree = du_gb(BASE)
    free = shutil.disk_usage(BASE).free / 1e9
    if tree > TREE_LIMIT_GB:
        alerts.append(f"test tree {tree:.1f} GB > {TREE_LIMIT_GB} GB soft limit")
    if free < DISK_FREE_LIMIT_GB:
        alerts.append(f"disk free {free:.1f} GB < {DISK_FREE_LIMIT_GB} GB")
    # biggest run dirs
    big = []
    for d in (BASE / "runs").iterdir():
        if d.is_dir():
            sz = du_gb(d)
            if sz > RUN_DIR_LIMIT_GB:
                big.append((sz, d))
    for sz, d in sorted(big, reverse=True)[:3]:
        alerts.append(f"run dir {d.name} is {sz:.1f} GB (possible runaway downloads)")
    if alerts:
        print("⚠️ HEP-Genesis storage alert:")
        for a in alerts:
            print(f"  - {a}")
        print(f"  test tree: {tree:.1f} GB, disk free: {free:.1f} GB")
        print("  Suggested: prune ~/hep-genesis-testing/projects/*/runs/* arxiv PDFs/TXTs,")
        print("  or old runs/ dirs after archiving findings to research-results/.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
