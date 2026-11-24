# Review r3 — temporary numbering and consolidated backups

- Job: 2026-11-23-opt01-opt03-four-hour-core
- Reviewed commit: **f36ff43c5e0d28b01c12af0cef4ece9c143a8ed9**
- Relocation starting point: 3d427a6cc1a2e447179a58e8ce5d9442e947363d
- Previously approved content: 1f220ef63a13fb45ee38350bc06d498c0e6b4872
- Original baseline: 99cf2a220a92c83e938167c05745af15d9bafe13
- ID-only commit: 01ba79c7b18bb7538c0c8bcd34f6141dd604d075
- Round: 3 of 3
- Verdict: **approved**
- Existing PR: #80, https://github.com/albert-no/slides/pull/80

## Outcome

Albert's temporary numbering is implemented: the active decks and their companions are opt01 and opt02; all four optimization archives and their companions are physically under opt03-backup. The approved mathematics, slide order and 150+90-minute teaching allocation are preserved. No new blocking findings. F01–F10 remain closed.

The content-aware companion repointing is important and correct: the historical regression/SGD material points to the full archived prerequisites, not accidentally to shortened main notes. Backup labels and the archive index distinguish the historical sequence from this year's two active lectures.

Approval is pinned to the reviewed commit above. It is not a merge order. Continue the existing PR; do not open another.

## Coverage of Albert's requests

| Request | Status at reviewed commit |
|---|---|
| C01 | Done: current teaching path and backup material remain distinct. |
| C02 | Done: prob09 remains the two-hour block; opt01 150 plus opt02 90 minutes supplies four hours. Final-exam allocation is unchanged. |
| C03 | Done: two main decks with matching HTML notes and accessible Markdown editions; prob09 untouched. |
| C04 | Done: the old Optimization Half opening and four-deck roadmap remain archive-only. |
| C05 | Done: the approved norms/SVD/EYM content and proofs are unchanged. |
| C06 | Done: every removed topic remains in full-original archives; regression and SGD are also retained with both note editions. |
| C07 | Done: no probability pruning or course-wide lec renaming. Only the two expressly allowed prob05 companion-provenance phrases change. |
| C08 | Done: simplest fixed-step deterministic GD and shared proof remain unchanged. |
| C09 | Done under C11's approved correction: strong convexity retained; co-coercivity/PL not prerequisites; convex sublinear function-gap and nonconvex best-squared-gradient guarantees stay correctly distinguished. |
| C10 | Done, with C12–C14 superseding the old paths: two active cores, all remaining optimization material in backup. |
| C11 | Done: approved argument, exclusions and 150+90-minute allocation preserved. |
| C12 | Done: temporary consecutive identities appear in folders, filenames, navigation and main GD metadata; GD is Lecture 11. |
| C13 | Done: active opt01 retained, former main opt03 renamed opt02 together with its notes and generator. |
| C14 | Done: old regression, SGD and both full-original opt01/opt03 archives are colocated in opt03-backup; no duplicate live files remain at the old locations. |

## Verified final manifest

Paths are relative to `courses/deepmath/`. Every listed deck has matching `-note.html` and `-note.md` companions.

| Role | Deck | Slides | Teaching time |
|---|---|---:|---:|
| Active SVD/EYM | `opt01-svd-lowrank/opt01-svd-lowrank.html` | 68 | 150 min |
| Active GD | `opt02-convexity-gd/opt02-convexity-gd.html` | 51 | 90 min |
| Full original SVD | `opt03-backup/opt01-svd-lowrank-full.html` | 119 | outside core |
| Full original GD | `opt03-backup/opt03-convexity-gd-full.html` | 134 | outside core |
| Regression/ERM | `opt03-backup/opt02-regression-erm.html` | 110 | outside core |
| SGD | `opt03-backup/opt04-sgd.html` | 117 | outside core |

`opt03-backup/OUTLINE.md` explains the intentional full-edition overlap and historical filename/lecture prefixes. Root/course indexes show 11 active decks, with four optimization archives separately listed. Regression/SGD title pills identify them as Backup. The old GD, regression, SGD, per-core backup and course backup-index directories are absent.

## Findings and disposition

| ID | Slide ID / page | Type | Blocking | Disposition |
|---|---|---|---|---|
| F01–F10 | Locations recorded in review-r1/r2; main GD paths now opt02 | previously recorded | no | Remain closed. No substantive teaching, equation, layout or type-size changes reopen them. |

No new corrective work order. Legacy/archive and review-environment limitations below are not introduced by this relocation and are not grounds for another content round.

## Independent checks

1. **Exact commit and preservation.** Read the pinned git diff and extracted the reviewed SHA into scratch. Verified all 17 first-step moves are R100. Across all 18 deck/HTML-note/Markdown file pairs, ordered raw math spans are identical. Existing deck/article IDs and Markdown BEGIN-ID order are unchanged. Each of the six deck sources is byte-identical after only its allowed resource-prefix, active-GD identity or archive-label substitutions. Both main notes retain their 68/51 paired sections; full-original notes retain 119/134. All six Markdown editions are ASCII-only.
2. **Boundaries.** DESIGN_SYSTEM changes only the two relocated exemplar paths. The GD generator changes only its deck-path documentation. Probability changes are exactly the two permitted prob05 provenance phrases. No prob09, exam, tex, shared theme or shared script changes. Previously frozen job files and current requests/evidence copies match reviewer-owned files byte-for-byte.
3. **Pointers and resources.** All actual local href/src/logo targets in the six decks and six HTML notes exist at their final paths. Changed companion and index pointers resolve by content identity, including legacy full-SVD/full-GD prerequisites. Existing bare companion names remain unique by-name references. No new stale old-directory reference was found in the affected navigation.
4. **Browser and math.** Loaded all twelve HTML entry points in Chromium from the reviewed archive. No broken images or KaTeX errors; styles/scripts resolve and math-element totals match the work report. Both active HTML notes fit an actual 430px viewport with no horizontal document overflow; all six notes fit at 1280px. Loaded title/footer logos and checked final-path presentation.
5. **Visual review.** Inspected active GD pp1–2 and 50–51, including Lecture 11 title/closer; active SVD p60; full SVD pp1/52/100; full GD pp1/34/110; regression pp1–2/49; SGD pp1–2/32. Titles, added Backup pills, equations and figures are intact with no new clipping, overlap or bad wraps. Inspected the renamed active GD note's narrow-screen title/front matter. Unchanged mathematical content relies on the earlier full review, not a fresh review of every archive slide.
6. **Lint.** All six decks pass deck lint. Root, Deepmath and backup OUTLINE checks give zero missing/stale pointers and zero warnings. Doc-index lint passes. Active Markdown notes have no errors; their existing companion-file wording warnings remain accepted.

### Precise qualifications to the work report

These independent results clarify the frozen work report without requesting that it be edited:

- Resource depth changed for the **two full-original deck/note pairs**, not all four archive pairs. Regression and SGD were already at the same directory depth; their resource URLs correctly remain unchanged.
- Accessible-Markdown lint finds **two** pre-existing heading jumps: `courses/deepmath/opt03-backup/opt01-svd-lowrank-full-note.md:50` and `opt03-convexity-gd-full-note.md:49`. Both reproduce at the previously approved content, which differs from the relocation starting point only in job logs. Existing visual-reference warnings likewise remain unchanged. No new Markdown error is introduced.
- The four legacy HTML notes still overflow at 430px: document widths **865 / 820 / 895 / 825** for full SVD/full GD/regression/SGD. Independently reproduced the identical widths at their old paths in the prior approved archive. They fit desktop width. Preserving this existing archive layout is consistent with the explicit pass-through boundary; it is not a new main-note regression.
- The review browser loads Yonsei display/logo and KaTeX faces, but its eager font load rejects **YonseiBody** with a promise NetworkError. This reproduces in the prior approved archive using the unchanged shared font/CSS assets. Thus the work report's unqualified all-fonts-loaded claim is not reproduced here. It does not result from the relocated paths and does not justify a shared-theme change in this job.

## Plan issues and next handoff

No new plan version is needed. Accept the Backup pill wording and historical archive wording explained by the index [judgment]. The two corrected Markdown line counts in the course outline are valid metadata maintenance. No archive-responsive redesign, legacy scientific revision or font-infrastructure work is authorized.

**slides:** copy this review unchanged into `log/2026-11-23-opt01-opt03-four-hour-core/`, refresh the living job files, and push **only job-log changes**. Do not edit frozen work reports, decks, notes or other content. Return the approved copied-review pointer with the pushed SHA. Every commit after `f36ff43c5e0d28b01c12af0cef4ece9c143a8ed9` must touch only `log/2026-11-23-opt01-opt03-four-hour-core/`.

After independently verifying that final push, slides-review will update existing PR #80's summary to the final opt01/opt02/opt03-backup paths and reviewed SHA, then report the updated PR to Albert. No merge, branch deletion or PDF delivery.
