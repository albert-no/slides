# Logs

**Pipeline jobs (from 2026-11-10).** `log/PIPELINE.md` is the contract between the **slides-review** (planning, review, PR) and **slides** (authoring) agents.

- `log/jobs/<job-id>/` — slides-review's working folder. Untracked (`.gitignore`).
- `log/<job-id>/` — the tracked record on the job branch: an unchanged copy of the job files plus slides' work reports. It reaches `main` with the PR and is the permanent log.
- Job files only. No chat transcripts, raw session output or hidden reasoning.

**Older per-PR transcripts (before 2026-11-10).** `YYYY-MM-DD-<pr-summary>.md`: every message between the two agents during that PR, verbatim, in order, with Asia/Seoul timestamps. Kept as history; no new ones are written.
