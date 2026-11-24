# work-r2 — 2026-11-23-opt01-opt03-four-hour-core

Round 2. This round answers `review-r1.md`. The plan is unchanged (`plan-v1.md`), and so are the argument, the scope and the timing: opt01 still has 68 slides for 150 minutes and opt03 has 51 slides for 90 minutes. No slide was added, removed, split or reordered, so the ID and page maps are the same as in work-r1.

## 1. Commits (after `19e8acf`)

- `3128143`: F02–F07, F09 and F10 in the decks, the HTML notes and OUTLINE, plus the F01 display breaks in the HTML notes.
- `71e1129`: opt03 HTML note S27. The word "instead" was left dangling after the Hessian sentence was removed; it is now deleted.
- `4a8184c` (opt01) and `f17c22d` (opt03): F08, the Markdown notes rewritten as standalone exposition. Each was done in its own worktree and merged in `7cc3dd9` and `1f1fbeb`.
- `fed1927`: the Markdown notes get `##` part headings (Opening, Part N: …, Closing, References) and two stale reference cross-references are fixed (§3, F08).
- The F10 note change (Mirsky extension moved to the backup pointer) is in the report commit.
- Review target: the SHA in the pointer message, which is the commit that adds this report and the refreshed job files.

## 2. Dispositions

All blocking findings are fixed, and the optional F10 is taken.

| Finding | Disposition |
|---|---|
| F01 | Fixed: the long displays are broken into short `aligned`/`gathered` steps with every step kept and the type size unchanged. The overflow-x rule stays only as a fallback, and no article needs it at 430 px (§4). |
| F02 | Fixed: the lower bound is restored in S01, S27 and S135 in both editions. S01 also names the attained minimum. S98's "Smoothness alone gives the one-step decrease" is unchanged because it is correct. |
| F03 | Fixed: deck S73 now reads $\|A\|_F^2$ as total energy. Notes S72 Message: "The squared Frobenius norm adds up every squared entry". Notes S73: energy is $\|A\|_F^2$ and the norm is its square root. |
| F04 | Fixed: deck S28 reads "$\ell_2$ gives Euclidean length" and keeps the (1,1) contrast. Notes S28: "$\ell_2$ is Euclidean (straight-line) length; all three are norms." Notes S27: "Squared Euclidean and Frobenius norms are still useful as objectives: they are smooth, and squaring a nonnegative quantity does not move its minimizers". |
| F05 | Fixed: "for $\sigma_i>0$" is added to deck S38 and notes S38. Notes S42: the factors have orthonormal columns but need not be square orthogonal matrices. Notes S81: the rank argument now goes through $A_kv_i=\sigma_iu_i$ and the span. Notes S123: the unweighted EYM guarantee does not apply, and truncating the SVD is not generally guaranteed. |
| F06 | Fixed: (1) The infinity-norm citation is now Boyd & Vandenberghe App. A.1.3 p.635 (E10), in the deck S28 cite and in both notes. (2) The Proposition 7.4 block and its "not independently sourced" sentence are removed from S91; the diag(2,1) spectral counterexample stays. (3) The smallest-L/Hessian sentence is removed from S27, and the direct L = 4 check is kept. (4) The S80 problem setup now cites Cornell CS4787/5777 Lecture 5 (E06). |
| F07 | Fixed: the S140 flow boxes and outcome boxes are at body size (1.55rem, the size of `p`), through a scoped `.o3b-flow .diagram-box` rule. The $\mu/2$ fraction is displayed. The three-row table is unchanged. Render in §4. |
| F08 | Fixed: both Markdown notes are rewritten as student-facing exposition. Details in §3. |
| F09 | Fixed: `courses/deepmath/OUTLINE.md` rows 10 and 12 now list only the core topics. Deferred topics appear only in the full-edition descriptions. |
| F10 | Taken, both parts. Deck S101 now reads "Proved in the note, using min–max (Weyl) inequalities". In both editions of the S101 note, the nuclear-norm case, "Theorem 8M (Mirsky, 1960)" and the "simultaneously optimal" paragraph are replaced by one sentence: the argument extends to the nuclear norm and, by Mirsky [2], to every unitarily invariant norm, and those extensions are kept in the full-edition note, which still contains them unchanged. |

## 3. Changed slides and articles

- **opt01 deck:** S28 (p12), S38 (p21), S73 (p39), S101 (p60).
- **opt01 HTML note:**
  - S27, S28, S38, S42, S72, S73, S81, S82, S83, S90, S91, S101, S102, S123;
  - reference list items 13 and 16, whose cross-references pointed to "Section 8.3" and "Section 7.4", sections that no longer exist. Item 13 now points to §8.3 of the full-edition note, and item 16 to article 60.
- **opt03 deck:** S140 (p50). The CSS lives in the deck `<style>`.
- **opt03 HTML note:** S01, S27, S80, S105, S106, S123, S135, S138.
- **Markdown notes (F08):** all sections of both notes (68 and 51) are rewritten.
  - **Removed:** narration about slides, cards, boxes, muted lines and highlights, and presenter instructions. Recaps and tables are linearized into bullets with a legend line. "Slide N" cross-references now read "section N, Title".
  - **Kept:** IDs, BEGIN/END markers, REGION comments, order, and every statement, proof, value and source.
  - **Added:** `##` part headings, which fix `lint-accessible-md.py`'s h1→h3 error. That error was already there in r1.
  - **S89 and S99:** the opt01 worker replaced descriptions of rows with the inequality chains themselves, one step per line, with a justification label on each step. I checked those labels against the HTML proof.
- **OUTLINE:** `courses/deepmath/OUTLINE.md` rows 10 and 12.

## 4. Checks

- `lint-deck.py`: ok on both decks. `outline-lint.py`: 0 stale pointers. The 5 warnings are in other courses and were there before.
- **`lint-accessible-md.py`:** 0 errors on both MDs. The one warning per file is the front matter naming the companion deck, which is a factual mention.
- **MD:**
  - Non-ASCII grep: empty.
  - Heading and marker lists are identical to `3128143` (checked with diff).
  - Independent math check: every HTML math span is in the MD after normalising `\gt`/`\le`/`\tfrac`. opt03: 0 missing out of 486. opt01: 4 out of 715 differ only in spelling (`^\top` vs `^{\top}`, `\cdots` spacing) and are present in substance.
  - Every URL in the HTML is also in the MD.
- **F01 width test:**
  - **Method:** headless Chromium with `html{width:430px}`. For every `.katex-display`, `pre` and `table`, compare `scrollWidth` with `clientWidth`.
  - **Before:** overflow in S82, S83, S90, S101, S102 (opt01) and S105, S106, S138 (opt03).
  - **After:** no overflowing element in either note at 430 px or at desktop width (1000 px). No `katex-error` nodes.
  - S123 (opt03) did not overflow at 430 px, but it is broken into two steps anyway, as the review asked.
- **Renders** (chromium, `-r 60`):
  - opt01 p12, p21, p39 and p60 fit, with no overlap. The S28 cite is two lines.
  - opt03 p50: the five flow labels are at table size, everything fits at 1280×720, and there is room below the muted line.

## 5. Notes for review

- I added no unsourced facts this round. The new S81 rank argument and the S27 "squaring … does not move its minimizers" are short derivations, written out in full.
- The F08 rewrite added no new mathematics, apart from the step labels on the S89/S99 chains noted above.
