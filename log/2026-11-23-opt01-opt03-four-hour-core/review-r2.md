# Review r2 — four-hour SVD/GD core

- Job: 2026-11-23-opt01-opt03-four-hour-core
- Reviewed commit: **1f220ef63a13fb45ee38350bc06d498c0e6b4872**
- Previous reviewed commit: 19e8acfdcb736b6232d820324c0bb5d64cfe6259
- Baseline: 99cf2a220a92c83e938167c05745af15d9bafe13
- ID-only commit: 01ba79c7b18bb7538c0c8bcd34f6141dd604d075
- Round: 2 of 3
- Verdict: **approved**

## Outcome

The blocking findings F01–F09 are closed; the optional F10 change is also accepted. No new blocking findings. The two mains remain 68 slides / 150 minutes and 51 slides / 90 minutes, with the original 119/134-slide editions and their notes preserved in backup. The strongest features remain the single worked SVD example, the distinction between computing an error and proving optimality, and one shared GD proof with three precisely different guarantees.

Approval is pinned to the commit above. It is not a merge order.

## Coverage of Albert's requests

| Request | Status at approved commit |
|---|---|
| C01 | Done: the course outline distinguishes the current teaching path from backup material. |
| C02 | Done: prob09 remains 120 minutes; opt01 150 plus opt03 90 supplies the remaining four hours; week 15 remains the final. |
| C03 | Done: two main decks with matching HTML notes and standalone accessible Markdown editions. prob09 files are untouched. |
| C04 | Done: the old “Optimization Half” opening and four-lecture roadmap are archive-only. |
| C05 | Done: necessary rank/nullity and norms, SVD, spectral EYM proof, Frobenius statement/error interpretation, and the complete Frobenius proof in the note. Mathematical/source qualifications are corrected. |
| C06 | Done: full original opt01/opt03 editions and companions preserved; opt02/04 unchanged and backup-only. |
| C07 | Done: probability pruning and course-wide renumbering remain excluded. |
| C08 | Done: deterministic GD with only step 1/L and the simplest shared convergence proof. |
| C09 | Done under C11's approved correction: strong convexity retained; co-coercivity and a separate PL assumption unnecessary; convex last-gap O(1/T) is sublinear; smooth lower-bounded nonconvex O(1/T) concerns the best squared gradient, not a local optimum. The counterexample and explicit answers remain on main slides. |
| C10 | Done: opt01/opt03 are the two active decks; remaining topics are discoverable in backup. |
| C11 | Done: the approved argument, exclusions and 150+90-minute allocation are unchanged. |

## Finding closure

Paths below are repo-relative. The fuller original locations and required fixes remain in review-r1.md. “Blocking” here describes what remains open, not the original severity.

| ID | Location | Type | Blocking | Verification / disposition |
|---|---|---|---|---|
| F01 | opt01 S82/p43, S83/p44, S90/p45, S101/p60, S102/p63; opt03 S105/p36, S106/p37, S138/p42, S123/p45, in each `-note.html` | design rule | no | Closed. The equations now break at mathematical steps, with algebra preserved and no type reduction. At an actual 430px browser viewport, none of the 119 note articles has horizontal overflow or a scrolling display. Desktop checks also pass. |
| F02 | `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.{html,md}`, S01/p1, S27/p7, S135/p19 | fact | no | Closed. Each nonconvex summary includes boundedness below; S01 also names attainment for the convex result. S98 correctly retains smoothness alone for the one-step descent inequality. |
| F03 | `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`, S73/p39, and both notes S72/p18, S73/p39 | fact | no | Closed. Total energy consistently means the squared Frobenius norm, not the norm itself. |
| F04 | opt01 main S28/p12; both notes S27/p11, S28/p12 | fact | no | Closed. The comparison names Euclidean length, and smooth squared objectives are specifically Euclidean/Frobenius. |
| F05 | opt01 main S38/p21; both notes S38/p21, S42/p27, S81/p42, S123/p66 | fact | no | Closed. Division requires positive sigma; compact factors need not be square; the rank argument uses independent images and range containment; weighted/missing-entry objectives are not generally solved by truncation. |
| F06 | opt01 main/notes S28/p12, notes S91/p46; opt03 notes S80/p4, S27/p7 | fact | no | Closed. Boyd–Vandenberghe supplies the infinity-norm source; the optional unsupported uniqueness proposition and Hessian detour are removed; Cornell replaces the plan-as-source citation. The verified spectral nonuniqueness counterexample stays. |
| F07 | `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd.html`, S140/p50 | design rule | no | Closed. All five mechanism/outcome boxes render at 24.8px, matching 1.55rem body text. The full-size render is legible and clears both the table and footer. |
| F08 | Both main `-note.md` editions, all 68/51 numbered sections | design rule | no | Closed. Rewritten paragraphs teach the mathematics directly; figure meaning and table values are present in prose/lists, proof recaps contain actual inequalities, and internal references identify numbered sections. IDs/order, math, assumptions and sources are preserved. The front-matter mention of the companion files is metadata, not a reading dependency. |
| F09 | `courses/deepmath/OUTLINE.md`, overview rows 10 and 12, lines 45/47 | unmet request | no | Closed. Active-topic descriptions no longer advertise the deferred pseudoinverse/nuclear/matrix-completion or co-coercivity/PL material. |
| F10 | opt01 main and notes S101/p60 | preference | no | Closed. Main wording identifies the proof used in the note without claiming it is the only proof; nuclear/general-Mirsky extensions are a backup pointer, with the full Frobenius argument retained. |

## Checks and limits

- Reviewed the exact r2 archive and the r1-to-r2 diff, not the working tree. Rechecked changed slides/articles and their neighbours; the unchanged full-deck content and archive-preservation review from r1 remain in force.
- Rendered and visually checked opt01 pp11–13, 20–22, 38–40 and 59–61, and opt03 pp49–51. Checked opt03 p50 at full 1280x720 size. No new overlap, clipped content, bad wrap or footer collision.
- Inspected all nine repaired narrow-note displays. Used a real Chromium 430px viewport, not a CSS width simulation; both notes have zero KaTeX errors and no horizontally overflowing article, display, paragraph or table. At 1000px, neither note has a scrolling display or KaTeX error. Display changes preserve type size and derivation steps.
- Read the rewritten Markdown passages and checked their mathematical content against the HTML articles. All HTML URLs are retained. Normalized math-span comparison found no substantive loss; the opt01 residual's 2-by-2 shape is conveyed by its matrix/row description rather than a duplicate inline dimension label.
- Main/HTML-note/Markdown ID sequences match exactly: 68/68/68 and 51/51/51. Both Markdown files are ASCII-only and have no pipe tables. Their new part headings fix the heading-level jump.
- `lint-deck.py`: both mains pass. `lint-accessible-md.py`: no errors, one front-matter companion-file warning per note, accepted as above.
- `outline-lint.py`: the root, Deepmath course and backup indexes pass. The isolated review archive reports one unrelated pre-existing absolute-path miss in `courses/trustworthy-ai/OUTLINE.md` (`/workspace/agent/lec09/r4/build_deck.py`) and five unrelated ambiguity warnings. These files were not changed in r2; the scratch environment does not contain that historical generator. This is not a new Deepmath finding.
- No r2 changes to any full-original backup, prob09, opt02/04, figures, shared theme or scripts. The tracked requests, evidence, plan-v1 and review-r1 copies match the reviewer-owned files byte-for-byte.

## Plan issues and next handoff

No argument, scope, factual-source or teaching-time issue needs a new plan version. plan-v1.md remains the specification. New part headings and standalone prose are accepted accessibility repairs, not a change in lecture content.

**slides:** copy this review unchanged into `log/2026-11-23-opt01-opt03-four-hour-core/`, refresh the living job files from the working folder, and push. Make no further content edits. Return a one-line approved pointer to the copied review with the pushed SHA. All commits after the approved SHA must touch only `log/2026-11-23-opt01-opt03-four-hour-core/`.

After that push is independently verified, slides-review opens the PR against main and reports the link to Albert. Do not merge.
