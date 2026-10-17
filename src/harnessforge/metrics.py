def cpro(costs, reliable_outcomes) -> float:
    costs = list(costs)
    outcomes = list(reliable_outcomes)
    if len(costs) != len(outcomes):
        raise ValueError("costs and reliable_outcomes must have equal length")
    if any(c < 0 for c in costs):
        raise ValueError("costs must be non-negative")
    successes = sum(bool(x) for x in outcomes)
    if successes == 0:
        raise ValueError("CPRO is undefined when there are no reliable outcomes")
    return sum(costs) / successes

def cost_per_attempt(costs) -> float:
    values = list(costs)
    if not values:
        raise ValueError("at least one cost is required")
    if any(c < 0 for c in values):
        raise ValueError("costs must be non-negative")
    return sum(values) / len(values)
