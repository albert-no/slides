# work-r2 — 2026-11-15-lec01-lec12-notes

## Branch and commits

- Branch: `2026-11-15-lec01-lec12-notes`. Reviewed in round 1: `3150ed4`. Head: the commit named in the pointer that delivers this file.
- Log copy (review-r1, plan-v2, living files): `15561e9`. Content diff for review: `git diff 15561e9 <head> -- courses/`. It touches only the 12 notes (+382/−362). No deck, tech supplement, OUTLINE, `reference/` or script file changed.
- Per-package content commits:

| Pkg | Note | Commit | Findings |
|---|---|---|---|
| P1 | lec01 | b156e38 | F01 F02 F10 F11 F58 |
| P2 | lec02 | 7677678 | F03–F10 F12 F59 F60 |
| P3 | lec03 | 37a4ac7 | F12–F16 F25 |
| P4 | lec04 | 46a44cc | F10 F17–F24, plan decision 5 (S42) |
| P5 | lec05 | 0f9acf4, 5496d17 | F26–F31 F61 F63 F65.1; S41 aligned with F26 |
| P6 | lec06 | 009850c | F32–F37 F62 F63 F65.2 |
| P7 | lec07 | 6c2f0fa | F38 F39 F42 F43 |
| P8 | lec08 | 31f77ec | F40 F41 F65.5 |
| P9 | lec09 | e6c2f5e | F44 |
| P10 | lec10 | f5fbcb4 | F45–F51 F65.6 |
| P11 | lec11 | f43a9c9 | F52 F53 F57 |
| P12 | lec12 | 66ed586 | F54 F55 F56 F65.3 (F65.4: no change) |

## Dispositions F01–F65

All 61 blockers are fixed; none is disputed. Each correction is applied throughout the article (Message, Reading, Script and any repeated technical or case text), not only in the short layer.

| F | IDs | Disposition | What changed |
|---|---|---|---|
| F01 | lec01 S19, S40, S44 | fixed | The stickers were optimized white-box (architecture and weights, §5) and then printed; "printer, not weights" is described as the point of action only. Figure 1 is described as its two photos. 84.8% drive-by is in Table 3; the lab tests are in Table 2. |
| F02 | lec01 S31 | fixed | Art. 35(1) impact assessment is an endeavour duty ("노력하여야 한다"), separate from the Art. 34(1) measures, which include human oversight. Named overseer via Decree Art. 27(1)(4). Scope: high-impact only. Direct Art. 34, Art. 35 and Decree links added. |
| F03 | lec02 S03 | fixed | False converse removed. Protection must come before release, since later work cannot retract a disclosure; a newly released filtered artifact needs its own guarantee. Constant-output counterexample added. |
| F04 | lec02 S29 | fixed | Posterior ≈51% at 171 cm vs ≈54% average Bayes accuracy; distributions labelled illustrative; LR $e^{0.04}$ derivation added. |
| F05 | lec02 S41 | fixed | DP bounds the incremental evidence from Alice's record, not inference from correlations. |
| F06 | lec02 S32, S39 | fixed | Additive event inequality replaces "with prob. 1−δ behaves as pure DP"; the tail lemma is labelled sufficient, not equivalent. |
| F07 | lec02 S46 | fixed | 90% is a debiased estimate, up to sampling error. |
| F08 | lec02 S57 | fixed | The Message gives the qualitative signal-to-noise lesson and its setup dependence. The derivation is scoped to one uniform sample per step, fixed T/G/normalization and a simplified constant, not a general accountant. |
| F09 | lec02 S30, S33, S36, S38, S40, S56, S68 | fixed | Categorical "not private / cannot tell" replaced by weak-worst-case-bound wording, which proves no leak. S30: non-constant. S56: a historical 2021–22 comparison. S68: scoped advantage bound. |
| F10 | lec01 S12, S34; lec02 S09, S20; lec04 S23, S26 | fixed | Same wording across all three packages: the block changed deployed outputs and does not establish erasure; post-patch persistence was not measured; alignment fine-tuning does change parameters. |
| F11 | lec01 S08 | fixed | Recorded two-year rearrest, not reoffending. Northpointe's defence is predictive parity at a cutoff, distinct from score-wise calibration. The impossibility uses equal PPV (0<PPV<1) vs equal FPR and FNR (FNR<1) under unequal base rates; calibration is not its premise. |
| F12 | lec02 S62; lec03 S51 | fixed | Same wording in both notes: a statistical lower bound with simultaneous confidence, fixed δ and valid denominators, $\varepsilon_{LB}=\max(0,\ln((\mathrm{TPR}_{lower}-\delta)/\mathrm{FPR}_{upper}))$. A result above the claim is a signal to investigate (implementation, accounting or assumptions); one below it is inconclusive. |
| F13 | lec03 S08 | fixed | Membership reveals a diagnosis only for a patients-only cohort. |
| F14 | lec03 S28 | fixed | The identity holds for Adversary 1 (randomized, bounded loss); Fig. 2 threshold attacks are an empirical companion. Proof kept. |
| F15 | lec03 S39, S43 | fixed | 5.9 is a density ratio; posterior odds = prior odds × Λ (≈85% at equal priors, ≈5.6% at a 1% prior). Low FPR is necessary, not sufficient, for a credible accusation (pointer to S46). |
| F16 | lec03 S47, S59 | fixed | Main setup is C4 subsets; Appendix D / Fig. 16 is a separate C4 vs deduplicated-C4 experiment. The instability is an observed LiRA result, not an impossibility. |
| F17 | lec04 S13 | fixed | A random canary makes accidental matches unlikely under a null (≈1/\|R\| per guess, ≤ q/\|R\| for q guesses), not impossible. |
| F18 | lec04 S36 | fixed | Repeated exposure is separated from more unique data. |
| F19 | lec04 S50 | fixed | The C4 Duplicates row worsens (≈2.5 → ≈5.5–6, read from the figure) because train/val overlap is removed. The 10× unprompted headline is kept apart from the ≈5× bar drop; "no cost" is scoped to clean rows. |
| F20 | lec04 S53 | fixed | The bound is on incremental probability under ε, δ and adjacency. Zero detections is an empirical outcome. Rates are given per bar and type. |
| F21 | lec04 S59 | fixed | Marginal P(flag \| fresh matched non-member) ≤ α with the ⌈(n+1)(1−α)⌉ rank cutoff; not posterior error, FWER or FDR. Observed 1.82%/0.02% is distinguished from certified 1.84%/0.04%. |
| F22 | lec04 S58 | fixed | About 1,030 token evaluations ≈ 20 MC samples ≈ 10× greedy, not 20×. Token count kept separate from wall-clock. |
| F23 | lec04 S31, S56, S58 | fixed | S31: Fig. 1 is a length- and duplication-normalized sample; uniform-sample rates (Fig. 2) are much lower with the same trend. S56: per-window known-prefix audit with the $p_z \ge 0.1\%$ threshold, not blind retrieval. S58: fixed 0.001 k-CBS threshold. |
| F24 | lec04 S60 | fixed | The random-data plateau is separated from the natural-text generalization experiments. 3.6 bits/param is a model- and protocol-specific estimate. |
| F25 | lec03 S49, S50 | fixed | The ratio picture is pure-DP intuition; approximate DP is stated with event probabilities plus additive δ. S50: the region is an outer bound from one inequality; the complementary bound TPR ≤ 1 − e^{−ε}(1−δ−FPR) added; "guarantee dies" → "this bound becomes vacuous". |
| F26 | lec05 S09, S39, S41, S43, S51, S52, S55, S61 | fixed | Statistical evidence against a retrained reference, not "confirm". One flag can be a false positive and no detection is not proof. TOFU is a controlled design compared with a retain-only model by a KS test. S41 (not in the plan map) carried the same "nothing leaks in from the web" claim; aligned in 5496d17. |
| F27 | lec05 S18, S50 | fixed | The approximate target is separated from a proved bound. Heuristic LLM methods generally lack a retrain-indistinguishability certificate. |
| F28 | lec05 S31 | fixed | Only the dense Hessian is ruled out; implicit HVPs avoid storing it. The real limits are solve cost and non-convex validity. |
| F29 | lec05 S48, S61 | fixed | Three terms: filter (external, access-model dependent), learned refusal (in weights) and unlearning (judged against retraining). "Certificate proves, audits support or refute." |
| F30 | lec05 S56 | fixed | 21%/83% are averages over the tested utility-constrained methods; rounding is the authors' explanation, not an identity. |
| F31 | lec05 S62 | fixed | 10 retain-set examples: RMU 61.6% vs 64.4% unprotected. Key: colour = method, shade = dataset, dotted 64.4%, chance ≈25%. Names the RMU–Wikitext near-chance exception. DPO is the safety-training baseline. |
| F32 | lec06 S28 | fixed | Zero means no observed average gap in these bins; it does not certify population calibration. |
| F33 | lec06 S45 | fixed | The upper bound concerns coverage near nominal and gives no bound on set size. |
| F34 | lec06 S55, S56, S57 | fixed | Consistency and semantic entropy are confabulation cues, not truth tests; a repeated misconception has low entropy. Table 1 is marked illustrative. |
| F35 | lec06 S22 | fixed | Knowledge is fixed in parameters with no automatic freshness detector. Disclosure is possible if prompted or trained, and supplied context helps. |
| F36 | lec06 S70 | fixed | More-claims explanation for o3, smaller-model explanation for o4-mini; the card says the cause needs more research. |
| F37 | lec06 S67 | fixed | The trend is generally negative and GPT-3 is the clear case; UnifiedQA 2.8B exceeds 770M. Historical results. |
| F38 | lec07 S67, S68 | fixed | The S67 monitor read reasoning only. Total cheating fell below baseline, but what remained was hidden. S68: "cannot guarantee reliability when directly optimized against". |
| F39 | lec07 S47 | fixed | AlwaysEqual is one of three available shortcuts; the ≈100% curve counts all studied hacks. |
| F40 | lec08 S64 | fixed | Exact min–max is the objective; PGD approximately solves the inner max. Empirical, not certified. |
| F41 | lec08 S54, S71 | fixed | Counting needs the whole ball, centre included, with the true label. "Surviving AutoAttack" is an upper-bound estimate. |
| F42 | lec07 S08 | fixed | 9–13 Jul is the reconstructed campaign window, including external staging; the intrusion inside HF ran from 11 Jul (≈2.5 days). |
| F43 | lec07 S65 | fixed | Chance-corrected disclosure score on inferred hint-use cases, clipped at 1; counts acknowledgment of causal use. 25%/39% kept. |
| F44 | lec09 S50 | fixed | The common 0.01%→0.1% range is replaced by the finding's sentence; the $60/year headline is kept. |
| F45 | lec10 S36 | fixed | Targets were proprietary chatbots and open-weight Llama-2. Transfer means no target gradients. |
| F46 | lec10 S22 | fixed | Same harmful prefixes per pair over Harmful HEx-PHI; KL = 0 means equal conditionals; later KL is smaller but nonzero. |
| F47 | lec10 S49, S52 | fixed | NLL falls approximately as a power law; the right panel is a separate psychopathy evaluation; exp(−aN^−b) is not a power law. S52: the fit is to −log(ASR). |
| F48 | lec10 S74 | fixed | Authors' tested attacks and settings, not a guarantee against stronger attacks. |
| F49 | lec10 S05, S06 | fixed | Some tested prompts remained effective on dated model versions; 240+ days is time online. |
| F50 | lec10 S64 | fixed | Required sentence used; rule fixed, length and score varied, constant harm not measured. |
| F51 | lec10 S25 | fixed | The GCG row is the mean of the 3 highest-ASR runs of 10 (App. A.4). |
| F52 | lec11 S34 | fixed | Conditional on paraphrasing making full-text TV small; the curve is an AUROC upper bound, not measured. |
| F53 | lec11 S67 | fixed | Systems placed on the market before 2 Aug 2026 must meet Art. 50(2) by 2 Dec 2026. |
| F54 | lec12 S10 | fixed | Auditing needs group labels in the audit data; dropping them from model inputs does not prevent separate retention. |
| F55 | lec12 S19b | taken (nonblocking) | One-way implication: calibration ⇒ equal PPV in the two-value top-bucket case; the converse need not hold. |
| F56 | lec12 S39a, S39b | fixed | Transformed evaluation data, not predictions; §10 test-partition protocol (25 random 50/20/30 splits) and App. B.4–5; fitted training-cell weights, held-out residuals. The unrecovered Fig. 4 generator is stated. |
| F57 | lec11 S73 | taken (nonblocking) | "At fixed true- and false-positive rates, rarer AI content means a larger fraction of flags are false." |
| F58 | lec01 S13 | fixed | Dec 2024 €15M fine kept; Tribunale di Roma judgment 4153/2026 (published 18 Mar 2026) first-instance annulment added; further appeal unverified. Garante notice link added. lec02 S20 already matched; no change for F58 there. |
| F59 | lec02 S43 | fixed | The recipe is scoped to additive-noise mechanisms; exponential mechanism cited as a counterexample. |
| F60 | lec02 S17 | fixed | A statistically supported advantage is evidence in the tested setup. A single flag can be a false positive, and no detection is not a certificate. |
| F61 | lec05 S29, S30, S64 | fixed | A3 applies to the retained objective; A1 domain caveat; ridge only on a bounded domain. Retraining convention (original n, fixed λ) made explicit with λ′ = nλ/(n−1), labelled as our own algebra. S64: matching Gaussian on both θ_u and θ_{−z}; the classical formula requires 0<ε<1. |
| F62 | lec06 S14, S17, S21 | fixed | Mis_b is TV distance to p coarsened on the adaptive partition V_b(g) (KV §3.2 Def. 2). The reading keeps all correction terms and is conditional, not an empirical floor. S17: explicit hypothetical. S21: the Arbitrary Facts model, scoped as conditional, separated from the FActScore observation. |
| F63 | lec05 S55; lec06 S71 | fixed | lec05: bars read per relearning set against the 1.00 target; syntactic ≥ topical in all nine comparisons, but not near the target everywhere (NPO gradient 0.39). lec06: axis P(preferred \| present vs absent), 50% neutral, dots posterior medians, lines 50%/95% CIs; strongest association in this fit, not a causal rank. |
| F64 | record only | corrected here | See "Correction to work-r1" below. |
| F65.1 | lec05 S33 | taken | Kurmanji et al. NeurIPS 2023 proceedings URL added (E42). |
| F65.2 | lec06 S69 | taken | Pinned README (commit e435b6b, 22 Sep 2026, E84) added; live leaderboard link kept. |
| F65.3 | lec12 S19b, S20b, S23a, S25, S26a, S26b, S30 | taken | "Definition 2.2" → "Definition 2 (predictive parity, Eq. 2.2)" at all seven. |
| F65.4 | lec12 S17a, S17b | no change needed | The notes already say "panel title kept"; no removal claim remains. |
| F65.5 | lec08 S66 | taken | Duplicate eight-times-compute Assumptions removed from S66; S67 keeps the calculation. |
| F65.6 | lec10 S60 | taken | "Twenty minutes" → "This section". Pacing unchanged. |

Plan decision 5 (lec04 S42): taken. 1.88% is a similarity > 0.5 copy-detection proxy, not verified duplicates.

## Correction to work-r1 (F64)

work-r1 Deviations said the lec03 repair `15057f6` was at S49 and restored the sentence "verbatim from `9a772bd`". Both are wrong:
- The repaired sentence is in lec03 **S66**.
- `9a772bd` introduced the truncation. It replaced the old pointer "(Verified against `mia4-modern.html`, Proposition 5; the same preimage argument shows the $(\varepsilon,\delta)$ guarantee itself survives post-processing.)" with "(Derivation in `lec03tech.html`; see the slide index there.)$ guarantee itself survives post-processing.)", leaving a broken tail.
- The restored clause comes from `ddf4915` (= `9a772bd^`), line 909. It is joined to 9a772bd's new derivation pointer as its own sentence, with "the" capitalized. The repair is therefore not verbatim; the wording of both parts comes from git history.

## Changed IDs and pages

112 articles; page = article position in the note.

- lec01 (8): S08/p8, S12/p12, S13/p13, S19/p19, S31/p31, S34/p34, S40/p40, S44/p44
- lec02 (19): S03/p3, S09/p9, S17/p17, S20/p20, S29/p29, S30/p30, S32/p32, S33/p33, S36/p36, S38/p38, S39/p39, S40/p40, S41/p41, S43/p43, S46/p46, S56/p56, S57/p57, S62/p62, S68/p68
- lec03 (9): S08/p8, S28/p28, S39/p39, S43/p43, S47/p47, S49/p49, S50/p50, S51/p51, S59/p59
- lec04 (12): S13/p13, S23/p23, S26/p26, S31/p31, S36/p36, S42/p42, S50/p50, S53/p53, S56/p56, S58/p58, S59/p59, S60/p60
- lec05 (18): S09/p9, S18/p18, S29/p29, S30/p30, S31/p31, S33/p33, S39/p39, S41/p41, S43/p43, S48/p48, S50/p50, S51/p51, S52/p52, S55/p55, S56/p56, S61/p61, S62/p62, S64/p64
- lec06 (13): S14/p14, S17/p17, S21/p21, S22/p22, S28/p28, S45/p45, S55/p55, S56/p56, S57/p57, S67/p67, S69/p69, S70/p70, S71/p71
- lec07 (5): S08/p8, S47/p47, S65/p65, S67/p67, S68/p68
- lec08 (4): S54/p54, S64/p64, S66/p66, S71/p71
- lec09 (1): S50/p50
- lec10 (10): S05/p5, S06/p6, S22/p22, S25/p25, S36/p36, S49/p49, S52/p52, S60/p60, S64/p64, S74/p74
- lec11 (3): S34/p34, S67/p67, S73/p73
- lec12 (10): S10/p13, S19b/p27, S20b/p29, S23a/p33, S25/p36, S26a/p37, S26b/p38, S30/p42, S39a/p52, S39b/p53

Against the plan-v2 map: two planned entries are unchanged (lec12 S17a, S17b; F65.4 needed no change). Two changed entries are outside the map: lec04 S42 (plan decision 5) and lec05 S41 (the F26 repetition). Titles, IDs, order and pacing lines are unchanged.

## Main-slide discrepancies explained in the notes (decks not edited)

Each note now explains the slide's shorthand and gives the precise statement. Suggested deck fixes are for a later job.

- **lec01**
  - S08: bars say "re-offend"; the outcome is recorded rearrest.
  - S12: "blocked the prompt, not the memorization" asserts persistence that was not measured.
  - S13: stops at the Dec 2024 fine; the Mar 2026 annulment is missing.
  - S19: "Attacker needs a printer, not weights"; the cite line gives Table 2 only (84.8% is in Table 3).
  - S31: "impact assessment" stated as a duty.
  - S40, S44: "printer / parking lot / road access" framing.
- **lec02**
  - S03: "Nothing after it can add privacy back."
  - S09: "the data stays inside."
  - S33, S36, S40: large ε "not private / not a guarantee."
  - S38: "you cannot tell which bell."
  - S41: "'Alice smokes' is not."
  - S43: "Every DP mechanism follows one shape."
  - S46: "the true rate p is 90%."
  - S57: "washes out."
  - S62: "A gap means a bug."
- **lec03**
  - S08: patient-only cohorts assumed.
  - S28: "loss-threshold advantage."
  - S50: "attainable" means not excluded by this line.
  - S51: bug-catch and looseness cards.
  - S59: "confirms the wall."
- **lec04**
  - S13: "must be memorization, not chance."
  - S23: "the weights unchanged."
  - S26: "Still in the weights."
  - S36: "both push the wrong way."
  - S50: "perplexity no worse" (fails on the C4 Duplicates row); ~10× vs the ≈5× bar drop.
  - S53: "no single record can be memorized."
  - S58: "~20× greedy cost" (≈10×); "1.4% verbatim" is the k-CBS curve, greedy ≈0.6%.
  - S59: "a quarter of the hits are noise."
  - S60: "then start generalizing."
- **lec05**
  - S18: "small, bounded difference."
  - S31: "Only rough approximations are feasible."
  - S43: "the only source."
  - S48: "nothing left to leak."
  - S50: "Approximate methods give no certificate."
  - S51: flagged/indistinguishable cards.
  - S56: 21%/83% shown without "average."
  - S61: "Refuses = output filtering."
  - S62: "10 unrelated examples." **The deck alt text on S62 (`figs/lucki-finetune.png`) says every curve climbs back, but the RMU–Wikitext curve stays near chance.**
- **lec06**
  - S22: "facts freeze / No internal flag."
  - S55: "samples agree ⇒ likely solid."
  - S56: "flags hallucination."
  - S57: "Scattered meanings signal an unreliable answer."
  - S67: "biggest model scores lowest" (UnifiedQA exception).
  - S70: "More claims per answer" applies to o3 only.
- **lec07**
  - S08: "Intrusion 9–13 Jul" is the campaign window.
  - S65: the axis label "mentions the hint."
- **lec08**
  - S64: caption "Inner max: PGD."
  - S71: "robust only if all four fail."
- **lec09**
  - S50: the figure alt text repeats the false common 0.01%→0.1% range. Alt text is not shown in the note, so this needs a deck fix.
- **lec10**
  - S05: "works for every user … for months."
  - S06: "works for anyone who copies it."
  - S22: "one harmful reply"; "KL near 0: unchanged."
  - S36: "closed chatbots" (Llama-2 is open-weight).
- **lec11**
  - S34: the title states the conditional claim unconditionally.
- **lec12**
  - S39a, S39b: label "Training data, not a trained model." and the alt text.

## Sources fetched this round

- arXiv 1707.08945v5 (Eykholt et al.): Fig. 1 caption, §2, §5, Tables 2–3.
- law.go.kr: AI Basic Act Art. 34 and Art. 35, Enforcement Decree Art. 27.
- arXiv 2202.07646v3 (Carlini et al.): Fig. 1 vs Fig. 2 sampling.
- arXiv abs/2006.07709 (Jagielski et al. 2020): title.
- NeurIPS 2023 proceedings, Kurmanji et al.: the URL resolves, title and authors match.
- arXiv 2409.18025 (Łucki et al.): §3.2, §5 and Table 1.
- arXiv 2410.16454v3 (Zhang et al.): abstract and §4.2.
- arXiv 2311.14648 (Kalai & Vempala): Def. 2, abstract, Corollary 1.
- arXiv 2509.04664v1 (Kalai et al.): §3.1, §3.3.1, Theorem 2.
- Figures read directly from the repo: Lee dedup perplexity, VaultGemma memorization, Cooper Fig. 3 (books and k-CBS), `lucki-finetune.png`, `syntax-similarity.png`.

All other corrections rest on the finding text and evidence entries. Every added href is in evidence.md:
- law.go.kr 1031810811, 1031810855 and 198081
- Garante 10085432
- NeurIPS Kurmanji 062d711fb777
- Vectara README e435b6bfb15d
- arXiv 2006.07709

## Open flags (not edited; need a decision or a check)

1. **lec01 S19, Eykholt tables.** The note follows F01: lab tests in Table 2, drive-by 84.8% in Table 3. While fetching v5, the worker saw that the paper's 100% summary row for camouflage art appears in Table 1. The note's "100% of lab images" may therefore be better cited to Table 1. Not changed.
2. **lec02 S62 case background.** It still says Jagielski et al. "found exactly such gaps in DP-SGD variants" and "later work found bugs in shuffling and sampling". This is outside F12 and was not re-verified.
3. **Deck alt-text errors** (lec05 S62, lec09 S50), listed above, are outside this job's scope.

## Checks (on the integrated head)

- `verify_notes.py 01 … 12`: ids_ok and h2_ok True, links_lost 0, nomsg 0, Key-takeaway 0 on all 12 notes. Links added:
  - lec01 +4
  - lec02 +1
  - lec03 +1
  - lec05 +1
  - lec06 +3
  - lec11 +1
- `lint-deck.py` on the 12 notes: 0 errors, 0 warnings.
- `outline-lint.py`: unchanged from round 1 (5 pre-existing warnings in infotheory and privacy). OUTLINE needs no change because no line pointers or structure moved.
- Render: every changed note was printed with headless Chromium.
  - `pdftotext` shows no ParseError and no raw `\frac`, `\mathrm` or `\varepsilon` in any of them.
  - Pages read at `-r 60`:
    - by workers: lec02 S29, S62; lec03 S50, S51; lec04 S56, S59; lec05 S29, S64; lec06 S14, S70–S71
    - by me: lec01 S08 and S19 (with neighbours), lec08 S63–S64, lec10 S48–S49, lec12 S19b/S19a and S42/S43
  - KaTeX rendered and nothing was clipped.
- `git diff --stat 15561e9 HEAD`: only the 12 notes.

## Deviations

- **Parallel work.** Six parallel subagents in separate worktrees under one brief, grouped by package. I integrated them by cherry-pick, reconciled the shared F10 and F12 wording across packages, re-ran all checks above and read every changed Message.
- **Message length.** 12 changed Messages run 51–59 words to keep a required qualifier:
  - lec01 S13, S19, S31, S34, S40
  - lec03 S47
  - lec04 S59
  - lec05 S50, S62
  - lec06 S56
  - lec11 S34
  - lec11 S73 (59 words: carries F57's required phrase)
- No fact was corrected from memory. No deck, tech supplement or teaching time changed.
