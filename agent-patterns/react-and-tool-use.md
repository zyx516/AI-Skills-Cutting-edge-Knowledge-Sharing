# ReAct & Tool Use / ReAct 与工具使用

## 1. The ReAct pattern / ReAct 模式

**English.** ReAct interleaves reasoning, action, and observation. The agent uses an internal task model to choose a next action; the environment returns an observation; the observation can confirm, contradict, or refine the plan. This is fundamentally different from generating a long answer first and checking it later.

**中文。** ReAct 把推理、行动和观察交替进行。Agent 根据内部的任务模型选择下一步行动；环境返回观察；观察可以确认、否定或细化计划。这与先生成长答案、最后再检查完全不同。

`Reason / 推理 → Action / 行动 → Observation / 观察 → Updated state / 更新状态`

## 2. Tools are contracts, not magic powers / 工具是契约，不是魔法能力

**English.** A tool should expose a narrow schema: name, purpose, input types, permission scope, output schema, timeout, cost, and side effects. The agent should not receive raw shell access when it only needs “run this approved test,” and it should not receive production database write access when a read-only query is enough.

**中文。** 工具应暴露一个范围明确的契约：名称、用途、输入类型、权限范围、输出模式、超时、成本和副作用。Agent 如果只需要“运行这个已批准的测试”，就不该获得原始 Shell 权限；如果只需要只读查询，就不该得到生产数据库写权限。

## 3. Evidence pipeline / 证据管线

**English.** Tool output is not automatically true. A browser may return outdated information, an API may return an error-shaped success object, and a database row may not match the question’s scope. For factual tasks, keep a chain: claim → source/tool result → extraction → verification → cited conclusion. For code, keep: requirement → patch → test result → diff review → release decision.

**中文。** 工具输出不会自动成为事实。浏览器可能返回过时信息，API 可能返回“看起来成功”的错误对象，数据库行也可能与问题范围不匹配。对于事实性任务，应保留链条：主张 → 来源/工具结果 → 信息提取 → 验证 → 带引用的结论。对于代码任务，应保留：需求 → 补丁 → 测试结果 → diff 审查 → 发布决策。

## 4. Tool-error handling / 工具错误处理

**English.** Separate execution failure from task failure. A timeout means “try a safer retrieval strategy,” not “the claim is false.” A permission error means “authority is missing,” not “invent a workaround.” Repeated failures should consume a retry budget and trigger re-planning or escalation.

**中文。** 要区分工具执行失败和任务结论失败。超时意味着“改用更安全的检索策略”，不意味着“这条主张是假的”；权限错误意味着“缺少授权”，不意味着“编造绕过方法”。重复失败应消耗重试预算，并触发重规划或升级给人工。

## 5. Prompt injection and authority / 提示注入与权限

**English.** Untrusted tool output must never redefine the agent’s authority. Web pages, documents, emails, and tool responses are data unless a trusted policy explicitly says otherwise. Put policies outside the retrieved text, validate actions against those policies, and require approval for external or irreversible effects.

**中文。** 不可信的工具输出绝不能重新定义 Agent 的权限。网页、文档、邮件和工具返回值默认都是数据，除非可信策略另有规定。应把策略放在检索文本之外，再用策略校验行动；对外部或不可逆影响必须要求批准。

