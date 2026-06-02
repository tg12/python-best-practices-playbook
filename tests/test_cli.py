"""Tests for the package surface."""

from __future__ import annotations

from python_best_practices_playbook import get_common_themes


def test_common_themes_are_stable() -> None:
    """Keep the published checklist deterministic."""
    themes = get_common_themes()
    assert len(themes) == 6
    assert themes[0] == "Centralize metadata and tool configuration in pyproject.toml."
    assert themes[-1] == "Keep release and dependency maintenance automated where practical."
