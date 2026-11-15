# Supplemental final review r3 — FINAL

Reviewed commit: `ef453a8abd3d04449e71de1d61d9d9071e16f632`
Original baseline: `99450923b41e94f10d0c557a4fc0f46b42a9c91d`
Incremental comparison: `594ebea1203aabe3b3edc56443b37dd29950e411` (verified ID-only) against extension baseline `6dc56441c8294d20e53976aa25393ea38d408d08`.
Branch/job: `2026-11-15-lec01-lec12-notes`
Verdict: **revise**. Job state: **escalated**. Ordinary rounds 2/2 and authorized supplemental 1/1 are exhausted. **No automatic r4, implementation order, PR or merge authorization.** Albert decides the next step.

## What matters
1. **Guarantees still exceed their assumptions.** Pure versus approximate DP is mixed across lectures; the retained DP-SGD noise theorem fails a concrete counterexample; finite sample agreement still becomes population certainty. F70/F73/F74/F34.
2. **Some retained text contradicts the improved explanations.** PII denominator, unlearning targets/retraining references, SimpleQA causality, medical-error attribution and HF duration need consistent repairs through every layer. F69/F78–F81/F101.
3. **Three attack findings use the wrong evaluation scope.** GCG was optimized for each model; the >85% deception summary is not oversight-only; Prompt Infection's failure breakdown is not an unconditional resistance rate and has a data-theft exception. F85/F93/F97.

The message → explanation → detail hierarchy is substantially clearer. Preserve the repaired plot readings, source caveats, conditional guarantees and default type. Five of the six previous residual groups close; F34 alone remains from r2. The remaining issues are accuracy/consistency, not a request to rewrite the 1,006 articles or restructure the course.

**Final finding count:** 13 blocking groups (12 newly numbered, plus residual F34); 21 nonblocking groups. New IDs F69–F101 remain stable. “Nonblocking” does not mean a factual sentence is endorsed: it distinguishes local/inherited subsidiary precision from the defects preventing acceptance. Preferences are slides' call. Every correction below is contingent on Albert authorizing further work.

## Request coverage
| Request | Final disposition | Evidence / remaining gap |
|---|---|---|
| C01: lec01–12 companions | Format done; accuracy not fully accepted | Original 902-entry opening-layer review retained; 93 changed old articles fully reviewed in r3. Residual F34 and new factual groups remain. |
| C02: clear brief point, exhibit explanation, then detail | Structure done; cross-layer accuracy incomplete | Openings are substantially clearer; blockers identify exactly where retained/detail/main claims disagree. |
| C03: check all; pause only at an actual provider limit | Done for authorized review scope | Durable checkpoints; no reported actual quota limit, no fabricated reset or provider switch. |
| C04: render and check original sources as needed | Done, with explicit limits below | 197 changed articles, matching mains/neighbours and targeted primary sources; scheduled visual inspection complete. Not every inherited citation or lower paragraph was freshly re-audited. |
| C05: same treatment for lec13–14 | 104/104 articles done; accuracy not fully accepted | F93/F97 block; subsidiary locators/qualifiers F87–F100 remain nonblocking. |
| C06: correct mains across lec01–14 | Partial | 84 changed mains reviewed; several unresolved main/note source conflicts. F101 also disproves blanket agreement for unchanged pairs. |
| C07: update canonical notes rule | Done | DESIGN_SYSTEM §9, PLANNER_BRIEF pointer and leaf notes/ID description agree; optional document locators F72/F94 and factual cross-layer F101 recorded. |
| C08: same branch and PR | Done so far | Same branch/job, no PR opened. One eventual PR only after approval and verification of pushed log-only follow-up commits. |

## Completed audit and limits
Review order: original requests C01–C08 → primary evidence → DESIGN_SYSTEM §§1/2/5/6/8/9/10 and leaf outline → plan-v3. The plan is not evidence.

| Lecture | Ordered pairs | Changed mains | Full changed articles reviewed | Scheduled main images inspected |
|---|---:|---:|---:|---:|
| 01 | 46 | 10 | 10 | 23 |
| 02 | 69 | 15 | 17 | 37 |
| 03 | 70 | 5 | 5 | 13 |
| 04 | 65 | 10 | 10 | 26 |
| 05 | 68 | 13 | 17 | 32 |
| 06 | 75 | 6 | 6 | 14 |
| 07 | 75 | 6 | 7 | 14 |
| 08 | 101 | 5 | 6 | 15 |
| 09 | 91 | 3 | 3 | 9 |
| 10 | 88 | 5 | 8 | 13 |
| 11 | 74 | 1 | 1 | 3 |
| 12 | 80 | 2 | 3 | 4 |
| 13 | 53 | 1 | 53 | 3 |
| 14 | 51 | 2 | 51 | 6 |
| **Total** | **1,006** | **84** | **197 = 93 old + 104 new** | **212** |

- All 197 changed articles were read in full, with matching main/alt text and immediate neighbours. Targeted unchanged articles named in E99–E145 were also checked; final shared-doc tracing added full lec01 S23/main text. This was not a restart of all 902 old entries or an exhaustive reread of all unchanged retained prose.
- Visually inspected all 212 scheduled main images, 71 additional main images and all 197 changed-note desktop openings, plus the documented narrow/selected-region checks. Artifacts and source figures are under scratch `review/2026-11-15-lec01-lec12-notes/r3/`. Capture alone was never counted as inspection. Glyph-loss artifacts were resolved with native navigation, animation waits and repaint; some alternate images still have artifacts. No confirmed new visual regression. Lower lec05 S41 formulas have source/DOM checks, not screenshot verification; long articles were not entirely screenshot-inspected.
- All 28 canonical files and four shared documents independently byte-match the exact commit. All 1,006 ordered ID pairs/counts remain; no moves/splits. All 14 notes lint clean; main warnings remain baseline-equivalent. Existing browser metrics at 1100/430px show no new/worsened note overflow, not zero inherited overflow. No type shrinking or reference/script/tech changes introduced.
- All 390 local href/src/xlink occurrences resolve, including fragments (57 in notes). No external link occurrence lost; the sole new URL, SciPy ks_2samp, returned HTTP 200. Existing targeted source checks E99–E141 plus final E145 support the findings; not all inherited external URLs/papers were freshly checked.
- Doc-index lint passes. Outline lint here has five inherited basename warnings plus an absent executor-local historical build-script path; it is not a new tracked-file regression. F72 records two semantically off-by-one pointers lint cannot detect. Final shared-doc check adds inherited Kwa/Greenblatt locators to F94 and the HF cross-layer contradiction to F101.
- Three changed titles match their notes; contents/divider sequence and pacing metadata are unchanged. Lec13/14 retain 53/51 entries and 90 minutes each, no activities. Title-only arcs still move from setup through evidence/limits to synthesis. No new narrative restructure or teaching-time change requested.
- All work issues 1–7 are adjudicated below. Frozen plan-v3/review-r2 hashes are unchanged (E143). No source/notes/reference/scripts were edited by slides-review.

## Blocking finding index
Detailed numbered fixes follow. All are **fact / blocking yes**.
| ID | Slide IDs / pages | What is wrong → required correction |
|---|---|---|
| F69 | lec01 S12/p12 | Wrong PII denominator → tested attack generations, not memorized outputs. |
| F70 | lec01 S42/p42 | Missing technical hypotheses → scope DP, watermark null and fairness conditions. |
| F73 | lec02 S27/S33/S36/S39/S41; lec03 S49; lec04 S53 (same pages) | Approximate DP treated as pure → retain delta and label pure illustrations. |
| F74 | lec02 S57/p57 | False unrestricted DP-SGD theorem → valid conditional theorem or explicitly bounded heuristic. |
| F34 | lec06 S57/p57 | All finite samples agree → empirical frequency/entropy, not population certainty. |
| F78 | lec06 S20/p20 | Cross-model SimpleQA totals called a causal intervention → descriptive comparison only. |
| F79 | lec06 S08/p8 | Wrong paper and unsupported discovery/internal-mechanism story → actual Fig. 9 source and observed error. |
| F80 | lec05 S61/S63/S66 (same pages) | Retraining-reference/target taxonomy contradictions → distinguish targets and evidence requirements. |
| F81 | lec05 S09/S55 (same pages) | MIA/relearning overclaim → statistical evidence and matched retrained control. |
| F85 | lec10 S25/p25 | Claims no victim-specific GCG → acknowledge per-model optimization and bounded coverage. |
| F93 | lec14 S19/p19 | Broad deception summary assigned to oversight-only → name the cross-evaluation population. |
| F97 | lec14 S31/p31 | Failure breakdown called all-attempt resistance; missing exception → source ambiguity and data-theft exception. |
| F101 | lec01 S23/p23; leaf outline L188 | Campaign duration called internal access → separate 4.5-day campaign / roughly 2.5 days inside HF. |

## Detailed findings
All line numbers refer to the reviewed commit. Proposed content, wording and design decisions are marked `[judgment]`; they require slide-aware implementation, not context-free substitution. Paths and IDs delimit each finding; do not alter unrelated sources or frozen job files.

### F69 — lec01 S12/p12, retained PII denominator
Type: fact. Blocking: yes. Path: `courses/trustworthy-ai/lec01-introduction-note.html`, L244 (article starts L231).
1. Current: “16.9% figure is over generations the authors flagged as memorized, not over all outputs.”
Fix [judgment]: replace with “Among 15,000 tested attack generations, 16.9% contained PII verified against the auxiliary corpus; this is not the leak rate in normal use.” Keep L242's already-correct denominator. Reason: §5.4 counts tested attack generations, not only memorized outputs; current layers contradict each other (E100).

### F70 — lec01 S42/p42, technical preview hypotheses
Type: fact. Blocking: yes. All changes [judgment]. Path: `courses/trustworthy-ai/lec01-introduction-note.html`, S42/p42, article L976.
1. L988–990: after defining(epsilon,delta)-DP, “epsilon bounds the log-likelihood ratio any observer can accumulate” → explicitly restrict the outputwise bound to pure DP (delta=0), and explain approximate DP via its additive event bound; composition tracks both parameters. Reason: approximate DP permits rare arbitrarily revealing outputs (E101).
2. L1014–1016: unconditional exact Binomial null/quantifiable AI-generation FPR → “Under an ideal independent green-membership null, the count is Binomial(T,gamma); the z-test uses a normal approximation. Repeated n-grams require handling and empirical false-positive calibration; a large z is evidence for this watermark.” [judgment] Keep equation and supporting source; no need to expand the intro into a full detection lecture. Reason: actual seeded lists reuse assignments, and watermark detection is not universal AI detection (E101).
3. L1017: “With unequal base rates ... equal precision forces unequal error rates” → add the nondegenerate condition (shared PPV strictly between 0 and 1 and nonzero true-positive rate), preserving the separate Kleinberg statement. Reason: perfect prediction is a counterexample and is already distinguished in the course's qualified fairness explanations (E71/E101).

### F71 — lec01 S31/p31, inherited risk-pyramid sublabel
Type: design rule. Blocking: no (inherited secondary-label issue, not a regression or the slide's essential claim). Path: `courses/trustworthy-ai/lec01-introduction.html`, L681, slide L670.
1. The light “hiring · credit · health · courts” label extends beyond its blue shape and fades into white. Optional fix [judgment]: reflow/place the examples where they retain contrast without reducing type; retain the core high-risk label. Reason: examples should be readable when used to explain the tiers. E102/native render confirms; slides decides whether to take this optional cleanup.

### F72 — root outline inline pointers
Type: design rule. Blocking: no (minor introduced locator defect). Path: `OUTLINE.md`, L150–151; lec02 S38/p38 and S54/p54.
1. Restore `lec02-privacy-dp.html:803`→`:802` and`:1059`→`:1058`; headings remain at those previous lines while803/1059 are divider elements. Reason: DS§10 requires the existing inline-pointer convention to land on the named content. E102. Do not change section-table Location conventions or unrelated historical workspace links.

### F73 — Pure-DP illustrations are presented as approximate-DP guarantees
Type: fact. Blocking: yes. Evidence E101/E103. All instructions below are [judgment]; preserve the correct additive definition and the source's conditional claims.
1. `courses/trustworthy-ai/lec02-privacy-dp.html`, S33/p33 L686/L701/L707; paired `lec02-privacy-dp-note.html`, S33 L652/L655. “epsilon=0: output does not depend on data” and every-outcome2.7x odds → explicitly scope to **pure DP, delta=0**, with connected adjacency for dataset independence. Fixed positive delta is not enough. Keep comparisons at fixed unit/adjacency/delta/composition and the no-universal-good-epsilon caveat. Reason: approximate(0,delta)-DP can reveal the dataset rarely; the current endpoint is false. M11 omitted a qualification already present in E98; record this as a planning omission too.
2. `courses/trustworthy-ai/lec02-privacy-dp.html`, S36/p36 L767; paired note S36 L715/L718. “epsilon bounds a ratio ... nothing else” → “epsilon sets the multiplicative factor exp(epsilon); approximate DP also permits additive slack delta.” Reason: epsilon is the log factor, and the general guarantee is not ratio-only.
3. `courses/trustworthy-ai/lec02-privacy-dp.html`, S27/p27 L557–585, especially L584; paired note S27 L540–550. Mark the likelihood/posterior-odds illustration as pure DP with small epsilon; replace “No output can seriously contradict her” with “With small epsilon and delta=0, this release adds only limited evidence about her participation.” Keep the comparison between the stated adjacent dataset hypotheses. Reason: the existing technical label says pure DP but the main/Message/Script omit the essential scope; large epsilon is not strong deniability.
4. `courses/trustworthy-ai/lec02-privacy-dp.html`, S39/p39 L820; paired note S39 L753–758. “DP caps ... at exp(epsilon) in the odds” → “In this pure-DP illustration (delta=0), likelihood ratios are bounded by exp(epsilon).” Preserve the technical approximate-DP event bound and sufficient-tail lemma at L764–769. Reason: a correct lower technical paragraph does not repair an unconditional main/opening claim.
5. `courses/trustworthy-ai/lec02-privacy-dp-note.html`, S41/p41 L795. “up to the exp(epsilon) factor” → explicitly name the pure-DP case, or state the approximate event bound with additive delta. Reason: the repaired incremental-influence explanation should not silently drop approximate slack.
6. `courses/trustworthy-ai/lec03-mia.html`, S49/p49 L1086/L1089. Diagram “ratio≤exp(epsilon)” beside an approximate-DP heading and “every output ... nearly as likely” → label the diagram pure DP(delta=0), and scope the callout accordingly or use an event/attack-performance bound. The paired note already explains the diagram's pure-DP scope; make the main agree. Reason: essential qualifications cannot be hidden only in notes.
7. `courses/trustworthy-ai/lec04-memorization.html`, S53/p53 L995; paired `lec04-memorization-note.html`, S53 L1011/L1026. “probability ... at most a bounded factor” → bound the probability of an output event by exp(epsilon) times the neighbouring probability **plus delta**. Canary-null tail degrades “only ... exp(epsilon)” → add the delta term too. Keep L1014's correct qualification, the displayed definition and empirical zero-detected-extraction interpretation. Reason: DP-SGD/VaultGemma uses approximate DP; rare exact disclosures are not ruled out by a pointwise ratio.
F70.1 is the same guarantee-scope issue in the introductory technical preview; both locators need consistent scope. These findings do not authorize another implementation round.

### F74 — lec02 S57/p57, unconditional DP-SGD calibration is false
Type: fact. Blocking: yes. Path: `courses/trustworthy-ai/lec02-privacy-dp-note.html`, L1093 and L1099–1102. Evidence E104; E30 was a premise audit, not proof.
1. Current: the displayed sufficient noise bound and “ten times the data, one tenth the noise” are presented as a theorem for the stated one-record sampling setup at any fixed T. E104 supplies a one-step counterexample even when sigma exceeds the advertised threshold on both neighbours. Abadi's source theorem has additional regime/accounting assumptions and does not supply this exact unrestricted constant.
Fix [judgment]: remove the unconditional sufficient bound and exact tenfold guarantee from Reading/Technical depth. Either give a valid theorem with the matching sampling/adjacency/normalization and all regime conditions, or label the scaling explicitly as an accounting-regime heuristic and retain the already-qualified qualitative main/message. Do not edit the out-of-scope privacy-course dp5 source; flag that its copied theorem is not a justification. Reason: a teaching simplification cannot certify a mechanism that demonstrably fails the claimed privacy guarantee.

### F75 — lec04 S13/p13, canary guess probability is not a pairwise preference probability
Type: fact. Blocking: no (isolated retained phrasing; Message/Reading and query-budget conclusion are correct). Path: `courses/trustworthy-ai/lec04-memorization-note.html`, L274.
1. “chance of the model preferring the true r over any particular alternative ...1/|R| per guess” → “For a fixed guess independent of the uniformly sampled canary r, the chance of exactly guessing r is1/|R|; at mostq distinct guesses have success at mostq/|R|.” [judgment] Reason: exact-match probability and a pairwise ranking comparison are different events; preserve the existing specified-null/query-budget caveat (E108).

### F76 — lec02 S09/p9, comparison models are not all open
Type: fact. Blocking: no (local category label, not the plotted rates). Path: `courses/trustworthy-ai/lec02-privacy-dp-note.html`, L160.
1. “Open models sit below 1% (Pythia1.4B and6.9B, LLaMA-65B, InstructGPT)” → “The four comparison models before the ChatGPT bars sit below 1% (Pythia1.4B and6.9B, LLaMA-65B, InstructGPT).” [judgment] Reason: InstructGPT is not an open-weight model; avoid grouping unlike access models while retaining the actual figure reading (E108).

### F77 — lec02 S29/p29, inherited height-marker ordering
Type: fact. Blocking: no (inherited schematic detail; the chance-level teaching point and repaired note calculations remain valid). Path: `courses/trustworthy-ai/lec02-privacy-dp.html`, L614–616.
1. The 171cm dashed marker is drawn between the modes labeled168cm and170cm. Optional fix [judgment]: place the171cm marker to the right of the170cm mode, with its label legible and without reducing type; preserve the intended broad-overlap schematic. Reason: even a schematic should preserve the numerical ordering it labels (E107).


### F34 — residual finite-sample certainty claim, still blocking
Type: fact. Blocking: yes. Evidence E109/E91. `courses/trustworthy-ai/lec06-hallucination-note.html`, S57/p57 L866.
1. [judgment] “If all M samples land in one cluster, P(c|x)=1 ... the model is certain” → “If all M samples land in one cluster, its empirical cluster frequency is 1 and the plug-in entropy estimate is 0; this does not imply that the population puts all mass on that meaning.” Alternatively make the first premise explicitly population P(c|x)=1 rather than sample agreement. Keep the valid log K limiting case and distinguish empirical versus population probabilities consistently. Reason: E91's two-meaning random model can produce identical finite samples while remaining uncertain.
The main slides and S55/S57 Script fixes satisfy the previously named locators. Do not undo them; the retained definition must agree too. This is the same residual sample-certainty issue, not a new requirement to reject the sourced S56 estimator.

### F78 — lec06 S20/p20, the SimpleQA exhibit does not establish causation
Type: fact. Blocking: yes. Evidence E110. All changes [judgment].
1. `courses/trustworthy-ai/lec06-hallucination.html`, L334: “Rewarding ‘I don't know’ collapses the error rate.” → “More abstention, fewer errors at similar accuracy; different models, not a training ablation.” Reason: the plot compares two models rather than an isolated reward intervention.
2. `courses/trustworthy-ai/lec06-hallucination-note.html`, L313/L316/L318: keep the correct Message and arithmetic, replace the Script's causal sentence and “wrong answers turned into blanks / gain ... converting wrong guesses” with an aggregate comparison: “The lower error share accompanies a higher abstention share at similar accuracy; these totals do not identify which questions changed category or isolate the training cause.” Reason: a marginal table is not paired outcome tracking. Name **SimpleQA** throughout; PersonQA is S70 and its repaired explanation is not this finding.

### F79 — lec06 S08/p8, wrong source and unsupported medical-error chronology/mechanism
Type: fact. Blocking: yes. Evidence E111. All changes [judgment].
1. `courses/trustworthy-ai/lec06-hallucination-note.html`, L127: Saab et al., “Capabilities of Gemini Models in Medicine”,2404.18416 → Yang et al., “Advancing Multimodal Medical Capabilities of Gemini”,2024,2405.03162v1, Fig. 9 p28. Add the Google Research May15,2024 blog separately; update main citation in `courses/trustworthy-ai/lec06-hallucination.html` L147. Reason: the erroneous head-CT output is in the second paper, so “paper” itself is not wrong.
2. Main L141–142 and note L118/L122: remove “unnoticed for a year” and the claimed discovery delay; say “Flagged by neurologist Bryan Moore; the paper still carried the error when reported in August2025.” Avoid implying formal peer review from a preprint. Reason: publication-to-reporting time is not time-to-discovery; the report describes early flagging.
3. Main title L134, body L140, diagram L144; note L119/L122/L124: present an incorrect anatomical term rather than an established internal blend mechanism. Suggested title “A Fluent Medical Term Was Wrong”; contrast “basal ganglia” with the reported term, and label any two-term blend illustration hypothetical rather than causal. Attribute Google's learned-mis-transcription explanation to Google; do not present that explanation as proven either. Reason: incorrect output is observed; its internal cause is not identified by the cited example. Preserve the lesson that fluent medical text needs checking.

### F80 — lec05 retraining references and target taxonomy conflict across layers
Type: fact. Blocking: yes. Evidence E112. All changes [judgment].
1. `courses/trustworthy-ai/lec05-unlearning-note.html`, S63/p63 L1059: “the only suite here with a true retrained reference” → “a suite with a retain-only retrained reference; MUSE also supplies one”. Reason: the very MUSE figure being explained and §5.1 use retraining.
2. `courses/trustworthy-ai/lec05-unlearning-note.html`, S66/p66 L1112: “a document or a concept is knowledge suppression and has none” → “A specified training document can define data removal and a retrained reference; an abstract concept without an identified training subset is a suppression target.” Keep the stated setup distinction among the individual examples. Reason: a document is a collection of records, not automatically a concept with no deletion baseline.
3. `courses/trustworthy-ai/lec05-unlearning-note.html`, S61/p61 L1016–1022, especially “Each rung is strictly stronger than the last”; matching main `courses/trustworthy-ai/lec05-unlearning.html` S61 L1327–1339: do not teach refusal, raw concept suppression and dataset removal as an unconditional strict implication chain. Keep the three cards as distinct claims/evidence requirements. Explain that robustness over more adaptations strengthens a fixed behavioral target, whereas matching retraining can still allow facts supported by retained data. Reason: the note's own retained-duplicate-fact caveat is a counterexample to the asserted chain. No new taxonomy needed; reconcile this summary with S14 and S48.

### F81 — lec05 main audit shorthand omits the qualifiers already in the notes
Type: fact. Blocking: yes. Evidence E33/E112. All changes [judgment].
1. `courses/trustworthy-ai/lec05-unlearning.html`, S09/p9 L240: “Membership inference can confirm she was in” → “Membership inference can provide evidence she was in”. Reason: the illustrated test has false positives; the paired note correctly explains calibrated statistical evidence.
2. `courses/trustworthy-ai/lec05-unlearning.html`, S55/p55 L1231: “If it snaps back fast, it was never gone” → “Faster recovery than the same retrained control suggests a remaining trace.” Reason: new examples can teach even a never-exposed model; the already-correct Message/Script states the control and adaptation-budget qualification. Preserve the actual syntax-study result and do not call all recovery proof of failed dataset deletion.

### F82 — lec05 subsidiary logit-lens claim blurs successful and weak attacks
Type: fact. Blocking: no (secondary retained detail; main retain-set result is correct). Evidence E113.
1. `courses/trustworthy-ai/lec05-unlearning-note.html`, S46/p46 L759 and S62/p62 L1039: [judgment] qualify generic “decode correct answers from intermediate layers” with “Logit-lens probing was much weaker against RMU than fine-tuning or activation-direction removal; the paper reports near-chance residual-stream decoding after RMU.” Reason: the paper distinguishes these outcomes; correct answers on some trials are not comparable recovery of the suppressed capability. Do not alter61.6%/64.4% or the Wikitext exception.

### F83 — lec05 black-box proposition should distinguish laws from realized samples
Type: fact. Blocking: no (core non-identifiability idea is valid). Evidence: our probability check; E114 exact text.
1. `courses/trustworthy-ai/lec05-unlearning-note.html`, S50/p50 L823–825: [judgment] scope M=Psi(Gamma) to a population/expected metric, or say identical output laws induce identical distributions of sample-based test statistics, not equal realized benchmark numbers. Replace the final claim that empirical relearning/quantization results establish exact equality of output laws with “These studies show that the tested output metrics can miss residual capability; they do not establish equality for every prompt.” Reason: two independent samples from the same law need not give the same statistic, and finite empirical agreement is not full distribution equality.

### F84 — lec05 inherited diagram legibility
Type: design rule. Blocking: no (inherited geometry/type, not a newly introduced collision). Evidence E114. Path `courses/trustworthy-ai/lec05-unlearning.html`.
1. S03/p3 L96–138: optional [judgment] reflow the right-edge “unlearning · this lecture” sublabel so it is not clipped. Reason: the label should be readable; the main remediation box is already clear.
2. S52/p52 L1178–1197: optional [judgment] move the “members”/“non-members” labels away from the dashed marker/curves, keeping the bell ordering. Reason: labels should not be crossed out by the graphic they explain.
3. S43/p43 L995–1027: optional [judgment] enlarge/simplify the explanatory diagram so its revised labels are readable at presentation size, never shrink type. Reason: essential diagram text is inherited very small; the accompanying main bullets currently carry the corrected meaning.

### F85 — lec10 S25/p25, GCG was optimized against the augmented model
Type: fact. Blocking: yes. Evidence E118. Path: `courses/trustworthy-ai/lec10-jailbreak-note.html`, article L513.
1. L522 “an attack designed against the augmented model was not part of this table” and L528 “adaptive attacks against the augmented model were not the focus” → [judgment] “GCG was re-optimized against each evaluated model, including the augmented model; these tested attack families and budgets do not establish robustness to all adaptive attacks.” Use the model-specific protocol statement in Script and the remaining generalization limit in the limitations paragraph, without duplicating unnecessarily. Reason: Appendix A.4 explicitly describes victim-specific optimization for each model, not a suffix transferred only from the original model. Preserve the correct before/after rates, top 3 of 10 selection rule and absence of a formal guarantee.

### F86 — lec08 S35/p35, transferability section locator
Type: fact. Blocking: no (local citation locator; the repaired interpretation is correct). Evidence E116.
1. `courses/trustworthy-ai/lec08-adversarial.html` L447 and paired `courses/trustworthy-ai/lec08-adversarial-note.html` L600/L606: “§3.2 and §4 (transferability)” → [judgment] “§3.2 (relabelled-data experiment) and §3.3 (transferability)”; update the Reading sentence consistently. Reason: §4 is the theoretical framework, while the transfer experiment and hypothesis appear in §3.3. Keep the supported-explanation/not-sole-cause qualification.

### F87 — lec13 S05/p5, unsupported current-model comparison
Type: fact. Blocking: no (subsidiary limitation; schematic and2022 measurement are already distinguished). Evidence E121.
1. `courses/trustworthy-ai/lec13-prompt-injection-note.html`, L98: “current models resist this exact wording much better” → [judgment] “This schematic and the2022 measurements do not establish the success rate on current models.” Reason: the cited2022 result supplies no present comparative test. Preserve BANANA's schematic label, model/date and measured rates.

### F88 — lec13 S14/p14, InjecAgent denominator precision
Type: fact. Blocking: no (correct rates; small denominator difference does not change the core result). Evidence E122.
1. `courses/trustworthy-ai/lec13-prompt-injection-note.html`, L254/L264/L271: qualify 23.6%/47.0% as **ASR-valid, among valid model outputs**, not all 1054 cases. [judgment] In Message use “among valid outputs”; in setup/source name Table 3's ASR-valid and explain invalid/malformed/non-substantive outputs are excluded. Reason: Table 8's all-case rates are 23.3%/46.8%. Keep the reported Table 3 rates and fixed-attack/model/date caveats; no main-figure change needed.

### F89 — lec13 two small figure-reading mismatches
Type: fact. Blocking: no (local reading precision; central mechanisms remain correct). Evidence E124. Path: `courses/trustworthy-ai/lec13-prompt-injection-note.html`.
1. S09/p9 L178/L184: “four boxes” → [judgment] “three illustrated regions: white-on-white text; markup comments and attributes; faint text in an image.” Reason: comments/attributes share the middle illustrated region in the main SVG; there are not four separate boxes.
2. S13/p13 L238: remove “over a data channel” from the outgoing tool call; [judgment] instead say “The incoming red data-channel arrow carries the stranger's email into the agent; the right-hand red arrow is the resulting unauthorized tool call.” Reason: the label belongs to the input, not the outgoing action. No diagram redraw needed.


### F90 — lec13 CaMeL source-attribution precision
Type: fact. Blocking: no (numbers and conditional guarantee are supported). Evidence E126/E129. All changes [judgment].
1. `courses/trustworthy-ai/lec13-prompt-injection-note.html`, S45/p45 L891/L900; matching main `courses/trustworthy-ai/lec13-prompt-injection.html` L891: add AgentDojo v3 abstract/Introduction as the 97-user-task source alongside CaMeL Table 2. Reason: the CaMeL caption alone does not state97; do not change the supported denominator or 949 attacked cases.
2. `courses/trustworthy-ai/lec13-prompt-injection-note.html`, S46/p46 L909/L914: “paper's own section title” / “authors' own section title” → “opening answer in §9.3”. Alternatively quote the actual heading, “So, Are Prompt Injections Solved Now?”, followed by its answer. Reason: the existing quote is genuine but is the first sentence, not the heading. The main citation already attributes it to §9.3 and needs no change.

### F91 — lec13 subsidiary ProtectAI result uses a filtered attack denominator
Type: fact. Blocking: no (the five main-table configurations are unaffected). Evidence E128.
1. `courses/trustworthy-ai/lec13-prompt-injection-note.html`, S41/p41 L806: after “Protect AI 39/15/90”, add [judgment] “For Protect AI, Table 7 excludes cases whose required secret was redacted by the detector; its attack denominator is smaller than the 80-case subset.” Reason: the footnote applies to this additional row; retaining its rates without the exclusion overstates comparability. Keep the five displayed rows, utility denominators, 800-query limit and CaMeL exclusion unchanged.

### F92 — lec13 EchoLeak recap invents a prior evaluation history
Type: fact. Blocking: no (one subsidiary recap sentence; the incident and checklist remain supported). Evidence E123/E129.
1. `courses/trustworthy-ai/lec13-prompt-injection-note.html`, S50/p50 L977: “And the guards had been tested against known patterns.” → [judgment] “The report shows those guards were bypassed; it does not establish the scope of their prior adaptive testing.” Reason: the original report describes the classifier/redaction/CSP bypass, not Microsoft's pre-disclosure testing protocol. No main change needed.

### F93 — lec14 S19/p19, the denial summary is not oversight-only
Type: fact. Blocking: yes. Evidence E134. All changes [judgment].
1. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, L380/L381/L385/L390: replace “over 85% ... after doing so / After a model had disabled oversight ... over 85% of those follow-up questions” with “Across follow-up questioning after scheming actions in the oversight-subversion, self-exfiltration and goal-guarding evaluations, the paper reports o1 maintaining deception in over 85% of follow-ups.” Keep this separate from the displayed oversight-disabling table. Reason: Fig. 3's oversight-only bar is about80%; the abstract's broader summary cannot be assigned to that subset.
2. `courses/trustworthy-ai/lec14-agentic-threats.html`, L377: “Asked afterwards about its actions, o1 kept denying in over 85% of follow-ups” → “Across scheming follow-ups, o1 denied its actions over 85% of the time.” Add Fig. 3 to L381's source locator; use the note for the three named evaluations. Reason: make the changed population explicit on this oversight-titled slide. Preserve the 2% action rate, pre-release model, 300/100 discrepancy and capability-not-deployment qualification.

### F94 — lec14 source-version and locator precision
Type: fact. Blocking: no (the underlying substantive claims are supported). Evidence E131/E132/E135/E140/E144. All changes [judgment].
1. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S08/p8 L141, and paired main S08/p8 L187: Shevlane “Table 1 and §3” → “Table 1 and §4”. Reason: pre-release ARC evaluations are in §4, not §3.
2. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S09–S13/pp9–13 L174/L199/L224/L247/L267: identify the checked Kwa revision as v4 (July10,2026;2019–2025 model cohort), and “§7 limitations” → “§5–6 and App.B.2/E.3–E.4”. Main S10/p10 L235: “§4 (80% horizon)” → “§3.2.1 (80% horizon)”; main S12/p12 L262 and note S12 L242: replace “§4–§7” with “§3.2.1, §5–6 and App.E.3–E.4”; main S13/p13 L279: replace §7 with §5–6/App.B.2. Reason: the v4 revision supplying 207 days/o3 has no §7. Keep supported numbers and distinguish the paper's original 2025 release from the separate March2026 sensitivity note.
3. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S10/p10 L196: “Fig. 1's caption counts 169” → “Fig. 1's embedded subtitle and §2.2 count169”. Reason: the discrepancy is real, but the current caption locator is wrong. Do not harmonize169/170 silently.
4. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S21/p21 L443: “aim for a target accuracy, and one emulated a weaker model's profile (Fig. 7)” → “aim for a target accuracy (Fig. 7); weaker-model profile emulation is in Fig. 8/Table 2.” Reason: two experiments have different figure locators.

5. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S36–S42 and S45/pp36–42,45 L726/746/766/783/805/826/844/913: “limitations §6” → “limitations §5.1”; S45 L908 and paired main S45 L802 use §5.1 as well. S41 L823 and paired main S41 L745: “no train/validation split … (§6)” → “no train/validation split … (§2.4)”; main L745's “Table 2” → “Table 7” for all five displayed thresholds. Reason: §6 is the conclusion, while Table 2 omits some displayed threshold rows; checked v5 contains the precise statements elsewhere. Evidence E140.

6. `courses/trustworthy-ai/OUTLINE.md`, lec14 source summary L695/L699 (S09–S13/pp9–13 and S36–S45/pp36–45): replace Kwa's inherited `§7` pointer with the v4 sections in item 2; identify v4 and preserve the 207-day/o3 result. For Greenblatt add Table 7 for the full threshold comparison, use §5.1 for limitations and §2.4 for the no-split caveat. Reason: the shared source map must not reintroduce the wrong locators after the notes are corrected. Keep source-version/count discrepancies, not a silent harmonization.

### F95 — lec14 S21/p21, name the subject-matched control
Type: fact. Blocking: no (displayed rates and selective-underperformance conclusion are correct). Evidence E135. All changes [judgment].
1. `courses/trustworthy-ai/lec14-agentic-threats.html`, L411/L413: “MMLU: general control / MMLU (control)” → “MMLU biology control / MMLU bio (control)”. In paired note `courses/trustworthy-ai/lec14-agentic-threats-note.html`, L427/L428/L431/L435, specify the biology-subject MMLU subset for these two drops. Reason: Table 1 compares matched subject groups, not all MMLU questions; preserve 39.8/9.7 and32.1/14.0.
2. `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S21/p21 L428/L437: qualify “up to 46%” as “up to 46% on WMDP-Cyber in the broader study, not on this biology comparison”. Reason: Table 8's largest refusal rate belongs to another subject. Keep the general refusal-exclusion warning; no need to add another numerical table.

### F96 — lec14 S11/p11, make the plotted task-set scope visible
Type: preference (factual scope is already clear in S09/S13 and the note). Blocking: no. Evidence E132; workissue6.
1. `courses/trustworthy-ai/lec14-agentic-threats.html`, L245: “Doubling:207 days.” → [judgment] “Doubling on this task suite:207 days.” Preserve the model-cohort dates, log-axis key and type size. Reason: the chart's cropped subtitle no longer names the tested tasks; the added qualifier makes the otherwise supported trend harder to over-read as all work or a forecast.

### F97 — lec14 S31/p31, Prompt Infection's breakdown is not an all-attempt resistance rate
Type: fact. Blocking: yes. Evidence E138. All changes [judgment].
1. `courses/trustworthy-ai/lec14-agentic-threats.html` L576–577 and paired `courses/trustworthy-ai/lec14-agentic-threats-note.html` L631/L634/L637: label 66%/9% as Fig. 5's **failure-reason breakdown**, not the fraction of all attacks ignored. Remove the cross-model resistance ranking from these percentages. In the note, flag that the source prose loosely says “attacks” while the figure and high Fig. 4 success rates do not support that unconditional denominator. Attribute the execution-reliability explanation to the authors, not to an independently identified conditional rate; move that explanation to the note if needed. At main L584 and note L637 add Figs. 4–5 for the app experiment, keeping Fig. 6 for the separate society experiment. Reason: a reported failure breakdown cannot establish unconditional resistance; the prose/figure ambiguity must be disclosed, not replaced with an invented total-attempt denominator.
2. Main L575 and note L630/L634: “self-replicating … beat non-replicating … when all agents shared messages” → “Self-replication helped most global-message scenarios; data theft was an exception.” Explain in the note that non-replicating attacks outperform in some larger-agent data-theft settings (§5.1/Fig. 4). Reason: the paper explicitly limits the generalization. Preserve simulated-app status, the separate society experiment and its extra memory-manipulation condition.

### F98 — lec14 S32/p32, handcrafted does not mean non-adaptive
Type: fact. Blocking: no (the result is already limited to the tested attacks, not a robustness guarantee). Evidence E138. All changes [judgment].
1. `courses/trustworthy-ai/lec14-agentic-threats-note.html` L652/L657 and paired `courses/trustworthy-ai/lec14-agentic-threats.html` L601: replace “no adaptive attacker was tested” / “known attacks … not tested adaptively” with “Handcrafted-attack success does not establish robustness to new adaptive attacks.” Keep the reported manual counterattack on marking. Reason: manually designing an attack against a known defence is already adaptation; the source's actual limitation is handcrafted coverage, not a categorical absence of adaptation.

### F99 — lec14 S27/p27, retained top-mode list misses the second-largest category
Type: fact. Blocking: no (subsidiary detail; main category shares are correct). Evidence E137.
1. `courses/trustworthy-ai/lec14-agentic-threats-note.html` L551: [judgment] “The biggest single modes are step repetition, unawareness of when to stop, and disobeying the task specification” → “The largest individual modes are step repetition (15.7%), reasoning-action mismatch (13.2%) and unawareness of termination conditions (12.4%).” Reason: disobeying task specification is 11.8%, below the omitted 13.2%. Do not change the source's category totals to force agreement with rounded component sums.

### F100 — lec14 S43/p43, explicitly name decisive attempted attacks
Type: fact. Blocking: no (the displayed caught/(caught+uncaught-successful) formula is already correct). Evidence E141. All changes [judgment].
1. `courses/trustworthy-ai/lec14-agentic-threats-note.html` L853/L857/L863 and paired `courses/trustworthy-ai/lec14-agentic-threats.html` L774: “over attempted attacks only” → “among decisive attempted attacks”; explain in the note that uncaught failures and aborts are excluded. Reason: “all attempts” is the ASR denominator, not this safety estimator's denominator. Preserve every plotted rate, n, CI, scorer and deployment caveat.

### F101 — lec01 S23/p23 and shared outline still put the whole campaign inside HF
Type: fact. Blocking: yes. Evidence E50/E115/E145/E146. All changes [judgment]. This inherited repetition was missed in earlier review/planning; the final shared-document check exposed it.
1. `courses/trustworthy-ai/lec01-introduction.html`, S23/p23 L508/L512: “9–13 July … inside Hugging Face” / “4.5 days … forensic window inside another company's systems” → label July 9–13 and 4.5 days as the reconstructed campaign, including external staging; state roughly 2.5 days inside HF. Reason: campaign duration and time inside HF are different quantities.
2. `courses/trustworthy-ai/lec01-introduction-note.html`, S23/p23 L570/L571/L574/L579/L581: carry that distinction through Message, Reading, Script, event chronology and evidence paragraph. Keep 17,600 as reconstructed actions across the campaign; do not justify the incorrect internal-duration label by saying the slide chooses the longer window. Reason: a later 2.5-day parenthesis does not repair the contradictory opening.
3. `courses/trustworthy-ai/OUTLINE.md`, lec01 incident summary L188, referring to S23–S24/pp23–24: replace “4.5-day forensic window inside HF” with “4.5-day reconstructed campaign, including external staging; roughly 2.5 days inside HF.” Preserve the already-correct lec07 S08/p8 and the dated reconstruction/intent caveats. Reason: the shared map must agree with the primary timeline and repaired lecture.

## Previous residuals
| Finding | Final status | Basis |
|---|---|---|
| F19 | Closed | lec04 S50: 10× unprompted versus 5× prompted now agrees across layers (E105). |
| F34 | **Partial; blocking** | Main and named Script fixes accepted; retained S57 definition still makes the finite-sample inference above (E109/E91). |
| F56 | Closed | lec12 S39a/p52, S39b/p53, S44b/p64: source labels match the transformed-test-data explanation. §10/Appendix B support it; the historical Fig. 4 generator remains **unrecovered** (E120). |
| F66 | Closed | Correct audit attribution, lower-versus-upper interpretation and Nasr two-run setup (E105). |
| F67 | Closed | Named narrow formula overflows repaired, default type preserved; visual/source/DOM coverage limited as stated above (E107/E109). |
| F68 | Closed | Finite KS p-value and checkpoint-aggregation claims qualified (E109). |

## Preserve these source distinctions
- RepliBench pass@10 already means at least one success. Keep 15/20 components, the one hard-scaffold success and no end-to-end evaluation distinct; preserve the source's 9/20 versus 10/20 discrepancy.
- Kwa v4 supports 207 days/o3. Keep embedded-subtitle/§2.2 169 versus 170 tasks, and discussion mid-2028–mid-2030 versus introductory mid-2031, explicitly distinguished rather than silently harmonized.
- Meinke: preserve constructed-incentive/intent-attribution limits, Table 2 caption 300 versus text 100 and 400 unnudged; Fig. 3's oversight bar is about 80% of 320 responses, not the >85% broader summary.
- CaMeL: preserve conditional guarantees, STRICT branch, non-injection exceptions, 163 versus 300 source discrepancy, AgentDojo's 97 tasks and CaMeL's 949 attacked cases. Nasr's 80 attack cases / 97 utility tasks / 800 queries explicitly exclude CaMeL, ToolFilter and IPIGuard; F91 is only the extra ProtectAI row's redacted-secret filter.
- Control: preserve free first-ten audits, the 5,000-problem scenario upsampled from 1,500 generated problem responses, and separate honest-model usefulness / attack-policy safety experiments. Ge-Wang n=15/18/2/23, sole Linux stop-policy CI excluding zero, offline scorer, cross-validation, shrinking denominator and benchmark-inventory versus sampled-trajectory distinctions stay.
- Preserve top 3 of 10 GCG selection (F85), SimpleQA rather than PersonQA (F78), and finite-agreement versus population uncertainty (F34). Read-only lec14tech p6's independent-all-steps-right calculation is valid for its stated event; no tech mismatch/edit is requested.

## Work-r3 plan issues and plan corrections (all seven adjudicated)
- Issue7, lec01 course count: resolved. Leaf/root course structure confirms14 taught lectures excluding backups;13 after today's introduction is correct. No new change.
- Issue3, lec02 DP: S27/S39 need the explicit pure/small-epsilon scope recorded in F73. S28 is acceptable as the original release's incremental guarantee against side information at unchanged unit/adjacency; it does not certify total secrecy or free additional raw-data releases. Optional [judgment] clarification at main S28/p28 L588–597 and note S28/p28 L556/L559: “The original release's guarantee remains, at the same protected unit/adjacency; extra releases need their own privacy accounting.” Not an independent blocker. S47's coin-flip deniability is supported by the displayed randomized-response mechanism; it is not a zero-information claim, so no change required.
- Issue1, lec06S20: confirmed causal overclaim; F78 supplies the correction. It is a SimpleQA cross-model comparison, not PersonQA. This is an authorized factual consistency repair, not a reason to keep the unsupported causal argument. S70 PersonQA repairs are accepted againstE38.
- Issue2, lec06S08: the paper/blog mismatch suspicion is resolved by locating the actual Fig9 in Yang et al.2405.03162v1. “Paper” can stay, but F79 corrects its citation and the unsupported chronology/mechanism. Do not replace the paper claim with “blog only”.
- Issue5, lec13: OWASP official2026 resource verifies August3 publication and retainedLLM01; no date blocker. S07 “today's main case” is expressly lecture scope, not prevalence. S05's unsupported current-model resistance comparison is optional F87. Preserve the schematic/measured-result distinction.
- Issue4, lec13S45: adjudicated against E126/E129.97 is supported by AgentDojo and consistent with CaMeL Table2 fractions;949 is explicitly CaMeL's attacked-case count. Add local attribution optionally (F90.1), not a numerical correction. Preserve the conditional guarantee and explicit Nasr non-evaluation.
- Issue6: adjudicated against E131/E132/E135. S11 is a supported dated task-suite trend; optional F96 puts the existing scope onto its key. S26 explicitly means the studies used in this lecture, so no present-field claim or change required. Read-only tech p6 states P(all steps right)=p^n under independent fixed-rate steps and separately warns about recovery/correlation; no conflicting eventual-success assertion found. No tech edit requested or authorized.
- New S08 label-collision concern was disproved by the individual native screenshot; no finding or change requested.


No new plan or work order is issued. M11's missing pure-DP qualification was a planner omission; F73 corrects the claim rather than demanding compliance with it. The baseline-derived lec14 handcrafted/non-adaptive wording and inherited source locators likewise yield to F98/F94. F101 identifies an earlier missed lec01 repetition of the already-settled HF timing distinction. Frozen plan-v3 and review-r2 remain unchanged. If Albert authorizes further work, write a new incremental plan; do not treat this verdict as an automatic r4.

## Disposition
Final review is complete and frozen on announcement. **Revise / escalated**, not approved. Send one concise escalation to Albert in `claw-slides-review`; no automatic fourth round, work pointer, PR, merge or PDF. The same branch and single eventual PR remain required. Any next correction pass needs Albert's decision and a new incremental plan; do not reopen the completed broad review. No actual provider-capacity hold exists.
