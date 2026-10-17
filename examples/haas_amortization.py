from harnessforge.haas import HaaSEconomics

for n in (1, 5, 20, 100):
    economics = HaaSEconomics(
        number_of_agents=n,
        local_engineering_cost_per_agent=10_000,
        shared_platform_cost=45_000,
        incremental_onboarding_cost_per_agent=1_000,
    )
    print(
        f"{n:3d} agents | "
        f"local=${economics.local_total():,.0f} | "
        f"HaaS=${economics.haas_total():,.0f} | "
        f"savings=${economics.savings():,.0f} | "
        f"HaaS/agent=${economics.amortized_haas_cost_per_agent():,.0f}"
    )
