# HandShake Protocol

## Purpose

Provide a repeatable process for Codex to continue work across devices and sessions without relying on conversation history.

## Required Project Records

Minimal recommended records:

```text
AGENTS.md
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
3. Read any nested `AGENTS.md` that applies to files being edited.
4. Read `docs/codex/INDEX.md` if present.
5. Follow the index to read status, handoff, todo, decisions, and environment records.
6. Identify the current device or environment signature from available local evidence such as hostname, OS, shell, workspace root, interpreter paths, virtual environment, package manager, and key tool versions.
7. Compare the current device with the most recent device recorded in `STATUS.md`, `HANDOFF.md`, or `ENVIRONMENT.md`.
8. Decide whether local environment facts can be reused:
   - same device and reuse allowed: perform a light sanity check before using recorded local paths or commands
   - different device, unknown device, or reuse not recorded: verify local paths, interpreters, dependencies, and commands before relying on them
9. Check for `PYTHON.md`, `PAPER.md`, or equivalent domain workflow records.
10. Check Git state when possible:
   - current branch
   - latest commit
   - staged, unstaged, and untracked files
11. Detect whether a specialized skill or project workflow applies.
12. Summarize orientation sources, device comparison, environment reuse status, and current risks before substantial edits.

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

1. Summarize completed work.
2. List changed or created files.
3. Record commands run and result summaries.
4. Record tests, lint checks, type checks, or manual verification.
5. Record decisions and rationale.
6. Record blockers and open questions.
7. Record next steps for the next session or device.
8. Record the current device, whether it matched the previous device, and whether local environment assumptions may be reused.
9. Update `STATUS.md`, `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, and `ENVIRONMENT.md` as needed.
10. Update `version/工作进度.md` and `version/版本迭代记录.md` when user-facing progress or release information changed.
11. Report Git synchronization state and local environment drift risks.

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

For Chinese-speaking users, the handoff should also leave `version/工作进度.md` readable enough to understand the current progress without reading Codex's internal management records.
