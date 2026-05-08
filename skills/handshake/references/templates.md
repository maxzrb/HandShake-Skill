# Project Record Templates

Use these summaries when creating project-local records. Keep templates concise and adapt them to the project.

The full copyable template set is bundled at:

```text
assets/project-template/
```

Use `scripts/init_project_handoff.py` to copy these templates into a target project.

## `AGENTS.md`

Purpose:

- Mandatory repository-carried instructions.
- Points Codex to `docs/codex/INDEX.md`.
- Defines startup and shutdown requirements.
- Records project-specific safety rules.

Required sections:

- Required Startup
- Required Handoff
- Workflow Priority
- Safety
- Versioning

## `docs/codex/INDEX.md`

Purpose:

- Entrypoint for project state.
- Lists required reading order.
- Links status, handoff, todo, decisions, and environment files.

Required sections:

- Required Reading Order
- Optional Domain Files
- Current State Files
- Rules

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

## `docs/codex/DECISIONS.md`

Purpose:

- Durable decisions that should survive across sessions.

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

Use checkbox lists and include blockers for active tasks.

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

Rules:

- Do not invent citations.
- Mark unsupported claims as pending verification.
- Do not mark chapters complete without source or evidence status.

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
