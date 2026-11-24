# work-r3 — 2026-11-23-opt01-opt03-four-hour-core

Round 3, executing `plan-v2.md` (Albert's C12–C14). Same branch, same PR #80. No slide was added, removed, split or merged, and no mathematical or teaching text changed. Teaching time is still 150 + 90 = 240 minutes.

## 1. Commits (after `3d427a6`)

- `19bcc8b`: renames only (17 `git mv`, no content change). The old `opt03-convexity-gd/`, `opt02-regression-erm/`, `opt04-sgd/`, `opt01-svd-lowrank/backup/` and `courses/deepmath/backup/` folders are gone.
- `2e827d1`: all text edits: links, labels, outlines, DESIGN_SYSTEM paths, the prob05 strings.
- Report commit: this file, `plan-v2.md` copied unchanged, the refreshed `job.md`/`requests.md`/`evidence.md`, and two stale Markdown line counts in `courses/deepmath/OUTLINE.md` (§4). Review target: the SHA in the pointer message, which is this commit.

## 2. C12–C14 coverage

| Change | Done |
|---|---|
| C12 | Active GD now reads Lecture 11 everywhere: S01 and S134 pills, deck `<title>` (`opt02 — …`), HTML note `<title>`/`<h1>` ("Deep Learning Math 11"), Markdown `#` title, the "Lecture 11 companion note" front matter and the S01 article in both notes. opt01 is still Lecture 10. Cornell Lecture 5 and other source citations are unchanged. |
| C13 | Old opt03 main → `opt02-convexity-gd/` with all 51 IDs (S01…S134) in their old order. opt01 is unchanged apart from note pointers. |
| C14 | All four optimization backups, with their notes, are in `courses/deepmath/opt03-backup/` together with its `OUTLINE.md`. Regression and SGD are labelled backup (§3) and are not shown as this year's Lecture 11 or finale. |

## 3. Old → new manifest

The slide-ID sequence was compared as an md5 of the ordered `data-slide-id` list at `3d427a6` and now. Page counts come from Chromium PDF renders.

| Old path (`courses/deepmath/…`) | New path | Slides | IDs |
|---|---|---|---|
| `opt03-convexity-gd/opt03-convexity-gd.html` (+ `-note.html`, `-note.md`, `figs/o3b_figs.py`) | `opt02-convexity-gd/opt02-convexity-gd.html` (+ same) | 51 | S01…S134, sequence identical |
| `opt01-svd-lowrank/backup/opt01-svd-lowrank-full.html` (+ 2 notes) | `opt03-backup/opt01-svd-lowrank-full.html` (+ same) | 119 | S01–S119, identical |
| `opt03-convexity-gd/backup/opt03-convexity-gd-full.html` (+ 2 notes) | `opt03-backup/opt03-convexity-gd-full.html` (+ same) | 134 | S01–S134, identical |
| `opt02-regression-erm/opt02-regression-erm.html` (+ 2 notes) | `opt03-backup/opt02-regression-erm.html` (+ same) | 110 | no slide IDs at baseline (none added) |
| `opt04-sgd/opt04-sgd.html` (+ 2 notes) | `opt03-backup/opt04-sgd.html` (+ same) | 117 | no slide IDs at baseline (none added) |
| `backup/OUTLINE.md` | `opt03-backup/OUTLINE.md` (rewritten, §4) | — | — |
| `opt01-svd-lowrank/opt01-svd-lowrank.html` (not moved) | same | 68 | S01…S119 subset, identical |

Regression and SGD never had `data-slide-id`. Their 110 and 117 are slide counts (render pages), not ID sequences. The two full-edition HTML notes still have 119 and 134 articles.

## 4. Declared text changes

Checked with a word-level `git diff -M 3d427a6`. Every change falls into one of the classes below, and nothing else changed.

1. **Resource depth (archives).** The four archive decks and four archive HTML notes change `../../../../reference/` to `../../../reference/`: 8 occurrences per deck (including `data-brand-logo`) and 4 per note.
2. **Active GD identity.** Lecture 12 → 11 and own-name `opt03-convexity-gd*` → `opt02-convexity-gd*` (C12 row). Extended-edition pointers `backup/opt03-convexity-gd-full*` → `../opt03-backup/opt03-convexity-gd-full*`. Reading list: "(opt02, opt04) are extended material, listed in `../backup/OUTLINE.md`" → "are extended material in `../opt03-backup/`, listed in `../opt03-backup/OUTLINE.md`". `figs/o3b_figs.py` docstring: deck filename only.
3. **Active opt01 notes.** `backup/opt01-svd-lowrank-full*` → `../opt03-backup/…` (HTML 5, MD 7). The GD companion is now `opt02-convexity-gd-note.html`. The regression/SGD reading-list sentence is changed as in item 2. In MD ref 20, the "Each of these notes lives at `../<name>/<name>-note.md`" clause now comes before the backup sentence, so it no longer seems to cover the backup notes.
4. **Archive companions, resolved by content identity** (plan P7/P8.3):
   - The full opt01 note's default-lecture pointers go to `../opt01-svd-lowrank/…`. Its reading list names the backup regression, full-GD and SGD notes in this folder. MD ref 20: `../../<name>/` → `../<name>/`, and old lectures 11–13 are described as historical backup notes in this folder.
   - The full opt03 note's default pointers go to `../opt02-convexity-gd/…`. Its opt01 companion is `opt01-svd-lowrank-full-note.*` (the deck needs the pseudoinverse). Its regression and SGD pointers are the same-folder files.
   - The regression note's opt01 references (conventions line, ref 18) go to `opt01-svd-lowrank-full-note.*` (pseudoinverse, four subspaces). Its sequel goes to `opt03-convexity-gd-full-note.*`.
   - The SGD note's opt01, opt02 and opt03 companions go to the full opt01 note, the regression note and the full GD note.
   - Same-folder companions are bare filenames, as the decks already used.
5. **Backup identification [judgment].** The regression and SGD title pills now read "Deep Learning Math · Lecture 11 · Backup" and "… Lecture 13 · Backup". These are the only visible slide changes in the archives. The historical course-map slides and "next lecture"/finale wording are left as they were, and `opt03-backup/OUTLINE.md` explains them, as the plan prefers. I did not add a year to the label because none is sourced.
6. **Outlines.**
   - Root `OUTLINE.md`: the deepmath bullet now says 2 active optimization decks: opt01 (Lecture 10, 68/150) and opt02-convexity-gd (Lecture 11, 51/90), plus the `opt03-backup/` collection.
   - `courses/deepmath/OUTLINE.md`:
     - "Deck plan (11 active decks + optimization backup collection)": row 11 is now `opt02-convexity-gd/`, and the old rows 11 (regression) and 13 (SGD) are removed from the active sequence.
     - A new paragraph describes the backup collection (119/134/110/117 with tex ranges). "Exam-review deck (not one of the 11)".
     - The accessible-editions sentence is reworded (still 17 files).
     - Per-deck sections now list the two active decks first, then the four backups, each headed "backup, `opt03-backup/`". Regression and SGD are described as "Historical Lecture 11/13 (backup in 2026, not taught)". GD reads "Lecture 11", with "folder renamed from `opt03-convexity-gd/` 2026-11-24".
     - All file:line pointers are repathed. Deck line numbers did not change, because no edit inserts or deletes lines.
     - The full backup descriptions and counts are kept word for word.
     - Two pre-existing stale Markdown line counts are corrected (opt01 1248 → 1285, GD 1066 → 1100; both stale since the round-2 F08 rewrite).
   - `opt03-backup/OUTLINE.md` is rewritten:
     - It is an archive-only index that names the two active core paths.
     - It explains the historical prefixes (old Lectures 10–13) and that the full editions overlap the cores on purpose.
     - It has tables for the four triplets with counts.
     - The prob06 link is unchanged.
     - "No deck has been moved" and "kept at their original paths" are removed.
7. **DESIGN_SYSTEM.md.** Lines 312 and 371: `courses/deepmath/opt03-convexity-gd/` → `courses/deepmath/opt02-convexity-gd/`. Path only, with no rule text changed and no lines shifted. `doc-index-lint.py` reports ok.
8. **prob05 note (HTML + MD).** "reused by name in opt04" → "reused in the backup SGD lecture". No other probability file changed. prob09, exam and tex are untouched.

Frozen logs, plans, reviews and the repo-level `backup/` are not edited. `*.standalone.html` build artifacts (gitignored) are ignored.

## 5. Link and resource checks

- **Stale-path scan** (all `.md`/`.html`/`.py`/`.sh`, excluding `log/`, repo `backup/` and standalone builds). There are no hits for `opt03-convexity-gd/`, `opt02-regression-erm/`, `opt04-sgd/`, `opt01-svd-lowrank/backup`, `convexity-gd/backup`, `deepmath/backup` or `../backup/OUTLINE`. The only remaining `opt03-convexity-gd/` string is the "renamed from" note in the course OUTLINE.
- **Pointer resolver.** Every `<code>`, backtick, `href`, `src` and `data-brand-logo` pointer in the 24 changed files and both outlines was resolved relative to its file. Results:
  - 0 real misses.
  - Remaining flags are pre-existing false positives: the `-note.html` suffix in the "or `-note.html` in the original" phrasing, and `deck.css`/`deck.js` prose at DESIGN_SYSTEM:474.
  - Bare cross-folder companion names such as `prob07-estimation-note.html` are the existing by-name convention, and each resolves to exactly one file.
- **Browser load.** All 6 decks and 6 HTML notes were loaded from their final paths in headless Chromium.
  - Every page: 0 broken images, scripts and styles from `reference/`, and the Yonsei fonts loaded.
  - Decks: the footer logo loads (naturalWidth 591).
  - KaTeX elements per deck (0 `katex-error` each): opt01 534, opt02-GD 345, full opt01 537, full opt03 602, regression 518, SGD 543.
  - KaTeX elements per note (0 `katex-error` each): 1394, 890, 1099, 1130, 700, 943.
- **Lint.**
  - `lint-deck.py`: ok on all 6 decks.
  - `outline-lint.py`: 0 stale or missing pointers. Its 5 warnings are pre-existing, in infotheory/privacy.
  - `lint-accessible-md.py`, on all 7 changed Markdown files: one ERROR, `opt03-convexity-gd-full-note.md:49` "heading jumps from h1 to h3". It is pre-existing: the same file at `3d427a6` gives the same error. Two "visual reference" warnings (full opt01 note:7, prob05 note:813) are also pre-existing. I did not fix the archive error, because plan P7 keeps the archives as pass-through.
  - `doc-index-lint.py`: ok.

## 6. Render checks (`-r 60`)

- **Active GD:** p1 (S01 title, "Lecture 11" pill), p2 (Contents), p50 (no extra conditions) and p51 (S134 closer, "Lecture 11" pill). Layout, type and equations are unchanged.
- **Archives:**
  - regression p1 ("Lecture 11 · Backup") and p49 (projection SVG with KaTeX overlay labels);
  - SGD p1 ("Lecture 13 · Backup") and p32 (contour figure);
  - full opt01 p100 (math/text);
  - full opt03 p110 (display math).
  - All are clean, with logo and fonts present.
- **Moved notes at a real 430 px viewport** (agent-browser `viewport 430 900`; headless `--window-size` clamps at 500), compared with the same files at `3d427a6`:
  - Active GD note: docW 430, no horizontal scroll.
  - The four archive notes: docW 865 / 820 / 895 / 825. They scroll horizontally at 430 px exactly as they did at their old paths (identical values at baseline), because the legacy notes have no narrow-screen layout.
  - No archive note scrolls horizontally at desktop width (1280).
  - I left the legacy layout unchanged; changing it would be outside the pass-through scope.

## 7. Open points

None blocking. The judgment calls are the "· Backup" pill wording and leaving the historical course-map slides as they are, explained by the backup index. If you want the legacy notes made responsive at 430 px, that is a new layout change to the archives, and I need a plan line for it.
