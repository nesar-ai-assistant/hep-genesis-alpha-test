---
name: estimate-data-volume
description: Before any query, download, or transfer that could move a lot of data to this machine: estimate the size, explain it, and prefer reducing it at the source
---

Use this BEFORE any call that brings data to this machine or moves it
between sites: catalog / table queries, particle or event dumps, file
downloads (HDF5, parquet, FITS, ROOT, NanoAOD, ...), dataset hubs, facility
artifacts fetched back after a dispatched job, Globus transfers. It applies
to every server and every science domain, not one data service.

1. ESTIMATE before fetching. Take the size from the cheapest reliable
   source, in this order:
   - Metadata the source already exposes: file listings / stat on the
     facility, a dataset's documentation or describe tool, a count or
     "dry run" option, HTTP Content-Length, a Globus ls.
   - Sample and scale: fetch 1 row / limit=1 / one file, measure it, then
     multiply by the expected count (rows, objects, events, files,
     snapshots).
   - Arithmetic when nothing else exists: rows × columns × bytes per value
     (8 for float64/int64, 4 for float32/int32), then × number of files or
     time steps. Compressed formats may shrink this 2-5×; say that it is a
     guess.
   Account for multipliers the user might not think of: every requested
   snapshot / redshift / run, every object's particles, every kernel call's
   artifacts, repeated calls in a loop.

2. EXPLAIN it to the user in a short table before proceeding: what is being
   fetched, from where, to where (local path), estimated size, how the
   estimate was made (metadata / sample-scaled / arithmetic), and a rough
   transfer time (assume ~10-50 MB/s on a typical home or office link
   unless measured). If a shell or coding tool is available, check free disk
   at the destination (df -h) and include it.

3. GATE on size:
   - Small (under ~100 MB): state the estimate in one line and continue.
   - Medium (~100 MB - 1 GB): state it, proceed unless the user objected
     earlier in the conversation.
   - Large (over ~1 GB, or over ~10% of free disk, or unknown size that
     could plausibly be large): STOP and ask before fetching, offering the
     reduced alternatives from step 4.

4. REDUCE at the source first — almost always better than downloading:
   - Select only the needed columns / fields; filter rows server-side (mass
     cuts, sky region, event selection, time range).
   - Aggregate remotely (histograms, summary statistics, binned profiles)
     and fetch the summary instead of the raw rows.
   - Subsample (random fraction, fewer snapshots, a few objects) to develop
     the analysis, then scale up only if needed.
   - If the data already sits at a facility, run the analysis there
     (dispatch) and fetch only results, not inputs.
   - For dispatched jobs: have the kernel write compact outputs; check
     artifact sizes on the facility before fetching all of them back.

5. REPORT after the fetch: actual size and location next to the estimate.
   If the estimate was off by more than ~3×, say so and save the corrected
   per-row / per-file size with the remember tool for next time.

Never silently start a multi-GB download, and never re-download data that
already exists locally from an earlier call; reuse it and say where it is.
