# Plan v2 — consolidate the approved Korean version into PR82

## Change from v1

Albert's new C05 (message40) explicitly requests everything in the same PR82. Replace only v1's separate-branch/PR delivery policy. All slide/note/content, source, preservation and language requirements stay unchanged. Do not create a third PR or rework the decks.

This is an administrative integration of approved content, not a new English review round or a request for further translation. Use work-r2 for the C05 handoff; the second review will verify exact-commit integration, not repeat unchanged-slide rendering.

## Pinned inputs and destination

Verified via GitHub REST before this order:
- PR82 is open/unmerged against main. Destination branch: `2026-11-26-261202YonseifutureAI-overview`; current head `e597ebf5e4ab2f0065aa603559ec1550aee645f9`.
- PR83 is open/unmerged against main. Source branch: `2026-11-26-261202YonseifutureAI-korean`; current head `4c663b60d8a95365dbbbc3a521f1cdd3d053b157`.
- The PR82 head is an ancestor of the PR83 head. The source head contains the complete approved English and Korean pair plus both job histories. Korean content was approved at `0bc0eb8d92699c895d3b6136e37f98f71385de85`; its finalization4c663b6 was independently verified log-only.

## Coverage

| Comment | Surface | Required outcome |
|---|---|---|
| C01–C04 | English/Korean main + notes, all45 paired slides | Preserve the exact approved artifacts. No source edits. |
| C05 | Existing PR82 head and job records; redundant PR83 | Both language versions delivered through PR82 only; PR83 closed by slides-review after verification. |

## P6 — integration work order for slides

1. Advance PR82's existing destination branch to include the exact approved combined source head `4c663b60d8a95365dbbbc3a521f1cdd3d053b157` using a normal fast-forward/non-force push. Preserve ancestry and the existing PR82; no history rewriting, squash or source reconstruction. If the remote destination moved beyond the pinned head, stop and report the new exact head rather than overwrite it.
2. On that destination branch, copy this new `plan-v2.md` unchanged and refresh this Korean job's living `job.md` and append-only `requests.md`. Keep both historical job records; never rewrite frozen plans, work reports or reviews. The English job's files need not change.
3. Write `log/2026-11-26-261202YonseifutureAI-korean/work-r2.md`: source/destination branch, exact old/new heads, confirmation that4c663b6 is an ancestor, and the complete diff against4c663b6. That diff must contain only this Korean job's log updates. Report all four HTML hashes to demonstrate that this is integration only.
4. Push to PR82's destination branch and send the usual exact-commit work-r2 pointer. Keep the source branch intact; no branch deletion is requested.

Allowed changes since4c663b6: only `log/2026-11-26-261202YonseifutureAI-korean/`. No deck, note, outline, asset, reference, script or other-job record edits. No new source seed, rendered exports, research or implementation subagents are needed.

## Verification and PR administration

slides-review will verify the named destination commit, ancestry, remote PR82 head, unchanged source tree, copied job files and C05 coverage. Unchanged deck content keeps its prior full review; no redundant45-page render is needed. After the review is copied/pushed and its log-only finalization verified, slides-review will update PR82's description to cover both languages and both job records, and close redundant PR83 with a pointer to PR82.

**No GitHub PR merge is authorized.** Do not call a merge endpoint, push main, force-push, delete branches or change repository settings. “Same PR82” means consolidation into its head branch for Albert's final check, not merging either PR into main.
