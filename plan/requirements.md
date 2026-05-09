# Requirements

## Purpose

This project designs a cross-device Codex and Claude Code handoff protocol for users who work on the same Python development and academic writing projects from multiple PCs.

The protocol must make each new Codex session reliably discover:

- Current project rules.
- Current project state.
- Active tasks.
- Recent decisions.
- Local environment constraints.
- Whether the current device matches the previous device and whether local environment assumptions can be reused.
- Handoff notes from the previous session.

## Target Users

- A single user working across multiple PCs.
- Codex sessions that do not share the same conversation history.
- Claude Code sessions that use project, personal, or plugin-provided skills.
- Projects that may be empty, partially initialized, or already managed by another workflow.

## Primary Use Cases

### Python Development

The protocol must support:

- Discovering Python version and dependency manager.
- Recording setup commands.
- Recording test, lint, type-check, and run commands.
- Tracking modified files and unfinished implementation work.
- Handling uncommitted changes without overwriting user work.
- Recording command results that matter for the next session.

### Academic Writing

The protocol must support:

- Recording paper topic, target format, and chapter structure.
- Tracking chapter status.
- Recording citation and source verification status.
- Distinguishing draft text from verified text.
- Recording figures, tables, experiments, and data dependencies.
- Preventing unsupported claims from being marked complete.

## Non-Goals

- Replace Git or cloud file synchronization.
- Store secrets, API keys, or private credentials.
- Force all projects into one rigid file structure when an existing workflow is already clear.
- Automatically publish or install skills globally without user approval.
- Guarantee conflict-free collaboration among multiple human editors.

## Operating Assumptions

- Final reusable skill artifacts are kept under `skills/` in this project.
- The skill should be self-contained so it can be copied into a global Codex skills directory.
- The skill should also be usable as a Claude Code standalone skill or repository plugin.
- Project-local rules should be stored in `AGENTS.md`.
- Project-local state should be stored under `docs/codex/`.
- If Git exists, it is the primary source for code history and synchronization state.
- If Git does not exist, the protocol must still work by reading and updating status files.
- Status files are intended to be committed unless they contain sensitive or local-only data.
- Local machine details may be recorded only when they help reproduce work; absolute paths should be avoided or clearly marked as local.
- Local machine details from a previous device must be treated as stale until the current device is matched or the environment is rechecked.
- User-facing Chinese progress and version documents should be generated under `version/`, but Codex management must not depend on them.

## Initialization Requirement

The skill must include a script that copies the project-local handoff templates into a target project.

The script must:

- Work when the skill is installed globally.
- Default to non-overwriting behavior.
- Support a dry-run mode.
- Support optional Python and academic-writing template files.
- Create Chinese user-facing `version/工作进度.md` and `version/版本迭代记录.md`.
- Require an explicit overwrite flag before replacing existing project files.

## Claude Code Support Requirement

The repository must support Claude Code without changing the core HandShake workflow.

It must:

- Keep `skills/handshake/SKILL.md` compatible with Agent Skills frontmatter.
- Provide Claude Code plugin metadata at the repository root.
- Document personal and project skill installation under `.claude/skills/handshake`.
- Provide a script or clear commands for installing the standalone Claude Code skill.
- Preserve existing Codex installation and validation behavior.

## Instruction Priority

The protocol must resolve instructions in this order:

1. Current user request.
2. System and developer instructions.
3. Project `AGENTS.md`.
4. Specialized skill or project-specific workflow.
5. Project status files under `docs/codex/`.
6. General cross-device handoff skill defaults.

If a specialized workflow has its own project management flow, Codex should use it, but it must still update or bridge to the repository's handoff records.

## Required Startup Behavior

At session start, Codex must:

- Locate and read `AGENTS.md` if present.
- Locate and read `docs/codex/INDEX.md` if present.
- Read the current status and latest handoff records.
- Compare the current device/environment with the latest recorded device.
- Recheck local paths, interpreters, dependencies, and commands when the device is different or unknown.
- Check Git state when the directory is a Git repository.
- Identify applicable project-specific skills.
- Report which files were used for orientation before making substantial edits.

## Required Shutdown Behavior

Before ending substantial work, Codex must:

- Update the latest handoff record.
- Update task status and decisions when they changed.
- Record commands run and verification results.
- Record current device identity and environment reuse guidance.
- Record unresolved blockers and next steps.
- Note uncommitted changes or synchronization risks.

## Versioning Requirement

Any skill that defines or changes the management workflow must be released under an explicit version number and must follow version control principles.

Default policy:

- Use semantic versioning: `MAJOR.MINOR.PATCH`.
- Increment `MAJOR` for breaking workflow changes.
- Increment `MINOR` for backward-compatible workflow additions.
- Increment `PATCH` for clarifications and non-behavioral fixes.
- Add a short changelog entry for every release.
- Never silently rewrite a released version.

## Open Questions

- What exact global skills directory should be used on each PC?
- Should handoff history be append-only or keep only the latest handoff plus archived summaries?
- Should academic writing require a formal source-verification checklist before completion claims?
