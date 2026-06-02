# Common Themes Reference

Use this reference when reviewing or scaffolding a Python repo.

## High-confidence defaults

1. Keep build metadata in `pyproject.toml`.
2. Use `src/` layout for distributable packages.
3. Keep tests separate from importable source.
4. Run lint, type, and test checks in CI.
5. Keep `README.md` accurate and useful.

## Mixed-evidence areas

### Build backend

There is no single winner across the survey.

Observed backend counts:

- hatchling: `17`
- setuptools: `14`
- flit: `5`
- mesonpy: `4`
- pdm: `3`
- poetry: `3`
- maturin: `2`

Treat backend choice as a policy decision. Do not present it as settled doctrine.

### Tooling granularity

The category consensus is strong. The exact tool consensus is not.

- Older templates split formatting, import sorting, linting, and syntax upgrades across multiple tools.
- Newer repositories compress more of that into Ruff.

If a repo is green and maintainable, do not churn tools for style points alone.
