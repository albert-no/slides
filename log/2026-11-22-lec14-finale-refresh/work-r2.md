# work-r2 — job 2026-11-22-lec14-finale-refresh

## Branch and commits

- Branch `2026-11-22-lec14-finale-refresh`. review-r1 copied, job.md and evidence.md refreshed: `e732675`.
- All F01–F09 fixes: `1f9f8c3`. This report: the commit named in the pointer.
- Counts unchanged: main 51 slides (`1 / 51`), note 51 entries, tech 14 slides (untouched).

## Dispositions

| Finding | Disposition |
|---|---|
| F01 (blocking) | Fixed. S45 boxes now read "Tested here" (these tasks and run lengths / this attack policy / this audit budget) and "Re-test when these change" (task length / how attacks are selected / attacks aimed at the monitor). Muted line: "Each evaluation has its own envelope; outside it, a result neither guarantees nor rules out safety." S45 note (Message, Reading, Script) matches and says that Ge-Wang tests attack selection. The S43 note bridge uses your wording: task-level start and turn-level stop decisions in multistep agent environments; earlier code-backdoor attacks already sought favourable opportunities. |
| F02 (blocking) | Fixed. Essential explanations now 25 SVG units at scale 1 (body 24.8 px). S04: the three box explanations and "check, don't trust"; the control box widened (x 812, width 264) to hold it. S12: the three definitions. S29: "hidden instruction", "has tools" and the "read" arrow label at 25. The top label is now "arrives as a teammate's message", as you suggested. Boxes re-laid (outside page 250 wide, agents A and B 170, C 275) so nothing collides. The colour key line stays at 21 as secondary annotation. The note Message and the SVG aria-label match the new wording. S33: "sees harmless text" and the shared-convention line at 25. The example is shortened to "e.g. a weather remark" so it fits at 25. Rendered p4, p14, p32, p34 at `-r 60`; p32 also at `-r 150`. |
| F03 (blocking) | Fixed. Both note tables (S41 Table 7 / Table 2; S43 Table 2) are now stacked labelled lists. Every value, the n, the 95% CIs and the † marker are kept. Checked against the removed rows. At a 430 px iframe: `scrollWidth` 415 = `clientWidth` 415. No element extends past the right edge except KaTeX's visually hidden MathML. |
| F04 (blocking) | Fixed. The S42 cite ends "no U: H then T (1.0, 0.02)". The note explains that H writes the first 2% and T the rest, that T alone is normalised to zero, and cites Greenblatt §3.1.1 and Table 2. |
| F05 (blocking) | Fixed. S33 muted line: "Limited success in these tests of models up to GPT-4." S33 cite: "NeurIPS 2024 (arXiv 2402.07510v5, revised 2025)". S34 cite: "Motwani et al. (NeurIPS 2024)". Note Message, Script, does-not-establish, sources and the OUTLINE key-citation entry all match. |
| F06 (blocking) | Fixed without repainting. The source crop now ends at row 1422, so "+40%" is whole. On the source, the tick label's last three rows (1420–1422) share rows with the tops of the category labels, which start at x = 424. So columns 0–399 run to row 1422 and columns 400–2561 to row 1419, with the remaining 3 rows left white (the source background there is RGB 255). No source pixel is altered; the label tops are omitted, as the labels are. The output is 1200×521. The HTML category labels are unchanged; the 1 px height change does not move them (render checked, p16). p1-PROVENANCE: crop box updated, "Known clip" line removed. S54a note figure line: "all tick labels are whole". |
| F07 (blocking) | Fixed. `p1-gen-curves.py` uses the slide's mapping `Y = 295 − 255p` (docstring updated). The S06 path is replaced with the script's exact output. The old path differed at two points (`L131.0,64.9`, `L462.5,176.9`). p1-PROVENANCE S06 line updated. |
| F08 (blocking) | Fixed. S21 key: "Controls: CSQA, commonsense questions; MMLU, broad knowledge" and "Target: WMDP, hazardous-knowledge proxy" replace the old one-line key. Full names in the S21 note: CommonsenseQA and Massive Multi-Task Language Understanding, both verified in van der Weij §3. The note keeps the full-MMLU versus biology-subset distinction. S27 question line: "MAST (Multi-Agent System Failure Taxonomy): why do agent teams fail?" MAST is expanded at its first note mention (S25) and in the S27 Message and Script, with the gloss "a map of team failures". |
| F09 (optional) | Taken. S52 note paragraph replaced with your sentence. S27 note: "that range is kept in the note for slide 31, S28". |

## Checks

- `lint-deck.py`: deck shows only the 5 baseline inline-colour warnings (S14 swatches); note ok.
- `outline-lint.py`: 0 stale pointers. Deck pointers after line 618 moved +1 for the extra S21 key line. All 51 slide pointers and 16 figure pointers checked against the file and each lands on its slide or `<img>`. Only the lec14 leaf points into the lec14 deck.
- Render at `-r 60` after all edits, 51 pages. Read: p4, p8, p14, p16, p25, p30, p32, p34, p35, p43, p45; p32 also at `-r 150`. No overflow, overlap or clipped labels.
- Note at 430 px: as F03.

## Flags

None new. The worktrees `slides-wt/lec14-p1..p4` and branches `lec14r-p1..p4` remain until approval, then I remove them.
