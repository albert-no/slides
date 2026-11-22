job: 2026-11-22-lec14-finale-refresh
size: medium
deck: courses/trustworthy-ai/lec14-agentic-threats.html
audience / mode / duration: existing mixed-major undergraduate course / concept-first / 90 minutes including flexible explanation time; no activities
baseline: 34b40ca35c9433be7c9d2ca2cc90d0d89bbdd233
id commit: 594ebea1203aabe3b3edc56443b37dd29950e411 (existing IDs, no new ID-only commit required)
branch: 2026-11-22-lec14-finale-refresh
pr: not opened
state: approved
round: 2 of 2
albert decisions:
- 2026-11-22: Albert requests a brief preparatory lec14 refresh after lec13: remove duplication, enlarge diagram type, add motivating real-world examples, explain selected recent works at high level, and add a brief course-wide take-home message. No merge order.

- 2026-11-22 follow-up (C06): Albert permits brief new topics beyond the 14 taught lectures. Active work order is plan-v2.md: two short previews, AI persuasion and AI companionship/emotional dependence, within the existing ending. Reserve new S55/S56; 50-slide target before optional splits, 90 minutes unchanged. This supersedes v1’s restriction to existing topic coverage; no broad survey or new core section.

- Review round 1 received 2026-11-22: exact commit ad77502e7f1c47f0a067a275f6ffb542e80676d9. Work-r1 reports 51 main/notes, S54a/S54b split and 90-minute total. Review against baseline34b40ca35c9433be7c9d2ca2cc90d0d89bbdd233 and active plan-v2; no verdict yet.

## Sizing and boundaries
Medium: the existing six-section argument stays. This is a bounded editorial/visual refresh, not a new deck, restructure, or literature survey. Source work is targeted verification of two concrete case reports and selected works already in lec14, with the relevant dated follow-up to one case. Do not expand into a comprehensive frontier roundup.

The baseline is GitHub main confirmed through REST on 2026-11-22; no open PRs. It includes the merged lec13 clarity revision. Main deck and paired notes have S01–S51 (51 each); the optional supplement has 14 slides. Reuse these IDs, reserve S52–S54 for additions, never recycle retired IDs.

Scope: lec14 main + paired instructor notes; only necessary concordance/readability changes to lec14tech; new assets/generators in a lec14-specific figure folder; lec14 leaf OUTLINE entry and dependent index/pointers. No edits to lec13, other lectures, reference/, design rules, or unrelated scripts. The known lec13tech duplicate wrapper is a separate follow-up, not part of this request.

## Decisions and checks
- Mount check: /workspace/extra/slides read-only; /workspace/extra/slides-log read-write. Reviewer writes only this working job folder, not tracked log/<job-id>/.
- Guideline basis: current PLANNER_BRIEF and DESIGN_SYSTEM §§1,2,4,5,6,8,9,10 at the baseline; leaf course OUTLINE and root course map read. Parent courses/OUTLINE.md does not exist.
- Resolve brief vs examples/recent works: replace repetitive material rather than append an extra survey; retain 90-minute teaching envelope, move statistical/protocol detail to notes. Counts/layouts are targets, not constraints.
- Review exact commit only. Approval does not authorize merge. Two review rounds maximum; unresolved blockers at the limit go to Albert.

## Work order — 2026-11-22
- plan-v1.md completed and issued; requests.md and evidence.md complete for this bounded pass. Existing six sections retained, roughly 48 main slides targeted (not a cap); three added case slides, six redundant slides migrated to paired notes.
- New case threads: Project Vend (June/December 2025) and METR real-developer trial (early-2025, explicitly caveated by February 2026 follow-up). Recent-work highlights use existing MAST and June 2026 attack-selection anchor, with high-level methods and limitations; no broad survey.
- Target 85 minutes section teaching plus 5 minutes flexible explanation/questions, no activities.
- Next: slides creates the named branch from frozen baseline, builds, copies reviewer files unchanged and sends exact work-r1 commit. No PR exists yet.

## Review r1 disposition — 2026-11-22
- Exact reviewed content: ad77502e7f1c47f0a067a275f6ffb542e80676d9. Verdict revise; review-r1.md is the round2 work order. State in-review → revise → in-work; next submission is final allowed round2.
- Eight blockers: control scope, essential label size, two overflowing note tables, no-U baseline label, Motwani date, METR crop clipping, S06 generator consistency, unfamiliar acronym explanations. One optional narration cleanup.
- Accepted51-slide split,85+5-minute schedule, S55/S56 sources and provenance; E24–E29 appended. Leave unused assets and lec13tech alone. No plan-v3 or scope expansion.

- Round2 received 2026-11-22: exact commit58e37fdf517799b978f042551f56c9c5dd7713ef, fixes1f9f8c3. Re-review changes/neighbours only; verdict pending.

## Final review — 2026-11-22
- Approved exact58e37fdf517799b978f042551f56c9c5dd7713ef, review-r2.md. F01–F08 closed; optionalF09 taken. C01–C06 done. E30 appended for final geometry/crop verification.
- Await slides copying final review/living records and pushing. Every post-review commit must be job-log-only before PR creation against main. No merge authorization.
