---
name: verify-hpc-dispatch
description: Verify a facility works end to end (IRI auth, Globus, scheduler, results back) with a cheap test job
---

Use this when the user asks whether ALCF/NERSC dispatch works, or after
sign-in / configuration changes, or before a long science run.

1. auth_status on the facility server (alcf-tools or nersc-tools)
   — relay any missing-token instructions (sign-in happens in the HPC panel,
   never in chat).
2. set_dispatch with site "polaris" or "perlmutter" (domain server).
3. run_test_job (domain server) — e.g. distribution='normal', n=100000,
   seed=42. This stages code, uploads via Globus, submits through IRI, runs
   on a compute node, and fetches results + a samples.csv artifact back.
   Tell the user first that it takes ~1-5 minutes including queue time and
   costs a negligible amount of allocation.
4. Report the returned verdict: computed_on (the compute node hostname),
   summary statistics (normal(0,1) should give mean ≈ 0, stdev ≈ 1), and
   artifact locations under ~/hep-genesis/artifacts/.
5. set_dispatch("local") afterwards unless the user wants to stay remote.

If it fails with HARD FAIL, the error names the broken layer (IRI auth,
Globus/GCP, scheduler) and the fix — surface it, do not retry. The HPC
panel's Test buttons run the quick IRI/Globus halves of this without a job.
