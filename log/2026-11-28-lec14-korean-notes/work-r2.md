# work-r2 — 2026-11-28-lec14-korean-notes

- **Branch:** `2026-11-27-lec14-focused-overview` (PR #84 continuation), baseline `3dd5a99`, round-1 head `6d067ac`.
- **Head:** the commit named in the pointer. Changes since `6d067ac`: the two Korean HTMLs (text only, the review-r1 findings below), this file, an unchanged copy of `review-r1.md`, and refreshed copies of `job.md`, `evidence.md`, `requests.md` and `plan-v1.md` (the last two are unchanged). No deck, English note, OUTLINE, reference or figure change. Counts are unchanged: 59/52 slides and 111 articles.

## Findings

| ID | Done | What changed |
|---|---|---|
| F01 | yes | Guide G1: the "neither can see pricing" sentence is replaced with the review wording. The spending cap limits the order amount. A purchase approval can examine price loss if cost and planned price are shown. A price change on stock already held may never reach the purchase gate. The preceding "safeguards don't replace one another" sentence and the design-inference label are kept. |
| F02 | yes | Guide G2: the prompt/context item now uses the weight-update distinction. Note m31 / S71: the prerequisite paragraph now says updated weights are used in later tests, reading input does not update weights, and that this is not a claim that an agent's records or the results of its actions disappear. The dashed-box reading now says "입력을 읽는 것만으로 가중치가 갱신되지는 않는다는 뜻". The flow label is now "현재 문맥을 읽고 행동". "모델 자체는 조금도 바뀌지 않습니다" is replaced with the review wording. The tested-setting qualifier on the ICL null result is kept. The quoted slide label "그 실행 안에서 행동함" in the slide reading stays, because it translates the slide's own text. |
| F03 | yes | Note m42 / S36a: the control-group definition now reads as the review asked, with untrained, plain-number and other-animal teachers as controls. The last sentence is now "이 구획의 AI control은 뒤의 뜻입니다." Guide G2: the definition now says "관심 있는 요인을 달리하고 나머지는 똑같이 처리한 비교 대상". It adds that a group trained the same way on other data can also be a control. The ordinary-data explanation is kept. |
| F04 | yes | Guide B3 (`#ba3`): replaced with the review wording, separating Hammond's grouping from the appendix's three kinds of evidence. The three examples are kept. |
| F05 | yes | (1) Note m16 / S60 is now a three-study roadmap: Betley gives background, Cloud tests teacher-written numbers, Askin (main 34–40) tests learner-written answers scored by the teacher. The Askin v2 citation from m35 is added to the section source line. The prevalence-trend clause is now "다른 모델이 만든 데이터를 학습에 활용하기도 합니다". (2) Note m41 / S35: the first-story recap now uses the review wording; the agent gloss is kept. (3) Guide G7: the orphan "다섯 질문" sentence is replaced with the review wording about the five areas. |
| F06 | yes | Note m49 / S39a: the message, the explanation and the slide-qualifier rendering now use 확증/입증 rather than 증거, as given in the review. |
| F07 | yes | Exports regenerated from this content and copied to the shared slides mount (paths below). |
| F08 | taken | m09 / S52a: "저자들은 에이전트가 손님의 요구를 지나치게 맞추려 했다고 설명합니다". m30 / S70 and b48 / S91: "대략 10배 높다". The about-10% vs plotted-.08 sentence is unchanged. m51 / S40: "사전 감사가" and "사전 감사는" (particle slips from the r1 term change). G0: "도입 5분". |

## Exports (F07)

The source is the head commit of this push; the export content matches the tracked HTMLs at that commit. The files are untracked (`*.standalone.html` is gitignored) and sit in the shared checkout's tracked-record area, following the earlier jobs' `log/<job>/standalone/` folders. They are not in `jobs/`. `/workspace/extra/slides-log` does not exist on my side; `/workspace/extra/slides` is the shared mount.

| File | sha256 |
|---|---|
| `/workspace/extra/slides/log/2026-11-28-lec14-korean-notes/standalone/lec14-agentic-threats-note-ko.standalone.html` | `f6cf41e0bd9d3fa02d4b5c1eb0a27a5d7d7e6509f01f7d5badb6d2b17046f5be` |
| `/workspace/extra/slides/log/2026-11-28-lec14-korean-notes/standalone/lec14-agentic-threats-guide-ko.standalone.html` | `9f49c28a7fa013f850e706843140148e46608af64006f72228c2797a858a0ab7` |

The note-ko export links to the guide-ko export and the guide-ko export links back. English repo-only links are unwrapped with the offline-unavailable note: 7 in the note, 5 in the guide.

## Checks run

- Offline test: both files copied to an empty folder and loaded with a dead proxy at 430px. 0 relative references, 0 broken images, 0 elements past 430px, and each file has the other as its only local link.
- Tracked HTMLs: 0 elements past 430px or past the desktop viewport in either doc, 0 broken images, 0 bad internal or cross-document anchors, 111 articles.
- Word diff against `6d067ac`: only the strings listed above changed.
- Render: m31 at 430 (the changed flow and the prerequisite text), checked visually. All other edits are sentence replacements inside existing paragraphs.

## Plan issues

None.
