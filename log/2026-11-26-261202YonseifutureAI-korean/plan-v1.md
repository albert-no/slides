# Plan-v1 — 추가 한국어 버전

## Summary / scope

영문은 그대로 두고, 승인된45장 전체에 **간결한 한국어 버전**을 추가한다. 새 주제나 새 논증을 만드는 작업이 아니다. 같은 그림, 사례, 순서, 사실의 범위와45분 흐름을 유지하고, 읽기 자연스러운 한국어와 익숙한 English를 섞는다.

- Job: `2026-11-26-261202YonseifutureAI-korean`; medium localization, up to2 review rounds.
- Frozen baseline: **e597ebf5e4ab2f0065aa603559ec1550aee645f9** (PR82, open/unmerged when checked). Reviewed English content:2336d436adcb8ccc4c60c72ab9f64b93d8ebf630.
- **New main:** `talks/261202YonseifutureAI/261202YonseifutureAI-ko.html`.
- **New notes:** `talks/261202YonseifutureAI/261202YonseifutureAI-ko-note.html`.
- **Untouchable:** existing `261202YonseifutureAI.html`, `261202YonseifutureAI-note.html`, existing figures, reference files and scripts. Byte-level preservation required, not merely “same meaning.”
- Read `PLANNER_BRIEF.md` and the design sections it points to; target leaf outline governs the current sequence. Korean Hangul treatment in `talks/261128yonseimath/261128yonseimath.html` is an existing presentation-language example, not a reason to modify shared assets or import its content.
- Keep the source's45-page order and IDs S01–S26/S28–S46; **do not revive S27**. Corresponding English and Korean pages should remain directly comparable. If a split is genuinely required for readability, report the mapping before treating it as accepted; never shrink text to force a match.
- Korean speaker notes are included to preserve the paired-deck workflow. Natural full sentences are welcome in notes; brevity is strictest on the main slides. No technical supplement, PDF/PPTX or standalone export delivery requested.

## Request coverage and conflict resolution

| Comment | Interpretation | Where / acceptance |
|---|---|---|
| C01 | Preserve current version; add Korean alongside it | Two new ko files; original HTML hashes unchanged; bilingual root/leaf entries |
| C02 | Short, direct Korean, not literal sentence-for-sentence translation | All45 main slides; same argument with phrases and diagram labels, no explanatory paragraphs added |
| C03 | Leave English when forced Korean sounds unnatural | Titles, terms, proper names, technical expressions and citations; natural prose remains Korean |
| C04 | Keep simple English such as Agent, Private, Public | These exact words remain English wherever used; consistent terminology across main/notes |

No conflict: C01 preserves the English files; C02–C04 govern the added Korean version only. The earlier request for English is not revoked. A fresh language artifact does not reopen the English job's exhausted review rounds.

## Language rules — must / prefer / slides decides

1. **Must:** use **Agent, Private, Public** in English, not forced 대리자/비공개/공개 replacements for those diagram labels. AI, GPT-2, GPT-4o, Reddit, Comet, Perplexity, Brave and cited names stay as written. Keep **Prompt injection** and **Jailbreak** where they identify the course concepts; explain each only as briefly as the existing main does.
2. **Prefer:** familiar role labels such as `Email reader`, `Coding agent`, `read-only`, `login code`, and `rollback` may stay English when that reads better. Do not turn every ordinary Korean phrase into English merely because some terms remain English. Natural words such as 요약, 승인, 매뉴얼, 환불, 권한, 학습 are fine.
3. **Must:** terse natural Korean, no translationese, nominalized chains or unnecessary 은/는/것이다. Diagram labels should describe the role/action immediately. Preserve needed distinctions and qualifiers rather than mechanically deleting them to meet a word count.
4. **Must:** do not strengthen 가능/위험/권장/당시 연구 into 확실/완벽/현재 적용/모든 AI. “Control, not a guarantee” must remain explicit. “Research demonstration” is 연구 시연, not 실제 침해 사례. “Illustration” is 예시; “vendor report” is 개발사 자체 보고. Date/evidence-type tags remain visible.
5. **Must:** English proper names, paper titles, URLs and citation locators remain accurate; original published figure pixels/redactions and numeric chart inputs stay unchanged. Translate surrounding labels or notes, never repaint source data for localization. Darker/lighter skin groups on S25 are not synonyms for 흑인/백인.
6. **Prefer:** name speaker `Albert No · 연세대학교`; use Albert's own supplied `인융대학원 부원장` if translating the role. Do not invent an expanded official school name, Korean personal name, event label or confirmed date.
7. **Slides decides [judgment]:** the proposed Korean titles below are starting points, not literal replacements. Improve awkward phrasing directly while preserving the point. Keep the current exhibits by default; adjust Korean line breaks or composition locally without changing shared styles/English files. Meaning-bearing labels must retain design-system legibility, including mixed Hangul/Latin text.

## Per-slide specifications

Common to **every row**: **must** preserve the named point/qualifier and the baseline visual's causal order, source data and case scope. **Prefer** the proposed Korean title; **slides decides** final wording/layout within those constraints. Reuse the corresponding baseline exhibit (workflow, comparison, figure/chart or divider); no new illustration is required. Main = concise localized title/labels/takeaway/necessary qualifiers. Notes = Korean message → how to read → speaking cues/sources/limits, aligned with that exact main. Source citations are inherited primary references, not this plan. Acceptance for each row: Korean title+exhibit express the listed point at a glance, numbers/qualifiers match the source, and the note does not contradict it.

`src:E##` below resolves to the fixed original evidence register identified in local evidence E02. Each source entry and English note supplies primary URL/version/locator. Structural rows have no new empirical claim. Page numbers are the current45-page English baseline, not the earlier46-page draft.

| Page / ID / package | Baseline English title | Proposed Korean title [judgment] | Must: point, exhibit and translation guardrail | Evidence | Target time |
|---|---|---|---|---|---|
| 1 / S01 / P1 | Trustworthy AI: What Should We Delegate? | Trustworthy AI: 어디까지 맡길까? | 제목과 발표자. 똑똑함보다 맡길 권한이 주제. 날짜·행사명을 새로 만들지 않음. | 구조/편집 | 30s |
| 2 / S02 / P1 | Every Semester, the Same Paperwork | 학기마다 반복되는 행정 업무 | 기존 학기별 폴더와 기억 문제. 인융대학원 부원장 역할; 실제 시간 절감 수치를 만들지 않음. | src:E02 | 50s |
| 3 / S03 / P1 | Email Becomes a Private Manual | 이메일로 만드는 Private 매뉴얼 | 흩어진 메일→나만 보는 웹 매뉴얼. 메일·페이지 그림은 예시임을 유지. | src:E02 | 55s |
| 4 / S04 / P1 | Updated Weekly | 매주 갱신하는 매뉴얼 | 새 메일→업데이트 초안→내 승인→갱신. 매주 반복; 무인 자동승인으로 번역하지 않음. | src:E02 | 45s |
| 5 / S05 / P1 | Agents Can Read and Act | Agent는 읽고, 실행한다 | 챗봇 답변과 도구를 쓰는 Agent의 결과 대비. 도구로 일을 수행하는 AI라는 짧은 정의. | src:E02, src:E01, src:E03 | 45s |
| 6 / S06 / P1 | When Email Gives Orders | 이메일 속 문장이 지시가 된다 | 내 요약 요청과 외부 메일의 지시를 대비. Prompt injection 한 줄 정의; 실제 공격 아닌 예시. | src:E04 | 65s |
| 7 / S07 / P1 | Access Without Authority | 접근 권한 ≠ 실행 승인 | 외부 메일→한 Agent→Private webpage. 원치 않는 변경의 가능한 경로; 이미 침해됐다는 단정 금지. | src:E04 | 50s |
| 8 / S08 / P1 | Read, Approve, Then Build | 읽기 → 승인 → 만들기 | read-only Email reader→내 수동 승인→별도 Coding agent→Private 매뉴얼. 위험 감소이지 보장은 아님. | src:E02, src:E04 | 75s |
| 9 / S09 / P1 | What Should AI Be Allowed? | AI에게 어디까지 허용할까? | 할 수 있는 일 안에 허용할 일을 구분한 그림. 능력과 위임 권한을 구분. | src:E02, src:E03, src:E04, src:E05 | 45s |
| 10 / S10 / P1 | Contents | 오늘의 이야기 | 네 섹션의 한국어 이름/순서가 divider와 정확히 일치. 설명 추가하지 않음. | 구조/편집 | 20s |
| 11 / S11 / P1 | 01 More Capable, More Consequential | 커진 능력, 커진 영향 | 섹션01. 기존 질문에서 더 넓은 결과/영향으로 이동. | 구조/편집 | 15s |
| 12 / S12 / P1 | From Answers to Actions | 답변에서 실행으로 | 답변→초안→실행 그림. 도구 연결로 결과가 현실의 변경이 될 수 있음. | src:E03, src:E01 | 75s |
| 13 / S13 / P1 | Same Error, Different Stakes | 같은 오류, 다른 피해 | 동일한 잘못된 안내가 Private 초안→고객 메일→청구 시스템으로 번짐. 예시, 피해가 필연이라는 주장 금지. | src:E03, src:E08 | 75s |
| 14 / S14 / P1 | Capability Is Not Assurance | 능력만으로 안심할 수는 없다 | 능력 확인과 실제 업무의 조건/권한/점검, 둘 다 필요. 모두 통과해도 위험0 보장 아님. | src:E03 | 75s |
| 15 / S15 / P2 | 02 When Useful AI Goes Wrong | 유용한 AI도 실패한다 | 섹션02. 서로 다른 실패와 점검으로 이어짐. | 구조/편집 | 15s |
| 16 / S16 / P2 | The Citation Looked Real | 그럴듯한 인용, 없는 판례 | 법률 인용→제출→검증→제재.2023년 특정 사건; 변호사들이 허위 인용을 제출하고 고수했다는 책임 맥락 유지. | src:E07 | 85s |
| 17 / S17 / P2 | The Chatbot Promised a Refund | 챗봇의 답이 회사의 약속으로 | 챗봇 안내와 실제 항공사 정책의 충돌. 유족 운임의 사후 신청 불가를 환불 전면 금지로 바꾸지 않음. | src:E08 | 75s |
| 18 / S18 / P2 | Answers Need Checkable Sources | 출처는 직접 확인해야 한다 | 인용 있음→원문 확인→사람 확인→행동, 불확실하면 전문가로. 출처 표시는 검증과 다름. | src:E03, src:E07, src:E08 | 55s |
| 19 / S19 / P2 | Agreeable Is Not Always Helpful | 맞장구가 늘 도움은 아니다 | OpenAI의2025년 GPT-4o 업데이트/rollback 연표. 개발사 자체 보고와 각 날짜를 유지. | src:E09 | 75s |
| 20 / S20 / P2 | Closed Tickets, Unsolved Problems | 문의는 종료, 문제는 그대로 | 환불 문의→종료 건수로 평가받는 AI→종료 처리와 미지급 환불 대비. 더 좋은 점수≠더 좋은 결과; 실제 기업 아닌 예시. | src:E10, src:E26 | 85s |
| 21 / S21 / P2 | Two Different AI Privacy Risks | Privacy 위험은 두 가지 | 지금 올린 파일의 접근/보관과 이전 학습 정보의 출력 가능성을 분리. 업로드의 학습 사용은 서비스·설정에 달림. | src:E26, src:E11, src:E22, src:E12 | 80s |
| 22 / S22 / P2 | A Model Repeated Personal Information | 모델이 개인정보를 그대로 내놓았다 | Carlini 원본 그림/가림 그대로.2021년 GPT-2·Public 웹 학습 데이터; 공개 정보도 반복 공개가 무해한 것은 아님. | src:E11 | 65s |
| 23 / S23 / P2 | Deletion Has More Than One Meaning | 파일 삭제 ≠ 학습 내용 제거 | 학습에 실제 사용된 경우의 전후 그림. 파일을 지워도 학습 영향 제거가 입증되는 것은 아님; 삭제 불가능 주장은 금지. | src:E12 | 60s |
| 24 / S24 / P2 | Cost Was Not the Same as Need | 의료비와 치료 필요는 다르다 | 의료비 예측→점수→지원 배정과 건강 필요의 차이. 같은 점수에서 흑인 환자의 질병 부담이 컸던 특정 연구. | src:E13 | 85s |
| 25 / S25 / P2 | One System, Very Unequal Errors | 같은 시스템, 크게 다른 오류율 | 동일 IBM 성별 분류기의 네 오류율 막대,0–40%축,얼굴 이미지1,270장의 벤치마크. 피부색 분류를 인종으로 치환하지 않음. | src:E14, src:E20 | 65s |
| 26 / S26 / P2 | A Familiar Face Was Not Proof | 익숙한 얼굴 ≠ 본인 확인 | 녹화된 deepfake 회의→메시지 지시→송금.2024년1월 홍콩 사례,약 HK$200 million 유지; 실시간 대화로 바꾸지 않음. | src:E15 | 85s |
| 27 / S28 / P2 | Mistakes and Attacks | 실수와 공격, 다른 점검 | 공격자 없는 오답과 외부 지시의 조종을 대비. 직전 deepfake는 의도적 기만이었음을 노트 전환에서 유지. | src:E03, src:E18, src:E04 | 50s |
| 28 / S29 / P3 | 03 Who Can Steer Your AI? | 누가 내 AI를 움직이나? | 섹션03. 이제 AI 자체를 조종하는 공격에 초점; 앞 내용이 모두 실수였다고 하지 않음. | 구조/편집 | 15s |
| 29 / S30 / P3 | A Stop Sign Fooled a Classifier | STOP 표지판을 오독한 모델 | Eykholt 원본 두 사진 유지. 설계된 스티커/당시 분류기 실험; 실험실·drive-by 촬영, 실제 자율주행 사고 아님. | src:E17 | 70s |
| 30 / S31 / P3 | Attacks Can Enter Earlier | 공격의 입구: 학습과 사용 | 변조된 학습 예와 업무 중 읽는 문서의 지시, 서로 다른 두 경로. 공격 절차·수식 추가 없음. | src:E18, src:E04 | 60s |
| 31 / S32 / P3 | Requests Versus Retrieved Instructions | 내 요청인가, 남이 심은 지시인가? | Jailbreak는 사용자 요청, 간접 Prompt injection은 외부 자료의 지시. 작성 주체/유입 경로 차이 유지. | src:E04, src:E01 | 65s |
| 32 / S33 / P3 | A Reddit Summary Exposed a Login Code | Reddit 요약하다 login code가 유출됐다 | 사용자의 요약 요청,Public 댓글→AI browser→Private 메일→Public 답글.2025년 Brave 연구 시연; 실제 피해/플랫폼 침해 주장 금지. | src:E25 | 115s |
| 33 / S34 / P3 | Who Can Change What? | 누가 쓰고, 무엇을 바꾸나? | 외부 메일의 작성자·읽는 주체·바꿀 대상을 구분. Agent의 권한이 외부 작성자의 권한은 아님. | src:E02, src:E03, src:E04 | 65s |
| 34 / S35 / P3 | Handoffs Do Not Sanitize Text | Agent를 거쳐도 지시는 남을 수 있다 | 외부 메일→읽기 전용 Agent→내가 승인한 요약→Coding agent. 사람 승인도 악성 지시를 놓칠 수 있음. | src:E05, src:E04 | 60s |
| 35 / S36 / P3 | Approve the Actual Change | 요약 말고, 변경 내용을 승인 | 출처·실제 주소 변경·대상 페이지가 드러난 검토 카드. 두 invented .example 주소 보존; 권장 확인 절차,현재 구성 아님. | src:E03, src:E04, src:E25, src:E02 | 60s |
| 36 / S37 / P3 | Enforce the Permission Boundary | 권한 제한은 모델 밖에서 | 제안된 행동→시스템의 권한 gate→허용/차단. 권장 예시; 파일 수정 제한만으로 외부 전송까지 막는다는 보장 금지. | src:E03, src:E04, src:E25, src:E02 | 50s |
| 37 / S38 / P4 | 04 What Leaders Should Ask | 리더가 물어야 할 질문 | 섹션04. 도입/위임 전에 할 수 있는 결정으로 전환. | 구조/편집 | 10s |
| 38 / S39 / P4 | Delegate a Bounded Job | 할 일부터 정하고, 권한은 최소로 | 한 주 메일 요약의 범위와 제외된 발송/수정 권한을 표시. 실제 필요 이상 접근 권한을 주지 않음. | src:E02, src:E04, src:E03 | 55s |
| 39 / S40 / P4 | Test the Actual Workflow | 실제 업무 흐름에서 테스트 | 정상·오류·조작 메일 예시→실제 업무→제한적 도입. 테스트 통과는 근거이지 안전 보장은 아님. | src:E03 | 60s |
| 40 / S41 / P4 | Detect, Stop, Recover | 발견하고, 멈추고, 복구하기 | 되돌릴 수 있는 페이지 수정 vs 송금·외부 공유. 로그는 탐지용, 되돌리기 어려운 행동은 실행 전 확인. | src:E15, src:E03 | 60s |
| 41 / S42 / P4 | A Safety Score Needs Context | 안전 점수는 조건과 함께 | 업무·접근 범위·공격·시험 조건을 숫자 주위에 배치. 설명 없는 수치/새 benchmark 만들지 않음. | src:E03 | 50s |
| 42 / S43 / P4 | Name the Human Owner | 책임질 사람을 정하라 | 승인·관찰·대응 주체를 지정. Air Canada 특정 판결을 모든 나라의 일반 법률로 바꾸지 않음. | src:E08, src:E03 | 50s |
| 43 / S44 / P4 | Back to My Weekly Manual | 다시, 나의 주간 매뉴얼 | 현재의 분리/승인 흐름과 추가 권장 확인을 구별. 추천 source/변경검토를 이미 하고 있다고 번역하지 않음. | src:E02, src:E04, src:E05, src:E25 | 60s |
| 44 / S45 / P4 | Five Questions Before Delegating | 맡기기 전, 다섯 가지 질문 | Task·Information·Authority·Checks·Owner 다섯 질문. 리더가 바로 쓸 짧은 한국어 질문,핵심 English 단어 허용. | src:E03, src:E02, src:E07, src:E08, src:E11, src:E25 | 60s |
| 45 / S46 / P4 | Thank You | 감사합니다 | 질문/토론으로 종료; 새 요약이나 주제 추가 없음. | 구조/편집 | 15s |

## Section names and timing

Contents and the four dividers must use the same chosen Korean names. Proposed:
-01 커진 능력, 커진 영향 — pp11–14,4:00.
-02 유용한 AI도 실패한다 — pp15–27,14:40.
-03 누가 내 AI를 움직이나? — pp28–36,9:20.
-04 리더가 물어야 할 질문 — pp37–45,7:00.

Opening pp1–10 stays before Contents as in the authorized personal-story structure:8:00. Total speech43:00, reserve2:00 =45:00. Retain the per-slide times above as planning values; Korean delivery is not yet a measured rehearsal. Do not double the time merely because two language versions now exist.

## Packages and shared surfaces

| Package | Slide IDs/pages | Editable content | Dependencies |
|---|---|---|---|
| P1 | S01–S14,pp1–14 | Korean opening/Contents/capability section and matching notes | Current authentic workflow; shared terminology |
| P2 | S15–S26,S28,pp15–27 | Korean failure/privacy/case section and matching notes | Current S20/S21 clarified designs; source figures and numbers unchanged |
| P3 | S29–S37,pp28–36 | Korean attack/Reddit/control section and matching notes | P1's personal workflow; source E25; not the retired GitHub case |
| P4 | S38–S46,pp37–45 | Korean leadership/closing section and matching notes | P1–P3 terminology/callbacks |
| P5 | Both new files' shared surfaces; root/leaf outlines | Counts, headings, lang/document titles, accessible descriptions, timing, section names, links/pointers | After P1–P4; do not alter English HTML |

These packages define scope, not a request to spawn parallel implementation agents. slides should resolve translation/design judgments with the full context.

- Register both languages separately in the leaf table and provide Korean section/slide pointers without invalidating English pointers. Root should say English and Korean versions,45slides each, not a90-slide talk. Disambiguate bare filename/line references when adding a second main HTML to the leaf.
- Reuse shared assets by their existing relative paths; no duplicate figure copies or shared-reference modifications. New Korean accessibility descriptions and metadata must agree with visible content.
- Stable IDs: preserve corresponding IDs, including the S27 gap, in both new files. Add the IDs to the new pair in a separate attribute-only commit, and report it; never change English IDs or renumber S28 as S27.

## Preservation / review acceptance

1. English main/note hashes exactly match local evidence E01. Existing assets/reference/scripts are unchanged; allowed source diff is new ko files + root/leaf outline registration only.
2.45 Korean main slides and45 paired articles, matching IDs/order; same concepts, cases, figures, numbers and43+2-minute budget. The most recent Private-webpage, clarified p20/p21, Reddit replacement and S27 retirement are all carried over.
3. Titles, labels, main takeaways, notes and accessibility descriptions are concise/natural Korean where appropriate; Agent/Private/Public remain English. No awkward forced terms, untranslated English explanatory paragraphs accidentally left in the Korean main, or literal phrasing that changes a claim.
4. Current/recommended, demonstration/incident, possible/guaranteed, input/training, model/classifier and identity/gender distinctions survive localization. No compressed-away security qualifier. Notes retain source URLs/locators and limits.
5. Render every Korean page at1280×720 and in print; inspect Hangul/Latin wraps, diagram-label sizes, glyphs, source figures, citations/footer clearance and section titles. Main/note lint and wordy/dense checks; target/root outline lint with actual pointer spot-checks. Test notes at desktop and about430px width. Font shrinking is not a translation strategy.
6. Return work-r1.md with exact content/head and ID-only SHAs, per-package result, English↔Korean page/ID mapping, hashes, terminology decisions, timing/counts, test results and any deviations. No new claim, source or argument change should be silently introduced.

## Branch / PR handoff

Use branch `2026-11-26-261202YonseifutureAI-korean` from the pinned baseline. Copy the completed planner files unchanged into this job's tracked record; refresh living files at each push. Do not edit or append content to the English job's record/branch/PR82. The new branch intentionally depends on that unmerged English baseline; slides-review will disclose this when opening the localization PR against main after approval. No merge to clear the dependency without Albert's direct order.

Only exact-commit review can approve the Korean version. At most2 rounds for this medium localization; only blockers trigger the second. After approval, finalization commits touch only this job log. No PDF, export delivery or merge is authorized by this plan.
