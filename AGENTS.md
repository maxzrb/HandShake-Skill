# HandShake Skill Repository Instructions

This repository develops the HandShake skill/plugin package. HandShake is a multi-agent continuity workflow for Codex, Claude Code, Cursor, Gemini CLI, OpenCode, and similar coding agents.

## Repository Shape

- `skills/handshake/` is the authoritative development package.
- `handshake/` is the root-level mirror for direct Codex GitHub installation.
- `SKILL.md` at the repository root is a compatibility entry for runtimes that look at the repository root first. Do not treat it as the package source for installers.
- `.claude-plugin/` and `.cursor-plugin/` hold plugin manifests.
- `hooks/` holds lightweight session-start context injection for plugin-capable platforms.
- `.codex/INSTALL.md`, `.opencode/INSTALL.md`, `CLAUDE.md`, and `GEMINI.md` are platform entry instructions.

## Startup

Before substantial work:

1. Read this file.
2. Read `CLAUDE.md` when running in Claude Code.
3. Read `skills/handshake/SKILL.md` as the authoritative behavior.
4. Read `skills/handshake/references/versioning.md` before changing workflow behavior, package layout, or release metadata.
5. Run `git pull --ff-only` when Git is available.
6. Run `git status --short --branch` before editing.

If repository-local HandShake records are present, also read `docs/codex/STATUS.md`. If they are missing, inspect the repository directly and create/update the records before closing substantial work.

## Editing Rules

- Edit `skills/handshake/` first, then run `python scripts/sync_root_mirror.py` to refresh `handshake/`.
- Keep package behavior synchronized across `SKILL.md`, `agents/openai.yaml`, scripts, references, plugin manifests, and README files.
- Do not manually edit `handshake/` unless fixing a mirror-only emergency; mirror drift is a packaging bug.
- Do not add platform instructions that require secrets or local-only absolute paths.
- Keep root `SKILL.md` concise. Put durable behavior in `skills/handshake/SKILL.md`.

## Validation

Run the relevant checks after changes:

```text
python scripts/sync_root_mirror.py --check
python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\handshake
python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py handshake
python -m json.tool .claude-plugin\plugin.json
python -m json.tool .cursor-plugin\plugin.json
python -m json.tool hooks\hooks.json
python -m json.tool hooks\hooks-cursor.json
python -m py_compile skills\handshake\scripts\init_project_handoff.py skills\handshake\scripts\check_project_handoff.py skills\handshake\scripts\install_claude_skill.py skills\handshake\scripts\update_installed_skill.py hooks\session_start.py
git diff --check
```

For installer changes, also run:

```text
python skills\handshake\scripts\update_installed_skill.py --source . --target %TEMP%\handshake-install-test\skills\handshake --dry-run
python skills\handshake\scripts\update_installed_skill.py --source . --target %TEMP%\handshake-install-test\skills\handshake --force
```

## Release Discipline

Use semantic versioning for workflow/package changes. Use pre-release labels such as `2.1.0-beta` for uncommitted or runtime-unverified adaptation builds. Update both skill copies, plugin manifests, README files, and `skills/handshake/references/versioning.md` for releases. Do not call a release complete until the branch and matching annotated tag have both been pushed.
