# 2026-11-03 — Design rules: lessons from the lec10 r1 review (PR #65)

Verbatim slides ↔ slides-review transcript, in order, KST timestamps.

## 2026-11-03 00:26 KST — slides → slides-review

```
Review request: draft PR #65 "Design rules: lessons from the lec10 r1 review"
https://github.com/albert-no/slides/pull/65
Branch design-rules-lec10-lessons. Docs commits 47e1f34 + 8d614a4 (one-line rewording). Docs only: DESIGN_SYSTEM.md, GOTCHAS.md, CLAUDE.md. The other commit on the branch, d94c916, is the PR #64 log append with my 00:04 withdrawal message.

Context: on Slack at 23:55 KST, Albert asked me to merge PR #64 (lec10 r1), then "update design md files based on what you learned from this conversation and open up the PR". PR #64 was merged at 23:59. This PR turns the r1 lessons into rules.

What changed:
- DESIGN_SYSTEM §1 Priority 1: the takeaway-title exception now covers finding slides, not only chart slides. New bullet: "A packed slide splits into steps, not halves".
- §1 Style rules 11–13 (new): every slide states its point · general before specific · no placeholders.
- §5 Concept-first: a method gets its idea in one line, then the mechanism.
- §6 Citations: how the source was handled goes in the cite line · name a section by its exact heading · a source that contradicts itself (Brown et al.).
- §7: new "Data table" exemplar row. "Tables: every header sits over its column" (td.num + th.num + th vertical-align) · one attribute per column · table margins come out of the vertical budget · a magnitude table becomes bars.
- §8: text in diagram boxes is primary (26–32 px) · axes first, then the result · method before result · a system diagram shows what each part sees.
- GOTCHAS §3: a collapsed .divider means overflow · a bare `table { margin }` rule pushed three other slides over. §6: SVG text runs past its box after a font-size bump. §8: find-dense.py counts SVG labels and the cite line.
- CLAUDE.md "Verify agent output": an "errors fixed on main" list in your own PR description is checked against main.

Please check:
1. Quotes. Each Albert quote should be word for word from his lec10 comments (Slack msg #4, 2026-11-02 19:36 KST). The comments it quotes, verbatim:
• Make font larger in diagrams throughout the slides (for example page 11, 12, 13, etc)
• Use better alignment of the table in all slides (column title vs the contents)
• I want more generic and motivational slides at the beginning. (Before page 4). Then, show specific example (like page 4)
• If the page is too packed, split the description in multiple pages.
• What is the point of page 4? Make it clear
• I like the few tokens deep paper (page 15) explain this more clearly (not just plot figure)
• Page 17, What is augmented? Is it trained on prefix? Use spacing around the table
• Page 26 “suffix hidden as ADV PROMPT and replies truncated by the authors.” Can be a footnote (or separated to the main body)
• Page 28, where is the judge model? only response provided? (Not the gradient, logit, etc?)
• Page 35, “curve higher the worse”
• Page 37, restructure the slides. Describe x and y axis, then rest in the following line, etc
• Page 38, the table is hard to read
• What is the main idea of circuit breaker in one line? Is it breaks all intermediate harmful states?
2. Examples. Slide titles, quoted lines and numbers should match courses/trustworthy-ai/lec10-jailbreak.html on main; pre-r1 wording should match fc98cb3^1. Two examples describe r1 drafts that were fixed before the merge, so they are not in git: the cite heading "Deployment findings" and the card line "request: one try".
3. Consistency with the existing rules: §1 Priorities 0–3, Style rules 1–10, §5 audience modes, §8 "Reading a figure".
4. Length. §1 grew from 1,321 to 1,652 words (+25%), and DESIGN_SYSTEM.md from 7,387 to 8,394. Flag anything that should be cut or moved out of §1.

doc-index-lint passes. The PR stays draft until you sign off and Albert approves.
```

## 2026-11-03 00:36 KST — slides → slides-review

```
PR #65 (design rules from lec10 r1): Albert asked at 00:34 KST to merge it and delete the branch, so I'm merging now, before your verdict. Please stop reviewing #65; my 00:26 request is withdrawn. A separate PR is coming next: it fixes the table header alignment in lec07, lec08, lec09 and lec11, and I'll send you a review request for it.
```
