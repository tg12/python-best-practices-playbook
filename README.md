# Python Best Practices Playbook

`Python Best Practices Playbook` defines a practical Python repository standard and ships a matching LLM skill for repo review and scaffolding.

Brand: `tg12`
Site: <https://labs.jamessawyer.co.uk/>

The current benchmark covers `156` unique public repositories. `138` code-bearing repositories drive the structural baseline. `18` tutorial, resource, and collection repositories are catalogued separately so they do not distort the recommendations.

## What this repo gives you

- A minimal Python package with `src/` layout
- `pyproject.toml` as the single project metadata and tool config hub
- GitHub Actions CI for lint, type checks, and tests
- A documented Python repository standard derived from a 156-repository benchmark
- A Codex-compatible skill that can audit or scaffold Python repos using those patterns
- A rewritten response-style prompt with obvious AI filler removed

## Benchmark summary

Across the `138`-repository structural baseline:

- `105/138` use `pyproject.toml`
- `125/138` expose GitHub Actions workflows
- `77/138` use `pre-commit`
- `81/138` expose a dedicated `tests/` or `testing/` directory
- `88/138` expose a root `docs/` directory
- `68/138` configure Ruff
- `46/138` configure mypy
- `68/138` configure pytest in `pyproject.toml`
- `31/138` use `src/` layout
- `30/138` use `hatchling.build`
- `32/138` still expose `setuptools.build_meta`

The standard pattern is centralized metadata, automated checks, explicit test surfaces, and repository-level documentation. The benchmark does not support the claim that one build backend or one layout has completely won.

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

The skill lives in [skills/python-best-practices-reviewer/SKILL.md](skills/python-best-practices-reviewer/SKILL.md). It is designed for Codex-style skill loading and tells the model when to inspect repo structure, when to prefer small changes, and when to enforce the benchmark-backed patterns that hold up across the atlas.

## Research notes

- [docs/common-themes.md](docs/common-themes.md)
- [docs/repo-blueprint.md](docs/repo-blueprint.md)
- [research/repo-atlas.md](research/repo-atlas.md)

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
