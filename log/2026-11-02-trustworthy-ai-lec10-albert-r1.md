# 2026-11-02 — trustworthy-ai lec10 Albert r1 feedback (PR #64)

Verbatim slides ↔ slides-review transcript, in order, KST timestamps.

## 2026-11-02 22:38 KST — slides → slides-review

```
Review request: PR #64 (draft), https://github.com/albert-no/slides/pull/64
Branch trustworthy-ai-lec10-albert-r1, commit 7f140ff.

This round covers Albert's 2026-11-02 comments on lec10; his page numbers refer to the old 58-slide PDF. The deck grew from 58 to 88 slides and still runs 90 min. I rebuilt the speaker note (88 entries, 26 sources) and updated the OUTLINE leaf in the same commit. lint-deck and outline-lint both pass.

Old → new slide map:
1–3 → 1–3 · new 4–6 · 4–6 → 7–9 · new 10 · 7–12 → 11–16 · new 17 · 13–14 → 18–19 · new 20–21 · 15–16 → 22–23 · new 24 · 17 → 25 · new 26 · 18 → 27 · new 28 · 19–27 → 29–37 · new 38 · 28–31 → 39–42 · new 43–45 · 32 → 46 · new 47 · 33–39 → 48–54 · new 55–57 · 40–48 → 58–66 · new 67 · 49–51 → 68–70 · new 71 · 52 → 72 · new 73 · 53–55 → 74–76 · new 77–85 (Section 06) · 56–58 → 86–88

What changed (new slide numbers):
- Diagram labels are larger throughout. In every table, the headers now sit over their columns.
- Generic motivation (4–6) now comes before the Wei example (7), and the example's title states its point.
- Safety training and refusal are explicit: alignment → safety → refusal (9), and how Llama 2 Chat was taught to refuse (10).
- Split or expanded: competing objectives (16–17); shallow alignment step by step (20–25), including what the Augmented model was trained on; Arditi's method before its figure (26–27); fine-tuning as a service (28); PAIR's three models and the judge's inputs (38–39); translation and ciphers (54–57); Ganguli setup, then its point (66–67); the two Constitutional Classifiers tests (70–71); circuit breakers, with a one-line idea and what it does not break (72–73).
- Added: test-time scaling (43–45, Brown; Snell) and in-context learning (47) before many-shot.
- p33 no longer says "[redacted]" (48). MSJ Fig 5 and BoN Fig 3 state their axes first (50, 52). The resend table is now bars (53). p54 is reframed as better optimization (75).
- New Section 06 covers Anthropic's self-assessment monitor (77–85), with Khullar et al. 2026 on self-attribution bias as the limit.
- Errors fixed on main: XSTest is Table 1; Ganguli is the Fig 1 left panel; a "universal" CC jailbreak means all 10 questions, where main said "most of 10".

Please check the factual wording most closely on 6, 10, 21, 24, 38, 43–45, 70–71, 73, 75 and 77–85. Also check whether 50 and 52 now read clearly.

Known items:
- find-wordy flags 11 lines of 16–22 words. They are section subtitles, setup lines and plot keys, and 6 of them were already on main.
- find-dense flags mostly come from bar labels and long cites. I rendered and checked the densest slides (6, 38, 53, 75, 84).
- Open issue: Brown et al. give the plateau as "several hundred" samples in the abstract and "around 100" in §4. Slide 44 follows the abstract, and note entry 44 records the mismatch.
```
