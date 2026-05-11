# HandShake-Skill

HandShake-Skill 是一个面向 AI 编程工具的项目交接工作流。它不是普通文档模板，而是让 Codex、Claude Code 等工具在交替接手同一个项目时，先读取同一组仓库内记录，再继续开发或写作。

当前版本：`1.7.1`

## 最近更新

- **1.7.0**：新增强制性启动 `git pull`、分步计划执行、每步完成后提醒提交。
- **1.6.0**：`version/工作进度.md` 升级为每次会话必需更新（增量追加不覆盖），`版本迭代记录.md` 要求先迁移历史再写入新版。

## 解决的问题

当一个项目在不同会话、不同电脑、不同目录或不同虚拟环境中继续推进时，新接手的 AI 工具经常不知道：

- 当前目标是什么；
- 上次改了哪些文件；
- 哪些命令跑过、哪些验证通过；
- 本地 Python 环境能不能沿用；
- 还有哪些阻塞、待办和下一步；
- 上一次是 Codex、Claude Code 还是用户自己在操作。

HandShake 通过 `AGENTS.md`、`CLAUDE.md` 和 `docs/codex/` 下的记录文件，把这些信息留在项目仓库里。

## 适用场景

- Codex 和 Claude Code 交替接手同一项目；
- 多台电脑开发同一项目；
- Python 项目跨虚拟环境继续开发；
- 论文写作项目跨会话继续推进；
- 长周期代码项目、写作项目或混合项目的会话续接。

## 不能保证的事情

- 不能自动解决 Git 冲突；
- 不能强制所有 AI 工具一定读取记录；
- 不能替代 `git commit`、branch、worktree 或人工同步习惯；
- 不能替代人工 review；
- 不能保证旧设备上的本地路径、虚拟环境和依赖状态在新设备上仍然可用。

## 仓库结构

```text
handshake/          # Codex GitHub 安装推荐路径
skills/handshake/   # Claude Code plugin 路径，也是仓库内主维护副本
scripts/            # 仓库维护脚本
```

项目模板会生成：

```text
AGENTS.md
CLAUDE.md
docs/codex/INDEX.md
docs/codex/STATUS.md
docs/codex/HANDOFF.md
docs/codex/TODO.md
docs/codex/DECISIONS.md
docs/codex/ENVIRONMENT.md
docs/codex/PROGRESS.zh-CN.md
docs/codex/PYTHON.md
docs/codex/PAPER.md
version/工作进度.md
version/版本迭代记录.md
```

其中 `PAPER.md`、`PYTHON.md` 是可选领域模板；`version/` 文件面向中文用户阅读，不作为 AI 工具的唯一依据。

## Codex 安装

从 GitHub 安装根目录镜像：

```text
python C:\Users\MAX2EB\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo maxzrb/HandShake-Skill --path handshake
```

安装后，在目标项目中可以这样要求 Codex：

```text
使用 HandShake 初始化这个项目的 AI 交接记录。先检查 git status，再创建缺失的 AGENTS.md、CLAUDE.md 和 docs/codex/ 记录。
```

## Claude Code 安装

开发本仓库时可以用 plugin 方式测试：

```text
claude --plugin-dir .
```

进入 Claude Code 后调用：

```text
/handshake-skill:handshake
```

长期使用可以安装为个人 Claude Code skill：

```text
python skills\handshake\scripts\install_claude_skill.py --dry-run
python skills\handshake\scripts\install_claude_skill.py --force
```

也可以安装到某个项目：

```text
python skills\handshake\scripts\install_claude_skill.py --project F:\my-project --force
```

初始化项目后，Claude Code 用户可以在项目中运行 `/memory`，检查 `CLAUDE.md` 是否被加载。模板里的 `CLAUDE.md` 会通过 `@AGENTS.md` 导入公共规则，避免两处规则重复维护。

## 初始化目标项目

先预览：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all --dry-run
```

确认后执行：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all
```

常用参数：

- `--python`：额外生成 `docs/codex/PYTHON.md`；
- `--paper`：额外生成 `docs/codex/PAPER.md`；
- `--all`：生成所有可选模板；
- `--dry-run`：只预览，不写文件；
- `--force`：覆盖已有同名文件，默认不会覆盖。

## 检查目标项目

检查关键交接文件、Git 状态、Python 版本和虚拟环境：

```text
python skills\handshake\scripts\check_project_handoff.py F:\my-project
```

这个脚本不联网，不需要管理员权限，不依赖符号链接。

## 每次开始任务的提示词

新项目初始化：

```text
使用 HandShake 初始化这个项目。先看 git status，再生成缺失的 AGENTS.md、CLAUDE.md 和 docs/codex/ 记录；不要覆盖已有文件。
```

Codex 接手 Claude Code 项目：

```text
请用 HandShake 接手这个项目。先读 AGENTS.md、docs/codex/INDEX.md、STATUS.md、HANDOFF.md、TODO.md、ENVIRONMENT.md，再看 git status，确认 Claude Code 上次做到哪里后再修改。
```

Claude Code 接手 Codex 项目：

```text
请按 HandShake 流程接手。先读 CLAUDE.md、AGENTS.md 和 docs/codex/INDEX.md，再读 STATUS.md、HANDOFF.md、TODO.md、ENVIRONMENT.md，检查 git status 后继续。
```

跨设备继续项目：

```text
我换了一台电脑继续这个项目。请先按 HandShake 读取记录，重点核对 ENVIRONMENT.md、HANDOFF.md、当前路径、Python/虚拟环境和 git status，再决定能否继续。
```

论文写作项目继续写作：

```text
请按 HandShake 继续论文写作。先读 AGENTS.md、docs/codex/INDEX.md、PAPER.md、STATUS.md、HANDOFF.md 和 DECISIONS.md，核对文献状态后再写。使用简体中文，语言自然规范，不要写成 AI 腔；不要编造引用，无法核验的信息标注“待人工复核”。
```

Python 项目换环境后继续开发：

```text
这个 Python 项目换了环境。请先按 HandShake 读取 ENVIRONMENT.md、PYTHON.md、STATUS.md 和 HANDOFF.md，检查 Python 版本、虚拟环境、依赖和测试命令，再继续开发。
```

## 每次结束任务的提示词

```text
请按 HandShake 收尾：最低更新 docs/codex/HANDOFF.md、STATUS.md 和 version/工作进度.md（追加不覆盖），记录本次修改文件、运行命令、验证结果、遗留问题和下一步。只有任务变化才更新 TODO.md，长期决策才更新 DECISIONS.md，环境变化才更新 ENVIRONMENT.md，版本号变化才更新 version/版本迭代记录.md。最后告诉我 git status 是否干净，是否建议现在提交。
```

## 最佳实践

- 一项任务结束后，先提交，或至少保持 `git diff` 清楚，再切换 Codex/Claude Code；
- 切换电脑前确认 `HANDOFF.md` 和 `STATUS.md` 已更新；
- 换 Python 环境后，不要直接沿用旧记录里的命令结果，先重新检查；
- 论文写作项目必须记录文献核查状态，不能把未核实引用写成已确认；正式文本尽量使用自然、规范、研究生能够写出的简体中文；
- `CLAUDE.md` 只放 Claude Code 专用入口说明，公共规则放在 `AGENTS.md`。

## Windows 注意事项

- 路径可以包含中文和空格，命令中建议给路径加引号；
- 不需要管理员权限；
- 不依赖 Windows 符号链接，`CLAUDE.md` 通过 `@AGENTS.md` 导入公共规则；
- 初始化脚本默认跳过已有文件，不会静默覆盖；
- `robocopy /MIR` 会镜像目录，使用前确认目标目录没有私人手改内容；
- 如果 Git 输出全局 ignore 权限警告，先看 `git status` 是否仍能正常返回项目状态。
