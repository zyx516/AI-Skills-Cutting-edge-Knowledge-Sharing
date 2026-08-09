---
name: safe-tool-use
description: Design and operate safe tool-using AI agents. Use when an agent can call a browser, shell, API, database, filesystem, or external service; when defining tool permissions, input validation, verification, audit logs, stopping rules, or human approval gates.
---

# Safe Tool Use / 安全工具使用

## Tool contract / 工具契约

For every tool, define: purpose, accepted inputs, output schema, allowed side effects, authorization scope, timeout, cost limit, error behavior, and evidence to retain.

为每个工具定义：用途、可接受输入、输出模式、允许的副作用、授权范围、超时、成本上限、错误行为和需要保留的证据。

## Execution rules / 执行规则

1. Give the agent the minimum privilege required for the current step.
2. Validate tool arguments before execution; never let natural-language text become an unrestricted command.
3. Treat tool output as evidence to inspect, not as automatically trusted truth.
4. Limit retries and require a different plan or escalation after repeated failure.
5. Require human approval before irreversible, external-facing, financial, private-data, or broad destructive actions.

1. 只给 Agent 完成当前步骤所需的最小权限。
2. 在执行前校验工具参数；不要让自然语言直接变成不受限制的命令。
3. 把工具输出当作需要检查的证据，而不是自动可信的真相。
4. 限制重试次数；连续失败后必须采用不同方案或升级给人工。
5. 在不可逆、对外发布、涉及资金、私密数据或大范围破坏的操作前，要求人工批准。

