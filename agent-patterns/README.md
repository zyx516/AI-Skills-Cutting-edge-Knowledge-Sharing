# Agent Patterns / Agent 理论与模式

An AI agent is most useful when it is treated as a system, not a single model call. It needs an objective, state, tools, feedback, constraints, and a stopping rule.

当 AI Agent 被当作一个系统、而不是一次模型调用时，才最有价值。它需要目标、状态、工具、反馈、约束和停止规则。

## Topics

- [Loop Engineering](loop-engineering.md): designing the recurring execution cycle.
- [ReAct](react-and-tool-use.md): interleaving reasoning, actions, and observations.
- [Reflection, memory, and evaluation](reflection-memory-evaluation.md): learning from feedback without blindly repeating work.

## A compact model

\`Goal → Plan → Act → Observe → Verify → Decide (stop / retry / escalate)\`

The loop is only safe when the agent has explicit limits: allowed tools, budget, time, privacy rules, and approval gates.

只有当 Agent 拥有明确限制时，循环才是安全的：允许使用的工具、预算、时间、隐私规则和审批关卡。

