# work-r2 — 2026-11-25-261128yonseimath-polish

- Branch `2026-11-25-261128yonseimath-polish`. Content commit: `ab5d5ba`. The log commit that adds this file is the pointer SHA.
- PR #81's head `2026-11-24-261128yonseimath-draft` is untouched and still at `37757bb`.

## Findings

- **F01 (blocking), done.** The S24 midpoint label is now the inline axis label $(a+b)/2$, on the same baseline as $a$ and $b$ (top 106% instead of a stacked \dfrac at 112%).
  - Type size, figure width, graph geometry, the inequality block and the positivity qualifier are unchanged.
  - Page 22 rendered at -r 150: the full label is clear of the inequality block, and the block is clear of the cite. Neighbours 21 and 23 rendered at -r 60 are unchanged and clean.
- **F02 (blocking), done.** S12 note data paragraph:
  - The general rule is stated once: green ×1.5, then ÷1.25, so green mass goes 50→60% at every position.
  - The numbers are tied to their positions. Position 1 is 40→48, 10→12 (green), 30→24, 20→16 (red), and positions 3 and 4 use the same assignment. Position 2 is 친구와 40→32 (red), 혼자 30→36, 가족과 20→24 (green), 급하게 10→8 (red). I checked these against `figs/watermark-demo-data.js`.
  - The spoken script now adds, after "초록과 빨강 두 묶음으로 나눕니다": "문맥을 바탕으로 무작위처럼 나누되, 같은 문맥에서는 같은 묶음이 나오게 합니다."
  - The statement that this is a fixed illustrative sequence, not sampled ChatGPT output, is kept. Demo data and visuals are unchanged.
  - work-r1 (frozen) gave the demo-spec probabilities as "48/12 green and 24/16 red". Those are the position-1 values. The rule is the general multiplier and normalisation above.
- **F03 (blocking), done.** The S24 `.msg` now reads: "양수 $a, b$에 대해 … $\log\frac{a+b}{2}$가 함수값의 평균 … 보다 크거나 같다(등호는 $a = b$일 때)."
  - This agrees with the slide's ≥ and $a, b \gt 0$, and with the detail text, which says equality holds only at a = b.
  - Rendered at 430 px; 0 KaTeX errors in the whole note.
- **F04 (preference), taken.** In the reduced-motion fallback (`.ym-demo.is-static`), the demo buttons are hidden by one local CSS rule, matching the print behaviour. Forced playback was not added.
  - CDP check with reduced motion: static frame shown, both buttons computed `display: none`, deck stays on 13 / 24.
  - Normal mode still passes the pause and resume check.

## Other changes

- The extra CSS line shifts the deck by one line from line 116 on. All leaf and root `OUTLINE.md` pointers are updated to match.

## Checks

- `lint-deck.py` passes for the deck and the note.
- `outline-lint.py`: 0 stale pointers. The 5 warnings are inherited and unrelated.
- Render: pages 21–23, and the note at 430 px.
- CDP: the reduced-motion run and the normal controls run both pass.
