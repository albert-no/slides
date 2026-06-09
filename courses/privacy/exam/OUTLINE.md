# privacy/exam/ — Homework & exam set (Data Privacy)

Flat folder. Three artifact groups — homework, midterms, finals — plus shared style.
Course was renamed from "Mathematical Problems in Deep Learning" (2024) to "Data Privacy"
(2025–). Source `.tex` files use the `versions.sty` toggle to render problem-only vs.
solution PDFs.

## Homework

| HW | Source | Rendered | Notes |
|---|---|---|---|
| 1 | `hw1.tex` | `hw1sol.pdf` | Due Mar 31, 2026 |
| 2 | `hw2.tex` | `hw2sol.pdf` | Due Apr 13, 2026 |
| 3 | `hw3.tex` | `hw3.pdf` | |
| 4 | `hw4.tex`, `hw4.html`, `hw4sol.html` | `hw4.pdf`, `hw4sol.pdf` | current 5-problem set |

- `hw4old.tex` — prior 10-problem HW4 draft.
- `backup-problems/` — the 5 problems cut from HW4 (`hw4-unused.html`, `hw4-unused-sol.html`).

## Exams

| Year | Midterm | Final | Notes |
|---|---|---|---|
| 2024 | — | `final24.pdf` | old course name "Mathematical Problems in Deep Learning" |
| 2025 | `midterm25.pdf` | `final25.pdf` | |
| 2026 | `midterm26.pdf` | `final26draft.tex` | final dated June 11, 2026 (no PDF yet) |
| 2027 | — | `final27draft.tex` | next-iteration draft |

- `2026_1_Privacy.pdf` — **byte-identical duplicate of `final24.pdf`** (misnamed; safe to delete).
- Finals 2024–25 and both midterms are PDF-only (no `.tex` source committed here).

## Style

`math_hw.sty`, `versions.sty`, `math_commands.tex` — shared homework/exam class and math
macros. Build any `.tex` with `pdflatex` from this folder.
