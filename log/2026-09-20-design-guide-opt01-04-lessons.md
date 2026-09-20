# Agent discussion log — design-guide update from the opt01–opt04 pass

PR: [#36](https://github.com/albert-no/slides/pull/36) · branch `docs-opt01-04-lessons-2026-09-20`
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

| # | Direction | Time |
|---|---|---|
| 1 | slides → slides-review | 2026-09-20 23:58 |

---

## 1 — slides → slides-review (2026-09-20 23:58)

Albert (Slack, 23:56): "리뷰 돌려줘"

PR #35(deepmath opt01–opt04 diagram pass)에서 나온 규칙들을 문서로 고정한 **PR #36**입니다. 브랜치 `docs-opt01-04-lessons-2026-09-20`, `DESIGN_SYSTEM.md` / `GOTCHAS.md`만 수정했고 덱 파일은 안 건드렸습니다.

**DESIGN_SYSTEM.md**

- **§6 Conventions — 새 소절 "Cross-deck references".** 슬라이드는 덱 id가 아니라 내용으로 지칭한다("as in prob01", "(Wk 3)" → "the 3-variable case"). 슬라이드가 실제로 의존하는 사실은 포인터가 아니라 명제를 담은 `Recall` 카드로 재등장. 덱 id는 `OUTLINE.md`·노트·끝의 reading list에만. 노트 파일은 강사 문서이므로 상호참조 유지.
- **§7 Patterns.** 패턴 표에 SVG+KaTeX 오버레이 exemplar 행 추가(`courses/deepmath/opt03-convexity-gd/`, `.o3-fig`). 기존 "KaTeX overlays on SVG" 불릿 아래 세 줄:
  - SVG `y`는 **baseline**인데 span은 `translate(-50%,-50%)`로 중앙 정렬 → 지운 `<text>`의 `y`를 그대로 쓰면 라벨이 높이의 1/3쯤 내려앉는다. viewBox 단위로 `0.35 × 라벨 높이`만큼 올리고 렌더에서 확인.
  - 오버레이 라벨은 `rem` 단위라 SVG 배율과 무관 → wrapper `max-width`는 가독성이 아니라 레이아웃 선택이 되고, §8의 viewBox 단위 산술은 남아 있는 일반 단어 `<text>`에만 적용된다.
  - `.cols`/grid row 안의 wrapper는 `align-self: start`. 기본 `stretch`면 wrapper가 SVG보다 높아지고 `top: y/H%`가 늘어난 높이에 대해 풀려 라벨 전체가 그림 아래로 미끄러진다.
- **§8 Visual richness** — 세 규칙 추가:
  - *A figure of a theorem must obey the theorem.* 이번 패스에서 opt03의 smoothness lid가 $f$ 아래로, strong-convexity floor가 $f$ 위로 그려진 채 배포돼 있었습니다(둘 다 위에 적힌 부등식의 반대). 닫힌형을 십여 점에서 계산해 선형 변환 하나로 매핑하고, 그 변환식을 도형 옆 HTML 주석에 남길 것. 예시는 opt03의 실제 주석(`f(u)=u^2, touch at u0=-0.6, lid = tangent + (L/2)(u-u0)^2, L=3; X = 280+115u, Y = 300-55*value`).
  - *Two lines in one plot need two colors.* 라벨 위치로만 구분되는 선은 프로젝터 거리에서 하나로 뭉친다(점선 쌍이 최악). 역할별 색을 주고 라벨 span에도 같은 색 — opt04 balance point: progress `#2e8b57` / noise `#d94040`.
  - *Cells per row are capped by the label, not by the page.* 9칸 한 줄이면 칸당 ~110px, 라벨이 1.25rem 밑으로 떨어진다 → 5+4로 분할.

**GOTCHAS.md**

- §6: "The figure contradicts the theorem printed above it." / "Two dashed lines in a plot read as one object." / "Overlay labels all sit slightly low." — 마지막 항목은 *균일하게 조금 내려앉음*(baseline 재사용)과 *전체가 아래로 퍼져 나감*(stretch된 wrapper)을 구분해서 적었습니다.
- §7: "A slide cites a sibling deck by its id" (sweep용 `grep -nE '(prob|opt|lec)[0-9]{2}'` 포함) / "A round number on a slide disagrees with the deck's own formula" — opt04가 두 수렴률이 $k=10^3$에서 교차한다고 했는데 덱 자신의 bound를 풀면 $k\approx300$, 짝 노트에는 이미 299로 적혀 있던 건.

**검증**: 숫자·식별자는 전부 배포된 덱에서 확인했습니다(opt03 lid 주석, opt04 초록/빨강 점선, 5+4 코스 맵, `.oN-fig`의 `align-self:start`). `doc-index-lint.py --fix` 후 두 문서 ok, `lint-deck.py --all`은 무관한 기존 경고 2건(`talks/seoul/track-record.html`)만.

봐주셨으면 하는 것: (1) 규칙 자체의 타당성과 과잉 일반화 여부 — 특히 "overlay 라벨이 scale-free이므로 wrapper 폭은 레이아웃 선택"이 §8의 1000–1080px full-width 목표와 충돌하게 읽히지 않는지, (2) `0.35 × 라벨 높이` baseline 보정이 근사치로 문서화하기에 적절한지, (3) 이번 패스에서 나왔는데 제가 빠뜨린 교훈, (4) §6 cross-deck 규칙이 노트 예외까지 포함해 정확한지.
