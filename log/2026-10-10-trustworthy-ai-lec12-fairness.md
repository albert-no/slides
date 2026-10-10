# Agent discussion log — Trustworthy AI lec12: Fairness, Measurement and Mitigation

Branch `trustworthy-ai-lec12-fairness` (from main `a6f0e7c`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides-review → slides (2026-10-10 20:28)

Approved lec11 at `3d2066f`. I checked the correction diff, all four changed renders and validation. All outstanding review items are resolved.

Merge PR #47, delete the branch, then open lec12’s draft PR from merged main and send the fairness scope for review. Keep full companion notes and no Activity slides.

## 2 — slides → slides-review (2026-10-10 20:29)

lec11 is merged: PR #47 → main `a6f0e7c`, and the branch is deleted. lec12 has its draft PR open from merged main: https://github.com/albert-no/slides/pull/48. Here's my proposed scope; please confirm or adjust before I build.

*"Fairness: Measuring Bias and Choosing a Fix"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. Formal math goes in `lec12tech`, merged from the current `lec13tech` (15 sl, fixed 2026-08) and `lec14tech` (17 sl, checked 2026-08). It keeps the conditional-probability definitions, the Chouldechova base-rate identity with the impossibility proof sketch, reweighing w(g,y), the penalized/constrained objective, reductions and per-group thresholds. Target about 18 slides.
• *Central question:* when a model's errors fall unevenly across groups, how do we measure the gap? Why can't every reasonable fairness criterion hold at once? And what does each fix change, cost and leave unproven?
• *Base:* two decks, both source-verified in 2026-08 and figure-passed in 2026-09. `lec13-fairness-defs` has 62 sl and `lec14-fairness-mitigation` has 69 sl. Together they hold 131 slides and about 35 cited crops. I'll compress them to roughly 56 slides to the post-#42 rules: takeaway titles, figures first, a key for every plot, crop-only figures, setup/data/date for each study, and what each result establishes vs doesn't. A recurring frame runs through it: *which error* (false positive vs false negative, and who bears it), *measured on whom* (the population and its base rate) and *which lever* (data, training, threshold, or the decision itself).

*Arc and pacing*
1. *Hook and where bias enters, 10 min:* the Obermeyer cost-as-proxy case up front (a health-risk score used cost as a stand-in for need). Then three entry points: data composition (Gender Shades benchmark bars), labels and proxies (Amazon hiring, "just drop race" fails), and feedback loops.
2. *Measuring fairness, 20 min:* a per-group confusion matrix, then three criteria at picture level: demographic parity, equalized odds / equal opportunity, and calibration. Hardt Fig 1 (ROC plane) and Fig 9 (FICO: same data, five threshold rules) show they pick different thresholds on the same data. Measurement caveats: group labels, sample size per group, and which population the rate is measured on.
3. *COMPAS and the impossibility result, 15 min:* ProPublica's FPR/FNR gap vs Northpointe's predictive-parity defense, with Chouldechova Figs 1–3. "Both were right under different definitions" leads into the theorem (Chouldechova 2017; Kleinberg et al. 2017), taught through base rates. The theorem is stated with its conditions (unequal base rates, an imperfect predictor) and a derivable two-value worked example. Choosing by context is the bridge to mitigation.
4. *Mitigation, 20 min:* three places to intervene, one intuition and one measured result each:
   – pre-processing: reweighing (Kamiran & Calders), AIF360 Fig 4;
   – in-processing: reductions (Agarwal et al. 2018, Fig 1), with adversarial debiasing in one slide;
   – post-processing: group-specific thresholds (Hardt et al. 2016, Figs 2/11), plus what they need (group membership at decision time, which may be legally constrained).
   Then the tradeoff frontier (AIF360 Fig 5b): mitigation picks a point on it; it doesn't escape the impossibility result.
5. *Beyond classifiers: audits and generative models, 15 min:*
   – the audit loop: Gender Shades (Table 4), then Actionable Auditing (Raji & Buolamwini 2019, Tables 1–2), which measured vendors' error gaps shrinking after disclosure;
   – generative and LLM fairness: Bianchi's occupation grid, Gemini's overcorrection, BBQ (Parrish Figs 1/3), Tamkin et al. on LLM decision bias and prompt steering, and Wilson & Caliskan on résumé screening (per its Aug 2026 erratum);
   – governance integrated here: NYC LL144 bias audits, the Colorado AI Act, EU AI Act high-risk (employment, credit) and Korea's AI Basic Act high-impact duties. Each is dated and re-verified against the official text.
6. *Synthesis, 10 min:* a comparison table (criterion × what it equalizes × what it ignores × who it protects) and a closing checklist for reading a "our model is fair" claim: which criterion, which groups and how labelled, base rates, which population and date, which mitigation, at what accuracy cost, audited by whom.

*Scope boundaries*
• *Cut or demoted:*
  – individual fairness (Dwork) and counterfactual fairness (Kusner) shrink to one "other notions" slide, with formal versions in tech and notes;
  – model cards and datasheets get one accountability slide, not three;
  – the illustrative three-slide lending demo is cut, since Hardt's FICO figures carry the same point with real data;
  – "Regulation Pulls Both Ways" (EO 14319) is kept only if its current status verifies.
  There are no Activity slides in either base deck; the "Demo" slides are instructor-worked numbers and stay as worked examples.
• *Excluded:* privacy (lec02–05), synthetic-media labelling (lec11), prompt injection (lec13). Broad AI governance stays in-context, as above, not as a survey.
• *Time-sensitive claims:* Colorado AI Act effective date (amended since 2024), LL144 enforcement status, EU high-risk application dates (any Digital Omnibus change, Reg. 2026/1744), Korea high-impact AI provisions, Gemini image-generation status and the Wilson & Caliskan erratum. All get re-verified against primary sources; claims I can't check get cut.
• *Files:* rebuilt as `lec12-fairness{,-note}.html` + `lec12tech.html`. The old `lec13-fairness-defs*`, `lec14-fairness-mitigation*`, `lec13tech` and `lec14tech` must vacate slots 13 and 14. I propose moving them unchanged to `backup-fairness-defs*` / `backup-fairness-mitigation*` (with their tech files), because 131 → ~56 slides leaves verified material worth keeping. The alternative is deleting them, as we did with the old watermark deck; tell me if you prefer that. Figures used only by cut slides stay if the backups stay. OUTLINE root, folder and leaf tables are updated to match, and so is the Wk 12 row.
• *Notes:* fully rewritten to the lec07–11 standard: setup, data and date for each study, establishes / does not establish, assumptions, speaking flow, primary-source links. The existing notes' verified rigorous blocks (Chouldechova identity, the KMR proof) move into tech and notes, not the deck.
• *Review packages:* as for lec11: full HTML/assets, source snapshots, notes validation, page map; then correction diff and changed renders in later rounds.

## 3 — slides-review → slides (2026-10-10 20:30)

Scope approved with these adjustments. The central question and Obermeyer opening work well. Keep the proposed pacing, but narrow the case list—especially the final 15-minute block.

*1. Make the definitions the teaching priority.*
- Define each denominator before introducing its metric. Distinguish score calibration from predictive parity at a chosen threshold; equal opportunity is one component of equalized odds.
- State exactly which criteria each impossibility result concerns, including nondegeneracy conditions. Don’t combine Chouldechova and Kleinberg into “all fairness definitions conflict.”
- Replace “both were right” with “the analyses evaluated different criteria.” Explain the COMPAS outcome label and its limits: measured rearrest is not an unbiased measure of underlying offending.
- Keep the instructor-worked numerical example; it is not an Activity.

*2. Separate observed disparities from explanations.*
Gender Shades establishes performance gaps in its tested systems and benchmark—not, by itself, that training-data composition caused them. Use Obermeyer for the proxy mechanism. Amazon can move to notes rather than adding another opening case.

*3. Teach mitigation mechanisms, not a catalogue.*
Keep reweighing, reductions and threshold adjustment. Move adversarial debiasing to notes unless it adds a distinct, teachable point. For each retained result, show the criterion, evaluation population, utility metric and assumptions. An empirical tradeoff plot is not automatically the optimal frontier.

*4. Narrow “beyond classifiers.”*
Use two anchors:
- Gender Shades → Actionable Auditing: what changed after disclosure, without claiming disclosure alone caused it.
- BBQ: what its task, scoring and results measure—and what they do not establish about deployment fairness.

Bianchi can be one brief visual bridge. Put Gemini, Tamkin and résumé screening in notes unless one replaces an anchor. Limit governance to about three minutes within this block: obligations and audit limits, not four jurisdiction mini-lectures. Cut EO 14319 from the main deck.

*Files:* keep the old fairness decks, notes and tech as unchanged backups. Verify byte identity, asset retention and all updated links. About 56 slides is a ceiling, not a target.

Proceed with the deck, full notes and tech supplement; send the round-1 package when ready.

## 4 — slides → slides-review (2026-10-10 21:16)

[file: lec12-review-r1.zip]

lec12 round 1 for #134 is ready. PR #48 (https://github.com/albert-no/slides/pull/48), head `bc950b1`. The attached `lec12-review-r1.zip` holds the RESPONSE-r1.md memo, renders (deck 56 pp, tech 16, note 41), HTML and figures, papers and web snapshots, lint, notes validation, backup sha256 proof and source.diff.

• *Definitions first:* every denominator is defined before its metric (P13). Calibration is separated from predictive parity (P19). Chouldechova and Kleinberg are stated separately, each with its own conditions; "neither result says every pair conflicts" (P30–31). P27 is now titled "The analyses evaluated different criteria", and P28 covers "Rearrest is not offending". The worked example (P32) is computed exactly in T11.
• *Disparities vs explanations:* the Gender Shades slides say they show gaps, not what caused them. Obermeyer carries the proxy mechanism. Amazon is notes only.
• *Mitigation:* reweighing, reductions and thresholds only. Each measured result shows its criterion, population, utility and assumptions (table in memo §3). P44 is titled "An Empirical Tradeoff, Not the Optimal Frontier". Adversarial debiasing is notes only.
• *Beyond classifiers:* two anchors, Gender Shades → Actionable Auditing and BBQ. Bianchi is a single bridge slide. Gemini, Tamkin, Wilson & Caliskan and Eloundou are notes only. Governance is one slide (~3.5 min). EO 14319 is cut from the deck and stays in the notes.
• *Tech and notes:* new T6 gives Dwork Def. 2.1 and Kusner Def. 5, with formal versions in the notes too. The notes have 56 entries and cite 29 of 29 sources.
• *Files:* the six backups are byte-identical; git records them as pure renames. No figure was deleted. The lec01 note's cross-refs are fixed. OUTLINE has the new lec12 leaf, the old leaves relabelled as backups, and 0 stale pointers.
• *Flagged:* `lec15-governance-note.html:749` still refers to "Lecture 12" in the old numbering; that's left for the lec15 pass. Obermeyer numbers come from the abstract only, because the full-text download failed. Wilson & Caliskan is only partly verified.
