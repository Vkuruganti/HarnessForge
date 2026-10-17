import pytest

from harnessforge.tools import ToolClass, ToolPolicy, governance_score


@pytest.mark.parametrize("tool_class, expected", [
    (ToolClass.READ, 0.70), (ToolClass.WRITE, 0.45), (ToolClass.EXECUTE, 0.25),
])
def test_base_scores(tool_class, expected):
    assert governance_score(ToolPolicy(tool_class)) == pytest.approx(expected)


@pytest.mark.parametrize("control, increment", [
    ("schema_validation", 0.08), ("approval_required", 0.12),
    ("sandboxed", 0.18), ("idempotent", 0.08),
])
def test_each_control_increases_score(control, increment):
    policy = ToolPolicy(ToolClass.EXECUTE, **{control: True})
    assert governance_score(policy) == pytest.approx(0.25 + increment)


def test_combined_controls_are_capped_at_one():
    policy = ToolPolicy(ToolClass.READ, True, True, True, True)
    assert governance_score(policy) == 1
