---
name: handshake
description: Use when a runtime loads this repository root instead of the packaged HandShake skill. Route to the authoritative HandShake package for project continuity, multi-agent handoff, Codex/Claude/Cursor/Gemini/OpenCode adaptation, installation, update, and release work.
---

# HandShake Repository Entry

This root-level file is a compatibility entry for platforms that inspect `SKILL.md` at the repository root.

Use the authoritative skill package at:

```text
skills/handshake/SKILL.md
```

For direct Codex GitHub installation, install the root-level mirror:

```text
handshake/
```

For Claude Code and Cursor plugin use, load the repository root so the plugin manifests can expose `skills/` and `hooks/`.

Before editing this repository, read `AGENTS.md`.
