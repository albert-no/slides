job: 2026-11-20-lec13-clarity
size: medium
deck: courses/trustworthy-ai/lec13-prompt-injection.html
audience / mode / duration: existing mixed-major undergraduate course; concept-first; 90 minutes; no activities
baseline: 9effc8ab67589f2d7e5789f04db5e92067ff46d9
id commit: existing S01–S53, introduced at 594ebea1203aabe3b3edc56443b37dd29950e411; no new ID-only commit needed
branch: 2026-11-20-lec13-clarity
pr: not opened
state: in-work
round: 1 of 2
albert decisions:
- 2026-11-20: Revise lec13 using all 19 comments, check updated design rules, clarify answers in both slides and notes, and open a PR. No merge authorization.

## Sizing and scope
Medium: many comments across the existing six-section lecture; the argument and incident/defense anchors stay. Targeted source verification and one requested conference example, not a literature survey or a new lecture. Baseline confirmed against GitHub main on 2026-11-20; no open PR exists. Albert's page numbers match baseline IDs S01–S53.

## Constraints and decisions
- Read-only repository and read-write log working mount verified with findmnt on 2026-11-20.
- Current PIPELINE.md, PLANNER_BRIEF.md, DESIGN_SYSTEM §§1,2,4,5,6,8,9,10, target leaf OUTLINE and root continuity map consulted. Parent courses/OUTLINE.md does not exist.
- Keep current instructor-note Message → explanation → details contract; all requested conceptual answers appear on slides, not only in notes.
- Keep 90 minutes and no activities. Extra pages are explanatory steps, not a new argument; slides reports mapping and timing changes.
- Questions are clarification requests, not assertions to accept unchecked: direct injection is possible through the request channel; a user's credential may access public and private repositories regardless of ownership; conference-organizer probes establish a detection mechanism, not a universal proof of reviewer misconduct.
- Updated design rules outrank legacy examples: no shrinking prose or essential diagram labels; simplify or split, use actual render checks; source/qualifier consistency across slide, notes and supplement.
- Review exact named commits; open PR only after approval and verification that subsequent commits are job-log-only. Never merge without Albert's direct order for this PR.

## Work order
- 2026-11-20: plan-v1.md complete and issued to slides. C00–C19 covered; target splits and three new mechanism slides specified. Working folder is `/workspace/extra/slides-log/jobs/2026-11-20-lec13-clarity/`.
- Targeted primary-source checks verified the requested ICML 2026 organizer probe, same-user GitHub demo, EchoLeak mechanism/provider status, and defense methods. Older incident status remains explicitly historical.
- Baseline has all S01–S53 IDs already. slides confirmed acceptance of plan-v1 and work starting on P1–P6 from the recorded baseline on 2026-11-20; exact work commit pending.
