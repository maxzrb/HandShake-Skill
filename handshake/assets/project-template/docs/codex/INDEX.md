# AI Handoff Index

This directory stores project-local state for Codex and Claude Code handoff across sessions, tools, devices, directories, and local environments.

## New Session Reading Order

1. `AGENTS.md`
2. `CLAUDE.md` when using Claude Code
3. `docs/codex/STATUS.md`
4. `docs/codex/HANDOFF.md`
5. `docs/codex/TODO.md`
6. `docs/codex/DECISIONS.md`
7. `docs/codex/ENVIRONMENT.md`

## Before Editing

- Check `git status`.
- Identify whether this is a new session, Codex taking over from Claude Code, Claude Code taking over from Codex, or a cross-device/cross-environment continuation.
- Compare the current device, workspace path, Python interpreter, virtual environment, package manager, and important commands with the latest records.
- If the device or environment is different or unknown, verify commands locally before relying on previous results.
- Read task-specific records before touching files.

## Required Closure

At the end of substantial work, always update:

- `HANDOFF.md`: what changed, files touched, commands run, verification, remaining issues, next steps.
- `STATUS.md`: current objective, current state, active work, sync state, environment reuse.

The final reply should tell the user whether `git status` is clean and whether a commit is recommended before switching agents or devices.

## Conditional Records

- `TODO.md`: update only when tasks are added, completed, cancelled, reprioritized, or moved between sections.
- `DECISIONS.md`: update only for durable design, architecture, dependency, workflow, or paper-writing stance choices.
- `ENVIRONMENT.md`: update only when Python version, virtual environment, dependency installation, system path, run/test commands, device, or local execution environment changes.
- `PAPER.md`: update for paper-writing projects when chapter state, source state, research scope, figures/tables, or citation status changes.
- `PYTHON.md`: update for Python projects when setup, dependency, run, test, lint, type-check, entry point, or data requirements change.
- `PROGRESS.zh-CN.md`: update when a Chinese quick progress summary would help the next human or AI reader.
- `version/工作进度.md` and `version/版本迭代记录.md`: update only when user-facing progress, milestone, or release information changes.

## Task-Specific Reading

- Code task: read `STATUS.md`, `HANDOFF.md`, `TODO.md`, `DECISIONS.md`, and `ENVIRONMENT.md`; read `PYTHON.md` when Python is involved.
- Python environment task: read `ENVIRONMENT.md` and `PYTHON.md`, then verify local interpreter and virtual environment state.
- Paper-writing task: read `PAPER.md`, `DECISIONS.md`, and current citation/source notes before writing.
- Cross-device continuation: read `ENVIRONMENT.md` and the device section in `HANDOFF.md` before running commands.
- Agent switch: read `HANDOFF.md` first, then confirm whether the previous work was done by Codex, Claude Code, or a human.

## Current State Files

- [Status](STATUS.md)
- [Handoff](HANDOFF.md)
- [Todo](TODO.md)
- [Decisions](DECISIONS.md)
- [Environment](ENVIRONMENT.md)
- [中文进度摘要](PROGRESS.zh-CN.md)
- [Python](PYTHON.md)
- [Paper](PAPER.md)

## Can Work Continue?

Work can continue when:

- The latest `STATUS.md` and `HANDOFF.md` are understandable.
- Git state is known.
- Current environment assumptions are either verified or marked for recheck.
- Active tasks and blockers are visible in `TODO.md` or `HANDOFF.md`.
- The next concrete action is clear.

If any of these are missing, inspect the repository directly, update the records you can verify, and tell the user what remains uncertain.
