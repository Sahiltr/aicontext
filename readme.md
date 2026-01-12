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

Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # macOS/Linux

