import pytest
from harnessforge.metrics import cpro, cost_per_attempt

def test_cpro():
    assert cpro([0.1, 0.1, 0.1, 0.1], [True, True, False, True]) == pytest.approx(0.4 / 3)

def test_cpro_requires_success():
    with pytest.raises(ValueError):
        cpro([0.1], [False])

def test_cost_per_attempt():
    assert cost_per_attempt([1, 2, 3]) == 2
