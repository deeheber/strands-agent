# Strands Agent

A Strands AI agent built with Python 3.13.

## Project Structure

```
agent/
├── src/
│   └── agent.py               # Main agent code
├── tests/
│   └── test_agent.py          # Tests
├── pyproject.toml             # Project config and dependencies
├── .python-version            # Python version (3.13)
└── README.md
```

## Setup

1. Create a virtual environment:

```bash
python3.13 -m venv .venv

# Activate on macOS/Linux:
source .venv/bin/activate

# Activate on Windows:
.venv\Scripts\activate
```

2. Configure environment variables (optional):

```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Install dependencies:

**Development (includes testing/linting tools):**

```bash
pip install -e ".[dev]"
```

This installs:

- `strands-agents` - Main agent framework
- `strands-agents-tools` - Community tools library
- `strands-agents-builder` - Development utilities
- `pytest` - Testing framework
- `mypy` - Type checker
- `ruff` - Linter
- `black` - Code formatter

**Production (only main dependencies):**

```bash
pip install .
```

This installs only `strands-agents` without dev tools.

## Usage

Run the agent:

```bash
python src/agent.py
```

### Environment Variables

- `LOG_LEVEL` - Control logging verbosity (default: `INFO`)
  - Options: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
  - Example: `LOG_LEVEL=DEBUG python src/agent.py`

## Development

### Run tests:

```bash
pytest
```

### Type check:

```bash
mypy src/
```

### Lint code:

```bash
ruff check .
```

### Format code:

```bash
black .
```

### Auto-fix linting issues:

```bash
ruff check --fix .
```

### Run all checks:

```bash
pytest && mypy src/ && ruff check . && black --check .
```

## Tools Configuration

Development tools are configured in `pyproject.toml`:

- **Black**: Code formatting
- **Ruff**: Linting
- **Mypy**: Type checking
- **Pytest**: Testing framework
