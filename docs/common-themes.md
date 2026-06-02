# Python Repository Standard

Date reviewed: 2026-06-02

## Scope

- unique repositories reviewed: `156`
- structural baseline: `138`
- appendix-only references: `18`
- duplicate aliases removed: `1`

The structural baseline excludes tutorial collections, reading lists, challenge repositories, and prompt or skill directories. Those repositories are still catalogued in the atlas, but they do not drive the standard.

## Headline counts

- `105/138` use `pyproject.toml`
- `125/138` expose GitHub Actions workflows
- `77/138` use `pre-commit`
- `81/138` expose `tests/` or `testing/`
- `88/138` expose a root `docs/` directory
- `68/138` configure Ruff
- `46/138` configure mypy
- `68/138` configure pytest in `pyproject.toml`
- `31/138` use `src/` layout
- `32/138` use `setuptools.build_meta`
- `30/138` use `hatchling.build`

## Findings

### 1. `pyproject.toml` is the control plane

Confidence: high

`pyproject.toml` has already won the control-plane fight. `105/138` baseline repositories use it, and most new or actively modernized projects place project metadata, test settings, lint settings, and build backend selection there. The remaining holdouts cluster around older compatibility-heavy projects or repos with unusually thin root packaging surfaces.

### 2. `src/` layout is the default for distributable packages

Confidence: moderate

`31/138` repositories use `src/` layout. That is not a majority. It is still the strongest default for a new distributable package because it reduces accidental import leakage and keeps package boundaries explicit. The benchmark does not support forcing it onto every existing codebase or every application repo.

### 3. Repository checks are expected

Confidence: high

`125/138` repositories expose GitHub Actions workflows. The missing `13` are not evidence against automation. They are usually older repositories, repos driven by another CI system, or projects with non-standard root layouts. Public Python repos at this level are expected to machine-check themselves.

### 4. Quality gates are automated

Confidence: high

The benchmark disagrees on exact tool brands. It agrees on the categories:

- formatting
- linting
- typing
- tests
- docs validation
- release checks

Observed counts:

- `77/138` use `pre-commit`
- `68/138` expose Ruff configuration
- `46/138` expose mypy configuration
- `68/138` expose pytest configuration in `pyproject.toml`
- `25/138` still expose `tox.ini`
- `5/138` expose `noxfile.py`

Inference:
Modern Python repos are collapsing more quality work into fewer tools. Ruff is the clearest example. Tox remains common in mature multi-environment projects. Nox appears, but it is not the dominant task runner in this benchmark.

### 5. Docs live in the repo

Confidence: high

`88/138` repositories expose a root `docs/` directory. That does not mean every repo needs a docs site on day one. It does mean that serious Python repositories usually grow a documentation surface separate from the README.

### 6. Build backend choice is fragmented

Confidence: high

Backend counts from the structural baseline:

- `32` use `setuptools.build_meta`
- `30` use `hatchling.build`
- `8` use `poetry.core.masonry.api`
- `5` use `flit_core.buildapi`
- `4` use `mesonpy`
- `3` use `pdm.backend`
- `3` use `maturin`
- `52` do not expose a parseable backend at the repo root

Implication:
There is no universal backend. Setuptools is still heavily present. Hatchling is the strongest modern pure-Python contender. Meson and maturin matter in compiled or mixed-language codebases. Backend choice is a design decision with maintenance consequences.

### 7. The standard varies by repo class

Confidence: high

The benchmark breaks into four practical classes:

1. Distributable packages and libraries
   These are the cleanest fit for `pyproject.toml`, `src/`, `tests/`, GitHub Actions, Ruff, pytest, and often mypy.
2. Applications and services
   These often keep `pyproject.toml` and CI, but they are less consistent about `src/` and sometimes flatter at the root.
3. Large research or ML projects
   These often carry `requirements.txt`, mixed build surfaces, and less uniform packaging discipline while still maintaining tests and workflows.
4. Mixed-language or compiled projects
   These show up in the `mesonpy`, `maturin`, and compatibility-heavy `setuptools` cases. Their structure follows build constraints more than pure Python fashion.

### 8. The benchmark does not reward template maximalism

Confidence: high

The best repositories are not the ones with the most files. They are the ones where the repo shape matches the problem:

- one metadata hub instead of split legacy config unless compatibility requires it
- one or two quality entry points instead of five overlapping linters
- tests and docs that are obvious at the root
- CI that exercises the real path to release or deployment
- no speculative ceremony

## Recommended default

For a new pure-Python package, the strongest default remains:

1. `pyproject.toml`
2. `src/` layout
3. `tests/`
4. `.github/workflows/ci.yml`
5. `pre-commit`
6. Ruff
7. pytest
8. mypy when the public surface is typed or expected to stay typed
9. `README.md`
10. `docs/` once the project has more than trivial usage or API surface

## Decision rules

- Do not force `src/` layout onto an operational one-file script.
- Do not keep `setup.py`, `setup.cfg`, and `pyproject.toml` together unless backward compatibility requires all three.
- Do not add `tox`, `nox`, and ad hoc shell scripts for the same jobs without a concrete reason.
- Do not treat the heaviest template as the default starting point.
- Do not remove tests or docs from the root path in the name of visual neatness.

## What this standard does not claim

- It does not claim `src/` layout is a majority pattern.
- It does not claim GitHub Actions is the only valid CI.
- It does not claim mypy belongs in every repository.
- It does not claim one build backend has settled the market.
- It does not claim tutorial or resource repositories should be treated as structural peers of maintainable software codebases.
