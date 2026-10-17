from harnessforge.model import AgentConfig, TaskProfile, evaluate

def test_evaluate_is_bounded():
    config = AgentConfig(
        model_capability=0.8, context_quality=0.8, memory_quality=0.8,
        tool_quality=0.8, verification_strength=0.8, runtime_quality=0.8,
        model_cost=0.1,
    )
    task = TaskProfile(complexity=0.5, structure=0.5)
    result = evaluate(config, task)
    assert 0 < result["reliability"] <= 1
    assert result["cost_per_attempt"] > 0
    assert result["cpro"] >= result["cost_per_attempt"]
