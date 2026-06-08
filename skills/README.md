# HandShake Skill Package

Current version:

```text
2.1.0-beta
```

This folder contains the authoritative HandShake skill package:

```text
skills/handshake/
```

The repository also keeps a root-level mirror for Codex direct GitHub installation:

```text
handshake/
```

Edit `skills/handshake/` first, then synchronize the mirror:

```text
python scripts\sync_root_mirror.py
```

## Platform Layout

| Platform | Repository entry |
| --- | --- |
| Codex | `handshake/` |
| Claude Code | `.claude-plugin/plugin.json`, `skills/handshake/`, `hooks/` |
| Cursor | `.cursor-plugin/plugin.json`, `skills/handshake/`, `hooks/` |
| Gemini CLI | `GEMINI.md` |
| OpenCode | `.opencode/INSTALL.md` |
| Generic agents | `AGENTS.md`, root `SKILL.md` |

The root `SKILL.md` is only a compatibility router. Do not treat it as the install package.

## What HandShake Does

HandShake helps AI agents continue project work across sessions, tools, computers, and local environments. Version 2.x uses a compact target-project record model:

```text
AGENTS.md
CLAUDE.md
docs/codex/INDEX.md
docs/codex/STATUS.md
version/工作进度.md
version/版本迭代记录.md
```

`docs/codex/STATUS.md` is the single AI-facing operational source of truth. `version/工作进度.md` is the Chinese user-facing progress log. `version/版本迭代记录.md` changes only when a project version or release changes.

## Initialize A Project

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --dry-run
python skills\handshake\scripts\init_project_handoff.py F:\my-project
```

## Check A Project

```text
python skills\handshake\scripts\check_project_handoff.py F:\my-project
```

## Update Installed Skill

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --force
python skills\handshake\scripts\update_installed_skill.py --source . --all --dry-run
python skills\handshake\scripts\update_installed_skill.py --source . --all --force
```

The updater accepts a repository root, `handshake/`, or `skills/handshake/` and validates the package before copying.
