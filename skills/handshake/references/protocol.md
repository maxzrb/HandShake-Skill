# HandShake Protocol

## Purpose

Provide a repeatable process for Codex, Claude Code, or another AI coding agent to continue work across tools, devices, directories, virtual environments, and sessions without relying on conversation history.

HandShake 2.x keeps the operational model intentionally small: one AI-facing status file plus two Chinese user-facing records.

## Required Project Records

Default records:

```text
AGENTS.md
CLAUDE.md
docs/codex/
  INDEX.md
  STATUS.md
version/
  工作进度.md
  版本迭代记录.md
```

`docs/codex/STATUS.md` is the only AI-facing source of truth. It contains:

- A current snapshot near the top.
- Active TODOs.
- Current risks and blockers.
- Durable decisions.
- Environment notes when relevant.
- Commands and verification.
- Git synchronization state.
- A timestamped session log appended at the end.

`version/工作进度.md` is a Chinese user-facing progress log. It mirrors the important progress from `STATUS.md` in readable Chinese and also appends timestamped entries at the end.

`version/版本迭代记录.md` is a Chinese user-facing release/version record and is updated only when the project version or release state changes.

Do not use split default records such as `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, `ENVIRONMENT.md`, `PROGRESS.zh-CN.md`, `PYTHON.md`, or `PAPER.md`. When an old project contains those files, migrate useful content into `STATUS.md`.

## Startup Workflow

1. Identify the workspace root and current working directory.
2. Read root `AGENTS.md` if present.
3. In Claude Code, read `CLAUDE.md` if present. It should import `AGENTS.md` and add Claude-specific reminders.
4. Read any nested `AGENTS.md` that applies to files being edited.
5. Read `docs/codex/INDEX.md` if present.
6. Read `docs/codex/STATUS.md` as the mandatory operational source of truth. Do not rely on `INDEX.md` alone.
7. Determine the takeover scenario:
   - new AI session taking over an existing project
   - Codex taking over from Claude Code
   - Claude Code taking over from Codex
   - same tool continuing after a session break
   - cross-device, cross-directory, or changed-virtual-environment continuation
8. Check local environment details only when the request, command execution, `STATUS.md`, or a failure mode makes them relevant.
9. If Git is available:
   a. Run `git pull` to synchronize with the remote before making changes.
   b. Check current branch, latest commit, staged, unstaged, and untracked files.
   c. If the pull reveals new remote commits, review them before editing.
10. Detect whether a specialized skill or project workflow applies.
11. Summarize orientation sources, current snapshot, Git status, and current risks before substantial edits.
12. For non-trivial tasks, draft a phased plan and confirm with the user unless the user already gave clear implementation direction. Execute step by step; do not batch unrelated changes into one step.

Do not use `version/工作进度.md` or `version/版本迭代记录.md` as startup source-of-truth files. Read them only when the user specifically asks about user-facing progress/version summaries or when updating those summaries.

## Work Rules

- Follow the current user request first.
- Preserve user changes.
- Avoid destructive Git commands unless explicitly requested.
- When Git is available, run `git pull` before starting work to avoid working from an outdated local repository.
- For non-trivial tasks, plan in phases, confirm the plan when needed, then execute step by step.
- After completing each execution step, remind the user to consider a git commit before continuing.
- Prefer existing project patterns and commands.
- Record meaningful state changes in `STATUS.md`.
- Append incrementally to `STATUS.md` and user-facing `version/` records; never overwrite previous log entries.
- Every substantial `STATUS.md` and `version/工作进度.md` log entry must use `YYYY-MM-DD HH:MM` timestamps.
- Keep sensitive values out of repository files.
- Use environment variable names instead of secret values.
- Treat local execution details as device-scoped unless they have been verified in the current environment.

## Shutdown Workflow

Before ending substantial work:

1. Update the current snapshot in `docs/codex/STATUS.md`.
2. Append a timestamped session log entry to the end of `STATUS.md`.
3. Record completed work, changed or created files, commands run, result summaries, verification, TODO changes, decisions, risks, blockers, remaining issues, next steps, and Git status.
4. Append a timestamped user-facing entry to the end of `version/工作进度.md`.
5. Update `version/版本迭代记录.md` only when the project version or release changed.
6. Report Git synchronization state, whether the working tree is clean, and whether a commit is recommended before switching tools or devices.

The `STATUS.md` update is mandatory. If it cannot be updated, the agent must state the reason and must not claim the handoff is complete.

## Conflict Handling

### Current User Request vs. Stored State

The current user request wins. Record meaningful deviations in `STATUS.md`.

### `AGENTS.md` vs. Skill Defaults

`AGENTS.md` wins when explicit. This skill supplies fallback behavior.

### Specialized Workflow vs. General Status

Use the specialized workflow for execution. Still update `STATUS.md` with the outcome, or cross-link to equivalent records if the user explicitly requires another record system.

### Status Records vs. Git State

Git is authoritative for file history and changed files. `STATUS.md` is authoritative for intent, tasks, decisions, and handoff context. If they disagree, inspect the current state and update `STATUS.md`.

### User-Facing Version Files vs. Project Records

The `version/` files are derived summaries. If they disagree with `STATUS.md` or Git state, treat them as stale and update them from authoritative records.

### Local Environment vs. Portable Setup

Machine-local notes may guide local execution on that device, but portable setup instructions must remain available in `STATUS.md` when they matter.

Local environment notes from one device must not be applied to another device until verified. If the current device cannot be confidently matched to the previous device, treat local paths, virtual environments, installed tools, and previous command results as stale until checked.

## Missing File Behavior

If `AGENTS.md` is missing:

- Continue with this skill.
- Recommend creating `AGENTS.md` for substantial work.

If `CLAUDE.md` is missing in a Claude Code workflow:

- Continue from `AGENTS.md` and `docs/codex/STATUS.md`.
- Recommend adding the generated `CLAUDE.md` template so Claude Code imports the same project rules.

If `docs/codex/INDEX.md` is missing:

- Read `docs/codex/STATUS.md` directly if present.
- Recommend initializing the current HandShake templates.

If `docs/codex/STATUS.md` is missing:

- Inspect the repository directly.
- Recommend initializing or migrating HandShake records before long-running work.

If Git is missing:

- Continue with `STATUS.md`.
- Warn that cross-device synchronization depends on external file sync or manual transfer.

## Completion Standard

A HandShake closeout is complete when a new Codex or Claude Code session can answer from `STATUS.md`:

- What is the current goal?
- What changed last?
- What files matter?
- What commands were run?
- What is verified?
- What TODOs are active or completed?
- What decisions are durable?
- What remains blocked?
- What should happen next?
- Is any environment recheck required?
- What is the current Git sync state?

For Chinese-speaking users, `version/工作进度.md` should also be readable enough to understand current progress without reading Codex's internal management record.
