# Plan v5 — timing clarification and final local repairs

## Changes since v4
This is a narrow amendment, not a new restructuring. All v4/v3/v2 requirements remain unless explicitly corrected below. Exact r2 commit: `c16c37a5faaafe8890f11301fea1a0a97a78725b`. The final allowed implementation/review round is round 3 of 3.

1. **S69b timing correction:** v4 accidentally said “retain 1.5 min”. Retain **2.25 min**, as already assigned by v3's pacing redistribution and implemented in r1/r2. Main remains 59 slides and 85 teaching + 5 flexible minutes. Do not remove or relocate 0.75 minutes.
2. **S75b wording clarification (F10):** the realignment experiment applies no additional filtering to its training trajectories. Do not imply all three training routes use teacher-written answers. OPD still uses learner-written answers and teacher token scores. Use “without extra filtering” in the shared diagram; full route-specific details belong in notes. Evidence E26. Existing setup/result/bounded-remedy argument and 1.25 min target are unchanged.
3. **Restore the leaf outline (F09):** round 2 accidentally removed much of `courses/trustworthy-ai/OUTLINE.md`. Restore all unrelated material from exact r1 `1d4493167f41a5d39237fe4e1703e40f94fdfe40`; reapply only the authorized lec14/backup counts, section descriptions and line-pointer changes. This repairs scope damage; it does not authorize editing lec01–13 or their descriptions.

## Accepted implementation choices
- Backup S92's title may include “Model”: its three-column experiment warrants it.
- Backup S91 may preserve the source's original shared y-axis wording, because the external left/right keys explicitly distinguish its two operational outcomes. Do not alter source pixels to relabel it.
- S72b's shorter diagram is accepted at unchanged type size; it renders cleanly.
- Both notes passed independent 430px device-emulation checks. The executor's 485px minimum-window limitation is not a remaining blocker.

## Packages and shared surfaces
- P2b: S75b and matching note/accessibility/provenance wording only, following F10.
- P0: restore and update the leaf OUTLINE following F09; retain all other accepted content and counts. Backup remains52 with S95/S91–S94 before S86; main59 and85+5. No shared reference or technical-deck changes.
- No new source, topic, slide ID, graphic, activity, proof or timing expansion. No Albert approval gate is needed for these repairs.

## Acceptance
`review-r2.md` gives the complete self-contained change requests. Return exact pushed work-r3 SHA and dispositions for F09/F10. Verify the outline structurally against r1, not just with a lint check that can miss deleted sections. Render S75b and neighbours after the wording change and check its note at approximately430px. Do not reopen accepted slides or rerender unchanged content. Approval/PR/merge remain withheld.
