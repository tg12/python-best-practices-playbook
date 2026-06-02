# Common Themes From Reviewed Python Repositories

Date reviewed: 2026-06-02

## Source set

- `https://github.com/pypa/sampleproject`
- `https://github.com/scientific-python/cookie`
- `https://github.com/cjolowicz/cookiecutter-hypermodern-python`
- `https://packaging.python.org/en/latest/tutorials/packaging-projects/`
- `https://docs.github.com/en/actions/tutorials/build-and-test-code/python`

## Findings

### 1. `pyproject.toml` is the control plane

Confidence: high

PyPA's packaging tutorial uses `pyproject.toml` for build backend selection and project metadata. `sampleproject` uses it in the same role. Modern templates then extend it to tool configuration.

### 2. `src/` layout is the default for distributable packages

Confidence: high

PyPA's packaging tutorial shows a `src/` directory with a package underneath it and a separate `tests/` directory. `sampleproject` mirrors that structure. The template repos follow the same pattern.

### 3. CI is assumed, not optional

Confidence: high

All three reviewed GitHub repos ship workflow files. GitHub's Python Actions guide uses `actions/setup-python` and shows `pytest`-driven runs. The current norm is that every push and pull request gets machine-checked.

### 4. Quality gates are automated

Confidence: high

The source repos disagree on the exact tools. They agree on the categories:

- formatting
- linting
- typing
- tests
- coverage

`scientific-python/cookie` has moved toward a stricter and more consolidated stack with `pre-commit`, MyPy, and Ruff. `cookiecutter-hypermodern-python` reflects an older split-tool stack with Black, Flake8, isort, mypy, pytest, and Bandit.

Inference:
Current high-signal templates are converging on fewer tools with broader coverage. Ruff is the clearest example.

### 5. Docs live in the repo

Confidence: high

`sampleproject` treats `README.md` as a project homepage surface. The template repos both include a `docs/` tree. The shared pattern is simple: a Python repo is expected to explain itself from the repository root and often from a documentation site as well.

### 6. Release hygiene is increasingly automated

Confidence: moderate

This is stronger in the templates than in `sampleproject`. `scientific-python/cookie` includes Dependabot, release configuration, Codecov, and PyPI trusted publisher guidance. Hypermodern Python includes release drafting, dependency updates, and publishing automation.

## What I did not claim

- I did not claim one build backend has won outright.
- I did not claim every Python project needs docs hosting.
- I did not claim every repo needs the full hypermodern stack.
- I did not claim `src/` layout is mandatory for every script repo.

## Practical baseline

For a new pure-Python repo, the defensible baseline is:

1. `pyproject.toml`
2. `src/` layout
3. `tests/`
4. GitHub Actions CI
5. Ruff
6. mypy
7. pytest
8. `README.md`

That baseline is smaller than the heavy templates, but it matches the overlap that holds up across the source set.
