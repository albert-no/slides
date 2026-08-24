# Pre-slim snapshot — 2026-08-23

Verbatim copies of the authoring docs as they stood before the token-economy
rewrite (branch `docs-slim-2026-08`).

| File | Bytes before | Why it was rewritten |
|---|---|---|
| `CLAUDE.md` | 12,130 | Token rules existed but were buried and unenforceable. |
| `DESIGN_SYSTEM.md` | 67,689 | Read cover-to-cover 91 times in one month (~1.51M tokens). |
| `GOTCHAS.md` | 42,059 | Read cover-to-cover 68 times (~0.70M tokens). |
| `.claude-commands/*.md` | — | Slash commands that told agents to "read DESIGN_SYSTEM.md". |

Measured from the agent transcripts for the `slides` group, 2026-07-24 → 08-21:
these two files alone accounted for ~2.21M tokens of tool payload, ~16% of all
context the agent consumed, and 9.5x everything spent on web search and fetch.

Nothing here is live. `git log` is the real history; this folder exists so the
prior wording can be diffed without checking out an old commit.
