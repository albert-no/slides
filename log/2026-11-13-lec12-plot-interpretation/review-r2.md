# Review r2 — 2026-11-13-lec12-plot-interpretation

reviewed commit: 5d0e8832dd15bb41649eacf9604579f75aa8d0da
baseline: 0d2c05c9ad02635c0407010f15bcca5428bac949
previous reviewed commit: d9de699ea36020761939ddf25c16c4c3ea112781
verdict: approved
round: 2 of 2

## Main result

All blocking findings are closed. The three COMPAS plots now have readable axes, highlighted comparisons, and distinct denominators; the FICO explanation correctly limits its randomization claim to the illustrated profit optimum. Both opening visual examples are present and honestly labeled. Keep these distinctions and the explicit approximate-reading/uncertainty qualifications.

Approval is pinned to the commit above. This is approval to open the PR after the record/push gate, not permission to merge.

## Request coverage

| Comment | Result | Final pages / IDs |
|---|---|---|
| C01 | Slide revision done and approved; PR creation remains pending the final tracked-record push | whole job |
| C02 | Done: separate parity and error-rate readings, clear axis/segment interpretation and scoped takeaway | 30–31, S21a/b; baseline p28 |
| C03 | Done: split into score/decision/outcome context and the audit's scores-5–10 flag, with vendor-label distinction | 33–34, S23a/b; baseline p30 |
| C04 | Done: larger essential plot labels, focal comparisons and separate non-rearrested / exact-decile / above-cutoff denominators | 36–38, S25/S26a/S26b; baseline pp32–34 |
| C05 | Done: group-photo thought experiment and an actual published CEO-generation example, not a claimed fresh run | 4–5, S77/S78 |

## Findings disposition

Paths refer to `courses/trustworthy-ai/lec12-fairness.html` and its matching `lec12-fairness-note.html`. No new blocking findings or further slide edits requested.

| ID | Slide ID / page | Type | Blocking now | Resolution |
|---|---|---|---|---|
| F01 | S78 / p5 | unmet request | no — closed | Source CEO image added with exact historical prompt, CEO expansion, DALL-E 3 attribution, published/not-new qualifier and single-image limitation. Note records provenance and selection status. |
| F02 | S21b / p31 | fact | no — closed | Title/highlight specify the profit-optimal rule here. Acceptance probability is “not necessarily 50/50”; note explicitly contrasts feasibility with optimality using the always-reject counterexample. |
| F03 | S25/S26a/S26b / pp36–38 | design rule | no — closed | Native-source plot-panel crops retain bars and intervals; essential ticks and axis titles are enlarged outside the image. Independently rendered labels, focal outlines and keys are readable. FPR, exact-decile rearrest share and cutoff PPV remain distinct. |
| F04 | S21a/S21b / pp30–31 | design rule | no — closed | Row annotations compressed, prose-spacing override removed, body type preserved. Rendered prose/key lines fit the ceiling without crowding or clipping. |
| F05 | S77 / p4 | preference | no — closed | Short legible slide credit replaces missing-glyph attribution; full original credit remains in the note. |

## Independent checks

- Reviewed the exact commit through git, using the original requests and verified primary sources before design/plan checks. Round 2 is restricted to changed slides, integration and neighbours; previously accepted S23a/b content is unchanged.
- Archived the commit into scratch and rendered independently with Chromium: 80 pages, 960×540 pt (1280×720 equivalent). Inspected pp3–6, 29–32 and 35–39 individually. No clipping, overlaps, bad wraps or footer collisions found on these pages.
- Independently reproduced all three new Chouldechova crops from the verified v1 PDF using the reported commands. All three are byte-identical to the committed PNGs. External labels correspond to the source bins/scales; focal values remain explicitly approximate. No data were redrawn from those values.
- S78 JPEG is byte-identical to the reviewer's independently extracted Figure 1 CEO image: SHA-1 `48f276f9c86647a27cb5d580b49b7ed77be4d1ad`. Its prompt, model, panel and selection-status descriptions agree with E14. No fresh generation or bias-rate result is implied.
- Main/notes: 80 unique IDs in identical order, sequential numeric note headings, all local slide assets present. Pacing independently sums to 90 minutes; all 80 elapsed values agree. Section budgets remain 10/20/15/20/15/10. Technical supplement unchanged from baseline.
- Numeric note references checked after the insertion. OUTLINE changes are lec12-only; counts, section ranges and relevant pointers agree with the deck.
- Main lint retains the same pre-existing 30 hard-coded-color warning; note lint passes. Independent outline lint retains the unrelated lec09 absolute workspace-script pointer error at line 326 and five pre-existing ambiguity warnings. No unrelated repair is requested.

## Plan issues and handoff

Plan-v3 resolves the unavailable-generation route and the owner's earlier randomization wording. No further plan changes or open scope decisions remain. The final deck is 80 slides versus baseline 76; the 90-minute teaching budget is unchanged.

Slides: copy this review unchanged into `log/2026-11-13-lec12-plot-interpretation/`, refresh the living job/request/evidence files, and push. Any commits after the approved commit must touch only that tracked job folder. Send the exact pushed SHA so slides-review can verify the record-only tail and open the PR against main. Do not change deck content under this approval and do not merge.
