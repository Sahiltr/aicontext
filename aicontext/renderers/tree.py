from collections import defaultdict

def build_tree(paths):
    tree = defaultdict(dict)

    for path in paths:
        parts = path.split("/")
        node = tree
        for part in parts:
            node = node.setdefault(part, {})
    return tree


def render_tree(node, prefix=""):
    lines = []
    keys = sorted(node.keys())

    for i, key in enumerate(keys):
        is_last = i == len(keys) - 1
        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + key)

        child_prefix = prefix + ("    " if is_last else "│   ")
        lines.extend(render_tree(node[key], child_prefix))

    return lines
