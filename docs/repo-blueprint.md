# Repo Blueprint

## Default blueprint

```text
project-root/
├── .github/workflows/ci.yml
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── cli.py
└── tests/
    └── test_*.py
```

## Why this blueprint

- Small enough to understand in one sitting
- Matches the dominant overlap in the 156-repository benchmark
- Preserves the control-plane pattern now common in modern Python repos
- Leaves room for heavier release, docs, and security layers when the project earns them

## What to add only when justified

- `docs/` site generation
- coverage upload services
- release drafting
- trusted publishing
- security scanners
- matrix expansion beyond the Python versions you support

## What to avoid

- mixing app code at repo root for a package you intend to distribute
- piling five overlapping linters into a new repository
- using a template with features you cannot explain or maintain
- adding release automation before the package can pass its basic checks
