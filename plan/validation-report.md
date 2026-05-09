# Validation Report

Date: 2026-05-09
Skill version: 1.4.0

## Scope

Validated the `handshake` skill package and planning artifacts for the root install path compatibility update.

## Files Checked

- `plan/requirements.md`
- `plan/protocol-architecture.md`
- `plan/templates-draft/`
- `plan/skill-design.md`
- `skills/handshake/SKILL.md`
- `handshake/SKILL.md`
- `skills/handshake/agents/openai.yaml`
- `skills/handshake/scripts/init_project_handoff.py`
- `skills/handshake/scripts/install_claude_skill.py`
- `scripts/sync_root_mirror.py`
- `handshake/`
- `skills/handshake/assets/project-template/`
- `skills/handshake/references/protocol.md`
- `skills/handshake/references/templates.md`
- `skills/handshake/references/versioning.md`
- `skills/handshake/assets/project-template/version/工作进度.md`
- `skills/handshake/assets/project-template/version/版本迭代记录.md`
- `.claude-plugin/plugin.json`

## Automated Validation

Python validator command:

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\handshake
```

Result:

```text
Skill is valid!
```

Root mirror validator command:

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py handshake
```

Result:

```text
Skill is valid!
```

Root mirror synchronization command:

```text
python scripts\sync_root_mirror.py --check
```

Result:

```text
root mirror is synchronized
```

Note:

- `python` now resolves to the local Python 3.14.3 installation.
- `PyYAML 6.0.3` is installed for the validator.
- A user-local `py.cmd` shim was added under `C:\Users\MAX2EB\AppData\Local\Python\bin` so `py` and common selector forms such as `py -3` work in this environment.
- A PowerShell static frontmatter check was also run and passed.

Static check command summary:

```text
Read skills\handshake\SKILL.md as UTF-8, verified YAML frontmatter delimiters, name: handshake, nonempty description, and no angle brackets.
```

Result:

```text
Static skill frontmatter check passed
```

## Initialization Script Validation

Dry-run command:

```text
python skills\handshake\scripts\init_project_handoff.py outputs\handshake-init-test-1.4.0 --all --dry-run
```

Result:

- Reported planned creation of `AGENTS.md`.
- Reported planned creation of all required `docs/codex/` records.
- Reported planned creation of optional `PYTHON.md` and `PAPER.md`.
- Reported planned creation of Chinese user-facing `version/工作进度.md` and `version/版本迭代记录.md`.

Real initialization command:

```text
python skills\handshake\scripts\init_project_handoff.py outputs\handshake-init-test --all
```

Result:

- Not run in this session. The dry-run path above validated script discovery and the full template file list without writing output files.

Template existence check result:

```text
Template file existence check passed
```

## Claude Code Support Validation

Plugin metadata command:

```text
python -m json.tool .claude-plugin\plugin.json
```

Result:

- `plugin.json` parsed as valid JSON.
- Plugin name is `handshake-skill`.
- Plugin version is `1.4.0`.

Standalone installer dry-run command:

```text
python skills\handshake\scripts\install_claude_skill.py --dry-run
```

Result:

- Reported source as `skills\handshake`.
- Reported target as `C:\Users\MAX2EB\.claude\skills\handshake`.
- Reported that it would create the Claude Code standalone skill directory.
- Reported standalone invocation as `/handshake`.

## Placeholder Scan

Command:

```text
rg "TODO|\[TODO|placeholder" plan skills
```

Result:

- No unresolved template placeholders were found.
- Matches were legitimate references to `TODO.md`.

## Versioning Check

Confirmed:

- `skills/handshake/SKILL.md` declares `Version: 1.4.0`.
- `handshake/SKILL.md` declares `Version: 1.4.0`.
- `references/versioning.md` records the current release as `1.4.0`.
- `.claude-plugin/plugin.json` records plugin version `1.4.0`.
- Semantic versioning rules are documented.
- The immutability rule for released workflow versions is documented.
- The release checklist requires version update, release notes, reference validation, structure validation, sensitive-data review, branch push, annotated tag creation, tag push, and remote verification.

## Scenario Coverage Review

### Empty Project With No Git Repository

Covered by:

- Missing Git fallback in `SKILL.md`.
- Missing file behavior in `references/protocol.md`.
- Planning note in `plan/protocol-architecture.md`.

Status: covered.

### Existing Git Repository With Uncommitted Changes

Covered by:

- Startup Git state inspection.
- Shutdown synchronization report.
- Conflict rule treating Git as authoritative for changed files.

Status: covered at protocol level; not executed against a real Git repository yet.

### Same Device vs. Different Device

Covered by:

- Startup device/environment comparison in `SKILL.md`.
- Startup and shutdown workflow updates in `references/protocol.md`.
- Device identity and environment reuse fields in `ENVIRONMENT.md`, `HANDOFF.md`, and `STATUS.md`.

Status: covered at protocol/template level; not forward-tested across two physical devices yet.

### Claude Code Skill Use

Covered by:

- Agent Skills-compatible `SKILL.md` frontmatter.
- `.claude-plugin/plugin.json` for repository plugin loading.
- `scripts/install_claude_skill.py` dry-run for standalone skill installation.
- README documentation for personal, project, and plugin-based Claude Code use.

Status: covered at package/documentation level; not executed inside an interactive Claude Code session in this validation run.

### Release Push and Tag Flow

Covered by:

- `SKILL.md` release push checklist.
- `references/versioning.md` Git publish checklist.
- Planning release flow requiring branch push, annotated tag creation, tag push, and remote verification.

Status: covered at workflow/documentation level; this release should be completed by pushing `main`, creating `v1.4.0`, pushing that tag, and verifying the remote tag.

### Root Install Path Compatibility

Covered by:

- Root-level `handshake/` mirror for Codex direct GitHub installation.
- `skills/handshake/` retained for Claude Code plugin use.
- Release checklist requiring both package paths to remain synchronized and validated.

Status: covered at package layout level; remote install should use `--path handshake`.

### Python Project

Covered by:

- Python-specific handling in `SKILL.md`.
- `PYTHON.md` template draft.
- Python fields in `references/templates.md`.

Status: covered at protocol level.

### Academic Writing Project

Covered by:

- Academic writing handling in `SKILL.md`.
- `PAPER.md` template draft.
- Source verification rules in `references/templates.md`.

Status: covered at protocol level.

### Existing Specialized Workflow

Covered by:

- Instruction priority rules.
- Specialized workflow bridge rule.
- Conflict handling in `references/protocol.md`.

Status: covered at protocol level.

## Remaining Risks

- The workflow has not yet been forward-tested by a fresh Codex session on a real Python or writing project.
- The device/environment continuity behavior has not yet been forward-tested across two physical devices.
- Claude Code support has not yet been forward-tested inside an interactive Claude Code session.
- The global skills directory path still needs to be selected per PC before installation.

## Recommendation

Treat `handshake` version `1.4.0` as the HandShake release that adds a root-level install path mirror so Codex GitHub installers do not need to locate `skills/handshake/`. The next release step is to push both `main` and the annotated `v1.4.0` tag, then verify the remote tag.
