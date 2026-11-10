# Job header

job: 2026-11-10-prob07-remove-gan
size: medium
deck: courses/deepmath/prob07-estimation/prob07-estimation.html
audience / mode / duration: existing junior-undergraduate AI mathematics course / rigorous / unchanged retained teaching pace; deletion reduces duration, no replacement material
baseline: cdc2949fd21af93b014994acb56a4c048a95becb
id commit: 9f2273b425192bef87a90bb66f25a3de17b93187 (deck-only; legacy section-organized notes recorded as F02)
branch: 2026-11-10-prob07-remove-gan
pr: not opened
state: approved
round: 2 of 2
review commit: bd7bc5e9309096a2150bae4ce715676a61cf441f
content commit: 61a2337da9be32ee0f9852865643fd35e3d69a66
albert decisions:
- 2026-11-10: Remove the GAN part completely, including JS divergence. This supersedes the older request to expand GAN/JS material in PR #62.
- No merge authorization.

## Sizing and scope

Medium: seven consecutive content slides removed, four retained/shared slides adjusted, both companion formats and the outline synchronized. This is a bounded deletion from the final application section, not a new deck or a redesign of the estimation argument. No new literature or replacement lesson is needed. Two review rounds maximum.

## Baseline and routing

- GitHub main and the read-only mount both resolve to the baseline above (checked 2026-11-10).
- PR #62 is already merged; GitHub reports no open PRs. Make a new job branch from this baseline, not the old PR branch.
- Baseline has 137 actual slide-class elements; `slide-num` is not a slide. Straight deletion gives a target of 130, not a fixed budget.
- Working mount confirmed read-write at `/workspace/extra/slides-log`; repository confirmed read-only at `/workspace/extra/slides`.
- Work order: `plan-v1.md`, supported by `requests.md` and `evidence.md`.

## Decisions and guardrails

- Remove GAN/JS from the prob07 deck, both companions, and current prob07 outline descriptions. Do not preserve it as an appendix or note-only lesson.
- Preserve KL, cross-entropy, the LLM and diffusion material, Jensen's inequality in the diffusion derivation, and the Gaussian bridge.
- Other lectures, source tex, shared reference files, and historical logs are out of scope.
- Baseline contains no stable slide IDs; assign S01–S137 in baseline order in an ID-only commit, including matching note articles as the contract requires. Record the SHA separately from content changes.
- The HTML companion is currently section-organized rather than one article per slide. Keep all retained prose/math intact during ID setup. If a faithful note-ID mapping requires substantive rewriting, return that as a plan issue before broadening this deletion job.
- Review the exact work-report commit. Open a PR only after approval and a verified log-only tail; never merge without Albert's direct order.

## Review decisions — 2026-11-10

- Round 1 reviewed a825c1ed76945e1f2cc6f121eb6e5996b2b9a5a7: C01 complete; content/render satisfactory; verdict revise for F01 (11 section-table Location offsets).
- State passed in-review → revise → in-work on delivery of review-r1.md. Round 2 is metadata-only; no additional slide edits requested.
- Note-ID plan issue: no matching per-slide articles exist in the baseline. Preserve chapter-style companions; record pre-existing structural limitation as nonblocking F02 rather than expand deletion into a note migration. No pipeline/standing instruction changes.

- Round 2 reviewed bd7bc5e9309096a2150bae4ce715676a61cf441f: F01 closed; verdict approved. No new blockers. Awaiting final review copy/push before PR creation; any post-review commits must be job-log-only.
