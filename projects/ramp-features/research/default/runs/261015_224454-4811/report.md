# Estimated number of 2025 arXiv papers on galaxy cluster physics

## Abstract

This is a rough estimate of how many arXiv papers on galaxy cluster physics appeared in 2025. The total number of astro-ph papers and their split by primary category are taken from a published year-in-review of 2025 astro-ph (arXiv:2602.12303). The fraction of papers about clusters is not taken from any source. No source examined gives that fraction as a number, so it is an assumption applied separately to each category.

The base is 18,660 primary-category astro-ph papers in 2025. On that base the estimate is:

- **Strict definition** (clusters are the main subject): about **1,200** papers, range roughly 950–1,550, which is about 5–8% of the total.
- **Broad definition** (clusters are a substantial secondary subject, plus cross-listed papers): about **2,000–3,000** papers.

The quoted values for the base were read from the paper's full text, but the supporting excerpts were not attached as validated citations, so the base is not independently verified. The cluster fraction remains an assumption.

## Background

Two bibliometric sources were identified for astro-ph output in 2025.

**Astrophysics Wrapped 2025 (arXiv:2602.12303).** This is a year-in-review of every astro-ph paper from 2025. Its abstract states the motivation: research output in astrophysics keeps growing year on year. It reports statistics by subfield and by keyword, and includes citation tables. Its breakdowns by keyword and by subfield (the top 25 subfields and research areas) are presented only as figures, not as numerical tables.

**AstroMLab 5 (arXiv:2511.12353).** This is a dataset of 408,590 astro-ph papers from 1992 through July 2025. Each paper has structured summaries and extracted concepts, and the code and data are public at github.com/tingyuansen/astro-ph_knowledge_graph. In principle, its concept tags could give a cluster fraction for January–July 2025.

**Scope example (arXiv:2311.06338).** The TNG-Cluster simulation paper was used only to illustrate the subject area: cluster simulations and the intracluster medium.

**Earlier unverified total.** The initial survey suggested an astro-ph total of about 18,000–21,000. That range came from an unverified web snippet about the Open Journal of Astrophysics, which reportedly published 213 papers in 2025, "just over 1%" of astro-ph submissions. Web-only numbers cannot be cited, so this snippet was used only as a sanity check.

## Results

### Total astro-ph output in 2025

Section 2.1 of arXiv:2602.12303 reports 18,660 papers uploaded to astro-ph in 2025. According to the text read during the run, this count excludes both replacement submissions and cross-submissions, so it covers primary-category papers only.

The critic noted that the excerpts recorded as evidence do not contain the 18,660 figure or the sentence about excluding cross-submissions. The value should therefore be treated as read from the full text but not independently verified. Whether cross-lists from gr-qc, hep-ph and physics are excluded is still formally an open question. That matters because including cross-lists could change the base by roughly 20–30%.

The 18,660 figure sits at the low end of the survey's unverified 18,000–21,000 range. That is consistent with a count that excludes cross-lists.

### Split by primary category

Table 1 of arXiv:2602.12303 gives the following 2025 counts by primary subject. The same caveat applies: the table was read, but not captured in a cited excerpt.

| Category | Papers |
|---|---|
| astro-ph.GA | 4,761 |
| astro-ph.HE | 3,869 |
| astro-ph.SR | 2,958 |
| astro-ph.CO | 2,789 |
| astro-ph.EP | 2,293 |
| astro-ph.IM | 1,722 |
| astro-ph (general) | 268 |

The categories where cluster papers mostly appear account for the following shares of the total:

- GA plus CO: 7,550 papers (40.5%).
- GA plus CO plus HE: 11,419 papers (61.2%).

### Attempts to measure the cluster fraction directly

None of the attempts produced a number.

- **arXiv:2602.12303.** The text names only the leading keywords: accretion, galaxy evolution, AGN, exoplanets, star formation and cosmology. Its keyword figure (Fig. 12) and top-25 subfield figure (Fig. 13) were extracted to the run directory (`/Users/nramachandra/hep-genesis-testing/projects/ramp-features/runs/261015_224454/figures_2602.12303/`). Neither image was read numerically.
- **arXiv:2511.12353.** The paper gives example concepts (for example, CMB with 9,166 papers) and aggregates over 1992 to July 2025. It gives no counts by year and no cluster concept. Its ADS keyword table lists "galaxies: evolution" at 5.5% and "dark matter" at 3.0%, but has no row for clusters.
- **Abstract searches.** Searches of arXiv abstracts return ranked subsets, not hit counts, so they cannot support any count. They did show that keyword searches pick up star clusters alongside galaxy clusters. Any future keyword count must therefore exclude star, globular and open clusters.

### Per-category estimate (cluster fraction assumed)

The following fractions are assumptions, not values from any source.

| Category | Assumed cluster fraction | Estimated papers |
|---|---|---|
| astro-ph.CO | 15–25% | about 420–700 |
| astro-ph.GA | 8–12% | about 380–570 |
| astro-ph.HE | 3–5% | about 120–190 |
| Other categories | — | about 30–80 |

The totals are:

- **Strict definition: about 950–1,550 papers, central value about 1,200.** That is about 6.5% of 18,660.
- **Broad definition: about 2,000–3,000 papers.** This adds group-scale work, simulations that include cluster analyses, high-energy work that uses clusters as targets, and gr-qc/hep-ph papers cross-listed into astro-ph. The critic pointed out that this range has no explicit derivation. It also combines a primary-only base with a cross-list contribution that was never quantified.

## Discussion

Fixing the base at 18,660 primary-category papers, rather than the survey's 18,000–21,000, pulls the strict central estimate down from the survey's 1,500 to about 1,200. The figure of 1,500 is not ruled out, but it sits at the top of the strict range.

Splitting the estimate by category is more transparent than applying one flat fraction. It does not make the estimate better supported. The resulting overall share of 5–8% is essentially the survey's original assumption, now spread across categories.

For comparison, "galaxies: evolution" accounts for 5.5% of keywords in AstroMLab 5. That makes a cluster share of a few percent plausible in order of magnitude, but it does not measure the cluster share.

The survey also argued that 2025 should be a high-output year for cluster science because of eROSITA, Euclid, ACT/SPT, LOFAR, XRISM and JWST protocluster work. That argument was not tested. The planned check of the 2020–2024 trend was not carried out.

The main dead end was trying to get a numerical cluster share from the two bibliometric papers. Both papers present the relevant breakdowns only as figures, or not at all.

## Limitations

- **One wave of tool calls.** The run stopped after a single wave because the budget ran out.
- **Base not validated as citations.** No `cite()` calls were made, so the 18,660 total and the Table 1 counts are recorded but not validated in references.bib.
- **Cross-list question open.** Whether the 2025 total excludes cross-lists is still formally unresolved.
- **Figures not read.** Figs. 12–13 of arXiv:2602.12303 were extracted but not read numerically.
- **No direct count.** No ADS or arXiv API facet count was available, so the cluster share and the final numbers are model-based.
- **Cross-check not started.** The independent cross-check using AstroMLab 5, which would also cover the 2020–2024 trend, produced nothing.
- **Partial-year data.** Scaling the AstroMLab January–July data to a full year would need at least a ±10% allowance for uneven submission rates across the year.
- **Borderline topics.** How to treat galaxy groups, cluster-scale simulations, and searches that use clusters only as targets is still unresolved.

## Open directions

1. Run the ADS query abs:("galaxy cluster" OR "clusters of galaxies" OR intracluster) year:2025 collection:astronomy, excluding star clusters, to replace the assumed 5–8% share with a measured one.
2. Read the values in Figs. 12–13 of arXiv:2602.12303 numerically, looking for a galaxy-cluster keyword or subfield bar.
3. Re-read the relevant parts of arXiv:2602.12303 and pass them to `cite()`, so that the 18,660 total, the exclusion of cross-submissions and the Table 1 counts are validated.
4. Derive a cluster concept share and a 2020–2025 trend from the public AstroMLab 5 concept data as an independent cross-check, scaling January–July to the full year with a stated allowance.
5. Measure the cross-list contribution from gr-qc and hep-ph to give the broad 2,000–3,000 estimate an explicit derivation.
