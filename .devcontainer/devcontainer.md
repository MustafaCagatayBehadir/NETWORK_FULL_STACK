# Dev Container configuration for `NETWORK_FULL_STACK`

## Common settings

### Git installation

There was an attempt to install `git` within devcontainer by usage of `features` capability of the tool, yet it did not work as expected - `git` was not visible in pre-built containers. The following configuration was used to that:

```json
    "features": {
        "git": {
            "version": "latest",
            "ppa": false
        }
    },
```

Additional debugging efforts may be needed to enable that functionality. As an alternative, `git` installation was added to `Dockerfile` for Netbox image used in this devcontainer.

## Visual Studio Code

The following `extensions` are installed:

### Extensions

- `Code Spell Checker`: as name says, highlighting of typos;
- `GitLens`: git blame in files, git history and many other git tools;
- `GitLab Workflow`: possibility to see GitLab CI/CD pipelines within IDE;

### Python specific extensions

- `Python` suite: to make Python development comfortable - syntax highlighting, debugger, definition lookup;
- `Ruff`: to enable formatting and linting with `ruff`;
- `autoDocstring - Python Docstring Generator`: autosuggestions for Python docstrings and ability to add them with `CMD + SHIFT + 2` / `CTRL + SHIFT + 2` keyboard shortcut;

### Markdown specific extensions

- `Markdown All In One`: keyboard shortcuts and multiple options for writing Markdown files easily;
- `markdownlint`: linter with set of useful rules that make Markdown files more readable;
- `Mermaid`: rendering of Mermaid diagrams within Visual Studio Code (GitLab has this built-in);
- `Markdown Footnotes`: possibility to use footnotes in Markdown files within Visual Studio Code (GitLab has this built-in);

### Other useful ones

- `Docker`: mainly, syntax highlighting for `Dockerfile`s;
- `Even Better Toml`: autoformatting and syntax highlighting for `.toml` files;
- `XML`: autoformatting and syntax highlighting for `.xml` files;
- `YAML`: autoformatting and syntax highlighting for `.yml` and `.yaml` files;
- `Shell Format`: autoformatting and syntax highlighting for shell scripts;
- `Todo Tree`: highlighting and additional pane for all `# TODO` (and many other) markers;

### Configuration

The following options are set up for Visual Studio Code:

- `python.defaultInterpreterPath`: selects Python interpreter for IDE to use - provided path to Netbox venv's Python;
- `python.analysis.extraPaths`: tells IDE where to look for Netbox modules - in the container, they are stored in `/opt/netbox/netbox`.
