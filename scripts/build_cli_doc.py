#!/usr/bin/env python3
"""Assemble the CLI usage doc page: releases-page skeleton + our content sections."""
from pathlib import Path

DOCS = Path.home() / "hep-genesis-testing" / "docs"
skeleton = (DOCS / "page-skeleton.html").read_text()
icons = (DOCS / "page-icons.svg").read_text()

# skeleton ends with </head>; open <body> + icon sprite right after </head>,
# BEFORE the topbar (which we keep and re-theme below)
skeleton = skeleton.rstrip().replace(
    "</head>", "</head>\n<body>\n" + icons, 1)

# retitle
skeleton = skeleton.replace("<title>HEP-Genesis-Agent</title>",
                            "<title>HEP-Genesis-Agent CLI — Usage Guide</title>")

# replace topbar nav + hero with our own (keep structure/classes)
old_hero_start = skeleton.find('<header class="topbar">')
hero_content = '''<header class="topbar">
  <div class="wrap">
    <div class="brand"><svg width="22" height="22"><use href="#logo"/></svg> HEP-Genesis-Agent</div>
    <nav class="nav">
      <a href="#basics">Basics</a>
      <a href="#quick">Quick mode</a>
      <a href="#research">Research mode</a>
      <a href="#servers">MCP servers</a>
      <a href="#llm">LLM backends</a>
      <a href="#control">Run control</a>
      <a href="#recipes">Recipes</a>
      <a href="https://hep-ke.github.io/hep-genesis-releases/">Releases&nbsp;↗</a>
    </nav>
  </div>
</header>

<div class="wrap hero" style="padding-block:64px 40px">
  <h1>Running HEP-Genesis-Agent from the command line.</h1>
  <p class="sub" style="max-width:760px">Every feature of the desktop app is scriptable: quick tool-backed chats,
  autonomous research runs with reports, MCP tool servers, custom LLM endpoints, and HPC dispatch.
  This guide documents the CLI as exercised in practice during alpha testing (v0.4.4).</p>
  <div class="actions">
    <a class="btn" href="#basics">Get started</a>
    <a class="btn ghost" href="#recipes">Recipe gallery</a>
  </div>
</div>
'''
skeleton = skeleton[:old_hero_start] + hero_content

sections = '''

<section id="basics">
  <div class="wrap">
    <div class="head">
      <div class="kicker">Basics</div>
      <h2>Install and invoke</h2>
      <p class="sub">The CLI is a Python wheel (requires Python 3.10+). The binary is <code>hep-genesis-agent</code>.</p>
    </div>
    <div class="grid g2">
      <div class="card">
        <h3>Install</h3>
        <div class="code"><pre>pip install --upgrade hep_genesis-0.4.4-py3-none-any.whl[all]</pre></div>
        <p>Grab the wheel from the releases page, verify against <code>SHA256SUMS.txt</code>, and install with the
        <code>[all]</code> extra (report LaTeX support, arXiv tooling). The CLI installs into your active Python
        environment as <code>hep-genesis-agent</code>.</p>
      </div>
      <div class="card">
        <h3>First commands</h3>
        <div class="code"><pre>hep-genesis-agent --help
hep-genesis-agent --list-projects
hep-genesis-agent --version</pre></div>
        <p>Everything is organized around <em>projects</em> (a directory with chats, research runs, reports,
        and provenance) and <em>chats</em> (a named conversation inside a project, default <code>default</code>).</p>
      </div>
    </div>
    <div class="code"><pre># minimal quick-mode call (no tools):
hep-genesis-agent --quick "What is 2+2?" --servers none --project demo

# two chat modes share one backend:
#   quick   — the model calls tools directly, conversation-style
#   research— plans, runs worker directions, critiques, writes a report</pre></div>
  </div>
</section>

<section id="quick">
  <div class="wrap">
    <div class="head">
      <div class="kicker">Quick mode</div>
      <h2>Tool-backed chat</h2>
      <p class="sub">Quick mode answers one question (or a follow-up in the same chat) using any connected MCP servers.</p>
    </div>
    <div class="code"><pre>hep-genesis-agent --quick "compute the relic density of a 1.1 TeV higgsino" \\
    --servers command:/path/to/serve-idm.sh \\
    --project dark-matter --chat idm</pre></div>
    <div class="grid g2">
      <div class="card">
        <h3>Key flags</h3>
        <p><code>--chat NAME</code> — named conversation; reusing a name keeps context, so follow-ups work.<br>
        <code>--servers SPEC</code> — which MCP servers to attach (repeatable).<br>
        <code>--max-rounds N</code> — cap tool-calling rounds (default 30).<br>
        <code>--temperature X</code> — sampling temperature (default 0.0).<br>
        <code>--report</code> — write the PDF report of the chat after answering.</p>
      </div>
      <div class="card">
        <h3>Follow-ups keep context</h3>
        <div class="code"><pre># turn 1
hep-genesis-agent --quick "list the emulators you have" \\
    --project qcd --servers module:hep_genesis.domain.mcp_server
# turn 2 — same chat, remembers turn 1
hep-genesis-agent --quick "now plot P(k) for the first one" \\
    --project qcd --servers module:hep_genesis.domain.mcp_server</pre></div>
      </div>
    </div>
  </div>
</section>

<section id="research">
  <div class="wrap">
    <div class="head">
      <div class="kicker">Research mode</div>
      <h2>Autonomous multi-step research</h2>
      <p class="sub">Research mode plans directions, runs them (optionally in parallel), critiques its own findings, and writes a LaTeX/PDF report.</p>
    </div>
    <div class="code"><pre>hep-genesis-agent "Survey recent arXiv work on sterile-neutrino dark matter and BBN constraints" \\
    --project sterile-dm \\
    --servers module:hep_genesis.domain.mcp_server \\
    --max-waves 2 --workers 3 --max-tool-calls 60 --wall-clock 30</pre></div>
    <div class="grid g3">
      <div class="card">
        <h3>Budget flags</h3>
        <p><code>--max-waves</code> — rounds of directions (default 4).<br>
        <code>--workers</code> — parallel directions (default 5).<br>
        <code>--max-tool-calls</code> — total tool budget (default 400).<br>
        <code>--wall-clock</code> — minutes (default 120).</p>
      </div>
      <div class="card">
        <h3>Phases</h3>
        <p>survey → plan → critic-plan → wave(s) → critic-wave → replan → report. Each wave posts findings to a
        <em>board</em> with claims and evidence; critics can close or block directions.</p>
      </div>
      <div class="card">
        <h3>Outputs</h3>
        <p><code>reports/&lt;timestamp&gt;/</code> — report.pdf, supplement.pdf, transcript.pdf (+ .tex sources).
        <code>research/&lt;chat&gt;/board.json</code> — machine-readable findings. Run events in
        <code>runs/&lt;run-id&gt;/events.jsonl</code>.</p>
      </div>
    </div>
    <div class="code"><pre>hep-genesis-agent --board --project sterile-dm        # view findings/critiques
hep-genesis-agent --list-runs --project sterile-dm   # list runs
hep-genesis-agent --show-run RUN_ID --project sterile-dm
hep-genesis-agent --report --project sterile-dm      # (re)generate the PDF</pre></div>
  </div>
</section>

<section id="servers">
  <div class="wrap">
    <div class="head">
      <div class="kicker">MCP servers</div>
      <h2>Connecting tool servers</h2>
      <p class="sub">Four spec forms; <code>--servers</code> is repeatable and accepts a comma-separated list.</p>
    </div>
    <div class="code"><pre># module: a Python module inside the app (bundled servers)
--servers module:hep_genesis.domain.mcp_server

# command: launch any executable that speaks MCP over stdio (most robust)
--servers command:/abs/path/serve-my-server.sh
--servers command:/abs/path/serve.sh?name=my-server        # custom display name

# url: hosted HTTP server
--servers url:https://example.edu/mcp

# path or git URL: pip-installs the server repo (see caveat below)
--servers /path/to/my-mcp-repo
--servers https://github.com/org/my-mcp-server</pre></div>
    <div class="note callout">
      <strong>What's new in v0.4.4 (2026-10-30):</strong> v0.4.4 syncs CIMD client metadata. Since v0.4.2, <code>load_table_data</code> auto-detects CSV header rows and reads <code>.npy/.npz</code> (fixes <a href="https://github.com/HEP-KE/hep-genesis-releases/issues/8">#8</a>/<a href="https://github.com/HEP-KE/hep-genesis-releases/issues/12">#12</a>); arXiv 429/503 rate-limits surface as retryable errors with a Semantic Scholar fallback; <code>--board</code>/<code>--list-runs</code> no longer create phantom projects and print a helpful hint when empty; <code>--report</code> deduplicates when the query already generated a report. Long tool outputs are wrapped in a marker and spilled to disk instead of silent 20k truncation. See <a href="https://github.com/HEP-KE/hep-genesis-releases/releases/tag/v0.4.4">release notes</a>.
    </div>
    <div class="note callout">
      <strong>Practical caveat (v0.4.4):</strong> path/git specs expect the repo to define a
      <code>[project.scripts]</code> console entry point; servers that ship as <code>python -m mcp_server</code>
      (a common pattern, including several HEP-KE servers) fail to launch with <code>FileNotFoundError</code>.
      Use <code>command:</code> with a small wrapper script until that is fixed
      (<a href="https://github.com/HEP-KE/hep-genesis-releases/issues/1">issue #1</a>).
    </div>
    <div class="grid g2">
      <div class="card">
        <h3>Wrapper recipe</h3>
        <div class="code"><pre>#!/bin/bash
cd /path/to/my-mcp-repo || exit 1
exec .venv/bin/python -m mcp_server "$@"</pre></div>
        <p>Point <code>--servers command:</code> at this. Per-server venvs avoid dependency collisions
        (e.g. an emulator pinned to <code>scipy&lt;1.11</code>).</p>
      </div>
      <div class="card">
        <h3>Bundled server</h3>
        <p><code>module:hep_genesis.domain.mcp_server</code> ("hep-research-aid") ships with the wheel:
        arXiv search/download, table loading and statistics, histograms, file I/O, skills, memory,
        report writing, and local/HPC dispatch (<code>set_dispatch local|polaris|perlmutter</code>).</p>
      </div>
    </div>
  </div>
</section>

<section id="llm">
  <div class="wrap">
    <div class="head">
      <div class="kicker">LLM backends</div>
      <h2>Custom endpoints and per-stage models</h2>
      <p class="sub">Any OpenAI-compatible endpoint works; configuration is via environment variables.</p>
    </div>
    <div class="code"><pre>export LLM_URL="https://your-gateway.example.org/v1"
export LLM_MODEL="claude-opus-5-5"          # or gpt-5.6-luna@openai, ...
export LLM_API_KEY="..."                     # from your provider

# optional: a different model per research stage
export LLM_SURVEY_MODEL="claude-haiku-5-5"
export LLM_WORKER_MODEL="claude-opus-5-5"
export LLM_CRITIC_MODEL="claude-opus-5-5"
export LLM_REPORT_MODEL="claude-opus-5-5"</pre></div>
    <div class="grid g2">
      <div class="card">
        <h3>Verified endpoints</h3>
        <p>Tested against the MAG gateway (<code>mag.genesis.americansciencecloud.org</code>) with
        <code>gpt-5.6-luna@openai</code> and <code>claude-opus-5-5</code> — both drive tool calls correctly.
        Per-stage overrides are read as <code>LLM_&lt;STAGE&gt;_URL/_MODEL/_API_KEY</code>.</p>
      </div>
      <div class="card">
        <h3>Token accounting</h3>
        <p>Every invocation ends with a usage line, e.g.
        <code>Tokens: 12K in (7.0K cached) · 369 out · 3 calls</code>. Research runs break it down per stage
        (worker / survey / report / critic / plan) — useful for cost tracking on metered gateways.</p>
      </div>
    </div>
  </div>
</section>

<section id="control">
  <div class="wrap">
    <div class="head">
      <div class="kicker">Run control</div>
      <h2>Steer, pause, resume, continue</h2>
      <p class="sub">Long research runs can be supervised and revived from another terminal.</p>
    </div>
    <div class="code"><pre>hep-genesis-agent --steer RUN_ID "also compare against the Planck value" --project sterile-dm
hep-genesis-agent --pause RUN_ID --project sterile-dm
hep-genesis-agent --resume RUN_ID --project sterile-dm      # or: query "continue"
hep-genesis-agent --stop RUN_ID --project sterile-dm        # stop and write the report
hep-genesis-agent --continue d-04 --project sterile-dm --servers ...   # one open direction</pre></div>
    <div class="grid g2">
      <div class="card">
        <h3>Coding tasks</h3>
        <p><code>--coding</code> enables the last-resort <code>run_coding_task</code> tool (pi harness); all code is
        saved under the project. Useful for one-off data wrangling a tool can't express.</p>
      </div>
      <div class="card">
        <h3>Workspace: skills &amp; memory</h3>
        <div class="code"><pre>hep-genesis-agent --list-skills      # workspace skills
# in chat: "Remember this lesson: ..." → remember tool
#          "Load the skill named X"   → load_skill tool</pre></div>
        <p>Workspace dir is configurable via <code>HEP_WORKSPACE_DIR</code>; projects via
        <code>HEP_PROJECTS_DIR</code>.</p>
      </div>
    </div>
  </div>
</section>

<section id="recipes">
  <div class="wrap">
    <div class="head">
      <div class="kicker">Recipes</div>
      <h2>Worked examples from alpha testing</h2>
      <p class="sub">Commands below were actually run against v0.4.4 with real MCP servers attached.</p>
    </div>
    <div class="grid g2">
      <div class="card">
        <h3>Physics query + explanation</h3>
        <div class="code"><pre>hep-genesis-agent --quick \\
  "Compute the DW production fraction of a 1 keV sterile
   neutrino with sin^2(2theta)=1e-8, and its radiative
   lifetime in seconds." \\
  --servers command:.../serve-sbbn.sh \\
  --project dm --chat sbbn</pre></div>
        <p>The agent called <code>predict_sterile_nu</code>, then explained the
        τ ∝ m<sup>−5</sup> scaling — correct against the tool's own numbers.</p>
      </div>
      <div class="card">
        <h3>Multi-server comparison</h3>
        <div class="code"><pre>hep-genesis-agent --quick \\
  "What is D/H for N_eff=3.044 (sterile-nu server) and
   the relic density of a 1 TeV higgsino (inelastic-dm
   server)? Which does Planck favor?" \\
  --servers command:.../serve-sbbn.sh \\
  --servers command:.../serve-idm.sh \\
  --project dm --chat multi</pre></div>
        <p>Two servers, one conversation, correct routing of each sub-question to the right tool.</p>
      </div>
      <div class="card">
        <h3>Bounded literature survey</h3>
        <div class="code"><pre>hep-genesis-agent \\
  "Survey 2024-2026 arXiv papers on sterile-neutrino DM
   and BBN. Which mass-mixing regions remain viable?" \\
  --project sterile-dm \\
  --servers module:hep_genesis.domain.mcp_server \\
  --max-waves 1 --workers 2 --max-tool-calls 25 \\
  --wall-clock 15</pre></div>
        <p>Downloaded 8 papers, produced 10 board findings and an honest PDF report
        (it flagged its own full-text extraction failure rather than inventing numbers).</p>
      </div>
      <div class="card">
        <h3>Data analysis in one line</h3>
        <div class="code"><pre>hep-genesis-agent --quick \\
  "Generate 1000 Gaussian(5, 2) samples via run_test_job,
   then compute statistics and a histogram." \\
  --servers module:hep_genesis.domain.mcp_server \\
  --project stats --chat dom</pre></div>
        <p>Chained tool calls across the bundled server's data pipeline.</p>
      </div>
    </div>
    <p class="meta-line" style="margin-top:16px">Environment variables: <code>LLM_URL</code> ·
    <code>LLM_MODEL</code> · <code>LLM_API_KEY</code> · <code>HEP_PROJECTS_DIR</code> ·
    <code>HEP_WORKSPACE_DIR</code> · per-stage <code>LLM_{SURVEY,PLAN,WORKER,CRITIC,REPORT}_*</code>.
    Full test log: <code>~/hep-genesis-testing/</code> (alpha-testing workspace).</p>
  </div>
</section>

<footer style="border-top:1px solid var(--line-soft);margin-top:8px">
  <div class="wrap" style="display:flex;align-items:center;gap:16px;padding-block:28px;color:var(--text-faint);font-size:13.5px">
    <svg width="18" height="18"><use href="#logo"/></svg>
    <span>HEP-Genesis-Agent CLI usage guide — alpha-testing edition (v0.4.4). Format matches the
    <a href="https://hep-ke.github.io/hep-genesis-releases/">releases page</a>.</span>
  </div>
</footer>

</body>
</html>
'''

page = skeleton + sections
out = DOCS / "cli-usage.html"
out.write_text(page)
print(f"wrote {out} ({len(page)} chars)")
