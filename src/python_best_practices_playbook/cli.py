"""Small CLI for printing the shared Python repo themes."""

from __future__ import annotations

import sys

from python_best_practices_playbook import get_common_themes


def main() -> None:
    """Print the shared themes in a deterministic order."""
    lines: list[str] = []
    for index, theme in enumerate(get_common_themes(), start=1):
        lines.append(f"{index}. {theme}")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
