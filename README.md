# Python Best Practices Playbook

`Python Best Practices Playbook` is a maintained starter repository and LLM skill for building and reviewing modern Python repositories.

Brand: `tg12`
Site: <https://labs.jamessawyer.co.uk/>

This repository now carries a 57-repository survey across Python frameworks, libraries, tooling, data platforms, scientific stacks, and application projects. The guide and skill reflect the overlap that survives across that wider corpus.

## What this repo gives you

- A minimal Python package with `src/` layout
- `pyproject.toml` as the single project metadata and tool config hub
- GitHub Actions CI for lint, type checks, and tests
- A documented baseline derived from a 57-repository survey
- A Codex-compatible skill that can audit or scaffold Python repos using those patterns
- A rewritten response-style prompt with obvious AI filler removed

## Aggregate findings

Across the current survey:

- `53/57` use `pyproject.toml`
- `57/57` expose GitHub Actions workflows
- `44/57` use `pre-commit`
- `42/57` are `pyproject`-only at the repo root, without `setup.py` or `setup.cfg`
- `40/57` expose a dedicated `tests/` or `testing/` directory
- `42/57` have a root `docs/` directory
- `40/57` configure Ruff
- `36/57` configure mypy
- `41/57` configure pytest in `pyproject.toml`
- `23/57` use `src/` layout

The stable pattern is not one fixed template. The stable pattern is centralized metadata, machine-enforced checks, and explicit maintenance surfaces.

## Repository layout

```text
.
├── .github/workflows/ci.yml
├── docs/
├── pyproject.toml
├── research/
├── skills/
├── src/
└── tests/
```

## Skill

The skill lives in [skills/python-best-practices-reviewer/SKILL.md](skills/python-best-practices-reviewer/SKILL.md). It is designed for Codex-style skill loading and tells the model when to inspect repo structure, when to prefer small changes, and when to enforce the common Python repo patterns that hold up across the survey.

## Research notes

- [docs/common-themes.md](docs/common-themes.md)
- [docs/repo-blueprint.md](docs/repo-blueprint.md)
- [research/repo-survey.md](research/repo-survey.md)

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
ruff check .
mypy src
```

## SEO targets

Primary keywords:

- python best practices
- python project template
- python repository standards
- python repo checklist
- python packaging guide
- llm python code review skill

## License

MIT
