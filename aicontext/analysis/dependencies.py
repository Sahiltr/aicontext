from collections import defaultdict

def build_dependency_graph(python_modules):
    graph = defaultdict(list)

    for module in python_modules:
        name = module["file"].replace("/", ".").replace(".py", "")
        for imp in module["imports"]:
            graph[name].append(imp)

    return dict(graph)
