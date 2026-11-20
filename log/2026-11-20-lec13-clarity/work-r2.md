# work-r2 — job 2026-11-20-lec13-clarity

## Branch and commits

- Branch `2026-11-20-lec13-clarity`. Round 1 head was `06678b4`; last content commit this round is `94602e3`. This report and the copied job files are in the commit named in the pointer.
- Round-2 commits:
  - `1eff815`: copies of plan-v2 and review-r1.
  - `6b16086`: F01, F02, F05–F09, plus labels on S13, S16, S30 and S31b.
  - `a777187`: F03 on S22, S24, S26, S29, S56 and S47a, and the S37/S39 keys.
  - `9ace198`, `109db60`, `bb14b6a`: F03 sweeps of the remaining diagrams.
  - Merges `41370a2` and `91af0bd`.
  - `d29432c`: integration fixes and the note buffer label.
  - `94602e3`: OUTLINE (F04).
- Counts are unchanged: main 65 slides, note 65 entries (same IDs and order), tech 15 slides.

## Slide mapping

No slide was added, removed, split or moved this round. Every ID keeps its round-1 page:

```
S01 1 · S02 2 · S03 3 · S04 4 · S05a 5 · S05b 6 · S06 7 · S07a 8 · S07b 9 · S08 10 · S09a 11 · S09b 12 ·
S10 13 · S11 14 · S12 15 · S13 16 · S14 17 · S15 18 · S16 19 · S17 20 · S18 21 · S19 22 · S20 23 ·
S21a 24 · S21b 25 · S22 26 · S23 27 · S24 28 · S25 29 · S26 30 · S27 31 · S28 32 · S29 33 · S30 34 ·
S31a 35 · S31b 36 · S32 37 · S33 38 · S34 39 · S35 40 · S36 41 · S37 42 · S38 43 · S39 44 · S54 45 ·
S40a 46 · S40b 47 · S55 48 · S56 49 · S41 50 · S42 51 · S43 52 · S44a 53 · S44b 54 · S45 55 · S46 56 ·
S47a 57 · S47b 58 · S47c 59 · S48 60 · S49 61 · S50 62 · S51 63 · S52 64 · S53 65
```

The exhibit changed on two slides:
- S43 (p52) now shows CaMeL Fig. 5.
- S37 (p42) and S39 (p44) now use new source crops.

## Findings

### F01 — CaMeL figure (S43 / p52)

- **Exhibit.** CaMeL **Fig. 5** (system architecture) replaces Fig. 1. The new title is "CaMeL Separates Planning, Parsing and Enforcement".
- **Crop.** `pdftoppm -png -r 250 -f 7 -l 7 -singlefile -x 204 -y 265 -W 1654 -H 808 camel.pdf`, arXiv 2503.18813v2, saved as `figs/lec13-clarity/r2-camel-fig5.png`. Crop only, caption removed. The cite says so.
- **Key.** A 4-item key in body-size text sits beside the figure:
  - the trusted request and configuration go to the P-LLM, which writes the program;
  - the interpreter runs it and checks each tool call against policy;
  - the Q-LLM parses untrusted data and has no tools;
  - runtime data can still affect arguments and branches.
- **Note.** The S43 Message, Reading and Script now describe Fig. 5. Fig. 1 is no longer used by lec13.
- **Deviation.** The figure's own internal labels render at about 11 px at 700 px width. The key carries every label the argument needs at body size, and the source figure stays readable as a picture. A larger crop would leave no room for the key, and splitting Fig. 5 into sequential crops would cut its arrows.

### F02 — Approval authorizes only a permitted exception (S44b / p54, S47c / p59, S48 / p60)

- **S47c highlight:** "A detector grants no authority. Approval may authorize a policy-permitted exception." Fallibility stays in the diagram and the note.
- **S48:** adds "Assumed: you may share this file, and policy allows the exception. Otherwise: deny." The routine / forbidden / consequential split and the system-record facts are kept.
- **S44b:** "The model cannot override a deny. Policy may let an authorized person grant an exception."
- **Note:**
  - The Message, Reading and Script for S44b, S47c and S48 now carry the same condition.
  - "Only you can make it" is removed.
  - The Invariant sentence now reads: repeated prompts *can encourage* blanket approval; Invariant reports users choosing "Always Allow"; this is an observation, not a controlled study.

### F03 — Essential diagram text at body size (deck-wide)

Every inline-SVG label was measured at final size in headless Chromium at 1280×720:

    rendered px = computed font-size × rendered SVG width ÷ viewBox width

**Result.** Every essential SVG label in the deck now renders at **≥ 25 px**. S17's Venn draws 460 → 520 px, so its labels render at 28 px.

**Slides changed.**
- Mechanism and flow diagrams:
  - S04, S05b, S07a, S08, S09a, S09b
  - S11, S12, S13, S15, S16, S17, S18
  - S21a, S22, S23, S24, S25, S26
  - S29, S30, S31b, S32
  - S54, S55, S56
  - S42, S44a, S44b, S47a, S47c
- Charts:
  - S41: legend.
  - S45: panel titles, bar names and group names.

**How labels were made to fit.** Boxes were made wider or taller, and lines were rewrapped. Uppercase role tags (S21a, S25) and the S23 account header became sentence-case 25 px headers. No type was shrunk.

**Secondary text left below 25 px**, all as allowed by F03:

| Slide | Text | Rendered size |
|---|---|---|
| S40a, S40b | "higher/lower = better" | 21 px |
| S40a, S40b | bar values | 23 px |
| S41 | bar values | 22 px |
| S45 | "higher/lower = better" and the 100% / 200 ticks | 20 px |
| S45 | bar values | 22 px |
| S47a | legend "red = untrusted text" | 22 px |

**Source-plot keys.**
- **S37 (p42).** New faithful crop of AgentDojo Fig. 6a: `pdftoppm -png -r 400 -f 7 -l 7 -x 605 -y 400 -W 875 -H 665 agentdojo.pdf`, saved as `figs/lec13-clarity/r2-agentdojo-fig6a.png`. An outside key at body size reads:
  - "✕ GPT-4o: 69% clean, 48% attack success"
  - "▲ Claude 3.5 Sonnet: 78% clean, 34% attack success"

  Both glyphs render.
- **S39 (p44).** New crop of Wallace Fig. 2's plot area: `pdftoppm -png -r 200 -f 7 -l 7 -x 290 -y 222 -W 1110 -H 302 wallace.pdf`, saved as `figs/lec13-clarity/r2-wallace-fig2-plot.png`. The x-axis evaluation names are outside the crop at 24.8 px. The in-plot bar values are about 18 px (secondary).

**Wording changes made to fit the larger type:**
- S37: dropped "50% under attack" and the "Several high-utility agents" bullet. Both are kept in the note.
- S39: the outside labels drop the repeated "Prompt Injection" prefix. The method line is merged.
- S56: "recorded, not executed" became "not executed".
- S30 and S31b: wording is under F09.

The note's "Reading the slide" for S37 and S39 is updated to match.

**Render checks.** Every changed slide and its neighbours were rendered at `-r 60` and read.

Two problems found in integration and fixed (`d29432c`):
- **S24:** the outer box borders were half-clipped at the figure edge.
- **S54:** the box-2 footer was crowded.

There is no overflow, clipping, detached arrow or footer collision on the final render.

### F04 — OUTLINE (`courses/trustworthy-ai/OUTLINE.md`)

- **Rebuilt from the baseline.** Started from the `9effc8a` file, so the duplicated lec12/lec13 sections and the misplaced lec11 text are gone.
- **Kept one lec13 section, updated:**
  - 65 slides, with section minutes from the note's pacing table;
  - final line pointers;
  - slide IDs, with the splits and S54–S56 order;
  - the 7 image files actually used, plus the bar-chart generator `p5-bars.py`;
  - figures no longer used, listed;
  - note entry pointers: entries 16, 31 and 50; Table 3 vs 5 flagged in entry 46; the E22 caveat in entries 39 and 46;
  - 31 distinct note sources;
  - tech at 15 slides;
  - a short record of the clarity revision.
- **Also updated:** the lecture index row (line 47) and the ID sentence (line 56).
- **Checks.** `git diff 9effc8a` touches only lines 47, 56 and the lec13 section. Exactly one `## lec13-prompt-injection.html` heading; no duplicate `## ` headings. `outline-lint.py` reports trustworthy-ai ok. The 5 warnings are pre-existing in infotheory/privacy.

### F05 — Authorized trace (S13 / p16)

- **Slide:** "Illustrative trace. Authorized path: 1 → 2 → 3 → 5; skip the send."
- **Note:** both path sentences now read step 1 → 2 → 3 → 5. They explain that step 3's inbox result is read and summarized, while its added instruction is not obeyed.

### F06 — Escaping (S31a / p35)

- **Slide:**
  - The example heading is now "Escaping (JSON string)".
  - The delimiter line is now "Encode marker characters as literal data; the model must still respect the boundary."
- **Note:**
  - A format-aware serializer and parser keep a syntactic boundary. Text markers shown to an LLM are not an enforced parse or authority boundary.
  - Markers the sender is "unlikely to guess" make faking harder; no compliance claim.
  - The parameterized-SQL contrast and S31b's inside-the-markers example are kept.

### F07 — Opening definition (S01 note)

The Message and Script now read: "Prompt injection tries to make lower-trust text override the instructions it should follow. We begin with indirect injection: an outsider's email steering the user's agent." The many-author motivation is kept.

### F08 — AgentDojo Table 5 aggregation

- **S40a cite:** "AgentDojo Table 5; GPT-4o; fixed attack; 629 security cases. Full values in the note."
- **Note:** S34 and S40a now carry the E22 caveat: clean utility as reported in Table 5; 97 distinct tasks; the aggregation behind the printed percentages is not fully specified.
- **Generator:** the `p5-bars.py` docstring is corrected the same way.
- **Unchanged:** all table values, and the CaMeL/Nasr denominators.

### F09 — Negative glyphs

Every ✗ and ✓ is gone (count 0 in the deck). They are replaced with words:

| Slide | New labels |
|---|---|
| S16 (p19) | "OK: you asked" / "OK: trusted source" / "OK if Bob may read it" / "Denied" |
| S30 (p34) | "Right: read it, report it" / "Wrong: obey it" |
| S31b (p36) | "Right … writes the summary" / "Wrong … also sends the plan" |
| S44b (p54) | "Yes" / "No" check columns |
| S47b (p58) | "Kept: read mail" / "Removed: send mail" |

All were checked on the final render. The note's S16 reading sentence is updated to match.

## Other changes

- The note's pacing row "Questions and discussion" is relabelled "Flexible explanation/question buffer" (8.5 min; total still 90), as review-r1 suggested.
- S13's code label now reads `send_email(plan, outside_addr)`, and the note was updated to match.

## Deviations from the plan

- **S43:** Fig. 5's internal labels stay at about 11 px; the outside key carries them (see F01).
- **Source crops:** in-figure text on S37/S39 is below body size; the outside keys carry what the slide discusses.
- **Wording trims:** on S37, S39 and S56, made to fit body-size labels. Removed content is kept in the note.

## Plan issues

None.

## Unsourced facts

None found. No fact, number or citation was changed except as specified in F01, F02, F06, F07 and F08.

## Checks

- `lint-deck.py`: ok for the main deck, the note and the tech supplement.
- `outline-lint.py`: trustworthy-ai ok.
- Main and note IDs match: 65/65, same order, unique.
- Note at 430 px: no horizontal overflow (W 415, scroll width 415).
- Font scan: computed rendered size for every SVG `<text>` on all 65 slides, with results as listed under F03.
- **Pages rendered** at `-r 60` (Chromium print, 1280×720):
  - 4, 6, 8, 10, 11, 12
  - 14, 15, 16, 18, 19, 20, 21
  - 24, 26, 27, 28, 29, 30
  - 33, 34, 35, 36, 37
  - 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55
  - 57, 58, 59, 60
