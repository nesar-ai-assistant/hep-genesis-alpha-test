#!/usr/bin/env python3
"""Rebuild papers/ — one flat folder of all reports with supplementary/ subdirs.

Usage:
  python3 scripts/build_papers.py

Source of truth: git-tracked projects/*/reports/*/bundle.json (i.e. what is
already on GitHub). Each report becomes:

  papers/YYYY-MM-DD__project__timestamp__short-title.pdf
  papers/supplementary/<same-stem>/  (supplement.pdf, transcript.pdf, .tex, bundle.json, figures/)

A README.md with a sortable table + MANIFEST.json are also written.

Safe to re-run: truncates stale papers entries, copies everything fresh.
"""
import json, re, shutil, subprocess
from pathlib import Path

BASE = Path.home() / "hep-genesis-testing"
PAPERS = BASE / "papers"

def slugify(s, maxlen=60):
    return re.sub(r"[^a-zA-Z0-9]+", "-", s.strip().lower()).strip("-")[:maxlen].rstrip("-") or "untitled"

def main():
    DEDUP_MODE = (BASE / "papers/.dedup_per_project").exists()
    if DEDUP_MODE:
        print("[papers] dedup mode: keeping only latest report per experiment (project)")

    tracked = subprocess.run(
        ["git", "-C", str(BASE), "ls-files", "projects/*/reports/*/bundle.json"],
        capture_output=True, text=True
    ).stdout.splitlines()

    # Prefer timestamped reports over the CLI's reports/latest rolling alias —
    # exclude `latest` from the papers/ view so timestamped history stays addressable,
    # and deduplicate to newest timestamp per project upstream.
    tracked = [t for t in tracked if not t.endswith("/latest/bundle.json")]
    if not tracked:
        print("[papers] no tracked reports found — nothing to do")
        return

    # Clean stale outputs (keep README/MANIFEST generation fresh; don't delete git-untracked extras blindly)
    # Instead, just overwrite what we produce and prune removed reports at the end.
    produced_pdfs = set()
    produced_supp_dirs = set()
    manifest = []

    for bundle_rel in tracked:
        bundle_path = BASE / bundle_rel
        report_dir = bundle_path.parent
        project = report_dir.parent.parent.name
        ts = report_dir.name
        m = re.match(r"(\d{2})(\d{2})(\d{2})_", ts)
        if m:
            date = f"20{m.group(1)}-{m.group(2)}-{m.group(3)}"
        elif ts == "latest":
            # CLI v0.4.6 writes reports/latest as a rolling symlink — infer date from bundle or mtime
            try:
                ca = (json.loads((report_dir / "bundle.json").read_text()).get("created_at") or "")[:10]
                date = ca if re.match(r"20\d{2}-\d{2}-\d{2}", ca) else __import__("datetime").datetime.fromtimestamp(report_dir.stat().st_mtime).strftime("%Y-%m-%d")
            except Exception:
                date = __import__("datetime").datetime.fromtimestamp(report_dir.stat().st_mtime).strftime("%Y-%m-%d")
        else:
            date = "unknown-date"

        try:
            bundle = json.loads(bundle_path.read_text())
        except Exception as e:
            print(f"[papers] SKIP {bundle_rel}: {e}")
            continue

        title = (bundle.get("title") or "").strip()
        if not title or title.endswith("\u2026"):
            tex = report_dir / "report.tex"
            if tex.exists():
                mt = re.search(r"\\title\{([^}]+)\}", tex.read_text())
                if mt:
                    title = mt.group(1).strip()
        short = slugify(title) if title else slugify(project)
        stem = f"{date}__{project}__{ts}__{short}"
        if len(stem) > 180:
            stem = stem[:180].rstrip("-")

            # Defer dedup until after manifest is built — mark but still collect        produced_pdfs.add(f"{stem}.pdf")
        produced_supp_dirs.add(stem)

        # Copy main report (force overwrite so re-reports update)
        src_report = report_dir / "report.pdf"
        if src_report.exists():
            dst = PAPERS / f"{stem}.pdf"
            PAPERS.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_report, dst)

        # Auxiliary bundle
        aux_dir = PAPERS / "supplementary" / stem
        aux_dir.mkdir(parents=True, exist_ok=True)
        for aux in ["supplement.pdf", "transcript.pdf", "supplement.tex", "transcript.tex", "report.tex", "bundle.json"]:
            s = report_dir / aux
            if s.exists():
                shutil.copy2(s, aux_dir / aux)
        fig_src = report_dir / "figures"
        if fig_src.exists():
            fig_dst = aux_dir / "figures"
            if fig_dst.exists():
                shutil.rmtree(fig_dst)
            shutil.copytree(fig_src, fig_dst)

        manifest.append({
            "filename": f"{stem}.pdf",
            "date": date,
            "timestamp": ts,
            "project": project,
            "title": title[:300],
            "figs": len(bundle.get("figures", [])),
            "model": bundle.get("models", {}).get("quick", {}).get("model", ""),
            "source": str(report_dir.relative_to(BASE)),
            "supplementary": f"supplementary/{stem}/",
        })

    # Deduplicate: keep only latest timestamp per project (experiment)
    if DEDUP_MODE:
        from collections import defaultdict
        by_proj = defaultdict(list)
        for m in manifest:
            by_proj[m["project"]].append(m)
        deduped = []
        dropped_stems = set()
        for proj, lst in by_proj.items():
            latest = max(lst, key=lambda x: x["timestamp"])
            deduped.append(latest)
            for m in lst:
                if m is not latest:
                    dropped_stems.add(m["filename"][:-4])
                    print(f"[papers] dedup drop {m['project']}/{m['timestamp']} -> {m['filename']}")
        manifest = deduped
        produced_pdfs = {m["filename"] for m in manifest}
        produced_supp_dirs = {m["filename"][:-4] for m in manifest}

    # Prune stale PDFs/supplementary dirs no longer in manifest
    for existing in PAPERS.glob("*.pdf"):
        if existing.name not in produced_pdfs:
            print(f"[papers] pruning stale {existing.name}")
            existing.unlink()
    supp_root = PAPERS / "supplementary"
    if supp_root.exists():
        for existing in supp_root.iterdir():
            if existing.name not in produced_supp_dirs:
                print(f"[papers] pruning stale {existing}")
                shutil.rmtree(existing) if existing.is_dir() else existing.unlink()

    # Manifest
    (PAPERS / "MANIFEST.json").write_text(json.dumps(sorted(manifest, key=lambda x: x["date"]+x["timestamp"], reverse=True), indent=2))

    # README table
    lines = [
        "# Reports",
        "",
        "Single browsable folder — every report as one PDF. Filenames are",
        "`YYYY-MM-DD__project__timestamp__short-title.pdf`. The matching",
        "`supplementary/<same-stem>/` holds `supplement.pdf`, `transcript.pdf`,",
        "`.tex` sources, `bundle.json`, and `figures/`. `source` below is the",
        "full experiment dir (rerun / board / provenance live there).",
        "",
        "AI-generated session summaries — verify before external use (see each",
        "report's disclaimer + its `supplement.pdf`).",
        "",
        "| Date | Experiment | Title | Figs | Model | Supplementary | Source |",
        "|------|------------|-------|------|-------|----------------|--------|",
    ]
    for m in sorted(manifest, key=lambda x: x["date"] + x["timestamp"], reverse=True):
        pdf = m["filename"]
        supp = m["supplementary"]
        src = m["source"]
        t = (m["title"][:70] + "…") if len(m["title"]) > 70 else m["title"]
        t = t.replace("|", "\\|")
        model_short = m["model"].split("@")[0] if m["model"] else "?"
        lines.append(f"| {m['date']} | `{m['project']}` | [{t}]({pdf}) | {m['figs']} | {model_short} | [supplementary/{pdf[:-4]}]({supp}) | `{src}` |")
    lines += ["", f"_{len(manifest)} reports. Regenerated by `scripts/build_papers.py`._", ""]
    (PAPERS / "README.md").write_text("\n".join(lines))

    total_mb = sum((PAPERS / m["filename"]).stat().st_size for m in manifest if (PAPERS / m["filename"]).exists()) / 1e6
    print(f"[papers] {len(manifest)} reports, {total_mb:.1f} MB of PDFs -> papers/ + papers/supplementary/")

if __name__ == "__main__":
    main()
