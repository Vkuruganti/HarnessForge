from harnessforge.decisions import ArchitectureDecision, detect_intent_drift

decisions = [
    ArchitectureDecision(
        decision_id="HADR-021",
        field="verification_required",
        expected_value=True,
        rationale="All state-changing financial operations require verification.",
    ),
    ArchitectureDecision(
        decision_id="HADR-027",
        field="max_retries",
        expected_value=2,
        rationale="Limit repeated external side effects and retry cost.",
    ),
]

observed_config = {"verification_required": False, "max_retries": 5}

for drift in detect_intent_drift(decisions, observed_config):
    print(f"{drift.decision_id}: {drift.field}")
    print(f"  expected={drift.expected!r}")
    print(f"  observed={drift.observed!r}")
    print(f"  rationale={drift.rationale}")
