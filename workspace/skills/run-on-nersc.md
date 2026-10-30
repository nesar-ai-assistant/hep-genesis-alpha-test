---
name: run-on-nersc
description: Run a science computation on NERSC Perlmutter: prerequisites, the set_dispatch flow, and differences from ALCF
---

Use this when the user asks to run a computation on NERSC / Perlmutter.

For kernels that live on a HOSTED server (its auth_status says the dispatch
backend is missing), use the run-hosted-pack-on-hpc skill instead —
set_dispatch below only affects servers running on THIS machine.

Same flow as ALCF, different site name:

1. Call auth_status (nersc-tools). If tokens are missing, relay its
   instructions — the user signs in via the HPC panel (NERSC · IRI API and
   NERSC · Globus Transfer). NERSC also needs its Globus Native App IDs
   (NERSC_IRI_CLIENT_ID, NERSC_IRI_RS_ID) configured in the HPC panel once.
2. Call set_dispatch with site "perlmutter".
3. Call the SAME domain compute tools you would use locally — they stage code,
   submit a Slurm job through IRI, poll, and fetch results/artifacts back.
   Nothing needs to pre-exist on Perlmutter.
4. Warn the user it takes minutes (queue + walltime; first run may add ~5-10
   min building the persistent remote environment).

NERSC specifics: the IRI filesystem API is fully implemented there (upload/
download work), so staging can go over IRI as well as Globus — the backend
picks automatically. Debug QOS caps walltime at 30 min; longer jobs need
qos=regular. Do NOT use the raw submit_job tool for science code — use the
dispatch flow above. If a dispatched tool returns a HARD FAIL error, surface
it to the user instead of retrying.
