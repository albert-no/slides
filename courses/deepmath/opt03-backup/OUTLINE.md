# Deep Learning Math — optimization backup collection (`opt03-backup/`)

Archive only: nothing here is on the 2026 teaching path. The active final block is prob09
(week 13, first 120 minutes), then the two active optimization decks
`../opt01-svd-lowrank/opt01-svd-lowrank.html` (Lecture 10, 61 slides, 150 minutes, split
across weeks 13–14) and `../opt02-convexity-gd/opt02-convexity-gd.html` (Lecture 11, 48
slides, 90 minutes, week 14). See `../OUTLINE.md`.

All four optimization backups live in this one folder (moved here 2026-11-24, job
`2026-11-23-opt01-opt03-four-hour-core`). Each deck sits with its HTML note and its
accessible Markdown note. The filename prefixes are the **historical** deck numbers
(opt01–opt04, lectures 10–13 of the pre-2026-11 course); they are not active lectures, and
`opt03-convexity-gd-full` is not the active `opt02-convexity-gd`. Inside these files,
"opt02" means the regression lecture, "opt03" the convexity/GD lecture and "opt04" the SGD
lecture, and lecture numbers 10–13 are the old ones.

## Full extended editions of the active decks

The complete pre-2026-11-23 decks, kept whole rather than as an extract of the removed
slides. They deliberately overlap the active cores: every baseline slide is kept with its
stable ID (`data-slide-id`), so an `Snn` in an active deck is the same slide here, and each
note has one article per slide.

| Deck | Slides | Note (HTML) | Accessible note (Markdown) |
|---|---|---|---|
| `opt01-svd-lowrank-full.html` — SVD & low-rank approximation, full (rank/range/null, norms, SVD, pseudo-inverse, matrix norms incl. nuclear, Eckart–Young–Mirsky with Frobenius proof, Netflix/matrix completion); active core: `../opt01-svd-lowrank/` | 119 (S01–S119) | `opt01-svd-lowrank-full-note.html` | `opt01-svd-lowrank-full-note.md` |
| `opt03-convexity-gd-full.html` — convexity & gradient descent, full (convexity, smoothness, co-coercivity, strong convexity, PL, GD rates); active core: `../opt02-convexity-gd/` | 134 (S01–S134) | `opt03-convexity-gd-full-note.html` | `opt03-convexity-gd-full-note.md` |

## Backup-only decks

Not taught in 2026. Content unchanged apart from the moved file pointers and a "Backup"
label on the title slide; they cite the full opt01/opt03 editions above (pseudo-inverse,
co-coercivity, the old lecture numbers 10–13).

| Deck | Slides | Note (HTML) | Accessible note (Markdown) |
|---|---|---|---|
| `opt02-regression-erm.html` — least squares, ERM, ridge | 110 | `opt02-regression-erm-note.html` | `opt02-regression-erm-note.md` |
| `opt04-sgd.html` — SGD rates, mini-batching, strongly convex SGD | 117 | `opt04-sgd-note.html` | `opt04-sgd-note.md` |

Older full edition elsewhere in the course (not part of this collection): `../prob06-generalization/backup/prob06-generalization-full.html` (105 slides).
