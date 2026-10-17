from harnessforge.context import simulate_retention

required = ["customer_id", "refund_limit", "approval_policy"]
trajectory = required + [f"tool_result_{i}" for i in range(1, 7)]

for budget in (9, 6, 4, 3):
    raw = simulate_retention(required, trajectory, budget, "truncate")
    oracle = simulate_retention(required, trajectory, budget, "preserve_required")
    print(f"Budget={budget}")
    print(f"  naive truncation CSR: {raw.context_sufficiency_ratio:.2f}")
    print(f"  controlled upper-bound CSR: {oracle.context_sufficiency_ratio:.2f}")
