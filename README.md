# HandShake-Skill

当前版本：`2.1.0-beta`

HandShake-Skill 用来让 Codex、Claude Code、Cursor、Gemini CLI、OpenCode 等 AI 编程工具在同一个项目里连续工作。它的核心很简单：在目标项目里维护一份面向 AI 的 `docs/codex/STATUS.md`，再用中文 `version/` 记录给用户看得懂的进度和版本变化。

## 多平台入口

| 平台 | 入口 |
| --- | --- |
| Codex | `handshake/` 根层镜像，用于 GitHub skill 安装 |
| Claude Code | `.claude-plugin/plugin.json` 或 standalone skill |
| Cursor | `.cursor-plugin/plugin.json` |
| Gemini CLI | `GEMINI.md` |
| OpenCode | `.opencode/INSTALL.md` |
| 通用 agent | `AGENTS.md` 与根层兼容 `SKILL.md` |

本仓库的权威 skill 包是 `skills/handshake/`，`handshake/` 是给 Codex 直接安装用的镜像。开发时先改 `skills/handshake/`，再运行：

```text
python scripts\sync_root_mirror.py
```

## 安装到 Codex

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

## Claude Code

在本仓库中测试插件：

```text
claude --plugin-dir .
```

插件调用名：

```text
/handshake-skill:handshake
```

安装为 standalone skill：

```text
python skills\handshake\scripts\install_claude_skill.py --dry-run
python skills\handshake\scripts\install_claude_skill.py --force
```

默认安装位置：

```text
%USERPROFILE%\.claude\skills\handshake
```

## Cursor / Gemini / OpenCode

Cursor plugin 元数据位于：

```text
.cursor-plugin\plugin.json
```

Gemini CLI 从 `GEMINI.md` 路由到：

```text
skills/handshake/SKILL.md
```

OpenCode 安装说明位于：

```text
.opencode\INSTALL.md
```

Claude/Cursor 插件共享 `hooks/session_start.py`。session-start hook 只注入轻量路由说明，真正执行时仍应读取当前 `SKILL.md`、项目 `AGENTS.md` 和目标项目的 `docs/codex/STATUS.md`。

## 初始化目标项目

预览将创建的文件：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --dry-run
```

创建缺失文件：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project
```

初始化后，目标项目会包含：

```text
AGENTS.md
CLAUDE.md
docs/codex/INDEX.md
docs/codex/STATUS.md
version/工作进度.md
version/版本迭代记录.md
```

`docs/codex/STATUS.md` 是唯一面向 AI 的项目状态来源。`version/工作进度.md` 是中文用户进度记录，`version/版本迭代记录.md` 只在版本或发布状态变化时更新。

## 检查目标项目

```text
python skills\handshake\scripts\check_project_handoff.py F:\my-project
```

检查内容包括必需文件、`STATUS.md` 结构、时间戳日志和 Git 状态。

## 更新已安装的 HandShake

从官方仓库更新本机 Codex 和 Claude Code 安装：

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --force
```

从当前本地仓库预览或安装：

```text
python skills\handshake\scripts\update_installed_skill.py --source . --all --dry-run
python skills\handshake\scripts\update_installed_skill.py --source . --all --force
```

从下载的 GitHub zip 包更新：

```text
python skills\handshake\scripts\update_installed_skill.py --zip C:\Downloads\HandShake-Skill-main.zip --all --force
```

安装脚本会识别仓库根目录、`handshake/` 或 `skills/handshake/`，并验证目标确实是完整 HandShake skill 包，避免把根层兼容 `SKILL.md` 当成可安装包。

## 仓库结构

```text
skills/handshake/   # 权威开发包
handshake/          # Codex GitHub 安装镜像
.claude-plugin/     # Claude Code plugin manifest
.cursor-plugin/     # Cursor plugin manifest
hooks/              # plugin session-start hook
.codex/             # Codex 安装说明
.opencode/          # OpenCode 安装说明
scripts/            # 仓库维护脚本
```

## 发布前验证

```text
python scripts\sync_root_mirror.py --check
python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\handshake
python C:\Users\MAX2EB\.codex\skills\.system\skill-creator\scripts\quick_validate.py handshake
python -m json.tool .claude-plugin\plugin.json
python -m json.tool .cursor-plugin\plugin.json
python -m json.tool hooks\hooks.json
python -m json.tool hooks\hooks-cursor.json
python -m py_compile skills\handshake\scripts\init_project_handoff.py skills\handshake\scripts\check_project_handoff.py skills\handshake\scripts\install_claude_skill.py skills\handshake\scripts\update_installed_skill.py hooks\session_start.py
git diff --check
```
