# review-r1 — 2026-11-10-prob07-remove-gan

reviewed commit: a825c1ed76945e1f2cc6f121eb6e5996b2b9a5a7
content commit: 61a2337da9be32ee0f9852865643fd35e3d69a66
id commit: 9f2273b425192bef87a90bb66f25a3de17b93187 (main deck only)
verdict: revise

## Result

The requested removal is complete and the rendered slides are sound. One small blocking metadata correction remains: the updated section-table Location links still point to blank lines/comments rather than the section slide starts. Fix only F01; no slide redesign or further content change is requested.

## Coverage

| Comment | Status | Verification |
|---|---|---|
| C01 | done | Exactly S128–S134 deleted; S02/S118/S120/S135 no longer name GAN; both companions lose §§11.4–11.6 and GAN-only references; scorecard retained with two families; current prob07 outline no longer advertises GAN/JS. |

The LLM/diffusion discussion and the Gaussian bridge are worth preserving as delivered. The two-card page is balanced; do not pad its whitespace.

## Findings

| ID | Slide ID / page | Type | Blocking | What is wrong | Concrete fix |
|---|---|---|---|---|---|
| F01 | Section dividers S03/S07/S15/S20/S27/S39/S57/S75/S92/S107/S118, pp3/7/15/20/27/39/57/75/92/107/118 | design rule | yes | The final Location column at `courses/deepmath/OUTLINE.md:387–397` lands on blank lines for sections 01–10 and a comment for 11. Preserving the baseline's bad offsets is not the DS §10 acceptance check. | Apply numbered request 1 below; do not change inline descriptive pointers or deck content. |
| F02 | Companion correspondence for S01–S137; all pages | design rule | no, pre-existing structure | `courses/deepmath/prob07-estimation/prob07-estimation-note.html` has chapter sections rather than per-slide articles; no matching articles exist to receive slide IDs. The deck-only ID commit must not be represented as full per-slide note-ID coverage. | Retain honest deck-only reporting for this job. Use the existing note subsection locators for this review. Creating one article per slide with matching IDs is a separate, explicitly scoped note-structure migration, not an incidental deletion edit. |

### 1. F01 — Correct the section table's final Location column

File: `courses/deepmath/OUTLINE.md`. Lines refer to reviewed commit a825c1e. Each replacement is the final `prob07-estimation/prob07-estimation.html:<line>` link on the specified row; leave other text on that row unchanged.

| OUTLINE line | Section / stable ID / page | Current final line → new final line |
|---|---|---|
| 387 | 01 / S03 / p3 | 153 → 155 |
| 388 | 02 / S07 / p7 | 213 → 215 |
| 389 | 03 / S15 / p15 | 361 → 363 |
| 390 | 04 / S20 / p20 | 443 → 445 |
| 391 | 05 / S27 / p27 | 548 → 550 |
| 392 | 06 / S39 / p39 | 732 → 734 |
| 393 | 07 / S57 / p57 | 990 → 992 |
| 394 | 08 / S75 / p75 | 1279 → 1281 |
| 395 | 09 / S92 / p92 | 1603 → 1605 |
| 396 | 10 / S107 / p107 | 1852 → 1854 |
| 397 | 11 / S118 / p118 | 2019 → 2020 |

Reason: DS §10 requires Location to be the section's first slide opening element, not an adjacent blank/comment. These replacement lines were checked against the exact reviewed source. Title and bridge Location entries are already correct.

## Checks independently performed

- Read Albert's C01 first, then baseline evidence and the deletion boundaries; checked applicable design rules before comparing plan compliance.
- Verified ID-only commit by stripping the added attributes: the original deck is byte-for-byte restored. Verified current ID sequence: exactly seven retired IDs, 130 remaining slides, no renumbering.
- Compared individual retained slide bodies: only S02, S118, S120 and S135 differ. Other retained slide bodies are identical to the ID-only baseline.
- Read both companion diffs. Note text before section 11 is unchanged; §§11.2–11.3 are exactly preserved in both formats. Reviewed the two-family scorecard, reference removals and remaining numbering.
- Independent whole-source search in deck and both companions found no GAN/JS/StyleGAN/Goodfellow/FFHQ/discriminator teaching remnants. Jensen's inequality remains in both diffusion notes; ordinary KL/CE and the discrete-data qualification remain.
- Diffusion path-likelihood versus generally-not-image-likelihood and reweighted simple-loss qualifications remain; CE-SFT/RLHF distinction remains. No new scientific result or numerical claim introduced, so no fresh literature survey was needed.
- Extracted a825c1e through git archive, not a working tree. Ran pinned `lint-deck.py`: ok. Rendered with Chromium: PDF is 130 pages, 1280×720 slide equivalent. Visually inspected pp1–3,117–121,126–130 at that resolution. No clipping, overlap, footer collision or type reduction found on these pages. The removed-block seam reads coherently.
- Inspected changed outline fields and section-start locations, discovering F01. Executor's global outline-lint result is reported in work-r1; not independently repeated across unrelated decks.
- Refreshed ignored standalone outputs were executor-reported; independent rendering here uses pinned source and pinned reference assets instead.
- This is a bounded deletion review, not certification that every inherited slide complies with all newer prose/style rules.

## Plan issue resolution

No new content plan is needed. The request to report a faithful-note-mapping obstacle was followed. There are no matching per-slide note articles in the baseline; requiring a whole-note restructure would broaden Albert's deletion job. Keep its existing chapter organization and record the pre-existing limitation as F02. The matching-article ID rule remains in force wherever matching articles exist; no standing instruction or pipeline document is being changed.

S120's alternate title is acceptable [judgment]: it retains the familiar-example framing rather than making an exhaustive taxonomy claim. Removing the orphan `.p7-red` rule is harmless; shared styling was untouched.

## Round 2 handoff

Only F01 needs action. Do not re-render unchanged slides. Return `work-r2.md` and an exact commit; the next pass will inspect the outline-only correction and confirm that the content stays unchanged. This is round 2 of 2. Copy this review unchanged and refresh living job files at the next push. No merge authorization.
