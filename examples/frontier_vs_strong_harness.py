from harnessforge import AgentConfig, TaskProfile, evaluate

task = TaskProfile(complexity=0.55, structure=0.85, memory_dependency=0.35, tool_dependency=0.75)

frontier_weak = AgentConfig(
    model_capability=0.96, context_quality=0.50, memory_quality=0.45,
    tool_quality=0.55, verification_strength=0.35, runtime_quality=0.55,
    model_cost=0.18, context_cost=0.04, memory_cost=0.005,
    tool_cost=0.02, verification_cost=0.0, runtime_cost=0.005,
    expected_retries=0.20,
)

small_strong = AgentConfig(
    model_capability=0.72, context_quality=0.92, memory_quality=0.88,
    tool_quality=0.94, verification_strength=0.92, runtime_quality=0.90,
    model_cost=0.04, context_cost=0.018, memory_cost=0.005,
    tool_cost=0.015, verification_cost=0.008, runtime_cost=0.004,
    expected_retries=0.06,
)

for name, cfg in [
    ("Frontier model + weak harness", frontier_weak),
    ("Smaller model + strong harness", small_strong),
]:
    result = evaluate(cfg, task)
    print(name)
    print(f"  reliability: {result['reliability']:.1%}")
    print(f"  cost/attempt: ${result['cost_per_attempt']:.4f}")
    print(f"  CPRO: ${result['cpro']:.4f}")
    print()
