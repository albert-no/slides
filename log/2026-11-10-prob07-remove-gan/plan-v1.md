# plan-v1 — Remove GAN and JS from prob07

## 1. Summary and header

- Job: `2026-11-10-prob07-remove-gan`; medium; C01; two review rounds maximum.
- Baseline: `cdc2949fd21af93b014994acb56a4c048a95becb`. All page/line locators refer to this immutable commit.
- Deck: `courses/deepmath/prob07-estimation/prob07-estimation.html`.
- Companions: `courses/deepmath/prob07-estimation/prob07-estimation-note.html` and `courses/deepmath/prob07-estimation/prob07-estimation-note.md`.
- Audience/mode: existing junior-undergraduate AI majors; rigorous; preserve the retained explanations and pacing. No new time allocation; remove the GAN teaching time rather than refill it.
- Argument retained: estimation → MLE/CE → conditional-mean denoising → LLM/diffusion training → Gaussian bridge.
- Delete S128–S134 completely. Adjust S02, S118, S120 and S135 to discuss only the two retained example families. Target 137→130 slides if no other changes prove necessary.
- Sources: E01–E04. No new empirical, historical or mathematical claims.
- Layout and final count are executor decisions under DESIGN_SYSTEM; no type shrinking or new shared styling.

## 2. Coverage

| Comment | Baseline page / title | Slide IDs | Owner/package |
|---|---|---|---|
| C01 | 128 GANs — the Framework through 134 Dropping a Mode — KL vs. JS | S128–S134 | P1 |
| C01 | 120 Three Families You Have Already Used | S120 | P2 |
| C01 | 2 Contents; 118 Generative Models Are MLE?; 135 Generative Models — the Scorecard | S02, S118, S135 | slides integration |
| C01 | note §§11.4–11.6, retained §11.7; GAN references/outline | paired sections and shared references | P1 + slides integration |

## 3. Numbered change specifications

### 1. Delete S128 — baseline p128, “GANs — the Framework” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2244.
- Current generator/discriminator diagram, minimax objective and discussion → remove the complete slide; no replacement title, exhibit or teaching time.
- Notes: remove the corresponding GAN framework exposition in §11.5 in both companion files.
- Evidence: E01, E02. Acceptance: no generator–discriminator lesson remains in prob07.
- Reason: C01 explicitly removes the whole GAN part, not merely its name.

### 2. Delete S129 — baseline p129, “Jensen–Shannon Divergence — Definition” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2282.
- Current definition, properties and mixture interpretation → remove the complete slide; no replacement.
- Notes: remove §11.4 in both formats (definition, bounds, symmetry, all worked cases).
- Evidence: E01, E02. Acceptance: no JS definition/equation is retained in notes or an appendix.
- Reason: JS divergence is explicitly included in C01.

### 3. Delete S130 — baseline p130, “Worked — JS Stays Finite Where KL Breaks” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2302.
- Current worked KL/JS table and disjoint-support example → remove complete slide and matching §11.4 examples in both notes; do not move elsewhere.
- Evidence: E01, E02. Acceptance: worked JS values disappear with the lesson; unrelated KL remains.
- Reason: the worked example belongs to the deleted JS unit.

### 4. Delete S131 — baseline p131, “Step 1 — the Best Discriminator” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2319.
- Current discriminator optimization, formula, support caveats and plot → remove whole slide and corresponding §11.5 proof text in both notes.
- Evidence: E01, E02. Acceptance: no orphan Step 1, discriminator result or plot.
- Reason: it is the first step of the removed GAN argument.

### 5. Delete S132 — baseline p132, “Step 2 — Plug In: G Minimizes JS” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2346.
- Current substitution proof and Goodfellow theorem → remove whole slide and the matching §11.5 derivation from both notes.
- Evidence: E01, E02. Acceptance: no JS minimax identity or orphan Step 2 remains.
- Reason: it is the second step of the removed argument.

### 6. Delete S133 — baseline p133, “Reading the GAN Loss” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2364.
- Current MLE/minimax table, density-ratio interpretation and loss-variant discussion → remove whole slide and corresponding remainder of note §11.5, including StyleGAN/FFHQ material.
- Evidence: E01, E02. Acceptance: no GAN loss comparison or GAN-only real-world example remains.
- Reason: complete removal includes interpretation and caveats, not just formulas.

### 7. Delete S134 — baseline p134, “Dropping a Mode — KL vs. JS” (must)
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2385.
- Current two-fit comparison and mode-collapse caveat → remove whole slide and note §11.6 in both formats, including the reverse-KL comparison tied to this example.
- Evidence: E01, E02. Acceptance: no orphan multimodal example, JS numbers or mode-collapse discussion. Do not invent a replacement KL-only lesson.
- Reason: the complete example belongs to the removed GAN block.

### 8. Revise S120 — baseline p120, “Three Families You Have Already Used” (must; wording/layout [judgment])
- File: `courses/deepmath/prob07-estimation/prob07-estimation.html`, baseline line 2065.
- Point: two familiar examples lead to different likelihood-training objectives.
- Proposed title: “Two Generative Model Families”.
- Exhibit: retain only the language-model and diffusion examples; remove the entire GAN/StyleGAN card. Rebalance the surviving comparison; do not leave an empty third slot.
- Current three-family framing → two example families, not an exhaustive taxonomy. Keep the existing named examples, introduce no new claims.
- Replace the broad “only LLM…” conclusion with a scoped comparison of autoregressive cross-entropy training versus diffusion's bound/reweighted denoising. E03 qualifiers must survive.
- Notes: shared integration updates §11.1 from “All three families” to “Both example families”; preserve the discrete/continuous distinction.
- Layout: slides decides; time: retain only the surviving explanation, no padding.
- Evidence: E01–E03. Acceptance: two examples, no GAN reference, no claim that all LLM training is MLE or only two families exist.
- Reason: deleting the dedicated block alone would leave GAN content on this earlier slide.

### 9. Update shared teaching surfaces (must; proposed wording [judgment])
- S02 / p2 “Contents”, `courses/deepmath/prob07-estimation/prob07-estimation.html` line 59 (text at 148): “LLMs, diffusion, GANs as MLE?” → “LLMs and diffusion through likelihood”. Keep the existing 11-section structure and ordering.
- S118 / p118 “Generative Models Are MLE?”, same file line 2021: remove GAN from subtitle; proposed “LLMs and diffusion through the likelihood lens”. Match the section name with Contents; preserve the motivating question. Exhibit: existing divider treatment; no added content.
- S135 / p135 “Generative Models — the Scorecard”, same file line 2405: remove the GAN row entirely; retain the LLM and diffusion comparison. Point: exact autoregressive data likelihood differs from the diffusion bound/reweighted objective. Keep the title or shorten it at slides' judgment. Exhibit: two-family scorecard, visually balanced. Replace “Among these three training setups…” with a conclusion scoped to the two retained examples. Preserve full-bound/path likelihood versus generally-not-image-MLE, simple-loss reweighting and ordinary-CE training scope (E03).
- Notes: remove the GAN row and final GAN/JS sentence in §11.7; renumber the surviving scorecard §11.4 in both formats and repair its cross-references. Do not delete the whole scorecard section.
- Notes/tech: no relocation of removed content; no new supplement. Time: no added teaching time.
- Evidence: E01–E03. Acceptance: Contents/divider agree, two-family summary is accurate, S127→S135→S136 is a coherent transition.
- Reason: the lecture must no longer promise or summarize material it no longer teaches.

### 10. Synchronize references, outline and outputs (must)
- `courses/deepmath/prob07-estimation/prob07-estimation-note.html` and `courses/deepmath/prob07-estimation/prob07-estimation-note.md`, §12: remove the old references 7 (Goodfellow) and 12 (Karras/StyleGAN), which support only deleted content. Renumber remaining references and repair mentions such as “cited by reference 8”; retain diffusion, language-model, score-matching and general estimation sources.
- `courses/deepmath/OUTLINE.md`, prob07 entry: remove GAN/JS/StyleGAN/FFHQ and removed diagrams/examples from section 11 and its descriptive paragraphs; update section ranges, title/count, folder-table count and exact line pointers. Do not edit unrelated lectures' descriptions.
- Deck's own count indicator: recompute rather than include `slide-num` in the slide count. Deleted IDs are retired; later retained IDs never change.
- Refresh normal standalone outputs if the executor's workflow uses them; do not newly commit generated artifacts excluded by repository policy. No stale locally published copy should still expose the removed lesson.
- Evidence: E02, E04. Acceptance: both note editions agree, all remaining references resolve, count/ranges match actual slides, no dangling GAN/JS promises.
- Reason: “completely” includes the teaching companions and active metadata, not historical logs or independent lessons elsewhere.

## 4. Packages and integration ownership

| Package | Slide IDs / scope | Allowed file regions | Dependencies |
|---|---|---|---|
| P1 | S128–S134 deletion | main deck block; note HTML/Markdown §§11.4–11.6 | ID-only baseline first |
| P2 | S120 two-family comparison | S120 in main deck only | ID-only baseline; shared qualifier guardrail E03 |
| Integration (slides) | S02, S118, S135; counts and transitions | deck shared surfaces; notes §§11.1,11.7,12; prob07 leaf outline entry | after P1/P2 |

The ranges are disjoint. Separate workers are optional; the scope does not require parallel work. Integration edits note numbering/references once after package results, never concurrently. slides owns all deck/note/script work.

## 5. Preserved scope and prerequisites

- S01, S03–S117, S119, S121–S127, S136–S137: unchanged content, aside from required stable IDs or mechanically necessary page/reference corrections. No retrospective redesign of the rest of prob07.
- Keep the existing KL/CE, Gaussian-MLE and MMSE results; the surviving application already recalls them. No new recap or redefinition.
- Preserve Jensen's inequality in the diffusion ELBO derivation. It is not Jensen–Shannon divergence. Preserve JavaScript asset links; a naive case-insensitive `js` replacement is forbidden.
- Other courses' GAN/JS lessons and prob02's divergence discussion remain out of scope. Do not touch shared `reference/`, source tex, old logs or independent bibliography entries.
- For ID setup, follow the contract's separate ID-only commit. Current notes have chapter sections rather than per-slide articles: if mapping them faithfully needs new exposition or changes retained content, return a plan issue rather than silently refactor the whole note.

## 6. Acceptance / review handoff

1. Report branch, immutable review SHA and ID-only SHA in `work-r1.md`; provide old page → stable ID → new page/deleted mapping.
2. Search source and refreshed presentation artifacts for GAN/GANs, generative adversarial, discriminator, Jensen–Shannon/Jensen-Shannon, JS divergence/formulas, StyleGAN, Goodfellow and FFHQ. Explain any legitimate non-teaching/log or JavaScript hits; none of the removed teaching material may remain in prob07.
3. Verify retained KL, Jensen's inequality and all LLM/diffusion qualifiers against baseline; no collateral content deletion.
4. Check ordinary lint/outline checks and actually render changed slides plus their neighbours: S01–S03, S117–S121, S126–S127, S135–S137. In the deletion-only target these are new pp1–3,117–121,126–130.
5. Inspect final-size layouts: no empty third comparison slot, overlaps, bad wraps, tiny labels or font reduction. Verify continuity across the removal seam and synchronize both note editions.
6. Expect seven deleted slides and target 130; report any deviation and reason, not a hidden reshuffle. Only blocking findings initiate round 2. No PDF delivery requested.

## 7. Baseline page/title/ID map

IDs below are the assignment for the first ID-only commit, not attributes already present. Lines are navigation aids, never edit keys. End slide has no h2; use its role. Source: E01.

| Stable ID | Baseline page | Baseline heading | Deck line |
|---|---|---|---|
| S01 | 1 | Estimation: MLE, MAP & Fundamental Limits | 46 |
| S02 | 2 | Contents | 59 |
| S03 | 3 | Why Estimation? | 156 |
| S04 | 4 | Where Does the Loss Come From? | 164 |
| S05 | 5 | A Claim to Prove Today | 180 |
| S06 | 6 | Two Faces of One Problem | 194 |
| S07 | 7 | Conditional Expectation | 216 |
| S08 | 8 | Recall — Conditional pmf | 225 |
| S09 | 9 | Definition — Conditional Expectation | 244 |
| S10 | 10 | Worked — Conditional pmfs and Means | 260 |
| S11 | 11 | $\mathbb{E}[X \mid Y]$ Is a Random Variable | 277 |
| S12 | 12 | Theorem — The Tower Property | 318 |
| S13 | 13 | Tower Property — Proof | 331 |
| S14 | 14 | Why the Tower Matters Today | 348 |
| S15 | 15 | The Estimation Problem | 364 |
| S16 | 16 | Setup — Sample and Label | 373 |
| S17 | 17 | Running Example — Two Nationalities | 388 |
| S18 | 18 | The Two Height Densities | 402 |
| S19 | 19 | Two Questions About One Height | 423 |
| S20 | 20 | Maximum Likelihood | 446 |
| S21 | 21 | Definition — MLE | 455 |
| S22 | 22 | MLE on the Heights | 472 |
| S23 | 23 | Worked — $x = 176$ | 486 |
| S24 | 24 | MLE Decision Boundary | 501 |
| S25 | 25 | Worked — $x = 185$ | 524 |
| S26 | 26 | What MLE Ignores | 537 |
| S27 | 27 | Maximum a Posteriori | 551 |
| S28 | 28 | Definition — MAP | 560 |
| S29 | 29 | From Model to Posterior — Bayes' Rule | 577 |
| S30 | 30 | $p_X(x)$ Does Not Matter | 592 |
| S31 | 31 | Heights with a Prior | 605 |
| S32 | 32 | Worked — $x = 176$, with Prior | 620 |
| S33 | 33 | Worked — $x = 185$: They Disagree | 633 |
| S34 | 34 | The Prior Moves the Boundary | 649 |
| S35 | 35 | Theorem — MAP Is Bayes Optimal | 676 |
| S36 | 36 | Proof — Score Any Estimator | 691 |
| S37 | 37 | Proof — Maximize Each Term | 706 |
| S38 | 38 | Implication — Regularization Can Encode a Prior | 720 |
| S39 | 39 | Fano's Inequality | 735 |
| S40 | 40 | The Fundamental-Limit Question | 744 |
| S41 | 41 | Theorem — Fano's Inequality | 759 |
| S42 | 42 | Reading the Bound | 774 |
| S43 | 43 | Fano — Proof Overview | 789 |
| S44 | 44 | Proof Step 1 — The Error Flag | 802 |
| S45 | 45 | Proof Step 2 — First Expansion | 818 |
| S46 | 46 | Proof Step 3 — DPI Enters | 832 |
| S47 | 47 | Proof Step 4 — Second Expansion | 847 |
| S48 | 48 | Proof Step 5 — The Flag Term | 859 |
| S49 | 49 | Proof Step 6 — The Label Term, Split by $E$ | 873 |
| S50 | 50 | Proof Step 7 — Both Scenarios Bounded | 888 |
| S51 | 51 | Proof Step 8 — Assemble the Upper Bound | 899 |
| S52 | 52 | Proof Step 9 — Close the Sandwich | 913 |
| S53 | 53 | Fano — Proof Summary | 926 |
| S54 | 54 | Worked — a 1024-Class Problem | 950 |
| S55 | 55 | When Fano Says Nothing | 965 |
| S56 | 56 | What Fano Buys Us | 978 |
| S57 | 57 | Parameter Estimation | 993 |
| S58 | 58 | New Target: a Parameter | 1002 |
| S59 | 59 | Work with the Log-Likelihood | 1017 |
| S60 | 60 | Example — Bernoulli MLE | 1031 |
| S61 | 61 | Bernoulli — Log-Likelihood | 1045 |
| S62 | 62 | Bernoulli — Set the Derivative to Zero | 1059 |
| S63 | 63 | The Obvious Guess Is the MLE | 1072 |
| S64 | 64 | Worked — 10 Flips, 7 Heads | 1087 |
| S65 | 65 | The Log-Likelihood Curve | 1104 |
| S66 | 66 | Example — Gaussian MLE | 1126 |
| S67 | 67 | Gaussian — Solve for $\mu$ | 1142 |
| S68 | 68 | Gaussian — Solve for $\sigma^2$ | 1157 |
| S69 | 69 | Definition — Empirical Distribution | 1174 |
| S70 | 70 | Example — Ten Samples, Four Symbols | 1187 |
| S71 | 71 | Worked — Average Loss, Grouped by Symbol | 1220 |
| S72 | 72 | The Promised Proof — CE Loss Is MLE | 1237 |
| S73 | 73 | CE Loss Is MLE — via KL | 1252 |
| S74 | 74 | One Identity, Three Names | 1266 |
| S75 | 75 | Naive Bayes | 1282 |
| S76 | 76 | Classification Needs a Model | 1290 |
| S77 | 77 | Without Structure, the Model Is Huge | 1307 |
| S78 | 78 | The Naive Bayes Assumption | 1321 |
| S79 | 79 | Example — Spam Filter | 1340 |
| S80 | 80 | Example — MNIST Digits | 1376 |
| S81 | 81 | Example — Binarized $7 \times 7$ MNIST | 1387 |
| S82 | 82 | The Naive Bayes Classifier | 1460 |
| S83 | 83 | Fit the Parameters — by Counting | 1472 |
| S84 | 84 | Fit the Prior Too | 1488 |
| S85 | 85 | MAP with the Fitted Model | 1502 |
| S86 | 86 | Worked — a 10-Mail Training Set | 1514 |
| S87 | 87 | Worked — Classify a New Mail | 1530 |
| S88 | 88 | The Zero-Count Failure | 1544 |
| S89 | 89 | Laplace Smoothing | 1559 |
| S90 | 90 | Worked — Smoothing the Table | 1575 |
| S91 | 91 | Naive Bayes — What to Take Away | 1591 |
| S92 | 92 | Bias–Variance | 1606 |
| S93 | 93 | An Estimator Is a Random Variable | 1615 |
| S94 | 94 | Definition — Bias | 1629 |
| S95 | 95 | Definition — Variance of an Estimator | 1643 |
| S96 | 96 | Definition — Mean Squared Error | 1659 |
| S97 | 97 | Technique Review — Add and Subtract | 1673 |
| S98 | 98 | Theorem — Bias–Variance Decomposition | 1688 |
| S99 | 99 | Proof — Insert the Center, Expand | 1704 |
| S100 | 100 | Proof — The Cross Term Dies | 1720 |
| S101 | 101 | The Dartboard Picture | 1733 |
| S102 | 102 | Example — the Sample Mean | 1769 |
| S103 | 103 | Worked — Can Bias Ever Help? | 1786 |
| S104 | 104 | Worked — the Numbers | 1801 |
| S105 | 105 | MSE Across All True $p$ | 1817 |
| S106 | 106 | Implication — the Regularization Trade | 1840 |
| S107 | 107 | MMSE Estimation | 1855 |
| S108 | 108 | Setup — Denoising | 1864 |
| S109 | 109 | Theorem — MMSE $=$ Conditional Mean | 1894 |
| S110 | 110 | MMSE — Proof Overview | 1907 |
| S111 | 111 | Proof Step 1 — Insert and Expand | 1919 |
| S112 | 112 | Proof Step 2 — Tower on the Cross Term | 1934 |
| S113 | 113 | Proof Step 3 — the Inner Factor Is Zero | 1948 |
| S114 | 114 | Proof Step 4 — Read Off the Minimizer | 1959 |
| S115 | 115 | MMSE — Proof Summary | 1971 |
| S116 | 116 | Worked — the Table, One Last Time | 1991 |
| S117 | 117 | Implication — Denoisers Learn $\mathbb{E}[X\|Y]$ | 2006 |
| S118 | 118 | Generative Models Are MLE? | 2021 |
| S119 | 119 | Generative Models — Learn $p_{\text{data}}$, Then Sample | 2030 |
| S120 | 120 | Three Families You Have Already Used | 2065 |
| S121 | 121 | LLMs — the Chain Rule Gives the Likelihood | 2092 |
| S122 | 122 | Worked — Scoring “the cat sat” | 2110 |
| S123 | 123 | Real World — Pretraining Is MLE at Scale | 2128 |
| S124 | 124 | Diffusion — an Auxiliary Forward Process | 2146 |
| S125 | 125 | DDPM — Learn the Backward Steps | 2190 |
| S126 | 126 | Each Backward Step Is a Gaussian MLE | 2208 |
| S127 | 127 | The Full ELBO Is Path-Likelihood Training | 2225 |
| S128 | 128 | GANs — the Framework | 2244 |
| S129 | 129 | Jensen–Shannon Divergence — Definition | 2282 |
| S130 | 130 | Worked — JS Stays Finite Where KL Breaks | 2302 |
| S131 | 131 | Step 1 — the Best Discriminator | 2319 |
| S132 | 132 | Step 2 — Plug In: $G$ Minimizes JS | 2346 |
| S133 | 133 | Reading the GAN Loss | 2364 |
| S134 | 134 | Dropping a Mode — KL vs. JS | 2385 |
| S135 | 135 | Generative Models — the Scorecard | 2405 |
| S136 | 136 | Next — the Distribution That Kept Showing Up | 2423 |
| S137 | 137 | Questions? (end slide) | 2438 |
