# work-r1 — 2026-11-26-261202YonseifutureAI-korean

- **Branch:** `2026-11-26-261202YonseifutureAI-korean`, from baseline `e597ebf`.
- **ID-only commit:** `8c6c4f4`. It adds `261202YonseifutureAI-ko.html` and `261202YonseifutureAI-ko-note.html` as byte copies of the English pair. These copies keep the existing `data-slide-id` attributes S01–S26 and S28–S46, and the S27 gap. The commit changes nothing else.
- **Content commit:** `7adb37c`. It adds the Korean main deck, the Korean notes and the OUTLINE registration.
- **Head:** the commit named in the pointer. It adds this file and unchanged copies of `job.md`, `plan-v1.md`, `requests.md` and `evidence.md`.
- **Scope:** plan-v1 only. There are 45 Korean slides and 45 note articles, with the same IDs, order, cases, figures, numbers and timing (43:00 + 2:00). No argument, claim or source was added or removed.

## Packages

| Package | IDs / pages | Result |
|---|---|---|
| P1 | S01–S14 · pp1–14 | **Main:** translated. The speaker line reads "Albert No · 연세대학교", the role is 인융대학원 부원장, and no date or event was added. **Notes:** translated. |
| P2 | S15–S26, S28 · pp15–27 | **Main:** translated. S20 and S21 keep the clarified designs, S25 keeps its bars and inputs, and S27 stays retired. **Notes:** translated. |
| P3 | S29–S37 · pp28–36 | **Main:** translated. S33 is the Reddit/Comet case (E25), with the "연구 시연 · 2025" tag and "Reddit·Gmail 침해 아님". **Notes:** translated. |
| P4 | S38–S46 · pp37–45 | **Main:** translated. The S45 keywords stay English: Task · Information · Authority · Checks · Owner. **Notes:** translated. |
| P5 | shared surfaces | See the list below. |

**P5 shared surfaces**

- **Head of both files:** `lang="ko"`, Korean `<title>`, a Korean notes `<h1>`, and the `1 / 45` counter.
- **Hangul line breaking:** `word-break: keep-all` is set on `.deck` in the main file and on `body` in the notes.
- **Brand footer:** `data-brand-text="연세대학교"`.
- **Accessibility text:** all 14 `aria-label`s and both figure `alt` texts are in Korean and match what the slide shows. The figure pixels are unchanged, because the files are reused through their existing `figs/` paths.
- **Notes:** the Contents slide, the dividers and the pacing table are in Korean.
- **OUTLINE files:** the leaf and root OUTLINE changes are listed under "OUTLINE" below.

The main deck I translated myself. The note text was drafted by three subagents, one per range (S01–S14, S15–S28, S29–S46), working from a fixed glossary and the Korean main deck. The plan says its packages are not a request to spawn agents, so I'm disclosing this. I checked every fragment myself:

- line and tag counts match the source
- every URL, E-ID, C-ID, locator, number and elapsed time is preserved
- the S25 wording
- spot reads

I then aligned the terminology across the three ranges. I assembled the file, set the head and the pacing table, and ran all the checks.

## EN ↔ KO mapping

The mapping is identity. Page N in English is page N in Korean, with the same ID. Display order is S01–S26, then S28–S46: 45 pages, and S27 is retired in both versions. Sections:

| Pages | Section | Time |
|---|---|---|
| pp1–10 | Opening | 8:00 |
| pp11–14 | 01 커진 능력, 커진 영향 | 4:00 |
| pp15–27 | 02 유용한 AI도 실패한다 | 14:40 |
| pp28–36 | 03 누가 내 AI를 움직이나? | 9:20 |
| pp37–45 | 04 리더가 물어야 할 질문 | 7:00 |

Speech totals 43:00, plus 2:00 reserve.

Line offsets:
- **Korean main:** each slide sits 2 lines below its English line, because of one added style comment and one added rule.
- **Korean notes:** each line sits 1 line below its English line, because of the added `body` rule.

## Hashes (English unchanged)

- `261202YonseifutureAI.html`: `d82463e5f5b790bd037a18102cb6077677be7b407f2e20c3846ffd761100cdb9` (same as E01)
- `261202YonseifutureAI-note.html`: `1d2465f6d0f9de1f763cf2f6e14cf257f1675e940c590f174976a460f1671c86` (same as E01)
- `git diff e597ebf --stat`: the two new `-ko` files, the leaf `OUTLINE.md` and the root `OUTLINE.md`, plus this log folder. No changes to `reference/`, `scripts/`, `courses/` or `figs/`.

## Terminology decisions

- **Kept in English:**
  - Agent (AI Agent), Private and Public. In diagram zones these are PUBLIC and PRIVATE.
  - Email reader, Coding agent, read-only, Prompt injection, Jailbreak, Rollback, login code, AI browser and deepfake.
  - Product, company and model names.
  - The S45 keywords, the `.example` addresses on S36, and every citation line.
- **Korean:**
  - Illustration → 예시; invented → 가상의 예시.
  - Research demonstration → 연구 시연; vendor report → 개발사 자체 보고.
  - Me → 나; court / tribunal → 법원 / 재판소.
  - editorial synthesis → 자체 종합; editorial recommendation → 자체 권장 사항.
- **S25 tag:** "Audit 연구". In this context "감사" reads as financial audit.
- **S26 tag:** "정부 공식 자료". The source is the Hong Kong Government's reply to LCQ9.
- **S25 groups:** 피부색이 어두운 / 밝은 (Fitzpatrick IV–VI / I–III per the note). The S25 slide and note never use 흑인 or 백인. The S24 note keeps 흑인 환자, because that is the study's own term.
- **Qualifiers kept:**
  - possible vs certain: 가능한 경로, "침해의 증거는 아님", "답변에 나올 수 있음"
  - recommended vs current setup
  - control, not a guarantee
  - "데이터가 실제로 학습에 쓰인 경우에만" (S23)
  - "학습에 쓰이는지는 서비스와 설정에 따라 다르다" (S21)
  - the 개발사 자체 보고 tag on S19
- **One English phrase kept as written:** the S07 note says "control과 action arguments가 모두 중요하며" (E04, §2/§3.1). The English is ambiguous between "control flow" and other readings. I did not interpret it from memory.

## OUTLINE

- **Leaf:**
  - The deck table has two rows, English and Korean, and each row names its own note.
  - A Korean-version paragraph states the job, the identity mapping and the language rules.
  - The section table gives the English and Korean names, and line ranges qualified with the file name for both files.
  - Every English slide pointer is qualified with its file name.
  - A Korean pointer table covers the 24 cited slides (ID, Korean title, `261202YonseifutureAI-ko.html:N`).
- **Root:** "English and Korean versions, 45 slides each, with speaker notes in each language (`-ko` suffix)".

## Checks

- **`lint-deck.py`:** `ok` for the ko main and the ko note.
- **`find-wordy.py` / `find-dense.py` (ko main):** no flags.
- **`find-wordy.py` (ko note):** flags prose `<li>` items. These are speaker-note prose, the same kind as in the English note.
- **`outline-lint.py`:** 0 stale pointers. The 5 warnings are pre-existing, in `courses/infotheory` and `courses/privacy`. The 24 Korean pointers were computed from `data-slide-id` lines and checked as English + 2.
- **Counts:**
  - 45 `.slide` with `1 / 45`; 45 articles.
  - The ID sequence is identical to English in both files.
  - 45 pace lines. Their cumulative times recompute with no mismatch, ending at 43:00. Section sums match the pacing table: 8:00 · 4:00 · 14:40 · 9:20 · 7:00.
- **Print render:** Chromium print-to-PDF, 45 pages, at `-r 60`.
  - I read all 45 pages once. After fixes I re-read the edited pages 6, 7, 19, 21, 23 and 32.
  - There is no overflow, overlap or clipped label, and no type was shrunk. Mixed Hangul/Latin glyphs render, the citations clear the footer, and the figures are unchanged.
  - Wraps I accepted as clean: S17 left card, S20 customer quote, S34 "Coding agent를 거쳐", S37, and S41 "또는 유출: 되돌리지 못할 수 있음" (3 lines).
- **Screen probe at 1280×720, compared with English:**
  - The brand-footer item appears on every slide in both decks.
  - `fa-mid` probe items appear on S21 and S36. They are arrow-column boxes, and the renders are clean.
  - The English S08/S41 HSCROLL items do not occur in Korean.
- **Notes layout:** probed at 1265 and 485 px (485 is the headless minimum). scrollWidth equals the viewport and no element extends past it, the same as the English note.
- **Notes print and narrow screen:** a 37-page print read at `-r 50` and a 485 px screenshot. Hangul wraps cleanly.

## Wording fixes made after the first render

- **S06:** sub-label "둘 다 따를 수 있음".
- **S07:** "Me" → "나".
- **S19:** sub-label "OpenAI의 평가".
- **S21:** node "답변에 나올 수 있음", with a matching aria-label.
- **S23:** condition "데이터가 실제로 학습에 쓰인 경우에만".
- **S33:** sub-label "code 공개 게시".

All of these are rewording; no type size changed.

## Deviations / plan issues

- I used subagents for the note drafts (see Packages). I verified their output and made the terminology decisions myself.
- No other deviations. The proposed titles were used where they read naturally; the final titles are in the leaf OUTLINE Korean pointer table and the notes `<h2>`s.

## Unsourced facts

None added. The translation subagents flagged no doubtful fact.
