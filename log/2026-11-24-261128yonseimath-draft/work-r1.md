# work-r1 — 2026-11-24-261128yonseimath-draft

Plan: `plan-v2.md`. Round 1.

## Branch

- Branch `2026-11-24-261128yonseimath-draft` from baseline `95df062`.
- `011a4eb`: draft deck, Korean note, generated figures, and planner copies.
- `1e7b5b9`: **ID-only commit**. It adds `data-slide-id` to the 24 deck slides and 24 note articles (48 lines) and changes nothing else.
- The head commit holds the leaf and root OUTLINE, the S05 cite-title fix and this report. Its SHA is in the pointer message.

## Packages

There was one package, done inline because the deck is new and every slide depends on shared CSS and figures. Files:

- `talks/261128yonseimath/261128yonseimath.html`: 24 slides. Local CSS is at `:17-93` with prefix `ym-`.
- `talks/261128yonseimath/261128yonseimath-note.html`: Korean script with 24 articles in display order. It has a pacing table: 6:00 + 11:00 + 7:00 + 1:00 buffer = 25:00. Each article carries 메시지, a reading guide, 대본 and 출처. There is no tech supplement, as the plan specifies.
- `talks/261128yonseimath/figs/generate-figures.py` produces four SVGs: `coins-100`, `binom-pmf`, `rectangles` and `log-chord`. All labels are HTML overlays. The script asserts these invariants:
  - exactly 70 heads in the coin grid;
  - the exact Fraction PMF tail = 0.00003925069822796835;
  - a+b = 10 with products 16/25;
  - the chord midpoint is ln 4, and ln x lies above the chord on (2, 8);
  - the E20 bars: 40/30/20/10 → 48/24/16/12, with marked mass 50% → 60%.
- `talks/261128yonseimath/OUTLINE.md` (leaf) and the root `OUTLINE.md` (one folder bullet and two lookup rows).

## Slide mapping

This is a new deck, so there are no old pages.

| slide ID | old page | new page | split / moved |
|---|---|---|---|
| S01–S20 | — | 1–20 | — |
| S23 | — | 21 | inserted before the close (AM–GM) |
| S24 | — | 22 | inserted before the close (log concavity / Jensen) |
| S21 | — | 23 | — |
| S22 | — | 24 | — |

No slide was split. Display order ≠ ID order only in the last four slides, as the plan specifies.

## Deviations (layout and placement, my authority)

- S12 and S19 use 1.5rem flow boxes (`.ym-row`, `.ym-4`), against 1.7rem on the other flows, so that four boxes or a side-by-side row fit. Both are at or above the body size, so this does not shrink type.
- The S10 cite names EU AI Act Art. 50(2) and 인공지능기본법 제31조. They are a social-motivation cue only and the slide makes no legal claim.
- SynthID (E07) appears only in the note, at S16, as an optional paragraph, to keep S16 to one exhibit.
- The note at S15 adds z = 4 and "약 2만 5천 번에 한 번". Both are my arithmetic from the exact tail (1/0.0000392507 ≈ 25,477).
- The note at S19 works "10번 중 7번 이상" = 176/1024 = 0.171875 (E16).

## Sources checked this round

- The full law name was verified on law.go.kr: 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 제31조(인공지능 투명성 확보 의무).
- The OpenAI page title was fetched: "On the Navier–Stokes Millennium Prize Problem". The deck S05 cite and the note 출처 now use it; the draft had "Navier–Stokes solution". No prize claim was added to the slide or the script.
- The Clay page title matches, "Navier-Stokes Announcement", and the cite now uses that spelling.
- The IMO cite title comes from E02 and was not re-fetched this round.
- R07 timed out. No claim relies on it.

## Removed as unsourced

- S05 note: "Clay가 내건 유명한 미해결 문제".
- S04 note: "사람이 읽을 수 있는 증명".

Each was deleted rather than corrected.

## Unsourced facts

None remain in the deck. The S20 reflection paraphrases Albert's own words (C24). Please confirm with Albert that the paraphrase is acceptable.

## Plan issues

None.

## Checks

- `lint-deck.py`: ok.
- `find-wordy.py` and `find-dense.py`: no flags.
- `outline-lint.py`: 0 stale pointers. The 5 warnings are pre-existing and none are in this talk.
- Note at 430 px: docW 485 ≤ vw 500, and no element overflows.
- Render: all 24 pages were checked at `-r 60`. After the layout pass I re-rendered pages 05, 07, 08, 11, 12, 13, 16, 17, 19, 20 and 22, and re-rendered page 05 again after the cite fix. There is no overflow and no overlap, and the cites and footer clear each other.
