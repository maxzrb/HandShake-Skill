#!/usr/bin/env python3
"""Update installed HandShake skill copies from local, Git, or zip sources."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


LOCAL_SKILL_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_REPO = "https://github.com/maxzrb/HandShake-Skill.git"
DEFAULT_CACHE_ROOT = Path.home() / ".codex" / "skill-sources"
DEFAULT_REPO_CACHE = DEFAULT_CACHE_ROOT / "HandShake-Skill"
DEFAULT_CODEX_TARGET = Path.home() / ".codex" / "skills" / "handshake"
DEFAULT_CLAUDE_TARGET = Path.home() / ".claude" / "skills" / "handshake"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Update installed HandShake skill directories from this package, "
            "a local source path, a Git repository, or a downloaded zip archive."
        )
    )
    source = parser.add_argument_group("source")
    source.add_argument(
        "--latest",
        action="store_true",
        help="Use the canonical HandShake-Skill GitHub repository.",
    )
    source.add_argument(
        "--source",
        help=(
            "Local source path. Accepts a HandShake repository root, the "
            "root-level handshake package, or skills/handshake."
        ),
    )
    source.add_argument(
        "--zip",
        dest="zip_path",
        help="Downloaded HandShake-Skill zip archive to extract and install from.",
    )
    source.add_argument(
        "--repo",
        nargs="?",
        const=CANONICAL_REPO,
        help=(
            "Git repository URL to clone or pull. Defaults to the canonical "
            "HandShake-Skill repository when no URL is supplied."
        ),
    )
    source.add_argument(
        "--cache-dir",
        default=str(DEFAULT_REPO_CACHE),
        help=(
            "Local clone directory for --repo. Defaults to "
            "~/.codex/skill-sources/HandShake-Skill."
        ),
    )

    targets = parser.add_argument_group("targets")
    targets.add_argument(
        "--codex",
        action="store_true",
        help="Update ~/.codex/skills/handshake.",
    )
    targets.add_argument(
        "--claude",
        action="store_true",
        help="Update ~/.claude/skills/handshake.",
    )
    targets.add_argument(
        "--all",
        action="store_true",
        help="Update both Codex and Claude Code personal skill directories.",
    )
    targets.add_argument(
        "--target",
        action="append",
        default=[],
        help=(
            "Additional explicit target directory. Must resolve to a "
            "'skills/handshake' directory."
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing target skill directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing files.",
    )
    return parser.parse_args()


def run_command(args: list[str], cwd: Path | None = None) -> None:
    completed = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.stdout:
        print(completed.stdout.strip())
    if completed.returncode != 0:
        raise RuntimeError(f"command failed ({completed.returncode}): {' '.join(args)}")


def selected_targets(args: argparse.Namespace) -> list[Path]:
    targets: list[Path] = []
    if args.all or args.codex:
        targets.append(DEFAULT_CODEX_TARGET)
    if args.all or args.claude:
        targets.append(DEFAULT_CLAUDE_TARGET)
    targets.extend(Path(target).expanduser() for target in args.target)
    return [target.resolve() for target in targets]


def source_option_count(args: argparse.Namespace) -> int:
    return sum(bool(value) for value in [args.latest, args.source, args.zip_path, args.repo])


def locate_skill_source(root: Path) -> Path:
    root = root.expanduser().resolve()
    candidates = [
        root,
        root / "handshake",
        root / "skills" / "handshake",
    ]

    if root.is_dir():
        for child in root.iterdir():
            if child.is_dir():
                candidates.extend(
                    [
                        child,
                        child / "handshake",
                        child / "skills" / "handshake",
                    ]
                )

    for candidate in candidates:
        if (candidate / "SKILL.md").is_file() and (candidate / "scripts").is_dir():
            return candidate.resolve()

    raise FileNotFoundError(f"could not locate HandShake skill package under: {root}")


def prepare_repo_source(args: argparse.Namespace) -> Path:
    repo_url = CANONICAL_REPO if args.latest else (args.repo or CANONICAL_REPO)
    cache_dir = Path(args.cache_dir).expanduser().resolve()

    if args.dry_run:
        if cache_dir.exists():
            print(f"would run git pull --ff-only in {cache_dir}")
            return locate_skill_source(cache_dir)
        print(f"would clone {repo_url} into {cache_dir}")
        return cache_dir / "handshake"

    if cache_dir.exists():
        if not (cache_dir / ".git").is_dir():
            raise FileExistsError(f"cache dir exists but is not a Git repository: {cache_dir}")
        print(f"updating repo cache: {cache_dir}")
        run_command(["git", "pull", "--ff-only"], cwd=cache_dir)
    else:
        cache_dir.parent.mkdir(parents=True, exist_ok=True)
        print(f"cloning repo: {repo_url}")
        run_command(["git", "clone", repo_url, str(cache_dir)])

    return locate_skill_source(cache_dir)


def prepare_zip_source(args: argparse.Namespace) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    zip_path = Path(args.zip_path).expanduser().resolve()
    if not zip_path.is_file():
        raise FileNotFoundError(f"zip archive not found: {zip_path}")

    temp_dir = tempfile.TemporaryDirectory(prefix="handshake-skill-")
    extract_root = Path(temp_dir.name)
    print(f"{'would inspect' if args.dry_run else 'extracting'} zip archive: {zip_path}")
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(extract_root)
    return locate_skill_source(extract_root), temp_dir


def prepare_source(args: argparse.Namespace) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    count = source_option_count(args)
    if count > 1:
        raise ValueError("choose only one source option: --latest, --source, --zip, or --repo")

    if args.latest or args.repo:
        return prepare_repo_source(args), None
    if args.zip_path:
        return prepare_zip_source(args)
    if args.source:
        return locate_skill_source(Path(args.source)), None
    return LOCAL_SKILL_ROOT.resolve(), None


def validate_source(skill_source: Path, *, dry_run: bool = False) -> None:
    if dry_run and not skill_source.exists():
        return
    if not (skill_source / "SKILL.md").is_file():
        raise FileNotFoundError(f"skill source missing SKILL.md: {skill_source}")
    if not (skill_source / "scripts").is_dir():
        raise FileNotFoundError(f"skill source missing scripts directory: {skill_source}")


def validate_target(target: Path, skill_source: Path) -> None:
    source = skill_source.resolve()
    if target.name != "handshake" or target.parent.name != "skills":
        raise ValueError(f"target must be a skills/handshake directory: {target}")
    if target == source:
        raise ValueError(f"target is the source package: {target}")
    if source in target.parents:
        raise ValueError(f"target is inside the source package: {target}")


def copy_skill(
    skill_source: Path,
    target: Path,
    *,
    force: bool,
    dry_run: bool,
) -> list[str]:
    validate_target(target, skill_source)
    messages: list[str] = []

    existed = target.exists()
    action = "overwrite" if existed else "create"

    if existed and not force:
        messages.append(f"skip existing {target}")
        messages.append("use --force to overwrite")
        return messages

    if dry_run:
        messages.append(f"would {action} {target}")
        return messages

    if existed:
        shutil.rmtree(target)

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        skill_source,
        target,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    messages.append(f"{'overwrote' if existed else 'created'} {target}")
    return messages


def main() -> int:
    args = parse_args()
    targets = selected_targets(args)

    if not targets:
        print("no target selected; use --codex, --claude, --all, or --target")
        return 2

    temp_dir: tempfile.TemporaryDirectory[str] | None = None
    try:
        skill_source, temp_dir = prepare_source(args)
        validate_source(skill_source, dry_run=args.dry_run)
        print(f"source: {skill_source}")

        seen: set[Path] = set()
        for target in targets:
            if target in seen:
                continue
            seen.add(target)
            print(f"target: {target}")
            for message in copy_skill(
                skill_source,
                target,
                force=args.force,
                dry_run=args.dry_run,
            ):
                print(message)
    finally:
        if temp_dir is not None:
            temp_dir.cleanup()

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
