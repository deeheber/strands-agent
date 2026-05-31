# Strands Agent

Python 3.13 agent with calculator, time, and letter counter tools.

## Quick Start

```bash
uv sync --extra dev
uv run python src/agentcore_app.py

# Test in another terminal
curl -X POST http://localhost:8080/invocations -H "Content-Type: application/json" -d '{"prompt": "What is 42 * 137?"}'
```

## Configuration

**Environment Variables**: `uv run` automatically loads environment variables from a `.env` file when running locally, so no separate dotenv package is needed.

```bash
# Copy the example and customize
cp .env.example .env

# Edit .env file
BEDROCK_MODEL_ID=your-preferred-model-id
LOG_LEVEL=DEBUG
```

**Model**: Set `BEDROCK_MODEL_ID` environment variable (see `DEFAULT_MODEL_ID` in `src/agentcore_app.py` for current default)

**Available Models**: See [AWS Bedrock Model IDs documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html)

## Adding Tools

**Community Tools:**

```python
from strands_tools import calculator, current_time
def get_agent() -> Agent:
    return Agent(tools=[calculator, current_time, letter_counter])
```

Additional tools (e.g. `http_request`, `file_read`) are available from `strands-agents-tools` -- import any you want and add them to the `tools=[...]` list.

**Custom Tools:**

```python
# In src/tools/my_tools.py
@tool
def my_tool(param: str) -> str:
    """Tool description."""
    return f"Result: {param}"

# Export in src/tools/__init__.py
from .my_tools import my_tool
__all__ = ["letter_counter", "my_tool"]
```

## Development

```bash
./quality-check.sh        # All quality checks (recommended)
uv run pytest             # Tests only
```

See [DEPLOYMENT.md](../DEPLOYMENT.md) for cloud deployment.
