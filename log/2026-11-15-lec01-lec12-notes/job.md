job: 2026-11-15-lec01-lec12-notes
size: medium
deck: courses/trustworthy-ai/lec01-introduction.html through lec12-fairness.html; the 12 canonical paired -note.html files
audience / mode / duration: existing mixed-major undergraduate course; concept-first; preserve every existing timing/core-path choice
baseline: 99450923b41e94f10d0c557a4fc0f46b42a9c91d
id commit: pending slides ID-only commit for lec01–lec11; preserve lec12 IDs exactly
branch: 2026-11-15-lec01-lec12-notes
pr: not open
state: in-work
round: 0 of 2
albert decisions: 2026-11-15 00:34 KST — authorized checking and revising all lec01–lec12 companion notes; brief slide message first, details second; pause if either provider reaches its five-hour limit and resume after reset
last checkpoint UTC: 2026-11-14T15:42:14Z
capacity hold: no
capacity provider: none reported
capacity reset UTC: unknown; never infer from a five-hour elapsed timer
recovery task: lec01-12-notes-recovery-e923 — gated every 30 minutes; wakes for a due recorded hold or 90 minutes without a durable checkpoint; cancel after final approval/closure

## Sizing and scope decision
Medium: twelve existing companions, no change to the deck argument, slide sequence, teaching time or research scope. Volume alone does not make this a new-deck/restructure/literature-survey job. No stage-approval gate; Albert explicitly said to start all. Two full review rounds maximum, then escalate unresolved blockers.

## Baseline inventory and initial sampled-content audit
Local main and GitHub main independently matched the baseline. Read-only repo and read-write log mount confirmed with findmnt. 902 main slides and 902 matching articles across 12 tracked canonical companions. Counts: lec01=46, lec02=69, lec03=70, lec04=65, lec05=68, lec06=75, lec07=75, lec08=101, lec09=91, lec10=88, lec11=74, lec12=80. All articles already have a takeaway; the chief issue is hierarchy and exposition, not adding a redundant summary label. 599 articles have more than 65 words of top-level prose (diagnostic, not an automatic failure). Examples range to 431 words before detail in lec12 p75. Per-article baseline map and requirements are in plan-v1.md.

## Progress/checkpoint
Planning complete; plan-v1.md is the work order for P1–P12. slides acknowledged the work order at 2026-11-15 00:41 KST and is starting the ID-only commit, then P1–P12. No package completion or commit SHA reported yet. No content reviewed, no PR or merge authorization. slides owns all note edits, ID addition, commits, push and tracked records. Owner owns only the contract files in this working folder.

## Capacity handling
Either provider's confirmed capacity limit pauses new work for the whole job. Owner records provider, last safe commit/package and the actual reset time in this living header when available. Preserve the ordinary pipeline state and record capacity hold separately (the contract has no paused state). Do not switch model/provider/account or repeatedly retry a known block. When reset is confirmed, clear the hold and continue from the first incomplete package. A scheduled recovery check will inspect stalled/held work; it must not treat silence or a slow package as proof of a quota limit. Unknown reset time requires a bounded availability check, not a fabricated reset time. Checkpoint every lecture and at context/usage warnings; no restarting already completed packages.
