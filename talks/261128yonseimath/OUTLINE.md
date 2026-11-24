# 261128yonseimath/ — 연세대 과학영재교육원 수료식 특별강연 (2026-11-28)

One Korean deck, 25 minutes, for the graduation ceremony of Yonsei's 과학영재교육원.
Speaker: Albert No (노알버트), an alumnus of the program. Audience: middle-school students
who can follow university-level mathematics, plus families and teachers. **Concept-first**
(DESIGN_SYSTEM §5): example → intuition → qualified claim; no tech supplement.

Thesis (a viewpoint, not a measured fact): AI의 발전은 수학 학습의 종말이 아니라, 이해한
수학으로 더 많은 질문을 탐색할 기회다. The deck never claims intuition is exclusively
human or that AI only calculates.

| Deck | Slides | Companion |
|---|---|---|
| `261128yonseimath.html` | 24 | `261128yonseimath-note.html` (Korean script, 24 articles, pacing table) |

Built by pipeline job `2026-11-24-261128yonseimath-draft` (plan-v2). Slide IDs are
`data-slide-id` on each slide div and note article. **Display order ≠ ID order** at the
end: …S20, S23, S24, S21, S22 (the AM–GM/Jensen pair was inserted before the close).

## Sections

| # | Section | Slides (display) | IDs | Lines | Time |
|---|---|---|---|---|---|
| — | Title · contents | 1–2 | S01–S02 | `:101-146` | 1:10 |
| 01 | AI 이후의 수학 | 3–8 | S03–S08 | `:148-250` | 4:50 |
| 02 | 글에 숨긴 확률 | 9–17 | S09–S17 | `:252-438` | 11:00 |
| 03 | 직관과 함께 커지는 가능성 | 18–24 | S18–S20, S23, S24, S21, S22 | `:440-556` | 7:00 |

Plus 1:00 buffer = 25:00.

## Slide pointers

- `:158` S04 IMO 2025, Gemini Deep Think 35/42 (gold-medal standard; scope line).
- `:180` S05 Navier–Stokes: OpenAI announcement 2026-09-08 → Clay response 2026-09-11; "발표와 최종 인정은 별개".
- `:235` S08 이해 → 정식화 → 검증 (coin); reused verbatim as the frame of S17 (`:422`).
- `:262` S10 removable tag vs generation-time trace; EU AI Act Art. 50(2), Korea AI 기본법 제31조 as social motivation only.
- `:285` S11 next-token toy distribution 김밥/라면/국수/샐러드 = 40/30/20/10 (invented, E20).
- `:305` S12 shared, context-dependent grouping rule (green-list idea, Kirchenbauer et al. ICML 2023).
- `:336` S13 boost ×1.5 + renormalise → 48/24/16/12; marked mass 50% → 60%.
- `:361` S14 100 coins, 70 heads; `:381` S15 exact Binomial(100, ½) PMF, tail P(K≥70) ≈ 0.0039% (note has exact value and z = 4).
- `:401` S16 limits (editing/translation/short text; no trace ≠ human); ICLR 2024 reliability paper. SynthID is in the note only.
- `:450` S19 question loop; note works "10번 중 7번" (176/1024).
- `:470` S20 Albert's own reflection (C24): 수학을 말로 이해하는 훈련, 직관.
- `:487` S23 AM–GM as fixed-sum balance, rectangles 2×8 vs 5×5.
- `:515` S24 log concavity: chord of y = ln x between 2 and 8, ln 5 > ln 4; "Jensen 부등식의 log 경우" (Boyd & Vandenberghe §3.1.8–3.1.9).
- `:536` S21 three questions + answer to the title; `:553` S22 closer.

## Figures (`figs/`)

`figs/generate-figures.py` writes all four SVGs and asserts their invariants; all text labels
are HTML overlays in the deck (positions printed by the script).

| File | Slide | Content / invariant |
|---|---|---|
| `coins-100.svg` | S14 | 10×10 coins, exactly 70 heads (rows 1–7) |
| `binom-pmf.svg` | S15 | exact Fraction PMF, n = 100; k ≥ 70 red; tail = 0.00003925069822796835 |
| `rectangles.svg` | S23 | 8×2 and 5×5 unit grids; a+b = 10, products 16/25, ab = 25 − (a−5)² |
| `log-chord.svg` | S24 | y = ln x on [1, 9]; chord 2–8; midpoint ln 4 < ln 5; curve above chord on (2, 8) |

S11/S13 bars are HTML; the generator checks their numbers (E20).

## Local CSS

`:17-93`, prefix `ym-`: Korean weight 400 and `keep-all`; cite moved bottom-left;
`.ym-flow` (larger flow boxes; `.ym-4` / `.ym-row` variants at 1.5rem), `.ym-fig` overlay
labels, `.ym-imo`, `.ym-big`, `.ym-text`/`.ym-tag`, `.ym-bars`/`.ym-pair`, `.ym-chip`,
`.ym-row`, `.ym-coins`, `.ym-out`, `.ym-return`, `.ym-amgm`.

## Related decks

The watermark mechanism and its z-test are taught formally in
`courses/privacy/lectures/06-watermark/watermark.html:245-592` and conceptually in
`courses/trustworthy-ai/` lec11 (S15–S20). This talk reuses only the idea
(sampling → grouping → counting) with its own lunch and coin examples.
