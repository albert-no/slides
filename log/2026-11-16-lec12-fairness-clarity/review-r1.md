# Review round 1 — lec12 fairness clarity

- Job: 2026-11-16-lec12-fairness-clarity
- Baseline: `6f5088cdfc7877ea7965b972df91c8447562b5f4`
- Reviewed commit: `f6c0205ff9ebff33b52e205c87765ba3a3a674e8`
- Verdict: **revise**
- Round: 1 of 2. The next review is the final normal round.

## What matters

The new teaching sequence works: the approval/missing-outcome distinction, denominator windows, calibrated-score mixture, and same-sign-gap counterexample directly answer Albert's questions. Keep those exhibits and the 90-minute allocation.

Seven localized corrections remain. The most important are the wrong incompatibility implication in the S80 note, the conflation of calibrated equalized-odds with the ordinary equalized-odds procedure, and notes-wide horizontal scrolling caused by S38's table. The other fixes remove misleading short statements or name the plotted metric correctly. No new section, slide or literature survey is requested.

## Blocking findings — self-contained work order

All line numbers refer to the reviewed SHA. “Note” means `courses/trustworthy-ai/lec12-fairness-note.html`; “main” means `courses/trustworthy-ai/lec12-fairness.html`.

1. **F01 | S79 / p23 | fact | blocking.** Note `courses/trustworthy-ai/lec12-fairness-note.html:418`, Message: “The four rates differ only in their denominator” is false; the numerators here are 4, 3, 1 and 3. **Replace the Message with:** “Each rate specifies whom we count and which outcome we count within that population. Group A gives selection 4/10, TPR 3/6, FPR 1/4 and precision 3/4.” Keep the correct table/formulas. **Reason:** the summary must not teach that all four share a numerator. Evidence E08.

2. **F02 | S80 / p27 | fact | blocking.** Note `courses/trustworthy-ai/lec12-fairness-note.html:511`, “nor whether they can hold together; Section 03 shows when they cannot” makes the later theorem about these three rows (DP, opportunity, odds). They can all hold, including with unequal base rates. **Replace that paragraph with:** “This table identifies the populations compared by the three rules; it does not choose a rule. These three can hold together, for example when approvals are random and independent of group and outcome. Section 03 instead examines equal PPV together with equal FPR and FNR, and states the conditions that make that combination impossible.” **Reason:** distinguish the summary-table rules from the actual impossibility triple. Evidence E21, E10. No main-slide theorem or new counterexample slide is needed.

3. **F03 | S76 / p70 | fact | blocking.** Note `courses/trustworthy-ai/lec12-fairness-note.html:1394`, “Calibrated equalized odds does the same starting from calibrated scores” incorrectly implies the same LP and same two-error guarantee. **Replace only that sentence with:** “Calibrated equalized-odds post-processing randomly replaces some scores by the group's base rate to match a chosen generalized-error cost while preserving calibration, when feasible. This is a relaxed constraint on scores, not a general guarantee of equal thresholded FPR and FNR.” Add the Pleiss primary citation with §3 Definition 1, §4/Eq. (3)/Algorithm 1 to this article. Keep the nine names and stage grouping on the main slide. **Reason:** otherwise this method appears to bypass the conflict just taught. Evidence E19. This clarifies an existing method, not an expansion of the lecture's argument.

4. **F04 | S49a / p77 | fact | blocking.** Note `courses/trustworthy-ai/lec12-fairness-note.html:1532`, Message ends “an answer that picks one follows religious identity, not evidence.” **Replace that clause/sentence with:** “Picking either man goes beyond the supplied evidence; systematic stereotype-aligned choices are what the benchmark tests.” Preserve the definition and correct answer Unknown. **Reason:** an unsupported answer alone does not identify its cause; the longer script already treats religious stereotyping as a concern to test, not an inference from every error. Evidence E22.

5. **F05 | S50a / p79 | fact | blocking.** Note `courses/trustworthy-ai/lec12-fairness-note.html:1591`, the last sentence of Boundaries (“A score of 0 says only that the non-Unknown answers do not lean…”) contradicts the all-Unknown case immediately before it. **Replace that sentence with:** “Zero can mean balanced non-Unknown answers or, in the ambiguous condition, no non-Unknown answers at all. Zero bias alone does not establish accuracy.” Keep the preceding disambiguated undefined-score qualification and the main slide's correct all-Unknown → 0 line. **Reason:** all layers must agree on what the score means. Evidence E22.

6. **F06 | S44b / p72 | fact | blocking.** Main `courses/trustworthy-ai/lec12-fairness.html:2093–2107`, especially line 2104: “accuracy ≈0.745” names the wrong/ambiguous metric, and the cropped plot has no y-axis title. **Change** “accuracy ≈0.745 both” → “balanced accuracy ≈0.745 both”; identify **y = balanced accuracy** on this slide without relying on the preceding slide. **[judgment]** A compact axis key or external label is slides' choice; retain body-size explanatory text and do not shrink the figure to add prose. The note already names balanced accuracy correctly. **Reason:** ordinary accuracy and balanced accuracy differ; the plotted quantity must be explicit. Approximate numbers are accepted (E20).

7. **F07 | S38 / p57 | design rule | blocking.** Note `courses/trustworthy-ai/lec12-fairness-note.html:1103–1109`, five-column weight table: at a true 430px viewport its right edge is about 542px, causing horizontal scrolling for the entire notes document. This is **pre-existing, not a regression**, but the revised notes still fail DS §9's narrow-viewport acceptance. **[judgment]** Reformat these four rows as vertically stacked records/lists, preserving expected share, observed share, exact weight and weighted count for each cell; retain the exact-2/3 explanation. Do not shrink the font or hide clipped columns. **Reason:** the lecturer must be able to read the whole note at the specified narrow width. Verify at 430px through viewport emulation rather than a headless window-size minimum; exclude hidden KaTeX MathML when checking overflow.

## Coverage of Albert's comments

“Not done” below means the specific corrections above remain, not that the requested section was omitted.

| Comment | Status | Revised location / disposition |
|---|---|---|
| C01 | Not done | Main/notes revision implemented; F01–F07 and final approval/PR remain. |
| C02 | Done | S77 removed; no unsupported controlled identity-swap claim retained. |
| C03 | Done | S51a p5 supplies the sourced occupation example; the unavailable X post is not represented as verified evidence. |
| C04 | Done | S74/S51a/S78 pp4–6 distinguish decisions, stereotyped portrayal and normative judgment. |
| C05 | Done | S04a/b pp7–8 and S54a p84 connect lower cost at comparable illness to missed extra-care priority; no sole delayed-care mechanism asserted. |
| C06 | Done | S07 p11 names benchmark tasks and evaluation, not vendor training data. |
| C07 | Done | S12a/b pp17–18, S13a–d pp19–22; approval versus prediction and stipulated versus missing outcomes explicit. |
| C08 | Not done | S79/S80 summary tables and S16 navy-box answer implemented; F01/F02 correct their notes. |
| C09 | Done | S17a p28: shared FPR/TPR point. |
| C10 | Done | S17b p29: same TPR height, FPR free. |
| C11 | Not done | S20a p16 now precedes the example; S12b/S79/S80/S81 expand foundations. F01/F02 remain in summary notes. |
| C12 | Done | S14–S16 pp24–26 and S80 p27 carry plain-language one-line criteria. |
| C13 | Done | S21b p36 explains maximizing profit within the equalized-odds constraint, including segment randomization. |
| C14 | Done | S23a p38 and S27 p44 identify Northpointe as COMPAS developer. |
| C15 | Done | S29 p46 defines recorded-rearrest base rate, distinguishes denominator and labels synthetic rates. |
| C16 | Done | S30 p47 explicitly rejects a universally golden FPR. |
| C17 | Done | S32a p49 and S33 p52 make recorded rearrest and the flag distinct. |
| C18 | Done | S32b/S82 pp50–51 provide incompatible and compatible constructions, with conditions and note edge cases. |
| C19 | Done | S40a/b pp60–61: repeated cost-sensitive fits, not an extra detector. |
| C20 | Done | S75/S83 pp62–63: suitable candidate pool, cost steering, same-sign gaps cannot cancel. |
| C21 | Done | S84 p64 gives protocol; S41a/b pp65–66 give curve readings and scoped comparison. |
| C22 | Done | S43a/b pp68–69 distinguish constrained modeled lender profit from social welfare; loss is weak, not necessarily strict. |
| C23 | Not done | Nine alternatives and separate before/after baselines clear in S76/S44a/b pp70–72; F03/F06 remain. |
| C24 | Done | S45 p73 and S54a p84 distinguish improving a rate from validating its recorded target. |
| C25 | Not done | S49a/b/S50a/b pp77–80 now define context sufficiency plainly; F04/F05 remove residual note overclaims. |

## Decisions on slides' reported plan issues

- Accept the approximate Figure 5(b) DI/accuracy readings and Agarwal Figure 1 readings after independent source-page inspection; E20 records their precision and limits. If retaining “roughly one point” in the S41a note, prefer the unambiguous unit “roughly one percentage point” (wording preference, nonblocking).
- Accept allocation of per-slide times to the agreed section totals and S45 at one minute. Independently summed totals: **10 / 25 / 15 / 20 / 13 / 7 = 90**.
- Accept leaving S54b/S55 sparse: the maps have a purpose and bottom whitespace is allowed. Do not add filler.
- S17a/b, S50b and other image changes inspected at slide size; the enlarged external keys preserve the explanatory content. Do not treat unchanged CSS font-size as sufficient evidence about raster readability in future checks.
- The retired images can remain unreferenced; no deletion requested.
- **Plan-v1 remains the argument/scope specification.** E19–E22 refine source interpretation and record review decisions; this review supplies the localized corrections. No plan-v2, new slide or timing change is required.

## Independent checks and limits

- Read exact-SHA content and baseline-to-target diff; extracted the exact archive for browser review. No deck, note, figure generator or shared-style files edited by slides-review.
- 87 unique main IDs and 87 note IDs in identical order; substantive titles match; tech file untouched; local asset/reference paths resolve. Section timing totals 90 minutes.
- Read all main-slide text and every substantively revised note article, with retained surrounding explanations; compared the requested concepts against primary sources and the original comments, not merely the plan.
- Chromium: all 87 main pages rendered at 1280×720 and visually reviewed as a sequence, with full-size inspection of dense/changed plots and tables. No broken image, KaTeX error, clipping or footer overlap found in the main deck.
- Notes: all articles checked for DOM overflow at 1100px and 430px. Inspected revised openings at both widths, including S04b, S07, S12b, S79–S84, S40a, S44b, S50a and S54a. S38's visible table is the sole detected narrow-overflow cause (F07); not hidden MathML.
- Main lint: no errors or font warnings, same 30 hardcoded-color occurrences as baseline. Notes lint: clean. Wordy check: three 16-word keys, accepted under plot-key/qualifier exceptions.
- Outline lint in the extracted tree: one **pre-existing environment-specific missing pointer**, OUTLINE.md line 332 to `/workspace/agent/lec09/r4/build_deck.py`; no lec12 pointer error. Do not alter the unrelated lec09 record for this job. This qualifies work-r1's “0 stale pointers” result on slides' own filesystem.
- All 22 `criteria_examples.py` generated fragments evaluated and match the inlined fragments; calibrated-count assertions and both mixture/gap assertions pass. Fig. 4's historical generator remains unrecovered, as documented; no claim to have validated that unavailable pipeline.

## Round 2 handoff

Implement F01–F07 only, plus any necessary paired explanation/outline synchronization. Keep all other approved content stable. `work-r2.md` must answer every finding ID and give the exact pushed commit. Recheck the changed main slide and neighbours, changed note articles at desktop/430px, and notes-wide horizontal width. The final normal review will target those changes and their neighbours, not restart the entire lecture review. No PR or merge is authorized at this stage.
