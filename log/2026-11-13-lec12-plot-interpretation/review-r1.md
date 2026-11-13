# Review r1 — 2026-11-13-lec12-plot-interpretation

reviewed commit: d9de699ea36020761939ddf25c16c4c3ea112781
baseline: 0d2c05c9ad02635c0407010f15bcca5428bac949
verdict: revise
round: 1 of 2

## Main result

The COMPAS split and the explicit score-versus-cutoff readings are materially better. Keep the score-6 example, the three separate denominator explanations, the approximate-reading labels, and the honest photo thought experiment. The remaining priorities are (1) finish the second opening visual, (2) qualify the randomization claim correctly, and (3) make the charts themselves readable rather than relying on their prose explanation.

## Request coverage

| Comment | Result | Reviewed pages / IDs |
|---|---|---|
| C01 | pending: revision not yet approved; no PR | all target pages |
| C02 | partial: comparison improved, but factual qualifier and density need correction | 29–30, S21a/b |
| C03 | done: concrete context and audit-label example, no automatic-detention claim | 32–33, S23a/b |
| C04 | partial: much clearer interpretations, but essential plot labels remain too small | 35–37, S25/S26a/S26b |
| C05 | partial: first photographic hook done; CEO hook missing | 4, S77; S78 absent |

## Findings

All paths are repo-relative and line numbers refer to the reviewed commit. Content/design/wording decisions marked [judgment] belong to slides, not a context-free implementation agent.

| ID | Slide ID / page | Type | Blocking | What is wrong | Concrete fix |
|---|---|---|---|---|---|
| F01 | S78 / absent, intended after current p4 | unmet request | yes | Only one opening example shipped; the image request produced no output. Dropping the second example is not the approved scope. | [judgment] Follow plan-v3's sourced CEO alternative: Wan & Chang ACL 2025 Figure 1 top-row CEO example, exact historical prompt, model/year and “published example, not a new run”. Add S78 and matching note, then update all counts/pacing/pointers. No credential change or repeat of the denied generation request is needed. |
| F02 | S21b / p30 | fact | yes | `courses/trustworthy-ai/lec12-fairness.html:627–628` says the probability is “not 50/50” and equal errors “need” a randomized rule. Equality alone allows trivial deterministic rules; the plot's utility-optimal solution is the relevant scope. The note repeats both claims at lines 484/486. | [judgment] Highlight → “The profit-optimal equalized-odds rule randomizes here.” Qualifier → “Fitted probability, not necessarily 50/50.” Keep the non-confidence-interval distinction. Use “probability”, not “odds”, for acceptance chance. In the note explicitly distinguish this optimum from feasibility (e.g. always-reject is equalized odds but generally not profit-optimal); align its takeaway. E13 corrects the owner's earlier under-qualified plan wording too. |
| F03 | S25/S26a/S26b / pp35–37 | design rule | yes | `courses/trustworthy-ai/lec12-fairness.html:757–822` retains chart-plus-large-prose-column layouts. At 1280×720 the selected decile/cutoff digits, scale ticks and source axis text are roughly 12–15 pixels; p36/37 plots occupy only about a third of the width. Students can read the answer but cannot comfortably read the evidence. | [judgment] Give each reading a figure-first page: concise x/y/encoding key, a large faithful chart crop, and one interpretation/limit. Remove redundant embedded plot titles/axis prose from the crop only when faithfully restated outside. Enlarge essential tick labels/selected-bin labels with external labels, or split an overview from a faithful zoom of the focal pair; retain the denominator and uncertainty. For S25 show the zero-prior comparison and interval; S26a decile 6; S26b cutoff 4 and pooled 5–10. Do not redraw bars from the approximate values. Inspect essential labels at final size, not just output resolution. |
| F04 | S21a/S21b / pp29–30 | design rule | yes | `courses/trustworthy-ai/lec12-fairness.html:592–631` renders about nine prose/key lines on each page, above the seven-line ceiling. New `.p12i-ann p { margin:0; }` at line 580 compresses prose rhythm. | [judgment] Remove the prose-spacing reduction. Compress row annotations, not type: S21a can use “Max profit: lender benchmark”, “Shared threshold: one cutoff for everyone”, “Demographic parity: same share approved”; retain the takeaway and axis-direction key. S21b can use “Opportunity: match TPR” and “Equalized odds: match TPR + FPR”, with the region rule and F02-qualified takeaway. If still over the line/element budget, split another teaching step. Keep the row crops/scale alignment and group encodings. |
| F05 | S77 / p4 | preference | no | The Armenian photographer name renders as missing-glyph boxes in the slide citation, although attribution is present correctly in the note and CC0 does not require it. | [judgment] Prefer a short legible slide cite such as “Photo: Wikimedia Commons, CC0 1.0, 2025; full credit in notes”, with the full original name and link retained in the note. No new fonts required solely for this. |

## Review checks

- Read the original comments C01–C05, checked source definitions and the source figures, then applied DS §§1/6/8/9/10 and the plan. Findings are not claims that the plan itself is evidence.
- Exact commit extracted with git archive into owner scratch. Independent Chromium render: 79 pages, 1280×720-equivalent geometry. Visually inspected pp3–5 and 28–38 individually, including all changed pages and immediate neighbours. No clipping/footer collision found; F03/F04 are legibility/density issues, not overflow.
- Main and notes have 79 identical ordered unique IDs; numeric note headings are in order. Pacing recomputation: 79 budgets sum to 90 minutes; every elapsed value agrees. Tech unchanged.
- Lint: main has the pre-existing 30 hard-coded-color warning; note passes. Independent outline lint has one pre-existing workspace-only lec09 script link (`OUTLINE.md:326`, `/workspace/agent/lec09/r4/build_deck.py` absent in this container), plus existing ambiguity warnings elsewhere. Do not fix unrelated lectures for this job. All diff changes in the course outline are lec12-related.
- Verified S77 source and CC0 metadata directly through Commons API; E12 records provenance. Do not repeat the work report's unsupported “no public figures” assertion as a fact.
- Approximate focal readings agree with the primary figure: FPR about .21/.10, decile-6 rearrest about .56/.58, cutoff-4 PPV about .63/.59. They must stay approximate and source/cohort-specific.
- Accept the executor's choice not to outline an individual Hardt segment; its endpoints remain visible and the group key is sufficient. This preference does not require another change.

## Plan issues resolved

Plan-v3 replaces unavailable live generation with a directly verified, actual published CEO output, preserving Albert's motivational example rather than dropping it. The photo is not newly generated and must not be presented as such. It also fixes the owner's randomization scope. Other accepted content stays; round 2 rechecks changed pages and neighbours only. Two-round limit remains in force.
