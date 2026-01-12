from aicontext.extractors.registry import register
from .core import extract_java_project


@register
def java_plugin(files, root):
    return "java", extract_java_project(files, root)
