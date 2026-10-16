# Estimating the number of 2025 arXiv papers on galaxy cluster physics

## Abstract

No published count of 2025 arXiv papers on galaxy cluster physics was found, and no direct database query was run. The number of papers in the field as a whole is well sourced: arXiv:2602.12303 reports 18,660 astro-ph papers in 2025. That figure counts primary submissions only and excludes replacements and cross-lists. The same paper reports 16,333 for 2024, so output grew by 14.2%. The share of those papers that concern galaxy clusters is not sourced and had to be assumed.

Applying assumed within-category fractions to the sourced per-category counts gives about 640 papers under a strict definition (3.4% of the total) and about 1,110 under a broad definition (5.9%). Because every fraction is assumed, the honest headline is **roughly 1,000 galaxy-cluster papers in 2025, with a plausible range of about 600 to 1,500**. This is a model-based estimate with low confidence, not a measurement.

## Background

The survey turned up two relevant sources.

**Astrophysics Wrapped 2025 (arXiv:2602.12303).** Lewis, Shah and Alfred compile statistics on every paper submitted to astro-ph in 2025. These include primary-subject counts, the most common keywords, subfields and research areas, and the leading institutes. It is the natural source for the 2025 total and possibly for the frequency of cluster topics.

**AstroMLab 5 (arXiv:2511.12353).** This dataset covers 408,590 astro-ph papers from 1992 through July 2025. It provides structured summaries and a vocabulary of about 10,000 extracted concepts. In principle, the concept tags could be used to measure what fraction of papers concern clusters.

**Earlier rough estimate.** Before this work, the base was estimated from a web-only blog statement. The statement said the Open Journal of Astrophysics published 213 papers in 2025, which was "only just over 1%" of astro-ph. That implies about 19,000 astro-ph papers. The cluster share was assumed to be 4–6% under a broad definition, giving about 750–1,150 papers, or about 1,000 after rounding. The blog figure is not citable on its own.

## Results

### The 2025 astro-ph base count

The base count is the well-sourced part of the estimate. Section 2.1 of arXiv:2602.12303 gives 18,660 astro-ph papers for 2025. The paper excludes replacements and cross-submissions in order to confine the dataset to "pure Astrophysics papers". The base is therefore primary submissions only. The paper gives no total that includes cross-lists, so that number is not available.

Section 3.1 gives 16,333 papers for 2024. The ratio 18,660/16,333 = 1.142 means growth of +14.2% from 2024 to 2025.

Table 1 gives primary-subject counts for 2025:

| Primary subject | Papers |
|---|---|
| astro-ph.GA (galaxies) | 4,761 |
| astro-ph.HE (high energy) | 3,869 |
| astro-ph.SR (solar and stellar) | 2,958 |
| astro-ph.CO (cosmology) | 2,789 |
| astro-ph.EP (earth and planetary) | 2,293 |
| astro-ph.IM (instrumentation and methods) | 1,722 |
| general astro-ph | 268 |

In addition, 8,684 papers carry a secondary subject.

The sourced total of 18,660 is consistent with the earlier web-derived figure of about 19,000. Their agreement supports the base, but the web figure itself is not cited.

One caveat applies. The stored text excerpts used to validate these numbers were truncated, and the exact sentences containing 18,660, 16,333 and the Table 1 values were not reproduced in full. The character ranges read and the successful citation are consistent with these values, but a final write-up should quote the exact sentences.

### Keyword and subfield evidence from Astrophysics Wrapped 2025

Figure 12 ("Most Common Keywords for 2025") and Figure 13 ("Top 25 sub-fields and research areas") were extracted as images. No tool returned bar values from them, so neither a galaxy-cluster bar value nor a smallest-bar bound could be read. The text gives three pieces of evidence:

- **Top author keywords.** "Galaxy Clusters" is not among the top 25 author-assigned keywords of 2025 (Table 8). The last entry on that list is "High Energy Astrophysics".
- **Top subfields.** It is not among the top-10 subfields named in the text. The top four are Observations, Simulations, Star Formation and Dark Matter.
- **Institute keywords.** "Galaxy Clusters" does exist in the paper's keyword taxonomy. Table 7 lists it as the top keyword of the Chinese Academy of Sciences, which has 7,837 institute-paper contributions. Cluster papers could therefore have appeared on the overall list.

These facts have limited quantitative value. Absence from the top 25 bounds only how often the literal keyword string "Galaxy Clusters" appears. It does not bound the share of cluster-topic papers, because cluster work is spread across terms such as ICM, SZ and cluster lensing. The Table 7 entry counts institute-paper contributions for a single institute. It is not a paper count and cannot serve as a lower bound for the field.

### AstroMLab 5 concept data

The text of arXiv:2511.12353 gives no per-year paper totals and no concept count for galaxy clusters, the ICM or the SZ effect. The only counts quoted are examples:

- ADS keyword "galaxies: evolution": 16,321 papers (5.5%).
- Concept "Gravitational Lensing Surveys": 278 papers.

An all-years cluster share therefore cannot be derived from the paper text. It would require the public concept CSV in the project's GitHub repository, which was not accessed.

### Synthesis estimate

The per-category counts come from Table 1. The fraction of each category assumed to concern galaxy clusters is an assumption, not a measurement.

- **Strict definition** (ICM and cluster physics, cluster cosmology): 0.12×2,789 (CO) + 0.04×4,761 (GA) + 0.03×3,869 (HE) = 335 + 190 + 116 = **641 papers**, which is 3.4% of 18,660. Stated range: 443–811.
- **Broad definition** (adding cluster galaxy evolution, protoclusters, lensing and instrumentation): 0.18×2,789 + 0.08×4,761 + 0.05×3,869 + 0.02×1,722 = 502 + 381 + 193 + 34 = **1,110 papers**, which is 5.9% of 18,660. Stated range: 848–1,413.

The arithmetic was checked independently. The broad share of 5.9% falls inside the 4–6% assumed in the brief, but it does not test that assumption, because both rest on assumed fractions. The ranges quoted above have no documented derivation.

The strict definition leaves out cluster instrumentation and SZ-survey papers whose primary category is astro-ph.IM. That is a definitional choice. Papers cross-listed into astro-ph from gr-qc or hep-ph are excluded from the base, and their contribution to the broad count is not quantified.

### Trend

No per-year data for cluster papers was found, so the trend in cluster output cannot be measured. The only sourced growth figure is for the field as a whole: +14.2% from 2024 to 2025. If the cluster share stayed constant (an assumption), 2024 would have had about 561 strict and about 972 broad cluster papers.

## Discussion

The total number of astro-ph papers is now a cited quantity, and it agrees with the earlier web-derived figure. The galaxy-cluster share is still the dominant source of uncertainty. Every within-category fraction used here is a judgement call. The resulting 3.4% strict and 5.9% broad shares only reproduce the range assumed at the outset, so the central answer is unchanged from the first rough estimate: about 1,000 papers. What has improved is the base. It is now sourced, it is known to exclude cross-lists, and the per-category numbers come from Table 1.

The keyword evidence is consistent with a cluster share of a few percent, but it does not constrain that share numerically. "Galaxy Clusters" is a valid keyword in the taxonomy, yet it does not reach the 2025 top 25. That is what one would expect if cluster work is a moderate niche whose papers are tagged under several related keywords. However, it bounds only that single keyword, not the topic.

Several attempts to measure the share failed:

- **Astrophysics Wrapped 2025.** Its text does not tabulate the bar values of Figures 12 and 13.
- **AstroMLab 5.** It quotes only example concepts, with no cluster, ICM or SZ concept and no per-year totals.
- **Literature searches.** Two arXiv abstract searches for bibliometric analyses of cluster publication fractions returned only irrelevant papers.

A measured share needs one of three things: the AstroMLab concept CSV, an ADS or arXiv API count, or a visual reading of Figure 12b.

## Limitations

- **No direct count.** No direct database query was run. The arXiv API count in the brief and the ADS query were both left undone, so there is no direct hit count. Without one, false positives from "star cluster", "globular cluster" and "clustering" could not be screened.
- **Figures not read.** The figure images were extracted but not read. Any value read from them in future would be approximate, roughly plus or minus one axis tick, and could not be cited as a verbatim quote.
- **Cross-lists not counted.** The base excludes cross-lists, and no source bounds their contribution.
- **No trend data.** No per-year cluster data exists in the sources consulted, so the trend question is open.
- **Partial-year data.** The AstroMLab data ends in July 2025. Even with the concept CSV, scaling a part-year share to the full year, or applying an all-years share to 2025, would be a proxy rather than a measurement.
- **Budget.** The run stopped when its wave budget was used, before any of these gaps could be closed.

## Open directions

1. Replace the assumed cluster share with a measured one by running the ADS query abs:("galaxy cluster" OR "clusters of galaxies" OR intracluster) year:2025 collection:astronomy, excluding star clusters, or by tallying cluster concepts in the AstroMLab 5 concept CSV.
2. Visually read the Galaxy Clusters bar, or the smallest-bar value, from Figures 12b and 13 of arXiv:2602.12303, and label the result as figure-read and approximate.
3. Quote the exact sentences in arXiv:2602.12303 that give 18,660, 16,333 and the Table 1 counts, so the base no longer rests on truncated excerpts.
4. Run the same cluster query for 2023 and 2024 as an independent cross-check, to test whether cluster output grew in line with the 14.2% rise in total papers.
5. Quantify the gr-qc and hep-ph cross-list contribution to the broad count, which is currently excluded from the primary-only base.
