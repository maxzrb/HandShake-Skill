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
1.3.1
```

## What It Provides

- A reusable Codex and Claude Code skill named HandShake.
- Claude Code plugin metadata for `claude --plugin-dir .`.
- A project initialization script.
- A Claude Code standalone skill installer.
- Repository-local handoff templates.
- Device and local environment continuity checks.
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

## Use With Claude Code

Test this repository as a Claude Code plugin:

```text
claude --plugin-dir .
```

Inside Claude Code, invoke:

```text
/handshake-skill:handshake
```

Install as a personal Claude Code skill:

```text
python skills\handshake\scripts\install_claude_skill.py --dry-run
python skills\handshake\scripts\install_claude_skill.py --force
```

After standalone installation, invoke it with:

```text
/handshake
```

## Update On Another PC

On each PC, keep a clone of this repository, then mirror `skills/handshake/` into the global Codex or Claude Code skills directory.

```text
git clone https://github.com/maxzrb/HandShake-Skill.git
cd HandShake
```

After this repository is updated on GitHub, update another PC with:

```text
git pull --ff-only
robocopy skills\handshake "$env:USERPROFILE\.codex\skills\handshake" /MIR
```

For Claude Code standalone skills:

```text
robocopy skills\handshake "$env:USERPROFILE\.claude\skills\handshake" /MIR
```

`robocopy /MIR` makes the global skill folder exactly match the repository copy. Do not keep private local edits inside `$env:USERPROFILE\.codex\skills\handshake`.

## Release This Skill

Every release must push both the branch and the annotated version tag:

```text
git push
git tag -a v<version> -m "Release HandShake <version>"
git push origin v<version>
git ls-remote --tags origin v<version>
```

If the branch was pushed without the release tag, add the missing tag to the exact release commit and push the tag before starting another release.

## Documentation

Beginner-friendly Chinese and English usage instructions are in:

```text
skills/README.md
```

Planning and validation records are in:

```text
plan/
```
