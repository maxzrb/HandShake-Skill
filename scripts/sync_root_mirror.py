#!/usr/bin/env python3
"""Synchronize the root-level HandShake skill mirror."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "skills" / "handshake"
TARGET = REPO_ROOT / "handshake"
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize root-level handshake/ from skills/handshake/."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Only verify that the mirror is synchronized.",
    )
    return parser.parse_args()


def ensure_source() -> None:
    if not (SOURCE / "SKILL.md").is_file():
        raise FileNotFoundError(f"missing source skill: {SOURCE}")


def sync() -> None:
    ensure_source()
    if TARGET.exists():
        shutil.rmtree(TARGET)
    shutil.copytree(SOURCE, TARGET, ignore=IGNORE)


def compare_dirs(left: Path, right: Path) -> list[str]:
    comparison = filecmp.dircmp(left, right, ignore=["__pycache__"])
    differences: list[str] = []

    for name in comparison.left_only:
        differences.append(f"missing from mirror: {left / name}")
    for name in comparison.right_only:
        differences.append(f"extra in mirror: {right / name}")
    for name in comparison.diff_files:
        differences.append(f"content differs: {left / name}")
    for name in comparison.funny_files:
        differences.append(f"could not compare: {left / name}")

    for subdir in comparison.common_dirs:
        if subdir == "__pycache__":
            continue
        differences.extend(compare_dirs(left / subdir, right / subdir))

    return differences


def check() -> int:
    ensure_source()
    if not TARGET.is_dir():
        print(f"mirror missing: {TARGET}")
        return 1

    differences = compare_dirs(SOURCE, TARGET)
    if differences:
        print("mirror is out of sync")
        for difference in differences:
            print(difference)
        return 1

    print("root mirror is synchronized")
    return 0


def main() -> int:
    args = parse_args()
    if args.check:
        return check()

    sync()
    return check()


if __name__ == "__main__":
    raise SystemExit(main())
