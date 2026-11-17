job: 2026-11-17-prob09-major-revision
size: large
deck: courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html
audience / mode / duration: junior undergraduate AI majors / rigorous, example-led / 150 minutes (two 75-minute teaching blocks); approved 2026-11-17 12:27 KST
baseline: b20ab73ac7e74e9489d379cf9caad7565f17e31e
id commit: not yet created; baseline has no slide IDs and chapter-style notes
branch: 2026-11-17-prob09-major-revision (created from baseline; planning record head 7e07e81235f89357f7546343186bd8f461a8e0f2)
pr: none
state: in-work
round: 1 of 3
current plan: plan-v2.md (complete stage-4 work order; 85 slide targets, 150 minutes, five packages plus integration)
current action: slides to perform accepted A/B setup and full build, then return exact-commit work-r1 pointer; owner review and PR follow
setup decision: work-r0 at 7e07e81235f89357f7546343186bd8f461a8e0f2 accepted; mechanical note wrappers, then joint attribute-only ID commit; Markdown untouched during setup; details in plan-v2
validation: 85 unique full specs, 113 baseline dispositions, 16 new IDs plus two splits; disjoint complete package ownership; section times total 150 minutes
albert decisions:
- 2026-11-17: requested a major revision of prob09 slides and notes after a content, continuity and redundancy audit against prob01-prob08.
- 2026-11-17 12:27 KST: Albert said “go ahead” in response to the scope/outline proposal; stages 1-3 and proposed pacing approved. Full build plan being completed; no merge authorization.
- 2026-11-17: stages 1-3 approval implemented in full plan-v2; build order issued in round 1. The earlier planning query is resolved by the accepted two-commit setup. No contract exception, merge or PDF delivery is authorized.

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

Albert approved stages 1-3 on 2026-11-17. Complete plan-v2, then send its work-order pointer. No content build order has yet been sent.

## Setup decision — 2026-11-17

Read work-r0.md at 7e07e81235f89357f7546343186bd8f461a8e0f2 and verified that changes from baseline touch only this job's tracked record. Accept the two-commit proposal: A adds only unlabelled note-article wrappers, preserving the existing content and order; B adds matching IDs to deck and HTML articles in a joint attribute-only commit. Commit B satisfies the ID-only requirement; no deck-only exception or semantic rewriting in setup is authorized. Temporary empty articles are scaffolding only and must all be replaced or removed according to the final slide mapping during the build. Leave Markdown untouched in A/B. Report all block-to-baseline assignments, including any non-exact match. Check wrapper-stripped byte equivalence (permit wrapper-insertion whitespace only), visible text/math equality and unchanged desktop/narrow rendering for A, and exact attribute-stripped byte equality for B. If chapter boundaries prevent 113 valid ordered wrappers without other edits, stop and return the problem. Record both SHAs; B becomes the id commit. This setup is authorized only with the completed plan-v2 work order, not this planning header alone.
