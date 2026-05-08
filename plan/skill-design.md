# Skill Design: handshake

## Skill Name

`handshake`

## Purpose

Guide Codex through a strict cross-device project handoff workflow for Python development, academic writing, and mixed projects.

## Trigger Description

Use when Codex needs to continue, inspect, initialize, or update a project across multiple computers, sessions, branches, or environments; when the user mentions handoff, project state, `AGENTS.md`, cross-device development, Python project continuity, academic writing continuity, or Codex workflow management; or when Codex must maintain repository-local status records for progress, decisions, tasks, environment notes, and release/version discipline.

## Package Location

```text
skills/handshake/
```

## Planned Structure

```text
skills/handshake/
  SKILL.md
  agents/
    openai.yaml
  scripts/
    init_project_handoff.py
  assets/
    project-template/
      AGENTS.md
      docs/codex/*.md
  references/
    protocol.md
    templates.md
    versioning.md
```

## Version

Current version:

```text
1.2.0
```

Rationale:

- `1.2.0` adds device/environment continuity checks so Codex can decide whether local setup assumptions can be reused across sessions.
- `1.1.2` updates repository URLs after the GitHub repository rename to `HandShake-Skill`.
- The workflow is considered the first named usable release.
- Breaking changes after `1.0.0` require a future major version bump.

## Release Policy

Use semantic versioning:

- `MAJOR`: breaking workflow changes.
- `MINOR`: backward-compatible workflow additions.
- `PATCH`: clarifications, typo fixes, and non-behavioral edits.

Every release must:

- State the version.
- Include a changelog entry or release note.
- Keep released versions immutable in practice.
- Document migration notes for breaking changes.
- Verify referenced files and templates before release.

## Core Workflow

### Startup Checklist

Codex must:

1. Read applicable `AGENTS.md` files.
2. Read `docs/codex/INDEX.md` when present.
3. Read linked status, handoff, todo, decision, and environment records.
4. Check Git state when Git is available.
5. Identify the current device/environment and compare it with the latest recorded device.
6. Decide whether local setup facts can be reused or must be rechecked.
7. Detect domain-specific records such as `PYTHON.md` and `PAPER.md`.
8. Detect specialized skills or project workflows.
9. Summarize orientation sources and environment reuse status before substantial edits.

### Work Execution Rules

Codex must:

- Follow the current user request first.
- Preserve user changes.
- Prefer existing project workflow when explicit.
- Keep records current when decisions, tasks, or state change.
- Avoid storing secrets.
- Record evidence for completed work.

### Shutdown Checklist

Codex must:

1. Update latest handoff.
2. Update status when project state changed.
3. Update todos when tasks changed.
4. Update decisions when durable choices were made.
5. Record commands and verification.
6. Record blockers and next steps.
7. Record the current device and environment reuse guidance.
8. Report synchronization risks.

### Initialization Script

The skill includes:

```text
scripts/init_project_handoff.py
```

The script copies bundled templates from:

```text
assets/project-template/
```

Required behavior:

- Default target is the current directory.
- Default mode creates missing required files and skips existing files.
- `--python` includes the Python workflow template.
- `--paper` includes the academic writing workflow template.
- `--all` includes all optional domain templates.
- `--dry-run` previews changes.
- `--force` overwrites existing files only when explicitly requested.

The script also creates `version/工作进度.md` and `version/版本迭代记录.md` by default. These are Chinese user-facing summaries, not Codex source-of-truth files.

### Global Use

The skill package must be self-contained. A user should be able to copy the full `handshake/` folder into a global Codex skills directory and use it from any target project.

## References

### `references/protocol.md`

Contains the detailed handoff algorithm, priority rules, conflict handling, and missing-file fallback behavior.

### `references/templates.md`

Contains repository template content and file purpose summaries.

### `references/versioning.md`

Contains the versioning and release rules for management workflow skills.

## Validation Plan

Validate against:

- Empty project with no Git repository.
- Git project with uncommitted changes.
- Python project with dependency and test commands.
- Academic writing project with source verification needs.
- Project with existing specialized workflow.

## Known Constraints

- A skill cannot force Codex to trigger itself unless the user request or description matches.
- `AGENTS.md` is required for repository-carried mandatory behavior.
- Cross-device consistency still depends on Git or another file synchronization mechanism.
- The skill should not become a large project database; status files own project facts.
