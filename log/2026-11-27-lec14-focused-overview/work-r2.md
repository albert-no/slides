# work-r2 — 2026-11-27-lec14-focused-overview

- **Branch:** `2026-11-27-lec14-focused-overview`. r1 head `1d44931`; this round's head is the commit named in the pointer.
- **Scope:** review-r1 (F01–F08) and plan-v4. The commit also holds unchanged copies of `review-r1.md` and `plan-v4.md` and refreshed copies of `job.md`, `requests.md` and `evidence.md`.
- **Counts:**
  - Main deck: **59 slides** (`1 / 59`), 59 note articles, 85 + 5 = 90 min. The section split is unchanged: Opening 5, 01 20, 02 35, 03 20, Closing 5.
  - Backup deck: **52 slides** (`1 / 52`), 52 note articles, 0 core minutes. That is 47 slides in r1, plus S95 and S91–S94.
- **Method:** I did this round myself in the r1 package fragments, then rebuilt both decks and the notes. No subagents.

## Finding dispositions

| ID | Disposition | Where · what changed |
|---|---|---|
| F01 | Fixed | **S69b (p29):** the judge box and flow now show the coherence step. Incoherent answers are dropped first, then the misaligned share is taken among the answers kept. The note gives the exact thresholds: coherence below 50 is discarded, and alignment below 30 among kept answers counts as misaligned. The message and alt text match. **S70 (p30):** shows only the **left subplot of Fig. 3a** (free-form questions), as the new crop `p2a-cloud-fig3a-left.png`. The baseline, all teacher conditions, the axis and the intervals are untouched; the crop is recorded in `p2a-PROVENANCE.md`. The key reads "share of kept, coherent answers judged misaligned". The approximate value from the text stays text and is not drawn as a bar. The full panel a moved to backup S91. |
| F02 | Fixed | **S72b (p33) "A Finding, Not a Universal Rule":** one evidence-boundary diagram. It uses only the two experiments already taught. Shown: owl/animal choice in tested model pairs via number lists; harmful answers from one insecure-code teacher, GPT-4.1, 8 questions. Not shown: untested model pairs and other data; other harmful traits, models and everyday use. No new paper, method or controversy appears. The three preprints moved to S92–S94, and their notes and citations moved with them. **S75b (p40) "A Safer Teacher Helped in These Tests":** one recovery sequence: narrowly misaligned learner → training guided by an aligned teacher, all its outputs kept → measured misalignment near base-model levels. The slide names what was tested: Llama-3.1-8B and OLMo-3-7B, 3 epochs, all three training routes. The boundary line reads "A recovery result in tested models, not a general remedy". There are no numeric bars. The "Fix study" bullet was removed (now S93). The training-time vs run-time transition stays in the note. Sources: Askin v2 §4.2, Fig. 5 (OLMo), Fig. 25 (Llama), App. E.3. |
| F03 | Fixed | **S78 (p55)** and **S45 (p56)** now state the denominator correctly: attempts that were neither caught nor successful are excluded, so the score is conditional on one of those two outcomes. "Per attempt" and "of attacks attempted" were removed. The notes match. |
| F04 | Fixed | **S74b (p38):** visible metric key added. The "three rounds" label now reads "after 3 epochs", as in the source. The key line is "Bars: learner answers judged misaligned and coherent (%) · Llama-3.1-8B · after 3 epochs". |
| F05 | Fixed | **S39b (p50):** the "no expert check" label is now only on the unaudited branch. The audited-clean branch no longer enters that box. |
| F06 | Fixed | Long bare URLs in the S79 backup note (backup p42, page unchanged) and the S45 main note are now descriptive link text; the text size is unchanged. Check: chromium's minimum window width is **485 px**, so I could not test at 430 px. At 485 px both notes have `scrollWidth` = 485 = viewport width. The only nodes wider than the viewport are hidden KaTeX MathML, which takes no layout space. If 430 px must be tested exactly, a device-emulation check would be needed; I did not run one. |
| F07 | Taken | **S59 (p15):** the cross is now an SVG path. **S76 (p44):** the cross is now a sans-serif ×. Both render with no missing-glyph box. |
| F08 | Taken | **S71 (p31)** names and defines **subliminal learning** once in plain language. It is not repeated elsewhere. |

## Deviations and plan issues

1. **S69b time:** plan-v4 says "retain 1.5 min", but r1 already had S69b at **2.25 min** (work-r1, P2a row). I kept 2.25 so the main total stays 85 + 5. Going to 1.5 would leave 0.75 min unassigned. Please confirm 2.25 or say where the 0.75 min should go. This is a teaching-time question, so I did not decide it.
2. **S92 title:** "Reproduction Varied by **Model,** Trait and Task" instead of the plan's "by Trait and Task". The exhibit (Fig. 2a, animal row) varies mainly by model (Qwen mostly positive, Gemma mixed, Ministral almost none), so a title without "model" would not describe what the figure shows. This is a design choice under my authority; reverting is a one-word change if you prefer.
3. **S91 y-axis:** the source figure is unaltered, so its shared y-axis label ("Misaligned response rate") stays on both subplots. Plan-v4's acceptance asks for "no common y-axis definition that conflates the outcomes". I met that with two separate visible keys beside the figure, one per subplot: left = kept, coherent answers judged misaligned; right = false answers on TruthfulQA. A muted line adds "A wrong fact is not a harmful intent: two separate measures." Editing the source label would change the figure, so I did not.
4. **S72b SVG:** I compressed the diagram height to 280 px so that the muted boundary line no longer touches the citation. Type size is unchanged.

## Backup mapping (new and changed)

`slide ID | backup page | source`

| ID | Page | Content |
|---|---|---|
| S80 | 1 | title (unchanged) |
| S81 | 2 | Contents. It now has six sections (B1–B6) in a two-column grid (`.fo4-toc`); one column of six overlapped the brand footer. |
| S01–S90 (r1 backup) | 3–46 | unchanged content. B5 is pp. 43–46. |
| S95 | 47 | **new** divider: "B6 · More on Hidden Transfer". Optional: further outcomes and unsettled literature. The note describes the four entries. |
| S91 | 48 | **new.** The full Cloud Fig. 3a (moved from main S70), with separate keys and a plain-language TruthfulQA explanation. The note takes over the r1 S70 note and adds the TruthfulQA reference (Lin, Hilton & Evans, Cloud ref. 49). |
| S92 | 49 | **new.** van der Weijden et al. Fig. 2a, animal row only (moved from the r1 S72b catalogue). Asset `p4-vdw-fig2a-animal.png`. |
| S93 | 50 | **new.** Yanagisawa et al. Fig. 1, wolf panel only (moved from the r1 S72b catalogue and the S75b "Fix study" bullet). Covers the number/math settings, small open models, French style, and "harmful traits: authors could not induce them" (Limitations). Asset `p4-yan-fig1-wolf.png`. |
| S94 | 51 | **new.** Nief et al. 2606.00831v2: the categorical headline set against the authors' revision notice, paraphrased. The Comments field was checked on 2026-11-27. "Not settled" in both directions. The note gives no date for the notice. |
| S86 | 52 | end (moved from 47) |

New assets are recorded in `figs/lec14-focused-overview/p4-PROVENANCE.md` and `p2a-PROVENANCE.md`.

**Moved from main to backup this round:**
- the full Fig. 3a panel (S70 → S91)
- the three-preprint catalogue (S72b → S92, S93, S94)
- the "Fix study" remedy bullet (S75b → S93)

The main slide IDs and order are unchanged from r1.

## Sources checked this round

- Cloud et al., Nature 652 (2026): Fig. 3a, main text, Methods (coherence and alignment thresholds; TruthfulQA ref. 49).
- Askin et al. v2: §4.2, Fig. 5, Fig. 25, App. E.3, Table 10 (epochs).
- van der Weijden et al. 2609.12586v1: §4.2, Fig. 2a.
- Yanagisawa et al. 2609.22215v1: §4.1, Fig. 1, Limitations.
- Nief et al. 2606.00831v2: abstract and Comments.
- Ge-Wang, Crosse et al. 2606.06529v1, eq. 1, and Greenblatt et al.: S78 and S45 denominators.

No fact was changed from memory.

## Checks

- `lint-deck.py`: main OK. On the backup, the only warning is the hardcoded-color warning, which r1 already had.
- `find-wordy.py` / `find-dense.py`: review prompts only. The S92 key line has 16 words, a plot-key exception under §1; it renders on one line.
- Overflow probe: clean on both decks.
- `outline-lint.py`: 0 stale pointers.
- Render check (`-r 60`) of the changed slides and their neighbours:
  - Main pages 15, 29, 30, 31, 33, 38, 40, 44, 50, 55, 56.
  - Backup pages 2 and 46–52.
  - S92 and S93 were also rendered at `-r 150`. The labels are readable. S92's model column labels are small in the source image, but the slide text names the models.
  - Per the handoff, I did not do a second full pass over the unchanged deck.
- `courses/trustworthy-ai/OUTLINE.md` is updated:
  - main pointers from p30 onward
  - backup B1–B6 and the 52-page counts
  - plan-v4 noted as amending plan-v3
  - S70 asset
