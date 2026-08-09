# Reflection, Memory & Evaluation / 反思、记忆与评测

## 1. Reflection is a controlled update, not self-praise / 反思是受控更新，不是自我表扬

**English.** Reflection converts outcome feedback into a concrete change for a future attempt. A useful reflection has four fields: observed failure, likely cause, evidence for the diagnosis, and one changed next action. “Be more careful” is not a reflection because it changes no state or policy.

**中文。** 反思是把结果反馈转化为下一次尝试中的具体改变。有效反思至少包含四项：观察到的失败、可能原因、诊断依据，以及一个改变后的下一步行动。“下次更仔细”不算反思，因为它没有改变任何状态或策略。

## 2. Memory needs a write policy / 记忆需要写入策略

**English.** Store only information likely to improve later decisions. A memory record should include content, source, confidence, scope, timestamp, and expiry/review policy. Do not automatically save every conversation or tool result: unfiltered memories produce retrieval noise, stale facts, and prompt-injection persistence.

**中文。** 只保存有望改善未来决策的信息。每条记忆都应包含内容、来源、可信度、适用范围、时间戳，以及过期或复核策略。不要自动保存所有对话和工具结果：未过滤的记忆会导致检索噪声、过时事实和提示注入的长期残留。

## 3. Retrieval is a decision / 检索本身也是决策

**English.** Retrieval should answer a current subquestion, not merely fill the context window. Rank candidates by relevance, reliability, recency, and importance; then show provenance to the model or verifier. When information is high-impact or volatile, re-check the original source rather than trusting an old memory summary.

**中文。** 检索应当回答当前的一个子问题，而不是单纯填满上下文。候选记忆应按相关性、可靠性、时效性和重要性排序，并把来源展示给模型或验证器。对于高影响或变化快的信息，应重新检查原始来源，而不是相信旧的记忆摘要。

## 4. Evaluation closes the learning loop / 评测让学习循环闭合

**English.** An agent should be evaluated on the task distribution it will actually face. Build an evaluation set with normal cases, boundary cases, adversarial inputs, and historical failures. Prefer deterministic validators for facts such as compilation, schemas, arithmetic, or file existence. Use rubrics and human review for open-ended quality, but audit evaluator disagreement and bias.

**中文。** Agent 应在它真实会遇到的任务分布上接受评测。评测集要包含正常案例、边界案例、对抗输入和历史失败案例。对编译、数据模式、算术或文件存在性等事实，优先使用确定性验证器；对开放式质量，可用评分标准和人工审阅，但要检查评分者的不一致与偏差。

## 5. Metrics and error analysis / 指标与错误分析

| Metric | What it exposes | 中文含义 |
| --- | --- | --- |
| Task success rate | Whether users get the target outcome | 用户是否得到目标结果 |
| Constraint / policy violation rate | Unsafe or unauthorized behavior | 是否发生不安全或未授权行为 |
| Verification pass rate | Whether outputs survive independent checks | 结果能否通过独立检查 |
| Cost and latency | Operational efficiency | 实际运行成本与等待时间 |
| Escalation rate | Where autonomy is insufficient or correctly limited | 自主能力不足或被正确限制的环节 |
| Regression rate | Whether a change broke old capabilities | 修改是否破坏已有能力 |

**English.** Do not average away failures. Cluster them: retrieval error, planning error, tool-call error, execution error, verifier error, or ambiguous requirement. Improve the narrowest component that explains the cluster, then test against a holdout set.

**中文。** 不要用平均分掩盖失败。应按错误聚类：检索错误、规划错误、工具调用错误、执行错误、验证器错误或需求歧义。优先改进最能解释该类失败的窄组件，再用留出集测试。

## 6. Reflection does not replace verification / 反思不能替代验证

**English.** A model can produce plausible explanations for why it failed, including explanations that are false. Treat reflection as a hypothesis generator. Promotion to memory or workflow policy should require evidence: a failing test, repeated trace pattern, source review, or human confirmation.

**中文。** 模型能为失败生成看似合理但实际错误的解释。应把反思当作假设生成器。只有在存在证据——例如失败测试、重复轨迹模式、来源审查或人工确认——时，才应把它提升为记忆或工作流策略。

