from aicontext.extractors.registry import register
from .core import extract_python_project

@register
def python_plugin(files, root):
    return "python", extract_python_project(files, root)
