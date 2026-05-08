# HandShake

HandShake is a private Codex workflow skill for cross-device project handoff.

It helps Codex continue Python development and academic writing projects across multiple PCs and multiple Codex sessions by using repository-local project records.

## Main Artifact

```text
skills/
  handshake/
```

Current release:

```text
1.1.2
```

## What It Provides

- A reusable Codex skill named HandShake.
- A project initialization script.
- Repository-local handoff templates.
- Python project workflow notes.
- Academic writing workflow notes.
- Versioned release rules for management workflow skills.
- Chinese user-facing progress and version documents under `version/`.

## Initialize a Target Project

```text
python skills\handshake\scripts\init_project_handoff.py <target-project> --all
```

Preview first:

```text
python skills\handshake\scripts\init_project_handoff.py <target-project> --all --dry-run
```

## Update On Another PC

On each PC, keep a clone of this repository, then mirror `skills/handshake/` into the global Codex skills directory.

```text
git clone https://github.com/maxzrb/HandShake-Skill.git
cd HandShake
```

After this repository is updated on GitHub, update another PC with:

```text
git pull --ff-only
robocopy skills\handshake "$env:USERPROFILE\.codex\skills\handshake" /MIR
```

`robocopy /MIR` makes the global skill folder exactly match the repository copy. Do not keep private local edits inside `$env:USERPROFILE\.codex\skills\handshake`.

## Documentation

Beginner-friendly Chinese and English usage instructions are in:

```text
skills/README.md
```

Planning and validation records are in:

```text
plan/
```
