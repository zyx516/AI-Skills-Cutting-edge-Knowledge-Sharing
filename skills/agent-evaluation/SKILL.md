---
name: agent-evaluation
description: Design and run evaluations for LLM or agent workflows. Use when comparing prompts, tools, models, agent loops, or releases; when defining success criteria; or when analyzing agent failures, quality, cost, latency, and safety.
---

# Agent Evaluation / Agent 评测

## Workflow / 工作流

1. Define the target task distribution and the user-visible outcome.
2. Create a small but representative evaluation set: normal cases, boundary cases, adversarial cases, and known failures.
3. Specify scoring before running the agent: deterministic checks where possible, and a rubric or human review where necessary.
4. Record success rate together with cost, latency, tool errors, policy violations, and escalation rate.
5. Inspect failures by category; change one variable at a time before claiming improvement.
6. Keep a holdout set that is not used during prompt or workflow iteration.

## 中文说明

1. 明确目标任务的分布，以及用户最终能看到的结果。
2. 构建小而有代表性的评测集：正常案例、边界案例、对抗案例和已知失败案例。
3. 在运行 Agent 前先写好评分方式：能确定性检查的就确定性检查，不能的再使用评分标准或人工复核。
4. 除了成功率，还要记录成本、延迟、工具错误、策略违规与升级给人工的比例。
5. 按失败类别分析问题；每次只改一个变量，再判断是否真的变好。
6. 保留一份不参与提示词或工作流调优的留出集，防止“只对训练题变好”。

## Release gate / 发布门槛

Do not release because one impressive demo works. Release only when the target cases meet the acceptance threshold, critical failures have a mitigation or human gate, and regression checks are repeatable.

不要因为一个惊艳演示能成功就发布。应当在目标案例达到验收阈值、关键失败已有缓解措施或人工关卡、并且回归检查可重复时再发布。

