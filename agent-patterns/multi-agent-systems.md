# Multi-Agent Systems / 多 Agent 系统

## 1. Delegation is not free / 委派不是免费的

**English.** Multiple agents help when subtasks are genuinely separable, require different tools or expertise, or benefit from independent review. They hurt when every agent needs the same context, tasks are tightly coupled, or the coordinator cannot verify outputs. The hidden cost is coordination: duplicated work, conflicting assumptions, context transfer, and false consensus.

**中文。** 当子任务确实可分离、需要不同工具或专长、或能够从独立审查中受益时，多 Agent 才有帮助。当每个 Agent 都需要相同上下文、任务高度耦合，或协调者无法验证输出时，多 Agent 反而有害。隐藏成本是协调：重复劳动、假设冲突、上下文传递和虚假共识。

## 2. Useful roles / 有价值的角色划分

| Role | Responsibility | 中文职责 |
| --- | --- | --- |
| Coordinator | Define objective, allocate work, resolve conflicts | 定义目标、分配任务、解决冲突 |
| Researcher | Gather and cite evidence | 搜集并引用证据 |
| Builder | Produce the artifact or code change | 产出文档或代码改动 |
| Verifier | Independently test claims or artifacts | 独立验证主张或产物 |
| Reviewer | Check scope, safety, and user impact | 检查范围、安全性与用户影响 |

## 3. Shared artifacts over chat / 用共享产物代替聊天

**English.** Agents should coordinate through explicit artifacts: task board, source table, API schema, design record, patch, test report, or decision log. A message such as “I think it is done” is not a handoff contract. A good handoff names the artifact, evidence, unresolved risks, and the acceptance test.

**中文。** Agent 应通过明确产物协作：任务板、来源表、API 模式、设计记录、补丁、测试报告或决策日志。“我觉得做完了”不是交接契约。好的交接要写明产物、证据、未解决风险和验收测试。

## 4. Independent review prevents correlated error / 独立审查防止相关性错误

**English.** If two agents receive the same prompt, same context, and same model, agreement is weak evidence—they may make the same mistake. Increase independence by assigning different evidence sources, different verification methods, or a reviewer who sees the artifact before the author’s rationale.

**中文。** 如果两个 Agent 接收相同提示词、相同上下文和相同模型，它们的一致性是弱证据——它们可能犯同一个错误。应通过不同证据来源、不同验证方法，或让审阅者先看产物再看作者理由，来提高独立性。

## 5. When to avoid multi-agent design / 何时不要使用多 Agent

Use a single bounded loop when the task is small, the work is sequential, or verification is cheap. Add another agent only when it creates a clear, measurable advantage in throughput, diversity of evidence, or independent verification.

当任务较小、工作必须顺序进行，或验证成本很低时，使用单一受限循环即可。只有当增加 Agent 能在吞吐量、证据多样性或独立验证上带来明确且可衡量的收益时，才应加入新的 Agent。

