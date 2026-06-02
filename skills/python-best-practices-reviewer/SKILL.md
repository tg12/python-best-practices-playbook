---
name: python-best-practices-reviewer
description: Use when the task is to scaffold, review, or tighten a Python repository against common modern repo patterns such as pyproject.toml metadata, src layout, tests, CI, linting, typing, and documentation. Prefer this when the user wants a research-backed baseline rather than framework-specific advice.
---

# Python Best Practices Reviewer

Use this skill when a user wants one of these:

- a new Python repo scaffold
- a review of an existing Python repo
- a checklist for repo hardening
- a smaller modern baseline instead of a heavy template

## Workflow

1. Inspect the repository root first.
2. Identify the project type:
   - package meant for distribution
   - application or service
   - one-off operational script
3. Read [references/common-themes.md](references/common-themes.md).
4. If the request includes writing style or prompt cleanup, read [references/writing-style.md](references/writing-style.md).
5. Recommend or implement the smallest coherent change set that closes the real gap.

## Baseline checks

For distributable packages, prefer this baseline unless the repo already uses a justified alternative:

- `pyproject.toml` exists and carries project metadata
- `src/` layout is used
- `tests/` exists
- CI runs on push and pull request
- linting is automated
- type checking is automated
- tests are automated
- `README.md` explains the project

## Decision rules

- Do not force `src/` layout onto a one-file ops script unless packaging or import safety makes it worth the churn.
- Do not add overlapping tools without a reason.
- Prefer consolidated tooling where it reduces maintenance cost.
- Treat heavy template features as optional until the repo proves it needs them.
- Preserve public behavior when tightening an existing repo.

## Output rules

- Lead with the concrete repo gap.
- Separate facts from inference.
- Use confidence labels when evidence is mixed.
- Cite the source repo or doc when a recommendation depends on it.
