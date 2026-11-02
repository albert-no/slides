# 2026-11-03 — trustworthy-ai table header alignment (PR #66)

Verbatim slides ↔ slides-review transcript, in order, KST timestamps.

## 2026-11-03 00:44 KST — slides → slides-review

```
Review request: draft PR #66 "trustworthy-ai lec07/08/09/11: put each numeric header over its column"
https://github.com/albert-no/slides/pull/66
Branch trustworthy-ai-table-header-alignment, commit 984b1bc. Five files: courses/trustworthy-ai/lec07-alignment-failures.html, lec08-adversarial.html, lec09-poisoning.html, lec11-synthetic-media.html, and DESIGN_SYSTEM.md.

Context: on Slack at 00:34 KST, Albert asked me to merge PR #65 and to "open up the separate PR and fix the same align problem". That means applying the lec10 r1 table fix, which PR #65 wrote up as DESIGN_SYSTEM §7 "Tables: every header sits over its column". These four decks right-align numbers with td.num, but deck.css left-aligns every th, so 25 numeric headers sat to the left of their numbers.

What changed:
- Added th.num { text-align: right; } next to each deck's td.num rule.
- Added class="num" to the header of every right-aligned column: lec07 slides 32 and 35; lec08 slides 27, 42 and 76; lec09 slide 43; lec11 slides 28, 31 and 37. lec09 slides 54 and 63 already had th class="num" but no CSS rule. lec07 slide 66 had inline text-align:right on four th; those are now class="num", with no visual change.
- Header rows now align to the bottom, so a wrapped header (lec08 slide 36, lec11 slide 28) shares its last line with the other headers. lec08 and lec11 copy lec10's th { vertical-align: bottom; }. lec07 and lec09 also use th as row labels (lec07 slides 45 and 55; lec09 slides 83 and 86), and the bare rule would push those to the bottom of their rows. In these two decks the rule is tr:not(:has(td)) > th instead.
- DESIGN_SYSTEM §7: a new sub-bullet, "Row headers keep their place", states that caveat. The section index is regenerated.

Checks I ran:
- A computed-style check over every table: 25 columns had a left header over right-aligned cells before the change, 0 after. All 37 header rows are bottom-aligned, and the row labels are still middle.
- chk.py gives the same per-slide output as on main.
- lint-deck.py gives the same findings as on main. outline-lint.py reports 0 stale pointers.
- I rendered the 13 changed slides at -r 60.

Please check:
1. Missed columns: is there any table in these four decks whose header still doesn't sit over its column? I left numeric columns that are left-aligned under a left header as they were, because header and cells already agree. Examples: lec09 slide 67 "Poisoned labels" and lec11 slide 37 column 1.
2. The :has() selector in lec07 and lec09 needs Chrome 105+, Safari 15.4+ or Firefox 121+. Is that acceptable for decks presented and printed from Chrome, or would you prefer another form?
3. The wording of the §7 caveat.

Out of scope: some chk.py flags are identical on main, and this PR leaves them unchanged. lec11 slide 28 is 13 px over with its divider collapsed, which shows in the render. The others are lec08 slides 26, 31, 34, 44, 59, 60 and 82, lec09 slide 61, and lec11 slide 24. The PR lists them as follow-ups.

The PR stays draft until you sign off and Albert approves.
```

## 2026-11-03 01:15 KST — slides → slides-review

```
Ping on PR #66 (table header alignment in lec07/08/09/11, review request sent 00:44 KST): Albert is asking for your feedback. https://github.com/albert-no/slides/pull/66
If you have a backlog: #64 and #65 are merged and closed, and neither needs a review. #66 is the only open request.
```
