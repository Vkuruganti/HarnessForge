from dataclasses import dataclass
from enum import Enum

class ToolClass(str, Enum):
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"

@dataclass(frozen=True)
class ToolPolicy:
    tool_class: ToolClass
    schema_validation: bool = False
    approval_required: bool = False
    sandboxed: bool = False
    idempotent: bool = False

def governance_score(policy: ToolPolicy) -> float:
    """Illustrative score, not a security certification."""
    base = {
        ToolClass.READ: 0.70,
        ToolClass.WRITE: 0.45,
        ToolClass.EXECUTE: 0.25,
    }[policy.tool_class]
    score = base
    score += 0.08 if policy.schema_validation else 0.0
    score += 0.12 if policy.approval_required else 0.0
    score += 0.18 if policy.sandboxed else 0.0
    score += 0.08 if policy.idempotent else 0.0
    return min(1.0, score)
