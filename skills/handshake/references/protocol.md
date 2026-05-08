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

## Startup Workflow

1. Identify the workspace root and current working directory.
2. Read root `AGENTS.md` if present.
3. Read any nested `AGENTS.md` that applies to files being edited.
4. Read `docs/codex/INDEX.md` if present.
5. Follow the index to read status, handoff, todo, decisions, and environment records.
6. Check for `PYTHON.md`, `PAPER.md`, or equivalent domain workflow records.
7. Check Git state when possible:
   - current branch
   - latest commit
   - staged, unstaged, and untracked files
8. Detect whether a specialized skill or project workflow applies.
9. Summarize orientation sources and current risks before substantial edits.

## Work Rules

- Follow the current user request first.
- Preserve user changes.
- Avoid destructive Git commands unless explicitly requested.
- Prefer existing project patterns and commands.
- Record meaningful state changes as they happen.
- Keep sensitive values out of repository files.
- Use environment variable names instead of secret values.

## Shutdown Workflow

Before ending substantial work:

1. Summarize completed work.
2. List changed or created files.
3. Record commands run and result summaries.
4. Record tests, lint checks, type checks, or manual verification.
5. Record decisions and rationale.
6. Record blockers and open questions.
7. Record next steps for the next session or device.
8. Update `STATUS.md`, `HANDOFF.md`, `TODO.md`, and `DECISIONS.md` as needed.
9. Report Git synchronization state.

## Conflict Handling

### Current User Request vs. Stored State

The current user request wins. Record meaningful deviations in `HANDOFF.md`.

### `AGENTS.md` vs. Skill Defaults

`AGENTS.md` wins when explicit. This skill supplies fallback behavior.

### Specialized Workflow vs. General Handoff

Use the specialized workflow for execution. Still update common handoff records, or cross-link to the specialized records if they are equivalent.

### Status Records vs. Git State

Git is authoritative for file history and changed files. Status records are authoritative for intent and handoff context. If they disagree, update status records after inspecting the current state.

### Local Environment vs. Portable Setup

Machine-local notes may override local execution on that device, but portable setup instructions must remain available.

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
