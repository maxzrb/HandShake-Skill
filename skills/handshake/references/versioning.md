# Versioning and Release Policy

## Current Release

Version: 1.1.2
Date: 2026-05-08
Status: repository rename documentation release

Changes:

- Updated repository URLs after the GitHub repository was renamed to `HandShake-Skill`.

Compatibility:

- Backward compatible with `1.1.1`.

## Previous Releases

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
2. Update this file's current release section.
3. Record changes and compatibility notes.
4. Confirm all referenced files exist.
5. Validate the skill frontmatter and folder structure.
6. Confirm no secrets or local-only sensitive data are included.

## Immutability Rule

Do not silently rewrite a released workflow version. Publish a new version for corrections.

## Pre-1.0 Policy

Versions before `1.0.0` may introduce breaking changes, but they must still be versioned and documented.
