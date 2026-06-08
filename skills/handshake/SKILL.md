---
name: handshake
description: Use HandShake for non-trivial repository work that needs project continuity, startup orientation, status logging, closeout records, AI agent coordination, multi-platform skill/plugin adaptation, or updating/upgrading the HandShake skill itself. Trigger even when the user does not name HandShake if they ask to start, continue, resume, pick up, take over, inspect status, update records, finish, close out, update HandShake skill, upgrade installed skill, switch between Codex, Claude Code, Cursor, Gemini CLI, OpenCode, or other coding agents, change devices, change directories, change virtual environments, or work in a repo containing AGENTS.md, CLAUDE.md, GEMINI.md, docs/codex/STATUS.md, version/工作进度.md, or version/版本迭代记录.md. Also trigger on Chinese requests such as 继续, 接手, 上次, 项目进度, 交接, 换电脑, 换环境, 收尾, 记录进度, 更新状态, 更新 HandShake skill, 更新 handshake skill, 升级 HandShake, Codex 接手 Claude, or Claude 接手 Codex. Maintains one repository-local AI status log plus Chinese user-facing progress and version records.
---

# HandShake

Version: 2.1.0-beta

Use this skill to make AI coding agent sessions portable across tools, devices, and local environments without forcing a heavy multi-file handoff system. HandShake keeps the AI-facing operational state in one required file, `docs/codex/STATUS.md`, and keeps Chinese user-facing summaries under `version/`.

## Implicit Trigger Guidance

Use HandShake proactively. Do not wait for the user to explicitly say "use HandShake" when a request is about continuing repository work, checking project status, taking over prior work, switching tools or machines, changing local environments, making a non-trivial edit in a repository with HandShake records, or closing out a session.

The frontmatter `description` is the main auto-trigger surface for Codex, Claude Code, Cursor, Gemini CLI, OpenCode, and similar agents before this file is loaded. Keep it broad, compact, and rich in natural trigger phrases when updating this skill.

## Required Record Model

Default project records:

```text
AGENTS.md
CLAUDE.md
docs/codex/INDEX.md
docs/codex/STATUS.md
version/工作进度.md
version/版本迭代记录.md
```

Rules:

- `docs/codex/STATUS.md` is the only AI-facing source of truth for project state.
- `STATUS.md` must contain a current snapshot near the top and a timestamped session log at the end.
- Agents must append new log entries at the end of `STATUS.md`; do not overwrite prior log entries.
- Each log entry must use a date plus time timestamp so same-day operations remain ordered.
- Tasks, TODOs, durable decisions, blockers, environment notes, commands, verification, file changes, and Git sync state all belong in `STATUS.md`.
- `version/工作进度.md` is the Chinese user-facing progress log. It follows the same append-at-end timestamp discipline, but uses user-readable wording.
- `version/版本迭代记录.md` is updated only when a project version or release changes.
- Do not create separate default `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, `ENVIRONMENT.md`, `PROGRESS.zh-CN.md`, `PYTHON.md`, or `PAPER.md` records. Migrate old projects into the new `STATUS.md` structure instead.

## Quick Start

At the start of substantial work:

1. Read applicable `AGENTS.md` files.
2. In Claude Code, read `CLAUDE.md` when present. It should import `AGENTS.md` and add Claude-specific startup/shutdown reminders.
3. Read `docs/codex/INDEX.md` if present.
4. Read `docs/codex/STATUS.md` as the operational source of truth.
5. If the workspace is a Git repository:
   a. Run `git pull` to synchronize with the remote before making changes.
   b. Run `git status` to inspect branch, commit, staged, unstaged, and untracked files.
6. Identify whether this is a new AI session, Codex taking over from Claude Code, Claude Code taking over from Codex, same-tool continuation, cross-device continuation, or changed-environment continuation.
7. Check environment details only when the task involves execution, Python, dependencies, changed paths, changed devices, changed virtual environments, or `STATUS.md` says recheck is required.
8. Identify Python, academic writing, or project-specific workflow needs and record their state inside `STATUS.md`.
9. Tell the user which orientation files were used and the current Git/workflow risk before making substantial edits.
10. For non-trivial tasks, draft a phased plan and confirm with the user before implementing. Execute step by step; do not batch unrelated changes into one step.

At the end of substantial work:

1. Update `docs/codex/STATUS.md`.
2. Append a timestamped log entry to the end of `STATUS.md` using `YYYY-MM-DD HH:MM`.
3. Update the snapshot sections near the top of `STATUS.md` so the next agent can orient quickly without reading the whole log.
4. Record completed work, changed files, commands run, verification results, TODO changes, durable decisions, blockers, remaining issues, next recommended steps, and Git status.
5. Append a timestamped user-facing entry to `version/工作进度.md`.
6. Update `version/版本迭代记录.md` only when the project version or release changed.
7. Report current Git status, whether the working tree is clean, and whether a commit is recommended before switching agents or devices.

The status update is mandatory for substantial work. If the agent cannot update `STATUS.md`, it must say why before claiming the task is complete.

## Phased Execution

For non-trivial work:

1. Plan first: break the task into numbered steps. Confirm the plan with the user before writing code, unless the user has already given clear implementation direction.
2. Execute one step at a time. After each step, verify the result.
3. After each completed step, remind the user: "Step N complete. Consider `git add` + `git commit` before continuing."
4. Do not batch unrelated changes into a single step. If a step grows too large, split it.
5. Before the final reply, update `STATUS.md` and `version/工作进度.md` or explicitly report why the record update could not be completed.

## Initialize a Project

When the user asks to initialize HandShake records in a target project, run the bundled script from this skill:

```text
python scripts/init_project_handoff.py <target-project>
```

Use options as needed:

- `--dry-run`: preview changes.
- `--force`: overwrite existing target files only when the user explicitly asks.

Default behavior creates only missing required files and skips existing files.

The initializer creates `CLAUDE.md` by default. The template imports `AGENTS.md` with `@AGENTS.md` and adds Claude Code-specific reminders without duplicating the whole rule set.

For old projects with previous HandShake files, migrate the useful content from `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, `ENVIRONMENT.md`, `PROGRESS.zh-CN.md`, `PYTHON.md`, and `PAPER.md` into the appropriate sections of `docs/codex/STATUS.md`. Do not keep the old split-file structure as the default workflow.

## Global Use

This skill is self-contained and can be installed into a global Codex skills directory. Keep the full `handshake/` folder together, including:

- `SKILL.md`
- `agents/openai.yaml`
- `scripts/init_project_handoff.py`
- `scripts/check_project_handoff.py`
- `scripts/install_claude_skill.py`
- `scripts/update_installed_skill.py`
- `assets/project-template/`
- `references/`

For Claude Code and Cursor plugin use, keep the repository root plugin manifests with the repository-level `skills/handshake/` directory and `hooks/` directory.

After global installation, use this skill in any project that needs cross-session continuity, then run the initialization script against the target project when repository-local records are missing.

## Update Installed Skill

Canonical repository:

```text
https://github.com/maxzrb/HandShake-Skill
```

Codex can update directly from GitHub with the root-level package path:

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

When working from any computer, an agent can update installed copies from the remote repository:

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --force
```

`--latest` uses the canonical repository `https://github.com/maxzrb/HandShake-Skill.git`.

If the repository has already been cloned on that computer, update the clone, then copy the package into installed skill directories:

```text
git pull --ff-only
python skills\handshake\scripts\update_installed_skill.py --all --force
```

If the user downloaded a GitHub zip archive instead of cloning the repository, install from that archive:

```text
python skills\handshake\scripts\update_installed_skill.py --zip C:\Downloads\HandShake-Skill-main.zip --all --force
```

If the archive has already been extracted, install from the extracted repository folder or from a package folder:

```text
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main --all --force
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main\handshake --all --force
```

Use narrower targets when needed:

```text
python skills\handshake\scripts\update_installed_skill.py --codex --force
python skills\handshake\scripts\update_installed_skill.py --claude --force
python skills\handshake\scripts\update_installed_skill.py --target C:\Users\maxzr\.codex\skills\handshake --force
```

Always preview destructive updates when uncertain:

```text
python skills\handshake\scripts\update_installed_skill.py --all --dry-run
```

The update script validates that the source contains a HandShake skill package before copying. With `--repo`, it clones or pulls into `~/.codex/skill-sources/HandShake-Skill` by default, then updates installed copies from that cache.

## Repository Install Paths

This repository intentionally exposes the same skill package in two locations:

1. `handshake/`: root-level mirror for Codex GitHub installers or agents that check the repository root and `<repo>/handshake/` first.
2. `skills/handshake/`: authoritative development package and plugin skill path for Claude Code, Cursor, and similar runtimes.

Keep these two directories synchronized for every release. If an installer reports that the skill is not in the repository root or `handshake/`, treat that as a packaging regression and restore the root-level `handshake/` mirror before release.

The repository root may also contain a compatibility `SKILL.md` for platforms that inspect the root first. Do not install that wrapper as the package source; use `handshake/` or `skills/handshake/`.

## Multi-Platform Use

HandShake uses the Agent Skills `SKILL.md` layout and exposes platform entry files:

- Codex: install the root-level `handshake/` package from GitHub.
- Claude Code: use standalone `~/.claude/skills/handshake/` or load the repository with `.claude-plugin/plugin.json`.
- Cursor: load the repository with `.cursor-plugin/plugin.json` when plugin support is available.
- Gemini CLI: read `GEMINI.md`, which routes to `skills/handshake/SKILL.md`.
- OpenCode: read `.opencode/INSTALL.md` and route to `skills/handshake/SKILL.md`.

Claude Code can use HandShake in three ways:

1. Standalone personal skill: copy the full `skills/handshake/` directory to `~/.claude/skills/handshake/`, then invoke it with `/handshake`.
2. Standalone project skill: copy the full `skills/handshake/` directory to `<project>/.claude/skills/handshake/`, then invoke it with `/handshake` inside that project.
3. Plugin during development: from this repository root, start Claude Code with `claude --plugin-dir .`, then invoke it with `/handshake-skill:handshake`.

The plugin manifests point to:

```text
skills: ./skills/
hooks: ./hooks/hooks.json or ./hooks/hooks-cursor.json
```

The session-start hook calls `hooks/session_start.py` and injects only lightweight routing context. Agents should still read the current `SKILL.md`, `AGENTS.md`, and project-local `docs/codex/STATUS.md` when the workflow requires them.

The helper installer can create a standalone Claude Code skill:

```text
python scripts/install_claude_skill.py --dry-run
python scripts/install_claude_skill.py --force
python scripts/install_claude_skill.py --project <target-project> --force
```

When Claude Code needs to run the bundled project initializer from an installed skill, use the skill directory path rather than assuming the current working directory is the skill directory:

```text
python "${CLAUDE_SKILL_DIR}/scripts/init_project_handoff.py" <target-project>
```

After initializing a target project, Claude Code users can run `/memory` in that project to confirm whether project memory includes `CLAUDE.md`. The generated `CLAUDE.md` imports `AGENTS.md`, so both Codex-style and Claude-style entrypoints point to the same repository-local status record.

## Instruction Priority

Use this priority order:

1. Current user request.
2. System and developer instructions.
3. Project `AGENTS.md`.
4. Specialized project or domain skill.
5. Project `docs/codex/STATUS.md`.
6. This skill's defaults.

If a specialized workflow conflicts with this skill, use the specialized workflow for execution and still record the resulting state in `STATUS.md`.

## User-Facing Version Documents

Maintain these Chinese user-facing documents with incremental updates:

- `version/工作进度.md`: append a dated time-stamped entry at the end of every substantial session. Never overwrite previous entries.
- `version/版本迭代记录.md`: when the project version number changes, move the old current version section to history first, then write the new version. Never delete or overwrite historical version entries.

Write them for a Chinese-speaking user who wants to quickly understand progress and version changes. Prefer clear summaries, short sections, and practical next steps.

Do not use these files as Codex's project management source. Codex must continue to rely on `AGENTS.md`, `docs/codex/STATUS.md`, the current user request, and Git state for operational decisions. If `version/` files disagree with `STATUS.md` or Git, treat the `version/` files as stale user-facing summaries and update them from authoritative records.

See `references/templates.md` for the exact Chinese filenames.

## Missing Records

If `AGENTS.md` is missing, continue with this skill's defaults and recommend creating one for substantial work.

If `CLAUDE.md` is missing in a Claude Code workflow, continue from `AGENTS.md` and `docs/codex/STATUS.md`, then recommend running the initializer or adding the Claude entry template.

If `docs/codex/STATUS.md` is missing, inspect the repository directly and recommend initializing or migrating HandShake records before long-running work.

If Git is missing, continue with `STATUS.md` and warn that cross-device synchronization is weaker.

## Device and Environment Continuity

HandShake 2.x does not record environment facts by default. Environment details are recorded inside `STATUS.md` only when they matter for the work.

Record environment notes when:

- The user says they changed devices, directories, Python interpreters, virtual environments, package managers, dependencies, or run/test commands.
- A command fails because of local setup.
- A future agent must recheck a local-only path, installed tool, generated output location, or environment variable name.

Do not store secrets. Use environment variable names instead of secret values.

## Domain Handling

For Python projects, record Python version, dependency manager, setup commands, test commands, lint/type-check commands, entry points, and data requirements in the relevant sections of `STATUS.md`.

For academic writing projects, record paper title, target format, chapter status, citation rules, source verification, figures/tables, data dependencies, writing preferences, and unsupported claims in `STATUS.md`.

When the task is paper writing, teaching design, coursework, literature review, curriculum-standard analysis, or other formal Chinese academic writing, prefer Simplified Chinese in user-facing communication. Keep writing natural, readable, and suitable for a graduate student or teacher-training student. Avoid stiff AI-style prose, repetitive phrasing, excessive frameworks, overuse of bullet points, hollow academic wording, and fabricated citations. References, policy files, curriculum standards, journal information, data, DOI, URL, author names, titles, years, volumes, issues, and pages must be verifiable. Mark unverifiable details as `待人工复核` or state uncertainty clearly. Verify online-checkable and time-sensitive information when available before making factual claims.

For mixed projects, keep code state and writing state as separate sections inside `STATUS.md` when one depends on the other.

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
   - `python skills\handshake\scripts\init_project_handoff.py outputs\handshake-init-test-<version> --dry-run`
   - `python skills\handshake\scripts\install_claude_skill.py --dry-run`
   - `python skills\handshake\scripts\update_installed_skill.py --latest --all --dry-run`
   - `python -m py_compile skills\handshake\scripts\init_project_handoff.py skills\handshake\scripts\check_project_handoff.py skills\handshake\scripts\install_claude_skill.py skills\handshake\scripts\update_installed_skill.py`
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
- Read `references/templates.md` when creating or updating project-local records.
- Read `references/versioning.md` when releasing or changing a management workflow skill.
