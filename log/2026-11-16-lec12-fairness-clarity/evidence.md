# Evidence register

Append-only. Verified 2026-11-16 against primary texts except entries explicitly unresolved. Baseline is 6f5088cdfc7877ea7965b972df91c8447562b5f4. Page/figure references below belong to the named source version. A teaching construction is not a published measurement.

## E01 — Importance-photo claim: not verified
- Claim: changing only apparent race/gender changes the selected person even with importance independently defined.
- Sources inspected: Howard et al., CVPR 2024, SocialCounterfactuals, https://openaccess.thecvf.com/content/CVPR2024/papers/Howard_SocialCounterfactuals_Probing_and_Mitigating_Intersectional_Social_Biases_in_Vision-Language_Models_CVPR_2024_paper.pdf (abstract/introduction; also arXiv 2312.00825v2); targeted searches for important-person selection and controlled identity swaps.
- Result: related counterfactual occupation/image-retrieval research exists, but this does not establish Albert's specific importance-selection experiment. The baseline S77 photo is explicitly a thought experiment, with no model output.
- Limit: not evidence that no such paper exists. No speculative substitution or invented test.
- Label: unresolved. Decision: remove S77 as Albert permits; do not replace with an adjacent claim presented as the remembered experiment.

## E02 — Kangwook post: user-provided motivation, not verified evidence
- URL: https://x.com/Kangwook_Lee/status/2084373047755354188 (parameters in C03).
- Direct web access returned 403; searches did not recover a verifiable primary copy. The reported “ceo reveal” behavior is Albert's description, not an independently verified run, frequency or model/version.
- Label: unresolved. Use E03's published occupation outputs for the opening, as C03 explicitly suggests. Do not label them as the X post, CEO-reveal generations, or evidence about its unknown model.

## E03 — Published occupation outputs
- Source: Bianchi et al., FAccT 2023, arXiv 2211.03759v2, https://arxiv.org/pdf/2211.03759v2, §2.2, Figures 3–4 and appendix methodology.
- Setup: Stable Diffusion v1.4, occupation-face prompts, 100 outputs per occupation. Figure 3 displays random samples. The paper's software-developer comparison is 99% model-represented White versus 56% self-identified White in its historical US labor comparator. CLIP-based closest group archetypes are a measurement proxy, with separate gender and race comparisons, not six intersectional categories.
- Limit: a displayed row is not an estimated frequency; CLIP assignments are not self-identification. The output comparison does not measure the training distribution, identify a training-data causal mechanism, or establish all current models behave this way.
- Label: published result. Reuse existing figure crops; preserve historical model/version and proxy caveats.

## E04 — Statistics do not alone settle fairness
- Sources: Chouldechova, Big Data 2017, https://arxiv.org/pdf/1703.00056, §1, pp.1–2 (fairness/social context); Hardt, Price, Srebro, NeurIPS 2016, https://arxiv.org/pdf/1610.02413v1, §§1–3 (criteria and limitations); E03 for the representational example.
- Claim: different statistical criteria answer different questions; choosing the relevant harm and criterion requires context. Empirical association is not by itself a justification for a harmful decision or stereotyped portrayal.
- Limit: the lecture should not assert that every correlation or unequal output is necessarily unfair, or infer discriminatory intent. Representation and allocation are related fairness concerns, not identical measured outcomes.
- Label: published conceptual framing plus explicitly normative teaching interpretation, not an experimental finding.

## E05 — Cost versus need, and the allocation consequence
- Source: Obermeyer, Powers, Vogeli, Mullainathan, Science 366 (2019), DOI 10.1126/science.aax2342; primary article copy https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf, article pp.2–4, Figures 1 and 3.
- Claim/setup: at a given algorithm score, Black patients had greater illness burden, while costs were broadly similar. At comparable health need, spending was lower for Black patients. Cost-based ranking therefore understated their need for extra care. The study discusses access barriers and provider/patient interactions; it does not isolate delayed hospital attendance to avoid bills as the sole cause.
- Thresholds: above 55th percentile screening referral; above 97th automatic identification. Same score means the same score-based rule, not different treatment because of race at that exact score. The unfairness is need misranking.
- 17.7%→46.5% is a simulated change in the Black share selected, not measured health benefit or a deployed fix.
- Label: published result. Prefer “similar cost prediction did not mean equal need assessment” over categorical perfect calibration.

## E06 — What the face datasets test
- Source: Buolamwini & Gebru, FAT* 2018, https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf, §§3.2–3.3, Table 2, §4/Table 4.
- IJB-A is a face-recognition benchmark; Adience an age/gender-classification benchmark. Their composition is audited; they are not all the same task. PPB (Pilot Parliaments Benchmark) is the balanced evaluation set used to audit commercial binary gender-classification systems, with gender categories as operationalized in that study, not identity recognition or inference of true identity.
- Published lighter-skin shares: IJB-A 79.6%, Adience 86.2%, PPB 53.6%; PPB n=1,270.
- Limit: composition bars are not accuracy bars and do not prove the cause of error gaps. These are test/audit datasets here, not a claim about vendor training sets.
- Label: published result.

## E07 — Binary criteria and ROC reading
- Source: Hardt, Price, Srebro, NeurIPS 2016, https://arxiv.org/pdf/1610.02413v1, §2, Definitions 2.1–2.2, §4 and Figure 1.
- Demographic parity compares selection rates over everyone; equal opportunity compares TPR (positive decisions among Y=1); equalized odds requires both TPR and FPR equality in the binary case. These are definitional requirements for that criterion, not necessary conditions for every moral notion of fairness. TPR equality also equals FNR equality when denominators exist.
- ROC: x=FPR, y=TPR. Equalized odds uses the same attainable point; equal opportunity only requires matching y-coordinates. Attainable sets include randomized decisions. Upper-left is better prediction for these axes, not a context-free ethical optimum.
- Limit: fully labeled evaluation assumptions matter; actual rejected loan applicants have unobserved counterfactual repayment. Hardt does not solve that identification problem by defining a rate.
- Label: published definitions; lending translation is a teaching interpretation.

## E08 — Synthetic lending counts and missing outcomes
- Label: illustrative example / our calculation, not empirical loan data.
- Inputs in baseline generator `courses/trustworthy-ai/figs/lec12-visual-motivation/criteria_examples.py`: A (TP,FP,FN,TN)=(3,1,3,3); B=(1,3,1,5). Both selection 4/10, TPR 1/2; FPR 1/4 versus 3/8; PPV 3/4 versus 1/4. Equalized-odds construction instead has 10 positive and 10 negative per group, TP=8, FP=2.
- Interpret Y for the lending teaching population as “would repay if granted this loan”; all labels are stipulated. Y-hat is approval/positive prediction. Not selected means denied, not missing from the training set. In real data, denial does not establish non-repayment and those unobserved Y cannot simply be counted as negatives.
- Generator changes, if needed, belong to slides. Preserve fixed numeric inputs and record any new generator path in work-r1 and an evidence addendum.

## E09 — Calibration is not selected-pool precision
- Sources: E07 §2.2; Chouldechova https://arxiv.org/pdf/1703.00056, Definition 2 and discussion after Eq.(2.2); baseline `criteria_examples.py`.
- Illustrative inputs (people, positives): A at scores .9/.6/.2=(20,18)/(10,6)/(10,2); B=(10,9)/(20,12)/(10,2). Each score bucket is calibrated. Threshold >.5 selects 30 of 40 per group; A positives 18+6=24, B=9+12=21, so PPV .8 versus .7.
- Our calculation: selected score weights A=(2/3,1/3) and B=(1/3,2/3) on (.9,.6); weighted averages .8 and .7. The .2 bucket is excluded, not part of either denominator.
- Limit: equal numeric calibration does not imply equal PPV at a shared threshold. One shared selected score can give equality; three values show failure of the general implication. No real lending dataset is involved.
- Label: published distinction + illustrative exact calculation. Regeneration: `criteria_examples.py`; new explanation may extend this generator.

## E10 — COMPAS, vendor, base rate and impossibility
- Source: Chouldechova, Big Data 5(2), 2017, https://arxiv.org/pdf/1703.00056, p.1 footnote, §§1.2/2.1/2.3, Eq.(2.6).
- Northpointe Inc. developed COMPAS; name its historical role, not a dataset or criterion. The audit label is recorded two-year recidivism/rearrest, not all offending, conviction or future guilt. Base rate is P(Y=1|group), out of the whole evaluated group, not the flagged subset; source rates are about 51% Black and 39% White in its filtered sample, not the lecture's synthetic 50%/25%.
- Identity: FPR=[p/(1-p)]·[(1-PPV)/PPV]·(1-FNR). Under 0<p<1, defined positive selection, 0<PPV<1 and TPR>0, unequal p prevents simultaneous equal PPV, FPR and FNR. Calibration is not a premise; FPR is merely the variable isolated algebraically, not a preferred ethical target.
- Limits: exact arithmetic theorem differs from approximate empirical parity. Degenerate/undefined rates require separate handling; do not call the source a universal “all fairness impossible” theorem.
- Label: published result.

## E11 — Worked calibrated audit and compatible exceptions
- Label: illustrative example / our calculation. Baseline regeneration: `courses/trustworthy-ai/figs/lec12-visual-motivation/calibrated_errors.py`.
- Baseline input: 60 per group. A high-score (positives,negatives)=(24,6), low=(6,24); B high=(4,1), low=(11,44). Scores .8/.2, flagged if >.5. Base rates .5/.25; PPV .8 both; FPR .2 versus 1/45; FNR .2 versus 11/15. These are fictional recorded rearrest outcomes for explanation, not the source's sample rates.
- New equal-base-rate construction: each group TP=8,FP=2,FN=2,TN=8, so p=.5, PPV=.8,FPR=.2,FNR=.2 all match despite mistakes. This shows possibility, not automatic equality whenever base rates match. A perfect predictor is another possible exception even with unequal base rates. PPV=1 plus equal nonzero TPR can also match all three with FPR=0, without perfect recall.
- Do not use the undefined PPV of an always-negative classifier as a solution. slides must provide deterministic regeneration for any new numeric figure in the work report.

## E12 — Reductions mechanism, not an added fairness detector
- Source: Agarwal, Beygelzimer, Dudík, Langford, Wallach, ICML 2018, https://proceedings.mlr.press/v80/agarwal18a/agarwal18a.pdf, §§3.1–3.3, Algorithm 1, Examples 3–4.
- A constraint's current penalty produces costs for predicting 0/1 on each training example; refit a cost-sensitive classifier; evaluate violations; update the penalties; output a distribution over fitted classifiers (average play in Algorithm 1). This is repeated ordinary fitting under changed costs, not one auxiliary classifier that detects/proves fairness and not necessarily the last fit.
- The protected attribute is needed to measure training constraints. It need not be an inference input in the general method, but was included among features in this experiment (E13). A cost-sensitive oracle is the general requirement; “any learner with unchanged labels and weights” is too broad. Auxiliary weighted-classification encodings may relabel working examples; the underlying observed target is not thereby repaired.
- Limit: finite-sample and approximate optimization guarantees have assumptions; no guarantee every successive fit reverses bias or monotonically improves fairness.
- Label: published result.

## E13 — The actual reductions experiment
- Source: E12 §4 and Figure 1, printed pp.7–8.
- Displayed top-row panels are demographic parity with logistic regression: Adult predicts income >$50k with gender attribute; COMPAS predicts recorded recidivism with race attribute (Black/White subset). Random split 75% training /25% test. Sweep tolerances ε from .001 to .1; train exponentiated-gradient reductions; evaluate resulting models/mixtures on test data alongside unconstrained, postprocessing, reweighting and relabeling baselines. Protected A included in X for all methods for comparability.
- x is the paper's maximum group-versus-overall deviation in positive prediction rate, not automatically the pairwise group gap. y is test classification error. Figure uses a convex envelope of classifiers obtained during training across tolerance choices; shaded 95% band is uncertainty in classification error, not variation across every fairness axis.
- Limit: empirical tradeoffs, not a certified optimum; income prediction is not observed loan service profit. Adult and COMPAS use different outcomes/populations, not a controlled dataset-only intervention.
- Label: published result.

## E14 — Mixture feasibility
- Label: our calculation / illustrative example linked to E12's randomized prediction.
- Existing regeneration: `courses/trustworthy-ai/figs/lec12-visual-motivation/reductions_mix.py`. h1 selection (A,B)=(.8,.4), h2=(.2,.6), half weights yields (.5,.5). Signed gaps +.4 and −.4 average to zero.
- A candidate pool whose gaps are all strictly positive cannot attain exactly zero by any nonnegative mixture. New counterexample h1=(.8,.4), h2=(.6,.4): mixtures have gap between .2 and .4. Zero can be reached if the convex hull of candidate gaps includes zero; a zero-gap member also suffices. More constraints require simultaneous feasibility, not one scalar sign test.
- Costs in E12 intentionally change incentives to seek useful alternatives; random restarts alone need not supply them. Never promise an arbitrary useful opposite-bias pair. A trivial constant classifier may meet demographic parity but sacrifice utility.
- New figure inputs/path must be recorded by slides; may extend `reductions_mix.py`.

## E15 — Constrained lender profit
- Source: Hardt et al., https://arxiv.org/pdf/1610.02413v1, §7, Figures 9 and 11, pp.17–21.
- “Profit-optimal equalized odds” maximizes modeled lender profit among decision rules satisfying equal TPR and FPR across the specified groups. Thresholds/randomization implement the constraint. It does not mean largest profit over all unconstrained rules.
- At break-even non-default probability .82, paper reports fractions of unconstrained maximum: single threshold .993, opportunity .928, odds .802, demographic parity .698. These are historical modeled comparisons, not general empirical loss percentages for all service providers.
- Our optimization inference: restricting a fixed feasible set cannot improve its globally optimized value under the same objective/data, but equality is possible. An imperfect practical baseline can be improved; social welfare and long-term value are not this objective.
- Label: published model result + elementary optimization inference.

## E16 — AIF360 before/after are separate method evaluations
- Source: Bellamy et al., arXiv 1810.01943v1 (2018), https://arxiv.org/pdf/1810.01943v1, §10, Table 2, Figure 5(b), Appendix B.
- Nine alternatives, not a nine-stage pipeline: reweighing, optimized preprocessing, fair representations, disparate impact remover; adversarial debiasing and prejudice remover; equalized-odds postprocessing, calibrated equalized-odds postprocessing, reject-option classification. Seven use LR/RF pairs; adversarial uses NN and prejudice remover LR.
- Adult/race; train/validation/test=50/20/30%; 25 random splits, means±1 SD. Validation chooses balanced-accuracy-maximizing thresholds where applicable; test reports performance. Balanced accuracy averages TPR and TNR. DI is unprivileged/privileged positive-prediction rate, ideal 1; define source groups in note.
- Different preprocessing for disparate impact remover and adversarial debiasing causes different before baselines. No universal baseline, single mitigation, equal cost, or optimal frontier.
- Label: published result. Preserve original Fig.4 provenance as unrecovered if mentioned; this job does not claim to recover that historical generator.

## E17 — “A biased label stays biased” is not “mitigation is useless”
- Sources: E05's cost/need distinction, E12's target-preserving constrained objective, E16's method distinctions; baseline named interventions reweighing/reductions/group thresholds.
- These three illustrated interventions change weights, a predictor or a decision rule; they do not establish that recorded cost equals need or rearrest equals offending. Improved parity against recorded Y does not validate Y as the intended target.
- Limit: do not generalize to all fairness methods, claim none can relabel data, or claim nothing improves. Auxiliary relabeling is not recovering the desired ground truth. Target/measurement redesign requires domain evidence beyond rate constraints.
- Label: source-grounded conceptual distinction.

## E18 — BBQ: context sufficiency, not confidence
- Source: Parrish et al., Findings of ACL 2022, https://aclanthology.org/2022.findings-acl.165.pdf, Figure 1, §3, §5, Figure 3.
- Ambiguous=the given context lacks the fact needed to decide between the two named candidates; correct answer Unknown. Disambiguated=added information makes one candidate correct. These terms describe input evidence, not whether the model feels certain, text is grammatically unclear, or the answer follows a stereotype.
- Figure 1's negative-question example: both men seen fleeing initially; later evidence says the Christian man confessed. Answer must follow the added evidence, not religious stereotypes. Label the fictional benchmark scenario, not a real crime.
- s_DIS=2(n_stereotype/n_nonunknown)−1; s_AMB=(1−accuracy)s_DIS, reported ×100. Compute within the appropriate condition, not by borrowing the disambiguated panel's numeric score for the ambiguous panel. Handle all-Unknown as zero ambiguous bias; other undefined ratios explicitly.
- Limit: scores describe directional response patterns, not real-world harm rates or interchangeable scales. Zero directional bias does not establish accuracy.
- Label: published definitions and example.
