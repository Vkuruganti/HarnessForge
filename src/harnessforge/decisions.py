from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional

@dataclass(frozen=True)
class ArchitectureDecision:
    decision_id: str
    field: str
    expected_value: Any
    rationale: str
    status: str = "accepted"
    supersedes: Optional[str] = None
    evidence: Dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class IntentDrift:
    decision_id: str
    field: str
    expected: Any
    observed: Any
    rationale: str

def detect_intent_drift(decisions: Iterable[ArchitectureDecision],
                        observed_config: Dict[str, Any]) -> List[IntentDrift]:
    drifts = []
    for decision in decisions:
        if decision.status != "accepted":
            continue
        observed = observed_config.get(decision.field, "<missing>")
        if observed != decision.expected_value:
            drifts.append(IntentDrift(
                decision_id=decision.decision_id,
                field=decision.field,
                expected=decision.expected_value,
                observed=observed,
                rationale=decision.rationale,
            ))
    return drifts
