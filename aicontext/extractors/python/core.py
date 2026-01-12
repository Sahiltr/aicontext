import ast
from pathlib import Path

def extract_python_project(files: list[str], root: Path):
    modules = []

    for file in files:
        if not file.endswith(".py"):
            continue

        path = root / file
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except Exception:
            continue

        imports = []
        classes = []
        functions = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports += [n.name for n in node.names]
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)

        modules.append({
            "file": file,
            "imports": imports,
            "classes": classes,
            "functions": functions
        })

    return modules
