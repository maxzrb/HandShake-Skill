---
name: handshake
description: Use HandShake for any non-trivial repository work that needs project continuity, startup orientation, shutdown handoff, project status, or AI agent coordination. Trigger even when the user does not name HandShake if they ask to start, continue, resume, pick up, take over, inspect status, update records, finish, close out, switch between Codex and Claude Code, change devices, change directories, change virtual environments, or work in a repo containing AGENTS.md, CLAUDE.md, docs/codex, version/工作进度.md, or version/版本迭代记录.md. Also trigger on Chinese requests such as 继续, 接手, 上次, 项目进度, 交接, 换电脑, 换环境, 收尾, 记录进度, 更新状态, Codex 接手 Claude, or Claude 接手 Codex. Maintains repository-local status, handoff, todo, decision, environment, Python, and paper-writing records.
---

# HandShake

Version: 1.8.0

Use this skill to make AI coding agent sessions portable across tools, devices, and local environments. HandShake is designed for projects that may be alternately handled by Codex and Claude Code, where the next agent must understand project state without relying on conversation history.

## Implicit Trigger Guidance

Use HandShake proactively. Do not wait for the user to explicitly say "use HandShake" when a request is about continuing repository work, checking project status, taking over prior work, switching tools or machines, changing local environments, making a non-trivial edit in a repository with HandShake records, or closing out a session.

The frontmatter `description` is the main auto-trigger surface for Codex and Claude Code before this file is loaded. Keep it broad, compact, and rich in natural trigger phrases when updating this skill.

## Quick Start

At the start of substantial work:

1. Read applicable `AGENTS.md` files.
2. In Claude Code, read `CLAUDE.md` when present. It should import `AGENTS.md` and add Claude-specific startup/shutdown reminders.
3. Read `docs/codex/INDEX.md` if present, then follow it to the status, handoff, todo, decision, and environment records.
4. If the workspace is a Git repository:
     a. Run `git pull` to synchronize with the remote before making changes.
     b. Check `git status` for branch, commit, staged, unstaged, and untracked files.
5. Identify whether this is a new AI session, Codex taking over from Claude Code, Claude Code taking over from Codex, or a cross-device/cross-environment continuation.
6. Identify the current device or local environment signature from available evidence such as hostname, OS, workspace path, active shell, Python interpreter, virtual environment, and package manager.
7. Compare the current device with the most recent device recorded in `STATUS.md`, `HANDOFF.md`, or `ENVIRONMENT.md`.
8. If the device is the same and the relevant local environment was marked reusable, local setup facts may be reused after a light sanity check. If the device is different or unknown, re-check local paths, interpreters, dependencies, and commands before relying on them.
9. Identify Python, academic writing, or project-specific workflow records.
10. If another skill has a more specific project management flow, follow it and bridge results back to the repository records.
11. Tell the user which orientation files were used and whether the local environment appears reusable before making substantial edits.
12. For non-trivial tasks, draft a phased plan and confirm with the user before implementing. Execute step by step; do not batch unrelated changes into a single step.

At the end of substantial work:

Minimum required closure:

1. Update `docs/codex/HANDOFF.md`.
2. Update `docs/codex/STATUS.md`.
3. Update `version/工作进度.md` — append a dated session entry; never overwrite previous entries.
4. Record changed files, commands run, verification results, remaining issues, and next recommended steps.
5. Record the current device, whether it matches the previous device, and whether future sessions may reuse local environment assumptions.
6. Report current Git status, whether the working tree is clean, and whether a commit is recommended before switching agents or devices.

Conditional updates:

- Update `docs/codex/TODO.md` only when tasks were added, completed, cancelled, or reprioritized.
- Update `docs/codex/DECISIONS.md` only when a durable design, architecture, dependency, or paper-writing stance was chosen.
- Update `docs/codex/ENVIRONMENT.md` only when Python version, virtual environment, dependency installation, system path, command, device, or local execution environment changed.
- Update `docs/codex/PAPER.md` or equivalent paper records only when chapter state, source state, research scope, or citation status changed.
- Update `version/版本迭代记录.md` when the project version number changed: move the old current version to history first, then write the new version. Do not delete or overwrite historical version entries.

## Phased Execution

For non-trivial work:

1. Plan first: break the task into numbered steps. Confirm the plan with the user before writing code.
2. Execute one step at a time. After each step, pause and verify the result.
3. After each completed step, remind the user: "Step N complete. Consider `git add` + `git commit` before continuing."
4. Do not batch unrelated changes into a single step. If a step grows too large, split it.

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

The initializer creates `CLAUDE.md` by default. The template imports `AGENTS.md` with `@AGENTS.md` and adds Claude Code-specific reminders without duplicating the whole rule set.

The initializer also creates:

- `docs/codex/PROGRESS.zh-CN.md` for a short Chinese progress summary inside the operational record folder.
- The Chinese progress summary under `version/`.
- The Chinese version history under `version/`.

These files are for quick human reading. Do not use them as the source of truth when `STATUS.md`, `HANDOFF.md`, task records, environment records, or Git state provide more precise evidence.

## Global Use

This skill is self-contained and can be installed into a global Codex skills directory. Keep the full `handshake/` folder together, including:

- `SKILL.md`
- `agents/openai.yaml`
- `scripts/init_project_handoff.py`
- `scripts/check_project_handoff.py`
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

After initializing a target project, Claude Code users can run `/memory` in that project to confirm whether project memory includes `CLAUDE.md`. The generated `CLAUDE.md` imports `AGENTS.md`, so both Codex-style and Claude-style entrypoints point to the same repository-local handoff records.

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

Maintain these Chinese user-facing documents with incremental updates:

- `version/工作进度.md`: append a dated session entry at the end of every substantial session. Never overwrite previous entries.
- `version/版本迭代记录.md`: when the project version number changes, move the old current version section to history first, then write the new version. Never delete or overwrite historical version entries.

Write them for a Chinese-speaking user who wants to quickly understand progress and version changes. Prefer clear summaries, short sections, and practical next steps.

Do not use these files as Codex's project management source. Codex must continue to rely on `AGENTS.md`, `docs/codex/`, the current user request, and Git state for operational decisions. If `version/` files disagree with `docs/codex/` or Git, treat the `version/` files as stale user-facing summaries and update them from the authoritative records.

See `references/templates.md` for the exact Chinese filenames.

## Missing Records

If `AGENTS.md` is missing, continue with this skill's defaults and recommend creating one for substantial work.

If `CLAUDE.md` is missing in a Claude Code workflow, continue from `AGENTS.md` and `docs/codex/INDEX.md`, then recommend running the initializer or adding the Claude entry template.

If `docs/codex/INDEX.md` is missing, inspect the repository directly and recommend initializing project state records before long-running work.

If Git is missing, continue with status files and warn that cross-device synchronization is weaker.

## Device and Environment Continuity

Treat repository records as portable, but treat local execution details as device-scoped until verified.

At startup, compare the current device or environment signature with the latest recorded device. Use practical evidence that is easy to verify in the current workspace: hostname when available, OS, shell, workspace root, Python executable, virtual environment path, package manager, and key tool versions.

If the current device matches the latest recorded device and the previous handoff says the local environment is reusable, Codex may reuse local setup assumptions after a quick sanity check. If the device differs, is unknown, or the environment reuse status is not recorded, Codex must not assume previous local paths, virtual environments, installed packages, or command results are valid.

Record device-scoped details in `docs/codex/ENVIRONMENT.md` and summarize the latest comparison in `docs/codex/HANDOFF.md`. Do not put secrets in device notes. Prefer stable labels such as "main desktop" or "office laptop" plus verifiable technical facts, not private identifiers unless the user explicitly wants them recorded.

## Domain Handling

For Python projects, look for Python version, dependency manager, setup commands, test commands, lint/type-check commands, entry points, data requirements, and local-only paths.

For academic writing projects, look for paper title, target format, chapter status, citation rules, source verification, figures/tables, data dependencies, writing preferences, and unsupported claims.

When the task is paper writing, teaching design, coursework, literature review, curriculum-standard analysis, or other formal Chinese academic writing, prefer Simplified Chinese in user-facing communication. Keep writing natural, readable, and suitable for a graduate student or teacher-training student. Avoid stiff AI-style prose, repetitive phrasing, excessive frameworks, overuse of bullet points, hollow academic wording, and fabricated citations. References, policy files, curriculum standards, journal information, data, DOI, URL, author names, titles, years, volumes, issues, and pages must be verifiable. Mark unverifiable details as `待人工复核` or state uncertainty clearly. Verify online-checkable and time-sensitive information when available before making factual claims.

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

1. Update the version in `SKILL.md`, `.claude-plugin/plugin.json` when present, `README.md`, `skills/README.md`, and `references/versioning.md` (both `skills/handshake/references/versioning.md` and the root `handshake/references/versioning.md` mirror).
2. Update both install path copies: `skills/handshake/` and the root-level `handshake/` mirror.
3. Move the previous current release entry in `references/versioning.md` under Previous Releases.
4. Run validation:
   - `python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\handshake`
   - `python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py handshake`
   - `python -m json.tool .claude-plugin\plugin.json`
   - `python skills\handshake\scripts\init_project_handoff.py outputs\handshake-init-test-<version> --all --dry-run`
   - `python skills\handshake\scripts\install_claude_skill.py --dry-run`
   - `python -m py_compile skills\handshake\scripts\init_project_handoff.py skills\handshake\scripts\check_project_handoff.py skills\handshake\scripts\install_claude_skill.py`
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
