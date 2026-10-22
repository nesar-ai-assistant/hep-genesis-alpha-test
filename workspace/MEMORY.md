# Agent memory

Lessons the agent saves with the `remember` tool are appended here.
- When predicting with the hydro emulator, always state the redshift first.
- run_test_job only supports standard distributions (normal is fixed at mu=0, sigma=1; no mu/sigma args) and returns artifact: null, so its samples cannot be passed to compute_statistics or compute_histogram.
