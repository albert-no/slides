# work-r1 — 2026-11-27-lec14-focused-overview

- **Branch:** `2026-11-27-lec14-focused-overview`, from baseline `7d9f51e`.
- **ID-only commit:** none. The baseline deck already carries `data-slide-id` S01–S56.
- **Head:** the commit named in the pointer. It holds the decks, the notes, the new backup pair, the `lec14tech.html` title change, the new assets, both OUTLINE files, this file and unchanged copies of `job.md`, `plan-v1.md`, `plan-v2.md`, `plan-v3.md`, `requests.md` and `evidence.md`.
- **Scope:** plan-v3. The main deck has **59 slides** (`1 / 59`) and the note has 59 articles, timed at 85 + 5 = 90 min. The new backup deck `backup-lec14-agentic-threats.html` has **47 slides** (`1 / 47`) and its note has 47 articles. In both decks the ID order matches the plan-v3 tables exactly; I checked this with a script against the plan tables.

## Packages

| Package | Main pages · IDs | Time | Result |
|---|---|---|---|
| P0 (me) | p1–3, p57–59 · S01, S02, S04, S46, S50, S51 | 5 + 5 | New title "When AI Learns and Acts", subtitle "Delegation, hidden behaviors and checks". Contents lists the three sections. S04 is a teaching map of the three questions. S50 "Actions" row note names Lecture 13 and sections 01 and 03. S04 note has "Earlier in the course" (lec01 p32, p38–40; lec07 p4–5; lec13 p4, p14–15). |
| P1 | p4–15 · S03 … S59 | 20 | S05a "A Shop Decision Changes the World"; S05b "Authorized Actions Can Still Be Mistakes"; S57a/S57b Vend shop and architecture (Fig. 2); S52a/S52b pricing; S53a/S53b Phase two; S58a "Approval Needs Commercial Evidence"; S58b "A Spending Cap Does Not Fix Pricing"; S59 "Test an Unprofitable-Order Scenario". S13's 1.5 min went +0.5 each to S52b, S53a and S58a. |
| P2a | p16–33 · S60 … S72b | 26 | Cloud et al. owl and misalignment transfer, taught step by step (S61a–S72b). S63a carries the one-line fine-tuning recall; S66b shows the weight-update steps; S71 makes the single training-time vs run-time contrast. S67a 2 min, S69b 2.25, S72a 1.75. |
| P2b | p34–40 · S73a … S75b | 9 | On-policy distillation in three steps (S73a–c); S73b: "Score = the teacher's own probability of writing that token." Askin bars S74a (Table 1) and S74b (Table 10). S75a reworked to teacher origin → channel → off-task learner test; S75b "Evidence so far / Still to test after a fix". |
| P3 | p41–56 · S35 … S45 | 20 | S36a "Check the Workflow, Not the Worker's Intentions"; S76 "The Backdoor Is in the Submitted Code"; one step per monitoring page (S39a, S39b, S40, S77); S43b 1.5 min and S78 1.75 min with new note sections (what the abort analysis does and does not simulate; why the score is conditional); S45 "Two Studies, Two Safety Questions" (qualitative, audit budgets 2% vs 1%). |
| P4 | backup p1–47 | 0 | Built from baseline slides plus the four v3 recall cards. 29 slides are byte-identical to the baseline (checked by script); S07, S16, S24 are rebuilt dividers and S13 is retitled. New: S80 title, S81 contents, S82 and S85 dividers, S86 end, S87–S90. |

I ran one subagent per package (P1, P2a + P2b, P3, P4) in the scratch area, each with its own class prefix (fo1-, fo2a-, fo2b-, fo3-, fo4-), and did P0 myself. I assembled the decks, notes, pacing table, backup build, OUTLINE and `lec14tech.html` change myself, and checked every package's output against the plan and the files (IDs, order, minutes, renders). A separate subagent did a read-only render audit; I reviewed its findings and re-read the pages I changed.

## Slide mapping

`slide ID | old page | new page | split or moved`. Old = baseline `7d9f51e` (51 slides). "B" = backup deck.

| ID | Old | New | Change |
|---|---|---|---|
| S01 | 1 | 1 | retitled |
| S02 | 2 | 2 | new contents |
| S03 | 3 | 4 | divider "Delegating Real Work" |
| S04 | 4 | 3 | rewritten (teaching map) |
| S52 | 5 | 9, 10 | split S52a/S52b |
| S53 | 6 | 11, 12 | split S53a/S53b |
| S05 | 7 | 5, 6 | split S05a/S05b, rewritten |
| S06 | 8 | B4 | moved |
| S07 | 9 | B3 | moved, divider B1 rebuilt |
| S08 | 10 | B5 | moved |
| S09–S12 | 11–14 | B7–B10 | moved |
| S13 | 15 | B12 | moved (v3), retitled "Recall: Capability and Delegation" |
| S54a, S54b | 16, 17 | B13, B14 | moved |
| S14, S15 | 18, 19 | B15, B16 | moved |
| S16 | 20 | B17 | moved, divider B2 rebuilt |
| S17–S23 | 21–27 | B20–B26 | moved |
| S24 | 28 | B27 | moved, divider B3 rebuilt |
| S25, S27, S28, S29, S31, S33, S34 | 29–35 | B28–B34 | moved |
| S35 | 36 | 41 | divider "Checking Untrusted Work" |
| S36 | 37 | 42, 43 | split S36a/S36b |
| S37 | 38 | 45, 46 | split S37a/S37b |
| S38 | 39 | 47, 48 | split S38a/S38b |
| S39 | 40 | 49, 50 | split S39a/S39b |
| S40 | 41 | 51 | redrawn (new generator); baseline version kept in backup as S89 (B39) |
| S41, S42 | 42, 43 | B40, B41 | moved |
| S43 | 44 | 53, 54 | split S43a/S43b |
| S45 | 45 | 56 | rewritten |
| S46 | 46 | 57 | closing divider |
| S49, S55, S56 | 47–49 | B44–B46 | moved |
| S50 | 50 | 58 | note row updated |
| S51 | 51 | 59 | unchanged closer |

New main IDs: S57a/b (p7–8), S58a/b (p13–14), S59 (p15), S60 (p16), S61a/b, S63a/b, S64, S65, S66a/b, S67a/b, S68, S69a/b, S70, S71, S72a/b (p17–33), S73a/b/c, S74a/b, S75a/b (p34–40), S76 (p44), S77 (p52), S78 (p55). New backup IDs: S80, S81, S82, S83, S84, S85, S86, S87, S88, S89, S90, and the recall cards S62a, S62b (B18–19) and S79 (B42).

**v2 → v3 moves:** S13 → B12 (after S88); S62a, S62b → B18, B19 (after S16); S79 → B42 (after S42). Their notes carry "Optional recall card, moved from the core lecture in its focused revision" and a backup pace line.

**Block timing (from the pace lines):** Opening p1–3 5 · 01 p4–15 20 · 02 p16–40 35 · 03 p41–56 20 · Closing p57–59 5 · flexible 5 = 90. The note head table is generated from the pace lines.

## C11 novelty and reuse

Earlier pages are from E21. The package workers did not re-open the earlier decks, and neither did I.

| ID | Earlier coverage (E21) | Disposition |
|---|---|---|
| S04 | lec01 p32, p38–40; lec07 p4–5; lec13 p4, p14–15 | Forward roadmap of today's three questions, not a recap; S50 is the single course summary |
| S05a | lec13 p4, p15 | Short self-contained recall plus a new shop consequence |
| S05b | lec13 p14–15 | New distinction: authorized vs commercially sound |
| S57a–S53b | none (Vend not taught earlier) | New |
| S58a, S58b | lec13 p58–60 | New inference specific to the shop case |
| S59 | lec13 p62–64 (see plan issue 1) | New test specific to the shop case |
| S60, S61a | lec02 p61; lec10 p81 | New contribution |
| S61b | none | New |
| S63a | lec10 p28–30; lec05 p8; lec07 p46–55 (MacDiarmid, not the Betley experiment) | Short recall plus new |
| S63b, S64–S70, S72a, S72b | none | New |
| S71 | lec13 p4; lec09 p14; lec08 p29–36 (analogy only) | New, with a one-line contrast |
| S73a–c | lec10 p81 (verdict labels vs token probabilities) | New |
| S74a | none | New |
| S74b, S75b | lec05 p48 (run-time output filtering, a different layer) | New |
| S75a | none | New |
| S35, S36b, S39a, S39b, S40 | none | New |
| S36a | lec07 p4–5, p68, p71–72; lec10 p80–85 | Short recall plus new (workflow test) |
| S76 | lec09 p14, p34, p73–75 | New: backdoor in the output program, kept distinct from a trained-in trigger |
| S37a, S37b | lec10 p80–85; lec13 p52–60 | New; the note says they are not equivalent |
| S38a, S38b | lec03 p51, p67 | New (whole-run safety score) |
| S77 | lec13 p54, p58–60 | New (this experiment's stop rule only) |
| S43a, S43b, S78 | lec08 p61 | New (attacker choices shape which attacks are measured) |
| S45 | lec01 p38–40; lec03 p51, p67 | New contribution (how to read the two scores) |
| S50 | all lectures | Course summary, once |
| S13 | lec01 p38–40; lec07 p5 | Moved to backup |
| S62a | lec10 p47; lec13 p4, p14–15 | Moved to backup |
| S62b | lec05 p8; lec10 p28–30 | Moved to backup |
| S79 | lec13 p54, p58–60 | Moved to backup |

**Within lec14:**
- S13 vs S88: kept distinct, both in backup.
- S79 vs S77: resolved by moving S79.
- S36a vs S37a: aim and test vs roles.
- S39a/b vs S37a/b: work flow vs roles.
- The runtime-vs-training contrast appears once in main (S71); its recalls S62a and S62b are only in backup.
- S04 roadmap vs S50 summary: S04 asks the three questions before the stories, and S50 maps the whole course after them.

Cross-lecture pointers are only in the notes, under "Earlier in the course". The main slides contain no "lecNN", "last week" or "as we saw" wording; I checked this with a text search. The slides keep their own short recall lines (S05a, S36a, S63a), which explain the idea on the slide.

## Deviations from the plan

- **Backup section numbers:** sections are B1–B5 (Measuring Autonomy, Against the Overseer, Many Agents, More Control Protocols, Further Frontiers), not the baseline numbers, so they do not collide with the main 01–03.
- **S05b:** its lead line ("One price change, two separate questions.") is removed, because the muted line collided with the cite. The point is in the script.
- **S36a:** the muted line is dropped for overflow; "Check what it submits." is folded into the Control line. No type was shrunk.
- **S65:** the owl system prompt is quoted in part on the slide (the cite says "quoted in part"); the full prompt is in the note.
- **S63b:** a schematic of Betley Fig. 1 questions and answers (abbreviated, labelled), not a crop.
- **S61a, S66a, S69a (render fix):** crop leftovers from neighbouring Cloud Fig. 2 parts are hidden with a CSS `clip-path` on the `<img>`; the PNG files are unchanged. This is recorded in `p2a-PROVENANCE.md`, and the S69a cite now says "fragment of the next label masked".
- **S57b:** a 14 px top margin on the "Point:" line, which was touching the figure.
- **"Student":** it appears only as the Nature figure label, written as "(figure: “Student”)" on S61a and S66b. Every other slide says teacher/learner.
- **`lec14tech.html`:** only the `<title>`, h1 ("When AI Learns and Acts: The Formal Pieces") and subtitle changed; content and page numbering are unchanged.

## Plan issues (for slides-review)

1. **lec13 range for S59:** plan item 6 cites lec13 p62–64; P1 reports E21 lists p63–64 for limits and synthesis, and baseline p62 is S50 "Six Checks, Run on the Email Example". The S59 note cites p62–64. Please confirm the range.
2. **S74a has no before-training bar.** Askin Table 1 has no before-training row for the learner. The teacher's 50.6% was not added, because it is a different model. Decide whether a baseline is required.
3. **S75b** is a two-card comparison with no figure. I judged that the cards are the visual. If a figure is required, that needs a source choice.

## Unsourced or weakly sourced facts (flagged, not fixed)

- **S53a note:** phase one and phase two report net worth differently. Carried over; not resolved from memory.
- **S58a note:** the sources do not say what purchase reviewers saw. The note says so.
- **Cloud misalignment judge (section 02):** the judge model is not named. Carried flag from P2a; the Askin judge (Gemini-2.5-Flash) is named on its slide.
- **E09 caveat:** sourced only to `evidence.md`.
- **Section 02:** "about 10%" in the text against a ~0.08 bar in the figure (carried P2a flag). Needs a primary-source check.
- **Dates:** the Betley and Cloud publication dates, and the E08/E09 venues, come from arXiv metadata only.
- **Terekhov et al. (backup only):** checked against its abstract only.
- **E21 pages:** the earlier-lecture page numbers were not re-opened against the earlier decks.
- **P3:** one unsourced claim (lec10/lec13 "adaptive attackers") was removed from the S43a note.

## Checks

- **`lint-deck.py`:** ok on the main deck, the main note, the backup note and `lec14tech.html`. The backup deck has 1 warning: 5 hardcoded inline colours, carried over unchanged (the baseline deck gives the same warning).
- **`find-wordy.py`:**
  - Main L422 (S53b qualifier, 16 words): kept as a §1 qualifier, renders on one line.
  - Backup L459 and L684: baseline text, unchanged.
- **`find-dense.py`:** review prompts only. The flagged slides render cleanly, and most of their counts are SVG labels.
- **`outline-lint.py`:** 0 stale pointers. The 8 warnings are pre-existing, outside this job.
- **Probe (1280×720):** clean on both decks and both notes, apart from the known brand-footer artifact.
- **Counts:**
  - Main: 59 `.slide`, `1 / 59`, 59 articles. The note ID order equals the deck's; 59 pace lines recompute to 85.
  - Backup: 47 `.slide`, `1 / 47`, 47 articles.
  - Baseline IDs: none retired. Every baseline ID lands in main or backup (table above).
- **Render (`-r 60`):**
  - All 59 main pages and backup pages 1, 2, 3, 12, 17, 18, 19, 42, 43 and 47 (new or changed slides) were read.
  - Main pages 3, 6, 11, 15, 42 and 53 were checked at 150 dpi where a gap was in question. Nothing touches.
  - After fixes I re-read main pages 8, 17, 23 and 28, and `lec14tech.html` page 1.
- **Notes:** a 485 px screenshot of the main note is clean (title, pacing table, first entries). Both notes probe clean.

## Files

- `courses/trustworthy-ai/lec14-agentic-threats.html` and `-note.html`: rebuilt.
- `courses/trustworthy-ai/backup-lec14-agentic-threats.html` and `-note.html`: new.
- `courses/trustworthy-ai/lec14tech.html`: title framing only.
- `courses/trustworthy-ai/figs/lec14-focused-overview/`: new assets.
  - P1: 1 PNG (Vend Fig. 2).
  - P2a: 9 PNG crops from Cloud and Betley (Nature).
  - P2b: generator `p2b-askin-bars.py`.
  - P3: 2 Ge-Wang crops and generator `p3-control-bars.py`.
  - Each package has its own `pN-PROVENANCE.md`.
  - No existing asset was modified.
- `courses/trustworthy-ai/OUTLINE.md`: lecture row, ID description, lec14 section rewritten, new backup row and `## backup-lec14-agentic-threats.html` section.
- Root `OUTLINE.md`: Wk 14 name, 8 backups.
