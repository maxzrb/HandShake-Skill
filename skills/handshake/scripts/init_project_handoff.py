#!/usr/bin/env python3
"""Initialize HandShake status records in a target project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "project-template"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy HandShake status templates into a target project without "
            "overwriting existing files unless --force is used."
        )
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing target files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing files.",
    )
    return parser.parse_args()


def required_files() -> list[Path]:
    return [
        Path("AGENTS.md"),
        Path("CLAUDE.md"),
        Path("docs/codex/INDEX.md"),
        Path("docs/codex/STATUS.md"),
        Path("version/工作进度.md"),
        Path("version/版本迭代记录.md"),
    ]


def copy_file(source: Path, target: Path, *, force: bool, dry_run: bool) -> str:
    if not source.is_file():
        raise FileNotFoundError(f"template missing: {source}")

    existed = target.exists()

    if existed and not force:
        return f"skip existing {target}"

    if dry_run:
        action = "overwrite" if existed else "create"
        return f"would {action} {target}"

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return f"{'overwrote' if existed else 'created'} {target}"


def main() -> int:
    args = parse_args()
    target_root = Path(args.target).expanduser().resolve()

    if not TEMPLATE_ROOT.is_dir():
        raise FileNotFoundError(f"template directory missing: {TEMPLATE_ROOT}")

    if not args.dry_run:
        target_root.mkdir(parents=True, exist_ok=True)

    print(f"target: {target_root}")
    print(f"template: {TEMPLATE_ROOT}")

    for relative_path in required_files():
        message = copy_file(
            TEMPLATE_ROOT / relative_path,
            target_root / relative_path,
            force=args.force,
            dry_run=args.dry_run,
        )
        print(message)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
