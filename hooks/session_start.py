#!/usr/bin/env python3
"""Emit lightweight HandShake startup context for plugin hooks."""

from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def additional_context() -> str:
    return (
        "<HANDSHAKE_PLUGIN_CONTEXT>\n"
        "HandShake is available in this repository as a multi-agent continuity skill.\n"
        "Use skills/handshake/SKILL.md for the authoritative workflow. "
        "Use AGENTS.md for repository maintenance rules when editing this skill repository.\n"
        "For target projects, initialize or read AGENTS.md, CLAUDE.md, "
        "docs/codex/INDEX.md, docs/codex/STATUS.md, version/工作进度.md, "
        "and version/版本迭代记录.md. Treat docs/codex/STATUS.md as the "
        "single AI-facing source of truth and append timestamped session logs.\n"
        "</HANDSHAKE_PLUGIN_CONTEXT>"
    )


def main() -> int:
    context = additional_context()
    if os.environ.get("CLAUDE_PLUGIN_ROOT"):
        payload = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": context,
            }
        }
    else:
        payload = {"additional_context": context}

    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
