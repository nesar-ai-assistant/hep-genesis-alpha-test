---
name: hpc-troubleshooting
description: Map HPC/dispatch failure signatures (auth 401s, Globus PERMISSION_DENIED, queue rejections) to their fixes
---

When a facility or dispatched tool fails, match the signature and relay the
fix — do not blind-retry, and never ask the user to paste tokens into chat.

- 401 mentioning high-assurance / Keycloak: the ~24 h ALCF MFA session
  expired. User re-logs in via HPC panel (ALCF · IRI API).
- Globus PERMISSION_DENIED naming a LOCAL path ("Path not allowed"): the
  local Globus Connect Personal denies that folder (dot-folders are denied by
  default). Files must live under ~/hep-genesis/; or the user adds the path
  in GCP → Preferences → Access.
- Globus PERMISSION_DENIED mentioning a session/domain: facility DTN policy
  needs a fresh interactive login. User: app.globus.org/logout, then HPC
  panel → Transfer Re-login for that facility.
- Upload stuck ACTIVE forever, or a dispatch error saying Globus Connect
  Personal is NOT CONNECTED or PAUSED: GCP on the user's machine is quit,
  paused or dropped its connection. Tell the user to start it from the HPC
  panel (Globus staging section, Start) and resubmit once it shows
  connected; auth_status reports its state.
- list_projects 401 vs "no allocations": 401 = not signed in (auth_status
  explains). An EMPTY allocations list is real — the project has no active
  allocation; that is fixed at the facility accounts portal, not here.
- Walltime rejected: 300 s is the exact floor. Polaris debug: ≤2 nodes,
  1 queued job/user. Perlmutter debug QOS: ≤30 min.
- submit_job 404/400: resource_id must be the UUID from list_resources, and
  ALCF requires account = project name. But if the goal is running science
  code, switch to set_dispatch + domain compute tools instead.
- Client timeout on a dispatched or run_pack_kernel call: the facility job
  may STILL be running — do NOT resubmit (that queues a duplicate job).
  Check job/run status or reconnect and fetch results; a first run on a
  facility adds ~5-10 min building the persistent remote environment.
- A tool result starting with HARD FAIL is final for this run — surface its
  message (it names the fix) and stop retrying that call.
