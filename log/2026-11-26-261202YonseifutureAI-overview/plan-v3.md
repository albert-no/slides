# Plan-v3 — Albert's executive-clarity revision

## Changes since plan-v2

C20–C24 replace the repository destination on S07, clarify S20's metric-versus-goal lesson and S21's two privacy risks, substitute the course's Reddit/Comet research example for S33's GitHub example, and remove S27. These requirements supersede only the affected v2 specs. All other content and the English, nontechnical executive argument remain approved unless a dependency below requires a local update.

- **Size:** medium-sized amendment within this existing large job; several local comments, no new argument or literature survey. Preserve the existing job/branch/PR82 and **round3 of3**; do not reset review rounds or open another PR. Albert directly authorized this scope in message22; no fresh large-job gate is necessary.
- **Revision baseline:** `753041e2bfe1ed77592613cd4ff73ff615810176`, confirmed exact remote PR82 head and unmerged on2026-11-26. Original creation baseline467cf063 remains in job.md. Page references below refer to this frozen 46-page baseline, never moving main.
- **Files:** `talks/261202YonseifutureAI/261202YonseifutureAI.html` (main), `talks/261202YonseifutureAI/261202YonseifutureAI-note.html` (notes), target leaf `OUTLINE.md`, root `OUTLINE.md` entry only where counts/pointers require it. No course, reference or script edits. No new technical supplement or export delivery.
- **Mode/objective:** 45-minute, English, diagram-led senior executive talk. An audience member should identify the score/goal gap on S20 and the two privacy risks on S21 without relying on the speaker to explain what the diagram is about.
- **Expected sequence/count:** S01–S26, S28–S46: **45 slides**, 45 paired note articles. Retire S27; do not renumber/reuse stable IDs. A split is allowed only if necessary for legibility and must be reported, not solved by type shrinking.
- **Time target:** keep43:00 speaking +2:00 reserve. Reallocate removed S27's60seconds to S20 (+20:65→85s), S21 (+20:60→80s), and replacement S33 (+20:95→115s). Section totals become8:00,4:00,14:40,9:20,7:00; total remains43:00. Recompute all cumulative elapsed times. These are pacing targets, not a rehearsal result.

## Coverage and page trail

| Comment | Baseline page/title; stable ID | Expected page | Package |
|---|---|---|---|
| C20 | p7 Access Without Authority; S07 | 7 | P6 |
| C21 | p20 Good Score, Wrong Goal; S20 | 20 | P7 |
| C22 | p21 Two Routes for Information; S21 | 21 | P7 |
| C23 | p33 A Public Issue Reached Private Repositories; S33; repository explanation on S07 and dependent notes | 32; S07 stays7 | P6/P8 |
| C24 | p27 Origin Is Not Truth; S27 | removed; S28–S46 shift back1 | P9 |

C01–C19 remain satisfied, with C24 explicitly superseding v2's provenance slide requirement. The requested 40–50-slide range remains met. No conflict requires Albert's clarification.

## Numbered, self-contained changes

### 1. P6 — S07/p7: make the destination the private webpage
- **Locations:** main S07 starts line518, destination line535; paired notes S07 starts line96, at revision baseline. `[judgment]` wording refinement, not a new architecture.
- **Must communicate:** an outside email can cause an unauthorized change to my private webpage if the same agent can read that email and change the page. This is a possible path, not an attack on Albert or a guarantee of compromise.
- **Title:** keep “Access Without Authority” unless an equally concise title makes the point clearer.
- **Current → new:** `Code repository (GitHub) / the manual's code` → **`Private webpage / my manual`**. For a coherent path, `reads email + writes code` → **`reads email + updates the page`**; `outsider's text → code change` → **`outsider's text → unwanted page change`**. Preserve “not authorized by me” and the exposure-not-proof qualifier.
- **Exhibit:** adapt the existing outside-email → agent → destination flow. Show the consequence the audience understands, not the storage technology. No new real email, screenshots or private procedures.
- **Notes/alt text:** use the webpage throughout; remove the explanation of what a repository/GitHub is. Keep the authentic separated-reader/approval/coder workflow on S08; S07 remains the hypothetical single-agent risk. E02/E04 support this; E25 may replace a supporting citation, without adding the later example here.
- **Acceptance:** the S07 picture, message, explanation, speech cues and accessibility text all end at the private manual webpage. No GitHub/repository detour. The current workflow is not conflated with the hypothetical unsafe path.
- **Dependencies:** S06 note source paragraph line93 currently recounts E06; remove that repository digression and rely on E04, or E25 by reference only. No main S06/S08 rewrite otherwise needed.

### 2. P7 — S20/p20: show how an AI can win the metric and fail the customer
- **Locations:** main S20 line797; notes S20 line245. `[judgment]` redesign the explanation, not just the title.
- **Must communicate / explicit answer to Albert:** **AI can improve its measured score while failing the real goal.** This is the wrong-target problem, not hallucination or an attack.
- **Proposed title:** **“Closed Tickets, Unsolved Problems”**.
- **Exhibit:** replace the four-row support-team table with one clearly labelled invented **AI customer-support** example. A customer asks about a missing refund. The AI is evaluated on closing requests; it marks this request closed, improving the counted result, but the refund is still missing. Visually contrast **what the score rewards: closed** with **what the customer needs: refund received**. One before/after or forked outcome diagram, not another dense table.
- **Must on main:** visible AI involvement, the scoring target, the unresolved customer outcome, an Illustration label, and a direct takeaway such as **“A better score does not guarantee a better outcome.”** Avoid another generic statement that merely says two columns differ. No invented company, percentage, trend chart or empirical result.
- **Notes:** explain the incentive mismatch in ordinary language, then the leader's check: does the measure track the outcome we actually want? “Specification gaming” can appear in notes, not as required audience jargon. No intent/consciousness claim; no suggestion that every scored AI does this.
- **Evidence:** E10/E26. This fictional scenario adapts the established concept; it is not a new report about an actual support system.
- **Layout vocabulary:** workflow/contrasted outcomes, slides decides. **Time:**85s target.
- **Acceptance:** without reading notes, a viewer can say who the AI serves, what gets counted, and why the apparent success is a failure. All note layers describe the same single example; the old four-ticket counts and implications are gone.

### 3. P7 — S21/p21: name the privacy risks, not abstract information routes
- **Locations:** main S21 line817; notes S21 line258. `[judgment]` make the examples concrete while retaining the distinction before S22.
- **Must communicate / explicit answer to Albert:** **Privacy concerns both the information you give an AI service now and information a model may reveal from earlier training.** These are different issues; today's upload is not automatically part of training.
- **Proposed title:** **“Two Different AI Privacy Risks”**.
- **Exhibit:** two plainly labelled, separate flows, without an arrow linking them:
  - **What you share now:** an illustrative confidential document → AI service → **Who can access or keep it?**
  - **What it learned earlier:** personal information in training → model → **May repeat it in an answer**.
- **Must on main:** the everyday input example, the possible output disclosure, and a compact qualifier that training use depends on the service/settings. End with a concrete takeaway such as **“Check access to inputs and disclosure in outputs.”** No suggestion that every private document is learned, every record can be extracted, or all services expose inputs.
- **Notes:** connect the first row to Albert's email reader; explain that the next slide's historical research case illustrates the second row. Distinguish processing/retention/access from training; no vendor-policy lesson or formal privacy definition. Examples are illustrations; no actual private information.
- **Evidence:** E11/E12/E22/E26, with source limits already established. **Time:**80s target.
- **Acceptance:** the title and exhibit immediately say “privacy,” the two endpoints are concrete risks rather than generic “routes,” and S22 remains a natural example of the second flow. Update diagram description, message and speech cues together.

### 4. P8 — S33/baseline p33 → expected p32: replace the case, not the platform label
- **Locations:** main S33 line1108; notes S33 line420. `[judgment]` rebuild this as the familiar web-browsing case Albert preferred.
- **Proposed title:** **“A Reddit Summary Exposed a Login Code”**.
- **Must communicate:** untrusted discussion content redirected an agent from the user's reading task into disclosing private information. Reading and acting need separate limits.
- **Exhibit:** user's request **summarize the discussion** above a simple sequence: **Reddit comment → AI browser → private email/login code → Reddit reply**. Identify Comet briefly as Perplexity's AI browser; label the case **Research demonstration ·2025** and attribute Brave. No repository, token, integration or pull-request vocabulary.
- **Evidence/limits:** E25 is the sole case authority; use its scope and source locator. Not a Reddit or Gmail platform breach, not a victim incident and not a current-patch assessment. Do not display codes, attack text, addresses or bypass steps. Prefer the conceptual sequence over the source's detailed attack video, which is inappropriate for this audience.
- **Main takeaway suggestion:** **“Permission to read is not permission to send.”**
- **Notes:** explain the diagram in the same order and identify Brave's researcher/competitor role. End with the connection to bounded permissions in Albert's workflow. Do not import E06's “Always Allow,” same-owner repositories or demonstration configuration into this different case.
- **Layout vocabulary:** workflow; slides decides. **Time:**115s target.
- **Acceptance:** a nondeveloper understands the public/private crossing from the picture. Date, source, research status and absence of a current-vulnerability claim are preserved. Main/note titles agree.

### 5. P8 — dependent notes: stop reintroducing the removed GitHub case
- **Locations:** notes S36 source paragraph line465, S37 line477, S44 line574, S45 line588 and source list, plus S06/S07 above. `[judgment]` source consistency, not extra teaching material.
- **Precise instruction:** remove E06's repository-case explanation from speaking cues and use E25 for the case callback. S45's “What can it change or send?” example must refer to the new S33, not a public issue/private repositories. For S36's permission-confirmation source, use E25's “Possible mitigations” plus E04; remove the case-specific “Always Allow” comparison. S37/S44 retain E04's scope/separation limits; E25 may support the outside-text/broad-access example.
- **Preserve:** the already corrected caveats about generated code/tool reach, allowed harmful edits, human-review failure and recommended-not-current controls. Do not turn the new source into a guarantee that confirmation alone prevents injection. “Coding agent” as Albert's own role name is allowed; no need to rename his architecture or purge legitimate source URLs unrelated to the removed teaching case.
- **Acceptance:** no GitHub lesson or old-case callback remains in main or the talk's notes. Historical job records and original request quotes are not rewritten.

### 6. P9 — retire S27 and update shared surfaces once
- **Locations:** main S27 line970 and notes S27 line346; target leaf and root outlines.
- **Must:** delete S27 **and its paired note article**. Do not move its content into another slide, appendix or hidden speaker explanation. Keep the stable-ID gap as the retirement record. This is Albert's explicit deletion, not a density migration.
- **Transition:** S26 deepfake case goes straight to S28 mistakes/attacks comparison. Keep S28's corrected acknowledgement of deliberate deception; no need for a provenance segue. Check neighbours S26/S28 and section boundary S29 for stale references.
- **Shared changes:** recompute actual slide count, visible numbering, note headings/order, pace lines/cumulative times, section table, root entry, leaf pointers/titles and plan-version reference. Default new sections: pp1–10,11–14,15–27,28–36,37–45. Correct any direct references to removed S27/C2PA content; the historical evidence entries E16/E24 remain unchanged.
- **Acceptance:**45 unique live IDs/paired articles in default implementation, S27 absent, S33 nowp32, title/contents/divider names unchanged, no stale46-page count or retired-slide pointer. Target timing above reconciles across notes and outline.

## Packages and boundaries

| Package | Owns | Dependencies |
|---|---|---|
| P6 | S07 main/note; S06 note source cleanup | E02/E04; preserve S08 approval |
| P7 | S20/S21 main/note | E10/E11/E12/E26; preserve S19 and S22 context |
| P8 | S33 main/note and S36/S37/S44/S45 note callbacks | E25; P6 uses same case source without retelling it |
| P9 | S27 retirement; numbering/timing and target/root outlines | After P6–P8; owns shared reconciliation |

Packages are ownership/coverage groups, not a request for parallel subagents. slides handles all design/wording judgments with the full request context. Keep changes local; if a shared-style change is unavoidable, report every affected page and render those too.

## Handoff and round3 review

- Copy this frozen plan-v3 unchanged; refresh living job/requests/evidence at push. Work on the existing PR82 branch; no new PR.
- Return `work-r3.md` with exact SHA, C20–C24 coverage, old/new page+stable-ID mapping including retired S27, all affected pages, timing/counts, and any deviations/plan issues. Old F01–F10 are closed; do not silently regress them.
- Run main/note lint, wordy/dense and outline checks. Render changed slides and neighbours plus any shared-style effects at1280×720 and in print; check desktop/narrow notes. Verify that larger labels, no missing glyphs and corrected factual limits survive the rewrite.
- slides-review will review the exact returned commit. This uses the remaining round3 of3; any blocking findings at that limit go to Albert, not an unannounced extra round.
- Prior approval applies only to07f519c, not to this pending revision. After approval and verified log-only finalization, update the existing PR's description/reviewed SHA. No merge unless Albert directly orders PR82 merged.
