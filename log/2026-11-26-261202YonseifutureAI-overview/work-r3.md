# work-r3 — 2026-11-26-261202YonseifutureAI-overview

- **Branch:** `2026-11-26-261202YonseifutureAI-overview` (PR82). Revision baseline `753041e` (approved content `07f519c`).
- **Head:** the commit named in the pointer. It contains this file, an unchanged copy of `plan-v3.md`, and refreshed copies of `job.md`, `requests.md` and `evidence.md`.
- **Scope:** plan-v3 (C20–C24) only. 45 slides and 45 note articles. Speaking time stays 43:00 + 2:00. No splits. No changes to `reference/`, courses or scripts.

## Coverage

| Comment | Package | Stable ID: old page → new page | What changed |
|---|---|---|---|
| C20 | P6 | S07: 7 → 7 | The destination node is now **Private webpage / my manual**. The agent sub-label reads "reads email + updates the page". The point line reads "Possible path: outsider's text → unwanted page change". The "not authorized by me" label and the "More exposure, not proof of compromise" line are kept. The aria-label is rewritten. In the S07 note, the message and how-to-read now end at the private webpage, and the explanation of GitHub/repositories is gone. The E06 source paragraph is removed and E04 remains. S08 is unchanged. |
| C20 dep. | P6 | S06 note | The "Supported by E06 …" sentence is removed from Sources. E04 remains. |
| C21 | P7 | S20: 20 → 20 | Retitled **"Closed Tickets, Unsolved Problems"**. The four-ticket table is replaced by one forked-outcome diagram: Customer "Where is my refund?" → AI support agent (scored on: requests closed) → green **What the score rewards: ✓ Request closed / score goes up** and red **What the customer needs: ✗ Refund received / still missing** (the `.yi-x` SVG cross from F08 is kept). The Illustration tag and the head line "An AI support agent, scored on closed requests" are visible. The point line reads "A better score does not guarantee a better outcome". The cite line is unchanged. The note is rewritten for this single example and includes the leader's check. "Specification gaming" appears only in the note, with no intent claim and no claim that every scored AI does this. |
| C22 | P7 | S21: 21 → 21 | Retitled **"Two Different AI Privacy Risks"**. The slide has two separate rows and no arrow links them. **1 · What you share now:** Confidential file (uploaded today) → AI service → *Who can access or keep it?* **2 · What it learned earlier:** Personal information (in training data) → AI model → *May repeat it in an answer*. The point line reads "Check access to inputs and disclosure in outputs". The qualifier reads "Whether today's uploads train a model depends on the service and settings." The note ties row 1 to the email reader (processing, retention and access are separate from training) and points ahead to S22 for row 2. Sources add E22/E26. |
| C23 | P8 | S33: 33 → **32** | Rebuilt as **"A Reddit Summary Exposed a Login Code"**. The top box shows the user's request "Summarize the discussion". Below it, the existing public/private zone strip runs over Reddit comment (planted text) → AI browser (Comet, by Perplexity) → Private email (reads a login code) → Reddit reply (code posted publicly). The point line reads "Permission to read is not permission to send". The tag reads "Research demonstration · 2025" with "By Brave, a rival browser maker; not a Reddit or Gmail breach". The cite is Brave, 20 Aug 2025. The slide shows no code, payload, address or bypass step. The note follows the diagram order, names Brave's role as a rival, and ends with the bounded-permission bridge. The note cites E25 only and includes the course provenance. |
| C23 dep. | P8 | S36, S37, S44, S45 notes | **S36** sources: E06 "Always Allow" is replaced by E25 "Possible mitigations" (scoped permissions plus confirmation), marked as recommended, not shown sufficient. **S37** sources: E06 is replaced by E25 (outside text plus broad logged-in access). **S44** sources: the E06 link is replaced by the E25 link. **S45** "What can it change or send?" now refers to the Reddit/Comet case and uses the slide's takeaway. S45 sources now read "E02, E07, E08, E11, E25". |
| C24 | P9 | S27: 27 → **retired** | The main slide and its note article are deleted. Nothing was moved elsewhere. Its now-unused `.p5-orig/-photo/-capt/-qs/-q/-qbox` CSS is removed. The ID gap is the record. S26 → S28 transition checked: S28's note already says "The deepfake call was different", so it needs no provenance segue. E16/E24 are untouched in evidence. |

Search over main and notes: no `GitHub`, `repository` (except the unrelated "repository baseline 467cf06" provenance on S11), `Invariant`, `Always Allow`, `pull request`, `E06`, `C2PA` or "Origin Is Not Truth" remains.

## Page map (old 46 → new 45)

S01–S26 keep pages 1–26. S27 is retired. S28–S46 move from pages 28–46 to pages 27–45 (each −1). S33 is now page 32. Title, Contents and divider names are unchanged. Sections: Opening pp1–10 · 01 pp11–14 · 02 pp15–27 · 03 pp28–36 · 04 pp37–45.

## Shared surfaces (P9)

- Main: `1 / 45`. `<!-- SLIDE N -->` comment bars are renumbered.
- Notes: 45 articles, with headings renumbered 1–45 in screen order. The pacing table reads 8:00 · 4:00 · 14:40 · 9:20 · 7:00 = 43:00, plus 2:00 reserve. Slide ranges are 15–27, 28–36, 37–45 and total 1–45. Pace lines: S20 85 s, S21 80 s, S33 115 s. Every cumulative elapsed time was recomputed, and the final value is 43:00. A script checked that the section sums match the table.
- Leaf `OUTLINE.md`: 45 slides / 45 articles. The "plan-v2; revised by plan-v3" line notes S27's retirement. The section table has new slide ranges, IDs (02 = S15–S26, S28), line ranges and times. All slide pointers are recomputed, the S20/S21/S33 descriptions are updated, and the S27 pointer is removed. Root `OUTLINE.md`: "46 slides" → "45 slides".

## Checks

- `lint-deck.py` main and note: ok. `outline-lint.py`: 0 stale pointers. `find-wordy`/`find-dense`: no flags on changed slides.
- Overflow probe at 1280×720 (screen): output is identical to the `753041e` baseline. Pre-existing items on S08/S25/S41/S44 were already reviewed in r2. No item is on a changed slide.
- Print render (Chromium → PDF, 45 pages, `-r 60`) of pp6, 7, 8, 19, 20, 21, 22, 26, 27, 28, 31, 32, 33, 45. No overflow or overlap, labels are at the kit's 1.55rem floor or larger, nothing is shrunk, and the ✓/✗ glyphs render. Notes: 45 articles at 1280 and 390 px widths, and the narrow print run gives 45 pace lines.
- F01–F10 are not regressed. F04 lived on S27, which Albert has now removed. F08's SVG cross is reused on S20. F06's S28 wording is intact.

## Deviations / plan issues

- None. The titles and takeaways proposed in the plan were used verbatim. S21 node wording is mine ("Confidential file / uploaded today", "Personal information / in training data"), and it stays within E26.
