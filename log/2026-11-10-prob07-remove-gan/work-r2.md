# work-r2 — 2026-11-10-prob07-remove-gan

- Branch: `2026-11-10-prob07-remove-gan`
- ID-only commit: `9f2273b` (main deck only; F02)
- Fix commit: `f4d1cb0`. Head commit: named in the pointer message (the commit that adds this file).
- Scope: `courses/deepmath/OUTLINE.md` only. No change to the deck or the notes since `a825c1e`.

## Findings

| ID | Action |
|---|---|
| F01 | Done. On the eleven section rows (01–11), the final Location pointer now lands on the section divider `<div class="slide section-slide left" data-slide-id="…">`: 155, 215, 363, 445, 550, 734, 992, 1281, 1605, 1854, 2020. I checked each line against the deck. Inline descriptive pointers, the title row and the bridge row are unchanged. |
| F02 | Accepted. Slide IDs stay deck-only for this job. The notes keep their chapter organization. |

## Checks run

- `outline-lint.py`: 0 stale/missing pointers (the same 5 pre-existing warnings in other folders).
- `git diff a825c1e f4d1cb0` touches only `courses/deepmath/OUTLINE.md`, 11 lines.
- No re-render: no slide changed.
