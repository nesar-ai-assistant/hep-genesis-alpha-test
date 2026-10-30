---
name: literature-research
description: Literature-grounded research on any physics topic: search strategy, reading discipline, citations, and published figures
---

Use this whenever published results matter — collider physics, neutrinos,
astroparticle, nuclear, cosmology alike. The method is identical in every
sub-field; do not reserve it for topics that look "researchy". A detector
explainer needs citations exactly as much as a cosmology analysis.

SEARCH:
- Query with 2-3 short keyword phrases, not full sentences — long phrase
  queries return junk (sometimes the SAME irrelevant paper for every
  variation; that is the search failing, not the literature missing).
- If the canonical paper is already known, skip search and go straight to
  its arXiv ID — the download/read tools take IDs directly.
- Nothing after 2-3 distinct keyword sets: say so and move on; do not
  keep permuting queries.

READ:
- Read papers in targeted sections (abstract, the relevant section, the
  figure captions) and distill findings into brief notes IMMEDIATELY.
  Never hold multiple full paper texts in context — full-text dumps have
  crashed real runs by overflowing the model's context window.

CITE:
- Every claim taken from a paper carries its arXiv ID or DOI. Uncited
  "well-known facts" are where wrong attributions slip in.

PUBLISHED FIGURES:
- Show a figure only with its caption and citation. Address figures by
  the PAPER's own numbering (the extractor reports it — trust that over
  file order). Extraction fails for many older / PDF-only papers; report
  that honestly — the fallback is downloading the PDF and extracting
  pages with a coding task.
- If the user names a figure you cannot resolve after ~2 lookups, ask one
  clarifying question instead of guessing across papers — and complete
  the unambiguous parts of the request meanwhile.

CLOSE THE LOOP: when compute tools can reproduce a published curve or
number, do it and compare — state explicitly what was and was not
reproduced, and why.
