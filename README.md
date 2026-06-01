# HandShake-Skill

HandShake-Skill 用来帮助 Codex、Claude Code 等 AI 编程工具在同一个项目中连续工作。它会在项目目录里建立一组轻量记录文件，让项目目标、当前进度、待办事项、验证结果和下一步保持可追踪。

当前版本：`2.0.0`

## 你可以用它做什么

- 在 Codex 和 Claude Code 之间切换同一个项目。
- 在多台电脑上继续同一个项目。
- 给长期项目保留清晰的当前状态、命令记录和验证结果。
- 把写作、课程材料、代码项目的进度保存在项目目录中。
- 用一份统一的状态文件替代分散的交接记录。

## 工作方式

HandShake 2.x 默认只维护一个面向 AI 工具的状态文件：

```text
docs/codex/STATUS.md
```

这个文件包含：

- 当前目标和项目状态
- 活跃待办
- 已完成事项
- 决策记录
- 风险和阻塞
- 环境说明
- 运行命令和验证结果
- Git 同步状态
- 按时间戳追加的会话日志

面向中文用户的记录放在：

```text
version/工作进度.md
version/版本迭代记录.md
```

`工作进度.md` 用来快速查看项目推进情况。`版本迭代记录.md` 只在版本或发布状态变化时更新。

## 安装到 Codex

从 GitHub 安装：

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

安装后，Codex 会使用仓库根目录的 `handshake/` 包。

## 安装到 Claude Code

在本仓库中测试 Claude Code 插件：

```text
claude --plugin-dir .
```

插件调用名：

```text
/handshake-skill:handshake
```

安装为 Claude Code standalone skill：

```text
python skills\handshake\scripts\install_claude_skill.py --dry-run
python skills\handshake\scripts\install_claude_skill.py --force
```

默认安装位置：

```text
%USERPROFILE%\.claude\skills\handshake
```

## 更新 HandShake

官方仓库：

```text
https://github.com/maxzrb/HandShake-Skill
```

从官方仓库更新本机 Codex 和 Claude Code 安装：

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --force
```

只更新 Codex：

```text
python skills\handshake\scripts\update_installed_skill.py --codex --force
```

只更新 Claude Code：

```text
python skills\handshake\scripts\update_installed_skill.py --claude --force
```

从下载的 GitHub zip 包更新：

```text
python skills\handshake\scripts\update_installed_skill.py --zip C:\Downloads\HandShake-Skill-main.zip --all --force
```

从已解压目录或本地仓库更新：

```text
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main --all --force
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main\handshake --all --force
```

覆盖安装前可以先预览：

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --dry-run
```

## 初始化一个项目

预览将要创建的文件：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --dry-run
```

创建缺失文件：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project
```

覆盖已有模板文件：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --force
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

已有同名文件时，初始化脚本默认跳过；只有使用 `--force` 时才覆盖。

## 检查项目记录

```text
python skills\handshake\scripts\check_project_handoff.py F:\my-project
```

检查内容包括：

- 必需文件是否存在
- `STATUS.md` 是否包含核心章节
- `STATUS.md` 和 `version/工作进度.md` 是否具备时间戳日志结构
- Git 状态是否可读取

## 文件说明

### `AGENTS.md`

项目内的通用入口文件。Codex 等工具会从这里了解项目记录位置和基本工作方式。

### `CLAUDE.md`

Claude Code 的项目入口文件。它会导入 `AGENTS.md`，避免同一套规则重复维护。

### `docs/codex/INDEX.md`

状态文件索引。它说明项目的状态入口是 `docs/codex/STATUS.md`。

### `docs/codex/STATUS.md`

项目状态主文件。日常的进度、待办、决策、命令、验证和下一步都集中在这里。

### `version/工作进度.md`

中文进度记录。适合用户快速查看项目做到哪里。

### `version/版本迭代记录.md`

中文版本记录。适合记录版本变化、发布结果和迁移说明。

## 从旧版记录迁移

旧版 HandShake 可能包含多个分散文件，例如：

```text
HANDOFF.md
TODO.md
DECISIONS.md
ENVIRONMENT.md
PROGRESS.zh-CN.md
PYTHON.md
PAPER.md
```

迁移到 2.x 时，可以把这些内容合并进 `docs/codex/STATUS.md`：

- `HANDOFF.md` 合并到会话日志
- `TODO.md` 合并到活跃待办
- `DECISIONS.md` 合并到决策记录
- `ENVIRONMENT.md` 和 `PYTHON.md` 合并到环境说明
- `PAPER.md` 合并到写作状态和待办
- `PROGRESS.zh-CN.md` 合并到 `version/工作进度.md`

迁移后，默认只需要维护 `STATUS.md`、`工作进度.md` 和 `版本迭代记录.md`。

## 常见用法

### 新项目

1. 安装 HandShake。
2. 在目标项目中运行初始化脚本。
3. 检查生成的 `docs/codex/STATUS.md`。
4. 正常使用 Codex 或 Claude Code 继续项目。

### 多台电脑

1. 每台电脑安装或更新 HandShake。
2. 项目文件通过 Git 或同步盘保持一致。
3. 切换电脑后先查看 `docs/codex/STATUS.md`。

### 离线或无法访问 GitHub

1. 在能联网的电脑下载 GitHub zip 包。
2. 把 zip 包复制到目标电脑。
3. 使用 `update_installed_skill.py --zip ...` 更新本机安装。

## 仓库结构

```text
handshake/          # 根目录 skill 包，适合 Codex 直接安装
skills/handshake/   # 开发和 Claude Code plugin 使用的主副本
scripts/            # 仓库维护脚本
```

普通使用通常只需要安装 skill 并初始化目标项目，不需要把整个 HandShake-Skill 仓库复制进业务项目。
