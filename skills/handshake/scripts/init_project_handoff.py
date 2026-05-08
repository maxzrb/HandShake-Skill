#!/usr/bin/env python3
"""Initialize Codex handoff records in a target project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "project-template"

OPTIONAL_DOMAIN_FILES = {
    "python": Path("docs/codex/PYTHON.md"),
    "paper": Path("docs/codex/PAPER.md"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy cross-device Codex handoff templates into a target project."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--python",
        action="store_true",
        help="Include the Python workflow template.",
    )
    parser.add_argument(
        "--paper",
        action="store_true",
        help="Include the academic writing workflow template.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Include all optional domain templates.",
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
        Path("docs/codex/INDEX.md"),
        Path("docs/codex/STATUS.md"),
        Path("docs/codex/HANDOFF.md"),
        Path("docs/codex/DECISIONS.md"),
        Path("docs/codex/TODO.md"),
        Path("docs/codex/ENVIRONMENT.md"),
    ]


def selected_files(args: argparse.Namespace) -> list[Path]:
    files = required_files()
    if args.all or args.python:
        files.append(OPTIONAL_DOMAIN_FILES["python"])
    if args.all or args.paper:
        files.append(OPTIONAL_DOMAIN_FILES["paper"])
    return files


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

    for relative_path in selected_files(args):
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
