# Python Repo Survey

Survey date: 2026-06-02

Corpus size: `57`

## Headline counts

- `53/57` use `pyproject.toml`
- `42/57` are `pyproject`-only at the root
- `57/57` use GitHub Actions workflows
- `44/57` use `pre-commit`
- `40/57` expose Ruff configuration
- `36/57` expose mypy configuration
- `41/57` expose pytest configuration in `pyproject.toml`
- `23/57` use `src/` layout
- `42/57` expose a root `docs/` directory
- `20/57` expose `tox.ini`
- `5/57` expose `noxfile.py`

## Repo notes

### Packaging and repo templates

- `pypa/sampleproject` - sample package layout; `pyproject`, `src`, `tests`, GitHub Actions, `nox`, `setuptools.build_meta`.
- `python-poetry/poetry` - packaging toolchain; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Poetry backend.
- `pdm-project/pdm` - PEP-first packaging tool; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, MkDocs, Ruff, mypy, pytest, PDM backend.
- `ofek/hatch` - project management and build tooling; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, MkDocs, mypy, Hatchling backend.
- `jazzband/pip-tools` - dependency pinning workflow; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, mypy, pytest, setuptools backend.

### Web frameworks and HTTP stack

- `pallets/flask` - web framework; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Flit backend.
- `pallets/click` - CLI toolkit; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Flit backend.
- `pallets/jinja` - template engine; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Flit backend.
- `pallets/werkzeug` - WSGI utility layer; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Flit backend.
- `pallets/itsdangerous` - signing and token utilities; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Flit backend.
- `django/django` - full-stack framework; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, setuptools backend, no `src/`.
- `tiangolo/fastapi` - ASGI framework; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, PDM backend.
- `encode/starlette` - ASGI core framework; `pyproject`, `tests`, `docs`, GitHub Actions, MkDocs, Ruff, mypy, pytest, Hatchling backend.
- `encode/httpx` - HTTP client; `pyproject`, `tests`, `docs`, GitHub Actions, MkDocs, Ruff, mypy, pytest, Hatchling backend.
- `encode/uvicorn` - ASGI server; `pyproject`, `tests`, `docs`, GitHub Actions, MkDocs, Ruff, mypy, pytest, Hatchling backend.
- `aio-libs/aiohttp` - async client and server stack; `pyproject`, `setup.cfg`, `setup.py`, `tests`, `docs`, GitHub Actions, `pre-commit`, setuptools backend.
- `psf/requests` - sync HTTP client; `pyproject`, `setup.py`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, pytest, setuptools backend.
- `urllib3/urllib3` - transport layer HTTP library; `pyproject`, `setup.cfg`, `src`, `docs`, GitHub Actions, `pre-commit`, `nox`, mypy, pytest, Hatchling backend.

### Data validation, ORM, and background jobs

- `pydantic/pydantic` - validation and settings; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, MkDocs, Ruff, pytest, Hatchling backend.
- `sqlalchemy/sqlalchemy` - ORM and SQL toolkit; `pyproject`, `setup.cfg`, `setup.py`, GitHub Actions, `pre-commit`, `tox`, `nox`, mypy, pytest, setuptools backend.
- `celery/celery` - distributed task queue; `pyproject`, `setup.cfg`, `setup.py`, `docs`, GitHub Actions, `pre-commit`, `tox`, mypy, pytest.
- `rq/rq` - Redis job queue; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, pytest, Hatchling backend.
- `prefecthq/prefect` - workflow orchestration; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Hatchling backend.
- `dbt-labs/dbt-core` - analytics engineering runtime; `pyproject`, `docs`, GitHub Actions, minimal root metadata surface compared with the rest of the survey.
- `apache/airflow` - orchestration platform; `pyproject`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Hatchling backend.
- `scrapy/scrapy` - crawling and scraping framework; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, pytest, Hatchling backend.

### Testing, linting, formatting, typing, and task automation

- `pytest-dev/pytest` - testing framework; `pyproject`, `src`, `tests`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, pytest, setuptools backend.
- `pytest-dev/pluggy` - plugin system; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, setuptools backend.
- `psf/black` - code formatter; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, mypy, pytest, Hatchling backend.
- `astral-sh/ruff` - linter and formatter; `pyproject`, `docs`, GitHub Actions, `pre-commit`, MkDocs, Ruff config, `maturin` backend.
- `python/mypy` - static typing engine; `pyproject`, `setup.py`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, pytest, setuptools backend.
- `PyCQA/isort` - import sorter; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, pytest, Hatchling backend.
- `PyCQA/bandit` - security scanner; `setup.cfg`, `setup.py`, `tests`, GitHub Actions, `pre-commit`, `tox`, no root `pyproject`.
- `pre-commit/pre-commit` - hook runner; `setup.cfg`, `setup.py`, `tests`, GitHub Actions, `pre-commit`, `tox`, no root `pyproject`.
- `wntrblm/nox` - task automation; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, `nox`, Ruff, mypy, pytest, Hatchling backend.
- `tox-dev/tox` - environment matrix runner; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, pytest, Hatchling backend.

### Terminal UI and developer experience

- `Textualize/rich` - terminal rendering library; `pyproject`, `setup.py`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, mypy, pytest, Poetry backend.
- `Textualize/textual` - terminal application framework; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, pytest, Poetry backend.
- `streamlit/streamlit` - data app runtime; `pyproject`, GitHub Actions, `pre-commit`, Ruff, mypy, no root `tests` or `docs` directory.
- `plotly/dash` - dashboard framework; `setup.py`, `tests`, GitHub Actions, no root `pyproject`.
- `getpelican/pelican` - static site generator; `pyproject`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, PDM backend.
- `locustio/locust` - load testing framework; `pyproject`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, Hatchling backend.
- `beeware/briefcase` - app packaging tool; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, pytest, setuptools backend.
- `pyinstaller/pyinstaller` - binary packaging runtime; `pyproject`, `tests`, GitHub Actions, Hatchling backend.

### Scientific, data, and machine learning

- `scikit-learn/scikit-learn` - machine learning library; `pyproject`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, `mesonpy` backend, no root `src` or `docs`.
- `pandas-dev/pandas` - dataframe engine; `pyproject`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, `mesonpy` backend.
- `numpy/numpy` - numerical computing core; `pyproject`, GitHub Actions, `mesonpy` backend, sparse root-level quality config compared with peers.
- `pola-rs/polars` - dataframe engine with Rust core; `docs`, GitHub Actions, MkDocs, no root `pyproject` in the Python-facing repo root.
- `matplotlib/matplotlib` - plotting library; `pyproject`, `src`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, pytest, `mesonpy` backend.
- `sympy/sympy` - symbolic mathematics; `pyproject`, `setup.py`, GitHub Actions, Ruff, mypy, pytest, flat layout.
- `bokeh/bokeh` - visualization framework; `pyproject`, `setup.py`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, Ruff, mypy, pytest, setuptools backend.
- `kedro-org/kedro` - data science framework; `pyproject`, `tests`, `docs`, GitHub Actions, `pre-commit`, MkDocs, Ruff, mypy, pytest, setuptools backend.
- `huggingface/transformers` - model framework; `pyproject`, `setup.py`, `src`, `tests`, `docs`, GitHub Actions, Ruff, pytest, mixed modern and legacy packaging surfaces.
- `explosion/spaCy` - NLP framework; `pyproject`, `setup.cfg`, `setup.py`, GitHub Actions, `pre-commit`, Ruff, setuptools backend.

### Security, cryptography, and systems

- `pyca/cryptography` - cryptography primitives; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `nox`, Ruff, mypy, pytest, `maturin` backend.
- `python-attrs/attrs` - typed class helpers; `pyproject`, `src`, `tests`, `docs`, GitHub Actions, `pre-commit`, `tox`, Ruff, mypy, pytest, Hatchling backend.
- `home-assistant/core` - large application codebase; `pyproject`, `tests`, GitHub Actions, `pre-commit`, Ruff, pytest, setuptools backend.

## Comparison summary

### Strong consensus

- `pyproject.toml` is normal.
- GitHub Actions CI is universal in this corpus.
- `pre-commit`, Ruff, mypy, and pytest form the most common quality stack.
- `docs/` and `tests/` are common maintenance surfaces.

### Weak consensus

- `src/` layout is common but not dominant.
- Build backend choice is fragmented.
- `tox` is still common; `nox` is visible but much less common.
- Large mature repos often carry mixed modern and legacy packaging surfaces for compatibility reasons.
