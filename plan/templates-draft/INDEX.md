# Codex Project State Index

This directory stores project-local state for Codex handoff across devices and sessions.

## Required Reading Order

1. `STATUS.md`
2. `HANDOFF.md`
3. `TODO.md`
4. `DECISIONS.md`
5. `ENVIRONMENT.md`

## Optional Domain Files

- `PYTHON.md`: Python setup, commands, and development workflow.
- `PAPER.md`: Academic writing structure, source status, and chapter workflow.

## Current State Files

- [Status](STATUS.md)
- [Handoff](HANDOFF.md)
- [Todo](TODO.md)
- [Decisions](DECISIONS.md)
- [Environment](ENVIRONMENT.md)

## Rules

- Update handoff records before ending substantial work.
- Keep sensitive values out of repository files.
- Prefer relative paths over absolute paths.
- Treat local environment notes as device-scoped unless the current device matches the latest recorded device and reuse is explicitly marked safe.
- If Git state and status records differ, report the mismatch and update records after confirming the current state.
