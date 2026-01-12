from pathlib import Path
from typing import Dict, List

IGNORE_DIRS = {
    "venv", ".venv", "env",
    "__pycache__", "site-packages",
    "node_modules", ".git",
    ".idea", ".vscode",
    "dist", "build", ".eggs",
    ".mypy_cache", ".pytest_cache",
    ".ruff_cache", ".tox"
}


def scan_project(root: Path) -> Dict[str, List[str]]:
    """
    Walk the project directory and return all relevant folders and files,
    excluding virtual environments and build artifacts.
    """
    folders = []
    files = []

    for path in root.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        try:
            relative = path.relative_to(root).as_posix()
        except ValueError:
            continue

        if path.is_dir():
            folders.append(relative)
        else:
            files.append(relative)

    return {
        "root": root.name,
        "folders": sorted(folders),
        "files": sorted(files),
    }
