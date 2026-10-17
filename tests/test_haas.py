import pytest

from harnessforge.haas import HaaSEconomics


def test_economics_totals_and_amortization():
    economics = HaaSEconomics(5, 100, 200, 10)
    assert economics.local_total() == 500
    assert economics.haas_total() == 250
    assert economics.savings() == 250
    assert economics.amortized_haas_cost_per_agent() == 50


def test_zero_agents_allows_totals_but_not_amortization():
    economics = HaaSEconomics(0, 100, 200, 10)
    assert economics.local_total() == 0
    assert economics.haas_total() == 200
    assert economics.savings() == -200
    with pytest.raises(ValueError, match="number_of_agents"):
        economics.amortized_haas_cost_per_agent()


@pytest.mark.parametrize("count", [-1, 1.5, True])
def test_invalid_agent_count(count):
    with pytest.raises(ValueError, match="number_of_agents"):
        HaaSEconomics(count, 100, 200, 10)


@pytest.mark.parametrize("field", [
    "local_engineering_cost_per_agent", "shared_platform_cost", "incremental_onboarding_cost_per_agent",
])
@pytest.mark.parametrize("value", [-1, float("nan"), float("inf"), -float("inf")])
def test_invalid_costs(field, value):
    with pytest.raises(ValueError, match=field):
        HaaSEconomics(1, **{
            "local_engineering_cost_per_agent": 100,
            "shared_platform_cost": 200,
            "incremental_onboarding_cost_per_agent": 10,
            field: value,
        })
