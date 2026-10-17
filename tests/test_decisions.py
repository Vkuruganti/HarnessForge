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


def test_missing_field_is_drift_even_when_expected_value_matches_display_marker():
    decision = ArchitectureDecision("missing", "setting", "<missing>", "required setting")
    drifts = detect_intent_drift([decision], {})
    assert len(drifts) == 1
    assert drifts[0].observed == "<missing>"
    assert detect_intent_drift([decision], {"setting": "<missing>"}) == []


def test_matching_values_and_inactive_decisions_do_not_drift():
    decisions = [
        ArchitectureDecision("match", "setting", None, "nullable setting"),
        ArchitectureDecision("inactive", "absent", True, "old decision", status="superseded"),
    ]
    assert detect_intent_drift(decisions, {"setting": None}) == []


def test_missing_nullable_field_is_drift():
    decision = ArchitectureDecision("nullable", "setting", None, "must be present")
    assert len(detect_intent_drift([decision], {})) == 1
