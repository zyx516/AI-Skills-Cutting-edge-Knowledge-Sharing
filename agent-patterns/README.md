# Agent Patterns / Agent 理论与模式

An agent is a decision-and-execution system around a model. The model proposes language and actions; the surrounding system supplies state, tools, verification, limits, and accountability.

Agent 是围绕模型构建的决策与执行系统。模型提出语言与行动；外围系统提供状态、工具、验证、限制与可追责性。

## Reading map / 阅读地图

| Topic | Core question / 核心问题 |
| --- | --- |
| [Agent Architecture & State](agent-architecture.md) | What components turn an LLM into an agent? / 什么组件让 LLM 成为 Agent？ |
| [Loop Engineering](loop-engineering.md) | How should an agent make bounded, verifiable progress? / 如何让 Agent 在受限条件下持续且可验证地推进？ |
| [ReAct & Tool Use](react-and-tool-use.md) | How should reasoning, actions, and observations interact? / 推理、行动与观察如何配合？ |
| [Planning & Search](planning-and-search.md) | When should an agent plan, branch, backtrack, or re-plan? / 何时规划、分支、回溯与重规划？ |
| [Reflection, Memory & Evaluation](reflection-memory-evaluation.md) | How can feedback improve later decisions without poisoning context? / 如何让反馈改进决策而不污染上下文？ |
| [Multi-Agent Systems](multi-agent-systems.md) | When does delegation help, and when does it create coordination debt? / 何时该协作，何时会产生协调债务？ |

## Agent loop / Agent 循环

`Goal → Observe → Update state → Plan → Act → Verify → Decide (finish / retry / escalate)`

The loop is not intelligence by itself. It is an execution harness that makes the model’s decisions inspectable and bounded.

循环本身不是智能；它是一个执行框架，使模型的决策可检查、可限制。

