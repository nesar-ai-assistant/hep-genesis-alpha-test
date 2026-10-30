---
name: trustworthy-analysis
description: Integrity rules for quantitative results: provenance for every number, sanity anchors, and what never to fabricate
---

Load this before presenting quantitative scientific results. Every rule
here has been violated in a real run.

NEVER FABRICATE:
- Never present numbers as the output of code that did not run ("verified
  output", "running this gives…"). If there is no execution tool, label
  every number as hand-computed.
- Never claim a computation ran on a facility without proof in the tool
  result (computed_on / a job id). Never pass one dataset off as another
  (a model curve is not "observed data"); a locally recomputed stand-in
  for a remote result must be labeled as such.
- Before declaring a capability missing, re-read the tool catalog (real
  runs have denied a capability one turn before using it). If it truly is
  missing, say so within ~3 attempts instead of burning the tool budget
  on workarounds that cannot succeed.

PROVENANCE:
- Every curve and headline number must be traceable: which tool, which
  arguments (and seed), where it ran, which local file holds it. Pass a
  distinct label per model when comparing.
- Keep ONE canonical results file per analysis and quote numbers only
  from it — re-deriving metrics in different turns is how reported
  numbers drift within a single conversation.

SANITY CHECKS:
- Anchor first: reproduce a known published value or count with the same
  pipeline before making novel claims, and cite the anchor.
- Check units and magnitudes explicitly (unit system, h factors, comoving
  vs physical, per-GeV vs per-bin) — state the convention on plots.
- An extremum at the edge of a tool's validity range is a boundary
  artifact, not a physical feature; quote validity ranges with results.
- Be skeptical of dramatic improvements measured on tiny samples — report
  the sample size next to the claim.

FAILURES:
- Distinguish infrastructure failures (LLM gateway 4xx, model offline,
  budget exceeded, schema rejections) from scientific ones — report them
  as environment problems, never as "the analysis found nothing".
- When the user's request is internally inconsistent (counts, numbering),
  state your interpretation explicitly rather than silently choosing.
