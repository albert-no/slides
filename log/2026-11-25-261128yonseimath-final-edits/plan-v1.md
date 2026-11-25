# Plan v1 — brief introduction and final wording/intuition edits

## Summary and fixed context

Add one brief biographical page immediately after the title, without years. Ground the AI idea loop in the watermark problem, remove the requested personal/closing prose, and replace growth with the simplest correct same-perimeter/maximum-area AM–GM intuition. Preserve the three-part argument and all unrelated approved exhibits.

- Baseline: **0bf4927790540020c4b826e9ae2a78da2d5d65fc**, 24 pages/paired notes; existing PR81.
- Files: `talks/261128yonseimath/261128yonseimath.html` (main), `talks/261128yonseimath/261128yonseimath-note.html` (note), target leaf/root `OUTLINE.md`; deck-local figure/generator only if needed for the new area comparison.
- Korean concept-first, advanced middle-school audience, 25 minutes. Target25 pages, approximately24 minutes plus1-minute buffer. New introduction≈40seconds; reduce AM–GM≈100→60seconds to make room. Shortened reflection/close may finish earlier; never pad or silently lengthen the talk.
- **Reconciliation:** C05 supersedes the prior job's growth choice and earlier preference against elementary rectangle teaching. Use a minimal symbolic area comparison, not the old numeric rectangle exercise. “연도빼고” means career years on the new introduction, not scientific result/event dates.
- **Crucial page mapping:** after the insertion, oldp19→newp20, oldp20→newp21, oldp21→newp22, oldp22(Jensen)→newp23, oldp23(close)→newp24. C06 targets S21, NOT the Jensen slide S24.
- All content/design choices below are **[judgment]** for slides; implement inline or with full context, not context-free text replacement.

## Coverage / baseline-title map

| Comment | Baseline page / title | Stable IDs | Target page | Package |
|---|---|---|---|---|
| C01 | opening, after p1 title | new S26 after S01; S01 note synchronization | 2 | P1 |
| C02 | p19 AI와 함께 더 많은 아이디어 시험하기 | S19 | 20 | P2 |
| C03 | same p19 | S19 | 20 | P2 |
| C04 | p20 오래 남은 것은 수학의 의미 | S20 | 21 | P2 |
| C05 | p21 평균 성장배율이 같아도, 들쭉날쭉하면 덜 성장한다 | S23; S24 note bridge only | 22; 23 note | P2 |
| C06 | p23 수학을 직관으로 이해하고, 현실에 적용하기 | S21 | 24 | P2 |

Preserve all existing IDs. S02/S16 stay retired; do not reuse them. Next unused ID is S26, paired main/note. All old pages after p1 shift by one if the target one-page insertion is used. Report the actual complete mapping in work-r1.

## Slide specifications

### S26 — new, after S01 (C01; P1)
- **Point/title:** briefly establish the speaker as a fellow program graduate and current professor. Suggested title: **“영재원 수료생에서 교수로”**; natural title is slides' call.
- **Must:** these five milestones in the supplied order, with no years:
  1. 연세대학교 과학영재교육원 심화반/사사반 수료
  2. 서울대학교 전기공학부/수리과학부 복수전공
  3. Stanford MS/PhD in EE
  4. 홍익대학교 전자전기공학부 조교수
  5. 현재 연세대학교 인공지능학과 부교수
- **Prefer:** render the Stanford item as “Stanford 전기공학 석사·박사” if this is clearer in Korean; it is the same requested MS/PhD in EE, not another degree. Preserve the two-degree/discipline information. Mark Hongik as a past role where needed so current employment is unambiguous.
- **Exhibit/layout suggestion:** one simple five-stage career-path diagram or clean five-row profile list (`ul` / `diagram-flow` vocabulary only). No year axis, extra summary paragraph, portrait requirement, awards, industry role or additional Hongik rank. Five short entries are enough; no tiny CV.
- **Note:** brief first-person introduction, same selective facts without career years, with profile URL and author-supplied course detail recorded in sources. Do not invent reminiscences. S01's note must no longer say “세부 이력은 넣지 않습니다”; avoid repeating all five facts on S01.
- **Evidence:** E01/E02. **Time:**≈40seconds.
- **Acceptance:** all five items legible, year-free, chronologically meaningful without implying Hongik is current. Paired S26 article immediately after S01. Title/event date elsewhere remains untouched.

### S19 — problem and idea above the AI loop (C02/C03; P2)
- **Point/title:** retain **“AI와 함께 더 많은 아이디어 시험하기”**; relate the loop to the concrete task just discussed.
- **Must, at the top of the body before the loop:**
  - **“문제: LLM이 생성한 문장에 표식남기기”**
  - **“아이디어: 의도적인 통계 삽입”**
- **Exhibit:** the existing idea → AI implementation/experiment → new-idea loop. Preserve that AI can contribute ideas; do not reintroduce the deleted independent-checking slogan. The two new lines are the task/approach framing, not a second unrelated exhibit.
- **Slides decides:** shorten or remove the subordinate “10번 중 7번이라면?” label if needed to keep the new framing clear. Optional coin calculation remains in the note, not new main content.
- **Note:** explain once that “통계 삽입” means creating a statistical property through biased generation, not literally inserting numerical statistics in the text. Then the existing example/iteration can follow. No new technical derivation.
- **Evidence:** E04. **Suggested layout:** existing `diagram-flow` with compact problem/idea framing. **Time:**≈60seconds.
- **Acceptance:** both requested lines visible above the loop; no crowding/type reduction; main and note agree on the meaning of the idea.

### S20 — remove the contrast statement (C04; P2)
- **Point/title:** retain **“오래 남은 것은 수학의 의미”** and the formula/technique → explaining in words → meaning/intuition flow.
- **Must:** delete the entire highlighted statement “문제 풀이 훈련도 도움이 됐지만, 저에게 진짜 중요했던 것은 직관이었습니다”. Do not replace it with a slightly reworded highlight making the same contrast.
- **Note:** update the short message/script to the direct reflection that explaining mathematics in words and understanding what an expression means mattered. Remove the same deleted contrast from mandatory speech; keep the authentic reflection rather than inventing an episode. The diagram's “문제 풀이 훈련” label itself is not prohibited by C04.
- **Evidence:** E01. **Suggested layout:** existing `diagram-flow`, without replacement filler. **Time:**up to70seconds, shorter if natural.
- **Acceptance:** requested sentence/contrast is absent; meaningful flow remains. No blank card or unnecessary substitute summary.

### S23 — same perimeter, greatest rectangle area (C05; P2)
- **Point/proposed title:** **“같은 둘레의 직사각형 중, 정사각형의 넓이가 가장 크다”** (wording can be tightened, but retain the scope “직사각형”).
- **Must:** the most concise geometric interpretation of known AM–GM: rectangle sidesa,b>0 → same-perimeter square with both sides(a+b)/2; rectangle areaab≤square area((a+b)/2)². Equality whena=b. This is not a claim that a square beats every plane shape.
- **Exhibit:** one symbolic rectangle/square comparison at a common length scale, with the common-perimeter relationship immediately apparent and square identified as maximum area. No numeric side lengths, fence story, multi-step exercise or elementary re-teaching of AM–GM. One compact AM–GM/area comparison may anchor the picture; avoid two redundant equivalent formula blocks.
- **Must remove:** growth paths, “들쭉날쭉”, “고르게” as growth comparison, “성장배율”, two-year growth discussion and their note/outline/caption remnants. A minimal rectangle comparison is now authorized by the latest direct request; do not restore the old large numerical rectangles lesson.
- **Note:** one short paragraph connecting fixed perimeter→fixedsum a+b, areaab maximized ata=b; optional single algebraic check fromE03. No growth/investment analogy or detailed proof lesson.
- **Evidence:** E03. **Suggested layout:** large comparison diagram with one `math-block` if useful. **Time:**≈60seconds.
- **Acceptance:** two depicted perimeters equal, common length scale, area ordering faithful, no on-screen numbers/growth terminology, scope clear. If generating an asset, report reproducible code/path/parameters; do not redraw a mathematically inconsistent schematic by eye.

### S24 — Jensen main stays; note bridge changes (C05 consistency; P2)
- **Must preserve:** approved main title, direct log inequality with positive-domain qualifier, graph/chord, legible inline midpoint label and equality-aware short note. No new theory or extra main text.
- **Only change needed:** replace the note's “성장 이야기와 곡선이 휘는 이야기가 하나로 이어집니다” bridge with the new fixed-perimeter/area interpretation. Preserve the mathematical log/AM–GM connection.
- **Evidence:** E03 plus inherited polish E10/E12. **Time:**≈110seconds, unchanged.
- **Acceptance:** no obsolete growth reference; do NOT treat new page23 as the target of C06.

### S21 — remove the closing sub-explanations (C06; P2)
- **Point/title:** retain **“수학을 직관으로 이해하고, 현실에 적용하기”**.
- **Must keep:** the two primary statements **“수학을 직관으로 이해하기”** → **“그 직관을 현실 세계의 문제에 적용하기”**.
- **Must delete:** both subordinate captions **“AM–GM = 성장 이야기”** and **“글의 표식 = 통계 문제”**. Do not substitute new examples or a new footer summary.
- **Note:** remove the false visual instruction that small captions appear below the boxes. Keep the close brief; no residual AM–GM growth explanation. No need to restate both detailed examples in the spoken close.
- **Evidence:** E01. **Suggested layout:** existing two-box `diagram-flow` only. **Time:**up to70seconds; shorter is fine.
- **Acceptance:** two main statements and arrow remain, both sub-explanations gone; note describes the actual screen and current intuition.

## Packages and shared surfaces

- **P1:** newS26 + S01 note only; main/note introductory region. Depends onE01/E02. No other biography from the linked profile.
- **P2:** S19/S20/S23/S21 main+note, S24 note bridge only. May add/update deck-local geometry and generator forS23; leave the tested watermark assets/player/data unchanged. Depends onE03/E04 and prior approved presentation.
- **Shared, by slides:** insertS26 with matching noteID; recompute all later page headings/counts/elapsed pacing, deck footer and both outlines. Root AM–GM lookup must say fixed-perimeter area, not growth. Target25 paired pages and no more than24minutes of speech plus1buffer. Keep existing no-Contents exception. No shared `reference/`, engine or design-system edits.
- Work report: exact commit/branch; each C01–C06; old→new page mapping; any wording/layout deviations; figure parameters/path if added; notes/outline synchronization and checks. Do not silently change the argument or timing. Only two review rounds.

## Acceptance / delivery

Render new/changed slides and neighbours, especially intro1–3 and closing19–25 under the target numbering; actual resulting indices govern. Check diagram labels and wraps without shrinking text. Check paired notes at430/1280 widths; lint main/note and pointers. Test the unchanged animation still resolves after insertion (no page-index assumptions); no new feature work or literature research.

Keep the existing PR81 head frozen at baseline while this job is built/reviewed. After approval, push exact planner records; reviewer verifies all post-review commits are only this job's log, then authorizes conditional fast-forward to PR81. No merge, force push, main push, branch deletion or PDF delivery.
