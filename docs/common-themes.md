# Common Themes From A 57-Repository Survey

Date reviewed: 2026-06-02

## Survey size

- repositories scanned: `57`
- GitHub Actions workflows present: `57`

## Findings

### 1. `pyproject.toml` is the control plane

Confidence: high

`53/57` repositories use `pyproject.toml`. `42/57` use it without a root `setup.py` or `setup.cfg`. The control-plane shift is already real. The holdouts are older or compatibility-heavy projects.

### 2. `src/` layout is the default for distributable packages

Confidence: moderate

`23/57` repositories use `src/` layout. That is enough to treat it as a strong default for new distributable packages, but not enough to pretend it is universal. Large and older projects still ship flat or custom layouts.

### 3. CI is assumed, not optional

Confidence: high

`57/57` repositories expose GitHub Actions workflows. CI is table stakes.

### 4. Quality gates are automated

Confidence: high

The survey disagrees on exact tool brands. It agrees on the categories:

- formatting
- linting
- typing
- tests
- docs validation
- release checks

Observed counts:

- `44/57` use `pre-commit`
- `40/57` expose Ruff configuration
- `36/57` expose mypy configuration
- `41/57` expose pytest configuration in `pyproject.toml`
- `20/57` still expose `tox.ini`
- `5/57` expose `noxfile.py`

Inference:
Modern repositories are consolidating more quality work into fewer tools. Ruff is the clearest example. Tox remains common. Nox is visible but rare.

### 5. Docs live in the repo

Confidence: high

`42/57` repositories expose a root `docs/` directory. Repos without one often still document heavily in the README or use non-root documentation layouts. Documentation remains a normal maintenance surface, not an optional afterthought.

### 6. Release hygiene is increasingly automated

Confidence: moderate

The survey shows a steady move toward automated release and maintenance hooks, but not one standard implementation. The dominant pattern is not a specific release workflow. The dominant pattern is that release, dependency, and compatibility work is pushed into CI.

### 7. Build backend choice is fragmented

Confidence: high

Backend counts from the survey:

- `17` use `hatchling.build`
- `14` use `setuptools.build_meta`
- `5` use `flit_core.buildapi`
- `4` use `mesonpy`
- `3` use `pdm.backend`
- `3` use `poetry.core.masonry.api`
- `2` use `maturin`
- `9` do not expose a parseable backend at the repo root

Implication:
There is no single winning backend across serious Python repos. Treat backend choice as a design tradeoff, not doctrine.

## What I did not claim

- I did not claim one build backend has won outright.
- I did not claim `src/` layout is universal.
- I did not claim every repo needs docs hosting.
- I did not claim every script repo should be reshaped into a package.

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

That baseline is smaller than the heaviest templates, but it matches the overlap that holds up across the survey.
