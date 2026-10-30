---
name: run-hosted-pack-on-hpc
description: Run a HOSTED MCP server's science kernels on ALCF/NERSC with THIS machine's credentials: the export_dispatch_pack → run_pack_kernel handoff, step by step
---

Use this when the user wants a computation from a HOSTED server (its
auth_status says the dispatch backend is not installed, or its files live on
a remote host) executed on a DOE facility. The server hands its kernels
over; THIS machine — which holds the facility tokens — dispatches them.

THE FLOW (each numbered call is one tool call):

1. auth_status on the facility server (alcf-tools or nersc-tools).
   Missing tokens → relay its sign-in instructions; stop.
2. export_dispatch_pack on the hosted server. The app saves the kernel files
   to disk and replies with pack_path plus a kernels manifest (function,
   args shape, pip_deps_by_backend, base_pip_deps, duration hints).
3. run_pack_kernel on the facility server, one call per kernel run:
   - pack: EXACTLY the pack_path from step 2 (it ends in the package name,
     e.g. .../code/packs/<server>/tools). NEVER pass a run or output
     directory — the tool rejects packs that don't contain the function.
   - function + args: from the manifest (args is a JSON object string).
   - pip_deps: base_pip_deps + the chosen backend's entry, exactly.
   - artifact_dir: your run directory. The kernel's returned arrays are also
     saved there as <function>_result.json/.csv, alongside fetched job logs.
   - duration: the manifest's hint; queue "debug" unless the user says else.
4. Verify: the result's "host" field names the compute node — quote it when
   reporting. No host field = it did not run on the facility; say so.

PITFALLS (each has burned real time):
- set_dispatch on one server NEVER affects another server's tools. For
  hosted servers use THIS handoff; set_dispatch is for servers that run on
  this machine.
- One run_pack_kernel call = one facility job (minutes; a first run may add
  ~5-10 min building the persistent remote env). Calls run sequentially —
  tell the user the expected wait up front.
- Plots: hosted servers cannot read this machine's files, so never pass
  local CSV paths to their plot tools. Either present the numbers /
  <function>_result.csv directly, or — for seeded, deterministic emulators —
  recompute on the hosted server locally for plotting and SAY the figure was
  rendered from an identical local recompute of the facility result.
- If a call returns a structured error, do NOT retry the same call — the
  message names the fix; surface it.
