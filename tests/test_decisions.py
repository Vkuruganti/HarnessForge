from harnessforge.decisions import ArchitectureDecision, detect_intent_drift

def test_detect_intent_drift():
    decisions = [
        ArchitectureDecision(
            decision_id="HADR-1",
            field="verification",
            expected_value=True,
            rationale="Required for write tools",
        )
    ]
    drifts = detect_intent_drift(decisions, {"verification": False})
    assert len(drifts) == 1
    assert drifts[0].decision_id == "HADR-1"
