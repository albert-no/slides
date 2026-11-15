# review-r2 — final ordinary review

- **Reviewed commit:** `6dc56441c8294d20e53976aa25393ea38d408d08`.
- **Previous reviewed commit:** `3150ed4ae9bc70f96da43e5cc68837b38d646ef6`.
- **Baseline:** `99450923b41e94f10d0c557a4fc0f46b42a9c91d`; ID-only commit `853024d8077bc8faa290873d91019d108996d558`.
- **Verdict: revise. State: escalated. Round 2 of 2.** Of the 61 original blockers, 58 are closed and 3 remain partially open (F19/F34/F56). Three additional blockers were found in the changed articles (F66–F68). Four optional r1 items have dispositions below.
- **No automatic round 3.** The six open finding groups below go to Albert for a decision. Proposed corrections are not a new work order; do not begin another revision/review cycle without his authorization. No PR or merge approval.

## What matters most
1. **Finish the remaining consistency repairs.** Deduplication's retained limitation still assigns 10× to the wrong experiment; self-consistency still “rules out” a stochastic failure; reweighing's citation labels contradict its repaired explanation.
2. **Correct two retained technical claims.** The DP-audit case misattributes implementation violations and describes the wrong run count. The TOFU p-value theorem applies continuous/iid-uniform assumptions that its finite-sample KS setting does not establish.
3. **Make three new formulas readable on a narrow display at default type size.** Desktop and lint checks pass, but these formulas extend beyond the viewport. Do not shrink type.

**Keep:** the Message → Reading → detail hierarchy, all 902 stable slide/article pairs, and the substantial improvements to populations, denominators, theorem conditions and source scope. This is a small residual set, not a reason to repeat the 902-entry rewrite.

## Request coverage
| Request | Disposition | Evidence / remaining work |
|---|---|---|
| C01 — lec01–lec12 companions | Done for scope | All 12 canonical companions revised; 902 IDs, titles, order and counts preserved. |
| C02 — simple message, usable plot/content reading, then details | Not yet approved | Architecture works and most corrections are closed; the six open groups below prevent final accuracy/usability approval. |
| C03 — check/revise all, actual-limit capacity handling | Done for work to date | Round1 covered all902 new layers; round2 covered all112 changed articles plus opening neighbours. No provider capacity limit reported, no invented hold/reset. Ordinary review limit reached; human decision required. |
| C04 — render and consult primary sources as needed | Done, targeted | Round1 source/main-exhibit checks retained; round2 exact-tree visual, source and mathematical checks E87–E92. Not an exhaustive audit of all retained proofs or every external URL. |

## Scope and verification
- Read through git at the exact named SHA and used its archived tree, not a moving main or working tree. Course-content changes since r1 are confined to the 12 notes. No main, tech, reference, script, teaching-time, title, slide-order or OUTLINE changes in r2. The earlier ID-only/main-scope checks remain in review-r1.
- All **112 changed articles read in full**, plus Message/Reading layers of unchanged immediate neighbours. Counts by lecture: **8/19/9/12/18/13/5/4/1/10/3/10**. Truncated outputs were reread in smaller views before counting coverage. The two out-of-map changes (lec04S42 copy-detection proxy and lec05S41 TOFU design) are appropriate consistency fixes; unchanged lec12S17a/b needed no F65.4 repair.
- Independently matched all12 scratch note files again to exact `git show`. All12 notes lint with zero errors/warnings; IDs/titles/order match the prior review. Frozen review-r1/plan-v2 copies at target match the announced files. Their original checksums remain unchanged.
- All12 notes opened at1100px and430px; zero KaTeX error nodes. Same-browser r1/r2 overflow comparison finds no new desktop overflow. Narrow new/worsened overflows are F67, despite unchanged global page widths caused by wider inherited formulas.
- **23 desktop screenshots inspected:** lec01 S08/S19; lec02 S29/S62; lec03 S50/S51; lec04 S58/S59; lec05 S29/S64; lec06 S14/S71; lec07 S65/S67; lec08 S54/S64; lec09 S50; lec10 S25/S49; lec11 S34/S67; lec12 S19b/S39a. Three additional narrow screenshots inspected for F67. These are viewport checks, not a claim that every full-length article has been photographed. Semantic-entropy Table1's actual image rechecked; the illustrative two-scenario reading is valid.
- All49 local href/src references, including fragments, resolve; no r1 occurrence lost. Seven unique new external targets checked. Korean URLs work after ordinary HTML entity decoding; literal `&amp;` in an initial reviewer curl request caused an error page, not a deck-link defect. Pinned Vectara README verified through GitHub REST; no leaderboard refresh needed. Reachability is not claim verification.
- Full source/mathematical evidence and limitations: E87–E92, supplementing E01–E86. The exact historical AIF360 Fig4 generator remains unrecovered. No claim of exhaustive retained-proof or every-external-reference verification.

## Open blocking findings — proposed corrections awaiting Albert
All locations below refer to the reviewed SHA. Page numbers include every slide. **[judgment]** marks a contextual content/design decision for slides, not a context-free implementation instruction. Correct the named residual only; do not reopen sound parts or edit main decks.

1. **F19 | lec04/S50, p50 | fact | blocking, partially open.**
   **File:** `courses/trustworthy-ai/lec04-memorization-note.html`, article L946, retained Limitation L965.
   **Current → correction [judgment]:** the limitation still assigns the “10×” reduction to the duplicated-prompt regime. Replace it with: “The approximately10× headline concerns unprompted training-text emission; the displayed train-duplicate prompted bars fall by roughly5×. These are different evaluations.” Retain the corrected C4 Duplicates perplexity exception and clean-row scope.
   **Reason:** the limitation contradicts the now-correct opening/Result and repeats the original population error. E24.

2. **F34 | lec06/S55, p55; S57, p57 | fact | blocking, partially open.**
   **File:** `courses/trustworthy-ai/lec06-hallucination-note.html`, S55 article L821, Reading L824 and Script L827; S57 article L858, Script L864.
   **Current → correction [judgment]:** “agreement … rules out … arbitrary invention” → “agreement is evidence against arbitrary confabulation in these samples, not proof of its absence.” “the model is not making things up at random” → “these samples show no disagreement; this does not exclude stochastic confabulation.” Keep the already-correct repeated-misconception caveat and S56's source-supported estimator discussion.
   **Reason:** finitely many stochastic samples can all agree; the repaired Message correctly calls this an empirical cue, but these sentences still turn it into exclusion. E40/E82/E91.

3. **F56 | lec12/S39a, p52; S39b, p53 | fact | blocking, partially open.**
   **File:** `courses/trustworthy-ai/lec12-fairness-note.html`, articles L958/L976, Primary sources L971/L993.
   **Current → correction [judgment]:** “Fig.4(a)/(c): reweighing on the training data” → “Fig.4(a)/(c): transformed evaluation-data metrics; test-partition interpretation per §10 and AppendixB.4–5.”
   **Reason:** the two retained source locators still assert the population that the corrected Message/Reading/Script expressly reject. The substantive plot explanation, exact training-cell balancing and unrecovered-generator qualification are accepted; do not rewrite them. E77.

4. **F66 | lec02/S62, p62 | fact | blocking, new.**
   **File:** `courses/trustworthy-ai/lec02-privacy-dp-note.html`, article L1188, case attribution L1203 and Nasr reference L1209.
   **Current → correction [judgment]:** replace the claim that Jagielski–Ullman–Oprea found the preceding above-guarantee implementation violations with their actual result: tighter empirical DP-SGD lower bounds that remain below the theoretical upper bounds. Describe Nasr2023's main method as **two training runs with intermediate-update access**, not “one-run”; its §6.3 implementation-error tests include faulty clipping and noise. Separately source the shuffling/sampling-bug attribution or remove it.
   **Reason:** tightness auditing and detection of faulty implementations are different evidence. The statistical-confidence logic in the new opening is accepted; this is a source-attribution correction, also resolving work-r2 open flag2. E88.

5. **F67 | design rule | blocking, new narrow-display regressions.**
   **Locations:**
   - `courses/trustworthy-ai/lec02-privacy-dp-note.html`, S29/p29, article L563, posterior-odds display **L577**.
   - Same file, S32/p32, article L628, approximate-DP display **L639**.
   - `courses/trustworthy-ai/lec03-mia-note.html`, S51/p51, article L999, epsilon lower-bound display with condition **L1008**.
   **Precise correction [judgment]:** at the existing default type size, break the long derivation into readable mathematical steps and place the attached condition in adjacent prose where appropriate. Preserve the mathematical claims and conditions; no smaller fonts or compressed prose rhythm.
   **Reason:** the new formulas extend off-screen at430px. S32/S51 introduce new overflowing articles; S29 worsens inherited overflow. Measured article client/scroll widths:359/409,359/542,359/622 respectively. E89 and three inspected screenshots establish regressions, not just an old page-level issue.

6. **F68 | lec05/S41, p41 | fact | blocking, newly found in a changed article.**
   **File:** `courses/trustworthy-ai/lec05-unlearning-note.html`, article L644, retained theorem/proof/moral **L654–656**.
   **Current → correction [judgment]:** “continuous truth-ratio samples ⇒ the reported KS p is exactly Uniform[0,1]” is false for a finite-sample two-sample KS test. Reframe the retained calculation as an **illustration assuming a continuous null test-statistic distribution and independent uniform p-values across runs**, not an exact theorem about TOFU's reported KS values or correlated checkpoints. State that finite-sample non-randomized KS p-values are discrete and generally super-uniform; the `k/(k+1)` and `1−0.9^k` formulas additionally require independence. Keep the valid lesson: a large p-value is not proof of equality and checkpoint selection can bias the reported score.
   **Reason:** continuity of observations does not imply continuity of the KS statistic. Under a continuous null with two observations per sample, exact p-values are1/3 or1 and P(p≥0.9)=2/3, not0.1. Shared-data checkpoints also need not be independent. E90 supplies the finite counterexample and primary documentation. No TOFU empirical result is being rejected.

## R1 disposition ledger — every finding reconciled
“Closed” means the requested correction is accepted within this review's scope, not that every claim in the article has been independently proved. New findings in the same article are listed separately.

| Finding | Disposition | Verified result |
|---|---|---|
| F01 | Closed | White-box preparation/physical deployment, two photos, lab/drive-by distinction; Table2 supports100% (E87). |
| F02 | Closed | Korean Art35 endeavor duty; Art34/decree oversight and scope preserved with direct links. |
| F03 | Closed | False post-processing converse replaced; constant-output counterexample retained. |
| F04 | Closed | 51% conditional posterior versus54% average accuracy; F67 separately concerns layout. |
| F05 | Closed | DP protects incremental evidence, not all attribute inference. |
| F06 | Closed | Additive-event definition; tail condition correctly sufficient rather than equivalent. |
| F07 | Closed | Debiased estimate, not exact population rate. |
| F08 | Closed | One-sample/fixed-step/clipping/normalization scope; relative versus absolute noise. |
| F09 | Closed | Large upper bound is not observed leakage; nonconstant mechanism and historical comparison qualified. |
| F10 | Closed | Blocking does not establish erasure; no measured post-patch persistence or parameter invariance claim. |
| F11 | Closed | Recorded rearrest; cutoff PPV versus score calibration and nondegenerate impossibility separated. |
| F12 | Closed | Fixed delta, simultaneous confidence and valid rates/denominators; no automatic bug diagnosis. F66/F67 separate. |
| F13 | Closed | Patients-only cohort condition. |
| F14 | Closed | Randomized bounded-loss adversary distinguished from threshold attacks. |
| F15 | Closed | Likelihood ratio versus prior/posterior odds; low FPR not sufficient regardless of prevalence. |
| F16 | Closed | Main C4 versus deduplicated comparison; observed LiRA limits, not impossibility. |
| F17 | Closed | Chance-null/query-budget qualification replaces impossibility. |
| F18 | Closed | Repetition/duplication separated from more unique data. |
| F19 | Partially open | Corrected plots/openings; retained limitation still wrong. Item1. |
| F20 | Closed | Incremental DP guarantee, empirical zero detections and per-bar exact/approximate rates. |
| F21 | Closed | Nonmember-conditioned FPR, observed versus certified rates, no posterior-hit attribution. |
| F22 | Closed | 20 MC samples versus about10× greedy token evaluations; not wall-clock identity. |
| F23 | Closed | Normalized sample, known prefixes and extraction-probability thresholds explicit. |
| F24 | Closed | Random capacity plateau separated from natural-text generalization. |
| F25 | Closed | Necessary ROC outer bounds, complementary inequality, vacuous bound not lost DP. |
| F26 | Closed | Membership/TOFU controls, statistical evidence and bounded-adaptation target; S41 consistency extension accepted. F68 separate. |
| F27 | Closed | Approximate target versus certificate; heuristic LLM scope. |
| F28 | Closed | Implicit HVP computation versus dense storage, cost/nonconvex limits. |
| F29 | Closed | Filter access, learned refusal and retraining target separated. |
| F30 | Closed | Aggregate21%/83% benchmark scope; quantization mechanism attributed, not universal identity. |
| F31 | Closed | Retain-set ten-example result, RMU–Wikitext exception and DPO baseline identified. |
| F32 | Closed | Zero empirical binned ECE is not population calibration. |
| F33 | Closed | Upper coverage bound does not bound set size; valid proof retained. |
| F34 | Partially open | Truth/misconception caveat repaired; finite agreement still treated as exclusion. Item2. |
| F35 | Closed | Fixed-parameter cutoff without automatic detector; uncertainty/context remain possible. |
| F36 | Closed | o3/o4-mini explanations separated; no causal deliberation ablation or empirical theorem floor. |
| F37 | Closed | Historical general trend with UnifiedQA exception. |
| F38 | Closed | Monitor input scope, lower total cheating and lack of guarantee under direct optimization. |
| F39 | Closed | AlwaysEqual as one of three shortcuts; aggregate hack curve identified. |
| F40 | Closed | PGD is approximate inner optimization, not a certificate. |
| F41 | Closed | Correct center and whole ball; AutoAttack survival is an empirical upper-bound estimate. |
| F42 | Closed | Campaign dates versus intrusion inside HF separated. |
| F43 | Closed | Chance-corrected normalized score, inferred use and causal acknowledgment defined. |
| F44 | Closed | Dataset-specific cost/share curves, not invented common endpoints. |
| F45 | Closed | Open-weight Llama2 versus black-box target use. |
| F46 | Closed | Harmful-prefix dataset; lower but nonzero later KL. |
| F47 | Closed | NLL/negative-log ASR power-law fits and separate panels/tasks. |
| F48 | Closed | Original target-aware attacks acknowledged; stronger tuning still possible. |
| F49 | Closed | Availability versus efficacy; online age versus continuous success. |
| F50 | Closed | Score change is not proof of safer or unchanged-harm outputs. |
| F51 | Closed | GCG top3-of10 selection, scoped to that row. |
| F52 | Closed | Conditional small full-text TV and AUROC upper bound. |
| F53 | Closed | Pre2Aug2026 eligibility versus2Dec2026 deadline. |
| F54 | Closed | Predictor inputs versus separate audit labels. |
| F55 | Optional accepted | Calibration implies top-bucket PPV equality; converse not asserted. |
| F56 | Partially open | Correct evaluation-data reading, but two source labels remain contradictory. Item3. |
| F57 | Optional accepted | Fixed TPR/FPR and fraction of false flags, not count. |
| F58 | Closed | Italian historical fine/first-instance annulment/further-appeal uncertainty consistent. |
| F59 | Closed | Additive-noise recipe scoped; exponential mechanism counterexample. |
| F60 | Closed | Statistical advantage versus one false-positive-prone flag. |
| F61 | Closed | Retained-objective Hessian condition, gradient-domain caveat, original-n/fixed-lambda retrainer and matching Gaussian distributions/range. |
| F62 | Closed | Adaptive partition, full correction terms, hypothetical citations and arbitrary-fact versus FActScore separation. |
| F63 | Closed | NPO gradient exception; forest-plot medians/credible intervals/50% baseline. |
| F64 | Optional accepted | Work-r2 corrects S66 and parent-revision provenance; independently verified (E92). Frozen work-r1 untouched. |
| F65 | Optional disposition complete | Items1/2/3/5/6 accepted: source URL, pinned snapshot, Definition2/Eq2.2, misplaced duplicate, spoken cue. Item4 withdrawn as reviewer error; r1 already kept panel titles (E92). |

## Work-report flags and plan decisions
- **Work-r2 flag1 closed:** RP2 Table2 is valid for the100% lab result. No plan/source correction needed there (E87).
- **Flag2 escalated as F66:** the retained audit case is within the authorized note-accuracy scope, but not supported by the cited papers as written.
- **Flag3 deferred:** inherited main-slide alt-text errors in lec05S62 and lec09S50, and work-r2's other main discrepancies, are documented. No main-deck edits authorized by this job. Deferral is not factual endorsement.
- **F64 accepted; F65.4 owner correction:** work-r2's historical repair explanation is accurate; the requested panel-title cleanup was unnecessary. No frozen record is rewritten.
- No other plan-v2 issue requires argument, scope or teaching-time change. Additional F66/F68 source/math corrections and F67 formatting are proposed here, not an automatically authorized plan-v3. The ordinary two-round allowance is exhausted.

## Decision gate
Albert chooses whether to authorize a limited follow-up covering the six open groups, accept/defer specified risks, or close the job. Until that decision: **escalated, no implementation order, no PR, no merge**. On any future approval, slides must first push unchanged job records; only log-only commits may follow the reviewed content SHA before PR creation.
