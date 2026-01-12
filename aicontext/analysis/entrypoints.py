from pathlib import Path

def find_entry_points(files, root: Path):
    entrypoints = []

    for file in files:
        if not file.endswith(".py"):
            continue

        path = root / file
        text = path.read_text(encoding="utf-8", errors="ignore")

        if 'if __name__ == "__main__"' in text:
            entrypoints.append(file)

    return entrypoints
