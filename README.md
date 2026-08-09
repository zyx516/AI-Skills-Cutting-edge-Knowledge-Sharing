# AI Skills & Agent Systems / AI Skills 与 Agent 系统

> A bilingual, practical knowledge base for reusable AI skills and reliable agent design.<br>
> 一个面向实践的双语知识库：收集可复用的 AI Skills 与可靠 Agent 的设计方法。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: English + 中文](https://img.shields.io/badge/language-English%20%2B%20中文-blue.svg)](#)

## Start here / 从这里开始

This repository deliberately keeps **English names and keywords** for discoverability, while placing a Chinese explanation directly below each concept. It is meant to be useful both to people searching GitHub and to Chinese readers who want to understand the mechanism.

本仓库刻意保留**英文名称和关键词**，方便在 GitHub 上被搜索到；每个核心概念下方紧跟中文解释，方便中文读者理解其工作机制。

| Area / 模块 | What it contains / 内容 |
| --- | --- |
| [AI Skills Directory](skills/README.md) | Discoverable skill names, Chinese usage guidance, and reusable `SKILL.md` examples / 可检索的 Skill 名称、中文使用说明和可复用范例 |
| [Agent Patterns](agent-patterns/README.md) | Architecture, loops, planning, tool use, memory, evaluation, and multi-agent coordination / Agent 架构、循环、规划、工具、记忆、评测与多 Agent 协作 |
| [Research Agent Loop Example](examples/research_agent_loop.py) | A small bounded loop that demonstrates observation, verification, and stopping conditions / 展示观察、验证与停止条件的受限循环 |
| [References](references.md) | Primary papers and first-party sources / 原始论文与一手资料 |

## Core thesis / 核心观点

An LLM is not automatically an agent. An agent is an LLM embedded in an execution system: it has goals, state, tools, feedback, constraints, and a stopping rule. Reliability comes from that system design—not from asking the model to sound more confident.

LLM 本身并不自动等于 Agent。Agent 是被嵌入执行系统中的 LLM：它有目标、状态、工具、反馈、约束和停止规则。可靠性来自系统设计，而不是要求模型“说得更自信”。

## Suggested reading path / 推荐阅读顺序

1. Read [Agent Architecture & State](agent-patterns/agent-architecture.md) to understand the system boundary.
2. Read [Loop Engineering](agent-patterns/loop-engineering.md) and [ReAct & Tool Use](agent-patterns/react-and-tool-use.md) for the execution loop.
3. Read [Planning & Search](agent-patterns/planning-and-search.md), [Reflection, Memory & Evaluation](agent-patterns/reflection-memory-evaluation.md), and [Multi-Agent Systems](agent-patterns/multi-agent-systems.md) for deeper patterns.
4. Browse [AI Skills Directory](skills/README.md) and adapt a real skill for a recurring task.

## Scope and safety / 范围与安全

- The notes are educational and tool-agnostic.
- “Loop Engineering” is an emerging engineering practice, not one settled academic theory.
- Production agents require access control, privacy review, evaluation, observability, and human approval for consequential actions.

- 本仓库用于学习，尽量不绑定单一平台。
- “Loop Engineering（循环工程）”是一种新兴工程实践，不是已经定论的单一学术理论。
- 生产级 Agent 还需要访问控制、隐私审查、评测、可观测性，以及对高影响操作的人类批准。

## Credits / 致谢

This is a personal learning collection organized with AI assistance. Please use Issues or Pull Requests to correct claims, add primary sources, or improve translations.

这是一个在 AI 协助下整理的个人学习资料库。欢迎通过 Issue 或 Pull Request 修正内容、补充一手资料或改进翻译。
