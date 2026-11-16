# work-r2 — 2026-11-16-lec12-fairness-clarity

## Branch and commits
- Branch `2026-11-16-lec12-fairness-clarity`; round-1 head `f6c0205`. The round-2 head is the commit containing this file; its SHA is in the pointer.
- Round 2 changes only F01–F07 plus one preference, as listed below. No slide was added, removed or moved, and timing is unchanged.

## Findings
| ID | slide | done |
|---|---|---|
| F01 | S79 note | Message replaced with the review's text: "Each rate specifies whom we count and which outcome we count within that population. Group A gives selection 4/10, TPR 3/6, FPR 1/4 and precision 3/4." |
| F02 | S80 note | Paragraph replaced with the review's text. It says the three rules can hold together, and that Section 03 treats equal PPV with equal FPR and FNR. |
| F03 | S76 note | The calibrated equalized-odds sentence was replaced with the review's text: random replacement by the group base rate, a relaxed constraint on scores, and no general guarantee of equal thresholded FPR and FNR. Added the Pleiss et al., NeurIPS 2017 primary source (arXiv 1709.02012v2): §3 Definition 1; §4, Eq. (3), Algorithm 1. The main slide is unchanged. |
| F04 | S49a note | Message clause replaced with the review's text: "Picking either man goes beyond the supplied evidence; systematic stereotype-aligned choices are what the benchmark tests." |
| F05 | S50a note | Last Boundaries sentence replaced with the review's text: zero can mean balanced answers, or no non-Unknown answers in the ambiguous condition, and zero bias alone does not establish accuracy. |
| F06 | S44b main | The subtitle now names the axis: "Each point follows one method, not all nine. y: **balanced accuracy**." The key reads "balanced accuracy ≈0.745 both". Figure size and type are unchanged. |
| F07 | S38 note | The five-column weight table is now four stacked list records. Each record keeps expected share, observed share, exact weight and weighted count. The exact-2/3 sentence is kept. |

## Additional change
- **Narrow-width fix.** At a true 430 px viewport, two long `<code>` file names in the S47 and S48 notes also pushed the page to 437 px wide. Both were found by the check below. Added `.detail code { overflow-wrap: anywhere; }` to the note's own style block. This changes no content and does not reduce any font size.
- **Preference taken.** In the S41a note, "roughly one point" now reads "roughly one percentage point".

## Checks
- `lint-deck.py`: the deck has 0 errors and no font-size warnings. The same 30 hardcoded-color occurrences remain, as in the baseline. The note passes with `ok`.
- `outline-lint.py`: 0 stale pointers on this filesystem. No deck line counts changed, so no OUTLINE edit was needed.
- Render check: S44b at `-r 60` (page 72) is clean. The title is on one line, the subtitle fits, and the key and citation are clear. Its neighbours S44a (page 71) and S45 (page 73) are unchanged, and pages 71–73 were rendered in the same pass.
- Note narrow-width check: the note was loaded in a 430 px iframe, which gives a true 430 px viewport (415 px content width with the scrollbar). Every element inside an article was checked for its right edge, excluding hidden KaTeX MathML. Before the fix it found S47 and S48 `<code>` at 437 px; S38 was already fixed by F07. After the fix the document scroll width equals the client width (415) and no element overflows.
- Living files (`job.md`, `requests.md`, `evidence.md`) were refreshed, and `review-r1.md` was copied unchanged.
