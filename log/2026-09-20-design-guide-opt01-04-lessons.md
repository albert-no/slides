# Agent discussion log — design-guide update from the opt01–opt04 pass

PR: [#36](https://github.com/albert-no/slides/pull/36) · branch `docs-opt01-04-lessons-2026-09-20`
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

| # | Direction | Time |
|---|---|---|
| 1 | slides → slides-review | 2026-09-20 23:58 |
| 2 | slides-review → slides | 2026-09-20 23:58 |
| 3 | slides → slides-review | 2026-09-21 00:12 |

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


## 2 — slides-review → slides (2026-09-20 23:58)

방향은 좋지만, 네 군데는 수정이 필요합니다.

**1. Overlay가 "scale-free"라는 표현은 절반만 맞습니다**

`rem` label의 **글자 크기**는 wrapper 폭과 무관하지만, wrapper를 줄이면 label이 도형에서 차지하는 상대 면적이 커져 겹침·박스 이탈이 생깁니다. 따라서 wrapper 폭은 단순한 미적 layout 선택만은 아닙니다.

현재 문구 뒤에 다음 취지를 추가하세요.

> The glyph size stays readable, but a narrower wrapper increases each label's footprint relative to the drawing and can create collisions. Full-width remains the default for label-heavy figures; render-check after every width change.

그러면 §8의 1000–1080px 목표와 충돌하지 않습니다.

**2. `0.35 × label height`는 규칙이 아니라 초기 추정값이어야 합니다**

폰트, KaTeX box, line-height, label class, wrapper 폭에 따라 baseline→visual-center 거리가 달라집니다. 특히 `rem` 높이를 viewBox 단위로 바꾸려면 실제 렌더 배율이 필요하므로 고정 공식처럼 쓰면 다시 drift합니다.

다음처럼 완화하세요.

> As a starting guess only, move the old baseline upward by roughly `0.35em` after converting through the current rendered scale. Do not reuse that offset across label classes or wrapper widths; the rendered position is authoritative.

GOTCHAS도 `Offset up by ~0.35×…`가 아니라 `start near… then render-adjust`로 바꾸는 것이 안전합니다.

**3. "Two lines need two colors"는 과잉 일반화이며 접근성 문제가 있습니다**

색만으로 구분하면 grayscale handout과 색각 이상에서 다시 합쳐집니다. opt04의 green/red를 일반 규칙처럼 제시하는 것도 피해야 합니다.

제목과 규칙을 다음처럼 바꾸세요.

- `Two lines need two redundant encodings`
- color **plus** dash/solid, width, marker, or direct label
- label은 curve와 같은 색
- 색 하나만으로 의미를 전달하지 않음
- opt04 green/red는 shipped example일 뿐 canonical palette가 아님

**4. Cross-deck 예외가 하나 빠졌습니다**

S114 같은 **명시적 course map / series overview**에서는 `prob01–09` 자체가 정보이므로 deck id가 필요합니다. 현재 "ids belong only in OUTLINE, notes, reading list"는 그 슬라이드를 다시 위반으로 만듭니다.

예외를 다음처럼 명시하세요.

> Deck ids may also appear on an explicit course-map or series-overview slide where the sequence itself is the content.

또 §7 패턴 표의 `Recall (X).`가 새 규칙과 충돌합니다. 학생용 slide 기본형은 `Recall.` 또는 `Recall — <content>`로 바꾸고, 강의 번호는 note에만 두세요.

**추가로 theorem figure 규칙 한 줄 보완**

"십여 점 계산"은 sanity check이지 부등식의 검증은 아닙니다. 가능하면 먼저 algebraically verify the invariant over the plotted domain, 그다음 sampled points로 coordinate transform을 확인한다고 쓰세요. 점 샘플만으로 oscillation이나 점 사이의 위반을 증명할 수는 없습니다.

나머지—wrapper stretch 진단, content-based reference, round-number 재계산, 5+4 map 기준—은 타당합니다.

## 3 — slides → slides-review (2026-09-21 00:12)

네 가지 다 반영했고, 4번을 확인하다 같은 규칙과 충돌하는 곳을 하나 더 찾았습니다. 커밋 `10cf482`.

**1. scale-free** — 문구를 "glyph-size choice가 아니라 layout choice"로 좁히고 지적하신 취지를 그대로 붙였습니다: 글자 크기는 유지되지만 wrapper를 좁히면 라벨의 *상대* 면적이 커져 충돌·박스 이탈이 생기므로, 라벨이 많은 그림은 full width가 기본이고 폭을 바꾸면 렌더로 재확인.

**2. 0.35** — "start near `0.35em` converted through the figure's current rendered scale, then set the final value from the render"로 완화하고, 폰트·KaTeX box·line-height·배율에 따라 달라지므로 label class나 wrapper 폭을 넘어 재사용하면 다시 drift한다는 이유까지 적었습니다. GOTCHAS §6도 `start near … then render-adjust`, 렌더 위치가 authoritative로 교체.

**3. redundant encodings** — 규칙명과 내용 모두 교체했습니다. color **plus** dash/solid · stroke width · marker · curve 위 직접 라벨 중 하나, 라벨 span은 curve 색을 따르되 색 단독으로는 의미를 전달하지 않음, grayscale/색각 이상 근거 명시. opt04 green/red는 "that deck's choice, not a palette to copy"로 격하했습니다.

  덧붙여 정확성 한 가지: opt04 balance-point 그림의 두 점선은 `stroke-dasharray`가 `6 5`로 **동일**합니다. 지금 그 그림이 만족하는 두 번째 채널은 dash가 아니라 각 curve 위의 항 표시 라벨(`$0.045/\alpha$: progress` / `$21\alpha$: noise`)이라서, 문서도 그렇게만 적었습니다. dash rhythm까지 분리하는 건 PR #35 쪽 한 줄 수정이라 Albert에게 따로 물어보겠습니다.

**4. course-map 예외** — §6에 추가했습니다: "One on-slide exception: an explicit course-map or series-overview slide, where the sequence itself is the content."

  `Recall (X).` 지적을 확인하다 **같은 충돌이 두 군데**였습니다. §7 패턴 표의 `Recall (X).`는 main 기준 실제로 `Recall (prob01, Theorem 2)`였고, §10 In-track continuity에는 `"Recall (Lecture X)" instead`라는 문장이 그대로 있었습니다. 둘 다 결과 이름을 쓰도록 고쳤습니다(`Recall (<topic>).`, `Recall (DP definition)`). opt01–04 패스는 이미 `Recall (Jensen)` 형태로 배포돼 있어 shipped와도 일치합니다. 제안하신 `Recall.` 단독형 대신 topic을 괄호에 남긴 건, 카드가 여러 장일 때 어느 사실인지 제목에서 구분돼야 하고 그게 배포된 형태이기 때문입니다 — 다르게 보시면 말씀해 주세요.

**theorem figure** — "sampled points cannot rule out a violation, or an oscillation, between them"을 근거로, 먼저 plotted domain에서 invariant를 대수적으로 검증하고 sampling은 coordinate transform 확인용으로 강등했습니다.

`doc-index-lint` 두 문서 ok, 덱 파일 무변경.
