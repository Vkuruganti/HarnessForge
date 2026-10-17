# Contributing

Contributions are welcome. Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Development setup

Use Python 3.10 or newer:

```bash
git clone https://github.com/Vkuruganti/HarnessForge.git
cd HarnessForge
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e ".[dev]"
python -m pytest -q
cffconvert --validate
python -m build
```

Run the examples listed in [README.md](README.md) when changing the models they use.
CI runs tests, examples, citation validation, and package builds on Python 3.10–3.14.

## Issues and pull requests

Use [GitHub issues](https://github.com/Vkuruganti/HarnessForge/issues) for bugs and feature proposals. Include reproduction steps, your Python version, and expected versus actual behavior for bugs. Discuss substantial changes in an issue first.

Create a branch from `main`, make a focused change, and open a pull request against `main`. Explain the problem, your approach, and how you verified it. Add regression tests for bug fixes and tests for new behavior; update documentation when behavior changes. Maintainer review and passing CI are expected before merging.

## Research principles

1. Clearly label synthetic theory-building examples.
2. Do not present simulator output as measured real-world model performance.
3. Add tests for new metrics and mechanisms.
4. Document provenance for empirical mechanisms.
5. Prefer framework-neutral abstractions.

Suggested areas: context retention, CPRO, HaaS, HADR lineage, HIR experiments, tool-risk policies, and visualization.

## Licensing

Submit only work you have the right to contribute. Contributions are provided under the project's Apache License 2.0. Identify third-party material and preserve its license and attribution notices.

Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).
