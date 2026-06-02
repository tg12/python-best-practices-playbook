# Common Themes Reference

Use this reference when reviewing or scaffolding a Python repo.

Benchmark scope:

- `156` unique repositories reviewed
- `138` repositories in the structural baseline
- `18` appendix-only repositories excluded from structural counts

## High-confidence defaults

1. Keep build metadata in `pyproject.toml`.
2. Use `src/` layout for distributable packages.
3. Keep tests separate from importable source.
4. Run lint, type, and test checks in CI.
5. Keep `README.md` accurate and useful.

## Mixed-evidence areas

### Build backend

There is no single winner across the benchmark.

Observed backend counts:

- setuptools: `32`
- hatchling: `30`
- poetry: `8`
- flit: `5`
- mesonpy: `4`
- pdm: `3`
- maturin: `3`

Treat backend choice as a policy decision. Do not present it as settled doctrine.

### Tooling granularity

The category consensus is strong. The exact tool consensus is not.

- Older templates split formatting, import sorting, linting, and syntax upgrades across multiple tools.
- Newer repositories compress more of that into Ruff.
- `68/138` baseline repos expose Ruff configuration.
- `46/138` baseline repos expose mypy configuration.
- `68/138` baseline repos expose pytest configuration in `pyproject.toml`.

If a repo is green and maintainable, do not churn tools for style points alone.
