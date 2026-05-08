---
name: handshake
description: Use HandShake when Codex needs to continue, inspect, initialize, or update project work across multiple computers, Codex sessions, branches, or local environments; when the user mentions handoff, project state, AGENTS.md, cross-device development, Python project continuity, academic writing continuity, or Codex workflow management; or when Codex must maintain repository-local records for progress, decisions, tasks, environment notes, and strict versioned release discipline for management workflow skills.
---

# HandShake

Version: 1.1.0

Use this skill to make Codex sessions portable across devices. The skill defines how to start from repository-local records, continue work without prior conversation history, and leave a clear handoff for the next session.

## Quick Start

At the start of substantial work:

1. Read applicable `AGENTS.md` files.
2. Read `docs/codex/INDEX.md` if present.
3. Read the linked status, handoff, todo, decision, and environment records.
4. Check Git state if the workspace is a Git repository.
5. Identify Python, academic writing, or project-specific workflow records.
6. If another skill has a more specific project management flow, follow it and bridge results back to the repository records.
7. Tell the user which orientation files were used before making substantial edits.

At the end of substantial work:

1. Update `docs/codex/HANDOFF.md`.
2. Update `docs/codex/STATUS.md` when project state changed.
3. Update `docs/codex/TODO.md` when task status changed.
4. Update `docs/codex/DECISIONS.md` when durable decisions were made.
5. Record commands run, verification results, blockers, and next steps.
6. Update the Chinese user-facing progress and version summaries under `version/` when meaningful progress or release information changed.
7. Report synchronization risks such as uncommitted changes or missing Git history.

## Initialize a Project

When the user asks to initialize handoff records in a target project, run the bundled script from this skill:

```text
python scripts/init_project_handoff.py <target-project>
```

Use options as needed:

- `--python`: include `docs/codex/PYTHON.md`.
- `--paper`: include `docs/codex/PAPER.md`.
- `--all`: include all optional domain templates.
- `--dry-run`: preview changes.
- `--force`: overwrite existing target files only when the user explicitly asks.

Default behavior creates only missing required files and skips existing files.

The initializer also creates:

- The Chinese progress summary under `version/`.
- The Chinese version history under `version/`.

These files are for human readers. Do not use them as Codex's source of truth.

## Global Use

This skill is self-contained and can be installed into a global Codex skills directory. Keep the full `handshake/` folder together, including:

- `SKILL.md`
- `agents/openai.yaml`
- `scripts/init_project_handoff.py`
- `assets/project-template/`
- `references/`

After global installation, use this skill in any project that needs cross-device handoff, then run the initialization script against the target project when repository-local records are missing.

## Instruction Priority

Use this priority order:

1. Current user request.
2. System and developer instructions.
3. Project `AGENTS.md`.
4. Specialized project or domain skill.
5. Project files under `docs/codex/`.
6. This skill's defaults.

If a specialized workflow conflicts with this skill, use the specialized workflow for execution and still update or cross-link the common handoff records.

## User-Facing Version Documents

Maintain these Chinese user-facing documents when the target project has meaningful progress, release, or milestone changes:

- the progress summary under `version/`
- the version history under `version/`

Write them for a Chinese-speaking user who wants to quickly understand progress and version changes. Prefer clear summaries, short sections, and practical next steps.

Do not use these files as Codex's project management source. Codex must continue to rely on `AGENTS.md`, `docs/codex/`, the current user request, and Git state for operational decisions. If `version/` files disagree with `docs/codex/` or Git, treat the `version/` files as stale user-facing summaries and update them from the authoritative records.

See `references/templates.md` for the exact Chinese filenames.

## Missing Records

If `AGENTS.md` is missing, continue with this skill's defaults and recommend creating one for substantial work.

If `docs/codex/INDEX.md` is missing, inspect the repository directly and recommend initializing project state records before long-running work.

If Git is missing, continue with status files and warn that cross-device synchronization is weaker.

## Domain Handling

For Python projects, look for Python version, dependency manager, setup commands, test commands, lint/type-check commands, entry points, data requirements, and local-only paths.

For academic writing projects, look for paper title, target format, chapter status, citation rules, source verification, figures/tables, data dependencies, and unsupported claims.

For mixed projects, keep code state and writing state separate but link them in the latest handoff when one depends on the other.

## Version Discipline

Management workflow skills must be released by explicit version number and follow version control principles.

Use semantic versioning unless a project selects a stricter scheme:

- Increment `MAJOR` for breaking workflow changes.
- Increment `MINOR` for backward-compatible workflow additions.
- Increment `PATCH` for clarifications, typo fixes, and non-behavioral edits.

Every release must record the version, release date, changes, compatibility notes, and any migration notes. Released versions must not be silently rewritten; publish a new version for corrections.

See `references/versioning.md` before changing this skill's workflow.

## References

- Read `references/protocol.md` when applying the full startup, shutdown, conflict, or fallback workflow.
- Read `references/templates.md` when creating or updating project-local `AGENTS.md` or `docs/codex/` records.
- Read `references/versioning.md` when releasing or changing a management workflow skill.
