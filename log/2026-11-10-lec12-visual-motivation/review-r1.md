# Review r1 — revise

Job: `2026-11-10-lec12-visual-motivation`
Reviewed commit: `6d1e21cc4b484d0b6333ca8d2607b79e9ec9facf`
Baseline: `cd0da5ca7ad75ceef107d28ad110407f0c33b4ff`
ID-only commit: `a6d894b9b93f852af5ba6f22131663282339f3b3`
Round: **1 of 2** · Verdict: **revise**.

## What matters

1. **Keep the new explanations.** The shared lending people, exact 60-person calibration example, and reductions loop/mixture make the argument substantially clearer. Baseline p6 is repaired; baseline p40 is now readable and correctly connected. The extra splits are justified.
2. **Fix the integration damage and remaining readability shortcuts.** OUTLINE.md accidentally repeats whole lecture sections. Paper keys still use reduced prose, and two source crops cut labels.
3. **Correct the small but consequential interpretation errors.** The Bianchi matcher is not six intersectional prototypes; the care recap conflates equal scores with different selection and overstates what all rates inherit; calibration support needs explicit scope.

## Original-request coverage

| Comment | Done? | Evidence / remaining |
|---|---|---|
| C01 | Partial | Full main/notes/tech revision delivered, but shared outline and blocking findings remain. |
| C02 | Yes | Decision hook, shared lending counts, calibrated counts, randomized mixture, complete BBQ example, care-case synthesis. |
| C03 | Partial | Main custom-diagram labels, especially S40a/b, improved; reduced paper-key prose and cropped labels remain (F02/F03). |
| C04 | Yes | S06 return arrow and S40 loop visibly attached and directed correctly; whole-deck diagram scan found no additional broken arrows. |
| C05 | Yes | This is the visual/motivational job, not Albert's later detailed-edit PR. No PR or merge yet. |
| C06 | Yes | Correct target lec12; duplicated unrelated outline blocks must be removed, not developed. |
| C07 | Yes | Same job/baseline continued. |

## Blocking findings — numbered, self-contained

Paths and line numbers below refer to the exact reviewed commit, not a working tree. **Main** means `courses/trustworthy-ai/lec12-fairness.html`; **note** means `courses/trustworthy-ai/lec12-fairness-note.html`; **tech** means `courses/trustworthy-ai/lec12tech.html`. For each finding the full path is repeated so it can be handled independently. All wording/design choices marked [judgment] should stay with slides, not a context-free implementation worker.

| ID | Slide ID / page | Type | Blocking | Problem and concrete fix |
|---|---|---|---|---|
| F01 | Shared outline; all pages | design rule | yes | `courses/trustworthy-ai/OUTLINE.md`, lines527–1262: lec09/10/11 headings now occur three times each, lec12 four times (baseline had one each). Old 56-page and new 74-page lec12 sections coexist. Restore baseline content outside the intended lec12 entries; retain exactly one updated lec12 section and the necessary index/tech/figure-index edits. Recompute current pointers/counts. Reason: the authoritative navigation is contradictory even though the pointer-range lint passes. |
| F02 | S41a/S41b/S42/S43a/S44a/S44b, main pp52–55,57–58 | design rule | yes | `courses/trustworthy-ai/lec12-fairness.html`, lines1274–1275 and key instances1564,1583,1603,1620,1669,1692: `.p4-key p` shrinks prose to 1.25rem and overrides line-height/margins; the nine-method key plus final line also exceeds the seven-line ceiling on pp57–58. [judgment] Remove the prose-size/spacing rescue and redesign/split the keys at native body size. For S44, use staged highlighted-method readings with a legible complete key, or a dedicated figure-key step; keep all plotted data and preserve method attribution. Do not silently erase other methods or repaint the source plot. Reason: important explanatory labels must not be shrunk to fit, especially in this job. |
| F03 | S17a/S17b pp21–22; S39 p48 | design rule | yes | `courses/trustworthy-ai/lec12-fairness.html`, lines474–507 and1428–1438; assets `courses/trustworthy-ai/figs/lec12-visual-motivation/p2-hardt-fig1-eqodds.png`, `p2-hardt-fig1-eqopp.png`, and existing `courses/trustworthy-ai/figs/reweighing-aif360.png`: the Hardt top 1.0 tick is cut; S39 has truncated right-panel row labels and a clipped join at the two panels. [judgment] Re-crop from originals with all essential labels intact. Keeping a source panel heading is preferable to cutting its ticks; no painting is required. Split S39 into SPD and DI reading steps if necessary, with clear dataset/attribute labels and axes. Store replacement S39 crops under this job's figure directory rather than changing the shared old asset. Reason: source labels are evidence, not disposable decoration. |
| F04 | S51b p68 | fact | yes | `courses/trustworthy-ai/lec12-fairness.html`, lines1861–1883; `courses/trustworthy-ai/lec12-fairness-note.html`, lines1124–1135: “male/female × White/Black/Asian” implies six intersectional archetypes. E24/§2.2 describes two gender centroids and three race centroids, matched separately. [judgment] Replace the box with “Separate nearest matches: gender (2); race (3)” and explain separate category-family cosine comparisons in the note. Keep 99%/56% and the non-self-identification caveat. Reason: the visual must describe the actual measurement. |
| F05 | S54a p71 | fact | yes | `courses/trustworthy-ai/lec12-fairness.html`, lines1914–1949: “Sicker Black patients / left out at the same score” follows a common score cutoff and suggests race changes selection at an identical score. [judgment] Replace with “Black patients / need understated by cost”; retain the supported statement “At a given score, Black patients were sicker” in slide/note. Check `courses/trustworthy-ai/lec12-fairness-note.html`, lines1185–1200 for agreement. Reason: E01/E25 establish a proxy-need disparity, not different threshold decisions for equal scores. |
| F06 | S54b p72 / corresponding note | fact | yes | `courses/trustworthy-ai/lec12-fairness.html`, lines1952–1965; `courses/trustworthy-ai/lec12-fairness-note.html`, lines1205 and1213: “any rate … error rates or selection rates, inherits the gap” is too strong; selection rate does not condition on Y. The same note says “a false positive jails someone” before correctly distinguishing score from judge. [judgment] Main box: “Fairness on cost is not fairness on need.” Note: “Meeting a criterion on cost-based predictions does not establish equitable allocation by medical need; selection rate itself uses decisions, not Y.” Replace the detention sentence with “A false high-risk flag may influence pretrial detention; the judge, not the score, makes that decision.” Reason: avoid both a metric-definition error and an automatic score→detention claim. |
| F07 | S61b tech p6 | fact | yes | `courses/trustworthy-ai/lec12tech.html`, lines89–99: unrestricted “for all s,a” plus “Every conditioning event has positive probability” leaves support unspecified; the work report says discrete/binned is explicit, but it is not in the rendered slide. [judgment] Add “Discrete score values here” and restrict the equality to (s,a) with Pr[S=s,A=a]>0. Keep the equality to assigned score s. No continuous-score derivation requested. Reason: state the actual setting without suggesting every real score has positive mass (E28). |

## Nonblocking preferences / accepted residuals

- **F08 — preference, not blocking:** tech S60/p4, `courses/trustworthy-ai/lec12tech.html:67–69`: the four underbrace words are smaller than the surrounding equation. [judgment] Prefer a native-size denominator key or removing these redundant annotations; do not shrink the equations. The equations and main-deck denominator examples are readable, so this alone does not start a round.
- Blank lower space on S17b is acceptable. Do not fill it for its own sake.
- BBQ nested context borders are faithful to the source, not a broken diagram; keep them. The visible answer is correctly presented as the correct answer, not an observed model output.
- Tight caption spacing on tech pp15/19/21 is not an overlap in this render. No extra redesign requested solely for that.
- Hardcoded colors used to match source legends are acceptable; do not arbitrarily recolor paper encodings to satisfy lint.
- Style-block placement is not itself a blocker. Only actual prohibited sizing/spacing is F02.

## Plan issues and evidence decisions

- **Splits:** accept S17a/b, S44a/b, S50a/b and all reported tech splits. No fixed page-count demand.
- **Time:** exact 74 note allocations sum to 90; section totals 10/20/15/20/15/10. Keep S75. This is a plausible planned budget for staged examples, not a measured rehearsal. Do not move it off screen merely because the page count rose.
- **Theorem title:** accept “Calibration Plus Balance Forces Exceptional Cases”; plan-v1's shortened title was incomplete. Plan-v2 corrects it.
- **Calibration:** discrete support clarification accepted; F07 implements it. No extra theory requested.
- **Obermeyer caption details:** verified against Fig.1 caption, now E25. No source blocker.
- **Balanced accuracy / AIF360 read-offs:** the definition was already in E09. Approximate note values are compatible with the shown plot; keep them explicitly approximate, not exact experimental measurements. E26 records the distinction.
- **Bianchi:** new Fig.3 crops, §2.2 and Appendix C version are verified. E16's old §3 location was wrong; E24 supersedes it. Old backup asset is out of scope and remains unchanged. The method correction F04 still blocks.
- **FICO note:** qualitative Fig.9 observation accepted; the four profit values verified from §7. Actual inline representation accepted and logged in E27; no duplicate generator needed.
- **Korean-law snapshot:** historical/unverified qualifier is present. No new current-law claim approved.

## Review checks actually performed

- Read original C01–C07; reviewed exact git tree, not the checkout. Checked source-backed claims against evidence and targeted primary-source rechecks, then current design rules, then plan.
- Independently verified the ID-only commit strips back byte-for-byte to baseline for main, note and tech; branch content changes are restricted to lec12, its assets, outline and job record. The outline's duplicated unrelated sections are F01.
- Extracted the named commit using git archive into reviewer scratch. Independently rendered Chromium PDFs: 74 main and23 tech pages. Inspected all97 via contact sheets; enlarged main pp7,21,28,48–51,57,64,68,71–72 and techp4. No general overflow/missing-image/math issue observed. Source cropping defects documented above.
- Main74 IDs exactly match note74 IDs/order; tech23 IDs are unique. Note pacing sums to90. Local source/image references resolve. Frozen tracked plan-v1 matches owner copy byte-for-byte.
- Re-ran deck lint: main has the reported32 inline-color warning; tech clean. Lint does not detect F01/F02/F03. No claim of complete external-link refresh or timed teaching rehearsal.
- Reviewed exact toy counts and FICO inline bar geometry; these are consistent. Do not rewrite those examples during repair.

## Round-2 handoff

Apply **F01–F07** only, plus direct consequences and optional F08. Follow plan-v2's corrections. Refresh living job files and copy both new frozen files unchanged into tracked log. In work-r2.md answer each finding ID, provide any new split mappings, exact commit and changed/neighbor render list. Recheck all six P4-key uses after the shared correction; revise timings only within the existing section totals. Review round2 will check changed slides and neighbours, not restart the whole lecture. Any remaining blocker after round2 escalates to Albert. No PR/merge/PDF delivery yet.
