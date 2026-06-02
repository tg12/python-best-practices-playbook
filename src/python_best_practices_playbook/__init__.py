"""Utilities for the Python Best Practices Playbook."""

__all__ = ["get_common_themes"]


def get_common_themes() -> list[str]:
    """Return the core themes repeated across the reviewed source repos."""
    return [
        "Centralize metadata and tool configuration in pyproject.toml.",
        "Use src layout for distributable packages.",
        "Keep tests in a dedicated tests directory.",
        "Automate linting, typing, and tests in CI.",
        "Treat README and docs as part of the product.",
        "Keep release and dependency maintenance automated where practical.",
    ]
