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

There is no single winner across the source set.

- PyPA tutorial defaults to Hatchling in the current packaging guide.
- `scientific-python/cookie` recommends Hatch for pure Python projects.
- Hypermodern Python used Poetry in its template.

Treat backend choice as a policy decision. Do not present it as settled doctrine.

### Tooling granularity

The category consensus is strong. The exact tool consensus is not.

- Older templates split formatting, import sorting, linting, and syntax upgrades across multiple tools.
- Newer templates compress more of that into Ruff.

If a repo is green and maintainable, do not churn tools for style points alone.
