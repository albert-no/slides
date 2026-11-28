# work-r1 — 2026-11-28-lec14-korean-notes

- **Branch:** `2026-11-27-lec14-focused-overview` (PR #84 continuation, no new PR), from baseline `3dd5a99`.
- **ID-only commit:** none. Both decks already carry `data-slide-id` (59 main, 52 backup; unchanged).
- **Head:** the commit named in the pointer. It holds the two new Korean HTMLs, the title-only edits, both OUTLINE files, this file and unchanged copies of `job.md`, `plan-v1.md`, `requests.md`, `evidence.md`.
- **New files:** `courses/trustworthy-ai/lec14-agentic-threats-note-ko.html` (111 articles) and `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html` (G0–G7, B1–B6, terms, reading list, map). No file renamed.

## Packages

| Package | Range | Result |
|---|---|---|
| P0 (me) | titles, assembly, shared surfaces | C01 title on main S01 (`<h1>`, subtitle, `<title>`), English note `<title>`/`<h1>`/S01 heading, backup deck `<title>`/subtitle, tech `<title>`/`<h1>`. Korean title/subtitle on both Korean docs. Assembly script, TOC, page labels, article→guide links, guide→note links, lightbox, mobile flow layout, OUTLINE entries, exports. |
| P1 | main p1–15 · m01–m15 (15) | S01…S59 per map. Vend/agent story; title rationale in m01 from plan §1. |
| P2a | main p16–30 · m16–m30 (15) | Cloud et al. owl and misalignment transfer; roles, denominators, context vs training. |
| P2b | main p31–40 · m31–m40 (10) | S72a–S75b: transfer scope, OPD three steps, Askin Tables 1/10, teacher-origin channel. |
| P3 | main p41–59 · m41–m59 (19) | AI control: roles U/T/H, backdoor in submitted code, audit routing, the two safety denominators, Ge-Wang abort analysis, closing. |
| P4a | backup p1–26 · b01–b26 (26) | B1–B2 (+ title/contents): METR, RepliBench, Apollo, multi-agent. |
| P4b | backup p27–52 · b27–b52 (26) | B3–B6: MAST, control protocols, persuasion, hidden transfer more. |
| P5 | guide | G0–G7, optional appendix `#ba`/`#ba1`–`#ba6`, `#terms`, `#reading`, `#map`. Prose by design, not a concatenation of the notes. |

One subagent per package wrote an HTML fragment in a scratch area against a shared brief (plan §4 contract and the fixed terminology). I assembled, integrated, re-checked every package against the source articles and the map, and fixed terminology across packages. A separate read-only subagent did the render audit and a second did a Korean-vs-English fidelity review of a sample (below); I verified each of their findings against the files before acting.

## Coverage

| Comment | Done | Where |
|---|---|---|
| C01 title | yes | EN "Trust Beyond Capability" / "Delegation, Hidden Learning, and Oversight" on main S01 + note + backup + tech title surfaces; KO "유능한 AI, 믿고 맡겨도 될까?" / "위임·학습·감독으로 살펴보는 신뢰의 조건" on both Korean docs and m01. No slide restructure; 59/52 slides and 85 + 5 min unchanged (diff is title strings only). |
| C02 complete Korean notes | yes | note-ko: 59 main articles, then "선택 읽기: 백업 슬라이드 52장" (`#backup`) with 52 articles, each marked optional (pace line "본강의 시간 0분"). |
| C03 slide-by-slide | yes | one article per stable ID, same order as both decks (script-checked against the deck ID order), main before appendix; page labels "본강의 N" / "백업 N". |
| C04 flow/background | yes | guide-ko: G0–G7 with local prerequisite explanations and transitions, optional B1–B6 appendix, term index, reading list, slide→chapter map. |

## Slide mapping

No slide was added, split or moved; every deck page keeps its ID and page. The mapping below is page → ID → Korean anchor → guide chapter.

| Page | ID | Korean anchor | Korean title | Guide chapter |
|---|---|---|---|---|
| 본강의 1 | S01 | `#m01` | 유능한 AI, 믿고 맡겨도 될까? | G0 (`#g0`) |
| 본강의 2 | S02 | `#m02` | 목차 | G0 (`#g0`) |
| 본강의 3 | S04 | `#m03` | 신뢰가 무너지는 세 갈래 | G0 (`#g0`) |
| 본강의 4 | S03 | `#m04` | 01 · 실제 일을 맡기기 | G1 (`#g1`) |
| 본강의 5 | S05a | `#m05` | 매점의 결정 하나가 현실을 바꾼다 | G1 (`#g1`) |
| 본강의 6 | S05b | `#m06` | 허용된 행동도 실수일 수 있다 | G1 (`#g1`) |
| 본강의 7 | S57a | `#m07` | 매점에는 실제 결과가 따른다 | G1 (`#g1`) |
| 본강의 8 | S57b | `#m08` | 매점 주인 에이전트가 할 수 있었던 일 | G1 (`#g1`) |
| 본강의 9 | S52a | `#m09` | 원가 확인보다 먼저 나온 가격 | G1 (`#g1`) |
| 본강의 10 | S52b | `#m10` | 원가보다 싸게 판 매점 주인 | G1 (`#g1`) |
| 본강의 11 | S53a | `#m11` | 그 뒤 실적은 나아졌다 | G1 (`#g1`) |
| 본강의 12 | S53b | `#m12` | 구매에는 여전히 사람이 필요했다 | G1 (`#g1`) |
| 본강의 13 | S58a | `#m13` | 승인에는 장사의 근거가 필요하다 | G1 (`#g1`) |
| 본강의 14 | S58b | `#m14` | 지출 한도로는 가격 실수를 고치지 못한다 | G1 (`#g1`) |
| 본강의 15 | S59 | `#m15` | 손해 나는 주문 시나리오로 시험하기 | G1 (`#g1`) |
| 본강의 16 | S60 | `#m16` | 02 · 숨은 행동의 학습 | G2 (`#g2`) |
| 본강의 17 | S61a | `#m17` | 교사 모델이 학습 데이터를 공급할 수 있다 | G2 (`#g2`) |
| 본강의 18 | S61b | `#m18` | 의도한 전달 | G2 (`#g2`) |
| 본강의 19 | S63a | `#m19` | 불안전한 코드: 좁은 범위의 학습 변화 | G2 (`#g2`) |
| 본강의 20 | S63b | `#m20` | 변화가 코드와 무관한 질문에까지 미쳤다 | G2 (`#g2`) |
| 본강의 21 | S64 | `#m21` | 서로 다른 두 학습 경로 | G2 (`#g2`) |
| 본강의 22 | S65 | `#m22` | 올빼미 성향을 지닌 교사 모델 | G3 (`#g3`) |
| 본강의 23 | S66a | `#m23` | 숫자 목록만 남긴다 | G3 (`#g3`) |
| 본강의 24 | S66b | `#m24` | 별도의 학습자 모델을 학습시킨다 | G3 (`#g3`) |
| 본강의 25 | S67a | `#m25` | 대조군 학습과 비교한다 | G3 (`#g3`) |
| 본강의 26 | S67b | `#m26` | 나중에 동물에 대해 묻는다 | G3 (`#g3`) |
| 본강의 27 | S68 | `#m27` | 숫자가 나중의 동물 선택을 바꾸었다 | G3 (`#g3`) |
| 본강의 28 | S69a | `#m28` | 선호에서 안전하지 않은 행동으로 | G3 (`#g3`) |
| 본강의 29 | S69b | `#m29` | 숫자 밖의 답을 평가한다 | G3 (`#g3`) |
| 본강의 30 | S70 | `#m30` | 안전하지 않은 경향도 전달되었다 | G3 (`#g3`) |
| 본강의 31 | S71 | `#m31` | 프롬프트 주입이 아니라 학습이다 | G3 (`#g3`) |
| 본강의 32 | S72a | `#m32` | 전달은 모델 쌍에 따라 달랐다 | G3 (`#g3`) |
| 본강의 33 | S72b | `#m33` | 보편 법칙이 아니라 특정 조건의 발견 | G3 (`#g3`) |
| 본강의 34 | S73a | `#m34` | 학습자가 먼저 쓴다 | G4 (`#g4`) |
| 본강의 35 | S73b | `#m35` | 교사는 토큰마다 점수만 준다 | G4 (`#g4`) |
| 본강의 36 | S73c | `#m36` | 점수가 학습을 이끈다 | G4 (`#g4`) |
| 본강의 37 | S74a | `#m37` | 점수만으로도 비정렬이 옮겨 갔다 | G4 (`#g4`) |
| 본강의 38 | S74b | `#m38` | 여기서는 걸러 내도 전달이 사라지지 않았다 | G4 (`#g4`) |
| 본강의 39 | S75a | `#m39` | 교사와 학습자를 함께 점검하라 | G4 (`#g4`) |
| 본강의 40 | S75b | `#m40` | 이 시험들에서는 정렬된 교사가 도움이 되었다 | G4 (`#g4`) |
| 본강의 41 | S35 | `#m41` | 03 · 믿을 수 없는 작업 점검하기 | G5 (`#g5`) |
| 본강의 42 | S36a | `#m42` | 작업자의 의도가 아니라 작업 흐름을 점검하기 | G5 (`#g5`) |
| 본강의 43 | S36b | `#m43` | 시험을 위해 나쁜 작업 모델을 가정하기 | G5 (`#g5`) |
| 본강의 44 | S76 | `#m44` | 백도어는 제출된 코드 안에 있다 | G5 (`#g5`) |
| 본강의 45 | S37a | `#m45` | 작업 모델과 감시 모델을 나누기 | G5 (`#g5`) |
| 본강의 46 | S37b | `#m46` | 정밀 감사는 별도의 자원이다 | G5 (`#g5`) |
| 본강의 47 | S38a | `#m47` | 백도어 하나면 그 실행 전체를 잃는다 | G5 (`#g5`) |
| 본강의 48 | S38b | `#m48` | 정밀 감사에는 예산이 있다 | G5 (`#g5`) |
| 본강의 49 | S39a | `#m49` | 수상한 작업에 표시하기 | G5 (`#g5`) |
| 본강의 50 | S39b | `#m50` | 감사를 필요한 곳에 쓰기 | G5 (`#g5`) |
| 본강의 51 | S40 | `#m51` | 이 실험에서는 감시가 사전 점검보다 나았다 | G5 (`#g5`) |
| 본강의 52 | S77 | `#m52` | 경고는 작업 흐름을 바꿔야 한다 | G5 (`#g5`) |
| 본강의 53 | S43a | `#m53` | 공격자는 시점을 고를 수 있다 | G6 (`#g6`) |
| 본강의 54 | S43b | `#m54` | 공격자는 도중에 그만둘 수도 있다 | G6 (`#g6`) |
| 본강의 55 | S78 | `#m55` | 까다롭게 고른 공격이 이 점검들을 약화시켰다 | G6 (`#g6`) |
| 본강의 56 | S45 | `#m56` | 두 연구, 두 가지 안전성 질문 | G6 (`#g6`) |
| 본강의 57 | S46 | `#m57` | 결과에서 책임으로 | G7 (`#g7`) |
| 본강의 58 | S50 | `#m58` | 신뢰에는 유창함이 아니라 증거가 필요하다 | G7 (`#g7`) |
| 본강의 59 | S51 | `#m59` | 무엇이 당신의 신뢰를 얻을 수 있을까? | G7 (`#g7`) |
| 백업 1 | S80 | `#b01` | 백업 자료 | 선택 부록 (`#ba`) |
| 백업 2 | S81 | `#b02` | 백업 자료 목차 | 선택 부록 (`#ba`) |
| 백업 3 | S07 | `#b03` | B1 절 표지 — 자율성 측정 | B1 (`#ba1`) |
| 백업 4 | S06 | `#b04` | 작은 오류도 쌓일 수 있다 | B1 (`#ba1`) |
| 백업 5 | S08 | `#b05` | 위임하기 전에 능력부터 시험한다 | B1 (`#ba1`) |
| 백업 6 | S87 | `#b06` | 자율성에는 여러 개의 다이얼이 있다 | B1 (`#ba1`) |
| 백업 7 | S09 | `#b07` | 시간 지평은 과제 난이도를 잰다 | B1 (`#ba1`) |
| 백업 8 | S10 | `#b08` | 과제에서 시간 지평까지 | B1 (`#ba1`) |
| 백업 9 | S11 | `#b09` | 시험한 과제에서 시간 지평이 늘어났다 | B1 (`#ba1`) |
| 백업 10 | S12 | `#b10` | 점수는 설정에 달려 있다 | B1 (`#ba1`) |
| 백업 11 | S88 | `#b11` | 능력은 안전한 실행 시간이 아니다 | B1 (`#ba1`) |
| 백업 12 | S13 | `#b12` | 복습: 능력과 위임 | B1 (`#ba1`) |
| 백업 13 | S54a | `#b13` | 실제 개발자들은 절약된 시간을 잘못 짐작했다 | B1 (`#ba1`) |
| 백업 14 | S54b | `#b14` | 다른 척도, 그리고 날짜가 있는 결과 | B1 (`#ba1`) |
| 백업 15 | S14 | `#b15` | 자기 복제의 구성 요소별 성공률은 고르지 않다 | B1 (`#ba1`) |
| 백업 16 | S15 | `#b16` | 부분의 성공이 전체를 입증하지 않는다 | B1 (`#ba1`) |
| 백업 17 | S16 | `#b17` | B2 절 표지 — 감독자를 겨냥한 행동 | B2 (`#ba2`) |
| 백업 18 | S62a | `#b18` | 복습: 가중치를 바꾸지 않는 맥락 | B2 (`#ba2`) |
| 백업 19 | S62b | `#b19` | 복습: 미세조정은 모델을 바꾼다 | B2 (`#ba2`) |
| 백업 20 | S17 | `#b20` | 설정, 행동, 추론 | B2 (`#ba2`) |
| 백업 21 | S18 | `#b21` | 에이전트가 자기 점검 장치를 끌 수 있을까? | B2 (`#ba2`) |
| 백업 22 | S19 | `#b22` | 일부 모델은 시험에서 감독 장치를 껐다 | B2 (`#ba2`) |
| 백업 23 | S20 | `#b23` | 샌드배깅은 능력을 숨긴다 | B2 (`#ba2`) |
| 백업 24 | S21 | `#b24` | 지시하면 특정 시험 점수만 낮출 수 있다 | B2 (`#ba2`) |
| 백업 25 | S22 | `#b25` | 심어 둔 위협이 일부 시험 점수를 낮췄다 | B2 (`#ba2`) |
| 백업 26 | S23 | `#b26` | 나쁜 점수에는 여러 설명이 있다 | B2 (`#ba2`) |
| 백업 27 | S24 | `#b27` | B3 여러 에이전트 | B3 (`#ba3`) |
| 백업 28 | S25 | `#b28` | 협력이 실패하는 방식은 여러 가지 | B3 (`#ba3`) |
| 백업 29 | S27 | `#b29` | MAST: 공격자 없이도 생기는 실패 | B3 (`#ba3`) |
| 백업 30 | S28 | `#b30` | 더 나은 조정에는 검증이 필요하다 | B3 (`#ba3`) |
| 백업 31 | S29 | `#b31` | 한 에이전트가 공격을 다음으로 넘길 수 있다 | B3 (`#ba3`) |
| 백업 32 | S31 | `#b32` | 전파는 환경에 달려 있다 | B3 (`#ba3`) |
| 백업 33 | S33 | `#b33` | 숨은 협력은 감독을 어렵게 한다 | B3 (`#ba3`) |
| 백업 34 | S34 | `#b34` | 증거의 강도는 서로 다르다 | B3 (`#ba3`) |
| 백업 35 | S82 | `#b35` | B4 추가 통제 프로토콜 | B4 (`#ba4`) |
| 백업 36 | S83 | `#b36` | 작업 모델, 감시 모델, 보호된 정밀 감사 | B4 (`#ba4`) |
| 백업 37 | S84 | `#b37` | 운영상의 통제에서 쓰는 두 점수를 먼저 정의하기 | B4 (`#ba4`) |
| 백업 38 | S90 | `#b38` | 제출 전에 감시하기 | B4 (`#ba4`) |
| 백업 39 | S89 | `#b39` | 이 게임에서는 감시가 사전 검사보다 나았다 | B4 (`#ba4`) |
| 백업 40 | S41 | `#b40` | 검사는 위임하거나 편집할 수 있다 | B4 (`#ba4`) |
| 백업 41 | S42 | `#b41` | 프로토콜마다 도달하는 균형점이 다르다 | B4 (`#ba4`) |
| 백업 42 | S79 | `#b42` | 복습: 검사에는 중단 권한이 필요하다 | B4 (`#ba4`) |
| 백업 43 | S85 | `#b43` | B5 더 먼 연구 주제 | B5 (`#ba5`) |
| 백업 44 | S49 | `#b44` | 아직 열려 있는 세 질문 | B5 (`#ba5`) |
| 백업 45 | S55 | `#b45` | AI는 답할 뿐 아니라 설득할 수 있다 | B5 (`#ba5`) |
| 백업 46 | S56 | `#b46` | 많이 쓴다고 이롭다는 증거는 아니다 | B5 (`#ba5`) |
| 백업 47 | S95 | `#b47` | B6 숨은 전이 더 보기 | B6 (`#ba6`) |
| 백업 48 | S91 | `#b48` | 두 결과, 서로 다른 두 점수 | B6 (`#ba6`) |
| 백업 49 | S92 | `#b49` | 재현 결과는 모델·특성·과제마다 달랐다 | B6 (`#ba6`) |
| 백업 50 | S93 | `#b50` | 선호를 줄이는 방법이 해로움의 해결책은 아니다 | B6 (`#ba6`) |
| 백업 51 | S94 | `#b51` | 단정적인 비판 논문, 현재 수정 중 | B6 (`#ba6`) |
| 백업 52 | S86 | `#b52` | 백업 자료 끝 | 선택 부록 (`#ba`) |

## Omitted or combined paragraphs

Nothing substantive was dropped. Deliberate reductions:
- English "Script" paragraphs are carried as explanation under topical headings, not as transcript; English quotations become attributed Korean paraphrase.
- S69b: the format line and eight-question caveat appear twice in English; merged into one section each.
- Instructor line numbers in "Earlier in the course" lists (S13, S62a, S62b, S71, S73a–c, S74b, S75b) dropped; lecture/page/slide ID kept.
- Internal evidence-register tags (E01, E11, E12, E13, E18) omitted as bookkeeping; S54b keeps one mention of E06 to explain why follow-up percentages are not repeated.
- S14: slide colour hex codes for the RepliBench key omitted; model names kept.
- Structural slides (title, contents, dividers, closer) kept to role and transition.
- Cross-references to other slides rendered as Korean page + ID (e.g. S13 → "백업 11", S27 → "백업 30").
- The guide omits per-slide numbers by design and points to the note for them (P5 list: Vend side episodes, Cloud MMLU −4 and panels b–d, Askin 50.6/39.7 and Table 10, Greenblatt 71/19/0.338 and Table 7, most backup numbers).

Additions, all readings or background, no new facts: background definitions at first use (training/weights, system prompt vs context, 대조군 vs 운영상의 통제, temperature, epoch, 95% CI, MMLU, token, LoRA, EM, OPD, alignment); m32 "0.5 = 50%포인트" unit conversion; m55 one sentence that three intervals crossing zero are not individually conclusive (reading of the note's "the only interval that excludes zero"); m58 one sentence linking the new title to the closing claim (plan §1 rationale); S06 0.95 × 0.95 step-through labelled as the lecture's own illustrative calculation. Remove m55/m58 sentences if unwanted.

## Translation and meaning pass

- **Fixed terminology** across both docs: 교사/학습자/평가 모델; 대조군 (experiment) vs 운영상의 통제 (AI control), never mixed (all "통제 실험/평가" → "운영상의 통제 실험/평가"; "통제된 비교" → "대조군을 둔 비교"; the remaining "통제" uses are the ordinary statistical sense); 감시 모델 / 정밀 감사 / 중단 권한; 작업 모델; 제출된 코드 속 백도어; 서브리미널 학습; OPD; 스키밍(scheming).
- **Number diff** (script, every article vs its English article + slide): every number in the Korean text occurs in the English source; remaining differences are the deliberate drops above and "300k" written as "30만" (S56).
- **Source locators** restored where packages had shortened them: METR (170 tasks, 207 days, 95% CI 166–240, 80% horizon 4–6× shorter, §5–6, App. B.2/E.3–E.4) on S11, S12, S88; RepliBench scope (4 domains, 20 families, 86 tasks, Fig. 1, §5.1, §6) on S15, S23; S22 follow-up §3.2; Greenblatt (§2, Table 2, Fig. 2, Table 7, §5.1) on S83, S90, S89, S41; backup recall copies say which main slide they copy (S83 ← S37, S90 ← S39, S84 ← S38).
- **Fidelity review** (independent subagent, sample: main S03, S05a, S60, S61a, S64, S66a, S69a, S70, S72a, S73b, S74a, S76, S36a, S37a, S40, S43a, S43b, S78, S53a; backup S11, S19, S22, S28, S56, S62b, S91, S93; guide g3, g5). Fixed:
  - S72a (m32): distillation gloss said "a big model teaches a small one"; now "one model learns to imitate another's outputs; size is not part of the definition" (EN S61a).
  - owl: "부엉이" → "올빼미" everywhere (P2b, guide), matching the rest of the note.
  - S37a (m45): "책략" → "스키밍(scheming)".
  - S62b (b19): removed the added causal sentence ("the effect came from training, not reading the context"); now "in the tested setting, placing it in context did not reproduce it; it appeared after fine-tuning".
  - S91 (b48): Educational insecure gloss corrected to "teacher fine-tuned on data where the user asked for insecure code for educational purposes".
  - guide g3: removed "OpenAI API" (not in any baseline source).
  - "취약 코드"/"보안 취약 코드" → "불안전한 코드"; upfront auditing "사전 점검" → "사전 감사" (consistent with 정밀 감사); attacker "공격 전략" → "공격 계획" (deck: "attack plan") or "공격 정책" (deck: "attack policy").
  - "영어 노트의 출처 요약 / 영어 노트는 …" (S11, S12, S88, S15, S19, S10, Greenblatt/Ge-Wang src lines) reworded so the Korean note does not present the English note as the authority.
  - Not taken: reviewer suggested removing §3.2 from S37a's source line; kept, because the slide cite reads "§2, §3.2".
  - Clean in the sample: all other listed articles.

## Render checks

- **Desktop (1280) and 430px**, both docs (430 emulated with `html{width:430px}`; chromium's minimum window is 485): 0 elements past the 430px edge, 0 past the desktop viewport, 0 broken images, all internal and cross-document anchors resolve, no duplicate IDs. Re-run after the fidelity fixes.
- **Visual (print to PDF, `-r 60`)**, 59 pages: note-430 and note-1280 at every main section start and every backup section start (B1–B6), guide-430 and guide-1280 at G0–G7, `#ba`, B1–B6, terms, reading list, map, plus figure-explanation pages (Cloud, Askin, Greenblatt, Ge-Wang, Cemri MAST, vdW). Korean renders in Yonsei (YonseiBold/YonseiLight embedded); no tofu, no clipping; tables fit at 430.
- Fixed from the audit: flow diagrams now stack vertically on phones with ↓ arrows; small figures at 430 (guide Cemri p34, vdW p37) get tap-to-enlarge (lightbox) plus a hint line; a raw lec13 filename was reworded.
- **Title surfaces** rendered at slide size: main S01 and S02, backup S80 (p1), tech p1. No type change; text fits.
- Lint: main deck and tech pass; backup deck has the 5 hardcoded-colour warnings it already had at baseline. `outline-lint`: 0 stale pointers (7 existing ambiguous-basename warnings).

## Offline export

`scripts/bundle.py` per doc, then the cross-link points at the other `…-ko.standalone.html`, and links to English repo-only files are unwrapped to text with "(저장소 파일 …, 오프라인 사본에는 없음)" (note 7, guide 5). Untracked (`*.standalone.html` is gitignored):

| File | sha256 |
|---|---|
| `/workspace/extra/slides-wt/lec14fo/log/2026-11-28-lec14-korean-notes/standalone/lec14-agentic-threats-note-ko.standalone.html` | `64b1666029ed13e3546d1f715bc1d77c2fc591d19ae630910147ba3bc6ada08a` |
| `/workspace/extra/slides-wt/lec14fo/log/2026-11-28-lec14-korean-notes/standalone/lec14-agentic-threats-guide-ko.standalone.html` | `e0601bda85905c5d0f540eaf9b658ddcbc44262a65d4f4202d9e222b8902dcc8` |

Test: copied both to an empty folder and loaded with the network disabled (dead proxy). 0 relative references, 0 broken images, fonts embedded (Hangul in Yonsei), cross-link between the two files works; same articles and anchors as the sources.

## OUTLINE comparison against `3dd5a99`

- Root `OUTLINE.md`: 1 line changed (lec14 title reference). Headings identical (8).
- `courses/trustworthy-ai/OUTLINE.md`: +15 / −4. Headings identical to baseline (31; diffed). Changes: title references updated; the lec14 table row gains the two Korean files; a new "Korean companions" block after the Tech bullets, before `## backup-lec14-agentic-threats.html`, lists anchors m01–m59, b01–b52, g0–g7 with page ranges, `#ba`/`#ba1`–`#ba6`, `#terms`/`#reading`/`#map`. No other section touched.

## Deviations

- Lightbox (tap to enlarge) and mobile flow-stacking CSS/JS are inline in the two Korean docs; no `reference/` change.
- Offline copies unwrap links to English repo files (they would be dead offline); the tracked HTMLs keep the links.
- P3 additions in m55/m58 (see above) kept as readings; remove on request.

## Plan issues

None blocking. The baseline inconsistencies below were not fixed in the Korean text (it follows the slides and English notes and names the conflict where the source is internally inconsistent); they need a decision outside this job:
- S43b gives n = 596/185, S78 Table 1 gives 600/184.
- S78 Stop BashArena interval [−24, +46] with n = 2.
- S38b section references differ between slide and note.
- S36a alignment wording differs from the plan's definition.
- S72a: "reliably above zero" (slide) vs "significant" (note). S73b: probability (slide) vs log-probability (note).
- S53a: "Sonnet 4.0" (note) vs "Sonnet 4" (figure). Vend net-worth phase plot vs text.
- S69a: EN note says the "Unrel…" fragment is visible; the slide masks it (cite "fragment of the next label masked"). Korean follows the slide; EN note should be updated.
- Cloud: Fig. 3a Secure bar ≈ 0.01 vs "under 1%"; S70/S91 text ≈ 10% vs bar ≈ 0.08; the judge model is not stated in the paper.
- Source-internal: METR 169 vs 170 tasks (S10); RepliBench 9/20 vs 10/20 families (S15); Apollo 300 vs 100 rollouts (S19); MAST S27/S28/S31. Korean names each conflict.
- S23 omits Fig. 4; S87/S88 refer to old main IDs S05/S13; S49 established/not-established pair mismatched; S35 links unversioned; old evidence IDs E01/E13 cited in English notes.

## Unsourced facts

None added. Venues for S92 and S93 are unchecked; cited as preprints as in the baseline.

## Checks run

`lint-deck.py` (main, backup, tech), `outline-lint.py`, OUTLINE heading diff vs `3dd5a99`, deck ID/order script vs note order, slide counts 59/52 vs baseline, link/anchor/duplicate-ID script, number diff, 430/desktop overflow + image script, offline load test, visual render audit (59 pages, `-r 60`), title-slide renders.
