# HandShake Skill

This folder contains the ready-to-use HandShake skill package:

```text
skills/
  handshake/
```

The repository also keeps a root-level mirror:

```text
handshake/
```

Use `skills/handshake/` for development and Claude Code plugin packaging. Use `handshake/` for direct Codex GitHub installation.

Current version:

```text
2.0.0
```

## What HandShake Does

HandShake helps Codex and Claude Code continue project work across sessions, tools, computers, and local environments. Version 2.x uses a compact record model:

```text
AGENTS.md
CLAUDE.md
docs/codex/INDEX.md
docs/codex/STATUS.md
version/工作进度.md
version/版本迭代记录.md
```

`docs/codex/STATUS.md` is the only AI-facing operational source of truth. It contains the current snapshot, TODOs, decisions, risks, environment notes when relevant, commands, verification, Git sync, and timestamped session logs.

`version/工作进度.md` is the Chinese user-facing progress log. `version/版本迭代记录.md` is updated only when a project version or release changes.

## Initialize A Project

Preview:

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --dry-run
```

Create missing files:

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project
```

Overwrite existing files only when explicitly intended:

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --force
```

## Check A Project

```text
python skills\handshake\scripts\check_project_handoff.py F:\my-project
```

The checker validates required files, the `STATUS.md` section shape, timestamped log placeholders or entries, and Git status when available.

## Update Installed Skill

Canonical repository:

```text
https://github.com/maxzrb/HandShake-Skill
```

Codex can update from GitHub:

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

Update from the remote repository on any computer:

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --force
```

`--latest` uses `https://github.com/maxzrb/HandShake-Skill.git`.

From a local clone, update the clone first, then update installed copies:

```text
git pull --ff-only
python skills\handshake\scripts\update_installed_skill.py --all --dry-run
python skills\handshake\scripts\update_installed_skill.py --all --force
```

From a downloaded GitHub zip:

```text
python skills\handshake\scripts\update_installed_skill.py --zip C:\Downloads\HandShake-Skill-main.zip --all --force
```

From an extracted repository or package folder:

```text
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main --all --force
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main\handshake --all --force
```

Single target updates:

```text
python skills\handshake\scripts\update_installed_skill.py --codex --force
python skills\handshake\scripts\update_installed_skill.py --claude --force
```

## Closeout Record Behavior

Substantial project work is recorded in `docs/codex/STATUS.md`. Each session keeps the current snapshot up to date and appends a `YYYY-MM-DD HH:MM` entry to the `Session Log` section. Chinese user-facing progress is appended to `version/工作进度.md`. `version/版本迭代记录.md` changes only when the project version or release state changes.

## Old Project Migration

If a project has older split records, migrate their useful content into `docs/codex/STATUS.md`:

- `HANDOFF.md` -> latest session log entry.
- `TODO.md` -> `Active TODO`.
- `DECISIONS.md` -> `Decisions`.
- `ENVIRONMENT.md` and `PYTHON.md` -> `Environment Notes`.
- `PAPER.md` -> writing/citation sections inside `STATUS.md`.
- `PROGRESS.zh-CN.md` -> `version/工作进度.md`.

After migration, default maintenance should only update `STATUS.md`, `version/工作进度.md`, and `version/版本迭代记录.md` when version/release state changes.

## Release Discipline

Before release, keep `skills/handshake/` and `handshake/` synchronized, validate both packages, update version references, commit, push the branch, create an annotated tag, and push the tag.
