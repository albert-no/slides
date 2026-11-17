job: 2026-11-17-prob09-major-revision
size: large
deck: courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html
audience / mode / duration: junior undergraduate AI majors / rigorous, example-led / 150 minutes (two 75-minute teaching blocks); approved 2026-11-17 12:27 KST
baseline: b20ab73ac7e74e9489d379cf9caad7565f17e31e
id commit: not yet created; baseline has no slide IDs and chapter-style notes
branch: 2026-11-17-prob09-major-revision (reserved; not created)
pr: none
state: planning
round: 0 of 3
albert decisions:
- 2026-11-17: requested a major revision of prob09 slides and notes after a content, continuity and redundancy audit against prob01-prob08.
- 2026-11-17 12:27 KST: Albert said “go ahead” in response to the scope/outline proposal; stages 1-3 and proposed pacing approved. Full build plan being completed; no merge authorization.
- Planning query to slides: baseline notes are 11 chapters, with no per-slide articles. Propose a contract-compliant way to prepare matching note articles and make the required joint deck/note ID-only commit. Can a separate purely mechanical note-structure preparation preserve every word/formula, followed by an attribute-only ID commit, satisfy the contract? Do not implement yet; report the setup decision/issue in the job record and send its pointer. No relaxation of the contract is authorized. Full plan follows.

## Sizing and boundaries

Large: Albert explicitly requests a major revision; the audit supports a restructure rather than a cosmetic pass. Stages 1-3 are presented together for approval in plan-v1.md. Stage 4 will be a new, full slide-level plan with stable-ID allocations and executable packages after that approval. Do not start implementation from plan-v1.md.

Only prob09 is to be revised. prob01-prob08 are read-only continuity sources, not an instruction to reopen eight earlier decks. Required companion scope includes both HTML instructor notes and the accessible Markdown edition, plus the prob09 entries in courses/deepmath/OUTLINE.md. Root/folder pointers may change only if made stale by this job. No global design-system changes are requested.

## Baseline and audit provenance

- RO repo and RW log mounts confirmed with findmnt on 2026-11-17. Owner writes are confined to this untracked job folder; no tracked record or deck source has been edited.
- GitHub REST GET confirmed main equals the baseline above; no open PRs at audit time. The latest prob07 removal and prob08 revision are already represented in this baseline; older memory of unmerged PRs is not used as the course state.
- prob09: 113 slides, no data-slide-id attributes. HTML companion: 11 chapter sections, zero slide articles, zero message paragraphs. Accessible Markdown: 704 lines.
- Audit read every prob09 slide body, the complete accessible note, corresponding HTML note structure and critical sections; inspected all prob01-prob08 title sequences and the actual prerequisite slides listed in plan-v1. This is a targeted continuity audit, not a claim that all earlier decks received a new full correctness/visual review.
- Read PLANNER_BRIEF.md and the referenced DESIGN_SYSTEM.md sections 1,2,4,5,6,8,9,10 at the baseline, root and deepmath outlines, and relevant generative-course outline/exemplar. Design rules remain in those canonical files, not copied into this record.
- Baseline archived without editing into /tmp/prob09-b20ab73 for a Chromium print render: 113 pages. Visually checked pp4,27,30,37,62,96,106,109. These selected renders do not establish a full-deck visual pass; no obvious clipping on those pages, but capacity/density and takeaway-title work is needed. Scratch renders are not deliverables and no PDF was sent.
- Mathematical source check and original calculation register: evidence.md. Source cutoff: 2026-11-17. Literature scope is foundations and the existing application, not a survey of current frontier-model training recipes.

## Implementation gate / ID migration

The contract requires an ID-only commit with deck and matching note IDs before substantive edits. Existing note chapters have no one-article-per-slide structure, so the stage-4 plan must resolve this setup explicitly with slides: do not label a substantive rewrite of 113 articles as ID-only. Preserve content and useful anchors during any mechanical identity preparation; pair every final article to its final slide and report the baseline-to-final trail. If contract-compliant preparation is not possible, obtain an explicit decision before building; no exception has been authorized.

## Next action

plan-v1.md is complete: scope, evidence map, audit decisions, title sequence and time budget. Obtain Albert's approval of stages 1-3. Then resolve ID/note preparation and write plan-v2 with full per-slide specifications and executable package boundaries before sending slides a work-order pointer. No work order has been sent.
