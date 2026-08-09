# Agent 理论与模式

AI Agent 最有价值的用法，是把它当作一个系统，而不是一次模型调用。它需要目标、状态、工具、反馈、约束和停止规则。

## 主题目录

- [Loop Engineering（循环工程）](loop-engineering.md)：如何设计 Agent 重复执行的完整循环。
- [ReAct 与工具使用](react-and-tool-use.md)：如何让推理、行动和观察交替进行。
- [反思、记忆与评测](reflection-memory-evaluation.md)：如何从反馈中学习，而不是盲目地反复尝试。

## 一个简化模型

`目标 → 规划 → 行动 → 观察 → 验证 → 决策（停止 / 重试 / 升级给人）`

只有当 Agent 拥有明确限制时，循环才是安全的：允许使用的工具、预算、时间、隐私规则和审批关卡。

