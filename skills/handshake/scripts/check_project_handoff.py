#!/usr/bin/env python3
"""Check lightweight HandShake project readiness."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


KEY_FILES = [
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("docs/codex/INDEX.md"),
    Path("docs/codex/STATUS.md"),
    Path("docs/codex/HANDOFF.md"),
    Path("docs/codex/TODO.md"),
    Path("docs/codex/DECISIONS.md"),
    Path("docs/codex/ENVIRONMENT.md"),
    Path("docs/codex/PROGRESS.zh-CN.md"),
]

OPTIONAL_FILES = [
    Path("docs/codex/PYTHON.md"),
    Path("docs/codex/PAPER.md"),
    Path("version/工作进度.md"),
    Path("version/版本迭代记录.md"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report Git, Python, virtual environment, and HandShake file status."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current directory.",
    )
    return parser.parse_args()


def run_command(args: list[str], cwd: Path) -> tuple[int, str]:
    try:
        completed = subprocess.run(
            args,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    except FileNotFoundError:
        return 127, f"{args[0]} not found"
    except OSError as exc:
        return 1, str(exc)

    return completed.returncode, completed.stdout.strip()


def print_section(title: str) -> None:
    print()
    print(f"## {title}")


def check_files(target: Path) -> int:
    missing_required = 0

    print_section("Handoff files")
    for relative_path in KEY_FILES:
        exists = (target / relative_path).is_file()
        if not exists:
            missing_required += 1
        print(f"{'ok' if exists else 'missing'} {relative_path}")

    print_section("Optional files")
    for relative_path in OPTIONAL_FILES:
        exists = (target / relative_path).is_file()
        print(f"{'ok' if exists else 'missing'} {relative_path}")

    return missing_required


def check_git(target: Path) -> int:
    print_section("Git")
    code, output = run_command(["git", "rev-parse", "--is-inside-work-tree"], target)
    if code != 0 or output.lower() != "true":
        print("git repository: no or unavailable")
        if output:
            print(output)
        return 0

    print("git repository: yes")

    code, branch = run_command(["git", "branch", "--show-current"], target)
    print(f"branch: {branch if code == 0 and branch else '(detached or unknown)'}")

    code, commit = run_command(["git", "rev-parse", "--short", "HEAD"], target)
    print(f"last commit: {commit if code == 0 and commit else '(unknown)'}")

    code, status = run_command(["git", "status", "--short"], target)
    if code == 0:
        print("working tree clean: yes" if not status else "working tree clean: no")
        if status:
            print(status)
    else:
        print("git status failed")
        print(status)

    return 0


def check_python(target: Path) -> int:
    print_section("Python")
    print(f"current executable: {sys.executable}")
    print(f"current version: {sys.version.split()[0]}")
    print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', '(not set)')}")
    print(f"CONDA_PREFIX: {os.environ.get('CONDA_PREFIX', '(not set)')}")

    code, output = run_command([sys.executable, "--version"], target)
    print(f"python command check: {'ok' if code == 0 else 'failed'}")
    if output:
        print(output)

    return 0


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()

    print(f"target: {target}")
    if not target.exists():
        print("target does not exist")
        return 2
    if not target.is_dir():
        print("target is not a directory")
        return 2

    missing_required = check_files(target)
    check_git(target)
    check_python(target)

    print_section("Summary")
    if missing_required:
        print(f"missing required handoff files: {missing_required}")
        return 1

    print("required handoff files present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
