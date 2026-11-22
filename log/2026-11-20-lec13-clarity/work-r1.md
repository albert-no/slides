# work-r1 — job 2026-11-20-lec13-clarity

## Branch and commits

- Branch `2026-11-20-lec13-clarity`, from baseline `9effc8a`. No ID-only commit: the baseline already carried S01–S53.
- Last content commit: `800151b`. This report and the refreshed living files are in the commit named in the pointer.
- Package commits, merged into the branch: P1 `28a5618`, P2 `351da7f`, P3 `c99a8fd`, P4 `f43da70`, P5 `f25a12b`, P6 `bb77e91`. Integrator shared surfaces: `9b8d42f`. Renumbering, pacing, note cross-references and OUTLINE: `800151b`.
- Counts: main 65 slides, note 65 entries, tech 15 slides (unchanged except one terminology line).

## Per package

- **P1 (S04–S09).**
  - S04 opens on agents reading text from many authors.
  - The running email example replaces BANANA as the opener (S05a/S05b). BANANA's content moved to the note.
  - S06 defines the two attacks by goal.
  - The direct/indirect split (S07a/S07b) uses a crop of Greshake Fig. 3 with an enlarged key.
  - S08 answers "why priority matters".
  - S09a covers the hidden-text paper injection; S09b covers ICML's use of the same trick to flag AI reviews.
- **P2 (S11–S18).**
  - Agent permissions and the agent loop are now on the running example.
  - S13 carries a worked trace.
  - S14 uses a re-crop of InjecAgent Fig. 1 with a key.
  - S16 now states its message: notes may choose a file, not a recipient.
  - Diagrams are re-laid at the label floors.
- **P3 (S20–S27).**
  - S20 explains how to read a report and defines provider (= vendor).
  - EchoLeak is split into the event (S21a) and its status (S21b).
  - S23 answers the C10 question: it is the same user's public and private repos.
  - S22, S24 and S26 diagrams are enlarged.
- **P4 (S29–S32).**
  - S29 states that priority means instruction authority, not search ranking. Its diagram is enlarged.
  - S31 is split. S31a covers what escaping and delimiters do. S31b covers why marked text can still give orders: marking is not enough.
- **P5 (S34–S41, new S54–S56).**
  - S54 explains repeat prompt and prompt sandwiching before the numbers.
  - The S40 table becomes bar charts S40a (reminders) and S40b (detector and tool filter).
  - New S55 (Prompt Guard) and S56 (MELON) explain the mechanisms before S41.
  - The S41 table becomes a fixed vs search bar chart.
- **P6 (S42–S48).**
  - S44 is split. S44a covers capabilities on the Bob example; S44b covers the policy check on proposed sends.
  - The S45 table becomes bar charts.
  - S47 is split into S47a (dual LLM), S47b (tool filter and least privilege) and S47c (detection vs approval).
  - S48 answers C19 on the slide: proceed / deny / ask only for consequential unresolved exceptions, with the system-filled approval dialog.
  - Tech slide 10 reads "Sees $p$ and the tool signatures $T$".
- **Integrator.**
  - Contents and section dividers.
  - S50: six checks run on the email example.
  - S51: open problems as usefulness vs enforceable limit.
  - S52: takeaways.
  - The `1 / 65` total.
  - Comments renumbered 1–65, and note `<h2>` numbers 1–65.
  - Pace and elapsed lines, and the pacing table.
  - Note cross-references converted from IDs to page numbers.
  - OUTLINE: lec13 row, ID note, leaf section table, figures, note pointers.
  - Terminology reconciled across packages:
    - the running email and Bob examples;
    - provider;
    - priority vs permission check;
    - "Detector" (AgentDojo's DeBERTa) vs "Prompt Guard" (Nasr Table 7).

## Coverage (Albert's pages refer to the baseline: page N = S N)

| ID | Where now (pages) | Answer on the slide |
|---|---|---|
| C00 | whole deck | Every diagram touched was relaid at ≥25 px primary / ≥20 px secondary labels. Questions are answered on the slides and expanded in the notes. |
| C01 | S04 (4) | Agents read text from many authors. |
| C02 | S05a, S05b (5–6) | Running email example; it recurs in S13, S50 and elsewhere. |
| C03 | S07a, S07b (8–9) | Direct = the request itself attacks the app rules; indirect = the attack arrives as data (the email). |
| C04 | S08 (10) | Which instruction should win when they conflict, and why that matters. |
| C05 | S09a, S09b (11–12) | Hidden text in papers; ICML used hidden text to flag AI reviews. |
| C06 | S16 (19) | Title states the message. |
| C07 | S20 (23) | How to read the status ladder; provider = the company operating the product. |
| C08 | S22 (26) | Larger diagram labels. |
| C09 | S21a, S21b (24–25) | What happened, then what Microsoft reported. |
| C10 | S23 (27) | Yes, the same user's public issue reached their private repos. |
| C11 | S24 (28) | Larger labels. |
| C12 | S26 (30) | Larger labels. |
| C13 | S29 (33) | Priority = whose instruction wins (instruction authority, not search ranking); larger labels. |
| C14 | S31a, S31b (35–36) | Escaping keeps text as text; marked text can still give orders: marking is not enough. |
| C15 | S54 (45), S40a (46) | Repeat prompt explained before the numbers. |
| C16 | S54, S55, S56 (45, 48, 49) | Prompt sandwiching, Prompt Guard and MELON each explained before S41 (50). |
| C17 | S44a, S44b (53–54) | Larger labels; capability then policy check, two slides. |
| C18 | S47a, S47b, S47c (57–59) | Three slides. |
| C19 | S48 (60) | Do not ask always: proceed, deny, or ask only for consequential exceptions, with the facts filled in by the system. |

## Slide mapping

| slide ID | old page | new page | split or moved |
|---|---|---|---|
| S01 | 1 | 1 | same page |
| S02 | 2 | 2 | same page |
| S03 | 3 | 3 | same page |
| S04 | 4 | 4 | same page |
| S05a | 5 | 5 | split |
| S05b | 5 | 6 | split |
| S06 | 6 | 7 | moved (page shift) |
| S07a | 7 | 8 | split |
| S07b | 7 | 9 | split |
| S08 | 8 | 10 | moved (page shift) |
| S09a | 9 | 11 | split |
| S09b | 9 | 12 | split |
| S10 | 10 | 13 | moved (page shift) |
| S11 | 11 | 14 | moved (page shift) |
| S12 | 12 | 15 | moved (page shift) |
| S13 | 13 | 16 | moved (page shift) |
| S14 | 14 | 17 | moved (page shift) |
| S15 | 15 | 18 | moved (page shift) |
| S16 | 16 | 19 | moved (page shift) |
| S17 | 17 | 20 | moved (page shift) |
| S18 | 18 | 21 | moved (page shift) |
| S19 | 19 | 22 | moved (page shift) |
| S20 | 20 | 23 | moved (page shift) |
| S21a | 21 | 24 | split |
| S21b | 21 | 25 | split |
| S22 | 22 | 26 | moved (page shift) |
| S23 | 23 | 27 | moved (page shift) |
| S24 | 24 | 28 | moved (page shift) |
| S25 | 25 | 29 | moved (page shift) |
| S26 | 26 | 30 | moved (page shift) |
| S27 | 27 | 31 | moved (page shift) |
| S28 | 28 | 32 | moved (page shift) |
| S29 | 29 | 33 | moved (page shift) |
| S30 | 30 | 34 | moved (page shift) |
| S31a | 31 | 35 | split |
| S31b | 31 | 36 | split |
| S32 | 32 | 37 | moved (page shift) |
| S33 | 33 | 38 | moved (page shift) |
| S34 | 34 | 39 | moved (page shift) |
| S35 | 35 | 40 | moved (page shift) |
| S36 | 36 | 41 | moved (page shift) |
| S37 | 37 | 42 | moved (page shift) |
| S38 | 38 | 43 | moved (page shift) |
| S39 | 39 | 44 | moved (page shift) |
| S54 | — | 45 | new |
| S40a | 40 | 46 | split |
| S40b | 40 | 47 | split |
| S55 | — | 48 | new |
| S56 | — | 49 | new |
| S41 | 41 | 50 | moved (page shift) |
| S42 | 42 | 51 | moved (page shift) |
| S43 | 43 | 52 | moved (page shift) |
| S44a | 44 | 53 | split |
| S44b | 44 | 54 | split |
| S45 | 45 | 55 | moved (page shift) |
| S46 | 46 | 56 | moved (page shift) |
| S47a | 47 | 57 | split |
| S47b | 47 | 58 | split |
| S47c | 47 | 59 | split |
| S48 | 48 | 60 | moved (page shift) |
| S49 | 49 | 61 | moved (page shift) |
| S50 | 50 | 62 | moved (page shift) |
| S51 | 51 | 63 | moved (page shift) |
| S52 | 52 | 64 | moved (page shift) |
| S53 | 53 | 65 | moved (page shift) |

## Deviations from the plan

- P1: S06 title kept. S07b's orange badge colour comes from the source figure. Greshake's in-figure labels render at ~14 px inside the crop, so an enlarged key sits beside the figure.
- P2: S14's in-figure InjecAgent text renders at ~20 px. It is a crop, so the key carries the reading.
- P5: MELON (S56) is an illustrative diagram, not a crop. The labels are renamed "Detector" (AgentDojo, ProtectAI DeBERTa) and "Prompt Guard" (Nasr Table 7) so the two are not conflated.
- P6: the S48 dialog uses the meeting document from the Bob example, not the email plan.
- P6's S45 caveat originally read "no adaptive attack tested". It now reads "Nasr et al. did not attack it adaptively". S40a's caveat now reads "Fixed attack only here". The broader claim had no source.

## Plan issues (need slides-review's decision)

1. **Teaching time.**
   - Per-slide paces sum to 81.5 min. The note shows an 8.5 min "Questions and discussion" row to reach 90.
   - Section sums against plan budgets:

     | Section | Actual | Plan |
     |---|---|---|
     | Core | 11.75 | 14 |
     | Surface | 13.75 | 15 |
     | Incidents | 15.25 | 17 |
     | Why hard | 9.75 | 11 |
     | Defenses | 24.75 | 27 |
     | Synthesis | 6.25 | 6 |

   - Decide: keep the buffer row, or redistribute minutes.
2. **E05 date.** evidence.md gives the ICML blog post as 26 Mar 2026. The fetched page shows 18 Mar 2026, so the slide and note cite 18 Mar. Please confirm or add a correcting entry.
3. **Prompt Guard version.** The Prompt Guard version behind Nasr Table 7 is not stated in the sources we hold. The slides say "Prompt Guard" without a version.
4. **AgentDojo's detector** is ProtectAI's DeBERTa, not Prompt Guard. The plan wording that linked them was not followed (see Deviations).
5. **Illustrative caption on S54.** The line "The model reads 1, 2, 3 in this order…" is illustrative ordering, not a source quote. It is labelled illustrative.
6. **Dropped citation on S47c.** P6 dropped a Prompt Guard model-card citation that had no source in evidence.md. "Uninformed" and "rubber-stamped" are marked in the note as our summary, motivated by Invariant Labs 2025 and CaMeL §9.2.

## Unsourced facts

- No new facts without a source. The only date discrepancy is item 2 above.
- Approval-design content (S47c, S48) is labelled as our design recommendation.

## Checks

- **Lint.** `lint-deck.py` reports ok on the deck, the note and the tech file. `outline-lint.py` finds 0 stale pointers; its 5 warnings are in other folders.
- **find-wordy.** Flags three plot-key lines (deck L382, L1157, L1208). These are bounded key exceptions and render cleanly.
- **find-dense.** Flags about 33 slides. Its word counts include SVG diagram labels (the baseline had about 5 flags). Treat these as review prompts; the render was the check.
- **Render.** All 65 pages rendered at `-r 60` in headless Chromium and viewed. No overflow, clipped labels, detached or reversed arrows, or footer collisions.
- **Note.** Rendered at a 430 px viewport; the pacing table wraps with no horizontal overflow.
- **Chart values checked against the source tables:**
  - S40a/S40b, AgentDojo Table 5, GPT-4o, as clean utility / utility under attack / attack success:

    | Setting | CU | UA | ASR |
    |---|---|---|---|
    | None | 69.0 | 50.0 | 57.7 |
    | Delimiting | 72.7 | 55.6 | 41.7 |
    | Repeat | 85.5 | 67.3 | 27.8 |
    | Detector | 41.5 | 21.1 | 8.0 |
    | Tool filter | 73.1 | 56.3 | 6.8 |

  - S41, Nasr Table 7, Gemini-2.5 Pro, fixed/search attack success: 30/100, 28/99, 21/95, 26/94, 0/89.
  - S45, CaMeL: Table 2 clean utility 84.5, 77.3, 73.2, 41.2; Table 4 attacks 11 ± 4.5 → 0 and 163 ± 140.1 → 0.
  - The generator is `figs/lec13-clarity/p5-bars.py` (`s40a | s40b | s41`).
- **New assets:**
  - `figs/lec13-clarity/p1-greshake-fig3.png`: Greshake p. 3, `pdftoppm -r 250 -x 1225 -y 1080 -W 600 -H 605`.
  - `figs/lec13-clarity/p2-injecagent-fig1-crop.png`: InjecAgent p. 2, `pdftoppm -r 200 -x 190 -y 195 -W 1008 -H 392`.
  - `greshake-plant.png` and `injecagent-overview.png` are no longer used. They are kept, not deleted.
