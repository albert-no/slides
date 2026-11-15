# work-r4 — 2026-11-15-lec01-lec12-notes

Executes plan-v4 (C09): the 13 blocking groups of review-r3, and a recorded disposition for every optional item. Bounded pass on top of ef453a8; no broad re-audit. One branch, no PR opened.

## Branch and commits

- Branch: `2026-11-15-lec01-lec12-notes`. Reviewed in round 3: `ef453a8`. Head: the commit named in the pointer that delivers this file.
- Commits after ef453a8:
  - `89a07bc` log: refresh job.md (r3 in-review)
  - `35f6a84` log: copy review-r3 and plan-v4; refresh living job files
  - `3456017` content: all round-4 slide, note and outline changes (21 files, +181/−173)
  - the work-r4 commit (this file and refreshed living files; log only)
- Content diff for review: `git diff ef453a8 3456017`. Files: decks and notes of lec01–06, lec08, lec13, lec14; lec10 note only; `courses/trustworthy-ai/OUTLINE.md`; root `OUTLINE.md`. No tech supplement, `reference/`, `figs/`, script, backup, Korean note, `DESIGN_SYSTEM.md` or `PLANNER_BRIEF.md` changed. No slide IDs added (all decks already carry them).
- All work was done in the main session in one commit; the r4A/r4B worktrees created at the start were removed unused.

## Per package

| Pkg | Lecture | Changes |
|---|---|---|
| P1 | lec01 | F69 note S12 denominator; F70 note S42 (pure vs approximate DP, watermark null, Chouldechova conditions); F101 main+note S23 and leaf OUTLINE (4.5-day campaign vs ≈2.5 days inside HF); F71 main S31 label split |
| P2 | lec02 | F73a–e (S27, S33, S36, S39 main+note; S41 note); F74 note S57 and same-claim repetition S54; F76 note S10 wording; F77 main S29 marker; S28 clarification; F72 root OUTLINE pointers |
| P3 | lec03 | F73f main+note S49 |
| P4 | lec04 | F73g main+note S53; F75 note S13 |
| P5 | lec05 | F80 main+note S61, note S63, S66; F81 main S09, S55; F82 note (logit lens vs RMU, two places); F83 note S50; F84 main S03, S52, S43 |
| P6 | lec06 | F34 note S57; F78 main+note S20; F79 main+note S08 (retitle) |
| P8 | lec08 | F86 main+note S35 locator |
| P10 | lec10 | F85 note S25 |
| P13 | lec13 | F87 (S05), F88 (S14), F89 (S09, S13), F90 (S45 main+note, S46), F91 (S41), F92 (S50) |
| P14 | lec14 | F93 main+note S19; F97 main+note S31; F94 locators (S08, S10–S13, S21, S36–S42, S45 and leaf OUTLINE source line); F95 S21; F96 S11; F98 S32; F99 S27; F100 S43 |
| P15 | integration | leaf OUTLINE revision paragraph (round-3 count 84 kept; this pass 31 main slides), lec14 source summary, F101 line; root OUTLINE F72 |

## Blocking findings

| ID | Where | Done |
|---|---|---|
| F34 | lec06 note S57 | Fixed. Empirical frequency / plug-in estimate wording; population P(c\|x)=1 stated as a separate premise; uniform population mass gives log K. |
| F69 | lec01 note S12 | Fixed with the review's sentence (15,000 tested attack generations, 16.9% verified PII; not the normal-use leak rate, which the paper does not measure). |
| F70 | lec01 note S42 | Fixed. e^ε budget sentence limited to pure DP (δ=0); approximate DP gets the additive event bound and composition tracks ε and δ. Watermark: ideal independent green-membership null, normal approximation, repeated n-grams and empirical FPR calibration, evidence for this watermark only. Chouldechova: shared PPV strictly between 0 and 1, nonzero TPR. Kleinberg statement kept. |
| F73 | lec02 S27, S33, S36, S39, S41; lec03 S49; lec04 S53 | Fixed on main and note. Pure-DP statements now say δ=0; approximate-DP statements add the additive δ. S33 note adds that a fixed positive δ alone is not enough ((0,δ) can reveal the dataset) and scopes the 2.7× claim to pure DP. lec02 technical L764–769 kept. |
| F74 | lec02 note S57 (+S54) | Fixed. "Technical depth — optional · a bounded heuristic": amplification by subsampling as a heuristic, no closed-form guarantee and no "ten times the data" claim; E104 one-step counterexample mentioned; Abadi et al. §3.1 Thm 1 / App. B cited as conditional (regime ε < c₁q²T, unspecified constants), link added. Same-claim repetition on S54 repaired, see Deviations. |
| F78 | lec06 S20 | Fixed. Main muted line: "More abstention, fewer errors at similar accuracy; different models, not a training ablation." Note Reading, Script and definitions describe an aggregate comparison only. |
| F79 | lec06 S08 | Fixed. Retitled "A Fluent Medical Term Was Wrong" (main h2, comment, note h2). Bullets: no such brain area / correct term basal ganglia; flagged by neurologist Bryan Moore; still in the paper when reported, Aug 2025. Blend diagram replaced by observed-vs-correct boxes with "Observed error; its internal cause is not shown." and "Google's account: a learned mis-transcription." Cite: Yang et al. 2405.03162v1 Fig. 9; Google Research blog 15 May 2024; The Verge Aug 2025. Note: "about a year", "unnoticed" and "the model blended" removed; mis-transcription attributed to Google; Saab 2404.18416 link replaced by Yang 2405.03162v1 (Fig. 9, p. 28) and the blog; Verge link kept; paper called an arXiv preprint (no peer-review implication); no clinical outcome claimed. |
| F80 | lec05 S61, S63, S66 | Fixed. Main lead "Three different claims, each with its own evidence." (title kept). Note drops the strict ladder: robustness over adaptations strengthens a fixed behavioural target; removal is a different target, and a model matching retraining can still state a fact the retained data supports. S63: TOFU as a suite with a retain-only retrained reference (MUSE also supplies one). S66: review's document-vs-concept wording. |
| F81 | lec05 S09, S55 | Fixed. "Membership inference can provide evidence she was in"; "Faster recovery than the same retrained control suggests a remaining trace". |
| F85 | lec10 note S25 | Fixed. Script: "GCG was re-optimized against each evaluated model, including the augmented model." Limitations: "these tested attack families and budgets do not establish robustness to all adaptive attacks (Appendix A.4 …)". Rates, top-3-of-10 rule and no-guarantee statement kept. |
| F93 | lec14 S19 | Fixed. Main: "Across scheming follow-ups, o1 denied its actions over 85% of the time"; Fig. 3 added to the cite. Note names the oversight-subversion, self-exfiltration and goal-guarding evaluations and says the 85% is not read from the oversight table. 2%, pre-release, 300/100 and capability-not-deployment caveats kept. |
| F97 | lec14 S31 | Fixed. Main: "Self-replication helped most global-message scenarios; data theft was an exception"; "Failure-reason breakdown, "ignored": GPT-4o 66%, GPT-3.5 9%"; "Not a resistance rate over all attacks". Ranking removed. Cite: §5; Figs. 4–5 (apps), Fig. 6 (society). Note flags the source-prose vs Fig. 4 ambiguity without inventing an all-attempt denominator, attributes the execution-reliability explanation to the authors, and gives the larger-agent data-theft exception (§5.1, Fig. 4). The third main bullet ("once compromised, GPT-4o carried out payloads more reliably") moved to the note as the authors' reading. |
| F101 | lec01 S23; leaf OUTLINE L188 | Fixed. Timeline row "Reaches Hugging Face; ≈2.5 days inside its production systems"; number label "reconstructed campaign, incl. external staging"; note Message, Reading, Script and evidence separate the 4.5-day campaign from ≈2.5 days inside HF, 17,600 actions across the campaign. Outline line matches. |

## Optional findings

| ID | Disposition |
|---|---|
| F71 | Fixed. lec01 S31 high-risk label split into two white 12-px lines ("hiring · credit", "health · courts"); "high risk" moved up. |
| F72 | Fixed. Root OUTLINE `lec02-privacy-dp.html:803`→`:802`, `:1059`→`:1058` (headings verified at those lines after edits). |
| F75 | Fixed with the review's exact-guess wording; the q/\|R\| sentence merged so it is not stated twice. |
| F76 | Fixed. "The four comparison models before the ChatGPT bars sit below 1%…". |
| F77 | Fixed. lec02 S29 171 cm marker at x=273, on the scale set by the 168 (x=205) and 170 (x=250) modes. |
| F82 | Fixed. Logit lens described as much weaker against RMU, near-chance residual-stream decoding (two places). |
| F83 | Fixed. Proposition scoped to population/expected metrics, distributions of statistics rather than equal realized numbers; final line uses the review's wording. |
| F84 | Fixed. lec05 S03 label split; S52 labels repositioned; S43 grid `1fr 1.7fr`, svg max-width removed. |
| F86 | Fixed. "§3.2 (relabelled-data experiment) and §3.3 (transferability)" on main and both note places. |
| F87 | Fixed with the review's sentence. |
| F88 | Fixed. "among valid outputs" in Message; setup and source name Table 3 ASR-valid and the exclusion of invalid outputs. |
| F89 | Fixed. "three illustrated regions" (Reading and Script); S13 arrow sentence per the review. |
| F90 | Fixed. AgentDojo v3 named as the 97-task source (note setup, new AgentDojo source line, main cite "97 AgentDojo v3 tasks"); S46 "opening answer in §9.3" in Reading and Script. |
| F91 | Fixed with the review's sentence. |
| F92 | Fixed with the review's sentence. |
| F94 | Fixed. Shevlane §4 (main+note S08); Kwa identified as v4 (10 Jul 2026, 2019–2025 cohort) with limitations §5–6 and App. B.2/E.3–E.4 in the five source lines; main S10 §3.2.1; main S12 and note S12 §3.2.1, §5–6, App. E.3–E.4; main S13 §5–6 and App. B.2; S10 note "Fig. 1's embedded subtitle and §2.2 count 169" (169/170 kept, not harmonized); S21 Fig. 7 vs Fig. 8/Table 2; Greenblatt limitations §5.1 (seven source lines, S45 note and main), no-split caveat §2.4 (S41 main+note), main S41 Table 7; leaf OUTLINE lec14 source summary updated (Kwa v4 sections, Greenblatt Tables 2 and 7, §2.4, §5.1; Prompt Infection Figs. 4–6). |
| F95 | Fixed. "MMLU biology: control" / "MMLU bio (control)"; note specifies the biology-subject subset; the 46% is qualified as WMDP-Cyber in the broader study (Table 8), not this comparison. |
| F96 | Fixed. "Doubling on this task suite: 207 days." |
| F98 | Fixed. Main highlight and note Message/Script use "Handcrafted-attack success does not establish robustness to new adaptive attacks"; manual counterattack on marking kept. |
| F99 | Fixed with the review's three modes and percentages. |
| F100 | Fixed. "among decisive attempted attacks" on main S43 and note; note explains that uncaught failures and aborts are excluded. |
| lec02 S28 | Fixed. Note Message and Script add that the original release's guarantee holds at the same protected unit and adjacency, and extra releases need their own privacy accounting. |

None declined.

## Slide mapping

No slide was added, removed, split or moved; every page number is unchanged. One title changed.

| Lecture | ID | Old page | New page | Title / split / move |
|---|---|---|---|---|
| lec01 | S23, S31 | 23, 31 | 23, 31 | text/label only |
| lec02 | S27, S29, S33, S36, S39 | same | same | text/marker only |
| lec03 | S49 | 49 | 49 | text only |
| lec04 | S53 | 53 | 53 | text only |
| lec05 | S03, S09, S43, S52, S55, S61 | same | same | text/layout only |
| lec06 | S08 | 8 | 8 | retitled "Invented Medical Facts" → "A Fluent Medical Term Was Wrong"; diagram replaced |
| lec06 | S20 | 20 | 20 | text only |
| lec08 | S35 | 35 | 35 | cite only |
| lec13 | S45 | 45 | 45 | cite only |
| lec14 | S08, S10, S11, S12, S13, S19, S21, S31, S32, S41, S43, S45 | same | same | text/cite only |

Note-only changes: lec01 S12, S42; lec02 S10, S28, S41, S54, S57; lec04 S13; lec05 S50, S63, S66 and the two logit-lens places; lec06 S57; lec10 S25; lec13 S05, S09, S13, S14, S41, S46, S50; lec14 S09, S27, S36–S40, S42.

31 main slides changed in this pass (lec06 S07 appears in an ID diff only because the S08 comment line sits above the S08 div).

## Deviations from the plan

- **lec02 S54, same-claim repetition of F74.** The note carried the same unconditional dp5 "Theorem (DP-SGD privacy)" with a proof ending in □. Relabelled "Heuristic calibration (privacy course dp5; not a theorem as stated)", sketch renamed "Heuristic sketch", ending "yields the heuristic scale above", □ removed. Authorized by plan-v4's same-claim-repetition clause (E104). E104's counterexample was checked numerically before the edit.
- **lec01 S23 timeline row** reads "Reaches Hugging Face; …" rather than "Campaign reaches Hugging Face; …": the longer row wrapped and pushed the number cards onto the cite.
- **lec02 S27 highlight** shortened to "Small ε, δ = 0: limited added evidence about her." The longer F73a sentence wrapped to two lines and touched the footer. The note keeps the full sentence.
- **lec14 S31** third app bullet moved to the note, as plan-v4 allows.

## Plan issues

1. **dp5 source, out of scope.** The privacy-course dp5 deck that lec02 S54 copied still states the DP-SGD calibration as an unconditional theorem with proof. Not edited (other course). Needs its own job.
2. **Planning omission, M11/E98.** plan-v3 M11 left out the pure-DP qualification that E98 already contained. F73a repairs the outcome; recorded here as plan-v4 asks.
3. None of the fixes changes the argument, required content, scope or teaching time.

## Unsourced facts

None added. Every new number or locator comes from review-r3, plan-v4 or the evidence entries it cites (E100–E141). That includes Kwa v4's date and sections, Table 8 and WMDP-Cyber, the 15.7/13.2/12.4 modes, Table 7 exclusions, AgentDojo v3, Fig. 3, and Figs. 4–5. Facts verified directly this round: the lec06 S08 Verge URL matches E111; E104's counterexample was recomputed (p(D′)=2.74e-6 against e·p(D′)+δ=8.45e-6 versus p(D)=1.00e-2).

## Checks actually run

- `scripts/lint-deck.py` on all 19 changed deck and note files: no errors and no font-size warnings. lec06 deck keeps 6 pre-existing hardcoded-colour warnings, all on unchanged slides.
- `verify_notes.py` 01–06, 08, 10, 13, 14: article and ID counts match their decks and the order is correct.
  - lec06: h2_ok=False because of the intended S08 retitle, compared with the pre-job baseline; links_lost=1 is the Saab link replaced on purpose.
  - lec10: h2_ok=False is the round-3 S06 retitle, unchanged here.
- `narrow_check.py` on the 10 changed notes at 430 px matches ef453a8 exactly; no new wide math.
- `scripts/outline-lint.py`: 0 stale. The 5 warnings are pre-existing, in other courses. `scripts/doc-index-lint.py`: ok (docs not edited).
- Render check at `-r 60` of every changed main slide:
  - lec01 p23, p31; lec02 p27, p29, p33, p36, p39; lec03 p49; lec04 p53
  - lec05 p3, p9, p43, p52, p55, p61; lec06 p8, p20; lec08 p35; lec13 p45
  - lec14 p8, p10–13, p19, p21, p31, p32, p41, p43, p45
- Three render defects were fixed and re-rendered clean: lec01 p23 cards on the cite, lec02 p27 highlight at the footer, lec13 p45 cite wrapping into the last bullet.
- lec05 p61's two-line muted footer and lec02 p29's "Japan" label crossing its curve are unchanged layout, not new defects.
