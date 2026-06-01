# HandShake-Skill

HandShake-Skill 是一个面向 Codex、Claude Code 等 AI 编程工具的项目连续性 skill。它把项目当前状态、待办、验证结果和下一步集中记录在仓库内，方便同一项目在不同会话、不同工具或不同电脑之间继续推进。

当前版本：`2.0.0`

## 主要变化

- `2.0.0`：默认记录模型改为单一 `docs/codex/STATUS.md`，不再默认维护 `HANDOFF.md`、`TODO.md`、`DECISIONS.md`、`ENVIRONMENT.md`、`PROGRESS.zh-CN.md`、`PYTHON.md` 和 `PAPER.md`。
- `2.0.0`：新增安装更新脚本，可从官方仓库、下载的 zip 包或本地目录更新 Codex / Claude Code 中已安装的 HandShake。
- `1.8.0`：优化自动触发描述，覆盖继续、接手、收尾、换设备、换环境等常见场景。

## 适用场景

- 一个项目需要在 Codex 和 Claude Code 之间交替处理。
- 同一项目会在多台电脑、多个目录或不同虚拟环境中继续。
- 长周期代码项目需要保留清晰的当前状态、命令记录、验证结果和下一步。
- 写作、课程材料或混合项目需要把进度和版本变化保存在项目目录中。

## 默认生成文件

```text
AGENTS.md
CLAUDE.md
docs/codex/INDEX.md
docs/codex/STATUS.md
version/工作进度.md
version/版本迭代记录.md
```

文件用途：

- `docs/codex/STATUS.md`：AI 工具使用的唯一项目状态记录，包含当前摘要、待办、决策、风险、环境说明、命令、验证、Git 状态和时间戳日志。
- `version/工作进度.md`：面向中文用户的进度记录，使用时间戳追加日志。
- `version/版本迭代记录.md`：面向中文用户的版本变化记录，仅在版本或发布状态变化时更新。
- `AGENTS.md`：项目内通用规则入口。
- `CLAUDE.md`：Claude Code 项目入口，导入 `AGENTS.md` 并补充 Claude Code 相关说明。
- `docs/codex/INDEX.md`：状态记录索引，明确 `STATUS.md` 是必读入口。

旧版分散记录可以迁移到 `STATUS.md`：`HANDOFF.md` 对应会话日志，`TODO.md` 对应待办，`DECISIONS.md` 对应决策，`ENVIRONMENT.md` / `PYTHON.md` 对应环境说明，`PAPER.md` 对应写作状态。

## Codex 安装

从 GitHub 安装根目录 skill 包：

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

安装后，`handshake/` 会作为可用 skill 放入 Codex 的 skills 目录。

## Claude Code 安装

开发或测试插件时，可在仓库根目录运行：

```text
claude --plugin-dir .
```

Claude Code 内的调用名：

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

## 更新已安装的 HandShake

官方仓库：

```text
https://github.com/maxzrb/HandShake-Skill
```

从官方仓库更新当前电脑上的 Codex 和 Claude Code 安装：

```text
python skills\handshake\scripts\update_installed_skill.py --latest --all --force
```

`--latest` 会使用官方仓库 `https://github.com/maxzrb/HandShake-Skill.git`，默认缓存目录为：

```text
%USERPROFILE%\.codex\skill-sources\HandShake-Skill
```

从下载的 GitHub zip 包更新：

```text
python skills\handshake\scripts\update_installed_skill.py --zip C:\Downloads\HandShake-Skill-main.zip --all --force
```

从已解压目录或本地 clone 更新：

```text
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main --all --force
python skills\handshake\scripts\update_installed_skill.py --source C:\Downloads\HandShake-Skill-main\handshake --all --force
```

只更新一个运行环境：

```text
python skills\handshake\scripts\update_installed_skill.py --codex --force
python skills\handshake\scripts\update_installed_skill.py --claude --force
```

所有覆盖安装都可以先使用 `--dry-run` 预览。

## 初始化目标项目

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

初始化脚本默认跳过已有文件，只有传入 `--force` 时才覆盖同名文件。

## 检查目标项目

```text
python skills\handshake\scripts\check_project_handoff.py F:\my-project
```

检查内容包括：

- 必需文件是否存在。
- `STATUS.md` 是否包含核心章节。
- `STATUS.md` 和 `version/工作进度.md` 是否具备时间戳日志结构。
- 当前 Git 状态是否可读取。

## 仓库结构

```text
handshake/          # 根目录镜像，用于 Codex 直接安装
skills/handshake/   # 主维护副本，用于开发和 Claude Code plugin
scripts/            # 仓库维护脚本
```

每次发布前需要保持 `skills/handshake/` 和 `handshake/` 内容同步。

## 发布说明

HandShake 按语义化版本发布。改变默认记录模型、启动流程或收尾流程属于破坏性变更，需要提升主版本号。正式发布需要同步两个 skill 路径、完成校验、提交代码，并推送分支和匹配的 annotated tag。
