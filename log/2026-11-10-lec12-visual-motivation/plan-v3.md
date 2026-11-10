# Plan v3 — authorized localized completion

Job: `2026-11-10-lec12-visual-motivation`
Baseline: `cd0da5ca7ad75ceef107d28ad110407f0c33b4ff`
Latest reviewed content: `f2e696dbe9793da8ce1167d7a368408bd278ed2c`
Latest record-only commit: `f635738b153f3fe2971270f54fd7a05a800843a3`
Branch: `2026-11-10-lec12-visual-motivation`

## Changes since v2

Albert authorized the two localized S76/p58 fixes and one final targeted check at 13:40 KST on 2026-11-10 (C08). This is an explicit exception to the medium-job two-round limit, not permission to restart the deck review. The job remains medium. Use work-r3.md and review-r3.md for this final check.

All plan-v2 requirements and accepted review-r2 decisions remain. Accept the current 76 main / 76 note / 23 tech pages and the unchanged 90-minute budget. No literature, argument, audience, or teaching-time expansion. This file activates review-r2's two numbered corrections as the work order; its prior hold is lifted only for these corrections.

## Coverage

| Comment | Baseline / current location | IDs | Package |
|---|---|---|---|
| C08 | New method-key page; no baseline page / current main p58 | S76; note S76 | P4 localized completion |
| C01–C07 | Existing coverage retained from plan-v2 and review-r2 | Unchanged | No reopened work |

## S76 — method key [must; wording judgment]

**Point:** identify each plotted method/classifier combination without claiming all methods share the same classifier setup.

**Proposed title [judgment]:** “Nine Methods, Different Classifier Setups”.

**Required content / evidence:** retain all nine method identities and their stage grouping. Seven methods have LR/RF pairs; adversarial debiasing is NN only; prejudice remover is LR only (E29, Bellamy et al. arXiv v1, Table2 and Fig5). The dark/light mapping must apply only to paired coloured dots, not the grey exceptions. Keep the empirical plots and their data unchanged.

**Exhibit:** keep the readable dedicated method key. Layout is slides' choice. Correct its title and qualify the shade mapping. Address the eighth body line without shrinking type or compressing prose spacing: the agreed option is “Fair representations” in the key, with the full “Learning fair representations” name in the note.

**Companion:** synchronize `courses/trustworthy-ai/lec12-fairness-note.html` article S76 title, classifier explanation and takeaway. State seven paired methods plus the two exceptions rather than “Each method is run with…”. Preserve the full method name and source attribution. No tech change needed.

**Time:** retain the current allocation within the existing mitigation section budget.

**Acceptance:** title, key and note agree with Fig5; all nine methods remain attributable; no more than seven rendered body lines; native type/spacing, no overflow or overlap; S76's neighbours remain intact.

## Package and shared surfaces

P4 localized completion may change S76 in `courses/trustworthy-ai/lec12-fairness.html` and its paired note article. Update only directly affected lec12 OUTLINE pointers/title references if needed. No edits to other slides, figures, generators, shared files or unrelated outlines. Copy this frozen plan and refresh living job files unchanged in the tracked record.

Render S76 and its neighbours, current main pp57–59. Report F02 residual and F09 separately in work-r3.md, with exact commit and checks. The reviewer will check the diff, paired note and affected renders only. If blockers remain after this authorized final check, return to Albert; no further automatic round.

After approval, normal pushed-record and PR gates apply. **C08 is not merge authorization.** No PDF delivery requested.
