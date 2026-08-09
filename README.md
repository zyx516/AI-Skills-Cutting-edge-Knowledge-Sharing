# AI Skills 前沿知识分享

> 一个面向实践的中文知识库：整理 AI Skills 与 Agent 系统中可复用的方法、理论和示例。

[![许可证：MIT](https://img.shields.io/badge/许可证-MIT-yellow.svg)](LICENSE)
[![语言：中文](https://img.shields.io/badge/语言-中文-blue.svg)](#)

## 仓库内容

这个仓库不是单篇文章，而是一个可以持续补充的小型知识库。每个主题都有独立文档、参考来源；Agent 部分还提供了可以改造的代码示例。

| 模块 | 内容 |
| --- | --- |
| [实用 Skills 目录](skills/README.md) | 按功能分类的常用 Skill 与使用流程 |
| [Agent 理论与模式](agent-patterns/README.md) | 构建可靠 Agent 的核心理论与实践模式 |
| [循环示例](examples/research_agent_loop.py) | 带安全边界的研究型 Agent 循环示例 |
| [参考资料](references.md) | 本仓库理论说明对应的原始资料 |
| [贡献指南](CONTRIBUTING.md) | 如何添加新的知识笔记与示例 |

## 为什么要整理这些内容？

好的 AI 实践通常不只是“把提示词写得更好”。它需要清晰的目标、合适的工具、可核验的证据、验证机制、记忆，以及明确的停止条件。

## 阅读顺序

1. 先从 [实用 Skills 目录](skills/README.md) 找到与你任务接近的分类。
2. 再阅读 [Agent 理论与模式](agent-patterns/README.md)，了解这些流程背后的设计思想。
3. 最后参考 [研究型 Agent 循环示例](examples/research_agent_loop.py)，将它改造成自己的工具流程。

## 使用范围说明

- 本仓库主要用于学习与交流，尽量不绑定单一工具或平台。
- 文中的 **Loop Engineering（循环工程）** 是一种新兴 Agent 工程实践，并非已经定论的单一学术理论。
- 示例展示的是通用模式。生产环境仍需要权限控制、隐私审查、评测，以及对关键操作的人类批准。

## 致谢

这是一个个人学习资料库，并在 AI 协助下完成整理。每篇内容中均给出了参考资料；欢迎通过 Issue 或 Pull Request 指出错误、补充来源或更新过时内容。
