import ast
from pathlib import Path

def extract_routes(files, root: Path):
    routes = []

    for file in files:
        if not file.endswith(".py"):
            continue

        path = root / file
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and hasattr(dec.func, "attr"):
                        if dec.func.attr in {"get", "post", "put", "delete", "patch"}:
                            if dec.args:
                                try:
                                    route = dec.args[0].value
                                except:
                                    route = "unknown"

                            routes.append({
                                "file": file,
                                "function": node.name,
                                "method": dec.func.attr.upper(),
                                "path": route
                            })

    return routes
