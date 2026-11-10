job: 2026-11-10-lec12-visual-motivation
size: medium
deck: courses/trustworthy-ai/lec12-fairness.html; paired lec12-fairness-note.html; visual/consistency pass on lec12tech.html
audience / mode / duration: existing mixed-major undergraduate audience (leaf OUTLINE: sophomores/juniors), concept-first, 90 minutes, no activities
baseline: cd0da5ca7ad75ceef107d28ad110407f0c33b4ff
id commit: a6d894b9b93f852af5ba6f22131663282339f3b3
branch: 2026-11-10-lec12-visual-motivation
reviewed work: f2e696dbe9793da8ce1167d7a368408bd278ed2c (round 2); previous round 6d1e21cc4b484d0b6333ca8d2607b79e9ec9facf
review verdict: round 2 revise; F02 residual and F09 on S76/p58 pending authorized final fixes
active plan: plan-v3.md
pr: not open
state: in-work
round: 3 of 3 (one localized exception authorized by Albert; ordinary medium limit remains 2)
albert decisions:
- 2026-11-10: Whole-deck visual/motivational revision, larger diagram labels, repair broken arrows. Albert will make detailed revisions afterward in a separate PR.
- 2026-11-10: “I meant lec12 fairness” corrects lec11 in the original request. Lec11 is out of scope.
- 2026-11-10 12:28 KST: Albert directly authorized resumption: “Continue from the job folder.” Continue the same pinned baseline and medium job; plan-v1 completed.

- 2026-11-10 13:40 KST: Albert authorized the two localized S76/p58 corrections and one final targeted check: “yes go ahead” (C08). Hold lifted for plan-v3 only; no merge authorization.

## Size and scope decision
Medium: all six existing sections are involved, but the argument, audience and 90-minute teaching scope stay. Reuse the deck's established literature and figures; add instructor-built examples and staged explanations, not a literature survey. Up to two review rounds. No large-job approval gate is needed unless scope or argument grows.

The existing arc remains: where bias enters → whose denominator a criterion uses → COMPAS and conditional incompatibilities → what interventions change → audits beyond classifiers → choose a criterion and state its limits. Preserve the important distinctions already present (recorded label versus actual harm, calibration versus predictive parity, empirical curves versus optimal frontiers).

Frozen baseline: 56 main slides, 56 matching note articles, 17 technical slides; no persistent slide IDs. Confirmed through the pinned git tree. Baseline browser PDF inspected as five contact sheets; baseline pages 6 and 40 inspected at full slide resolution. This is planning triage, not the implementation review. Scratch render: /workspace/agent/review/2026-11-10-lec12-visual-motivation/.

## Resolved ambiguities / exclusions
- “Whole slides” means the entire lec12 main lecture; notes must follow, and technical slides get readability/diagram/consistency fixes, not new mathematics.
- Page 6 and page 40 are examples, not the limit of the repair pass.
- New visual examples use established studies or explicitly illustrative numbers. No new empirical claim without an evidence entry.
- No new activity, homework, additional lecture, governance survey, or edits to lec11/other decks/backups/reference/shared scripts.
- The leaf's narrower audience takes precedence over the root's junior/senior wording for this job; no curriculum-wide audience change.
- No contradictory content comments remain after the lec12 correction.
- Albert's later detailed revision is separate. This job should leave a readable, motivated baseline, not anticipate unspecified later edits.

## Handoff / review gates
- slides creates the job branch from the exact baseline and adds IDs only in a separate commit, including matching main-note IDs; reports its SHA in work-r1.md.
- Scope, facts, teaching time and required-content disagreements come back before implementation changes them; layouts/splits remain slides' decision.
- Review against the exact work-pointer SHA. All main slides require visual review; technical changes and neighbouring pages require visual review too. Round 2 checks only changes and neighbours.
- No PR before approval and pushed tracked job record. No merge without Albert's direct order in claw-slides-review.

## Access checks
2026-11-10 findmnt: /workspace/extra/slides is ro; /workspace/extra/slides-log is rw. Owner writes only assigned job files under this jobs/<job-id> directory. GitHub REST open-PR query succeeded; no open PR was returned at planning time. Do not create or merge a PR during planning.
