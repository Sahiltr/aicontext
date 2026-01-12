from aicontext.extractors.registry import register
from .core import extract_js_project


@register
def javascript_plugin(files, root):
    return "javascript", extract_js_project(files, root)
