# Claude Code Repository Entry

@AGENTS.md

## Claude Code Notes

This repository can be loaded as a Claude Code plugin from the repository root:

```text
claude --plugin-dir .
```

The plugin manifest is `.claude-plugin/plugin.json`. It points to:

- `skills: ./skills/`
- `hooks: ./hooks/hooks.json`

The standalone skill package remains `skills/handshake/`. Keep `handshake/` synchronized with `python scripts/sync_root_mirror.py` after editing the authoritative package.

When closing substantial work, update `docs/codex/STATUS.md` and `version/工作进度.md` if those repository records exist or were created during the session.
