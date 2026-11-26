job: 2026-11-26-261202YonseifutureAI-korean
size: medium
deck: talks/261202YonseifutureAI/261202YonseifutureAI-ko.html; talks/261202YonseifutureAI/261202YonseifutureAI-ko-note.html
audience / mode / duration: same CEO-level senior general audience; concise Korean with natural English terms; same approved45-page/45-minute talk
baseline: e597ebf5e4ab2f0065aa603559ec1550aee645f9
id commit: pending; preserve English-to-Korean stable-ID correspondence, S27 remains retired
branch: 2026-11-26-261202YonseifutureAI-korean
pr: none yet; distinct additive localization job, dependent on unmerged English PR82
state: in-work
round: 1 of 2
active plan: plan-v1.md — complete translation/adaptation work order; no English content edits
albert decisions:
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
