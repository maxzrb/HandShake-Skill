#!/usr/bin/env python3
"""Check HandShake status-record readiness."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


KEY_FILES = [
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("docs/codex/INDEX.md"),
    Path("docs/codex/STATUS.md"),
    Path("version/工作进度.md"),
    Path("version/版本迭代记录.md"),
]

TIMESTAMP_RE = re.compile(
    r"^#{2,3} (?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}|YYYY-MM-DD HH:MM)",
    re.MULTILINE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report Git and HandShake status-record readiness."
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

    print_section("HandShake files")
    for relative_path in KEY_FILES:
        exists = (target / relative_path).is_file()
        if not exists:
            missing_required += 1
        print(f"{'ok' if exists else 'missing'} {relative_path}")

    return missing_required


def check_status_shape(target: Path) -> int:
    status_path = target / "docs/codex/STATUS.md"
    progress_path = target / "version/工作进度.md"
    issues = 0

    print_section("Status log shape")

    if not status_path.is_file():
        print("missing docs/codex/STATUS.md")
        return 1

    status = status_path.read_text(encoding="utf-8")
    for section in ["## Current Snapshot", "## Active TODO", "## Session Log"]:
        if section not in status:
            print(f"missing section in STATUS.md: {section}")
            issues += 1
        else:
            print(f"ok STATUS.md contains {section}")

    if TIMESTAMP_RE.search(status):
        print("ok STATUS.md contains a timestamped log entry or placeholder")
    else:
        print("missing timestamped STATUS.md log entry or placeholder")
        issues += 1

    if progress_path.is_file():
        progress = progress_path.read_text(encoding="utf-8")
        if TIMESTAMP_RE.search(progress):
            print("ok version/工作进度.md contains a timestamped log entry or placeholder")
        else:
            print("missing timestamped version/工作进度.md log entry or placeholder")
            issues += 1

    return issues


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
    shape_issues = check_status_shape(target)
    check_git(target)

    print_section("Summary")
    if missing_required or shape_issues:
        print(
            "handoff readiness failed: "
            f"{missing_required} missing required files, {shape_issues} status shape issues"
        )
        return 1

    print("required HandShake status records present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
