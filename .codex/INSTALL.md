# Codex Install Notes

Install HandShake from GitHub with the repository package path:

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

For local development, edit `skills/handshake/`, then synchronize the root mirror:

```text
python scripts\sync_root_mirror.py
```

After installing, use HandShake in a target project and run:

```text
python <installed-skill>\scripts\init_project_handoff.py <target-project>
```

The generated project records make Codex, Claude Code, and other agents read the same `docs/codex/STATUS.md` source of truth.
