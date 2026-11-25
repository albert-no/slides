job: 2026-11-25-261128yonseimath-polish
size: medium
deck: talks/261128yonseimath/261128yonseimath.html
audience / mode / duration: Korean concept-first graduation talk; middle-school students able to understand university mathematics; 25 minutes including 1-minute buffer
baseline: 37757bb365a74b434a65a0ec0f6d86d40c9b253a
id commit: inherited 1e7b5b90af65f688aa078aefb784c869ae572a8b; IDs S01–S24 already present in main and note
branch: 2026-11-25-261128yonseimath-polish
pr: existing #81 — https://github.com/albert-no/slides/pull/81; delivery head branch 2026-11-24-261128yonseimath-draft
state: in-work
round: 1 of 2
albert decisions:
- 2026-11-25 21:57 Asia/Seoul, message 16 in claw-slides-review: C01–C19 author revisions, recorded verbatim in requests.md; execute without another outline-approval gate.
- Prior audience, 25-minute duration, no detailed-formula lesson and authentic personal reflection remain in force. This is new author feedback, not another correction round of the approved draft job.
current plan: plan-v1.md
current decisions:
- Medium: many local replacements and insertions, but the three-part argument remains AI mathematics → watermarking as mathematical engineering → intuition and applications. Target approximately 24 slides, not a cap. Limited primary-source verification, not a new literature survey.
- Freeze the exact PR head above. GitHub REST readback on Nov25 confirms PR81 open/unmerged against main, head37757bb and base95df062f8f980c686f0ef45974ebd3f626ff79d2. Earlier content81a87f9 remains the approved draft, not approval of this revision.
- Create this job-named branch from baseline. Keep the old PR81 head unchanged until this follow-up is approved. After final log-only verification, slides may fast-forward the old PR head branch to the exact approved descendant (same procedure as opt01/opt02 polish). If PR head has moved independently, stop delivery and report. No second PR, force push, main push, merge or branch deletion.
- Direct author exceptions for this talk only: remove Contents despite three sections; loop the S12 illustrative animation despite the general manual-build rule; make S14 a question/exhibit without an answer paragraph, answered by S15. Do not edit shared design rules.
- C03's “회전하는 그림” is interpreted as OpenAI's original swirling-vortex illustration, whose source and exact image asset are verified in E03. Do not invent a rotating simulation or substitute unrelated fluid imagery.
- C11 uses the dgMARK site as a visual reference, not the diffusion method. Build an autoregressive, left-to-right soft-bias illustration, with local/offline playback and static fallback. C12 disallows always-green generation.
- Reconcile factual shorthand without adding caveat slides: “세상의 모든 글” → “대량의 글에서 배운 문맥별 통계적 패턴”; all-odd pixels are a deliberately planted pattern, not mathematically impossible naturally; gold-medal standard, not a physical medal awarded to a chatbot.
- No PDF requested; no merge authorization.

## Access and ownership
findmnt confirms the slides repo is read-only and /workspace/extra/slides-log is read-write. Planner files live only in jobs/2026-11-25-261128yonseimath-polish/ on that log mount. Slides copies these unchanged into log/2026-11-25-261128yonseimath-polish/ on the job branch. Slides alone owns main, companion, assets, local generator/demo code and outlines. Review exact named commits, not a working tree.
