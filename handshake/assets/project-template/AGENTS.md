# Project Instructions for AI Coding Agents

This project uses HandShake records so Codex and Claude Code can alternately take over the same repository without relying on previous chat history.

## Required Startup

Before substantial work, the active AI agent must:

1. Read this file.
2. If running in Claude Code, read `CLAUDE.md` if present.
3. Read `docs/codex/INDEX.md`.
4. Read the latest project status and handoff files linked from the index.
5. If this is a Git repository:
   a. Run `git pull` to synchronize with the remote before making any changes.
   b. Run `git status` to see branch, commit, staged, unstaged, and untracked files.
6. Identify whether this is a new session, Codex taking over from Claude Code, Claude Code taking over from Codex, or a cross-device/cross-environment continuation.
7. Compare the current device/environment with the latest recorded device in `STATUS.md`, `HANDOFF.md`, or `ENVIRONMENT.md`.
8. If the device is different or unknown, verify local paths, interpreters, virtual environments, dependencies, and commands before relying on previous environment notes.
9. Report the orientation files used and whether the local environment appears reusable before editing.
10. For non-trivial tasks, draft a phased plan and confirm with the user before implementing. Execute step by step.

## Required Handoff

Before ending substantial work, the active AI agent must update the project handoff records under `docs/codex/`.

At minimum, update:

- `docs/codex/HANDOFF.md` with completed work, changed files, commands, verification, blockers or remaining issues, and next steps.
- `docs/codex/STATUS.md` with the current objective, current state, active work, synchronization state, and environment reuse status.
- `version/工作进度.md` with a dated session entry (append, never overwrite previous entries).
- The final user reply must mention current Git status, whether the worktree is clean, and whether a commit is recommended before switching tools or devices.
- After each completed execution step, remind the user to consider a git commit before proceeding to the next step.

Update conditionally:

- `docs/codex/TODO.md` only when tasks are added, completed, cancelled, or reprioritized.
- `docs/codex/DECISIONS.md` only when durable design, architecture, dependency, workflow, or writing-position decisions are made.
- `docs/codex/ENVIRONMENT.md` only when Python version, virtual environment, dependency installation, system paths, run/test commands, device, or local execution environment changes.
- `docs/codex/PAPER.md` or equivalent writing records only when chapter state, source state, research scope, or citation status changes.
- `version/版本迭代记录.md` when the project version number changed: move the old current version to history first, then write the new version. Do not delete or overwrite historical version entries.

## Workflow Priority

Use this priority order:

1. Current user request.
2. System and developer instructions.
3. This `AGENTS.md`.
4. Specialized project or domain skill.
5. Files under `docs/codex/`.
6. General cross-device and cross-agent handoff skill defaults.

If a specialized workflow has its own management records, use that workflow but keep `docs/codex/` updated or clearly cross-linked.

Do not treat `version/工作进度.md` or `version/版本迭代记录.md` as authoritative project state. They are derived summaries for Chinese-speaking users.

## Safety

- Do not overwrite user changes.
- Do not run destructive Git commands unless explicitly requested.
- Do not store secrets in repository files.
- Record local-only paths as local notes, not portable setup instructions.
- Do not reuse local environment assumptions from another device until they have been verified on the current device.

## Academic Writing Tasks

For papers, teaching designs, coursework, literature reviews, curriculum-standard analysis, and similar formal writing tasks:

- Read `docs/codex/PAPER.md` before writing or revising.
- Communicate with the user in Simplified Chinese unless asked otherwise.
- Write naturally and clearly at a graduate-student or teacher-training-student level; avoid stiff AI-style prose, excessive frameworks, repetitive phrasing, and inflated abstractions.
- Use bullets only when they help readability. Do not break ordinary prose into unnecessary lists.
- Never invent references, policy documents, curriculum standards, journal details, data, DOI, URL, author names, titles, years, volumes, issues, or pages.
- Mark unverifiable bibliographic details or claims as `待人工复核`.
- Verify online-checkable and time-sensitive information when available before making factual claims.

## Versioning

Management workflow skills and templates used by this project must be released by explicit version number and follow version control principles.
