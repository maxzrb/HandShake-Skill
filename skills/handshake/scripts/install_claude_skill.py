#!/usr/bin/env python3
"""Install HandShake as a Claude Code standalone skill."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PERSONAL_TARGET = Path.home() / ".claude" / "skills" / "handshake"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy HandShake into a Claude Code standalone skill directory."
    )
    parser.add_argument(
        "--target",
        default=str(DEFAULT_PERSONAL_TARGET),
        help="Target skill directory. Defaults to ~/.claude/skills/handshake.",
    )
    parser.add_argument(
        "--project",
        help=(
            "Install into <project>/.claude/skills/handshake instead of the "
            "personal skills directory."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing target skill directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing files.",
    )
    return parser.parse_args()


def selected_target(args: argparse.Namespace) -> Path:
    if args.project:
        return Path(args.project).expanduser().resolve() / ".claude" / "skills" / "handshake"
    return Path(args.target).expanduser().resolve()


def copy_skill(target: Path, *, force: bool, dry_run: bool) -> list[str]:
    messages: list[str] = []

    if not (SKILL_ROOT / "SKILL.md").is_file():
        raise FileNotFoundError(f"skill root missing SKILL.md: {SKILL_ROOT}")

    if target.exists() and not force:
        messages.append(f"skip existing {target}")
        messages.append("use --force to overwrite")
        return messages

    action = "overwrite" if target.exists() else "create"
    if dry_run:
        messages.append(f"would {action} {target}")
        return messages

    if target.exists():
        shutil.rmtree(target)

    shutil.copytree(
        SKILL_ROOT,
        target,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    messages.append(f"{'overwrote' if action == 'overwrite' else 'created'} {target}")
    return messages


def main() -> int:
    args = parse_args()
    target = selected_target(args)

    print(f"source: {SKILL_ROOT}")
    print(f"target: {target}")

    for message in copy_skill(target, force=args.force, dry_run=args.dry_run):
        print(message)

    print("Claude Code standalone invocation: /handshake")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
