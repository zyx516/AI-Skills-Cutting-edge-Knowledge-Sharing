"""A small, safe-by-design agent-loop sketch.

This example is intentionally self-contained. Replace the fake callbacks with
approved search, database, or code tools in a real application.
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
    """Run a bounded observe → act → verify → decide loop.

    The loop does not perform side effects beyond callbacks supplied by the host.
    A production system should enforce tool permissions and ask a human before
    publishing, spending money, or accessing sensitive data.
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

        # Completion condition: evidence has been verified and a draft can be made.
        break

    return state


if __name__ == "__main__":
    fake_collect = lambda query: Observation("example.org", f"Evidence for {query}", False)
    fake_verify = lambda observation: observation.source == "example.org"
    result = run_research_loop("How should an agent use tools safely?", fake_collect, fake_verify)
    print(result)

