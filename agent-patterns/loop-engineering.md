# Loop Engineering / 循环工程

## 1. From prompt engineering to execution design / 从提示词工程到执行设计

**English.** Prompt engineering optimizes a single interaction. **Loop Engineering** designs the recurring execution cycle: what enters the loop, what state survives, which tools are legal, how output is checked, what happens after failure, and exactly when the system must stop or ask a human. It is an emerging engineering practice rather than one settled theory.

**中文。** 提示词工程优化的是一次交互；**Loop Engineering（循环工程）**设计的是持续执行的完整循环：什么进入循环、哪些状态可以保留、允许使用哪些工具、如何检查结果、失败后做什么，以及系统何时必须停止或请求人工帮助。它是一种新兴工程实践，而不是已经定论的单一理论。

## 2. A control-loop view / 用控制循环理解 Agent

**English.** A reliable agent loop resembles a feedback controller:

`goal and constraints → observe → estimate state → choose action → execute → measure result → compare with target → stop / revise / escalate`

The important detail is the **measurement** step. Without independent observations or tests, the agent only sees its own generated text and can repeatedly reinforce a mistaken plan. A verifier supplies an error signal: a compiler error, unit test, database constraint, source citation check, schema validation, or human review.

**中文。** 可靠的 Agent 循环类似反馈控制器：

`目标与约束 → 观察 → 估计状态 → 选择行动 → 执行 → 测量结果 → 与目标比较 → 停止 / 修改 / 升级`

最关键的是**测量**步骤。没有独立观察或测试时，Agent 只能看到自己生成的文本，很容易反复强化错误计划。验证器提供误差信号：编译错误、单元测试、数据库约束、来源引用检查、数据模式校验或人工审阅。

## 3. What the loop must specify / 循环必须明确的内容

| Design element | English explanation | 中文解释 |
| --- | --- | --- |
| Goal | A measurable target, not “do your best.” | 可衡量的目标，而不是“尽力做好”。 |
| Observation | Fresh evidence from the environment. | 来自环境的新证据。 |
| Action space | Explicitly allowed actions and parameters. | 明确允许的行动及参数范围。 |
| State | Structured task facts and artifacts. | 结构化的任务事实与产物。 |
| Verifier | A test or reviewer independent of the draft. | 独立于草稿的测试或审阅者。 |
| Budget | Limits on time, tokens, cost, retries, and side effects. | 对时间、Token、成本、重试和副作用的限制。 |
| Termination | Success, no-progress, budget exhaustion, or escalation. | 成功、没有进展、预算耗尽或升级给人工。 |

## 4. Failure recovery / 失败恢复

**English.** Retrying the same action after the same error is not recovery. After a bounded number of failures, the loop should classify the failure: missing information, invalid tool arguments, unmet precondition, conflicting evidence, unsafe request, or insufficient capability. The next action must change the information, plan, tool, or authority—not merely regenerate text.

**中文。** 在相同错误后重复同一行动，不叫恢复。经过有限次数失败后，循环应分类错误：信息缺失、工具参数无效、前置条件不满足、证据冲突、请求不安全或能力不足。下一步必须改变信息、计划、工具或授权范围，而不能只是重新生成一段文字。

## 5. Example: coding agent / 示例：编码 Agent

**English.** A safe loop is: inspect the issue and repository → state the suspected cause → change the smallest relevant file → run targeted tests → inspect the diff → either finish with evidence or ask for approval before a public push. The test output and diff are the observations; the acceptance criteria are the stopping rule.

**中文。** 一个安全的编码循环是：检查问题和仓库 → 写出怀疑原因 → 只修改最相关的文件 → 运行针对性测试 → 检查 diff → 带着证据完成，或在公开推送前请求批准。测试输出和 diff 是观察结果；验收标准就是停止规则。

