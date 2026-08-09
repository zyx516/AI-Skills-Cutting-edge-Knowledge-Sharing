# ReAct and Tool Use

## English

**ReAct** combines reasoning with actions in an interleaved sequence. Instead of producing a full answer from internal knowledge alone, an agent can reason about a next step, call a search/API/code tool, observe the result, and update its plan. This pattern is helpful when the environment—not only the model’s parameters—contains the evidence needed to solve the task.

**Tool use** gives the agent specialized capabilities: a calculator for arithmetic, a database for records, a browser for current information, a compiler for code, or a calendar for scheduling. A tool result is still input, not truth by default. The system should validate arguments, constrain permissions, handle failure, and cite or preserve relevant evidence.

### How AI uses it

For a research question, an agent might first break the question into claims, search primary sources, extract the supporting passages, compare them, and write an answer that labels any inference. For a coding task, it might inspect files, apply a small patch, run tests, then use the test result as the next observation.

## 中文说明

**ReAct** 将推理与行动交替结合。Agent 不必只根据内部知识一次性生成完整答案，而可以先思考下一步，调用搜索、API 或代码工具，观察结果，再更新计划。当解决问题所需证据存在于外部环境，而不只存在于模型参数中时，这种模式很有帮助。

**工具使用（Tool Use）**为 Agent 提供专门能力：用计算器算数、用数据库查记录、用浏览器获取最新信息、用编译器验证代码，或用日历安排时间。工具返回的结果仍是输入，默认不应被直接视为真相。系统需要校验参数、限制权限、处理失败，并保留或引用关键证据。

### AI 如何使用

面对研究问题时，Agent 可以先把问题拆成多个待验证的主张，搜索一手资料，提取支撑段落，进行比较，再写出明确标注推断的回答。面对编码任务时，它可以检查文件、应用小型补丁、运行测试，然后把测试结果作为下一轮观察。

## Further reading

- Yao et al., [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- Schick et al., [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)

