# Strands Agent

A Strands AI agent built with Python 3.13.

## Project Structure

```
agent/
├── src/
│   └── agentcore_app.py       # Agent implementation
├── tests/
│   └── test_agent.py          # Tests
├── pyproject.toml             # Project config, dependencies & tool settings
├── Dockerfile                 # Container definition for deployment
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

This installs only runtime dependencies without dev tools.

## Usage

### Local Testing

Run the AgentCore app locally:

```bash
python src/agentcore_app.py
```

In another terminal, test it:

```bash
# Simple query
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is 42 * 137?"}'

# Multiple tools
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What time is it and how many Rs in strawberry?"}'
```

This simulates how the agent runs in AWS AgentCore Runtime.

### Cloud Deployment

See [DEPLOYMENT.md](../DEPLOYMENT.md) for deploying to AWS Bedrock AgentCore Runtime.

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

## Configuration

All project configuration is centralized in `pyproject.toml`:

- **Dependencies**: Runtime and development dependencies
- **Build System**: Hatchling build backend
- **Black**: Code formatting (line length: 100)
- **Ruff**: Linting (Python 3.13 target)
- **Mypy**: Type checking (strict mode)
- **Pytest**: Testing framework
