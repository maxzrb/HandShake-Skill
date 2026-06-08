# OpenCode Install Notes

HandShake is an Agent Skills style package. Use the repository package at:

```text
skills/handshake/
```

If OpenCode is pointed at this repository root, read `SKILL.md` first, then route to `skills/handshake/SKILL.md`.

For target projects, initialize repository-local continuity records:

```text
python skills\handshake\scripts\init_project_handoff.py <target-project>
```

The important runtime rule is simple: use `docs/codex/STATUS.md` as the single AI-facing state log and append session updates instead of relying on chat history.
