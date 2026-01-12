# aicontext

> **AI-grade multi-language project understanding for real codebases**

`aicontext` is an open-source CLI tool that scans a software repository and produces a structured, machine-readable representation of its architecture — including file structure, language semantics, dependencies, entry points, frameworks, and API routes — designed to be consumed by AI systems (ChatGPT, Claude, Cursor, Copilot, etc.) for deep project understanding.

This allows any AI agent to reason about your entire codebase instead of isolated files.

---

## 🚀 What aicontext Does

Given a project directory, `aicontext` produces:

- Clean file & folder tree (ignoring `venv`, `node_modules`, etc)
- Language-level semantics:
  - Python: imports, classes, functions
  - Java: imports, classes, annotations (Spring ready)
  - JavaScript / TypeScript: imports & modules
- Dependency graph
- Application entry points
- Framework detection (FastAPI, Flask, Django, Spring, React, etc)
- API route extraction
- AI-ready JSON export
- Human-readable project tree

---

## 🧠 Why This Exists

Large Language Models do not understand “projects”.  
They only understand what you paste.

`aicontext` solves this by generating a **single source of truth** for your repository that can be uploaded or pasted into any AI agent so it can:

- Understand architecture
- Trace dependencies
- Detect entry points
- Reason about APIs
- Suggest safe refactors
- Review pull requests

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourname/aicontext
cd aicontext
```

Clone the repository:

```bash
git clone https://github.com/yourname/aicontext
cd aicontext
```

Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # macOS/Linux

Install dependencies:

```
pip install -r requirements.txt

## Usage

Run from the root of any project:

```bash
python -m aicontext scan . --out project_context.json
```

You will see:
File & folder counts

Language modules detected

Entry points

Frameworks

API routes

Project tree

And it will generate:

```bash
project_context.json
```
This file is what you upload or paste into ChatGPT, Claude, Cursor, etc.

## 📂 Example Output
Found 142 files and 23 folders
Detected 18 python modules
Detected 6 javascript modules
Detected 1 entry point
Detected frameworks: fastapi, react
Detected 12 API routes

```bash
Found 25 files and 9 folders
Detected 1 entry points

Project Tree:
├── aicontext
│   ├── __init__.py
│   ├── __main__.py
│   ├── analysis
│   │   ├── dependencies.py
│   │   └── entrypoints.py
│   ├── cli.py
│   ├── exporters
│   │   └── json_exporter.py
│   ├── extractors
│   │   ├── java
│   │   │   ├── __init__.py
│   │   │   ├── core.py
│   │   │   └── spring.py
│   │   ├── javascript
│   │   │   ├── __init__.py
│   │   │   ├── core.py
│   │   │   └── react.py
│   │   ├── python
│   │   │   ├── __init__.py
│   │   │   ├── core.py
│   │   │   ├── frameworks.py
│   │   │   └── routes.py
│   │   └── registry.py
│   ├── renderers
│   │   ├── __init__.py
│   │   └── tree.py
│   └── scanner
│       ├── __init__.py
│       └── fs.py
├── architecture.txt
├── project_context.json
├── readme.md
└── requirements.txt
```

## Supported Language:
```bash
| Language                | Status                   |
| ----------------------- | ------------------------ |
| Python                  | ✅                        |
| Java (Spring Boot)      | ✅                        |
| JavaScript / TypeScript | ✅                        |
| C / C++                 | 🔜 (Tree-sitter planned) |
| Go                      | 🔜                       |
| Rust                    | 🔜                       |
```

## 🧱 Architecture
```bash
FILESYSTEM
   ↓
Scanner (fs.py)
   ↓
Language Plugins (Python / Java / JS)
   ↓
Dependency & Entry Analysis
   ↓
Tree Renderer
   ↓
AI-Ready JSON Export
```
This is the same architecture used by professional static-analysis and AI tooling platforms.

## 🤝 Contributing
New languages, frameworks, and analyzers are welcome.

To add a language:

Create extractors/<language>/core.py

Register it in extractors/<language>/__init__.py

Done — no CLI changes required


## 📜 License

MIT — free forever.




