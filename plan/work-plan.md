# Cross-Device Codex Handoff Protocol Work Plan

## 1. Project Goal

Design a reusable cross-device project handoff protocol for Codex-assisted work. The protocol must support Python project development and academic writing, while remaining compatible with projects that already have their own management workflow or specialized skills.

The final reusable artifacts will be placed under `skills/`.

## 2. Design Principles

- Keep project rules with the repository through `AGENTS.md`.
- Keep reusable operating procedures in a Codex skill.
- Keep current project state in repository-local status files.
- Prefer an existing project-specific or domain-specific management workflow when it is clearly defined.
- Require strict handoff reading at session start and strict handoff writing before session end.
- Preserve user changes and avoid destructive Git operations unless explicitly requested.
- Record evidence for completed work, including commands run, files changed, tests, and unresolved risks.
- Release management workflow skills strictly by version number and follow version control principles.

## 3. Expected Deliverables

### 3.1 Protocol Specification

Create a concise specification covering:

- Startup workflow for every Codex session.
- End-of-session handoff workflow.
- Priority order among user instructions, `AGENTS.md`, project status files, and specialized skills.
- Conflict handling when Git state, status records, and user instructions disagree.
- Rules for cross-device synchronization.
- Rules for Python projects.
- Rules for academic writing projects.
- Rules for sensitive data and local-only environment details.

### 3.2 Repository Template Files

Prepare templates for project-local management files:

- `AGENTS.md`
- `docs/codex/INDEX.md`
- `docs/codex/STATUS.md`
- `docs/codex/HANDOFF.md`
- `docs/codex/DECISIONS.md`
- `docs/codex/TODO.md`
- `docs/codex/ENVIRONMENT.md`
- Optional Python-specific file: `docs/codex/PYTHON.md`
- Optional academic-writing file: `docs/codex/PAPER.md`

### 3.3 Codex Skill

Create a skill under `skills/` that instructs Codex to:

- Detect whether the current project has `AGENTS.md`.
- Read the project status entrypoint before starting work.
- Identify applicable project-specific skills and respect their management flow.
- Fall back to the general cross-device protocol when no project-specific workflow exists.
- Update handoff records at meaningful checkpoints.
- Enforce versioned releases for management workflow skills.
- Initialize target projects by copying repository-local handoff templates.
- Remain self-contained so it can be installed and used globally.

### 3.4 Validation Materials

Prepare lightweight validation cases:

- Empty Python project with no Git repository.
- Existing Python Git repository with uncommitted changes.
- Academic writing project with chapter drafts and literature records.
- Project with an existing management skill that should take priority.
- Cross-device scenario where status files and Git state differ.

## 4. Work Phases

### Phase 1: Requirements and Scope

Clarify the operating assumptions:

- Whether this protocol is for personal use only or reusable distribution.
- Whether skills should live inside each project or in the global Codex skills directory.
- Whether project status files should be committed to Git by default.
- How strict the workflow should be when the user asks for a quick one-off task.
- How to handle private paper data, unpublished results, and machine-local paths.

Output:

- Finalized scope note in `plan/requirements.md`.

### Phase 2: Protocol Architecture

Define the protocol layers:

- Global skill behavior.
- Repository `AGENTS.md` behavior.
- Project status file schema.
- Optional domain-specific extensions.
- Conflict and fallback rules.

Output:

- `plan/protocol-architecture.md`.

### Phase 3: Template Design

Draft templates for:

- `AGENTS.md`
- Codex status files.
- Python project extension.
- Academic writing extension.

Output:

- Template drafts under `plan/templates-draft/`.

### Phase 4: Skill Design

Design the skill package:

- Skill name and triggering description.
- Required startup checklist.
- Required shutdown checklist.
- Versioning and release policy.
- Optional references or scripts.

Versioning requirement:

- The skill must include an explicit version.
- Releases must use semantic versioning unless a stronger versioning scheme is later chosen.
- Breaking workflow changes require a major version bump.
- Backward-compatible workflow additions require a minor version bump.
- Clarifications, typo fixes, and non-behavioral edits require a patch version bump.
- Each release must have a short changelog entry.
- Released versions must not be silently rewritten; publish a new version for changes.

Output:

- Skill design document in `plan/skill-design.md`.

### Phase 5: Implementation

Create the initial skill and supporting resources under `skills/`.

Expected structure:

```text
skills/
  handshake/
    SKILL.md
    agents/
      openai.yaml
    scripts/
      init_project_handoff.py
    assets/
      project-template/
        AGENTS.md
        docs/codex/*.md
    references/
      protocol.md
      templates.md
      versioning.md
```

Output:

- Working skill package under `skills/handshake/`.

### Phase 6: Validation

Validate the workflow against representative scenarios:

- Confirm startup checklist forces Codex to inspect project state.
- Confirm shutdown checklist writes clear handoff notes.
- Confirm the protocol handles a missing Git repository.
- Confirm it does not override specialized project workflows.
- Confirm versioning rules are visible and actionable.

Output:

- `plan/validation-report.md`.

### Phase 7: Release

Prepare the first versioned release of the skill.

Release checklist:

- Validate skill frontmatter.
- Confirm all referenced files exist.
- Confirm version and changelog are updated.
- Confirm templates are internally consistent.
- Confirm no sensitive local data is included.
- Tag or record the release version according to the selected version control strategy.

Output:

- Versioned skill release under `skills/handshake/`.
- Release notes in `skills/handshake/CHANGELOG.md` if changelog is kept inside the skill package, or in the versioning reference if avoiding extra package files is preferred.

## 5. Open Decisions

- The skill should support global installation by copying the full `handshake/` folder.
- Target projects should be initialized by the bundled script unless a project-specific process already exists.
- Should `docs/codex/HANDOFF.md` be append-only, or should it only contain the latest handoff?
- Should academic-writing projects require source verification before any chapter is marked complete?
- Should version history be kept in Git tags, a changelog file, or both?

## 6. Immediate Next Steps

1. Finalize requirements in `plan/requirements.md`.
2. Draft the protocol architecture in `plan/protocol-architecture.md`.
3. Draft the skill design in `plan/skill-design.md`.
4. Implement `skills/handshake/`.
5. Validate with the five representative scenarios.
