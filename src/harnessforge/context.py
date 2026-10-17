from dataclasses import dataclass
from typing import Sequence, Set

@dataclass(frozen=True)
class ContextSnapshot:
    required_facts: Set[str]
    active_facts: Set[str]
    tokens_used: int
    token_budget: int

    @property
    def utilization(self) -> float:
        if self.token_budget <= 0:
            raise ValueError("token_budget must be > 0")
        return self.tokens_used / self.token_budget

    @property
    def context_sufficiency_ratio(self) -> float:
        if not self.required_facts:
            return 1.0
        return len(self.required_facts & self.active_facts) / len(self.required_facts)

def simulate_retention(required_facts: Sequence[str], trajectory_facts: Sequence[str],
                       max_items: int, strategy: str = "truncate") -> ContextSnapshot:
    if max_items <= 0:
        raise ValueError("max_items must be > 0")
    required = set(required_facts)

    if strategy == "truncate":
        active = set(trajectory_facts[-max_items:])
    elif strategy == "preserve_required":
        selected = list(dict.fromkeys(required_facts))
        remaining = max_items - len(selected)
        if remaining > 0:
            selected.extend(x for x in reversed(trajectory_facts) if x not in required)
        active = set(selected[:max_items])
    else:
        raise ValueError(f"unknown strategy: {strategy}")

    return ContextSnapshot(required, active, len(active), max_items)
