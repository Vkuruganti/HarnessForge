from __future__ import annotations
from dataclasses import dataclass
from math import exp
from typing import Dict

@dataclass(frozen=True)
class AgentConfig:
    model_capability: float
    context_quality: float
    memory_quality: float
    tool_quality: float
    verification_strength: float
    runtime_quality: float
    model_cost: float
    context_cost: float = 0.0
    memory_cost: float = 0.0
    tool_cost: float = 0.0
    verification_cost: float = 0.0
    runtime_cost: float = 0.0
    expected_retries: float = 0.0

    def validate(self) -> None:
        for name in (
            "model_capability", "context_quality", "memory_quality",
            "tool_quality", "verification_strength", "runtime_quality",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        if self.expected_retries < 0:
            raise ValueError("expected_retries must be >= 0")
        for name in (
            "model_cost", "context_cost", "memory_cost", "tool_cost",
            "verification_cost", "runtime_cost",
        ):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} must be >= 0")

@dataclass(frozen=True)
class TaskProfile:
    complexity: float
    structure: float
    memory_dependency: float = 0.0
    tool_dependency: float = 0.0

    def validate(self) -> None:
        for name in ("complexity", "structure", "memory_dependency", "tool_dependency"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

def reliability(config: AgentConfig, task: TaskProfile) -> float:
    """Synthetic theory-building model, not a calibrated predictor."""
    config.validate()
    task.validate()

    generic_harness = (
        0.34 * config.context_quality
        + 0.20 * config.verification_strength
        + 0.18 * config.runtime_quality
        + 0.14 * config.memory_quality
        + 0.14 * config.tool_quality
    )
    dependency_fit = (
        task.memory_dependency * config.memory_quality
        + task.tool_dependency * config.tool_quality
    ) / max(1.0, task.memory_dependency + task.tool_dependency)

    model_weight = 0.40 + 0.35 * task.complexity
    harness_weight = 1.0 - model_weight
    harness_multiplier = 0.75 + 0.50 * task.structure

    effective = (
        model_weight * config.model_capability
        + harness_weight * generic_harness * harness_multiplier
        + 0.12 * dependency_fit
        - 0.45 * task.complexity
    )
    return min(0.995, max(0.01, _sigmoid(4.0 * (effective - 0.15))))

def cost_breakdown(config: AgentConfig) -> Dict[str, float]:
    config.validate()
    base = {
        "model": config.model_cost,
        "context": config.context_cost,
        "memory": config.memory_cost,
        "tools": config.tool_cost,
        "verification": config.verification_cost,
        "runtime": config.runtime_cost,
    }
    base_total = sum(base.values())
    retry = base_total * config.expected_retries
    return {**base, "retry": retry, "total": base_total + retry}

def evaluate(config: AgentConfig, task: TaskProfile) -> Dict[str, float]:
    r = reliability(config, task)
    costs = cost_breakdown(config)
    total = costs["total"]
    return {
        "reliability": r,
        "cost_per_attempt": total,
        "cpro": total / r,
        **{f"cost_{k}": v for k, v in costs.items() if k != "total"},
    }
