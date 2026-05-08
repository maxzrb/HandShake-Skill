# Project Instructions for Codex

## Required Startup

Before substantial work, Codex must:

1. Read this file.
2. Read `docs/codex/INDEX.md`.
3. Read the latest project status and handoff files linked from the index.
4. Check Git status when this is a Git repository.
5. Compare the current device/environment with the latest recorded device in `STATUS.md`, `HANDOFF.md`, or `ENVIRONMENT.md`.
6. If the device is different or unknown, verify local paths, interpreters, virtual environments, dependencies, and commands before relying on previous environment notes.
7. Report the orientation files used and whether the local environment appears reusable before editing.

## Required Handoff

Before ending substantial work, Codex must update the project handoff records under `docs/codex/`.

At minimum, update:

- `docs/codex/STATUS.md` when current state changes.
- `docs/codex/HANDOFF.md` with completed work, changed files, verification, blockers, and next steps.
- `docs/codex/TODO.md` when task status changes.
- `docs/codex/ENVIRONMENT.md` when device identity, local paths, virtual environments, dependency state, or command availability changes.

Codex should also update these Chinese user-facing summaries when meaningful progress or version information changed:

- `version/工作进度.md`
- `version/版本迭代记录.md`

These two files are for users to read. Codex project management must not depend on them.

## Workflow Priority

Use this priority order:

1. Current user request.
2. System and developer instructions.
3. This `AGENTS.md`.
4. Specialized project or domain skill.
5. Files under `docs/codex/`.
6. General cross-device handoff skill defaults.

If a specialized workflow has its own management records, use that workflow but keep `docs/codex/` updated or clearly cross-linked.

Do not treat `version/工作进度.md` or `version/版本迭代记录.md` as authoritative project state. They are derived summaries for Chinese-speaking users.

## Safety

- Do not overwrite user changes.
- Do not run destructive Git commands unless explicitly requested.
- Do not store secrets in repository files.
- Record local-only paths as local notes, not portable setup instructions.
- Do not reuse local environment assumptions from another device until they have been verified on the current device.

## Versioning

Management workflow skills and templates used by this project must be released by explicit version number and follow version control principles.
