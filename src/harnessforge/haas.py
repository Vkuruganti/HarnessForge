from dataclasses import dataclass

@dataclass(frozen=True)
class HaaSEconomics:
    number_of_agents: int
    local_engineering_cost_per_agent: float
    shared_platform_cost: float
    incremental_onboarding_cost_per_agent: float = 0.0

    def local_total(self) -> float:
        return self.number_of_agents * self.local_engineering_cost_per_agent

    def haas_total(self) -> float:
        return self.shared_platform_cost + self.number_of_agents * self.incremental_onboarding_cost_per_agent

    def savings(self) -> float:
        return self.local_total() - self.haas_total()

    def amortized_haas_cost_per_agent(self) -> float:
        if self.number_of_agents <= 0:
            raise ValueError("number_of_agents must be > 0")
        return self.haas_total() / self.number_of_agents
