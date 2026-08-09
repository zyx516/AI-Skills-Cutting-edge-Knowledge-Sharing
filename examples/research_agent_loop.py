"""一个内置安全边界的小型 Agent 循环示例。

本示例刻意保持自包含。实际应用中，请用已获授权的搜索、数据库或代码工具
替换其中的模拟回调函数。
"""

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Observation:
    source: str
    text: str
    verified: bool


@dataclass
class AgentState:
    goal: str
    observations: list[Observation] = field(default_factory=list)
    lessons: list[str] = field(default_factory=list)
    iterations: int = 0


def plan_next_step(state: AgentState) -> str:
    if not state.observations:
        return "collect an authoritative source"
    if not any(item.verified for item in state.observations):
        return "verify the collected evidence"
    return "draft an answer with source links"


def run_research_loop(
    goal: str,
    collect: Callable[[str], Observation],
    verify: Callable[[Observation], bool],
    max_iterations: int = 3,
) -> AgentState:
    """运行一个有次数上限的“观察 → 行动 → 验证 → 决策”循环。

    循环本身不会执行宿主回调函数以外的副作用。生产系统应限制工具权限，
    并在发布、花费资金或访问敏感数据前请求人工批准。
    """
    state = AgentState(goal=goal)

    while state.iterations < max_iterations:
        state.iterations += 1
        step = plan_next_step(state)

        if step == "collect an authoritative source":
            state.observations.append(collect(goal))
            continue

        if step == "verify the collected evidence":
            latest = state.observations[-1]
            latest.verified = verify(latest)
            if not latest.verified:
                state.lessons.append("The first source was insufficient; seek independent evidence.")
                state.observations.append(collect(f"independent evidence for: {goal}"))
            continue

        # 完成条件：证据已通过验证，可以开始生成初稿。
        break

    return state


if __name__ == "__main__":
    fake_collect = lambda query: Observation("example.org", f"Evidence for {query}", False)
    fake_verify = lambda observation: observation.source == "example.org"
    result = run_research_loop("How should an agent use tools safely?", fake_collect, fake_verify)
    print(result)
