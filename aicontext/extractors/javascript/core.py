import re
from pathlib import Path

IMPORT_RE = re.compile(
    r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]|require\([\'"]([^\'"]+)[\'"]\)'
)


def extract_js_project(files, root: Path):
    modules = []

    for file in files:
        if not file.endswith((".js", ".ts", ".jsx", ".tsx")):
            continue

        path = root / file
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue

        imports = []
        for match in IMPORT_RE.findall(text):
            imp = match[0] or match[1]
            if imp:
                imports.append(imp)

        modules.append({
            "file": file,
            "imports": imports
        })

    return modules
