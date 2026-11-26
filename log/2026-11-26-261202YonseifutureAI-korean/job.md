job: 2026-11-26-261202YonseifutureAI-korean
size: medium
deck: talks/261202YonseifutureAI/261202YonseifutureAI-ko.html; talks/261202YonseifutureAI/261202YonseifutureAI-ko-note.html
audience / mode / duration: same CEO-level senior general audience; concise Korean with natural English terms; same approved45-page/45-minute talk
baseline: e597ebf5e4ab2f0065aa603559ec1550aee645f9
id commit: 8c6c4f4f6f1734d5a64a290bc7f1dd4d045b5d12 (ID-preserving English byte-copy seed; verified)
branch: 2026-11-26-261202YonseifutureAI-overview (PR82 destination per C05; original implementation branch: 2026-11-26-261202YonseifutureAI-korean)
pr: 82 — https://github.com/albert-no/slides/pull/82; PR83 pending supersession/closure after consolidation
state: in-work
round: 2 of 2 (C05 integration-only verification; source content remains approved at round1)
active plan: plan-v2.md — consolidate approved English/Korean artifacts into existing PR82; no source edits
albert decisions:
  - 2026-11-27 00:20 Asia/Seoul, message40/C05: “do it all in same PR#82”. Supersedes separate-PR policy below; integration only, no merge order.
  - 2026-11-26 23:38 Asia/Seoul, message30: preserve the current slides and add a Korean version; use concise expressions, retain awkward-to-translate English terms and simple words such as Agent, Private, Public.
  - New language deliverable, not a fourth review round on the completed English job. No reopened English findings, no merge authorization and no PDF/PPTX/export request.

## Sizing and frozen scope
Medium: localization of an approved argument/sequence, not a new-content talk or restructure. All45 slides reuse the existing cases, figures, data, section order and timing; no literature survey or new facts. The new files require a full language/render pass and at most two review rounds. The English job remains separately approved at2336d436adcb8ccc4c60c72ab9f64b93d8ebf630.

Baseline is the exact English PR82 head, independently confirmed open/unmerged on2026-11-26. Read-only repo/read-write job-log mounts verified. Read pipeline, planner brief, relevant design sections, target outline and approved slide/note message sequence. Sources remain the pinned original evidence register and primary references, not the translation plan.

## Additive delivery and branch ownership
slides creates this named branch from the baseline. Do not append new content to PR82 or change its branch: Albert asked to keep the current slides. Build the additional Korean main and companion note HTML in the same talk folder; reuse existing figure files without changing them. Root/leaf outlines may gain bilingual entries; existing English locations remain valid.

The baseline contains the pending English PR82. After Korean approval, slides-review will open a distinct localization PR against main with that dependency explicit; if PR82 has already merged, the diff naturally excludes it. Do not merge PR82 as an implementation convenience, retarget/replace it, rebase onto moving main, or push anything to main. All merges still need Albert's direct order for the particular PR.

## Preservation boundary
The two English HTML files and all existing figures/reference/scripts are immutable in this job. No language toggle or editorial cleanup may alter them. Evidence E01 records their exact hashes. Only new Korean files, target/root outline additions, and this job's tracked record may differ from baseline.

## Review handoff
- Round1 exact head: `0bc0eb8d92699c895d3b6136e37f98f71385de85`; received work-r1 pointer. Comparing the additive Korean files against the frozen English baseline.

## Round1 outcome
- `review-r1.md`: approved at `0bc0eb8d92699c895d3b6136e37f98f71385de85`; full Korean language/source-equivalence and45-page screen/print pass complete. C01–C04 done, no blocking findings.
- ID seed verified as exact English byte copies carrying the stable IDs; no English/assets/reference/scripts changed.
- Await slides' log-only finalization/push and exact head before opening a distinct Korean PR against main, explicitly dependent on English PR82. No merge/export order.

## Finalization and PR
- Finalization `4c663b60d8a95365dbbbc3a521f1cdd3d053b157` verified: sole postreview commit changes only this job's `job.md` and `review-r1.md`; all five planner files matched at that head. Remote branch head confirmed identical.
- PR83 opened against main through GitHub REST API. Returned head matches the verified finalization. English PR82 remains open/unmerged at baseline e597ebf; dependency and the resulting combined main-relative diff are explicit in PR83.
- No merge authorized for either PR; no source edits or export delivery performed.

## C05 consolidation order (supersedes earlier delivery policy)
- plan-v2.md replaces the earlier prohibition on appending Korean work to PR82. Both PRs verified open/unmerged; PR82 head e597ebf is an ancestor of approved combined head4c663b6.
- slides will advance PR82's branch normally, preserve all approved sources and both job histories, and return exact work-r2 head. slides-review will verify, update PR82 and close redundant PR83.
- No merge/main push, force push, source edit or branch deletion authorized.
