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
| `261128yonseimath.html` | 25 | `261128yonseimath-note.html` (Korean script, 25 articles, pacing table) |

Built by pipeline job `2026-11-24-261128yonseimath-draft` (plan-v2); polished by
`2026-11-25-261128yonseimath-polish` (plan-v1, author comments C01–C19); final edits by
`2026-11-25-261128yonseimath-final-edits` (plan-v1, C01–C06). Slide IDs are
`data-slide-id` on each slide div and note article. **Display order ≠ ID order**: S02
(contents) and S16 (limits) are retired; S10 split into S10a/S10b; S25 (image parity) sits
after S10b; S26 (speaker intro) sits after S01; the close runs …S20, S23, S24, S21, S22.

## Sections

| # | Section | Slides (display) | IDs | Lines | Time |
|---|---|---|---|---|---|
| — | Title + speaker intro | 1–2 | S01, S26 | `:164-189` | 1:10 |
| 01 | AI 이후의 수학 | 3–8 | S03–S08 | `:194-290` | 5:00 |
| 02 | AI가 쓴 글에 보이지 않는 표식 남기기 | 9–18 | S09, S10a, S10b, S25, S11–S15, S17 | `:295-483` | 11:00 |
| 03 | 직관과 함께 커지는 가능성 | 19–25 | S18–S20, S23, S24, S21, S22 | `:488-600` | 6:50 |

24:00 of speech plus 1:00 buffer = 25:00.

## Slide pointers

- `:176` S26 speaker intro: five year-free milestones (영재원 심화반·사사반 → SNU EE/수리과학 → Stanford EE MS/PhD → 홍익대 조교수 (전) → 연세대 AI 부교수), vertical timeline.
- `:204` S04 IMO 2025 Gold Medal: Gemini Deep Think 35/42, gold-medal standard (official grading).
- `:218` S05 Navier–Stokes: OpenAI vortex figure (original, `figs/navier-stokes-vortex.png`), "OpenAI의 해법 발표" 2026-09-08; Clay 2026-09-11 is note-only context.
- `:234` S06 solving vs researching (Tao, "Math 2.0", 2026-10-09, PDF p. 16; three questions are the speaker's).
- `:259` S07 계산기 → 컴퓨터 → AI; `:277` S08 무엇을 만들까 → 수학 문제로 → 구현; its frame returns in S17 (`:469`).
- `:305` S10a hypothetical 독서 감상문 (motivation); `:323` S10b visible tag vs invisible trace.
- `:347` S25 image parity: grayscale NASA Blue Marble vs all-odd copy (odd 18.37% → 100%, max diff 1).
- `:367` S11 next-token toy distribution 김밥/라면/국수/샐러드 = 40/30/20/10 (invented).
- `:395` S12 looping left-to-right green-list demo (`figs/watermark-demo.js`; ~40 s loop, P/R keys, static frame for print/reduced motion); dgMARK = visual style only.
- `:414` S13 50/50 → 60/40 (chosen) vs 100% green (awkward).
- `:436` S14 100 coins, 70 heads; `:450` S15 exact Binomial(100, ½) PMF, tail P(K≥70) ≈ 0.0039%.
- `:469` S17 wish → 수학문제화 (bias) → 통계 문제; limits (old S16) moved to its note.
- `:498` S19 문제 (LLM 문장에 표식 남기기) / 아이디어 (의도적인 통계 삽입) above the idea ↔ AI implement/experiment ↔ new idea loop; note works "10번 중 7번" (176/1024).
- `:521` S20 Albert's reflection: 공식·기법 → 말로 설명하기 → 의미와 직관 (flow only).
- `:538` S23 AM–GM as fixed-perimeter area: among rectangles with perimeter 2(a+b), the square of side (a+b)/2 has the largest area; ab ≤ ((a+b)/2)², equality a = b. HTML boxes at one scale (36 px/unit, a=2, b=8; no numbers shown).
- `:562` S24 log concavity: chord of y = ln x, "Jensen 부등식의 log 경우" (Boyd & Vandenberghe §3.1.8–3.1.9).
- `:582` S21 answer: 직관으로 이해 → 현실에 적용 (two boxes, no sub-captions); `:597` S22 closer.

## Figures (`figs/`)

`figs/generate-figures.py` writes the SVGs, the parity PNG and the demo data, and asserts
their invariants; text labels are HTML overlays in the deck.

| File | Slide | Content / invariant |
|---|---|---|
| `navier-stokes-vortex.png` | S05 | OpenAI announcement image, stored unmodified (1254×1254) |
| `image-original-gray.png` | S25 | NASA Blue Marble 2002 (North America print), 8-bit gray, 1024×574 |
| `image-all-odd.png` | S25 | even values +1; odd 100%, 479,789 pixels changed, max diff 1 |
| `watermark-demo-data.js` | S12 | 4 steps × 4 candidates, ×1.5 green then ÷1.25; step 2 picks red 친구와 |
| `watermark-demo.js` | S12 | demo player (phases, hold, controls, static frame) |
| `coins-100.svg` | S14 | 10×10 coins, exactly 70 heads (rows 1–7) |
| `binom-pmf.svg` | S15 | exact Fraction PMF, n = 100; k ≥ 70 red; tail = 0.00003925069822796835 |
| `log-chord.svg` | S24 | y = ln x on [1, 9]; chord 2–8; midpoint ln 4 < ln 5 |

## Local CSS

`:17-157`, prefix `ym-`: Korean weight 400 and `keep-all`; cite bottom-left; `.ym-mid`
(vertical centring under the title); flows, `.ym-fig` overlays, `.ym-imo`/`.ym-big`,
`.ym-ns`, `.ym-qs`, `.ym-text`/`.ym-tag`/`.ym-sheet`/`.ym-ask`, `.ym-imgs`, `.ym-bars`,
`.ym-demo*`/`.ym-w*`, `.ym-split`, `.ym-coins`, `.ym-path` (S26), `.ym-frame` (S19), `.ym-return`, `.ym-rect` (S23), `.ym-big-flow`.

## Related decks

The watermark mechanism and its z-test are taught formally in
`courses/privacy/lectures/06-watermark/watermark.html:246-593` and conceptually in
`courses/trustworthy-ai/` lec11 (S15–S20). This talk reuses only the idea
(sampling → grouping → counting) with its own lunch and coin examples.
