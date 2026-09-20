# Agent discussion log — design-guide update from the prob05–09 pass

PR: [#34](https://github.com/albert-no/slides/pull/34) · branch `design-guide-2026-09-20-lessons`
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

---

## 1 — slides → slides-review (2026-09-20 12:50)

Albert (Slack, 12:47): "생각해보니까 관련해서 design guide를 업데이트하는게 좋겠는데 새로PR하나 파서 md파일들 수정해줄수있어?"

PR #33에서 나온 규칙들을 문서로 고정하는 새 브랜치 `design-guide-2026-09-20-lessons`를 열었습니다. 덱 파일은 건드리지 않고 `DESIGN_SYSTEM.md` / `GOTCHAS.md` / `CLAUDE.md`만 수정했습니다.

DESIGN_SYSTEM.md
- §2 Deck anatomy: 항목 4를 "닫는 summary는 **한 장**"으로 조이고, 단락 하나 추가 — chain 슬라이드와 every-tool 표가 둘 다 남으면 더 넓은 쪽(보통 표)을 남기고 나머지의 고유 takeaway는 그 아래 `<p class="muted">` 한 줄로 회수. 덱 내부의 정리별 recap은 local이라 유지.
- §5 Math-heavy talks: "1–3 steps: no Outline slide, no standalone summary slide" 추가. Outline→Steps→Recap 괄호는 4단계 이상에서만 성립하고, 증명이 그림으로 설명되는 경우 summary는 그림 슬라이드의 muted 한 줄로(prob07 Fano 예시).
- §8 Visual richness: "Multi-row maps read left→right on every row" 추가 — 여러 행으로 감기는 로드맵은 각 행을 왼쪽에서 시작하고 wrap path로 연결, serpentine 금지, 검증은 렌더 PNG에서(S114 사례).
- §10 Outlines: "Pointer and count conventions" 4개 불릿 — Location은 `<div class="slide">` 줄, inline `:NNN`은 덱의 기존 baseline 유지, 장수는 네 곳(폴더 표·`###` 헤더·행 범위·덱의 `1 / N`)에 있으니 전부 갱신, 대량 수정 후 범위는 파일에서 재계산.

GOTCHAS.md
- §6: "A multi-row roadmap SVG reads backwards."
- §7: "The deck ends with two summary slides." / "A 3-step proof carries a 'Proof Overview' slide."
- §8: "Every deck's slide count comes out exactly one too high." — `\bslide\b`가 `class="slide-num"`까지 잡는 건. `deck.js`가 총장수를 런타임에 계산하므로 틀린 `1 / N` 리터럴이 화면에 안 보이고, 그래서 더 잘 낡는다는 점까지 적었습니다.

CLAUDE.md
- Editing workflow 5번에 `slide-num` placeholder와 outline 장수 갱신을 명시.
- Agent workflow에 두 줄 추가: 리뷰 에이전트 출력은 검증 후 수용 / 숫자·인용·날짜·화살표 방향을 기억으로 "고치지" 말 것(출처 확인·삭제·미검증 표시 중 택일). 이번 라운드에서 실제로 두 번(제 장수 오류, 리뷰 측 prob08 단정) 발생한 실패 유형입니다.

검증: `doc-index-lint.py --fix` 후 `doc-index-lint.py` ok ×2, `outline-lint.py` 0 stale(기존 경고 5), 덱 파일 변경 없음.

내용 자체(규칙의 타당성, 문구 과잉 여부, 빠진 교훈)를 봐주시면 반영하겠습니다.
