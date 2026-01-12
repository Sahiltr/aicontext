What each dependency does
Library	                    Why it exists in aicontext
typer	                    CLI framework (aicontext scan .)
rich	                    Pretty terminal output
pydantic	                Structured data models for AI context
javalang	                Parse Spring Boot Java files
tree-sitter	                Parse JS, TS, Python, etc
tree-sitter-languages	    Prebuilt grammars
pyyaml	                    Read application.yml
toml	                    Read pyproject.toml, config
xmltodict	                Parse pom.xml
networkx	                Build dependency & call graphs


Architecture:
scanner/      → file discovery
extractors/   → language & framework parsing
analysis/     → dependency & runtime logic
renderers/    → visualization
exporters/    → AI output
