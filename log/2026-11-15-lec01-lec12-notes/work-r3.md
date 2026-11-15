# work-r3 — 2026-11-15-lec01-lec12-notes

Executes plan-v3 (C05–C08): main-slide corrections lec01–14, a full main/note audit, lec13/14 message-first notes and the notes design rule. One branch, no PR opened.

## Branch and commits

- Branch: `2026-11-15-lec01-lec12-notes`. Reviewed in round 2: `6dc5644`. Head: the commit named in the pointer that delivers this file.
- Log copy (review-r2, plan-v3, living files): `8c3ec7c`.
- **ID commit:** `594ebea`. It adds `data-slide-id` to lec13 (S01–S53) and lec14 (S01–S51), deck and note, and changes nothing else. lec01–12 already carried IDs.
- Content diff for review: `git diff 594ebea <head>`. 32 files (+787/−536): 28 deck/note files, the trustworthy-ai and root `OUTLINE.md`, `DESIGN_SYSTEM.md`, `PLANNER_BRIEF.md`. No `lecNNtech.html`, `reference/`, `figs/` or script file changed.

| Pkg | Scope | Commit | Items |
|---|---|---|---|
| P1 | lec01 | c07ae0f | M01–M07 |
| P2 | lec02 | 31ef7ed | M08–M17, F66, F67 (S29, S32) |
| P3 | lec03 | 46e396a | M18–M22 (M20 verified, unchanged), F67 (S51) |
| P4 | lec04 | 55de2f0 | M23–M31, F19 |
| P5 | lec05 | ba0a51c | M32–M38, F68 |
| P6 | lec06 | a98362e | M39–M42, F34 |
| P7 | lec07 | 6fb693f | M43–M45 |
| P8 | lec08 | 828052e | M46–M48; M53/E59 repeat on S39 (note), S94, S97 |
| P9 | lec09 | 2a256df | M49, M50; S86 audit fix (E56) |
| P10 | lec10 | 52604aa | M51–M53; E58 qualifier on S25 |
| P11 | lec11 | 8785867 | M54 |
| P12 | lec12 | 7bdf020 | M55, F56 |
| P13 | lec13 | ecc6e9a | new message-first note S01–S53; S36 suite name |
| P14 | lec14 | 81ec4f5 | M56, M57; new message-first note S01–S51 |
| P15 | docs, integration | 87013b7, 7e3982b, 4e97d4e | §9 contract, PLANNER_BRIEF, OUTLINE; render fixes (below) |

The lec09 and lec11 commit subjects carry the worker's internal labels ("P2", "P3"). Their plan packages are P9 and P11.

All 15 packages are complete. Every M item is fixed, except M20 (verified, unchanged) and M57 main (verified, unchanged; note fixed). None is disputed.

## Item dispositions (M01–M57)

Each fix is on the main slide (title, body, key, caption, alt or cite, as needed), and the note agrees in Message, Reading, Script and details. Repeated text in the same lecture was corrected too; those IDs are listed.

| M | IDs | Disposition | Main slide |
|---|---|---|---|
| M01 | lec01 S08 | fixed | headers "Labeled high risk, not rearrested" / "Labeled low risk, rearrested"; Northpointe answered with predictive parity; outcome is two-year rearrest, not offending |
| M02 | lec01 S12 | fixed | "Blocking this exploit does not establish removal of memorized data." |
| M03 | lec01 S13 | fixed | "€15M fine, Dec 2024; annulled at first instance, Mar 2026"; cite adds Tribunale di Roma 4153/2026 (E78) |
| M04 | lec01 S19, S40, S44 | fixed | lab classifier, not a production car; designed with the weights, applied with a printer; Fig. 1, Table 2 lab, Table 3 drive-by |
| M05 | lec01 S31 | fixed | "a named human overseer; impact assessment only a duty to try"; cite Arts 34–35 |
| M06 | lec01 S42 (+S02, S41) | fixed | "thirteen lectures after today", labels mapped to the taught lectures; S02/S41 "fourteen lectures" |
| M07 | lec01 S05 | fixed, note only | lending and healthcare get no case slide in this lecture |
| M08 | lec02 S03 | fixed | post-processing preserves the guarantee; later steps cannot retract an earlier disclosure |
| M09 | lec02 S09 | fixed | "Blocking an attack is not proof of erasure." |
| M10 | lec02 S11 | fixed | "two worked: Stripe *test* keys from Stripe's own docs" (Huang et al. arXiv 2309.07639 §5.2.2; E02 alone does not carry it) |
| M11 | lec02 S30, S33, S36, S40, S68 (+S17 note) | fixed | deterministic data-dependent release cannot be DP; ε = 0 means output independent of the data; δ in the list; large ε is a weak bound, not a measured leak; DP bounds MIA advantage, does not make it zero |
| M12 | lec02 S38, S41 | fixed | a single sample gives limited evidence; DP limits what Alice's own record adds |
| M13 | lec02 S43 | fixed | "A common DP recipe: calibrate added noise to sensitivity." |
| M14 | lec02 S46 | fixed | p̂; "the debiased sample estimate of p is 90%" |
| M15 | lec02 S56 | fixed | gap narrowed across this figure's 2021–22 methods: history, not a promise |
| M16 | lec02 S57 | fixed | at a fixed privacy target relative noise shrinks; "more data usually helps; not a theorem" |
| M17 | lec02 S62 | fixed | fixed δ and stated confidence; valid lower bound above the claimed upper bound challenges the guarantee or its assumptions; cite split Jagielski 2020 / Nasr et al. 2023 |
| M18 | lec03 S08 | fixed | "If eligibility requires the trait, membership alone reveals it." |
| M19 | lec03 S28 | fixed | "linked to overfitting"; sufficient, not necessary |
| M20 | lec03 S47 | verified, unchanged | no deduplication claim on the slide |
| M21 | lec03 S50, S51 | fixed | "DP outer bound", "allowed", "not every point under it is reachable"; S51 lower bound on ε, red-flag vs inconclusive cards |
| M22 | lec03 S59 | fixed | "Strongest attacker in these tests"; limited power on many one-epoch-pretraining records |
| M23 | lec04 S13 | fixed | match unlikely by chance, given the queries tried |
| M24 | lec04 S23, S26 | fixed | prompt later blocked, removal not shown |
| M25 | lec04 S36 | fixed | size and repetition push memorization up; more unique data is a different question |
| M26 | lec04 S42 | fixed | copy-detection proxy; smallest training set mostly copies; SD vs 12M LAION subset 1.88% above 0.5 |
| M27 | lec04 S50 | fixed | train-dup continuations drop ~5×; clean sets no worse, C4 Duplicates worse; right-image alt corrected |
| M28 | lec04 S53 | fixed | bounded-factor guarantee; "no memorization detected in this test" |
| M29 | lec04 S58 | fixed | k-CBS 1.4% / 2.6% at ε = 5 edits, greedy ~0.6%; deterministic lower bound, ~10× greedy token evaluations |
| M30 | lec04 S59 | fixed | 7.5% members vs 1.8% non-members, a measured false-positive rate |
| M31 | lec04 S60 | fixed | plateau measured on random data; separate natural-text runs |
| M32 | lec05 S18, S31, S50 (+S02 note) | fixed | certified = (ε,δ)-close under assumptions vs heuristic; implicit HVPs avoid forming the Hessian; heuristic LLM methods carry no certificate |
| M33 | lec05 S23 (+S10) | fixed | retraining costly per deletion request, not hopeless |
| M34 | lec05 S43 | fixed | facts enter mainly through fine-tuning; fewer pretraining confounders; compared with a retrained model |
| M35 | lec05 S48, S51 (+S52) | fixed | filter can be skipped by anyone running the weights; no gap is consistent with forgetting, not proof |
| M36 | lec05 S56 | fixed | 21% / 83% labelled as averages over tested methods; cause given as the authors' explanation |
| M37 | lec05 S61 (+S03) | fixed | refuses = filter or learned refusal; removed = proved by a certificate; audits support or refute |
| M38 | lec05 S62 (+S46, S66 notes) | fixed | new alt; RMU 61.6% (baseline 64.4%) after 10 retain-set examples, not after Wikitext (E36) |
| M39 | lec06 S22 | fixed | facts in fixed weights stop at the cutoff; the model may guess; no built-in "unseen" detector |
| M40 | lec06 S55, S56, S57 | fixed | conflict ⇒ likely invented; agreement / one meaning is no proof of truth |
| M41 | lec06 S67 | fixed | "generally less truthful"; UnifiedQA 2.8B beats 770M (checked on `figs/truthfulqa-size.png`) |
| M42 | lec06 S70 | fixed | o3 more claims, more right and more wrong; o4-mini smaller, less world knowledge |
| M43 | lec07 S08 | fixed | "Campaign 9–13 Jul 2026"; ≈2.5 days inside HF |
| M44 | lec07 S65 (+S63 note, S64) | fixed | share of flips to the hint whose reasoning credits the hint, corrected for chance (Chen et al. §2.1/§2.3) |
| M45 | lec07 S74 (+S69, S70) | fixed, **S70 renamed** | a shared shape, not one demonstrated cause |
| M46 | lec08 S35 | fixed | evidence supports features as one explanation of transfer |
| M47 | lec08 S64 | fixed | approximate inner maximization: PGD |
| M48 | lec08 S71 | fixed | robust = correct when clean and all four attacks fail: an estimate, not proof |
| M49 | lec09 S50 | fixed (alt) | per-dataset curves; no invented common endpoints |
| M50 | lec09 S81; S90 | fixed; S90 verified, unchanged | named slide and named Tran et al. histograms replace "previous/next" |
| M51 | lec10 S05, S06 | fixed, **S06 renamed** | prompts stayed online for months and worked in tests; success varied across model versions |
| M52 | lec10 S22 | fixed | later KL lower but nonzero |
| M53 | lec10 S36 (+S34, S35, S37 notes) | fixed | same suffix sent to black-box targets, incl. open-weight Llama-2 |
| M54 | lec11 S34 | fixed, **renamed** | conditional title; y label "AUROC upper bound"; "if paraphrase makes TV small" |
| M55 | lec12 S39a, S39b | fixed | transformed evaluation data, not a trained classifier; cite Fig. 4(a)/(c), §10, App. B.4–5 |
| M56 | lec14 S06 (+S50) | fixed | "Fixed, independent errors with no recovery compound with length."; S50 "unchecked errors can compound" |
| M57 | lec14 S33 | main verified, unchanged; note fixed | the note Message is dated: the 2025 judgment, not a 2026 measurement |

Beyond the M list, each settled by an existing source:
- lec10 S25: key "mean of 3 runs (GCG: best 3 of 10)", per E58.
- lec08 S39 (note), S94, S97: the M53/E59 "black-box / open-weight" wording, repeated across lectures. I accepted it as a terminology reconciliation with lec10. Revert it if it is out of scope.
- lec09 S86: "Detection fails" (E56, Wang et al. §VIII.C).
- lec13 S36: the "mail" suite is renamed "workspace" (AgentDojo v3 §3.1).
- lec14 S04 (note): "two additions" corrected to the three boxes on the slide.

### Renames (note `<h2>` = new deck title)

- lec07 S70: "One Pattern, Four Faces" → "One Shape, Four Faces".
- lec10 S06: "Jailbreak Prompts Are Shared and Last for Months" → "Jailbreak Prompts Are Shared and Stay Online for Months".
- lec11 S34: "If AI Text Looks Human, Every Detector Is Near a Coin Flip" → "Small Full-Text Distribution Distance Limits Detection".

## Residual groups

| F | Disposition |
|---|---|
| F19 lec04 S50 | Fixed. The note limitation now reads: unprompted ~10× vs the displayed prompted train-duplicate bars ~5×, "different evaluations". The C4 Duplicates exception is kept. The main slide carries the same split (M27). |
| F34 lec06 S55/S57 | Fixed. "Agreement is evidence against arbitrary confabulation in these samples, not proof of its absence"; S57 "does not exclude stochastic confabulation". The main slides say the same (M40). |
| F56 lec12 S39a/b | Fixed. The source captions read "transformed evaluation-data metrics; test-partition interpretation per §10 and Appendix B.4–5". The S44b source line is repeated. The Fig. 4 generator was not recovered, and the note says so. |
| F66 lec02 S62 | Fixed. "Means a bug" is gone. The failure modes are the Nasr §6.3 bugs. Jagielski's lower bounds stayed below the upper bounds (0.46 vs 4, §1.1/§4.2), and the shuffling/sampling claim is removed. Nasr is described as two training runs with intermediate-update access (E88). |
| F67 narrow overflow | Fixed. At 430px, lec02 S29 (+248) and S32 (+35) and lec03 S51 (+168) no longer overflow. The displays were split into steps, with side conditions moved into prose. |
| F68 lec05 S41 KS | Fixed. The "theorem" is now an illustration under stated idealized assumptions. Exact KS p-values are discrete and super-uniform. Counterexample n = m = 2: p ∈ {1/3, 1}, P(p ≥ 0.9) = 2/3 (I recomputed it). Added link: SciPy `ks_2samp` docs (HTTP 200). The main S41 has no KS claim and is verified, unchanged. |

## Coverage ledger: all 1006 pairs

Every ID was compared slide-vs-article: title, takeaway, body, key, alt, cited setup and qualifiers. "Consistent" means no disagreement, or none that an existing source settles. Disagreements without a settling source are listed under plan issues and were left unchanged.

| Lecture | IDs | Changed (main + note) | Note only | Consistent |
|---|---|---|---|---|
| lec01 | 46 | S02 S08 S12 S13 S19 S31 S40 S41 S42 S44 | S05 | all others |
| lec02 | 69 | S03 S09 S11 S30 S33 S36 S38 S40 S41 S43 S46 S56 S57 S62 S68 | S17 S29 S32 | all others (S27, S28, S39, S47: plan issues) |
| lec03 | 70 | S08 S28 S50 S51 S59 | — | all others (S47 verified for M20, S57 checked) |
| lec04 | 65 | S13 S23 S26 S36 S42 S50 S53 S58 S59 S60 | — | all others |
| lec05 | 68 | S03 S10 S18 S23 S31 S43 S48 S50 S51 S52 S56 S61 S62 | S02 S41 S46 S63 S66 | all others |
| lec06 | 75 | S22 S55 S56 S57 S67 S70 | — | all others (S08, S20: plan issues) |
| lec07 | 75 | S08 S64 S65 S69 S70 S74 | S63 | all others |
| lec08 | 101 | S35 S64 S71 S94 S97 | S39 | all others |
| lec09 | 91 | S50 (alt) S81 S86 | — | all others (S90 verified for M50) |
| lec10 | 88 | S05 S06 S22 S25 S36 | S34 S35 S37 | all others |
| lec11 | 74 | S34 | — | all others |
| lec12 | 80 | S39a S39b | S44b | all others |
| lec13 | 53 | S36 | S01–S53 converted; S44 detail Figs. 4–6; S45 Denominators | all (S05, S06, S07, S45: plan issues) |
| lec14 | 51 | S06 S50 | S01–S51 converted; S04, S33 | all (S11, S26: plan issues) |

Total: 1006 pairs, 84 main slides changed. Per-lecture article counts match the decks (46, 69, 70, 65, 68, 75, 75, 101, 91, 88, 74, 80, 53, 51).

## Changed main slides (page, line range at head)

There are no splits. Slide counts, IDs, order, `1 / N` and `.pace` lines are unchanged. Page = slide number, except lec12 (lettered splits).

- **lec01:**
  - S02 p2 L69–97
  - S08 p8 L164–196
  - S12 p12 L256–285
  - S13 p13 L286–320
  - S19 p19 L430–443
  - S31 p31 L670–697
  - S40 p40 L914–937
  - S41 p41 L938–945
  - S42 p42 L946–972
  - S44 p44 L993–1027
- **lec02:**
  - S03 p3 L88–130
  - S09 p9 L197–212
  - S11 p11 L229–244
  - S30 p30 L624–654
  - S33 p33 L682–711
  - S36 p36 L758–770
  - S38 p38 L801–813
  - S40 p40 L826–837
  - S41 p41 L838–846
  - S43 p43 L855–878
  - S46 p46 L932–940
  - S56 p56 L1107–1118
  - S57 p57 L1119–1151
  - S62 p62 L1207–1220
  - S68 p68 L1341–1353
- **lec03:**
  - S08 p8 L214–238
  - S28 p28 L649–663
  - S50 p50 L1094–1118
  - S51 p51 L1119–1138
  - S59 p59 L1261–1279
- **lec04:**
  - S13 p13 L324–335
  - S23 p23 L518–538
  - S26 p26 L577–589
  - S36 p36 L733–741
  - S42 p42 L814–828
  - S50 p50 L918–933
  - S53 p53 L988–1003
  - S58 p58 L1069–1084
  - S59 p59 L1085–1100
  - S60 p60 L1101–1117
- **lec05:**
  - S03 p3 L96–138
  - S10 p10 L265–297
  - S18 p18 L436–467
  - S23 p23 L565–577
  - S31 p31 L770–796
  - S43 p43 L995–1027
  - S48 p48 L1099–1118
  - S50 p50 L1127–1159
  - S51 p51 L1160–1177
  - S52 p52 L1178–1197
  - S56 p56 L1242–1258
  - S61 p61 L1327–1339
  - S62 p62 L1340–1357
- **lec06:**
  - S22 p22 L356–371
  - S55 p55 L815–823
  - S56 p56 L824–838
  - S57 p57 L839–863
  - S67 p67 L989–1003
  - S70 p70 L1057–1074
- **lec07:**
  - S08 p8 L141–149
  - S64 p64 L775–789
  - S65 p65 L790–810
  - S69 p69 L846–853
  - S70 p70 L854–867
  - S74 p74 L913–926
- **lec08:**
  - S35 p35 L438–450
  - S64 p64 L765–774
  - S71 p71 L849–858
  - S94 p94 L1120–1135
  - S97 p97 L1157–1169
- **lec09:**
  - S50 p50 L564–580
  - S81 p81 L950–963
  - S86 p86 L1011–1024
- **lec10:**
  - S05 p5 L100–108
  - S06 p6 L109–124
  - S22 p22 L282–298
  - S25 p25 L326–342
  - S36 p36 L450–465
- **lec11:**
  - S34 p34 L447–456
- **lec12:**
  - S39a p52 L1527–1545
  - S39b p53 L1546–1564
- **lec13:**
  - S36 p36 L722–735
- **lec14:**
  - S06 p6 L137–166
  - S50 p50 L866–879

Integrator fixes after merging (7e3982b), both found in the render audit:
- **lec02 S33:** the two-line "ignores / the data" label pushed the callout onto the footer. It is now a single label, "ignores data", and the viewBox is restored to `0 0 460 96`.
- **lec03 S50:** the moved "allowed" label touched the red bound line. It is back at the baseline label position (y = 150).

No type was shrunk in either fix.

## Doc edits (P15)

- **`DESIGN_SYSTEM.md` §9:** the "Speaker-script variant" paragraph is replaced by the **instructor-note contract**:
  - Message (`p.msg`, `.kt` label, qualifiers kept), then Explanation (for plots: axes, encodings, comparison, limits), then Details (sources, provenance, subordinate cues).
  - No repeated Key-takeaway line and no word cap; structural entries may be brief.
  - The main slide, Message, Explanation and Details must agree.
  - Pairing by `data-slide-id`; legible math, valid links, no horizontal overflow at ~430px, never shrink type.
  - `doc-index-lint.py --fix` was run.
- **`PLANNER_BRIEF.md`:** one sentence in the Companions paragraph points to the §9 contract and article-level acceptance.
- **`courses/trustworthy-ai/OUTLINE.md`:**
  - The notes paragraph now covers all 14 lectures under §9.
  - ID scheme: lec01–11, lec13 and lec14 use `S01…SNN`; lec12 uses S01–S78 with lettered splits.
  - lec13/14 entries now read "(IDs S01–S53/S51) … Message, Reading, script"; the old exception is removed.
  - Added a round-3 sentence: 84 main slides corrected, no splits, the three renames.
- **Root `OUTLINE.md`:** two lec02 pointers shifted by one line (`:802` → `:803`, `:1058` → `:1059`).

## Plan issues (not changed; for slides-review)

1. **lec06 S20:** "Rewarding 'I don't know' collapses the error rate" overstates causation against the GPT-5 System Card Table 8. The note Message already says it is not a controlled test, but the Script repeats the claim. Fixing it changes the argument.
2. **lec06 S08:** "Med-Gemini paper" on the slide vs a blog edit in the note. Unverified.
3. **lec02 S27** "No output can seriously contradict her", **S28** "The guarantee still holds" (needs same unit/adjacency) and **S47** "Noise hides people" are possible over-claims. **S39** is fine under pure DP but reads inconsistently with the S32 δ caveat.
4. **lec13 S45, "97 tasks":** 97 is AgentDojo's task count (arXiv 2406.13352v3, Introduction: "97 realistic tasks and 629 security test cases"). The CaMeL Table 2 caption does not state it. Suggest citing AgentDojo for that denominator.
5. **lec13:**
   - S07 "Today's main case: indirect" could read as a prevalence claim.
   - S05 "current models resist this exact wording much better" has no source.
   - S06 OWASP "3 Aug 2026" was not verified this round.
6. **lec14:**
   - S11 key line lacks "on this task set" (the note carries it).
   - S26 header "Today's evidence" could read as the state of the field.
   - The lec14 tech supplement's formal S06 was not checked for the no-recovery assumption (it is read-only for this job).
7. **lec01:** the course is now described as "fourteen lectures" (today + thirteen); interpretability and governance are named as backups in the S42 note. Please confirm against the course plan.

## Pre-existing render defects (unchanged slides or unchanged regions; reported, not fixed)

- **lec01 p31:** pyramid label "hiring · credit · health · courts" clipped at the band edges. Identical at 594ebea; only the right-hand bullet and cite changed.
- **lec05 p52:** dashed line crosses "members", curve crosses "non-members". Identical at 594ebea; only the caption changed.
- **lec05 p3:** "unlearning · this lecture" label touches or clips the right edge.
- **lec05 S43:** SVG text renders small (needs a figure redraw).
- **Render audit, unchanged slides:** lec02 p31, lec04 p22 and lec04 p52.

## Sources fetched this round

- Huang et al., arXiv 2309.07639, §5.2.2 (M10).
- Chen et al., arXiv 2505.05410v1, §2.1 and §2.3 (M44).
- AgentDojo, arXiv 2406.13352v3: §3.1 suites and Introduction counts (lec13 S36, S45).
- CaMeL, arXiv 2503.18813v2: Figs. 4–6, 9 and 11 captions, Tables 2–4 (lec13 S44, S45).
- Hammond et al., arXiv 2502.14143v1, §1: "errors that may be acceptable in isolation could compound in complex, dynamic networks of agents" (M56).
- SciPy `ks_2samp` docs (F68; E90).
- Local figure checked: `figs/truthfulqa-size.png` (M41), `figs/carlini-cost.png` (M49).

Everything else rests on existing evidence entries.

## Checks actually run

- **`verify_notes.py` 01–14:** ids_ok True, links_lost 0, nomsg 0, KT 0, order_bad [] for every lecture. h2_ok is False only for lec07, lec10 and lec11, which are the three renames.
- **`lint-deck.py`, all 28 deck/note files:** output identical to 594ebea (pre-existing warnings only).
- **`outline-lint.py`:** 0 stale pointers, 5 pre-existing warnings. **`doc-index-lint.py`:** clean after `--fix`.
- **Narrow display, headless Chromium at 430px, every note against 594ebea:**
  - No article is new or worse.
  - lec02 S29 and S32 and lec03 S51 are cleared.
  - lec07, lec08, lec10, lec13 and lec14 notes have no overflow.
  - Inherited overflows in lec02–06, lec09, lec11 and lec12 are unchanged and outside F67.
- **Link inventory against 594ebea:** one href added (SciPy `ks_2samp`, HTTP 200); no href lost in any deck or note.
- **Renders, Chromium print-to-PDF, `pdftoppm -r 60`:**
  - All 84 changed pages and their neighbours were viewed: 120 images in an independent audit, plus each worker's own views.
  - After the integrator fixes, I re-viewed lec02 p33 and lec03 p50 myself. I compared lec01 p31, lec03 p50 and lec05 p52 against their 594ebea renders.
- **Note PDFs:** `pdftotext` finds 0 raw `\frac`, `\mathrm` or `ParseError` in every changed note. Math and plot pages were viewed per lecture, plus about 5 pages spread through each of the lec13 and lec14 notes.
- **Spot-checks of worker claims against sources:**
  - F68 arithmetic (recomputed).
  - F66 wording vs E88.
  - lec01 Garante annulment vs E78.
  - lec10 330 pairs and GCG 3-of-10 vs E58.
  - Hammond quote (arXiv HTML).
  - lec13 97-task source (above).
