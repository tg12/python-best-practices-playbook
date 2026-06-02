# Sources

Reviewed on 2026-06-02.

## Primary sources

1. PyPA `sampleproject`
   - URL: `https://github.com/pypa/sampleproject`
   - Notes: `pyproject.toml`, `src/sample/`, `tests/`, `noxfile.py`, GitHub workflows.
2. `scientific-python/cookie`
   - URL: `https://github.com/scientific-python/cookie`
   - Notes: docs-heavy template, `pre-commit`, Ruff, MyPy, pytest, nox, Dependabot, release automation, GitHub Actions, backend selection.
3. `cookiecutter-hypermodern-python`
   - URL: `https://github.com/cjolowicz/cookiecutter-hypermodern-python`
   - Notes: docs, nox, tests, pre-commit, Poetry, type checking, release automation, GitHub Actions.
4. Python Packaging User Guide
   - URL: `https://packaging.python.org/en/latest/tutorials/packaging-projects/`
   - Notes: official `src/` layout example, `tests/`, `pyproject.toml`, backend choices.
5. GitHub Docs: Build and test Python
   - URL: `https://docs.github.com/en/actions/tutorials/build-and-test-code/python`
   - Notes: `actions/setup-python`, `pytest`, matrix examples, artifact publishing patterns.

## Selection rule

I chose sources that satisfied at least one of these:

- official guidance
- highly referenced template repository
- maintained repository with visible automation patterns

## Excluded from the evidence set

- blog posts that only restate official packaging guidance
- random "best practices" repos with no clear adoption signal
- tutorial repos that do not expose CI, packaging, or maintenance conventions
