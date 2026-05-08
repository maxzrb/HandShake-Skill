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
1.0.0
```

## What It Provides

- A reusable Codex skill named HandShake.
- A project initialization script.
- Repository-local handoff templates.
- Python project workflow notes.
- Academic writing workflow notes.
- Versioned release rules for management workflow skills.

## Initialize a Target Project

```text
python skills\handshake\scripts\init_project_handoff.py <target-project> --all
```

Preview first:

```text
python skills\handshake\scripts\init_project_handoff.py <target-project> --all --dry-run
```

## Documentation

Beginner-friendly Chinese and English usage instructions are in:

```text
skills/README.md
```

Planning and validation records are in:

```text
plan/
```
