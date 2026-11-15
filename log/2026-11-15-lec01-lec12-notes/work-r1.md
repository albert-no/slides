# work-r1 — 2026-11-15-lec01-lec12-notes

## Branch and commits

- Branch: `2026-11-15-lec01-lec12-notes`, from baseline `99450923b41e94f10d0c557a4fc0f46b42a9c91d`.
- ID-only commit: `853024d`. Adds `data-slide-id="S01…SNN"` (sequential, scoped by deck) to the lec01–lec11 main slides and their paired note articles. 22 files, attribute additions only. lec12 IDs are kept as they were, including lettered splits.
- Log copy (job, plan-v1, requests, evidence): `9ab4aa0`.
- Head: the commit named in the pointer that delivers this file. Content diff for review: `git diff 853024d <head> -- courses/`.

## Per package

Each package rewrote one note, `courses/trustworthy-ai/lecNN-*-note.html`. Every article now opens with a **Message** (`p.msg`, 1–2 plain sentences that keep the needed qualifiers). Next comes **Reading the slide**, which explains the exhibit in its reading order. All earlier material follows inside `.detail` under `<h3>Script</h3>`: the script verbatim, then figure, technical depth, sources and assumptions, under their existing headings. `Key takeaway` lines were removed and their content folded into the Message. Overbroad seeds were qualified, not copied. Each note gets one CSS rule (`p.msg`) and an updated intro line describing the new order. Pace lines (`p.pace`) are unchanged.

| Pkg | Note | Articles | Commit | Msg words min/med/max |
|---|---|---|---|---|
| P1 | lec01 | 46 | b16e7f0 | 14/45/53 |
| P2 | lec02 | 69 | f38aa8f | 15/37/49 |
| P3 | lec03 | 70 | 526a818 (+ 15057f6, see Deviations) | 21/43/52 |
| P4 | lec04 | 65 | 5c56679 | 17/44/55 |
| P5 | lec05 | 68 | 68209f7 | 21/43/48 |
| P6 | lec06 | 75 | 0b5642c | 29/37/50 |
| P7 | lec07 | 75 | a022ce7 | 18/43/55 |
| P8 | lec08 | 101 | af13335 | 16/35/47 |
| P9 | lec09 | 91 | 101ec69 | 16/43/52 |
| P10 | lec10 | 88 | a40f90a | 31/44/50 |
| P11 | lec11 | 74 | 4668a6c | 9/45/55 |
| P12 | lec12 | 80 | 7da04f9 | 17/43/54 |
| | **total** | **902** | | |

The shortest Messages (9–20 words) are mostly title, divider and closer entries (plan rule 1). There are 39 of 902 Messages at 51–55 words: lec01 5, lec03 2, lec04 8, lec07 3, lec09 6, lec11 10, lec12 5. They are over the target only because they keep a qualifier.

Shared surface: `courses/trustworthy-ai/OUTLINE.md`. The note-format paragraph now describes Message → Reading the slide → Script, says that lec13–lec14 notes keep the older Key-takeaway format, and records the stable IDs on lec01–lec11. No line pointers changed. No deck, tech supplement or `reference/` file was edited after the ID commit.

## Slide mapping

Unchanged. All 902 slide/article pairs keep their page, order, ID and title, and there are no splits or moves. Main decks are untouched after `853024d`.

## Source and claim changes

- Links: no baseline href was lost in any note. Added links:
  - lec02: +1, De et al. 2022.
  - lec06: +2.
  - lec11: +1, reusing the EUR-Lex URL already cited at S65.
- Cross-references:
  - lec02: 34 position words ("previous slide" etc.) converted to slide IDs.
  - lec01: cross-lecture pointers corrected to the repo's lec numbering.
  - lec09 S81 and others: the note now gives explicit IDs.
- Qualified seeds (examples):
  - lec01 S16: deployer liability is stated as the cited rulings, not a universal rule.
  - lec02 S56: "keeps shrinking" is now an observation from Fig. 1 (2021–22 methods).
  - lec02 S30: "always randomized" becomes "non-constant".
  - lec06 S20: GPT-5 System Card Table 8 is a comparison, not an ablation.
  - lec07 S74: "one pattern" becomes a shared shape, not a proven common cause.
  - lec08 S35: transfer explanation attributed to Ilyas et al.
  - lec08 S15: "examples, not a rate".
  - lec10 S49: keeps the two panels apart.
  - lec12: chart readings marked approximate; S52 legal material dated as a snapshot, not legal advice.
- lec06 S07 note: a lone `$` before 31,100 changed to "USD 31,100…", matching the deck SVG.
- No fact was changed from memory. No source was re-fetched in this round. Sources dated 2026 (lec01 S08–S10/S24, lec07 S08–S10 and S73 quotes, lec06 S69 leaderboard, lec12 S52 law) rely on the note's existing verification dates.

## Unique details removed

- lec01 S09: the takeaway's "40× gap" is dropped. The ratio depends on which pair is chosen (34.7/0.8 vs IBM's 0.3), so the Message gives the endpoint numbers instead.
- lec07: two content-free takeaways removed: S03 "Keep this question in mind" and S38 "Headlines compress; we decompress".
- lec09 S26: the old figure description no longer matched the captured image. It now describes the image as captured; see plan issue 8.
- Nothing else. Every script paragraph and detail section is retained.

## Plan issues (need a decision; no slide edited)

1. **lec01 S42 / S02.** The 14 topic boxes don't match the repo's lec02–lec14:
   - lec07 alignment has no box;
   - fairness has two boxes for one lecture (lec12);
   - interpretability and governance exist only as backup decks.

   Also, S02 "fifteen topics" fits only if today counts. The note's Reading describes the slide as it is.
2. **lec01 S05.** The lending and healthcare cards have no case slide in Section 02.
3. **lec02 S56, S30, S68, S11.** Slide wording:
   - S56 "keep shrinking" claims a trend that Fig. 1 does not show;
   - S30 "always randomized" lacks "non-constant";
   - S68 has no scope (per unit and ε);
   - S11 "two still worked" omits that both were Stripe's own documented test keys.

   The notes qualify each one.
4. **lec03 S68.** The four-question incident strip has no baseline note content, so the Reading describes only what is visible. Content may be wanted.
5. **lec04 S42.** "Full set: about 1.9% near-duplicates" sits under Fig. 5(c). Per the note, 1.88% is Stable Diffusion against a 12M LAION subset. Suspected slide error.
6. **lec04 S50.** "~10×" sits under Lee Fig. 3, which shows about 5× (0.40 → ~0.08). The ~10× is the paper's unprompted-emission headline. Suspected slide error.
7. **lec05 S23.** "Correct and useless" overstates the point; suggested wording: "correct but too costly per request". **lec05 S12:** the subtitle "under regulatory pressure" sits uneasily with the cited chart.
8. **lec07 S74.** "Sycophancy, gaming, hacking: one pattern" is in tension with S70 ("a shared shape, not one demonstrated cause").
9. **lec08 S35.** "That is why they transfer" states Ilyas et al.'s interpretation as fact.
10. **lec09 S26.** The slide cites Shafahi et al. "Fig. 6(a)", but the captured image is a clean-label spam schematic, not a base/poison grid. Either the figure number or the crop is wrong. Not checked against the paper.
11. **lec09 S90 vs S87.** S90 asks 4 questions; the S87 checklist has 5 (clean performance). Add the fifth or drop the count? **lec09 S81:** the slide text itself says "previous slide" / "next example".
12. **lec10 S60.** The script says "Twenty minutes" for section 05; the pacing table gives 17.5 min (S60–S76). Script left verbatim because this is teaching time.

## Unsourced or unverified facts found (flag only)

- lec03 S47: C4 called "deduplicated"; no source in the note.
- lec04:
  - Cooper et al.: the deck says COLM 2026 in one place, the S56 slide and note say 2025 (the note keeps 2025).
  - S46 docket: link text 4:24-cv-05417, text 3:24-cv-05417.
  - Hayes et al.: (n, q) in S56 vs (n, p) in S58.
  - S31: "120M" on the slide vs "125M" in the note.
  - S58: "~20× greedy cost" vs "cost of twenty samples".
  - S12: "inserted once is already exposed" is generous against the plot (about 10 vs about 35).
- lec05:
  - S33: no reference URL for Kurmanji et al. (NeurIPS 2023).
  - S57/S62: "TMLR 2025", year unverified.
  - Several course-derived slides have no citation, as in the baseline.
- lec06:
  - S56: the script says "Farquhar and colleagues"; the table is Kuhn, Gal & Farquhar 2023 (the Reading names both).
  - S61: the slide says "reward a correct I don't know", but the table scores IDK 0.
  - S43: no worked prediction set.
- lec07:
  - S35: RE-Bench footnote vs hack rate, flagged.
  - S51: the transcript comes from a "don't hack" run, already disclosed.
- lec08:
  - S66: the "Roughly eight times" Assumptions paragraph belongs to S67; kept in place to avoid losing it. Decide whether to delete.
  - S84: Table 1/2 disagreement, already disclosed.
- lec12:
  - Chouldechova "Definition 2.2" in the note vs "Def. 2 / Def. 1" in the deck captions.
  - S52 Korean statute references not re-checked.
- lec06 deck S07 (not in scope): the bullet "The court fined the firms $31,100" has a single `$`. KaTeX auto-render needs a closing delimiter, so it most likely shows as a plain dollar sign. Not render-checked.

## Checks

- `verify_notes.py` (my own checker, run on the head for all 12 notes). It compares each article to the deck and to baseline 9945092:
  - IDs match the deck sequence;
  - h2 matches the baseline;
  - no baseline href is lost;
  - the Message is present and first;
  - there are 0 `Key takeaway` lines.

  Result: 902/902 pass.
- `lint-deck.py` on the 12 notes: 0 errors, 0 warnings. The baseline at `9ab4aa0` also has 0 warnings.
- `outline-lint.py`: 0 stale pointers, 5 warnings. All 5 predate this job (ambiguous basenames in `courses/infotheory` and `courses/privacy`).
- `git diff 9ab4aa0..HEAD --stat` touches only the 12 notes, `courses/trustworthy-ai/OUTLINE.md` and `log/2026-11-15-lec01-lec12-notes/`.
- Render: all 12 notes printed with headless Chromium and converted with `pdftoppm -r 60`.
  - Each package read its first, middle, last and math-heavy pages: 6–10 pages per note.
  - I re-read lec01 p2, lec02 p25 (theorem and definition math), lec08 p48 (S56 formula) and lec12 p33 (S41–S42).
  - Each page showed the Message first in larger type, KaTeX rendered and no clipping. `pdftotext` shows no raw `\frac` and no ParseError.
  - Raw `$` in the lec01, 02, 09 and 11 text is currency.

## Deviations

- **Delegation.** I ran the 12 packages as parallel subagents in separate worktrees under a shared brief, one note each. I integrated them by cherry-pick. I re-ran all checks above myself on the integrated head and spot-read the diffs.
- **lec03 repair `15057f6`, outside the content scope.** Since `9a772bd`, a sentence in the post-processing proof (S49 area) had been truncated to `…there.)$`, which rendered a stray dollar sign. I restored the sentence verbatim from `9a772bd`: "…see the slide index there. The same preimage argument shows the $(\varepsilon,\delta)$ guarantee itself survives post-processing.)" The text comes from git history, not from memory.
- The plan suggests about 30–50 words per Message. 39 Messages run to 51–55 words to keep qualifiers (rule 1: do not force a mechanical count).
