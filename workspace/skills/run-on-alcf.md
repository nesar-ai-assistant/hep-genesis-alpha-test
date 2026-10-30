---
name: run-on-alcf
description: Run a science computation on ALCF Polaris: prerequisites, the set_dispatch flow, and what to expect
---

Use this when the user asks to run a computation on ALCF / Polaris.

For kernels that live on a HOSTED server (its auth_status says the dispatch
backend is missing), use the run-hosted-pack-on-hpc skill instead —
set_dispatch below only affects servers running on THIS machine.

THE ONE CORRECT PATH for local servers: dispatch through the domain compute tools.

1. Check readiness: call auth_status (alcf-tools). If a token is missing,
   relay its instructions — the user signs in via the HPC panel (ALCF · IRI API
   and ALCF · Globus Transfer). Never ask for tokens in chat.
2. Call set_dispatch with site "polaris".
3. Call the SAME compute tools you would use locally (run_test_job on the
   domain server verifies the pipeline; dispatch-capable science servers'
   compute tools work the same way).
   Each dispatched call stages the science code, submits a PBS job through IRI
   under the configured project, polls for results, and transfers artifacts
   back automatically. Nothing needs to pre-exist on Polaris.
4. Tell the user BEFORE the first dispatched call that it takes minutes
   (queue + walltime; a first run may add ~5-10 min building the persistent
   remote environment). Results come back as session datasets; artifacts
   (stdout/stderr, files) land under ~/hep-genesis/artifacts/.
5. Call set_dispatch("local") when done if the user wants later calls local.

Do NOT use the raw facility submit_job tool to run science code — it executes
a pre-existing binary and stages nothing. Facility tools are for status,
allocations, files, and monitoring (list_jobs, get_job_status, read_file).

Prerequisites (from the HPC panel, not chat): ALCF sign-ins, a project with an
active allocation (check list_projects + get_project_allocations), a facility
workdir, and Globus Connect Personal running locally.

Constraints to respect: debug queue allows 1 queued job per user, max 2 nodes
(3-10 nodes route to debug-scaling/preemptable, 10+ to prod; the HPC panel's
node cap, ALCF_MAX_NODES, is enforced before staging); walltime floor is
exactly 300 s. If a dispatched tool returns a HARD FAIL
error, do not retry — surface the message (it contains the fix) to the user.
