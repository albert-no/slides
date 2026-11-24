# plan-v2 — Consecutive active decks and one optimization backup folder

## Changes since plan-v1

Albert's C12–C14 (2026-11-24 14:20 Asia/Seoul) supersede the keep-existing-paths decisions: the two active decks become **opt01 and opt02**, and **all four sets of remaining optimization material physically move into `opt03-backup/`**. This is temporary packaging, not the later probability pruning or lec01–lec11 redesign.

Continue **the same branch and PR #80**, `2026-11-23-opt01-opt03-four-hour-core`; do not open another PR. Original job baseline remains `99cf2a220a92c83e938167c05745af15d9bafe13`. Freeze the relocation starting point at **`3d427a6cc1a2e447179a58e8ce5d9442e947363d`**, the verified pushed log-only successor of approved content `1f220ef63a13fb45ee38350bc06d498c0e6b4872`. This work supersedes review-r2's no-further-content-edits handoff restriction only to the extent specified below. Review-r3 will assess the relocation and changed presentation/navigation, not reopen unchanged mathematics.

Size remains the existing **large** job; this addendum is a bounded packaging revision, with **round 3 of 3** next. No literature pass or new argument approval is needed: Albert directly chose the new grouping, and audience, objectives, title sequence, exclusions, 68/51 slide sequences and **150+90 minutes** remain unchanged. All plan-v1 slide specs and review-r2 corrections remain binding except paths and active GD lecture numbering.

## 1. Final file map — must

All paths in this table are relative to `courses/deepmath/`. Retain the descriptive filename suffixes; “opt01/opt02” means the active numbering prefixes, not a request to erase useful topic names.

| Current path at relocation starting point | Final path | Acceptance |
|---|---|---|
| `opt01-svd-lowrank/opt01-svd-lowrank.html`, `-note.html`, `-note.md` | Unchanged | Active SVD/EYM, 68 slides / 150 minutes; update backup pointers only. |
| `opt03-convexity-gd/opt03-convexity-gd.html`, `-note.html`, `-note.md` | `opt02-convexity-gd/opt02-convexity-gd.html`, `-note.html`, `-note.md` | Rename both folder and all three deck/companion filenames, not just the visible title. Active GD, 51 slides / 90 minutes. |
| `opt03-convexity-gd/figs/o3b_figs.py` | `opt02-convexity-gd/figs/o3b_figs.py` | Move generator with its deck; preserve calculations. Opaque script/class names need not be renumbered. Repair embedded path documentation only if necessary. |
| `opt01-svd-lowrank/backup/opt01-svd-lowrank-full.html`, `-note.html`, `-note.md` | `opt03-backup/opt01-svd-lowrank-full.html`, `-note.html`, `-note.md` | Preserve all 119 original slides and all original note content. |
| `opt03-convexity-gd/backup/opt03-convexity-gd-full.html`, `-note.html`, `-note.md` | `opt03-backup/opt03-convexity-gd-full.html`, `-note.html`, `-note.md` | Preserve all 134 original slides and all original note content. |
| `opt02-regression-erm/opt02-regression-erm.html`, `-note.html`, `-note.md` | `opt03-backup/opt02-regression-erm.html`, `-note.html`, `-note.md` | Preserve all 110 slides and both companion editions. |
| `opt04-sgd/opt04-sgd.html`, `-note.html`, `-note.md` | `opt03-backup/opt04-sgd.html`, `-note.html`, `-note.md` | Preserve all 117 slides and both companion editions. |
| `backup/OUTLINE.md` | `opt03-backup/OUTLINE.md` | One accurate index of the four physically colocated optimization backups, with valid relative paths. Keep its link to prob06's separately located archive valid; do not move prob06. |

**Archive interpretation [judgment]:** retain the already-approved full-original editions rather than extracting only omitted slides again. They contain every removed topic, deliberately overlap the main cores for historical context, and are outside the four-hour path. Make this explicit in the backup index. Historical prefixes in the backup filenames identify their original decks; they do not create extra active lectures. Do not overwrite old regression with the newly named GD deck. No combined 480-slide backup deck is requested.

After the move there must be no second live copy at the old main GD, regression, SGD, per-main backup or course-level backup-index locations. No compatibility copies, redirects or extra lecture aliases are needed. Historical paths inside frozen job logs remain untouched.

## 2. Coverage and slide-level delta

| Request | Affected material / IDs | Required communication | Package |
|---|---|---|---|
| C12 | File/folder identities, course navigation; active GD S01/p1 and S134/p51 plus matching notes | This is the consecutive temporary active path, not a changed syllabus. | P6, P8 |
| C13 | opt01 unchanged; old opt03 main becomes opt02, with all 51 existing IDs retained | SVD/EYM first, GD second; 150+90 minutes unchanged. | P6 |
| C14 | Full opt01 S01–S119, full opt03 S01–S134, all old regression/SGD pages and their notes | The omitted/extended material is in one clearly marked backup location, not taught in 2026. | P7, P8 |
| C01–C11 | All previously approved material | Remain done; C12–C14 override only the earlier path/grouping choice. | All |

1. **Active GD S01/p1 and S134/p51 — must.** Preserve the takeaway, title, diagram/equation, duration and layout. Update the active course label from **Lecture 12 to Lecture 11** (nine probability decks, then opt01 and opt02). Apply the same numbering to the document title and both notes' title/front matter/S01 article. opt01 stays Lecture 10. This is a display/navigation change, not permission to renumber slide IDs or references to external sources such as Cornell Lecture 5. Evidence: C12–C13 and E14.
2. **All other active GD IDs — must.** Content, order and per-slide notes remain exactly as approved. Update only deck/companion/backup file pointers and any active lecture-identity metadata. All plan-v1 point/exhibit/source/time assignments survive the rename. No slides added, split, removed or merged.
3. **All active opt01 IDs — must.** No mathematical or visible teaching change. Update note references to the moved backup files/index, including the Frobenius extension and bibliography pointers. Keep the same notes content and IDs.
4. **All archive pages/notes — must.** Preserve content and order, including existing IDs where present. Only relocation-dependent asset/companion links, clear backup identification and unavoidable navigation wording may change. Do not migrate or rewrite the original notes, add fresh proofs, silently correct legacy mathematics, or regenerate the archives from the shortened mains. Keep historical lecture labels identifiable as historical; do not advertise regression/SGD as this year's active Lecture 11/finale. Prefer a short archive wrapper/index explanation over editing every historical course-map slide [judgment].

No new sources, exhibits, layouts, slide IDs or teaching-time allocations are introduced.

## 3. Work packages and boundaries

### P6 — Rename active GD

Own the old/new main GD files and its `figs/` generator. Depend on the file map above; separate the full backup before deleting the old folder. Apply the identity changes in §2, retaining main CSS, proof text, figures, ID/article ordering, Markdown accessibility and all F01–F10 fixes. Report old path → new path explicitly.

### P7 — Centralize backup material

Own the four archive deck/HTML-note/Markdown-note triplets and their old/new locations. Move rather than copy. Repair relative shared-resource and image paths from each new physical location; verify actual loaded resources rather than assuming a directory depth. Companion reading lists in an archive should link to the corresponding **full historical material** where the topic needs a removed prerequisite (e.g. pseudoinverse or co-coercivity), not accidentally to the shortened core.

No shared `reference/` or shared script edits. Preserve generator mathematics; there is no request to change rendering infrastructure. These are pass-through archives, not a new scientific review of regression/SGD.

### P8 — Navigation and companion consistency (slides owns after moves)

1. `OUTLINE.md` and `courses/deepmath/OUTLINE.md`: advertise **11 active decks** (prob01–09 + opt01/opt02), with one separate optimization backup collection. Preserve full backup descriptions and counts but relocate/label them as archival, rather than keeping old opt02/opt04 as active sequence rows. Update all file:line pointers and the active GD label to Lecture 11. Retain 68/51 and 150/90. Do not renumber probability folders or change their content.
2. `courses/deepmath/opt03-backup/OUTLINE.md`: list all four triplets and counts, explain historical prefixes and full-original overlap, and identify the two active core paths. Replace “no deck has been moved” and “kept at their original paths”. Keep prob06's archive only as an unchanged external-to-this-collection link.
3. Both active companions and all relocated archive companions: repair every local resource link, code-form filename pointer, front-matter companion name and cross-deck reading-list reference. Resolve by **content identity**, not blind opt02/opt03 substitution. Original regression stays regression; old full GD stays the extended GD archive.
4. Concrete relocated exemplar links in `DESIGN_SYSTEM.md` (at the starting point lines 312 and 371) may be changed to the new active GD folder. **Do not alter design rules.** Dated historical examples keep their historical numbering. Other implementation-document references, if needed, are path-only maintenance; report each changed file, not broad text replacement.
5. The two prob05 note occurrences “reused by name in opt04” may say “reused in the backup SGD lecture” (or an accurate new archive pointer) [judgment]. This narrow provenance/navigation edit is the only permitted probability-note change; no probability slide or mathematical text edits. All prob09 files remain untouched.
6. Any additional dependent file outside these boundaries: report the exact pointer before making a broader substantive change. Frozen logs, plans and past reviews are historical records and must not be rewritten to new paths.

## 4. Acceptance and handoff

1. **Preservation:** supply an old→new manifest for every moved file, with slide counts/ID order. Compare against the frozen starting SHA after normalizing only declared path/lecture-label/archive-wrapper substitutions. Explain every remaining difference. No topic or note content disappears; no backup generation from revised mains.
2. **Naming:** only opt01 and opt02 are active optimization decks at course root; all four optimization backups and companions are under `opt03-backup/`. Active GD contains no stale own-name opt03/Lecture 12 metadata. Legitimate historical backup filenames and dated references are not false positives.
3. **Links/resources:** scan the current navigation, active/backup companion paths and asset references for stale targets. Load all six deck entry points and all six HTML notes from their final paths; confirm local scripts/styles/images/fonts resolve and KaTeX runs. Check HTML/Markdown companion names and index links separately from mathematical citations.
4. **Rendering:** render the changed active title/closer and neighbouring slides, plus a representative math/figure page from each moved archive. Verify moved HTML notes at desktop and actual ~430px viewport. Keep fonts, diagrams, equations and accessibility unchanged; no shrink-to-fit fixes. Run deck/accessible/outline lint on affected deliverables and distinguish new failures from documented pre-existing archive/environment warnings.
5. **No scope creep:** stable main ID sequences 68/51; archive sequences 119/134/110/117; teaching time 240 minutes. All prior source qualifications and convergence corrections survive. Probability/exam/tex material stays unchanged except the two allowed note provenance strings.
6. **Report:** write `work-r3.md` with the exact pushed SHA, C12–C14 coverage, file moves, declared text changes, link checks and render checks. Copy plan-v2 unchanged and refresh living job files. Hand back the usual one-line `work-r3.md ready — in-review (<sha>)` pointer. This is the final scheduled review round; unresolved blockers go to Albert rather than an automatic fourth round.

slides-review will review the named commit, update PR #80's summary after approval, and report the new paths to Albert. No new PR, no merge, no branch deletion, and no PDF delivery.
