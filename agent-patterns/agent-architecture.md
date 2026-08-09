# Agent Architecture & State / Agent 架构与状态

## 1. The system boundary / 系统边界

**English.** An LLM becomes an agent only when it can repeatedly observe a changing environment, choose an allowed action, receive feedback, and update state toward a goal. A useful abstraction is:

`Agent = Model + Policy + State + Tools + Environment + Verifier + Budget + Human gates`

The model generates candidates; the **policy** decides which phase it is in and what actions are allowed; **state** carries task facts across turns; tools affect or inspect the environment; a verifier checks whether an output is acceptable; budgets and gates bound autonomy.

**中文。** 只有当 LLM 能反复观察变化中的环境、选择被允许的行动、接收反馈，并围绕目标更新状态时，它才构成 Agent。可以用下面的抽象理解：

`Agent = 模型 + 策略 + 状态 + 工具 + 环境 + 验证器 + 预算 + 人工关卡`

模型负责提出候选方案；**策略**决定当前处于哪个阶段、允许做什么；**状态**保存跨轮次的任务事实；工具用于检查或影响环境；验证器判断结果是否合格；预算和人工关卡限制自主范围。

## 2. State is not just chat history / 状态不等于聊天记录

**English.** Long chat history is a poor database: it is costly, ambiguous, and vulnerable to stale instructions. Separate state by purpose:

| State type | Purpose | Example |
| --- | --- | --- |
| Working state | Immediate task context | current hypothesis, open subtask, tool arguments |
| Artifact state | Durable task outputs | a patch, report draft, test result, source list |
| Episodic memory | What happened before | failed API call and its error, prior decision |
| Semantic memory | Reusable facts | repository conventions, validated domain facts |
| Procedural memory | Reusable method | a checked deployment or research workflow |

**中文。** 长聊天记录并不是好数据库：它成本高、语义含混，还容易把过期指令带进当前任务。应按用途区分状态：

| 状态类型 | 用途 | 例子 |
| --- | --- | --- |
| 工作状态 | 当前任务的即时上下文 | 当前假设、未完成子任务、工具参数 |
| 产物状态 | 可持续保存的任务输出 | 补丁、报告草稿、测试结果、来源列表 |
| 情景记忆 | 之前发生了什么 | 失败的 API 调用及错误、历史决策 |
| 语义记忆 | 可复用的事实 | 仓库规范、已验证的领域事实 |
| 程序记忆 | 可复用的方法 | 已检查过的部署或研究工作流 |

## 3. State update discipline / 状态更新纪律

**English.** Every state write should answer: who wrote it, from what evidence, for what scope, when does it expire, and how can it be corrected? This prevents an agent from turning a one-off observation into permanent “knowledge.” Retrieval should rank candidates by relevance, recency, reliability, and task scope—not by semantic similarity alone.

**中文。** 每次写入状态前，都应回答：谁写入的、基于什么证据、适用于什么范围、何时过期、如何更正？这样能防止 Agent 把一次性的观察误当作永久“知识”。检索时应同时考虑相关性、时效性、可靠性和任务范围，而不只看语义相似度。

## 4. Failure modes / 常见失败模式

**English.** Context rot occurs when irrelevant history crowds out the current goal. Memory poisoning occurs when untrusted text is saved as instruction or fact. State drift occurs when the artifact and the agent’s description of it disagree. The practical mitigation is to keep structured source-of-truth artifacts, attach provenance to memory, and re-read the actual environment before consequential actions.

**中文。** 当无关历史挤占当前目标时，会发生上下文腐化；当不可信文本被保存为指令或事实时，会发生记忆投毒；当实际产物与 Agent 对产物的描述不一致时，会发生状态漂移。实用的缓解方式是：维护结构化的事实源、为记忆附上来源，并在关键操作前重新读取真实环境。

