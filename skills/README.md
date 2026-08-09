# AI Skills Directory / 实用 Skills 目录

A **skill** is a reusable operating procedure, not merely a prompt. In a Codex-compatible skill, the English `name` and `description` in `SKILL.md` are discovery metadata; the body tells an agent what to inspect, which tools to use, how to validate, and when to stop.

**Skill（技能）**是一套可复用的操作流程，不只是提示词。在兼容 Codex 的 Skill 中，`SKILL.md` 里的英文 `name` 和 `description` 用于发现与触发；正文则告诉 Agent 要检查什么、调用哪些工具、如何验证、何时停止。

## Reusable skills in this repository / 本仓库可复用的 Skills

| Skill | Trigger / 触发场景 | What it does / 功能 |
| --- | --- | --- |
| [web-research-and-citations](web-research-and-citations/SKILL.md) | Research current facts, compare sources, or prepare cited notes | 用一手来源完成可追溯研究，并把事实与推断分开 |
| [agent-evaluation](agent-evaluation/SKILL.md) | Design tests or evaluate an LLM/agent workflow | 构建代表性任务集、评分规则、失败分析与发布门槛 |
| [safe-tool-use](safe-tool-use/SKILL.md) | Give an agent browser, shell, API, or data-access tools | 设计权限边界、工具契约、验证与人工审批关卡 |

## High-value skill categories / 高价值 Skill 分类

| English skill name | 中文用途 | Recommended workflow / 推荐流程 |
| --- | --- | --- |
| **Web Research & Citation** | 有来源意识的网页研究 | 明确待验证结论 → 优先一手来源 → 记录链接与日期 → 区分事实和推断 |
| **Document Intelligence** | 文档与 PDF 提取 | 提取文字 → 检查表格、图像与页码 → 保留原始文件 → 标出无法确认的部分 |
| **Codebase Orientation** | 快速理解陌生代码库 | 阅读项目说明 → 找入口文件 → 检查测试与配置 → 写清楚假设 |
| **Test-Driven Debugging** | 小范围调试 | 复现 → 缩小原因范围 → 添加或调整测试 → 做最小安全修改 |
| **Code Review** | 审查改动风险 | 检查正确性、安全性、边界条件、测试与可维护性；按影响程度排序 |
| **GitHub Publishing** | 安全发布代码和文档 | 检查 diff → 仅暂存目标文件 → 提交 → 推送 → 说明验证方式 |
| **Evaluation Design** | 比较提示词、模型或 Agent | 定义成功标准 → 准备代表性案例 → 评分 → 分析失败，而不只看平均分 |
| **Security Review** | 数据、凭据和网络操作 | 找出信任边界 → 最小权限 → 验证输入 → 增加负面测试 |
| **Task Decomposition** | 多步骤工作 | 把目标拆为可验证的子任务 → 显式写出依赖关系 → 为每步设置完成条件 |
| **Tool Routing** | 选择搜索、代码、数据库或 API | 定义输入输出契约 → 校验参数 → 记录观察 → 处理工具失败 |
| **Human-in-the-Loop Approval** | 具有现实影响的操作 | 识别不可逆步骤 → 暂停 → 展示证据与影响 → 获取明确批准 |

## What makes a good `SKILL.md`? / 好的 `SKILL.md` 应具备什么？

1. **Discoverability / 可发现性**：使用清晰、具体的英文 `name` 与 `description`，写出它解决什么问题和何时触发。
2. **Procedural knowledge / 流程知识**：记录通用模型不一定知道的步骤、工具顺序、项目规则或数据约束。
3. **Validation / 验证**：说明如何检查结果，而不是只告诉 Agent “完成任务”。
4. **Boundaries / 边界**：写出权限、隐私、成本、停止条件和需要人工批准的情形。
5. **Progressive disclosure / 渐进加载**：核心流程保持简洁；较长的细节放到 `references/` 或 `scripts/` 中按需读取。

