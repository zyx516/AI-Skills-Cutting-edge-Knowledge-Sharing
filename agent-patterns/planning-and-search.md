# Planning & Search / 规划与搜索

## 1. Planning is useful when actions have dependencies / 有依赖关系时才需要规划

**English.** A plan is a hypothesis about how subgoals lead to a goal. It is valuable when actions depend on one another, cost is high, or an early mistake is expensive. For small, well-specified tasks, planning overhead can be worse than acting directly. The right question is not “should every agent plan?” but “does planning reduce expected rework enough to justify its cost?”

**中文。** 计划是关于“子目标如何通向最终目标”的假设。当行动相互依赖、成本较高，或早期错误代价很大时，计划才有价值。对于小而明确的任务，规划开销可能反而比直接行动更差。正确的问题不是“每个 Agent 是否都应规划”，而是“规划减少的返工，是否足以覆盖它的成本？”

## 2. Plan-and-Solve / 先规划再求解

**English.** Plan-and-Solve separates decomposition from execution. First, produce a checklist of subproblems and their dependencies; then solve each item while checking whether the plan still matches observations. This reduces missing-step errors, but a plan must be revisable—otherwise the agent follows a fluent but obsolete plan after the environment changes.

**中文。** Plan-and-Solve（先规划再求解）把拆解与执行分开：先生成子问题清单及其依赖关系，再逐项解决，并持续检查计划是否仍符合观察结果。它能减少漏步骤，但计划必须可修改；否则环境已经变化时，Agent 仍会流畅地执行过时计划。

## 3. Search and branching / 搜索与分支

**English.** Some tasks have high branching risk: debugging multiple plausible causes, designing an architecture, or solving a combinatorial problem. A single reasoning path commits too early. Tree-of-Thought-style search generates several coherent partial paths, evaluates them against a criterion, then expands, prunes, or backtracks. It trades latency and cost for better exploration.

**中文。** 有些任务分支风险很高，例如存在多个合理原因的调试、架构设计或组合问题。单一路径会过早承诺。类似 Tree of Thoughts 的搜索会生成多个连贯的部分路径，按标准进行评估，然后扩展、剪枝或回溯。它以更高的延迟和成本，换取更好的探索能力。

## 4. Practical decision table / 实用决策表

| Situation | Preferred pattern | 中文建议 |
| --- | --- | --- |
| One clear action and cheap verification | Act → verify | 直接行动后验证，不必过度规划 |
| Several dependent subtasks | Plan → execute → re-plan | 先拆解，再执行，根据观察重规划 |
| Several plausible approaches | Branch → evaluate → prune | 并行提出路径，评估后剪枝 |
| High-impact irreversible action | Plan → evidence review → human gate | 先规划和核验证据，再请求人工批准 |
| Repeated failure | Diagnose class of failure → change strategy | 先分类失败，再改变策略，不要机械重试 |

## 5. A plan needs exit criteria / 计划需要退出条件

**English.** Stop searching when a candidate meets explicit acceptance criteria, additional branches have low expected value, or the budget is exhausted. “Keep thinking until confident” is not an operational rule; confidence is neither calibrated nor a substitute for evidence.

**中文。** 当候选方案满足明确验收标准、额外分支的预期价值很低，或预算耗尽时，应停止搜索。“一直想直到有信心”为止不是可操作的规则；信心既未必校准，也不能替代证据。

