# Slide jobs — contract between slides-review and slides

Lives at `log/PIPELINE.md`. slides-review owns each job (size, research, plan, review, PR). slides does the slide work. Albert is the final check and the only one who orders a merge.

## Job folders

A job has two folders with the same name, `<job-id>`, which is `YYYY-MM-DD-<deck>-<slug>`, e.g. `2026-11-12-lec11-watermark-feedback`.

- **Working folder** `log/jobs/<job-id>/`: written only by slides-review. Never tracked by git (`log/jobs/` is in `.gitignore`).
- **Tracked record** `log/<job-id>/` on the job branch: written only by slides. It holds an unchanged copy of the working folder plus the work reports. This is what reaches `main` with the PR.

Keeping the two apart is deliberate: an untracked file at a path that a merged branch also tracks makes `git pull` on `main` abort.

| File | Writer and place | Contents |
|---|---|---|
| `job.md` | slides-review, working folder | Header (below), and for a small job the request and the spec too |
| `requests.md` | slides-review, working folder | Albert's request or comments, verbatim, each with an ID (`C01`…). Never edited after it is written; later comments are appended |
| `evidence.md` | slides-review, working folder | Claim and source register (`E01`…). Medium and large jobs |
| `plan.md` | slides-review, working folder | The plan, with a revision number. Slide-level specs and packages (`P1`…) |
| `work-rN.md` | slides, tracked record | Work report for round N |
| `review-rN.md` | slides-review, working folder | Review of round N |

Each file has one writer. The other agent reads it and never edits it. slides reads the working folder directly. slides-review reads the tracked record through git at the commit slides names. A small job needs only `job.md`, `work-r1.md` and `review-r1.md`.

The files are the messages. Messages between the agents are one-line pointers: `job <job-id>: <file> ready — <state>`, plus the commit SHA when slides hands over work. Do not copy chat transcripts, raw session output or hidden reasoning into any file.

## `job.md` header

```
job: <job-id>
size: small | medium | large
deck: <path to the deck>
audience / mode / duration: <for new decks and restructures>
baseline: <commit>
branch: <job branch>
state: <state>
round: <N> of <limit>
albert decisions: <dated list: approvals, answers, merge order>
```

## States

`planning` → `awaiting-albert` (large jobs: scope and outline approval) → `ready-for-work` → `in-work` → `in-review` → `revise` (back to `in-work`) → `approved` → `pr-open` → `merged` or `closed`. `escalated` when the round limit is reached or the agents disagree on a blocking point.

Only slides-review changes `state`. It sets `in-work` when it sends the work order and `in-review` when it receives the work pointer. Round limits: small 1, medium 2, large 3.

The branch name is the `<job-id>`. slides creates it from `baseline`; slides-review records it in `job.md`.

## IDs

- **Comments** `C01`…: one per comment from Albert, in `requests.md`.
- **Evidence** `E01`…: one per source-backed claim, in `evidence.md`.
- **Slides** `S01`…: a `data-slide-id` attribute on each slide. slides adds them the first time a deck enters a job, in a commit that changes nothing else. IDs are never renumbered. A split of `S07` gives `S07a`, `S07b`. A new slide takes the next free number, and the plan states its position ("`S57`, after `S07`"). The matching `<article>` in the note file carries the same ID; slides adds both in the same ID-only commit.
- **Packages** `P1`…: groups of slides one worker can do alone.
- **Findings** `F01`…: one per review finding; numbering continues across rounds.

Albert gives feedback by page number, so keep the trail: comment → baseline page and title → slide ID → new page.

## `plan.md`

1. **Summary**: what changes and why, in a few lines. For a large job: audience, objectives, argument, title sequence, time budget.
2. **Coverage table** (medium and large): `comment | baseline page / title | slide IDs | package`.
3. **Slide specs**, one per slide ID:
   - point (one line) and proposed title
   - required content, with the qualifiers the claim needs
   - exhibit: what the visual is and how to read it
   - evidence IDs
   - what goes on the slide, in the note, in the tech supplement
   - suggested layout (component name only) and time
   - acceptance check
   - marked **must**, **prefer**, or **slides decides**
4. **Packages**: for each, the slide IDs, the files and note sections it may touch, and what it depends on.
5. **Shared surfaces**: Contents, dividers, totals, `OUTLINE.md`, recap, cross-references. slides does these after merging the packages.

A plan says what each slide must communicate. It does not prescribe markup, CSS, pixel values or font sizes. Slide counts and layouts are targets; `DESIGN_SYSTEM.md` wins over the plan.

## `evidence.md`

Per entry: the claim; the source with version, and page, section or figure; the setup behind any number; what the source does not establish; and a label: published result, our calculation, illustrative example, or unresolved. For a generated figure, record the inputs, parameters and the path of the code that regenerates it, inside the repo.

## `work-rN.md`

- branch and head commit
- per package: what was done
- slide mapping: `slide ID | old page | new page | split or moved`
- deviations from the plan, each with the reason
- plan issues: anything that needs a decision from slides-review (argument, required content, facts, scope, time)
- unsourced facts found
- checks run: lint result, which slides were render-checked
- for round 2 and later: each finding ID and what was done about it

## `review-rN.md`

- reviewed commit
- verdict: `approved` or `revise`
- coverage: each comment ID, done or not
- findings: `ID | slide ID / page | type | blocking | what is wrong | fix`. Types: fact, unmet request, design rule, preference
- plan changes made in response to slides' plan issues

Only blocking findings start another round. Review order: Albert's request, the sources, the design rules, then the plan.

## Git, PR and merge

- slides owns branches, commits and pushes. It copies a working-folder file into the tracked record, unchanged, when it receives the `ready` pointer for that file, and commits it with its next push. slides-review announces a file only when it is complete and does not change an announced file afterwards; a changed plan gets a new revision number and a new pointer.
- slides-review reviews a named commit, read through git on its read-only mount (`git show <sha>:<path>`, `git diff main...<sha>`, `git archive <sha>` into scratch space to render). Approval is pinned to that commit.
- After `approved`, slides copies the final review into the tracked record and pushes. slides-review confirms that the commits after the reviewed one touch only `log/<job-id>/`, then opens the PR against `main` through the GitHub API.
- **Nobody merges unless Albert directly orders the merge of that PR.** One order, one PR.
- After the merge, slides-review may delete its working folder. The tracked record is the permanent log.

## Slack

Agents do not post in Slack for agent-to-agent work. Only slides-review reports to Albert, and each post starts with `[<job-id>]`. If Albert asks either agent about a job in its own channel, it answers him there, briefly. slides may render PDFs for its own checks but does not send them to Albert; slides-review sends one only when Albert asks.

## Direct requests

Edits Albert asks slides for directly in #claw-slides are outside this contract: no job folder, no slides-review review, and slides opens the PR. If Albert asks for a review of one, slides-review opens a small job for it. The merge rule applies to every PR.
