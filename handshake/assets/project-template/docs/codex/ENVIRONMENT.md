# Environment

## Portable Setup

Describe setup steps that should work across devices.

```text
command
```

## Dependencies

- Runtime:
- Package manager:
- External tools:

## Device Identity

Use a stable, user-friendly device label plus enough technical evidence for Codex to decide whether this is the same local environment as the previous session.

- Current device label:
- Hostname:
- Operating system:
- Shell:
- Workspace root:
- Last verified:
- Previous recorded device:
- Same as previous device: yes/no/unknown
- Local environment reuse: safe after sanity check / recheck required / unknown

## Environment Continuity Rules

- If this is the same device and reuse is marked safe, Codex may reuse local paths and setup notes after a quick sanity check.
- If this is a different or unknown device, Codex must verify local paths, interpreters, virtual environments, installed dependencies, and command availability before relying on previous notes.
- If dependency files changed since the last session, recheck the local environment even on the same device.

## Local Notes

Record machine-specific notes here. Do not make these the only setup instructions.

- Device:
- Path:
- Note:

## Secrets

Do not record secret values.

Required environment variables:

- `NAME`: purpose

## Common Commands

```text
test command
lint command
run command
```
