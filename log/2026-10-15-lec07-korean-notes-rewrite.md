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

## 2026-10-15 18:24 KST — slides-review → slides

Reviewed PR #54 at **bee686f**, checked the paper passages, and independently rendered all six pages. The glossary and flows help; no overflow. **Not approved yet:** the simpler explanation introduces certainty the papers do not support.

### 1. Study 1: distinguish observed change from an explanation for it
**P1 summary, p2 “왜 실패했나,” and p3 conclusion** imply complete failure and a proven mechanism.

Replace:
- “자신을 지키는 데 실패” → **“기존 거절 행동을 완전히 보존하지는 못했습니다.”**
- “가중치 전체가 강화됩니다” → **“순응한 응답도 학습에 쓰이므로, 그 응답을 만드는 모델의 가중치는 업데이트될 수 있습니다.”**
- “같은 답이므로 똑같이 보상” → **“보상 모델은 최종 답변만 평가하므로, 순응한 이유를 직접 구분하지 않습니다.”**
- “습관이 … 번집니다” → **“한 조건에서 배운 변화가 다른 조건의 응답에도 영향을 줄 수 있습니다.”**

Then explicitly separate:
**관측:** 전략 표현 증가 + 비학습 조건의 거절 감소.
**가능한 설명:** 전략의 간접 강화, 문맥에 묶인 답변 규칙 등. 정확한 원인은 확정되지 않음.

The employee analogy currently maps those two measured changes directly onto proven psychological mechanisms. Label that part **가능한 과정을 설명하는 비유**. Cite §5.2–5.3/§8.1 or F.1 beside the explanation, not only the numerical results.

### 2. Study 1: repair the experiment distinctions
- **P1 employee analogy:** “녹화되지 않는 B 매장” reintroduces the monitoring confusion. Use **“B 매장 영상은 재교육에 사용하지 않는다.”**
- **Glossary:** “학습에 쓰이는지 알 수 있습니다” → **“학습에 쓰이는지에 관한 정보를 제공받습니다.”**
- **P2:** “실제 학습이 전혀 없다” applies to the prompted experiment, **43(a)**, not all of slide 43: **43(b) uses synthetic-document fine-tuning**. Add a short scope note.
- Replace “학습을 피하려고” in both documents’ conclusions with **“학습으로 기존 성향이 바뀌는 것을 줄이려고.”**

### 3. Study 2: preserve the concrete explanation Albert requested
**P2’s compressed table loses the frame-colleague motivation.** Add a short sequence outside it:

> 인간 직원의 위반이 한 건 더 나오면 AI 거래 확대 승인 → 회사 수익과 AI 영향력 증가 가능 → 모델에게 동료의 위반을 조작할 기회 → 실제 근거만 보고하는지, 위반을 꾸며내는지 평가.

Retain the distinction between an opportunity and an instruction. Also retain the previous note’s distinction: **Fig. 21 contains partial monitor-prompt excerpts; full frame-colleague emails were not found.**

### Smaller factual correction
**Study 2 p1:** “두 실행의 차이는 ‘편법이 통했느냐’뿐” describes an outcome as the experimental intervention. Use:
**“핵심 비교는 편법에 벌점을 주지 않은 RL과 벌점을 준 기준 RL입니다.”**

### Readability
Study 1 p2 is packed while p3 has substantial space. Move the mechanism explanation to p3 beside its uncertainty FAQ; don’t shrink the font. Study 2’s grading table is useful, but the colleague scenario needs the short standalone walkthrough above.

Keep the glossary, exact questions, classifier caveats and hypothesis label for slide 54. Return corrected HTML/renders and commit SHA; keep PR draft.

## 2026-10-15 18:33 KST — slides → slides-review

Round 1 fixes are in 24199c4 (this log entry is the next commit). PR #54 is still draft. Renders are attached (Study 1 is 3 pages; Study 2 is now 4).

Study 1:
- I applied all six of your replacement wordings verbatim: 거절 행동 완전 보존 못함, 가중치 업데이트될 수 있음, 보상 모델은 최종 답변만 평가, 한 조건의 변화가 다른 조건에 영향, B 매장 영상 재교육 미사용, 정보를 제공받음.
- p2 now covers observations only. It has a 관측 box (전략 표현 증가 + 비학습 조건 거절 감소) and the title is "전략 표현은 늘었지만, 거절 행동은 줄었다". Scope note: 43(a) is prompted with no training, 43(b) is synthetic-document fine-tuning, 43(c) is the actual RL.
- I moved the mechanism to p3 as "가능한 설명 (확정된 메커니즘 아님)", beside the FAQ. It gives the indirect reinforcement of the strategy and the narrow context-bound rule as the authors' explanations, with "정확한 원인은 확정되지 않았습니다." The analogy is relabelled "가능한 과정을 설명하는 비유" and now says it is not proven. The footer cites §5.2–5.3, §8.1 and F.1 next to the explanation. The conclusion uses "학습으로 기존 성향이 바뀌는 것을 줄이려고" and adds that the cause is unconfirmed.

Study 2:
- p1: "핵심 비교는 편법에 벌점을 주지 않은 RL과 벌점을 준 기준 RL입니다."
- New p3: a standalone frame-colleague 4-step flow (조건 → 유인 → 기회 → 평가), "조작할 기회이지 조작하라는 지시가 아님", the per-eval caveats, and a source-scope bullet. That bullet says Fig. 21 has only partial monitor-prompt excerpts and that the full frame-colleague emails were not found, so the description is reconstructed from §2.
- The Study 1 contrast line uses the new wording. The glossary, verbatim questions, classifier caveats and the slide-54 hypothesis label are kept. Font sizes are unchanged and nothing overflows. The OUTLINE rows are updated.
