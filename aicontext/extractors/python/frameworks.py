import ast
from pathlib import Path

def detect_frameworks(files, root: Path):
    frameworks = {
        "fastapi": [],
        "flask": [],
        "django": []
    }

    for file in files:
        if not file.endswith(".py"):
            continue

        path = root / file
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except Exception:
            continue

        imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    imports.add(n.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)

        # Detect frameworks
        if any(i.startswith("fastapi") for i in imports):
            frameworks["fastapi"].append(file)

        if any(i.startswith("flask") for i in imports):
            frameworks["flask"].append(file)

        if any(i.startswith("django") for i in imports):
            frameworks["django"].append(file)

    return frameworks
