import pytest

from harnessforge.context import simulate_retention


def test_preserve_required_fills_budget_with_distinct_recent_facts():
    result = simulate_retention(["required"], ["required", "a", "b", "b"], 3, "preserve_required")
    assert result.active_facts == {"required", "a", "b"}
    assert result.tokens_used == 3
    assert result.context_sufficiency_ratio == 1
    assert result.utilization == 1


def test_preserve_required_prioritizes_required_then_most_recent():
    result = simulate_retention(["r1", "r2"], ["a", "b", "c"], 3, "preserve_required")
    assert result.active_facts == {"r1", "r2", "c"}


def test_preserve_required_when_budget_is_smaller_than_required_set():
    result = simulate_retention(["r1", "r1", "r2"], [], 1, "preserve_required")
    assert result.active_facts == {"r1"}
    assert result.context_sufficiency_ratio == 0.5


def test_truncate_keeps_last_items():
    result = simulate_retention(["r"], ["r", "a", "b"], 2)
    assert result.active_facts == {"a", "b"}
    assert result.context_sufficiency_ratio == 0


def test_empty_context_has_full_sufficiency_without_required_facts():
    result = simulate_retention([], [], 2)
    assert result.context_sufficiency_ratio == 1
    assert result.utilization == 0


@pytest.mark.parametrize("budget", [0, -1])
def test_invalid_budget(budget):
    with pytest.raises(ValueError, match="max_items"):
        simulate_retention([], [], budget)


def test_invalid_strategy():
    with pytest.raises(ValueError, match="strategy"):
        simulate_retention([], [], 1, "unknown")
