# Versioning and Release Policy

## Current Release

Version: 1.8.0
Date: 2026-05-12
Status: proactive trigger optimization release

Changes:

- Expanded the `SKILL.md` frontmatter description with broader auto-trigger phrases for non-trivial repository work, startup orientation, shutdown handoff, status checks, tool/device/environment switches, and common Chinese continuation requests.
- Added an "Implicit Trigger Guidance" section that tells agents not to wait for an explicit HandShake request when repository continuity signals are present.
- Updated Codex UI metadata in `agents/openai.yaml` to emphasize proactive use for continuation, closeout, and project state workflows.
- Updated Claude plugin metadata so installed plugin listings describe proactive project continuity rather than only explicit handoff.

Compatibility:

- Backward compatible with `1.7.1`.

## Previous Releases

### 1.7.1

Date: 2026-05-11
Status: version reference synchronization release

Changes:

- Synchronized README version references to `1.7.1`.
- Preserved the `1.7.0` workflow behavior while aligning user-facing documentation with the tagged package version.

Compatibility:

- Backward compatible with `1.7.0`.

### 1.7.0

Date: 2026-05-11
Status: mandatory workflow discipline release

Changes:

- Added mandatory `git pull` at startup when Git is available, to prevent working from an outdated local repository.
- Added a "Phased Execution" section requiring step-by-step plans confirmed by the user before implementation.
- Added a rule requiring the agent to remind the user to consider a git commit after each completed step.
- These rules are written into `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, and `protocol.md` for both Codex and Claude Code.

Compatibility:

- Backward compatible with `1.6.0`.

### 1.6.0

Date: 2026-05-11
Status: mandatory incremental version/ session records release

Changes:

- Elevated `version/工作进度.md` from conditional to minimum required closure for both Codex and Claude Code shutdown workflows.
- Added incremental log templates with explicit "append, never overwrite" rules.
- Added explicit version migration rules for `version/版本迭代记录.md` (move old to history first, then write new).
- Updated all agent entry points: `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `openai.yaml`, and `protocol.md`.
- Synced missing template files (`CLAUDE.md`, `PROGRESS.zh-CN.md`, `check_project_handoff.py`) to the repo.

Compatibility:

- Backward compatible with `1.5.0`.

### 1.5.0

Date: 2026-05-09
Status: Codex and Claude Code handoff compatibility release

Changes:

- Added a generated `CLAUDE.md` project entry template that imports `AGENTS.md` with `@AGENTS.md`.
- Clarified Codex to Claude Code and Claude Code to Codex takeover scenarios in the skill, protocol, and templates.
- Changed shutdown guidance to minimum required closure plus conditional record updates.
- Added `docs/codex/PROGRESS.zh-CN.md` and a lightweight `check_project_handoff.py` readiness script.
- Added academic writing preferences to `PAPER.md`, `AGENTS.md`, `CLAUDE.md`, and the skill's Domain Handling section for formal Chinese writing tasks (papers, teaching designs, coursework, literature reviews).
- Updated README copyable prompts for initialization, agent handoff, cross-device continuation, paper writing, and Python environment changes.

Compatibility:

- Backward compatible with `1.4.0`.

### 1.4.0

Date: 2026-05-09
Status: root install path compatibility release

Changes:

- Added a root-level `handshake/` skill package mirror so Codex GitHub installers can find the skill without scanning `skills/handshake/`.
- Documented the dual install path contract: `handshake/` for Codex direct installation and `skills/handshake/` for Claude Code plugin use.
- Updated release validation to check both skill package locations.

Compatibility:

- Backward compatible with `1.3.1`.

### 1.3.1

Date: 2026-05-09
Status: release push checklist clarification

Changes:

- Added an explicit release push checklist covering validation, commit, branch push, annotated tag creation, tag push, and remote tag verification.
- Documented the recovery rule for a release commit that was pushed without its release tag.
- Updated user-facing notes to require pushing both the branch and annotated release tag.

Compatibility:

- Backward compatible with `1.3.0`.

### 1.3.0

Date: 2026-05-09
Status: Claude Code support release

Changes:

- Added Claude Code plugin metadata under `.claude-plugin/plugin.json`.
- Documented standalone Claude Code personal and project skill installation paths.
- Added `scripts/install_claude_skill.py` to copy HandShake into Claude Code skill directories.
- Documented Claude Code invocation forms for standalone skills and plugin testing.

Compatibility:

- Backward compatible with `1.2.0`.

### 1.2.0

Date: 2026-05-08
Status: device/environment continuity release

Changes:

- Added startup guidance to identify the current device or local environment signature.
- Added rules for comparing the current device with the latest recorded device before reusing local setup assumptions.
- Added template fields for device identity, same-device comparison, and environment reuse status.
- Required handoff records to note whether local paths, virtual environments, dependencies, and command results may be reused.

Compatibility:

- Backward compatible with `1.1.2`.

### 1.1.2

Date: 2026-05-08
Status: repository rename documentation release

Changes:

- Updated repository URLs after the GitHub repository was renamed to `HandShake-Skill`.

Compatibility:

- Backward compatible with `1.1.1`.

### 1.1.1

Date: 2026-05-08
Status: update-instructions documentation release

Changes:

- Added documentation for updating HandShake on other PCs after GitHub releases.

Compatibility:

- Backward compatible with `1.1.0`.

### 1.1.0

Date: 2026-05-08
Status: user-facing version document release

Changes:

- Added Chinese user-facing `version/工作进度.md`.
- Added Chinese user-facing `version/版本迭代记录.md`.
- Updated the initializer to create the `version/` documents by default.
- Clarified that Codex project management must not depend on the `version/` documents.

Compatibility:

- Backward compatible with `1.0.0`.

### 1.0.0

Date: 2026-05-08
Status: first named HandShake release

Changes:

- Renamed the skill product to HandShake.
- Changed the skill folder and machine-readable skill id to `handshake`.
- Kept initialization and global-use support from `0.2.0`.

Compatibility:

- Breaking rename from `cross-device-handoff` to `handshake`.
- Users of `0.2.0` should copy or install the `handshake/` folder and refer to the skill as HandShake.

### 0.2.0

Date: 2026-05-08
Status: usable draft with initialization support

Changes:

- Added self-contained template assets under `assets/project-template/`.
- Added `scripts/init_project_handoff.py` to initialize target projects.
- Added global-use guidance.
- Kept default initialization non-overwriting unless `--force` is used.

Compatibility:

- Backward compatible with `0.1.0`.

### 0.1.0

Date: 2026-05-08
Status: initial usable draft

Changes:

- Added startup and shutdown handoff workflow.
- Added conflict and missing-file rules.
- Added Python and academic writing handling.
- Added repository record template guidance.
- Added strict versioned release discipline for management workflow skills.

Compatibility:

- Initial release. No migration required.

## Version Scheme

Use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

## Increment Rules

Increment `MAJOR` for:

- Breaking changes to required startup behavior.
- Breaking changes to required shutdown behavior.
- Renaming required project records.
- Changing instruction priority in a way that affects existing projects.

Increment `MINOR` for:

- New optional project records.
- New domain-specific guidance.
- Backward-compatible validation checks.
- Backward-compatible template additions.

Increment `PATCH` for:

- Clarifications.
- Typo fixes.
- Formatting fixes.
- Non-behavioral wording improvements.

## Release Checklist

Before release:

1. Update the version in `SKILL.md`.
2. Update `.claude-plugin/plugin.json` when present.
3. Update both package locations, `skills/handshake/` and the root-level `handshake/` mirror.
4. Update user-facing version references such as `README.md` and `skills/README.md`.
5. Update this file's current release section.
6. Record changes and compatibility notes.
7. Confirm all referenced files exist.
8. Validate the skill frontmatter and folder structure in both package locations.
9. Confirm no secrets or local-only sensitive data are included.

## Git Publish Checklist

After release files are validated and committed:

1. Push the branch: `git push`.
2. Create an annotated tag on the release commit: `git tag -a v<version> -m "Release HandShake <version>"`.
3. Push the tag: `git push origin v<version>`.
4. Verify the branch and tag:
   - `git status --short --branch`
   - `git log -1 --oneline --decorate`
   - `git ls-remote --tags origin v<version>`

Never consider a release complete until both the branch and the matching annotated tag are visible on the remote. If the branch was pushed first and the tag was forgotten, add the missing annotated tag to that exact release commit and push the tag before starting another release.

## Immutability Rule

Do not silently rewrite a released workflow version. Publish a new version for corrections.

## Pre-1.0 Policy

Versions before `1.0.0` may introduce breaking changes, but they must still be versioned and documented.
