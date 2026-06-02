# Python Best Practices Playbook

`Python Best Practices Playbook` is a research-backed starter repository and LLM skill for building and reviewing modern Python repositories.

Brand: `tg12`
Site: <https://labs.jamessawyer.co.uk/>

This repository was built by reviewing a small set of high-signal Python template and guidance sources:

- PyPA `sampleproject`
- `scientific-python/cookie`
- `cookiecutter-hypermodern-python`
- Python Packaging User Guide
- GitHub Actions Python build-and-test docs

## What this repo gives you

- A minimal Python package with `src/` layout
- `pyproject.toml` as the single project metadata and tool config hub
- GitHub Actions CI for lint, type checks, and tests
- A documented shortlist of common patterns shared across respected Python repos
- A Codex-compatible skill that can audit or scaffold Python repos using those patterns
- A rewritten response-style prompt with obvious AI filler removed

## Common themes found across the source set

1. Project metadata belongs in `pyproject.toml`.
2. Published packages usually use `src/` layout and a separate `tests/` directory.
3. CI is standard, usually via GitHub Actions and `actions/setup-python`.
4. Quality gates are automated: linting, formatting, typing, and tests.
5. Documentation is part of the repo, not an afterthought.
6. Release hygiene is automated where possible.

The exact toolchain differs. The stable pattern is not a specific brand of tool. The stable pattern is centralized config, repeatable checks, and tight feedback loops.

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

The skill lives in [skills/python-best-practices-reviewer/SKILL.md](skills/python-best-practices-reviewer/SKILL.md). It is designed for Codex-style skill loading and tells the model when to inspect repo structure, when to prefer small changes, and when to enforce the common Python repo patterns found in the source set.

## Research notes

- [docs/common-themes.md](docs/common-themes.md)
- [docs/repo-blueprint.md](docs/repo-blueprint.md)
- [research/sources.md](research/sources.md)

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
