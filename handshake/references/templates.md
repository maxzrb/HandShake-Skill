# Project Record Templates

Use these summaries when creating project-local records. Keep templates concise and adapt them to the project.

The full copyable template set is bundled at:

```text
assets/project-template/
```

Use `scripts/init_project_handoff.py` to copy these templates into a target project.

## `AGENTS.md`

Purpose:

- Mandatory repository-carried instructions for AI coding agents.
- Points Codex and Claude Code to `docs/codex/INDEX.md` and `docs/codex/STATUS.md`.
- Defines startup, mandatory status logging, shutdown, safety, and versioning requirements.
- Forces substantial work to be recorded in the repository.

Required sections:

- Required Startup
- Required Status Logging
- Required Closeout
- Workflow Priority
- Safety
- Versioning

## `CLAUDE.md`

Purpose:

- Claude Code entrypoint.
- Imports `AGENTS.md` with `@AGENTS.md` so rules are not duplicated.
- Adds Claude-specific startup, shutdown, and Chinese-response reminders.

Required sections:

- Claude Code Startup
- Claude Code Closeout

## `docs/codex/INDEX.md`

Purpose:

- Entrypoint for project state.
- Points agents to the single AI-facing operational record.
- Explains required reading order, required closeout, migration of old split files, and how to judge whether work can continue.

Required sections:

- Mandatory Status Entry
- New Session Reading Order
- Before Editing
- Required Closeout
- Old Record Migration
- Can Work Continue?

## `docs/codex/STATUS.md`

Purpose:

- Single AI-facing source of truth for current project state, TODOs, decisions, environment notes, commands, verification, Git sync, and chronological session logs.

Recommended sections:

- Current Snapshot
- Active TODO
- Recently Completed
- Decisions
- Risks And Blockers
- Environment Notes
- Verification And Commands
- Git Sync
- Next Recommended Step
- Session Log

Rules:

- Keep the current snapshot short and current.
- Append each session entry to the end of `Session Log`.
- Use `YYYY-MM-DD HH:MM` timestamps in every session entry.
- Record changed files, commands, verification, TODO changes, durable decisions, risks, blockers, and next steps in the entry.
- Do not create separate default `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, `ENVIRONMENT.md`, `PROGRESS.zh-CN.md`, `PYTHON.md`, or `PAPER.md` files. Fold those concerns into `STATUS.md`.

## `version/工作进度.md`

Purpose:

- Chinese user-facing progress log.
- Helps the user quickly understand project progress without reading Codex's internal status file.
- Uses the same timestamped append-at-end log discipline as `STATUS.md`.

Rules:

- Keep it readable for a Chinese-speaking user.
- Append a new timestamped entry at the end for every substantial session; never overwrite previous log entries.
- Summarize current goal, current progress, recent work, risks, and next recommendations.
- Do not treat it as Codex's source of truth.
- If it disagrees with `STATUS.md` or Git state, update it from authoritative records.

## `version/版本迭代记录.md`

Purpose:

- Chinese user-facing version history and release/change log.
- Helps the user understand version changes, impact, verification, and migration needs.
- Accumulates version entries over time; older versions move to the historical section.

Rules:

- Prefer semantic versioning.
- When publishing a new version: copy the current version section to the top of historical versions, write the new version info in current version, and never delete or overwrite historical entries.
- Explain changes in user-facing language.
- Record verification and known risks.
- Do not treat it as Codex's source of truth.
