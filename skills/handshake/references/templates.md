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
- Points Codex and Claude Code to `docs/codex/INDEX.md`.
- Defines startup and minimum/conditional shutdown requirements.
- Records project-specific safety rules.

Required sections:

- Required Startup
- Required Handoff
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
- Claude Code Shutdown

## `docs/codex/INDEX.md`

Purpose:

- Entrypoint for project state.
- Lists required reading order.
- Links status, handoff, todo, decisions, and environment files.
- Explains minimum closure, conditional records, task-specific reading, and how to judge whether work can continue.

Required sections:

- New Session Reading Order
- Before Editing
- Required Closure
- Conditional Records
- Task-Specific Reading
- Current State Files
- Can Work Continue?

## `docs/codex/STATUS.md`

Purpose:

- Current objective and synchronization state.

Recommended fields:

- Last updated
- Current objective
- Current state
- Current device/environment
- Active work
- Recently completed
- Current risks
- Synchronization state
- Environment reuse status
- Next recommended step
- Last active agent and likely next agent
- Whether a commit is recommended before switching agents or devices

## `docs/codex/HANDOFF.md`

Purpose:

- Latest session handoff for the next device or Codex session.

Recommended fields:

- Date
- Current device
- Previous device comparison
- Environment reuse guidance
- Session summary
- Work completed
- Commands run
- Verification
- Decisions made
- Open questions
- Blockers
- Next steps
- Notes for next device
- Previous agent/session and recommended next agent
- Git status at handoff
- Which conditional records were updated and why

## `docs/codex/DECISIONS.md`

Purpose:

- Durable decisions that should survive across sessions.
- Only updated for durable choices, not every minor implementation detail.

Recommended fields:

- Date
- Status
- Context
- Decision
- Reason
- Consequences
- Superseded decisions
- Related files

## `docs/codex/TODO.md`

Purpose:

- Active, waiting, done, and dropped tasks.

Use checkbox lists and include blockers for active tasks. Update only when tasks are added, completed, cancelled, reprioritized, or moved between sections.

## `docs/codex/ENVIRONMENT.md`

Purpose:

- Portable setup instructions and local-only notes.
- Device identity and environment continuity records.

Rules:

- Do not record secret values.
- Prefer relative paths.
- Mark machine-specific paths as local.
- Record whether the current device matches the previous device.
- Record whether local paths, virtual environments, dependencies, and command results may be reused.
- If device identity is unknown or different, require local environment verification before command execution.
- Update only when environment, command, dependency, path, Python, virtual environment, or device facts changed.

## `docs/codex/PYTHON.md`

Purpose:

- Python-specific setup and execution records.

Recommended fields:

- Python version
- Dependency manager
- Install commands
- Run commands
- Test commands
- Lint and type-check commands
- Project layout
- Local data notes
- Environment switch notes

## `docs/codex/PAPER.md`

Purpose:

- Academic writing workflow state.

Recommended fields:

- Paper identity
- Research question
- Structure
- Chapter status
- Source verification
- Figures and tables
- Writing rules
- Writing preferences
- Last updated agent/session for chapter and source state

Rules:

- Do not invent citations.
- Mark unsupported claims as pending verification.
- Do not mark chapters complete without source or evidence status.
- Prefer Simplified Chinese for user-facing academic writing unless the user asks otherwise.
- Keep formal writing natural, readable, and suitable for graduate-student or teacher-training-student work.
- Avoid stiff AI-style prose, excessive frameworks, repetitive phrasing, unnecessary bulleting, and hollow academic wording.
- Mark unverifiable source or bibliographic details as `待人工复核`.
- Verify online-checkable and time-sensitive policy, data, journal, software, API, model, price, time, and version information when available.

## `docs/codex/PROGRESS.zh-CN.md`

Purpose:

- Short Chinese progress summary inside the operational record folder.
- Helps a human user or next AI agent quickly understand current progress.
- Does not replace `STATUS.md`, `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, `ENVIRONMENT.md`, or Git state.

Recommended fields:

- Current goal
- Current progress
- Recent work
- Blockers or risks
- Switch-agent or switch-device reminders

## `version/工作进度.md`

Purpose:

- Chinese user-facing progress summary.
- Helps the user quickly understand project progress without reading Codex's internal handoff files.

Rules:

- Keep it readable for a non-technical or semi-technical Chinese-speaking user.
- Summarize current goal, current progress, recent work, risks, and next recommendations.
- Do not treat it as Codex's source of truth.
- If it disagrees with `docs/codex/` or Git state, update it from authoritative records.

## `version/版本迭代记录.md`

Purpose:

- Chinese user-facing version history and release/change log.
- Helps the user understand version changes, impact, verification, and migration needs.

Rules:

- Prefer semantic versioning.
- Explain changes in user-facing language.
- Record verification and known risks.
- Do not treat it as Codex's source of truth.
