# HarnessForge

**Open-source tools for engineering reliable, governable, and cost-efficient AI agent harnesses.**

HarnessForge is a research companion toolkit for the paper:

> **Harness Engineering for Agentic AI: From Model Capability to Reliable, Governable, and Economic Value**

The project provides small executable models that help engineers build intuition about:

- model capability vs. harness capability,
- Cost Per Reliable Outcome (CPRO),
- context sufficiency and context degradation,
- read/write/execute tool risk,
- Harness-as-a-Service (HaaS),
- Architecture Decision Lineage,
- Architecture Intent Drift,
- and when a smaller model with a stronger harness can outperform a larger model with a weaker harness.

## Important research disclaimer

HarnessForge is currently a **theory-building and educational artifact**, not a predictive model of real-world AI systems.

Default parameters are synthetic. The examples are designed to expose mechanisms and test hypotheses, not to estimate the performance, safety, or cost of any specific commercial model.

## Quick start

```bash
git clone https://github.com/Vkuruganti/HarnessForge.git
cd HarnessForge
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Run examples:

```bash
python examples/frontier_vs_strong_harness.py
python examples/context_overflow.py
python examples/tool_risk.py
python examples/haas_amortization.py
python examples/architecture_intent_drift.py
```

Run tests:

```bash
pytest
```

## Core intuition

```text
Raw model capability
        ↓
Harness architecture
        ↓
Context selection
Memory continuity
Tool constraints
Verification
Runtime policy
Resource routing
        ↓
Effective agent capability
        ↓
Reliable, governable, economic value
```

## CPRO

CPRO = Total attributable execution cost / Reliable outcomes.

CPRO is not a universal quality score. Its usefulness depends on a defensible, task-specific definition of a reliable outcome.

## Harness-as-a-Service

HarnessForge also includes a simple HaaS model in which multiple agents inherit shared, versioned harness configuration instead of implementing context, retry, model-routing, verification, and policy logic independently.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and the pull request process, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations. Report vulnerabilities privately using [SECURITY.md](SECURITY.md).

## Citation

See [CITATION.cff](CITATION.cff) for software and paper citation metadata.

## License

Copyright 2026 Vas Kuruganti and HarnessForge Contributors.

Licensed under the [Apache License 2.0](LICENSE). HarnessForge is an independent project and is not affiliated with the Apache Software Foundation.
