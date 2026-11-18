# work-r2 — job 2026-11-18-prob09-oracle-tails-softmax

Response to `review-r1.md` (reviewed 74ee811). Same branch; 70 slides, IDs and order unchanged.

## Findings

| ID | Action |
|---|---|
| F01 (S132, p47) | Done as preferred. Removed the stacked bar and its caption, and the logits row. The slide keeps the defining line, a table (outcome header, masses 1/2/4 with red "sum Z = 7", probabilities 1/7, 2/7, 4/7 with 4/7 in blue, "sum 1") and the scope highlight. Table row gap widened 4 → 12px; type unchanged. Unused `.p9g-bar`/`.p9g-barcap` CSS removed. The logits 0, ln 2, ln 4 now appear only in H/M ("Reading the table" / explanation); M Slide description rewritten to match. |
| F02 (S133, p51) | Removed the general ratio; the math-block now starts at μ̂_SN = 3(4+4)/3(1+4+4) (3s cancelled) = 8/9 ≈ 0.89 vs μ = 4/7 ≈ 0.57. That alone left the slide 727/720 px, so the caption moved beside the three draw boxes inside the same flex row ("One illustrative batch; blue C draws feed the numerator", two lines at body size). The lead line, A/C/C batch and takeaway are unchanged. H/M now say that the slide applies the SNIS formula of 50 to these numbers. |
| F03 (S64, M) | "A return arrow is labelled" → "The red line beneath the flow reads". |

## My r1 miss

My r1 render check read the PDF page for S133 as clean and missed the 14px overflow and the collapsed divider. In r2 I checked every slide in screen mode at 1280×720: each slide was made active in turn, and I compared scrollHeight with clientHeight and checked the divider's height. The probe reproduced F02 on 74ee811 (S133 734/720) and now reports no slide over 720px and no zero-height divider.

## Integration

- `courses/deepmath/OUTLINE.md`: line pointers shifted (CSS −4, S132 −3) were updated to 113/173/516/792/1022/1357/1566 and theorems 605/833, each checked with `sed -n`. Text unchanged; the Part 04 row never described the bar.
- Copied `review-r1.md` unchanged, and refreshed `job.md` (`requests.md`, `evidence.md` and `plan-v1.md` are unchanged).

## Checks

- `lint-deck.py`: deck and H note ok. `lint-accessible-md.py`: 23 warnings, the baseline count (one new "on the slide" phrase reworded). M is ASCII.
- D/H/M parity: 70/70/70, identical order. `outline-lint.py`: 0 stale/missing.
- Overflow probe (above): no slide exceeds 720px.
- Rendered at `-r 60`: pp47 and 51 read, both clean. p47 now has empty space below the highlight; I accepted it as the cost of the single-exhibit fix.

## Plan issues

None. No changes to the opening, the tail/oracle content or RL.
