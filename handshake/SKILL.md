---
name: handshake
description: Use HandShake when Codex needs to continue, inspect, initialize, or update project work across multiple computers, Codex sessions, branches, or local environments; when the user mentions handoff, project state, AGENTS.md, cross-device development, Python project continuity, academic writing continuity, or Codex workflow management; or when Codex must maintain repository-local records for progress, decisions, tasks, environment notes, and strict versioned release discipline for management workflow skills.
---

# HandShake

Version: 1.4.0

Use this skill to make Codex sessions portable across devices. The skill defines how to start from repository-local records, continue work without prior conversation history, and leave a clear handoff for the next session.

## Quick Start

At the start of substantial work:

1. Read applicable `AGENTS.md` files.
2. Read `docs/codex/INDEX.md` if present.
3. Read the linked status, handoff, todo, decision, and environment records.
4. Check Git state if the workspace is a Git repository.
5. Identify the current device or local environment signature from available evidence such as hostname, OS, workspace path, active shell, Python interpreter, virtual environment, and package manager.
6. Compare the current device with the most recent device recorded in `STATUS.md`, `HANDOFF.md`, or `ENVIRONMENT.md`.
7. If the device is the same and the relevant local environment was marked reusable, local setup facts may be reused after a light sanity check. If the device is different or unknown, re-check local paths, interpreters, dependencies, and commands before relying on them.
8. Identify Python, academic writing, or project-specific workflow records.
9. If another skill has a more specific project management flow, follow it and bridge results back to the repository records.
10. Tell the user which orientation files were used and whether the local environment appears reusable before making substantial edits.

At the end of substantial work:

1. Update `docs/codex/HANDOFF.md`.
2. Update `docs/codex/STATUS.md` when project state changed.
3. Update `docs/codex/TODO.md` when task status changed.
4. Update `docs/codex/DECISIONS.md` when durable decisions were made.
5. Record commands run, verification results, blockers, and next steps.
6. Record the current device, whether it matches the previous device, and whether future sessions may reuse local environment assumptions.
7. Update the Chinese user-facing progress and version summaries under `version/` when meaningful progress or release information changed.
8. Report synchronization risks such as uncommitted changes, missing Git history, or local environment drift.

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
- `scripts/install_claude_skill.py`
- `assets/project-template/`
- `references/`

For Claude Code plugin use, keep the repository root `.claude-plugin/plugin.json` with the repository-level `skills/handshake/` directory.

After global installation, use this skill in any project that needs cross-device handoff, then run the initialization script against the target project when repository-local records are missing.

## Repository Install Paths

This repository intentionally exposes the same skill package in two locations:

1. `handshake/`: root-level mirror for Codex GitHub installers or agents that check the repository root and `<repo>/handshake/` first.
2. `skills/handshake/`: Claude Code plugin skill path and the original repository package path.

Keep these two directories synchronized for every release. If an installer reports that the skill is not in the repository root or `handshake/`, treat that as a packaging regression and restore the root-level `handshake/` mirror before release.

## Claude Code Use

HandShake also works as a Claude Code skill because it uses the Agent Skills `SKILL.md` layout. Claude Code can use it in three ways:

1. Standalone personal skill: copy the full `skills/handshake/` directory to `~/.claude/skills/handshake/`, then invoke it with `/handshake`.
2. Standalone project skill: copy the full `skills/handshake/` directory to `<project>/.claude/skills/handshake/`, then invoke it with `/handshake` inside that project.
3. Plugin during development: from this repository root, start Claude Code with `claude --plugin-dir .`, then invoke it with `/handshake-skill:handshake`.

The helper installer can create a standalone Claude Code skill:

```text
python scripts/install_claude_skill.py --dry-run
python scripts/install_claude_skill.py --force
python scripts/install_claude_skill.py --project <target-project> --force
```

When Claude Code needs to run the bundled project initializer from an installed skill, use the skill directory path rather than assuming the current working directory is the skill directory:

```text
python "${CLAUDE_SKILL_DIR}/scripts/init_project_handoff.py" <target-project> --all
```

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

## Device and Environment Continuity

Treat repository records as portable, but treat local execution details as device-scoped until verified.

At startup, compare the current device or environment signature with the latest recorded device. Use practical evidence that is easy to verify in the current workspace: hostname when available, OS, shell, workspace root, Python executable, virtual environment path, package manager, and key tool versions.

If the current device matches the latest recorded device and the previous handoff says the local environment is reusable, Codex may reuse local setup assumptions after a quick sanity check. If the device differs, is unknown, or the environment reuse status is not recorded, Codex must not assume previous local paths, virtual environments, installed packages, or command results are valid.

Record device-scoped details in `docs/codex/ENVIRONMENT.md` and summarize the latest comparison in `docs/codex/HANDOFF.md`. Do not put secrets in device notes. Prefer stable labels such as "main desktop" or "office laptop" plus verifiable technical facts, not private identifiers unless the user explicitly wants them recorded.

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

## Release Push Checklist

When releasing this skill repository, do not stop after `git push`. Complete the branch push and tag push as one release flow:

1. Update the version in `SKILL.md`, `.claude-plugin/plugin.json` when present, `README.md`, `skills/README.md`, and `references/versioning.md`.
2. Update both install path copies: `skills/handshake/` and the root-level `handshake/` mirror.
3. Move the previous current release entry in `references/versioning.md` under Previous Releases.
4. Run validation:
   - `python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\handshake`
   - `python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py handshake`
   - `python -m json.tool .claude-plugin\plugin.json`
   - `python skills\handshake\scripts\init_project_handoff.py outputs\handshake-init-test-<version> --all --dry-run`
   - `python skills\handshake\scripts\install_claude_skill.py --dry-run`
   - `python -m py_compile skills\handshake\scripts\init_project_handoff.py skills\handshake\scripts\install_claude_skill.py`
   - `git diff --check`
5. Commit the release changes with a versioned message.
6. Push the branch, usually with `git push`.
7. Create an annotated release tag on the release commit: `git tag -a v<version> -m "Release HandShake <version>"`.
8. Push the tag: `git push origin v<version>`.
9. Verify the remote branch and tag:
   - `git status --short --branch`
   - `git log -1 --oneline --decorate`
   - `git ls-remote --tags origin v<version>`

If a release commit was pushed without a tag, immediately add the missing annotated tag to that exact release commit and push the tag before making the next release commit.

See `references/versioning.md` before changing this skill's workflow.

## References

- Read `references/protocol.md` when applying the full startup, shutdown, conflict, or fallback workflow.
- Read `references/templates.md` when creating or updating project-local `AGENTS.md` or `docs/codex/` records.
- Read `references/versioning.md` when releasing or changing a management workflow skill.
