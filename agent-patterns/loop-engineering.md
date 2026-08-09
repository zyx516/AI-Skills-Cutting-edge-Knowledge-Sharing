# Loop Engineering

## English

**Loop Engineering** is an emerging practice for designing the cycle an agent runs, rather than optimizing only one prompt. A useful loop gives an agent a goal, a bounded context, permitted tools, independent checks, durable state, and clear decisions to stop, retry, or ask a person for help.

At each pass, the agent should:

1. **Observe** the task state and available evidence.
2. **Plan** the smallest useful next action.
3. **Act** through an allowed tool or produce a bounded artifact.
4. **Verify** the result with a test, source, schema, policy, or reviewer.
5. **Decide** whether to finish, revise, retry with new evidence, or escalate.

This moves the design question from “What prompt gives the best answer?” to “What system can produce evidence-backed progress without running indefinitely or taking unsafe actions?” In practice, a coding agent may inspect a repository, change one file, run targeted tests, review the diff, and stop or request approval before pushing.

### Design checklist

- Define a measurable completion condition.
- Put a time, cost, and iteration budget on the loop.
- Record observations and decisions so a later step can audit them.
- Use independent verification where possible; self-critique alone is weak evidence.
- Add a human approval gate before irreversible, private, financial, or external-facing actions.

## 中文说明

**Loop Engineering（循环工程）**是一种新兴的 Agent 工程实践：它关注如何设计 Agent 反复执行的完整循环，而不只优化一次提示词。一个好的循环会为 Agent 提供目标、受限上下文、允许调用的工具、独立校验、可持续保存的状态，以及“停止、重试或向人求助”的明确决策。

每一轮可按照以下流程进行：

1. **观察**任务状态与可用证据。
2. **规划**最小且有价值的下一步。
3. **行动**：调用已授权工具或生成范围受控的产物。
4. **验证**：用测试、来源、数据模式、策略或人工审阅检查结果。
5. **决策**：完成、修改、带着新证据重试，或升级给人类处理。

它把问题从“哪个提示词能得到最好的回答？”转换为“如何设计一个能持续产出可验证进展、不会无限运行、也不会做出不安全操作的系统？”例如，编码 Agent 可以先检查仓库，只修改一个文件，运行针对性测试，审查 diff，再决定停止，或在推送之前请求批准。

### 设计清单

- 为任务定义可衡量的完成条件。
- 为循环设置时间、成本和迭代次数预算。
- 记录观察结果与决策，便于后续步骤审计。
- 尽量使用独立验证；仅靠模型自我批评不是强证据。
- 在不可逆、涉及隐私、财务或对外发布的操作前设置人工批准关卡。

## Further reading

- IBM, [What Is Loop Engineering?](https://www.ibm.com/think/topics/loop-engineering)

