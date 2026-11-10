# work-r3 — 2026-11-10-lec12-visual-motivation

- Branch: `2026-11-10-lec12-visual-motivation`. Previous content head: `f2e696d`. Record-only commit: `f635738`.
- Head commit: named in the pointer message (the commit that adds this file).
- Scope: plan-v3 (C08) only. Two files changed:
  - S76 in `courses/trustworthy-ai/lec12-fairness.html`;
  - its paired note article in `lec12-fairness-note.html`.
- No other slides, figures, tech or OUTLINE content changed. Line numbers did not move, so the OUTLINE pointers still hold.

## F09 — classifier setup (S76, main p58)

- Title is now "Nine Methods, Different Classifier Setups". The slide comment and the note `<h2>` use the same wording.
- Bottom key line: "Paired dots: dark = logistic regression (LR) · light = random forest (RF)".
  - The rule now applies only to the coloured pairs.
  - The grey entries keep their explicit "(NN only)" and "(LR only)" labels.
- Note S76:
  - "Each method is run with…" is replaced with the plan's sentence: "Seven methods are run with LR and RF; adversarial debiasing uses NN only, and prejudice remover uses LR only."
  - Two further sentences say the dark/light rule covers the seven paired methods and that the grey dots are the two single-classifier exceptions.
  - Takeaway: "Colour is the method; for the seven paired methods, shade is the classifier."
- All nine methods and their stage grouping are kept. The source attribution (Fig. 5 legend, Table 2) is unchanged.

## F02 residual — eighth body line (S76)

- Key label shortened to "Fair representations". It renders on one line.
- The note keeps the full name: "The key shortens learning fair representations to 'Fair representations'."
- Rendered body lines: intro 1 + stage headings 1 + longest column 4 + shade key 1 = **7**.
- Type and spacing are native; no CSS changed.

## Checks

- `lint-deck.py`:
  - main: only the accepted inline source-colour warning;
  - note: ok.
- `outline-lint.py`: 0 stale or missing pointers. The 5 warnings are pre-existing and unrelated.
- Rendered at `-r 60` and viewed main pp57–59 (S43b, S76, S44a): no overflow, overlap or clipping.
- S44a's pointer "full key, previous slide" still holds.
