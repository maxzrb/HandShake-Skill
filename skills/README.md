# HandShake Skill

中文说明在前，English instructions follow.

## 中文使用说明

### 1. 这里是不是可以直接使用的成品？

是。`skills/` 文件夹中当前可用的成品是：

```text
skills/
  handshake/
```

这个 skill 已通过结构校验：

```text
Skill is valid!
```

当前版本：

```text
1.1.1
```

它是一个自包含 skill，包含：

```text
handshake/
  SKILL.md                         # Codex 会读取的核心 skill 说明
  agents/openai.yaml               # skill 的界面元数据
  scripts/init_project_handoff.py  # 初始化目标项目的脚本
  assets/project-template/         # 要复制到目标项目的模板
  references/                      # 协议、模板、版本规则说明
```

### 2. 这个 skill 解决什么问题？

它用于解决多个电脑、多个 Codex 会话之间项目交接困难的问题。

它会让 Codex 在开始工作前先查看项目规则和项目状态，在结束工作前更新交接记录。这样下一台电脑或下一次 Codex 会话可以知道：

- 当前项目目标是什么。
- 上一次做到哪里。
- 哪些文件被改过。
- 哪些命令跑过。
- 哪些测试通过或没跑。
- 还有什么待办、阻塞和下一步。

### 3. 适合哪些项目？

适合：

- Python 开发项目。
- 论文写作项目。
- 同时包含代码和论文的项目。
- 需要在多台电脑上继续推进的项目。
- 需要 Codex 每次启动都先读项目记录的项目。

### 4. 推荐的使用方式

有两种使用方式。

#### 方式 A：在当前仓库中使用

如果你只想在当前这个仓库里使用，不需要安装到全局，直接让 Codex 使用：

```text
Use the HandShake skill in skills/handshake.
```

然后让 Codex 初始化目标项目，例如：

```text
python skills\handshake\scripts\init_project_handoff.py F:\path\to\your-project --all
```

#### 方式 B：安装为全局 skill

如果你想在所有项目中都使用它，需要把整个文件夹放到 Codex 的全局 skills 目录。

Windows 常见目录：

```text
C:\Users\<你的用户名>\.codex\skills\
```

当前机器通常可以使用：

```text
C:\Users\maxzr\.codex\skills\
```

要安装时，应保留完整目录结构：

```text
C:\Users\maxzr\.codex\skills\
  handshake\
    SKILL.md
    agents\
    scripts\
    assets\
    references\
```

安装后，新的 Codex 会话就可以在任意项目中通过描述触发这个 skill，例如：

```text
使用 HandShake 初始化这个项目的 Codex 交接记录。
```

#### 方式 C：其他电脑如何更新全局 HandShake

建议每台电脑都保留一份本 GitHub 仓库克隆，然后把仓库里的 `skills/handshake/` 同步到全局 Codex skills 目录。

第一次在某台电脑配置：

```text
git clone https://github.com/maxzrb/HandShake.git
cd HandShake
robocopy skills\handshake "$env:USERPROFILE\.codex\skills\handshake" /MIR
```

以后当你在主电脑更新 HandShake 并推送到 GitHub 后，其他电脑这样更新：

```text
cd HandShake
git pull --ff-only
robocopy skills\handshake "$env:USERPROFILE\.codex\skills\handshake" /MIR
```

注意：

- `git pull --ff-only` 只接受正常快进更新，能避免意外合并。
- `robocopy /MIR` 会让全局 skill 目录完全等于仓库中的 `skills/handshake/`。
- 不要在 `$env:USERPROFILE\.codex\skills\handshake` 里保留私人手改内容；要改就改仓库，再提交和推送。
- 更新后开启新的 Codex 会话，通常就会读取新版 skill。

### 5. 如何初始化一个目标项目？

进入本仓库目录后运行：

```text
python skills\handshake\scripts\init_project_handoff.py <目标项目路径> --all
```

例子：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all
```

执行后，目标项目会得到：

```text
AGENTS.md
docs/codex/INDEX.md
docs/codex/STATUS.md
docs/codex/HANDOFF.md
docs/codex/DECISIONS.md
docs/codex/TODO.md
docs/codex/ENVIRONMENT.md
docs/codex/PYTHON.md
docs/codex/PAPER.md
version/工作进度.md
version/版本迭代记录.md
```

### 6. 初始化脚本参数

```text
--python
```

只额外加入 Python 项目模板 `docs/codex/PYTHON.md`。

```text
--paper
```

只额外加入论文写作模板 `docs/codex/PAPER.md`。

```text
--all
```

加入所有可选模板。推荐新手使用这个参数。

```text
--dry-run
```

只预览会创建哪些文件，不实际写入。第一次使用时建议先跑这个。

```text
--force
```

覆盖目标项目中已经存在的同名文件。这个参数要谨慎使用。

### 7. 新手推荐流程

第一次给某个项目启用交接协议时，推荐这样做：

1. 先预览：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all --dry-run
```

2. 确认输出没问题后正式初始化：

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all
```

3. 打开目标项目，让 Codex 接管时说：

```text
请使用 HandShake 流程，先读取 AGENTS.md 和 docs/codex/INDEX.md，再继续工作。
```

4. 每次结束较大工作时，让 Codex 更新交接：

```text
请按 HandShake 流程更新 docs/codex/HANDOFF.md、STATUS.md 和 TODO.md。
```

### 8. 每个文件的作用

`AGENTS.md`：
项目规则入口。Codex 每次进入项目时应该先读它。

`docs/codex/INDEX.md`：
项目状态索引。告诉 Codex 接下来该读哪些状态文件。

`docs/codex/STATUS.md`：
当前项目状态。记录当前目标、进度、风险和同步状态。

`docs/codex/HANDOFF.md`：
交接说明。记录本次做了什么、改了什么、验证了什么、下一步是什么。

`docs/codex/TODO.md`：
待办清单。记录活跃任务、等待事项、已完成事项和放弃事项。

`docs/codex/DECISIONS.md`：
决策记录。记录长期有效的设计选择和原因。

`docs/codex/ENVIRONMENT.md`：
环境说明。记录安装、运行、测试命令和本地环境差异。

`docs/codex/PYTHON.md`：
Python 项目专用说明。记录 Python 版本、依赖管理、运行命令、测试命令等。

`docs/codex/PAPER.md`：
论文写作专用说明。记录论文结构、章节状态、引用核查、图表和待验证论断。

`version/工作进度.md`：
面向中文用户的可读进度说明。它帮助用户快速了解项目推进情况，但不是 Codex 的项目管理依据。

`version/版本迭代记录.md`：
面向中文用户的版本变化记录。它帮助用户了解版本变化、影响和验证情况，但不是 Codex 的项目管理依据。

### 9. 注意事项

- 默认不会覆盖目标项目已有文件。
- 如果看到 `skip existing`，表示已有文件被保留。
- 不要把 API key、密码、token 写进 `docs/codex/`。
- 如果多个电脑开发，建议把这些交接文件提交到 Git。
- 如果目标项目还不是 Git 仓库，这个流程仍可使用，但跨设备同步需要你自己保证。
- 管理流程 skill 必须按版本发布，不能静默改写已发布版本。
- `version/` 下的两个中文文档只给用户阅读；Codex 自身管理仍依赖 `AGENTS.md`、`docs/codex/` 和 Git 状态。

## English Instructions

### 1. Is this a ready-to-use output?

Yes. The ready-to-use skill in this folder is:

```text
skills/
  handshake/
```

It has passed skill validation:

```text
Skill is valid!
```

Current version:

```text
1.1.1
```

The skill is self-contained:

```text
handshake/
  SKILL.md                         # Main skill instructions for Codex
  agents/openai.yaml               # UI metadata
  scripts/init_project_handoff.py  # Target project initializer
  assets/project-template/         # Templates copied into target projects
  references/                      # Protocol, templates, and versioning rules
```

### 2. What problem does it solve?

It helps Codex continue project work across multiple PCs and multiple Codex sessions.

Before work starts, Codex reads project rules and project state. Before work ends, Codex updates the handoff records. The next session can then understand:

- The current goal.
- What was done last.
- Which files changed.
- Which commands were run.
- What was verified.
- What remains blocked.
- What should happen next.

### 3. Suitable projects

Use it for:

- Python development projects.
- Academic writing projects.
- Mixed code and paper projects.
- Projects continued across multiple computers.
- Projects where Codex must read local project records before working.

### 4. Usage options

#### Option A: Use from this repository

Tell Codex:

```text
Use the HandShake skill in skills/handshake.
```

Then initialize a target project:

```text
python skills\handshake\scripts\init_project_handoff.py F:\path\to\your-project --all
```

#### Option B: Install globally

Put the full `handshake/` folder into your global Codex skills directory.

Common Windows location:

```text
C:\Users\<your-user-name>\.codex\skills\
```

On this machine, that is usually:

```text
C:\Users\maxzr\.codex\skills\
```

Keep the full structure:

```text
C:\Users\maxzr\.codex\skills\
  handshake\
    SKILL.md
    agents\
    scripts\
    assets\
    references\
```

After global installation, you can use it in any project by asking:

```text
Use HandShake to initialize Codex handoff records for this project.
```

#### Option C: Update HandShake On Other PCs

Recommended setup: keep one clone of this GitHub repository on each PC, then mirror `skills/handshake/` into the global Codex skills directory.

First-time setup on another PC:

```text
git clone https://github.com/maxzrb/HandShake.git
cd HandShake
robocopy skills\handshake "$env:USERPROFILE\.codex\skills\handshake" /MIR
```

After you update HandShake on the main PC and push to GitHub, update another PC with:

```text
cd HandShake
git pull --ff-only
robocopy skills\handshake "$env:USERPROFILE\.codex\skills\handshake" /MIR
```

Notes:

- `git pull --ff-only` avoids accidental merge commits.
- `robocopy /MIR` makes the global skill folder exactly match `skills/handshake/` from the repository.
- Do not keep private manual edits inside `$env:USERPROFILE\.codex\skills\handshake`; edit the repository, then commit and push.
- Start a new Codex session after updating so the new skill version is loaded.

### 5. Initialize a target project

From this repository, run:

```text
python skills\handshake\scripts\init_project_handoff.py <target-project-path> --all
```

Example:

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all
```

The target project will receive:

```text
AGENTS.md
docs/codex/INDEX.md
docs/codex/STATUS.md
docs/codex/HANDOFF.md
docs/codex/DECISIONS.md
docs/codex/TODO.md
docs/codex/ENVIRONMENT.md
docs/codex/PYTHON.md
docs/codex/PAPER.md
version/工作进度.md
version/版本迭代记录.md
```

### 6. Script options

```text
--python
```

Also include the Python workflow template: `docs/codex/PYTHON.md`.

```text
--paper
```

Also include the academic writing template: `docs/codex/PAPER.md`.

```text
--all
```

Include all optional templates. Recommended for beginners.

```text
--dry-run
```

Preview changes without writing files.

```text
--force
```

Overwrite existing files. Use with care.

### 7. Beginner workflow

1. Preview first:

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all --dry-run
```

2. Initialize:

```text
python skills\handshake\scripts\init_project_handoff.py F:\my-project --all
```

3. In the target project, ask Codex:

```text
Use the HandShake workflow. Read AGENTS.md and docs/codex/INDEX.md before continuing.
```

4. Before ending substantial work, ask Codex:

```text
Update docs/codex/HANDOFF.md, STATUS.md, and TODO.md according to the HandShake workflow.
```

### 8. What each generated file does

`AGENTS.md`:
Project instruction entrypoint. Codex should read it first.

`docs/codex/INDEX.md`:
State index. Tells Codex which project records to read.

`docs/codex/STATUS.md`:
Current status, goal, risks, and synchronization notes.

`docs/codex/HANDOFF.md`:
Latest handoff: completed work, changed files, verification, blockers, and next steps.

`docs/codex/TODO.md`:
Active, waiting, done, and dropped tasks.

`docs/codex/DECISIONS.md`:
Durable project decisions and rationale.

`docs/codex/ENVIRONMENT.md`:
Setup, run, test commands, and local environment differences.

`docs/codex/PYTHON.md`:
Python-specific setup, dependency, run, test, lint, and project layout notes.

`docs/codex/PAPER.md`:
Academic writing structure, chapter status, citation verification, figures, and unsupported claims.

`version/工作进度.md`:
Chinese user-facing progress summary. It helps the user understand project progress, but it is not Codex's project management source of truth.

`version/版本迭代记录.md`:
Chinese user-facing version history. It helps the user understand version changes, impact, and verification, but it is not Codex's project management source of truth.

### 9. Notes

- Existing files are skipped by default.
- `skip existing` means the existing target file was preserved.
- Do not store API keys, passwords, or tokens in `docs/codex/`.
- For cross-device work, commit these handoff files to Git when appropriate.
- If the target project is not a Git repository, the workflow still works, but synchronization is your responsibility.
- Management workflow skills must be released with explicit versions and must not silently rewrite released versions.
- The two files under `version/` are for users to read; Codex management still depends on `AGENTS.md`, `docs/codex/`, and Git state.
