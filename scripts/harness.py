#!/usr/bin/env python3
"""
HEP-Genesis-Agent CLI test harness v2 (ramp-up week edition).

Changes vs v1:
- Battery profiles: --profile smoke|core|research|combo|features so the
  ramp-up cron can run different batteries at different times of day.
- Harder, multi-step physics questions; multi-server combinations.
- Storage monitor: records du of test tree into runs/<run-id>/storage.json;
  warns if growth since last run > 3 GB or total > 15 GB.
- Research-results archival: after research/combo profiles, copies boards,
  report PDFs, and a findings digest into research-results/YYYY-MM-DD/.
- Flags are appended to ~/hep-genesis-testing/ISSUES.md automatically.

Usage:
  python harness.py [--profile NAME] [--date-suffix S]
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "hep-genesis-testing"
SCRIPTS = BASE / "scripts"
RESEARCH_RESULTS = BASE / "research-results"
ISSUES_PATH = BASE / "ISSUES.md"
STORAGE_SOFT_LIMIT_GB = 15.0
GROWTH_WARN_GB = 3.0


# ------------------------------------------------------------------ helpers

def sh(cmd, timeout=600, cwd=None, env=None, log=None):
    """Run a shell command, capture combined stdout+stderr; log to file."""
    e = dict(os.environ)
    if env:
        e.update(env)
    t0 = time.time()
    try:
        p = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            timeout=timeout, cwd=cwd, env=e,
        )
        out = (p.stdout or "") + (p.stderr or "")
        rc = p.returncode
    except subprocess.TimeoutExpired as ex:
        out = ""
        if isinstance(ex.stdout, bytes):
            out += ex.stdout.decode(errors="replace")
        elif ex.stdout:
            out += ex.stdout
        if isinstance(ex.stderr, bytes):
            out += ex.stderr.decode(errors="replace")
        elif ex.stderr:
            out += ex.stderr
        rc = 124
    dur = time.time() - t0
    if log is not None:
        log.parent.mkdir(parents=True, exist_ok=True)
        log.write_text(out)
    return rc, out


def du_gb(path) -> float:
    try:
        out = subprocess.run(["du", "-sk", str(path)], capture_output=True,
                             text=True, timeout=120)
        return int(out.stdout.split()[0]) / 1_048_576  # KB -> GB
    except Exception:
        return -1.0


def load_env_sh():
    """Source test-env.sh and capture the environment it exports."""
    rc, out = sh(f'source "{SCRIPTS}/test-env.sh" && env', timeout=60)
    if rc != 0:
        raise RuntimeError(f"sourcing test-env.sh failed: {out[:500]}")
    env = {}
    for line in out.splitlines():
        if "=" in line and not line.startswith("_"):
            k, _, v = line.partition("=")
            if re.match(r"^[A-Z][A-Z0-9_]*$", k):
                env[k] = v
    return env


def latest_release():
    rc, out = sh(
        "gh api 'repos/HEP-KE/hep-genesis-releases/releases?per_page=5' --jq "
        "'.[0] | {tag: .tag_name, published: .published_at, assets: [.assets[].name]}'"
    )
    if rc != 0:
        raise RuntimeError(f"gh api failed: {out[:500]}")
    return json.loads(out)


def install_latest(run_dir: Path, log: Path):
    """Download + install the latest wheel into the hep-genesis conda env."""
    rel = latest_release()
    tag = rel["tag"]
    wheel_name = next((a for a in rel["assets"] if a.endswith(".whl")), None)
    if not wheel_name:
        raise RuntimeError(f"no wheel asset in {tag}: {rel['assets']}")
    ver = wheel_name.split("-")[1]
    pip = str(Path.home() / "anaconda3/envs/hep-genesis/bin/pip")
    rc, cur = sh(f"{pip} show hep-genesis 2>/dev/null | head -2")
    if f"Version: {ver}" in cur:
        log.write_text(f"[install] {tag} already installed (v{ver}); skipped download\n")
        return rel, f"already installed: v{ver} ({tag})"
    dl = BASE / "downloads"
    dl.mkdir(exist_ok=True)
    rc, out = sh(
        f'cd "{dl}" && curl -sL -O "https://github.com/HEP-KE/hep-genesis-releases/releases/download/{tag}/{wheel_name}" '
        f'&& curl -sL -O "https://github.com/HEP-KE/hep-genesis-releases/releases/download/{tag}/SHA256SUMS.txt" '
        f'&& grep "{wheel_name}" SHA256SUMS.txt | shasum -a 256 -c -',
        timeout=300, log=log,
    )
    if rc != 0:
        raise RuntimeError(f"download/verify failed: {out[-800:]}")
    rc, out = sh(
        f'{pip} install --upgrade "{dl / wheel_name}[all]"',
        timeout=900, log=log,
    )
    if rc != 0:
        raise RuntimeError(f"pip install failed: {out[-800:]}")
    sh(f'rm -f {Path.home()}/anaconda3/envs/hep-genesis/bin/hep-genesis')
    return rel, f"installed v{ver} ({tag})"


# ----------------------------------------------------------- storage monitor

def check_storage(run_dir: Path) -> dict:
    free = shutil.disk_usage(BASE).free / 1e9
    now = {
        "timestamp": datetime.now().isoformat(),
        "test_tree_gb": round(du_gb(BASE), 2),
        "projects_gb": round(du_gb(BASE / "projects"), 2),
        "downloads_gb": round(du_gb(BASE / "downloads"), 2),
        "research_results_gb": round(du_gb(RESEARCH_RESULTS), 2) if RESEARCH_RESULTS.exists() else 0.0,
        "disk_free_gb": round(free, 1),
    }
    prev = sorted(BASE.glob("runs/*/storage.json"))
    if prev:
        try:
            old = json.loads(prev[-1].read_text())
            now["growth_gb_since_prev"] = round(
                now["test_tree_gb"] - old.get("test_tree_gb", now["test_tree_gb"]), 2)
        except Exception:
            pass
    now["soft_limit_hit"] = now["test_tree_gb"] > STORAGE_SOFT_LIMIT_GB
    now["growth_warn"] = now.get("growth_gb_since_prev", 0) > GROWTH_WARN_GB
    (run_dir / "storage.json").write_text(json.dumps(now, indent=2))
    if now["soft_limit_hit"] or now["growth_warn"]:
        print(f"[storage] WARNING: {json.dumps(now)}")
    else:
        print(f"[storage] ok: {now['test_tree_gb']} GB test tree, {now['disk_free_gb']} GB free")
    return now


# --------------------------------------------------------- research archival

def archive_research_results(run_dir: Path, env, project: str) -> Path:
    """Copy board.json + report PDFs + findings digest into research-results/<date>/<project>.

    Archives ALL report dirs for the project (each as report-<timestamp>/),
    deriving the date from the latest report's YYMMDD_HHMMSS name so late
    backfills land on the right day."""
    proj = Path(env["HEP_PROJECTS_DIR"]) / project
    reports = sorted(proj.glob("reports/*"))

    def date_of(name: str, fallback: str) -> str:
        m = re.match(r"(\d{2})(\d{2})(\d{2})_", name)
        return f"20{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else fallback

    today = datetime.now().strftime("%Y-%m-%d")
    copied = []
    boards = list(proj.glob("research/*/board.json"))
    for b in boards:
        # boards live under the latest report's date bucket
        d = RESEARCH_RESULTS / date_of(reports[-1].name if reports else "", today) / project
        d.mkdir(parents=True, exist_ok=True)
        shutil.copy2(b, d / f"board-{b.parent.name}.json")
        copied.append(str(b))
    for r in reports:
        d = RESEARCH_RESULTS / date_of(r.name, today) / project
        d.mkdir(parents=True, exist_ok=True)
        rdest = d / f"report-{r.name}"
        if rdest.exists():
            shutil.rmtree(rdest)
        shutil.copytree(r, rdest)
        copied.append(f"{d.name}/{project}/report-{r.name}/")
    dest = RESEARCH_RESULTS / date_of(reports[-1].name if reports else "", today) / project
    dest.mkdir(parents=True, exist_ok=True)
    boards = list(proj.glob("research/*/board.json"))
    digest = []
    for b in boards:
        try:
            bd = json.loads(b.read_text())
            for f in bd.get("findings", []):
                digest.append({
                    "id": f.get("id"), "direction": f.get("direction_id"),
                    "claim": (f.get("claim") or "")[:500],
                    "run": f.get("run_id"),
                })
        except Exception:
            pass
    (dest / "findings.json").write_text(json.dumps(digest, indent=1))
    manifest = {
        "archived_at": datetime.now().isoformat(),
        "project": project,
        "run_dir": str(run_dir),
        "copied": copied,
    }
    (dest / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return dest


# --------------------------------------------------------------- case builders

def server_specs():
    SCR = SCRIPTS
    return {
        "SBBN": f"command:{SCR}/serve-sbbn.sh",
        "IDM": f"command:{SCR}/serve-idm.sh",
        "HYD": f"command:{SCR}/serve-hydro.sh",
        "DOM": "module:hep_genesis.domain.mcp_server",
    }


def research_topics():
    """Rotating research topics spanning HEP/cosmo, matched to our MCP servers.

    Each topic declares the server spec its query assumes (server_key); the
    research profile passes that server alongside the bundled domain server.
    Without it the agent gets prompted to "use the X tools" it doesn't have
    (seen 2026-10-16 higgsino-dd and 2026-10-17 baryonic-pk runs).
    """
    return [
        dict(slug="sterile-bbn-xray", title="Sterile neutrino DM: BBN + X-ray joint constraints",
             server_key="SBBN",
             query=("Survey recent arXiv work (2024-2026) on sterile-neutrino dark matter. Combine BBN constraints "
                    "(use the sterile-nu tools for Yp/D/H numbers) and X-ray constraints: which (m_s, sin^2 2theta) "
                    "regions remain viable? Quantify with tool calls where possible.")),
        dict(slug="higgsino-dd", title="Higgsino thermal target vs direct detection",
             server_key="IDM",
             query=("Survey recent arXiv work on the higgsino thermal relic target (1.0-1.2 TeV). Use the inelastic-DM "
                    "tools to compute the relic density at several masses; compare with LZ/XENONnT sensitivities and "
                    "the Planck abundance. Where does the higgsino sit relative to current limits?")),
        dict(slug="baryonic-pk", title="Baryonic suppression of the matter power spectrum",
             server_key="HYD",
             query=("Survey recent work on baryonic suppression of the matter power spectrum. Use the hydrodynamics "
                    "emulator tools to predict the Pk-ratio at z=0 for a couple of parameter points, explain the AGN "
                    "feedback physics of suppression, and assess the impact on weak-lensing cosmology.")),
        dict(slug="sbl-neff", title="Short-baseline anomalies vs N_eff constraints",
             server_key="SBBN",
             query=("Survey the sterile-neutrino short-baseline anomaly status (2024-2026) and contrast with "
                    "BBN/CMB N_eff limits (use the BBN tools for numbers). Are eV-scale sterile neutrinos still viable?")),
        dict(slug="lyman-wdm", title="Lyman-alpha forest constraints on warm/sterile DM",
             server_key="SBBN",
             query=("Survey recent Lyman-alpha forest constraints on warm dark matter. How do they compare with "
                    "sterile-neutrino non-resonant production? Use the sterile-nu tools for production fractions.")),
        dict(slug="cluster-profiles", title="Cluster thermodynamic profiles and hydrostatic bias",
             server_key="HYD",
             query=("Survey recent work on hydrostatic mass bias in galaxy clusters. Use the hydrodynamics emulator "
                    "to predict CGD (gas density) and CTP (temperature) profiles at two redshifts and discuss how "
                    "profile shape evolution affects mass reconstruction.")),
    ]


def pick_topic():
    topics = research_topics()
    day = datetime.now().timetuple().tm_yday
    return topics[day % len(topics)]


def build_cases(env, run_dir: Path, profile: str = "core"):
    S = server_specs()
    SBBN, IDM, HYD, DOM = S["SBBN"], S["IDM"], S["HYD"], S["DOM"]
    cases = []

    def add(cid, mode, args, desc, timeout=600):
        cases.append(dict(id=cid, mode=mode, args=args, desc=desc, timeout=timeout))

    if profile == "smoke":
        add("01-help", "cli", "--help", "CLI --help renders", 60)
        add("02-quick-chat", "quick",
            '--quick "In one sentence: what is the significance of the Bullet Cluster for dark matter?" '
            '--servers none --project quick-smoke --chat plain',
            "Quick chat sanity (no tools)", 240)
        add("03-tool-discovery", "quick",
            f'--quick "List every tool you can call, in compact form." --servers {DOM} '
            '--project quick-smoke --chat dom',
            "Bundled server tool discovery", 300)
        add("04-sbbn-ping", "quick",
            f'--quick "Call describe_sterile_nu_tools and summarize what this server provides in 3 bullets." '
            f'--servers {SBBN} --project quick-smoke --chat sbbn',
            "sterile-nu-bbn server ping", 300)
        return cases

    if profile == "core":
        add("01-help-version", "cli", "--help", "CLI --help renders full usage", 60)
        add("02-list-projects", "cli", "--list-projects", "List projects", 60)
        add("03-quick-reasoning", "quick",
            '--quick "A 7 keV sterile neutrino decays radiatively with flux F proportional to '
            'sin^2(2theta) * m_s^5 / (4*pi*D^2). If the mixing is reduced by 10x, by what factor does the '
            'flux drop, and what does that imply for detectability of fainter lines? Reason step by step." '
            '--servers none --project ramp-core --chat reasoning',
            "Hard reasoning, no tools (chain-of-thought quality)", 420)
        add("04-sbbn-dw-scan", "quick",
            '--quick "Compute the Dodelson-Widrow production fraction for a 5 keV sterile neutrino with '
            'sin^2(2theta)=3e-9. Then compute it for 10 keV with the same mixing. Explain the mass scaling '
            'you observe in terms of the underlying production physics. Cite the numbers from your tool calls." '
            f'--servers {SBBN} --project ramp-core --chat sbbn',
            "sterile-nu: two-point DW scan + scaling explanation", 600)
        add("05-sbbn-bbn-scan", "quick",
            '--quick "Compute BBN predictions for N_eff = 3.0, 3.044, and 3.4. Present Yp and D/H in a table. '
            'Then answer: at what N_eff would delta-Yp exceed 1 percent of the standard value? Use tool calls for numbers." '
            f'--servers {SBBN} --project ramp-core --chat sbbn',
            "sterile-nu: 3-point BBN comparison + extrapolation", 600)
        add("06-idm-freezeout", "quick",
            '--quick "For a 100 GeV WIMP with annihilation cross section 3e-26 cm^3/s: compute the relic density '
            'today and the freeze-out temperature. Explain physically why freeze-out happens at x_f of order 20-25. '
            f'Use the tools for numbers." --servers {IDM} --project ramp-core --chat idm',
            "inelastic-dm: relic density + freeze-out reasoning", 600)
        add("07-hydro-gsmf", "quick",
            '--quick "Predict the galaxy stellar mass function (GSMF) at z=0.5 for median parameters, then at '
            'z=1.0. Describe the qualitative evolution between the two redshifts and what it means physically '
            f'(quenching vs star-forming regimes)." --servers {HYD} --project ramp-core --chat hydro',
            "hydroemu: GSMF prediction at two redshifts + interpretation", 600)
        add("08-hydro-cross", "quick",
            '--quick "Predict the cluster gas-density profile (CGD) and cluster temperature profile (CTP) at '
            'z=0.1 for median parameters. Explain how the two profiles are related physically in a galaxy '
            f'cluster (hydrostatic equilibrium hints)." --servers {HYD} --project ramp-core --chat hydro',
            "hydroemu: cross-observable physics link", 600)
        add("09-dom-data", "quick",
            '--quick "Generate a random sample of 1000 points from a Gaussian with mean 5 and sigma 2 using '
            'run_test_job. Then compute statistics and a histogram of the result. Report the mean and std you '
            'get and whether they match expectations." '
            f'--servers {DOM} --project ramp-core --chat dom',
            "Domain server: data analysis pipeline", 600)
        add("10-multi-server", "quick",
            '--quick "I am comparing dark-matter models. Using the sterile-nu server: what is the D/H prediction '
            'for N_eff=3.044? Using the inelastic-dm server: what is the thermal relic density of a 1 TeV '
            'higgsino? Present both numbers and state which model Planck data favors." '
            f'--servers {SBBN} --servers {IDM} --project ramp-core --chat multi',
            "Multi-server combo: sbbn + idm in one conversation", 900)
        return cases

    if profile == "research":
        topic = pick_topic()
        proj = f"ramp-research-{topic['slug']}"
        topic_srv = S[topic["server_key"]]
        add(f"R1-{topic['slug']}", "research",
            f'"{topic["query"]}" --project {proj} --servers {DOM} --servers {topic_srv} '
            '--max-waves 2 --workers 3 --max-tool-calls 60 --wall-clock 30',
            f"Research: {topic['title']}", 2400)
        add("R2-report", "cli", f"--report --project {proj}",
            "Generate PDF report for the research run", 900)
        return cases

    if profile == "combo":
        topic = pick_topic()
        proj = f"ramp-combo-{topic['slug']}"
        add("C1-multi-server-research", "research",
            f'"{topic["query"]}" --project {proj} '
            f'--servers {SBBN} --servers {IDM} --servers {HYD} --servers {DOM} '
            '--max-waves 2 --workers 3 --max-tool-calls 50 --wall-clock 30',
            f"Research with 4 servers: {topic['title']}", 2400)
        add("C2-report", "cli", f"--report --project {proj}",
            "Report for combo research run", 900)
        add("C3-skills", "cli", "--list-skills", "List workspace skills", 60)
        return cases

    if profile == "features":
        # find an existing research project for board/run listing (created by
        # the research/combo batteries on previous runs)
        rprojs = sorted((BASE / "runs").glob("*/cases/R1-*.meta.json")) + \
                 sorted((BASE / "runs").glob("*/cases/C1-*.meta.json"))
        rproj = "hep-testing-research"  # exists since first session; safe fallback
        if rprojs:
            try:
                m = json.loads(rprojs[-1].read_text())
                rproj = re.search(r"--project (\S+)", m["cmd"]).group(1)
            except Exception:
                pass
        add("F1-list-chats", "cli", "--list-chats --project ramp-core", "List chats in a project", 60)
        add("F2-board", "cli", f"--board --project {rproj}",
            "Board of a research project", 60)
        add("F3-list-runs", "cli", f"--list-runs --project {rproj}",
            "List research runs", 60)
        add("F4-temperature", "quick",
            '--quick "Estimate the number of galaxies in the observable universe. Show your reasoning." '
            '--servers none --temperature 0.7 --project ramp-features --chat temp07',
            "Temperature parameter (0.7)", 420)
        add("F5-table", "quick",
            '--quick "Use tools to compute, for m_s = 7 keV and sin^2(2theta)=1e-10: (a) the radiative lifetime, '
            '(b) the DW production fraction, (c) the X-ray line energy. Present all three in a table." '
            f'--servers {SBBN} --project ramp-features --chat table --max-rounds 20',
            "Table-formatted multi-tool answer + --max-rounds", 600)
        add("F6-quick-report", "quick",
            '--quick "What is the Hubble tension? Two paragraphs, then write a report." --report '
            '--servers none --project ramp-features --chat hubble',
            "Quick mode + report generation in one invocation", 900)
        add("F7-memory", "quick",
            '--quick "Remember this lesson for future sessions: when predicting with the hydro emulator, always '
            'state the redshift first. Then confirm you saved it." '
            f'--servers {DOM} --project ramp-features --chat mem',
            "Memory tool (remember) + confirmation", 600)
        add("F8-skill", "quick",
            '--quick "Load the skill named statistical-analysis if available, then summarize what it instructs." '
            f'--servers {DOM} --project ramp-features --chat skill',
            "Skill loading in quick mode", 600)
        # F8 needs a real skill file in $HEP_WORKSPACE_DIR/skills/ — the CLI
        # only lists files with `name:` frontmatter (ISSUES.md #18). Create it
        # if missing so the load path is always exercised.
        _ws = os.environ.get("HEP_WORKSPACE_DIR", str(Path.home() / "HEP-Genesis"))
        _sd = Path(_ws) / "skills"
        _sd.mkdir(parents=True, exist_ok=True)
        _skill = _sd / "statistical-analysis.md"
        if not _skill.exists():
            _skill.write_text(  # pragma: no cover - test fixture
                "---\nname: statistical-analysis\n"
                "description: Guidance for statistical analysis of data tables.\n---\n\n"
                "# Statistical Analysis\n\n"
                "- Report the sample size N alongside every statistic.\n"
                "- Uncertainties to one significant figure; values matched to that decimal place.\n"
                "- State whether errors are statistical or systematic.\n"
                "- Prefer robust estimators (median, MAD) for N < 30.\n"
                "- For fits, report chi-squared per dof and covariance diagnostics.\n"
            )
        add("F9-research-noservers", "research",
            '"Give a rough estimate, with reasoning, of how many arXiv papers on galaxy cluster physics were '
            'published in 2025." --project ramp-features --servers none '
            '--max-waves 1 --workers 1 --max-tool-calls 15 --wall-clock 10',
            "Research mode with no servers (pure LLM multi-step)", 900)
        return cases

    raise ValueError(f"unknown profile {profile}")


# ------------------------------------------------------------------- judging

def judge(case, rc, out):
    """Heuristic pass/flag judgment per case type."""
    low = out.lower()
    if rc == 124:
        return False, "harness timeout"
    if case["mode"] == "cli":
        if rc == 0 and len(out.strip()) > 20:
            return True, "exit 0, output present"
        return False, f"rc={rc}, output={len(out)} chars"
    # quick / research
    if "traceback (most recent call last)" in low:
        if "tokens:" in low or "final" in low:
            return False, "traceback present (run may have continued)"
        return False, "python traceback in output"
    if rc != 0:
        return False, f"nonzero exit rc={rc}"
    if len(out.strip()) < 100:
        return False, "suspiciously short output"
    if "error" in low and "final" not in low and len(out) < 500:
        return False, "error-like output"
    return True, "exit 0 with substantive output"


def run_case(case, env, run_dir: Path):
    slug = case["id"]
    cases_dir = run_dir / "cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    print(f"  [{slug}] {case['desc']}")
    hgbin = env["HG_BIN"]
    cmd = f'"{hgbin}" {case["args"]}'
    rc, out = sh(cmd, timeout=case.get("timeout", 600), env=env,
                 log=cases_dir / f"{slug}.out")
    dur = time.time() - t0
    passed, note = judge(case, rc, out)
    meta = {
        "id": slug,
        "desc": case["desc"],
        "mode": case["mode"],
        "cmd": cmd.replace(env.get("LLM_API_KEY", "KEY"), "***"),
        "rc": rc,
        "duration_s": round(dur, 1),
        "passed": passed,
        "note": note,
        "timestamp": datetime.now().isoformat(),
    }
    (cases_dir / f"{slug}.meta.json").write_text(json.dumps(meta, indent=2))
    status = "PASS" if passed else "FLAG"
    print(f"      -> {status} in {dur:.0f}s ({note[:110]})")
    return meta


# -------------------------------------------------------------------- main

def append_issues(run_id, metas):
    flagged = [m for m in metas if not m["passed"]]
    n_pass = len(metas) - len(flagged)
    lines = [f"\n## {run_id} — {n_pass} pass / {len(flagged)} flagged\n"]
    if flagged:
        for m in flagged:
            lines.append(f"### {m['id']} — {m['desc']}\n")
            lines.append(f"- rc={m['rc']}, duration={m['duration_s']}s, note: {m['note']}\n")
            lines.append(f"- transcript: runs/{run_id}/cases/{m['id']}.out\n")
    else:
        lines.append("Clean run — no flags.\n")
    with open(ISSUES_PATH, "a") as f:
        f.write("\n".join(lines) + "\n")
    return len(flagged)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="core",
                    choices=["smoke", "core", "research", "combo", "features"])
    ap.add_argument("--date-suffix", default=None,
                    help="e.g. 'am' to make runs/2026-10-16-am-core/")
    args = ap.parse_args()

    run_id = datetime.now().strftime("%Y-%m-%d")
    if args.date_suffix:
        run_id += f"-{args.date_suffix}"
    run_id += f"-{args.profile}"
    run_dir = BASE / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    install_log = run_dir / "install.log"
    print(f"[harness] session dir: {run_dir}")
    print(f"[harness] profile: {args.profile}")

    env = load_env_sh()
    if not env.get("LLM_API_KEY"):
        print("[harness] FATAL: no LLM_API_KEY resolved", file=sys.stderr)
        sys.exit(2)
    print(f"[harness] backend: {env.get('LLM_URL')} / {env.get('LLM_MODEL')}")
    if "opus" not in (env.get("LLM_MODEL") or ""):
        print(f"[harness] NOTE: backend is not Opus — model={env.get('LLM_MODEL')}")

    storage = check_storage(run_dir)

    try:
        rel, ver_out = install_latest(run_dir, install_log)
        print(f"[install] {ver_out}")
        print(f"[install] release: {rel['tag']} (published {rel['published']})")
    except Exception as e:
        tb = traceback.format_exc()
        (run_dir / "INSTALL_FAILED.txt").write_text(tb)
        with open(ISSUES_PATH, "a") as f:
            f.write(f"\n## {run_id} — INSTALL FAILED\n\n```\n{tb}\n```\n")
        print(f"[install] FAILED: {e}", file=sys.stderr)
        sys.exit(3)

    cases = build_cases(env, run_dir, profile=args.profile)
    metas = []
    for c in cases:
        try:
            metas.append(run_case(c, env, run_dir))
        except Exception as e:
            print(f"  [{c['id']}] EXCEPTION: {e}")
            metas.append({
                "id": c["id"], "desc": c["desc"], "mode": c["mode"],
                "rc": -1, "duration_s": 0, "passed": False,
                "note": f"harness exception: {e}",
                "timestamp": datetime.now().isoformat(),
            })

    # Archive research results for ANY case that produced a report dir,
    # regardless of profile (features battery also runs research cases).
    archived_projects = set()
    for case in cases:
        for proj in re.findall(r"--project (\S+)", case["args"]):
            if proj in archived_projects:
                continue
            try:
                archive_research_results(run_dir, env, proj)
                archived_projects.add(proj)
                print(f"[archive] {proj} -> research-results/")
            except Exception as e:
                print(f"[archive] FAILED for {proj}: {e}")

    n_flagged = append_issues(run_id, metas)
    if n_flagged:
        print(f"[issues] {n_flagged} flagged -> appended to {ISSUES_PATH}")

    n_pass = len(metas) - n_flagged
    summary = [
        f"# HEP-Genesis-Agent test session — {run_id}",
        "",
        f"- Version under test: {rel['tag']} (published {rel['published']})",
        f"- Profile: {args.profile}",
        f"- Backend: {env.get('LLM_URL')} / {env.get('LLM_MODEL')}",
        f"- Cases: {len(metas)} total, {n_pass} pass, {n_flagged} flagged",
        f"- Storage: test tree {storage['test_tree_gb']} GB "
        f"(free {storage['disk_free_gb']} GB)"
        + (" **⚠ SOFT LIMIT HIT**" if storage["soft_limit_hit"] else "")
        + (" **⚠ GROWTH WARN**" if storage.get("growth_warn") else ""),
        "",
        "## Results",
        "",
        "| # | Case | Mode | Status | Time | Note |",
        "|---|------|------|--------|------|------|",
    ]
    for i, m in enumerate(metas, 1):
        status = "✅ PASS" if m["passed"] else "🚩 FLAG"
        summary.append(
            f"| {i} | {m['id']} | {m['mode']} | {status} | "
            f"{m['duration_s']}s | {m['note'][:80]} |")
    flagged = [m for m in metas if not m["passed"]]
    if flagged:
        summary += ["", "## Flagged issues", ""]
        for m in flagged:
            summary.append(f"### {m['id']} — {m['desc']}")
            summary.append(f"- rc={m['rc']}, duration={m['duration_s']}s")
            summary.append(f"- note: {m['note']}")
            summary.append(f"- transcript: cases/{m['id']}.out")
            summary.append("")
    (run_dir / "summary.md").write_text("\n".join(summary))
    print(f"\n[harness] done: {n_pass} pass / {n_flagged} flagged")
    print(f"[harness] summary: {run_dir / 'summary.md'}")
    return 0 if n_flagged == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
