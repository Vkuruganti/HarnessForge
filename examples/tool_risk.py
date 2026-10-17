from harnessforge.tools import ToolClass, ToolPolicy, governance_score

policies = [
    ToolPolicy(ToolClass.READ),
    ToolPolicy(ToolClass.WRITE, schema_validation=True, approval_required=True, idempotent=True),
    ToolPolicy(ToolClass.EXECUTE, schema_validation=True, approval_required=True, sandboxed=True),
]

for policy in policies:
    print(policy.tool_class.value, f"{governance_score(policy):.2f}")
