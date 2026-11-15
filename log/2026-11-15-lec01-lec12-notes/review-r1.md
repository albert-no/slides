# review-r1 — first review

- **Reviewed commit:** `3150ed4ae9bc70f96da43e5cc68837b38d646ef6`.
- **Baseline:** `99450923b41e94f10d0c557a4fc0f46b42a9c91d`; ID-only commit: `853024d8077bc8faa290873d91019d108996d558`.
- **Verdict: revise.** Round 1 of 2; **61 blocking findings and 4 nonblocking refinements**. One revision/review round remains. Open blockers after round 2 go to Albert; no third round by default.
- **Work order:** `plan-v2.md`, an incremental correction to `plan-v1.md`, not another rewrite of 902 entries.

## What matters most
1. **Do not turn conditional evidence into a guarantee.** Privacy bounds, attacks, unlearning audits, calibration, robustness and detection repeatedly become categorical promises. Put the necessary condition in the short explanation and repair contradictory retained Scripts as well.
2. **Read the actual exhibit.** Restore the population, denominator, axis transformation, selection rule and visible exceptions. Several current readings describe an abstract/headline instead of the plotted result.
3. **Make layers and sources agree.** Correct dated legal status, threat-model access and theorem hypotheses; preserve accurate historical snapshots rather than silently updating them to present tense.

**Keep:** the Message → Reading → detailed-reference hierarchy, all 902 stable pairs, useful proofs and source material, and the many already-qualified explanations. The architecture is useful; this revision is about accuracy and lecturer usability, not redesign or a mechanical word-count cut.

## Request coverage
| Request | Done? | Evidence / remaining work |
|---|---|---|
| C01 — all lec01–lec12 companions | Yes, scope implemented | All 12 canonical files and all 902 entries have the new structure; counts and ordered IDs preserved. Accuracy approval remains subject to the findings. |
| C02 — clear brief message, usable exhibit reading, then details | **Not yet** | Hierarchy implemented, but the 61 blockers prevent reliable teaching from these notes. Keep the architecture and correct the listed entries. |
| C03 — check/revise all; pause only for an actual provider limit | Yes for work to date | Every new layer reviewed; package checkpoints preserved. No actual capacity block reported, no quota hold or reset invented. Same rule continues during revision. |
| C04 — render plots and consult originals where needed | Yes, targeted review completed | Exact-commit browser checks, targeted main-slide renders and source/math/legal checks recorded in E14–E86. This is not a claim of exhaustive retained-proof or external-reference verification. |

## Review scope and checks
- Read all **902 new Message/Reading pairs**, with matching main-slide text: 46/69/70/65/68/75/75/101/91/88/74/80 by lecture. Inspected changed-old-paragraph inventories and selected complete retained passages. Truncated outputs count as read only where subsequently reread in bounded views.
- All 12 exact-commit companions opened at desktop and narrow widths; 36 first/middle/last screenshots inspected for hierarchy; zero KaTeX error nodes. Targeted main-slide renders inspected: lec01 pp4/9/19/30; lec02 pp8/29/56/60; lec03 pp28/39/44/47/52; lec04 pp12/15/31/42/50/53/56/58/59/60; lec05 pp12/28/30/33/34/41/53/55/56/62/63/64; lec06 pp18/21/31/33/43/56/67/71; lec07 pp17/20/25/43/48/53/54/65/67; lec08 pp7/15/31/34/48/57/60/61/66/84/86/88; lec09 pp6/23/24/26/30/31/40/50/53/56/64/74/82; lec10 pp22/23/27/36/49/50/52/64/67/80/82/84; lec11 pp9/18/21/23/24/26/30/35/41/43/45/52/57; lec12 pp4/7/23/24/30/31/36/37/38/52/53/57/58/60/63/64/72/73/74. Manual activation's artificial 1/N counter is not a page-number defect.
- Baseline browser comparison: **no new overflowing article**; four old narrow overflows in lec11 resolved. Inherited overflow is not a regression from this job (E76). All 12 archived companions independently lint with 0 errors / 0 warnings; all 49 local href/src references resolve; baseline href multiplicities preserved (E86).
- Four unique new external URLs checked; no claim to have independently read every retained proof, all old paragraphs, or all 803 external references. Source links merely surviving is not source verification. Evidence register distinguishes source claims, our calculations and unresolved provenance.
- Post-ID main slides unchanged; shared content change is the leaf OUTLINE. Owner changed no deck, note, reference or implementation script.

## Blocking findings
Paths and article-start lines below refer to the exact reviewed commit, not the moving branch. Slide IDs are deck-scoped; page numbers include every slide. Each numbered item gives the error, concrete correction and reason. Content/wording choices marked **[judgment]** require slides' contextual judgment, not context-free implementation. Keep every correction consistent through Message, Reading, Script and other repetitions in the listed article.

**Scope:** explain a main slide's inherited shorthand/error explicitly in its note and record the main discrepancy in work-r2. Main-slide content edits, new slides, altered teaching time, supplements, reference files and scripts are not authorized. Correcting false retained prose is authorized; preserving evidence does not mean preserving an error.

1. **F01 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec01-introduction-note.html:451` — lec01/S19, p19; `courses/trustworthy-ai/lec01-introduction-note.html:955` — lec01/S40, p40; `courses/trustworthy-ai/lec01-introduction-note.html:1035` — lec01/S44, p44.
   “not the model's weights”/“a weaker attacker” is wrong for RP2's optimization. [judgment] Explain white-box preparation using architecture/weights, followed by physical application using printed stickers; do not call the demonstrated attack black-box. Describe the actual two photos rather than multiple tested angles; point to Table 3 for 84.8% drive-by and Table 2 for lab tests. E14.  Also correct this repeated implication in S40/p40 and S44/p44 explanations where present. **Reason:** The attack preparation/access distinction is the threat-model lesson.

2. **F02 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec01-introduction-note.html:795` — lec01/S31, p31.
   [judgment] “requires impact assessments” → explain Article 35's endeavor-to-assess obligation, separate from other high-impact duties; use a direct statute/article link, not the law.go.kr home page. Correct Message, Reading, Script and case-background repetitions. E15. Do not silently imply every AI service has every listed duty. Named oversight is supported by Article 34(1)(4) and Enforcement Decree 27(1)(4); keep it with that scoped citation (E78), not as an obligation on every AI service. **Reason:** An endeavor duty is not the same legal obligation as a mandatory completed assessment.

3. **F03 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:41` — lec02/S03, p3.
   The asserted converse of post-processing (“no output filter can lower” infinite epsilon) is false. [judgment] Replace the opening/Reading and erroneous technical paragraph with: protect an artifact before releasing it; later work cannot retract information already disclosed; a newly released filtered/sanitized artifact needs its own guarantee. Explain the constant-output counterexample if retaining mathematical detail. E16–E17. Do not change the sound post-processing theorem on S37. **Reason:** The false converse teaches the opposite of the actual post-processing guarantee.

4. **F04 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:563` — lec02/S29, p29.
   [judgment] The Reading assigns 54% accuracy to the particular 171 cm observation. Replace with approximately 51% posterior for Korea at 171 cm under equal priors; separately identify approximately 54% as average Bayes accuracy across random people. Label the height distributions illustrative rather than verified demographic measurements. E17. **Reason:** Conditional posterior confidence and average classification accuracy answer different questions.

5. **F05 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:786` — lec02/S41, p41.
   “Alice smokes does not [stay learnable]” overclaims. [judgment] Explain that DP limits the incremental evidence from Alice's protected record; it does not prevent inferring her attributes from correlations, population facts or other information. Read the slide's categorical phrase as shorthand, not a guarantee of attribute secrecy. Consistent with the population-knowledge discussion in E16. **Reason:** Attribute secrecy is stronger than the guarantee DP actually supplies.

6. **F06 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:625` — lec02/S32, p32; `courses/trustworthy-ai/lec02-privacy-dp-note.html:745` — lec02/S39, p39.
   [judgment] The retained statement that with probability 1 − delta an approximate-DP output behaves as pure epsilon-DP is not the general definition. Replace with the additive event-probability inequality; if a privacy-loss tail condition remains, distinguish a sufficient condition from an equivalent characterization and check its directions/parameters. E16/E30. The full S39 proof was checked: its sufficient-condition lemma is valid. Keep that proof; correct S32 and the sentence following the proof that incorrectly treats the tail condition as equivalent to approximate DP. **Reason:** A sufficient privacy-loss condition must not replace the general approximate-DP definition.

7. **F07 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:860` — lec02/S46, p46.
   [judgment] “the true rate is 90%” → “the debiased estimate of the true rate is 90%.” Carry finite-sample randomness into the opening, not only the final sentence of Reading. E17; no new measurement. **Reason:** Finite-sample uncertainty is essential to interpreting the randomized-response estimate.

8. **F08 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:1083` — lec02/S57, p57.
   The universal 1/n DP-SGD claim and “chance any given step touches your record is 1/n” omit batch/sampling/averaging assumptions. [judgment] State the qualitative signal-to-noise lesson in Message; scope the displayed bound to the specific fixed-sampling/batch, clipping, step-count and normalization setup of its cited theorem, or remove the unqualified scaling claim. E30 resolves the local source: `courses/privacy/lectures/01-dp/dp5-erm.html:691–817` uses one uniform sample per step. State that special case, fixed T/clipping/normalization, and do not present its simplified constant as a universally applicable accountant. The plotted bars have fixed absolute noise and rising signal; the note must distinguish absolute noise from relative error. **Reason:** The apparent scaling law is not portable without its sampling and normalization premises.

9. **F09 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:579` — lec02/S30, p30; `courses/trustworthy-ai/lec02-privacy-dp-note.html:643` — lec02/S33, p33; `courses/trustworthy-ai/lec02-privacy-dp-note.html:707` — lec02/S36, p36; `courses/trustworthy-ai/lec02-privacy-dp-note.html:735` — lec02/S38, p38; `courses/trustworthy-ai/lec02-privacy-dp-note.html:776` — lec02/S40, p40; `courses/trustworthy-ai/lec02-privacy-dp-note.html:1067` — lec02/S56, p56; `courses/trustworthy-ai/lec02-privacy-dp-note.html:1307` — lec02/S68, p68.
   Avoid treating a large epsilon upper bound as proof that a system has no privacy, or overlap as making all membership inference impossible. [judgment] Say that a large reported bound offers weak worst-case protection and smaller epsilon limits distinguishability under the fixed setup; it does not certify an actual leak or literal inability to guess. Remove categorical “large epsilon is not private,” “does not help,” and “cannot tell” claims from the new explanatory layer; retain meaningful intuitions with their scope. Also align the retained Scripts at S30/p30 L579 (non-constant mechanism), S56/p56 L1067 (historical benchmark comparison, not an ongoing guaranteed annual trend), and S68/p68 L1307 (scoped advantage bound rather than literal prevention), which still undo their already qualified new readings. E16/E30; the retained source limits are part of the correction. **Reason:** An upper-bound parameter is not a measurement of an actual attack or a ban on guessing.

10. **F10 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec01-introduction-note.html:231` — lec01/S12, p12; `courses/trustworthy-ai/lec01-introduction-note.html:864` — lec01/S34, p34; `courses/trustworthy-ai/lec02-privacy-dp-note.html:157` — lec02/S09, p9; `courses/trustworthy-ai/lec02-privacy-dp-note.html:422` — lec02/S20, p20; `courses/trustworthy-ai/lec04-memorization-note.html:443` — lec04/S23, p23; `courses/trustworthy-ai/lec04-memorization-note.html:505` — lec04/S26, p26.
   The old/new prose asserts alignment training does not change weights' contents and the memorization definitely remains after a prompt block. Alignment fine-tuning changes parameters; the cited extraction result demonstrates residual extraction in tested models, not a universal invariant or a post-patch measurement. [judgment] Use “blocking this route does not establish removal of memorized data,” and qualify all Script/Technical connection repetitions. Primary Nasr paper and authors’ patch discussion checked (E22). Extend the same fix to lec04 S23/p23 L443 and S26/p26 L505: remove the unsupported factual claim “weights unchanged” and post-patch persistence asserted as a measurement. Likewise at lec02 S20/p20, “none of them changes what the model memorized” should become “these procedural measures do not establish removal of memorized information”; no weight-level measurement is cited. **Reason:** A blocked extraction route does not establish whether information remains in model parameters.

11. **F11 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec01-introduction-note.html:112` — lec01/S08, p8.
   [judgment] Replace “re-offend” with “recorded rearrest” when explaining the measured label; keep the distinction consistent through Script/details. E18. Also correct the retained attribution/theorem: Northpointe's defense here is approximately similar cutoff PPV, distinct from scorewise agreement called calibration by other analyses. Explain that unequal base rates conflict with equal PPV plus both equal error rates under the stated nondegeneracy conditions; do not claim calibration alone makes error parity impossible. lec12/S20b/S27/S30 and E71 supply the precise distinction. **Reason:** The outcome label and the precise fairness quantities determine the theorem being taught.

12. **F12 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:1181` — lec02/S62, p62; `courses/trustworthy-ai/lec03-mia-note.html:998` — lec03/S51, p51.
   A finite empirical attack operating point is not automatically a certified lower bound or proof of a code bug. [judgment] Add statistical confidence/uncertainty, fixed delta and valid numerator/denominator conditions to the audit claim; only a statistically supported violation challenges the claimed guarantee. Jagielski Algorithm 2/Theorem 2 checked (E29). Extend to lec03 S51/p51 L998, including its Script and “formal counterexample/bug certificate” language. For fixed delta and positive denominator, define epsilon_LB = max(0, log((TPR_lower-delta)/FPR_upper)) when the numerator is positive, with stated simultaneous confidence; do not write a mere inequality defining an arbitrary epsilon-hat as the bound. An inconsistency can concern assumptions/accounting/implementation, and below-claim results do not prove the proof is loose. **Reason:** Statistical uncertainty and valid assumptions separate empirical evidence from a contradiction of a guarantee.

13. **F13 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec03-mia-note.html:135` — lec03/S08, p8.
   “Being in a disease study/clinical trial reveals a diagnosis” lacks the patient-only qualifier already present at S07. [judgment] State that a confirmed member of a *patient-only* cohort may reveal its diagnosis; a general clinical study may include healthy controls. Correct Message, Reading and Script. Reason: the cohort eligibility, not its name alone, supports the inference. E28.

14. **F14 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec03-mia-note.html:504` — lec03/S28, p28.
   The Message attributes the exact normalized-gap identity to the fixed loss-threshold attack. [judgment] Say the identity holds for Yeom's randomized bounded-loss adversary; the plotted threshold attacks have their own assumptions. Retain the valid coin-flip proof and separate it from Fig. 2's empirical relation. Reason: the opening currently contradicts its own theorem. E19.

15. **F15 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec03-mia-note.html:741` — lec03/S39, p39; `courses/trustworthy-ai/lec03-mia-note.html:827` — lec03/S43, p43.
   “the in-hypothesis is about six times as likely” confuses likelihood ratio and posterior odds; “Only A can point at a person and usually be right” also drops the base rate taught at S46. [judgment] Say “the observed score has about 5.9 times the density under IN as under OUT; posterior odds additionally require prior odds.” Describe low-FPR performance as needed for credible accusations, not sufficient regardless of prevalence/TPR. Correct Script repetitions. Reason: otherwise the example teaches the inverse-probability error that the next section warns about. E30 and S46's Bayes calculation.

16. **F16 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec03-mia-note.html:905` — lec03/S47, p47; `courses/trustworthy-ai/lec03-mia-note.html:1186` — lec03/S59, p59.
   Script calls the main C4 setup deduplicated; case background says no separate deduplicated comparison. [judgment] State main setup C4 and describe Appendix D/Fig. 16 as a separate C4-versus-deduplicated-C4 experiment. Remove “even for the optimal test” where the text upgrades observed LiRA instability to an impossibility for all tests. Reason: the corpus treatment and experiment's inferential scope matter. E20.

17. **F17 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:264` — lec04/S13, p13.
   “any reappearance … must be memorization rather than chance” / “chance cannot reproduce it” is false and contradicts the retained nonzero null probability. [judgment] Use “a fresh random canary makes accidental matches unlikely under a specified null; compare exposure with that baseline and query budget.” Preserve the useful uniqueness argument without claiming certainty. E21.

18. **F18 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:687` — lec04/S36, p36.
   “more data … push[es] memorization in the wrong direction” is not one of the paper's three drivers. [judgment] Distinguish more repeated exposures/duplication from more unique data; the latter does not imply higher per-record memorization at fixed capacity/training budget. Explicitly qualify the main slide's shorthand rather than endorsing it in Message and Script. Reason: reverses a central data-scale/overfitting distinction. E23/E27.

19. **F19 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:946` — lec04/S50, p50.
   Reading says validation perplexity is equal or better throughout, but the rendered C4 Duplicates row is substantially worse after deduplication. [judgment] Describe that exception and why removing train/validation overlap reduces artificially easy prediction there. Keep the 10× unprompted-emission headline distinct from the roughly 5× train-dup bar drop. Scope “no cost in quality” to the evaluated clean/generalization metrics, not every row or all applications. Reason: the explanation must actually read both plots. E24.

20. **F20 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:1008` — lec04/S53, p53.
   The new Message correctly limits single-record influence but Script still says “no single record can be memorized.” [judgment] Replace that categorical promise with a bound on the incremental probability of reproducing a record under the stated adjacency/epsilon/delta; say zero detections is an empirical outcome under the reported test, not proof of zero storage/emission. Preserve the duplicate/group caveat. Also correct the retained 0.01% lower end: the exact-match Gemma 3 bar is below 0.001%, while approximate matching is near 0.01%; report by bar/type or omit a crude range. Reason: the retained Script reverses the new opening's qualifier. E16/E27; inspected plot.

21. **F21 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:1173` — lec04/S59, p59.
   Technical depth reverses conditioning: “a member flagged … is a false positive with probability at most alpha.” [judgment] Replace with marginal P(flag | fresh matched non-member)≤alpha under exchangeability with *non-member* controls; include the finite-sample rank/cutoff correction if retaining the formula. Do not call the member-minus-control rate the paper's calibrated memorization definition. In Message/Script replace “a quarter of hits are predictability/noise” with “the non-member reproduction rate is about a quarter as large as the member rate”; it does not identify which member completions were not memorized. Distinguish displayed observed rates 1.82%/0.02% from the revised paper's certified levels 1.84%/0.04%. Reason: statistical guarantees and denominators are the point of this slide. E25.

22. **F22 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:1140` — lec04/S58, p58.
   The main slide says 20× greedy cost; the source specifies about 20 Monte Carlo samples, about 10× greedy token evaluations with its 50/50/20 setup. [judgment] Add this explicit clarification to Reading, keep token-evaluation cost separate from wall-clock time, and retain the lower-bound qualifier. Reason: otherwise the lecturer cannot reconcile the slide with the source. E26.

23. **F23 | unmet request | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:573` — lec04/S31, p31; `courses/trustworthy-ai/lec04-memorization-note.html:1077` — lec04/S56, p56; `courses/trustworthy-ai/lec04-memorization-note.html:1140` — lec04/S58, p58.
   The new readings omit experimental qualifiers needed to interpret the rates. [judgment] S31: identify Fig. 1's length/duplication-normalized sample, not a corpus-wide random fraction. S56: make clear that the book audit uses known prefixes and reports per-window/probability-threshold coverage, not necessarily blind whole-book retrieval; name the orange bar's0.1% probability threshold. S58: name the fixed 0.001 extraction-probability threshold for its probabilistic/k-CBS curves. Reason: a lecturer cannot interpret those percentages without the sample and counting rule. E23/E26; S56 plotted legend and retained method. Do not infer newer book-version results from this older capture.

24. **F24 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec04-memorization-note.html:1205` — lec04/S60, p60.
   The Message moves directly from random-data capacity to “then start generalizing,” making the Fig. 1 plateau sound like evidence for generalization on random strings. [judgment] Separate the experiments: random-data models plateau at capacity; the natural-text experiments explore the memorization/generalization shift. State 3.6 bits/parameter as this model/protocol estimate, not a universal storage constant. Reason: the figure has no learnable underlying pattern. E27.

25. **F25 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec03-mia-note.html:942` — lec03/S49, p49; `courses/trustworthy-ai/lec03-mia-note.html:971` — lec03/S50, p50.
   Reading makes the pure-DP pointwise ratio apply to approximate DP, then labels the region below one ROC ceiling as “what any attack can attain.” [judgment] Identify the ratio picture as pure-DP intuition; for approximate DP use event probabilities with additive delta. Call the shaded region an outer bound from one inequality, not the exact attainable region: the complementary-event bound already proved in S49 also applies. The retained statement that the “average-case guarantee dies” when the loose bound exceeds 1 should instead say *this bound becomes vacuous*, not DP itself. Reason: a necessary inequality is not a sufficient characterization. E16 and the note's own valid S49 proof.

26. **F26 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:138` — lec05/S09, p9; `courses/trustworthy-ai/lec05-unlearning-note.html:608` — lec05/S39, p39; `courses/trustworthy-ai/lec05-unlearning-note.html:685` — lec05/S43, p43; `courses/trustworthy-ai/lec05-unlearning-note.html:824` — lec05/S51, p51; `courses/trustworthy-ai/lec05-unlearning-note.html:841` — lec05/S52, p52; `courses/trustworthy-ai/lec05-unlearning-note.html:901` — lec05/S55, p55; `courses/trustworthy-ai/lec05-unlearning-note.html:1009` — lec05/S61, p61.
   Single membership flags or correct TOFU answers do not prove failed forgetting, and a passed audit does not certify removal. [judgment] Replace “confirm”, “shows a trace remains”, “forgetting succeeded/failed”, and “removed … shown by … an audit” with statistical evidence relative to the retrained reference and calibrated controls. A single hit can be a false positive/guess; failed detection is not proof of equality. Keep S51's valid one-sided theorem but state confidence is needed for finite empirical gaps. Correct every Script repetition. Reason: the opening contradicts its own proof and the course's audit lesson. E33–34. Extend this qualification to S39/p39 L608 (“made … stop producing” → reduced tested Harry-Potter behavior), S43's “only source/no leakage” (controlled synthetic design, not a universal absence proof), and S55/p55 L901 (compare recovery with a retrained/unexposed control; a successful attack refutes only the stated adaptation-budget target, not every definition of deletion). E85.

27. **F27 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:274` — lec05/S18, p18; `courses/trustworthy-ai/lec05-unlearning-note.html:810` — lec05/S50, p50.
   “Approximate” is treated as both automatically bounded and universally uncertified. [judgment] Distinguish approximate *target* from a method's proved bound: some certified methods allow epsilon/delta discrepancy, while practical heuristic edits may have no certificate or established distance. S50 “approximate methods give no certificate” → “the heuristic large-model methods here generally lack a retrain-indistinguishability certificate.” Reason: preserve S19/S30's certified approximate examples. E33.

28. **F28 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:478` — lec05/S31, p31.
   Opening infers mandatory d² storage from needing H^-1v, contradicting the technical paragraph. [judgment] Say explicitly that forming a dense Hessian is infeasible, but implicit Hessian-vector products/iterative solves avoid storing it; compute cost and non-convex validity remain challenges. Do not claim the storage argument alone proves only rough estimates are possible. Reason: the original influence paper's key method is precisely implicit computation. E32.

29. **F29 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:789` — lec05/S48, p48; `courses/trustworthy-ai/lec05-unlearning-note.html:1009` — lec05/S61, p61.
   Filtering is not bypassable under every access model, and refusal behavior is not identical to an external filter. [judgment] Qualify bypass as possible with direct weight/model access that omits the external filter, or through tested filter vulnerabilities; fine-tuning API access alone does not establish the filter is removable. Say refusal can be learned in weights or imposed by a wrapper, and does not prove removal. Also replace “verified removal would have nothing left to leak” with absence of the removed records' incremental influence relative to retraining: remaining records can contain the same knowledge. Reason: targets, behavior, and implementation are different axes. E33; same counterexample family as F03.

30. **F30 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:929` — lec05/S56, p56.
   New Message turns the 21%→83% average into one model's literal retained-knowledge measurement. [judgment] Identify the aggregate over tested utility-constrained methods and benchmark metric; scope the quantization explanation to the authors' supported mechanism, not an exact rounding identity. Preserve the stronger limitations already in the case background. Reason: denominator and scope are needed to read the headline. E35.

31. **F31 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:1021` — lec05/S62, p62.
   “All curves … baseline” and “5 to 10 … Wikitext” misread Fig. 2. [judgment] Attribute the ten-example headline to the retain set (RMU 61.6% vs64.4% baseline), identify methods by color/dataset by style, and explicitly note the near-chance RMU-Wikitext exception in the rendered crop. DPO is the safety-training baseline, not another unlearning algorithm; align the case-background labels. Reason: the lecturer needs the actual experimental comparison, not the abstract pasted onto every curve. E36.

32. **F32 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:429` — lec06/S28, p28.
   “Zero is perfect calibration” is false for the finite binned ECE just defined. [judgment] Use “zero means no observed average gap in these bins; it does not certify population calibration or correctness at every confidence value.” Correct Script too; retain existing binning caveats. Reason: the note already explains within-bin cancellation. E37.

33. **F33 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:682` — lec06/S45, p45.
   Upper coverage bound does not say the sets are “not wastefully large.” [judgment] Replace with “coverage is close to the nominal target under distinct scores; this places no bound on set size or efficiency.” Keep the sound theorem/proof unchanged. Reason: coverage and usefulness are distinct. E37.

34. **F34 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:820` — lec06/S55, p55; `courses/trustworthy-ai/lec06-hallucination-note.html:836` — lec06/S56, p56; `courses/trustworthy-ai/lec06-hallucination-note.html:857` — lec06/S57, p57.
   Openings imply agreement/low entropy makes an answer reliable without identifying the method's blind spot. [judgment] State that consistency/semantic entropy is an empirical cue for arbitrary confabulation, not a truth test: confident repeated misconceptions can have low entropy. Preserve the clustering example, describe broad probability mass across meanings rather than merely many meanings, and do not promise paraphrases “no longer” create false alarms with an imperfect entailment judge. Reason: the next TruthfulQA section supplies the counterexample. E40. The retained estimator wording and LLN attribution were confirmed in the source Methods (E82); no additional estimator rewrite is required.

35. **F35 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:348` — lec06/S22, p22.
   “Facts freeze”, “no internal flag”, and retained “cannot signal it” make a risk categorical. [judgment] Scope to information learned in fixed parameters without later evidence or updates: a cutoff gives no automatic reliable freshness detector, but a model can be prompted/trained to disclose uncertainty and can use supplied context. Do not assert every post-cutoff question must receive an equally confident guess. Reason: otherwise the entry contradicts its own later RAG and abstention lessons. This is our logical scope correction: a response saying it lacks post-cutoff information is permitted by the generation setup, so inability to signal uncertainty does not follow from a cutoff alone.

36. **F36 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:1043` — lec06/S70, p70.
   “Because they make more claims” merges two distinct explanations; “reasoning … can worsen it” implies a causal ablation. [judgment] Keep the verified rates; attribute more-claims observation to o3 and distinguish o4-mini's smaller-model explanation. Say these models still hallucinate; this comparison does not isolate the causal effect of deliberation. Remove the unsupported retained singleton-floor/chain-of-thought inference. Reason: the system card explicitly leaves the cause open. E38.

37. **F37 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:996` — lec06/S67, p67.
   “Within each family the largest … least truthful” is contradicted by UnifiedQA 2.8B above 770M in the displayed figure. [judgment] State the generally negative trend in these historical models, explicitly noting the UnifiedQA exception/nonmonotonicity; keep the clear GPT-3 comparison. Correct Reading/figure detail and explain the slide's overbroad closing shorthand. Reason: actual plot beats an inherited caption. E39.

38. **F38 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec07-alignment-failures-note.html:1367` — lec07/S67, p67; `courses/trustworthy-ai/lec07-alignment-failures-note.html:1390` — lec07/S68, p68.
   Message says monitoring “cannot … stay reliable when directly optimized against,” contradicting its retained Assumptions. [judgment] Replace with “cannot guarantee reliability when directly optimized against.” In S67's reading identify the pressured monitor as reasoning-only, unlike S66's reasoning-plus-actions monitor; note that total cheating was lower than baseline even though remaining cheating became hidden. Reason: preserve the demonstrated failure without converting it into universal impossibility or hiding the intervention's tradeoff. E45.

39. **F39 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec07-alignment-failures-note.html:956` — lec07/S47, p47.
   “The model was rewarded for one shortcut” attaches the aggregate near 100% hack rate and broad generalization to AlwaysEqual alone. [judgment] Say “AlwaysEqual was one of three shortcuts available in the study; as overall hacking rose, the separate misalignment scores rose.” Retain the concrete example, but explicitly label the measured curve as all studied hacks, not an isolated one-hack experiment. Reason: the lecturer needs example-versus-measurement scope. E44.

40. **F40 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec08-adversarial-note.html:1112` — lec08/S64, p64.
   “Find the worst change … with PGD” / inner max “found by PGD” overstates a heuristic solver. [judgment] Use “approximately solve the inner maximization with PGD, then train on the high-loss examples found.” Align Script; keep exact min–max formula as the objective. Reason: the current opening contradicts S60 and the central empirical-versus-certified distinction. E46.

41. **F41 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec08-adversarial-note.html:930` — lec08/S54, p54; `courses/trustworthy-ai/lec08-adversarial-note.html:1268` — lec08/S71, p71.
   S54 counts every noncrossing ball as robustly correct, forgetting initially wrong predictions; S71 calls four attack failures “robust” without the empirical qualifier. [judgment] S54: “For these correctly classified images, crossing can expose an error; robust accuracy requires the whole ball, including its center, to have the true label.” S71: “counted as surviving AutoAttack, an upper-bound estimate, if all four fail.” Reason: stability and failure to find an attack are not correctness or proof. E47.

42. **F42 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec07-alignment-failures-note.html:152` — lec07/S08, p8.
   Retained Script calls July 9–13 “activity inside its systems,” while HF's timestamp window includes external staging. [judgment] Identify July 9–13 as the reconstructed campaign window, with the main intrusion inside HF from July 11; describe 17,600 as reconstructed attacker actions across that campaign. Keep the concise opening's broad July 2026 framing. Reason: the source explicitly distinguishes a 4.5-day campaign from roughly 2.5 days inside HF. E50. Flag corresponding main-slide date shorthand, without editing the deck.

43. **F43 | unmet request | blocking.**
   **Where:** `courses/trustworthy-ai/lec07-alignment-failures-note.html:1327` — lec07/S65, p65.
   The new reading labels the plotted normalized estimate as a literal share of known hint-using cases. [judgment] Identify it as the paper's chance-corrected disclosure score among inferred hint-use cases; say the classifier checks acknowledgment of causal use, not any mention of the hint. Keep 25%/39% and S63's plain-language setup. Reason: the actual metric has a conditioning rule and correction, not access to inner reasoning. E51.

44. **F44 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec09-poisoning-note.html:756` — lec09/S50, p50.
   Reading says every cost curve starts around 0.01% and ends at 0.1% or more; the rendered curves contradict both. [judgment] Replace that sentence with: “The attainable share differs by dataset at the same budget; higher curves mean more data controlled for the same cost.” Keep the verified approximate$60/year LAION access headline. Reason: the new explanation must read the actual plot rather than repeat its faulty alt-text range. E55.

45. **F45 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:738` — lec10/S36, p36.
   Llama-2 is grouped with “four closed chatbots.” [judgment] Change this to “other target models, including proprietary chatbots and open-weight Llama-2,” in Message/Reading/Script. Explain transfer as not optimizing on those target models; no target gradients were used for this suffix. Reason: open weights versus black-box use are different, central threat-model axes. E59. Flag the main slide's closed-model shorthand without editing the deck.

46. **F46 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:440` — lec10/S22, p22.
   The reading converts lower later KL into unchanged distributions and calls the measured dataset plot one harmful reply. [judgment] Explain that the comparison uses the same harmful prefixes in each pair of models, evaluated on Harmful HEx-PHI; later KL is substantially smaller but still nonzero. “KL0” means equal conditional distributions; do not call the displayed later steps unchanged. Reason: this preserves the shallow-alignment finding without falsely teaching equality or a single-example result. E58.

47. **F47 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:1003` — lec10/S49, p49; `courses/trustworthy-ai/lec10-jailbreak-note.html:1068` — lec10/S52, p52.
   Message at S49 makes likelihood itself the power law, while the fitted quantity is NLL; its new Reading also fails to distinguish the two evaluations. [judgment] Say “NLL falls approximately as a power law over the tested range,” and explicitly identify right-hand psychopathy evaluation as separate from left-hand malicious-use-case percentages. At S52 likewise attach the power-law fit to negative-log ASR, not literal ASR. Do not describe every empirical curve as exactly a fitted straight line. Reason: the axis transformation and different tasks determine what can be inferred. E60.

48. **F48 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:1518` — lec10/S74, p74.
   “These are the reported attacks, not adaptive ones” incorrectly excludes the original target-aware search/white-box evaluations. [judgment] Replace with “These are the authors' tested attacks and settings, not a guarantee against better-tuned or stronger attacks.” Keep the later optimization counterexample, and don't label all original attacks fixed or non-adaptive. Reason: the next slide improves the same input-embedding attack, rather than introducing target optimization for the first time. E61.

49. **F49 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:83` — lec10/S05, p5; `courses/trustworthy-ai/lec10-jailbreak-note.html:102` — lec10/S06, p6.
   “one shared trick works for every user … for months” and “works for anyone who copies it” upgrade availability to guaranteed success and online longevity to continuous efficacy. [judgment] Say “a published prompt is cheap for many users to try; some tested prompts remained effective on dated model versions.” Keep 240+days explicitly as time online, and qualify effectiveness by model/version/request. Align Script. Reason: the source itself shows large snapshot-dependent drops, matching the lecture's later reproducibility lesson. E62.

50. **F50 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:1297` — lec10/S64, p64.
   Message says “The judge moved, not the safety,” which is stronger and less accurate than its retained explanation. [judgment] Replace with “The measured score changed with reply length; this does not establish that the replies became safer.” The substring rule stayed fixed, and this experiment does not measure constant underlying harm. Reason: absence of evidence of safer output is not evidence of unchanged safety. E63.

51. **F51 | unmet request | blocking.**
   **Where:** `courses/trustworthy-ai/lec10-jailbreak-note.html:513` — lec10/S25, p25.
   “mean of 3 runs” omits the GCG selection rule. [judgment] Add to Reading/setup that the GCG result averages the 3 highest-ASR runs selected from 10 optimization trials, per Appendix A.4; do not apply this selection claim indiscriminately to every row. Reason: the lecture explicitly requires search budget and denominator for interpreting ASR. E58.

52. **F52 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec11-synthetic-media-note.html:672` — lec11/S34, p34.
   The opening and first Script explanation turn human-looking paraphrase into small TV, although the later caveat correctly makes that conditional. [judgment] Replace with “If paraphrasing makes the full-text distribution close to human text in TV, the bound forces every single-text detector near chance; looking human alone does not establish this.” Call the drawn curve an AUROC upper bound. Reason: the theorem's hypothesis is not visual plausibility or a proved property of any paraphraser. E67.

53. **F53 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec11-synthetic-media-note.html:1324` — lec11/S67, p67.
   [judgment] Reading's “systems already on the market by 2 Dec 2026” merges the eligibility date with the compliance deadline. Change to “systems placed on the market before 2 Aug 2026 must meet Art. 50(2) by 2 Dec 2026,” matching S65 and the quoted amendment. Reason: the new summary must not extend the transition to newer systems. E69. Keep the dated legal framing and scope/exception detail.

54. **F54 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec12-fairness-note.html:235` — lec12/S10, p13.
   “It also removes the ability to measure the gap” confuses excluding a feature from prediction with discarding the audit attribute everywhere. [judgment] Say that auditing and group-aware mitigation require group labels in the relevant data; removing them from model inputs does not prevent retaining them separately for an audit. Qualify the Script and “makes them impossible” detail consistently. Reason: otherwise the note teaches an unnecessary conflict between a group-blind predictor and a group-aware audit. E75.

56. **F56 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec12-fairness-note.html:958` — lec12/S39a, p52; `courses/trustworthy-ai/lec12-fairness-note.html:976` — lec12/S39b, p53.
   The opening, Reading, Script and source locators repeatedly call Fig. 4's data “training data” while describing substantial residuals after exact cell reweighing. [judgment] Identify the plot as transformed evaluation data, not model predictions; explain that fitted training-cell reweighing equalizes the weighted table, while applying learned weights to held-out data can leave residual disparity. The test-partition interpretation is supported by §10/Appendix B; do not claim the exact historical Fig. 4 generator was recovered. Cite §10's test-partition protocol and Appendix B.4–5 rather than claiming the plot measures failure of exact training balancing. Reason: the current narrative contradicts the preceding worked reweighing example. E77. Flag the inherited main “training data” caption; no deck edit authorized. If the executor has the exact historical Fig. 4 generator establishing a different partition, return that evidence before choosing wording.

58. **F58 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec01-introduction-note.html:257` — lec01/S13, p13.
   The September 2026 status still says the €15M fine is under appeal with outcome unverified, while lec02/S20 correctly reports the March 2026 first-instance annulment. [judgment] Keep the historical suspension/fine, add the annulment in the short reading, and replace the stale status paragraph with the first-instance outcome and unverified further-appeal status. Cite the Garante notice directly. Reason: the two lectures currently teach incompatible timelines. E78.

59. **F59 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:804` — lec02/S43, p43.
   “Every DP mechanism” → “For additive-noise mechanisms such as Laplace/Gaussian releases, the recipe is compute the statistic, add calibrated noise, then release.” [judgment] Explain that the slide is a recipe for this mechanism family, not the definition of all DP; the exponential mechanism is a counterexample to the universal recipe. Align Script. Reason: students otherwise learn a false taxonomy. E16/E85.

60. **F60 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec02-privacy-dp-note.html:351` — lec02/S17, p17.
   “a positive result proves leakage” is ambiguous between one predicted member and a successful evaluated attack. [judgment] Replace with “a statistically supported attack advantage is evidence of leakage in the tested setup; one positive flag can be wrong, and failure to detect leakage is not a privacy certificate.” Align Script and preserve the valid testing bound. Reason: this is the distinction needed by the later audit/unlearning lectures. E85.

61. **F61 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:428` — lec05/S29, p29; `courses/trustworthy-ai/lec05-unlearning-note.html:446` — lec05/S30, p30; `courses/trustworthy-ai/lec05-unlearning-note.html:1062` — lec05/S64, p64.
   The retained proof's assumptions and retraining convention are incomplete. [judgment] State that the M-Lipschitz-Hessian bound applies to the retained objective used by the Newton step (or impose sufficient per-loss bounds); remove unrestricted ridge regression from the bounded-gradient examples, or state an appropriate bounded parameter domain. Explicitly keep original-n normalization and regularizer in the reference retrainer; do not silently equate it with ordinary n−1 averaging at fixed lambda. For the Gaussian comparison, specify the same Gaussian noise distribution (matching covariance) for the retrained reference and the edited output, plus the range for the cited classical noise formula (0 < epsilon < 1, 0 < delta < 1), rather than noise versus a deterministic point. Reason: the displayed O(1/n²) argument is sound only under its actual hypotheses. E81.

62. **F62 | fact | blocking.**
   **Where:** `courses/trustworthy-ai/lec06-hallucination-note.html:196` — lec06/S14, p14; `courses/trustworthy-ai/lec06-hallucination-note.html:258` — lec06/S17, p17; `courses/trustworthy-ai/lec06-hallucination-note.html:327` — lec06/S21, p21.
   The retained theory overextends arbitrary-fact bounds to real citation/biography data. [judgment] S14: define Mis_b using the source's g-dependent adaptive partition, not “nearest” coarsening; keep correction terms in the informal reading and use §§3.2/5/6/8 for the current paper. S17: remove the unsupported assertion that real citations are typically singleton and therefore theorem-forced; present a hypothetical arbitrary-fact setting instead. S21: state the random-independent-answer model and calibration/correction conditions, and separate it from the FActScore observation. Reason: a conditional mathematical result is not an empirical error floor for these datasets. E83.

63. **F63 | unmet request | blocking.**
   **Where:** `courses/trustworthy-ai/lec05-unlearning-note.html:901` — lec05/S55, p55; `courses/trustworthy-ai/lec06-hallucination-note.html:1058` — lec06/S71, p71.
   Two new plot readings still do not read their exhibits correctly. [judgment] S55: “close to the target on every axis” → “syntactic examples generally exceed topical examples on similarity and relearning in these tests”; explicitly avoid calling the NPO gradient bar (~0.4 vs target 1) nearly equal. S71: replace “per the slide's alt text” with the actual key: dots are posterior medians, lines 50%/95% credible intervals, 50% is neutral; matching beliefs is strongest in this fitted analysis, not a universal causal ranking. Reason: C02 asks for a usable explanation of the displayed comparison, not an alt-text paraphrase. E41–42.

## Nonblocking refinements — slides decides
These four items alone do not start another review round. Report accepted or declined; do not treat any other discarded draft suggestion as a hidden requirement.

55. **F55 | fact | nonblocking.**
   **Where:** `courses/trustworthy-ai/lec12-fairness-note.html:478` — lec12/S19b, p27.
   [judgment] “The two would coincide” can imply equivalence. Replace with the Script's precise one-way statement: with two shared score values and only the top bucket selected in both groups, calibration implies equal PPV; the converse need not hold. Reason: equal PPV does not calibrate every bucket. E71. The main mathematical example and existing Script are correct; this item alone would not start another round.

57. **F57 | unmet request | nonblocking.**
   **Where:** `courses/trustworthy-ai/lec11-synthetic-media-note.html:1432` — lec11/S73, p73.
   [judgment] “rarer AI content means more false flags” → “at fixed true- and false-positive rates, rarer AI content means a larger fraction of flags are false.” Reason: preserve the main slide/Script's denominator and held-fixed condition in the short message; do not confuse counts with the false-discovery share. E75. This item alone would not start another round.

64. **F64 | fact | nonblocking.**
   **Where:** `log/2026-11-15-lec01-lec12-notes/work-r1.md:145` — record only, no slide/page.
   The claimed verbatim restoration from 9a772bd is not supported: that revision still has the truncated sentence, and the repair is at lec03/S66/p66, not S49. In work-r2, correct the provenance/location or identify the actual source revision; do not edit frozen work-r1. Reason: preserve an auditable repair history. The repaired mathematics itself was checked and accepted.

65. **F65 | preference | nonblocking.**
   **Where:** Multiple entries; exact locations in the subitems below.
   [judgment] Optional source, provenance and spoken-cue cleanups; these do not change scope or time:
   1. `courses/trustworthy-ai/lec05-unlearning-note.html:517` — lec05/S33, p33: add the Kurmanji NeurIPS 2023 URL in E42, so the method has a direct source.
   2. `courses/trustworthy-ai/lec06-hallucination-note.html:1029` — lec06/S69, p69: pin the verified 22 September 2026 README from E84 instead of relying only on a moving leaderboard; the six historical rows are correct.
   3. `courses/trustworthy-ai/lec12-fairness-note.html` — S19b/p27:L494; S20b/p29:L534; S23a/p33:L603; S25/p36:L673; S26a/p37:L694; S26b/p38:L716; S30/p42:L786: “Definition 2.2” → “Definition 2 (Eq. 2.2)” (E71); use the paper's actual definition/equation labels.
   4. `courses/trustworthy-ai/lec12-fairness-note.html:397` — lec12/S17a, p23; `courses/trustworthy-ai/lec12-fairness-note.html:419` — lec12/S17b, p24: remove retained claims that the panel title was removed; the current slide and render keep it.
   5. `courses/trustworthy-ai/lec08-adversarial-note.html:1153` — lec08/S66, p66: remove the duplicate eight-times-compute Assumptions paragraph; keep the calculation at S67, where it belongs.
   6. `courses/trustworthy-ai/lec10-jailbreak-note.html:1233` — lec10/S60, p60: “Twenty minutes” → “This section,” preserving the 17.5-minute schedule; this corrects an obsolete spoken cue, not teaching time.

## Plan-issue and source decisions
`plan-v2.md` records decisions for all 12 work-r1 plan issues and the source flags; its per-entry correction map overrides inaccurate plan-v1 seeds. Main-slide changes remain deferred, not silently approved.

Closed checks with **no new blocker**: semantic-entropy Methods/LLN wording (E82); named Korean oversight with high-impact scope (E78); Bartz approval and both official docket prefixes (E79); Vectara's exact September 22 snapshot (E84); qualified lec05 legal discussion (E80); SISA reference convention; lec06 worked conformal set and relative IDK payoff; METR footnote and existing transcript-run disclosure; Cohen table-source discrepancy. F56 deliberately retains the unrecovered exact Fig. 4 generator limitation: §10 and Appendix B support the evaluation/test-partition interpretation, not a claim of recovered code.

## Revision handoff and acceptance
Implement only the blocking corrections plus any explicitly chosen nonblocking refinements. Keep source limits in the short layer and full support underneath; do not rewrite the 902 entries again. Report each F01–F65 as fixed, declined (nonblocking), or disputed with evidence. Work-r2 must name the exact commit, changed IDs/pages, source/plan deviations and checks. The owner will review changed entries and their neighbours, not repeat the completed first pass. At round 2's limit, unresolved blockers are escalated to Albert. No PR until approval and pushed job records; no merge without Albert's direct order.
