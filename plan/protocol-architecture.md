# Protocol Architecture

## Layer Model

The handoff system has four layers.

### 1. Codex Skill Layer

Purpose:

- Provides the reusable operating procedure.
- Tells Codex how to discover project records.
- Defines startup and shutdown checklists.
- Provides fallback behavior for projects without local rules.
- Defines versioned release rules for management workflow skills.

The skill should stay general and should not store project-specific state.

### 2. Repository Rule Layer

Primary file:

- `AGENTS.md`

Purpose:

- Stores mandatory rules that travel with the repository.
- Tells Codex where the project state entrypoint is.
- Defines project-specific commands and constraints.
- Overrides the general skill where the project requires stricter behavior.

`AGENTS.md` should be short. It should point to detailed status files instead of duplicating them.

### 3. Project State Layer

Primary directory:

- `docs/codex/`

Purpose:

- Stores current progress, decisions, tasks, environment notes, and handoff records.
- Gives a new Codex session enough context to continue work without conversation history.
- Stores evidence of completed work and verification.

### 4. Domain Workflow Layer

Examples:

- Python development workflow.
- Academic writing workflow.
- Existing project-specific management skill.
- Existing research-writing skill.

Purpose:

- Adds domain-specific rules.
- May replace parts of the general handoff flow when more precise.
- Must still bridge back to project-local records.

## File Map

```text
AGENTS.md
docs/codex/
  INDEX.md
  STATUS.md
  HANDOFF.md
  DECISIONS.md
  TODO.md
  ENVIRONMENT.md
  PYTHON.md
  PAPER.md
```

Only `INDEX.md`, `STATUS.md`, and `HANDOFF.md` are required for a minimal project. Other files are optional but recommended when relevant.

## Startup Algorithm

1. Identify workspace root.
2. Read `AGENTS.md` from the workspace root if present.
3. If operating in a subdirectory, check for nested `AGENTS.md` files that apply to the edited files.
4. Find `docs/codex/INDEX.md`.
5. If `INDEX.md` exists, follow its links to status, handoff, decisions, todos, and environment files.
6. If `INDEX.md` does not exist, search for obvious project state files before falling back to general inspection.
7. Check whether the workspace is a Git repository.
8. If Git exists, inspect branch, last commit, and working tree status.
9. Detect applicable domain files such as `PYTHON.md` or `PAPER.md`.
10. Detect whether another skill or project workflow has explicit management rules.
11. Summarize orientation sources before substantial edits.

## Shutdown Algorithm

1. Summarize work completed.
2. Record files changed or created.
3. Record commands run and verification results.
4. Record decisions made.
5. Record blockers and open questions.
6. Record next recommended action.
7. Update `STATUS.md` if current project state changed.
8. Update `HANDOFF.md` with latest handoff.
9. Update `TODO.md` if tasks changed.
10. If Git exists, report whether changes are committed, staged, unstaged, or untracked.

## Conflict Rules

### User Request vs. Stored State

The current user request wins. Record any meaningful deviation from stored state in `HANDOFF.md`.

### `AGENTS.md` vs. Skill Defaults

`AGENTS.md` wins when it is explicit. The skill supplies fallback behavior only.

### Specialized Workflow vs. General Handoff Skill

Use the specialized workflow for domain-specific execution. Still update the common project state files unless the specialized workflow defines an equivalent state record.

### Status Files vs. Git State

Git state is authoritative for code history and file changes. Status files are authoritative for intent, rationale, and handoff context. If they disagree, update status files to reflect the current Git state and record the mismatch.

### Local Environment vs. Repository Records

Machine-local environment notes may override setup commands for that PC, but they must be clearly marked local. Do not make local-only paths the only reproducible setup path.

## Missing File Behavior

If `AGENTS.md` is missing:

- Continue using the skill defaults.
- Recommend creating `AGENTS.md` when project work is substantial.

If `docs/codex/INDEX.md` is missing:

- Continue with repository inspection.
- Recommend creating the state directory before long-running work.

If Git is missing:

- Continue using status files.
- Warn that cross-device synchronization is weaker.
- Do not assume commit history exists.

## Data Safety

Status files must not contain:

- API keys or tokens.
- Passwords.
- Private credentials.
- Sensitive unpublished data unless the repository is private and the user explicitly accepts that.
- Full local absolute paths unless marked as machine-specific.

Use environment variable names instead of secret values.

## Versioned Skill Release Flow

Management workflow skills must follow this release process:

1. Update the explicit version.
2. Update the changelog or version reference.
3. Validate the skill structure.
4. Verify all referenced files exist.
5. Record compatibility and breaking changes.
6. Publish or tag the release according to the selected version control strategy.

Released versions must be immutable in practice. Corrections require a new version.
