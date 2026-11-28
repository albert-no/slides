# work-r3 — 2026-11-27-lec14-focused-overview

- **Branch:** `2026-11-27-lec14-focused-overview`. The r2 head was `c16c37a`. This round's head is the commit named in the pointer.
- **Scope:** review-r2 F09 and F10, and plan-v5. Nothing else changed:
  - main deck: 59 slides (`1 / 59`), 85 + 5 min;
  - S69b stays at 2.25 min, as plan-v5 item 1 says;
  - backup deck: 52 slides (`1 / 52`);
  - slide IDs, order, figures and the tech deck are unchanged.
- **Commit contents:** besides the fixes, the commit adds unchanged copies of `review-r2.md` and `plan-v5.md`, and refreshed copies of `job.md`, `requests.md` and `evidence.md` (which includes E26).

## Finding dispositions

| ID | Disposition | What changed |
|---|---|---|
| F09 | Fixed | I rebuilt `courses/trustworthy-ai/OUTLINE.md` from the exact r1 file (`1d44931`) and re-applied only the lec14 changes. See the structural check below. |
| F10 | Fixed | The S75b diagram label "all its outputs kept" now reads **"without extra filtering"**. The S75b alt text and the note's Message use the same route-neutral wording. In the Script, "Nothing is filtered: the teacher is aligned, so all of its outputs are kept" is replaced verbatim with the sentence from review-r2. "All three training routes we have seen" now reads "all three training routes tested in the paper". In `p2b-PROVENANCE.md`, "all outputs kept" now reads "training trajectories retained without additional filtering". No values, models, pacing or other diagram text changed. |

### F09: what went wrong and what was re-applied

In r2, my edit to the backup section matched from the backup table row in the "Backup / swap-in" list down to the `## backup-lec14-agentic-threats.html` section. It replaced that whole span, which deleted r1 lines 97–756. That span included the main lec14 section, so the main-deck pointer updates I reported in r2 were also missing from the committed file.

r3 is the r1 file with only these changes:

1. **Lecture index row 14 and the slide-ID paragraph.** These are the two small r2 changes, kept as they were in r2.
2. **Backup / swap-in table row.** Only "(47 sl" became "(52 sl incl. B6 More on Hidden Transfer". The row ends as in r1, and the `## backup-lec14-agentic-threats.html` cross-reference is intact.
3. **`## lec14-agentic-threats.html`:**
   - "plan-v3" became "plan-v3 amended by plan-v4".
   - Every line pointer was remapped mechanically: I matched each r1 pointer's source line in the r1 deck to the identical line in the r3 deck. Only `p2a-cloud-fig3a.png :872` changed by hand, to the new `p2a-cloud-fig3a-left.png :873`.
   - The row label "Cloud Fig. 3a misalignment" became "Fig. 3a left subplot, misalignment".
   - "conditional mitigation" became "aligned-teacher recovery".
   - In the citations, Askin gains Figs. 5 and 25. The Yanagisawa citation and the "evidence map" citations are replaced by "the further hidden-transfer preprints moved to backup B6".
4. **`## backup-lec14-agentic-threats.html`:** the heading is kept. The body is the r2 B6 / 52-slide update: topic text, the section table with B6 and End, and the B6 figures and citations. In r2, "&amp;" in the citations was a typo; it now reads "&". The `p4-PROVENANCE.md` path is qualified so that it is not ambiguous.

**Structural check against r1:**
- `git diff 1d44931 -- OUTLINE.md`: **29 insertions, 21 deletions**, in 6 hunks. All 6 are inside the lec14 rows and sections listed above.
- Line count: r1 has 1,189 lines, r3 has 1,197 (the extra lines are B6).
- The list of every `#` heading is **identical** in r1 and r3. That covers all of them, including `## Cross-folder reuse`, `## lec01-introduction.html`, `## lec08` through `## lec14`, `## backup-lec14-agentic-threats.html`, and the other backup sections.
- Every section and table row outside lec14 is byte-identical to r1.
- `outline-lint.py` reports 0 stale pointers. It warns about two ambiguous provenance basenames on line 716. That line has the same text as r1, so I left it unchanged; this is a scope rule.

## Checks

- `lint-deck.py` on the main deck: ok.
- Probe output for the main deck is identical to r2's.
- Render check (`-r 60`) of main pages 39, 40 (S75b) and 41: "without extra filtering" fits inside the box, nothing overflows, and the citation is clear.
- Narrow note check: I loaded `lec14-agentic-threats-note.html` in a 430 px iframe. Its document `clientWidth` and `scrollWidth` are both 415 px. No visible element extends past the frame (hidden KaTeX MathML excluded).
- None of the old phrases ("outputs kept", "all of its outputs") remain in the main deck, its note or `p2b-PROVENANCE.md`.
