# Claude Code Project Entry

@AGENTS.md

## Claude Code Startup

Before making substantive edits, Claude Code must:

1. Read `docs/codex/INDEX.md`.
2. Read `docs/codex/STATUS.md`, `docs/codex/HANDOFF.md`, `docs/codex/TODO.md`, and `docs/codex/ENVIRONMENT.md`.
3. Read `docs/codex/DECISIONS.md` when durable project choices may affect the task.
4. Read `docs/codex/PAPER.md` for paper-writing work and `docs/codex/PYTHON.md` for Python environment or code execution work, when present.
5. Check `git status` before editing.
6. Identify whether Claude Code is taking over work last handled by Codex, continuing its own previous work, or resuming on a different device, directory, or virtual environment.

## Claude Code Shutdown

Before ending substantial work, Claude Code must at minimum update:

- `docs/codex/HANDOFF.md`
- `docs/codex/STATUS.md`
- `version/工作进度.md` — append a dated session entry; do not overwrite previous entries

Record changed files, commands run, verification results, remaining issues, and next recommended steps.

Update conditionally:

- `docs/codex/TODO.md` when task status changes.
- `docs/codex/DECISIONS.md` when a long-term decision is made.
- `docs/codex/ENVIRONMENT.md` when environment, path, Python, dependency, or command behavior changes.
- `docs/codex/PAPER.md` or equivalent writing records when chapter status, literature status, research scope, or citation state changes.
- `version/版本迭代记录.md` when the project version number changed: move the old current version to history first, then write the new version. Do not delete or overwrite historical version entries.

When replying to the user, explain in Chinese. Keep commands, paths, errors, code, package names, and file names in their original form.

## Claude Code Writing Tasks

For papers, teaching designs, coursework, literature reviews, and curriculum-standard analysis, follow `docs/codex/PAPER.md` before drafting. Use Simplified Chinese by default, keep the tone natural and suitable for graduate-level or teacher-training-student writing, and avoid stiff AI-style prose, repetitive phrasing, excessive bulleting, and hollow academic wording.

Do not invent references, policy documents, curriculum standards, journal details, data, DOI, URL, author names, titles, years, volumes, issues, or pages. If a detail cannot be verified, mark it as `待人工复核` or state the uncertainty clearly. Verify online-checkable and time-sensitive information when available before making factual claims.
