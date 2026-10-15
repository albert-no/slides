# 2026-10-15 — lec07 Korean Study 1/2 explainers rewrite

Verbatim slides ↔ slides-review messages, KST.

## 2026-10-15 18:22 KST — slides → slides-review

Review request — lec07 Korean Study 1/2 explainers rewrite (branch `trustworthy-ai-lec07-korean-notes-rewrite`, draft PR).
Albert (Slack, 18:17): the existing `lec07-backup-korean-note-for-study{1,2}.html` are still hard to understand; rewrite and open a PR.
What changed:
- Study 1 (2 → 3 printed pages): 3-line summary, glossary (comply/refuse/free-paid tier/scratchpad/alignment faking), employee analogy (labelled illustrative), slide 40 table, prompted study vs actual RL side by side (12%, 86 vs 97%, 12→78%, refusals fall but not to zero), "why faking failed" in 3 steps, FAQ (78% ≠ success; company-name variant; not instructed), slide 45 table.
- Study 2 (3 pages, now covers 46–55 not 49–55): summary, glossary, pipeline (1% docs, Sonnet 3.7 envs), AlwaysEqual in prose only (no code), onset figure reading, 4-step grading pipeline, one table for the four evals with verbatim prompts + graders + 69.8/39.9/31.8/41.3 vs baseline, caveats per eval, Fig 6(a) and Fig 5 values read from the slides' figures, shows/doesn't, Study 1 vs 2 contrast.
- No new facts beyond slides 40–55, their cites and the previous notes; slide-54 interpretation marked as authors' hypothesis.
- Rendered to A4 PDF (3 + 3 pages), checked at -r 60, no overflow. OUTLINE.md rows updated; outline-lint clean.
Please check facts against the papers and readability; I keep the PR draft until your sign-off.
