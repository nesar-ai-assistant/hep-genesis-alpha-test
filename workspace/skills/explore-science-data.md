---
name: explore-science-data
description: First contact with an unfamiliar dataset or science server: discover before querying, validate parameters from schemas, inspect big files before analyzing
---

Use this when working with a dataset, catalog, or science MCP server you
have not used in this conversation before — simulation catalogs, event
samples, survey data, and emulators alike.

DISCOVER BEFORE YOU QUERY:
1. Enumerate what the server offers first: its documentation / list /
   describe tools (get_documentation_*, list_*, describe_*), before the
   first real query.
2. Parameter values (simulation names, snapshot steps, dataset ids, model
   enums) come ONLY from the tool schema or a discovery tool — never from
   memory of similar datasets, and never echo the user's spelling into an
   enum argument (fix typos against the schema). A guessed identifier is
   the #1 cause of "Invalid arguments" rejections.
3. Start small: fetch 1 row / limit=1 / one file before the full query,
   and confirm the output shape matches what you assumed.

SUBMITTED RUNS (submit → poll → results):
- Check what is already running (list_runs or equivalent) BEFORE
  submitting; servers commonly cap concurrent runs — submit in waves that
  fit the cap, and never resubmit a quota-rejected call while the queue
  is full.
- Batch: when a tool accepts a list (of ids, tags, objects), one call
  with N items beats N calls — each call may be a separate queued job.
- Poll the status tool patiently; queued/running is progress, not failure.

BIG OUTPUT FILES (HDF5 / parquet / FITS / ROOT):
- Previews and summary plots are NOT the data — column names, ids, and
  rows are usually absent from them. To see real structure, read the
  server's dataset documentation, or download the file and inspect it
  locally (a coding task with h5py/pyarrow/uproot: list groups, datasets,
  columns, and shapes FIRST).
- Never assume a layout (per-object groups vs one flat table); verify,
  then analyze. Identify which key joins the tables (an object/event id)
  before writing analysis code.

PERSIST WHAT YOU LEARN: when you discover a dataset's layout, valid
parameter values, a server quirk, or a bug plus its workaround, save it
with the remember tool immediately — one line each. The next session
starts from what this one learned.
