import click
from pathlib import Path

from aicontext.scanner.fs import scan_project
from aicontext.exporters.json_exporter import export_to_json
from aicontext.extractors.registry import run_all
from aicontext.analysis.dependencies import build_dependency_graph
from aicontext.analysis.entrypoints import find_entry_points
from aicontext.renderers.tree import build_tree, render_tree


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path", default=".")
@click.option("--out", default=None, help="Write result to a JSON file")
def scan(path, out):
    """Scan a project directory and extract multi-language system context."""
    project_path = Path(path)

    if not project_path.exists():
        click.echo("Invalid path")
        return

    # 1️⃣ Physical structure
    result = scan_project(project_path)

    # 2️⃣ Language plugins (Python, Java, JS, future languages)
    languages = run_all(result["files"], project_path)
    result["languages"] = languages

    # 3️⃣ Dependency graph (language-agnostic)
    dependency_graph = {}
    for lang, modules in languages.items():
        if isinstance(modules, list):
            dependency_graph[lang] = build_dependency_graph(modules)

    result["dependencies"] = dependency_graph

    # 4️⃣ Entry points
    entry_points = find_entry_points(result["files"], project_path)
    result["entry_points"] = entry_points

    # 5️⃣ Tree rendering
    all_paths = result["folders"] + result["files"]
    tree = build_tree(all_paths)
    tree_lines = render_tree(tree)
    result["tree"] = tree_lines

    # 6️⃣ Report
    click.echo(f"Found {len(result['files'])} files and {len(result['folders'])} folders")

    for lang, data in languages.items():
        if isinstance(data, list):
            click.echo(f"Detected {len(data)} {lang} modules")

    click.echo(f"Detected {len(entry_points)} entry points")

    click.echo("\nProject Tree:")
    for line in tree_lines:
        click.echo(line)

    # 7️⃣ Export
    if out:
        export_to_json(result, out)
        click.echo(f"\nWritten to {out}")
