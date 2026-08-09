# Practical Skills Catalog / 实用技能目录

A **skill** is a repeatable workflow: it describes what to inspect, which tools to use, how to verify the result, and when to stop. The value is not a clever prompt alone; it is a dependable process.

**Skill（技能）**是一套可重复执行的工作流：它说明要检查什么、调用哪些工具、如何验证结果以及何时停止。它的价值不只是一个巧妙的提示词，而是一套可靠流程。

## 1. Research & knowledge retrieval / 研究与知识检索

| Skill | Best for | A good workflow |
| --- | --- | --- |
| Source-aware web research | Current facts, product comparison, academic exploration | Form a query → prefer primary sources → record links and dates → distinguish facts from inference |
| Document/PDF extraction | Turning reports into searchable notes | Extract text → inspect tables/figures → cite page numbers → preserve the original file |
| Literature mapping | Learning a new technical topic | Start from surveys or seminal work → follow citations → group ideas by problem, method, and limitation |

**使用提示：**先定义“我需要验证的结论是什么”，再搜索。对于会变化的信息，记录来源链接和访问日期；不要把搜索摘要当作证据本身。

## 2. Software delivery / 软件交付

| Skill | Best for | A good workflow |
| --- | --- | --- |
| Repository orientation | An unfamiliar codebase | Read project instructions → map entry points → inspect tests and configuration → state assumptions |
| Surgical debugging | A reproducible defect | Reproduce → isolate the smallest cause → add/adjust a test → make the smallest safe change |
| Code review | Preventing regressions | Check correctness, security, edge cases, tests, and maintainability; rank findings by impact |
| Git/GitHub publishing | Sharing work safely | Inspect the diff → commit only intended files → push a branch → describe purpose and validation in the PR |

**使用提示：**把“能运行”与“被验证”区分开。一个改动应当有可复现的检查，例如测试、类型检查、构建或手工验收步骤。

## 3. Quality, safety & evaluation / 质量、安全与评测

| Skill | Best for | A good workflow |
| --- | --- | --- |
| Evaluation design | Comparing prompts, agents, or models | Define success criteria → prepare representative cases → score outputs → inspect failures, not just averages |
| Security review | Code that handles data, credentials, or network access | Identify trust boundaries → check authorization and input handling → minimize privileges → add negative tests |
| Output verification | High-impact answers or actions | Cross-check against independent evidence → state uncertainty → request human approval when consequences are material |

**使用提示：**评测集应覆盖正常路径、边界条件和失败路径。不要只用模型自己生成的“容易题”来证明它可靠。

## 4. Communication & knowledge artifacts / 沟通与知识产物

| Skill | Best for | A good workflow |
| --- | --- | --- |
| Technical writing | READMEs, guides, and design notes | Lead with the outcome → explain decisions and trade-offs → add examples → keep links current |
| Document/slides production | A deliverable that must look correct | Draft structure → generate artifact → render visually → revise layout and wording → final review |
| Data storytelling | A chart or dashboard that supports a decision | Verify data → choose one question per visual → label units and caveats → explain the decision implication |

**使用提示：**选择最小且清晰的表达形式。复杂关系可用表格或流程图；简单结论通常一句话即可。

## 5. Agent orchestration / Agent 编排

| Skill | Best for | A good workflow |
| --- | --- | --- |
| Task decomposition | Multi-step work | Turn the goal into independently checkable steps; keep dependencies explicit |
| Tool routing | Choosing search, code, database, or API tools | Define tool contracts → validate arguments → log observations → handle tool failures deliberately |
| Human-in-the-loop gates | Actions with real-world consequences | Identify irreversible or high-impact steps → pause → show evidence → obtain explicit approval |

See [Agent Patterns](../agent-patterns/README.md) for the theory behind these workflows.

