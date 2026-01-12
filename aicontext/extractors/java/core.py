from pathlib import Path
import javalang


def extract_java_project(files, root: Path):
    modules = []

    for file in files:
        if not file.endswith(".java"):
            continue

        path = root / file
        try:
            tree = javalang.parse.parse(path.read_text(encoding="utf-8"))
        except Exception:
            continue

        imports = []
        classes = []
        annotations = []

        for imp in tree.imports:
            imports.append(imp.path)

        for _, node in tree.filter(javalang.tree.TypeDeclaration):
            classes.append(node.name)
            for ann in node.annotations:
                annotations.append(ann.name)

        modules.append({
            "file": file,
            "imports": imports,
            "classes": classes,
            "annotations": annotations
        })

    return modules
