# HandShake Protocol

## Purpose

Provide a repeatable process for Codex, Claude Code, or another AI coding agent to continue work across tools, devices, directories, virtual environments, and sessions without relying on conversation history.

## Required Project Records

Minimal recommended records:

```text
AGENTS.md
CLAUDE.md
docs/codex/
  INDEX.md
  STATUS.md
  HANDOFF.md
```

Expanded records:

```text
docs/codex/
  DECISIONS.md
  TODO.md
  ENVIRONMENT.md
  PYTHON.md
  PAPER.md
```

User-facing summaries:

```text
version/
  工作进度.md
  版本迭代记录.md
```

The `version/` files are readable Chinese summaries for users. They are not authoritative project management records for Codex.

## Startup Workflow

1. Identify the workspace root and current working directory.
2. Read root `AGENTS.md` if present.
3. In Claude Code, read `CLAUDE.md` if present. It should import `AGENTS.md` and add Claude-specific reminders.
4. Read any nested `AGENTS.md` that applies to files being edited.
5. Read `docs/codex/INDEX.md` if present.
6. Follow the index to read status, handoff, todo, decisions, and environment records.
7. Determine the takeover scenario:
   - new AI session taking over an existing project
   - Codex taking over from Claude Code
   - Claude Code taking over from Codex
   - same tool continuing after a session break
   - cross-device, cross-directory, or changed-virtual-environment continuation
8. Identify the current device or environment signature from available local evidence such as hostname, OS, shell, workspace root, interpreter paths, virtual environment, package manager, and key tool versions.
9. Compare the current device with the most recent device recorded in `STATUS.md`, `HANDOFF.md`, or `ENVIRONMENT.md`.
10. Decide whether local environment facts can be reused:
   - same device and reuse allowed: perform a light sanity check before using recorded local paths or commands
   - different device, unknown device, or reuse not recorded: verify local paths, interpreters, dependencies, and commands before relying on them
11. Check for `PYTHON.md`, `PAPER.md`, or equivalent domain workflow records.
12. Check Git state when possible:
   - current branch
   - latest commit
   - staged, unstaged, and untracked files
13. Detect whether a specialized skill or project workflow applies.
14. Summarize orientation sources, device comparison, environment reuse status, and current risks before substantial edits.

Do not use `version/工作进度.md` or `version/版本迭代记录.md` as startup source-of-truth files. Read them only when the user specifically asks about user-facing progress/version summaries or when updating those summaries.

## Work Rules

- Follow the current user request first.
- Preserve user changes.
- Avoid destructive Git commands unless explicitly requested.
- Prefer existing project patterns and commands.
- Record meaningful state changes as they happen.
- Keep sensitive values out of repository files.
- Use environment variable names instead of secret values.
- Treat local execution details as device-scoped unless the current device has been matched and the handoff explicitly allows reuse.

## Shutdown Workflow

Before ending substantial work:

Minimum required closure:

1. Update `docs/codex/HANDOFF.md`.
2. Update `docs/codex/STATUS.md`.
3. Record completed work, changed or created files, commands run, result summaries, verification, remaining issues, and next steps.
4. Record the current device, whether it matched the previous device, and whether local environment assumptions may be reused.
5. Report Git synchronization state, whether the working tree is clean, and whether a commit is recommended before switching tools or devices.

Conditional updates:

- Update `docs/codex/TODO.md` only when tasks were created, completed, cancelled, reprioritized, or moved between active/waiting/done/dropped.
- Update `docs/codex/DECISIONS.md` only when durable project decisions were made, including architecture, dependency, workflow, or paper-writing stance decisions.
- Update `docs/codex/ENVIRONMENT.md` only when device identity, Python version, virtual environment, dependency state, setup path, system path, or run/test command availability changed.
- Update `docs/codex/PAPER.md` or equivalent writing records only when chapter status, source verification, research scope, figures/tables, or citation state changed.
- Update `version/工作进度.md` and `version/版本迭代记录.md` only when user-facing progress, milestone, release, or version information changed.

## Conflict Handling

### Current User Request vs. Stored State

The current user request wins. Record meaningful deviations in `HANDOFF.md`.

### `AGENTS.md` vs. Skill Defaults

`AGENTS.md` wins when explicit. This skill supplies fallback behavior.

### Specialized Workflow vs. General Handoff

Use the specialized workflow for execution. Still update common handoff records, or cross-link to the specialized records if they are equivalent.

### Status Records vs. Git State

Git is authoritative for file history and changed files. Status records are authoritative for intent and handoff context. If they disagree, update status records after inspecting the current state.

### User-Facing Version Files vs. Project Records

The `version/` files are derived summaries. If they disagree with `docs/codex/` or Git state, treat them as stale and update them from the authoritative project records.

### Local Environment vs. Portable Setup

Machine-local notes may override local execution on that device, but portable setup instructions must remain available.

Local environment notes from one device must not be applied to another device until verified. If the current device cannot be confidently matched to the previous device, treat local paths, virtual environments, installed tools, and previous command results as stale until checked.

## Missing File Behavior

If `AGENTS.md` is missing:

- Continue with this skill.
- Recommend creating `AGENTS.md` for substantial work.

If `CLAUDE.md` is missing in a Claude Code workflow:

- Continue from `AGENTS.md` and `docs/codex/INDEX.md`.
- Recommend adding the generated `CLAUDE.md` template so Claude Code imports the same project rules.

If `docs/codex/INDEX.md` is missing:

- Inspect the repository directly.
- Recommend initializing `docs/codex/`.

If Git is missing:

- Continue with status files.
- Warn that cross-device synchronization depends on external file sync or manual transfer.

## Completion Standard

A handoff is complete when a new Codex session can answer:

- What is the current goal?
- What changed last?
- What files matter?
- What commands were run?
- What is verified?
- What remains blocked?
- What should happen next?
- Which device was used last?
- Can local environment assumptions be reused on the current device?
- Is the next agent expected to be Codex, Claude Code, or either one?

For Chinese-speaking users, the handoff should also leave `version/工作进度.md` readable enough to understand the current progress without reading Codex's internal management records.
