# Contributing to Strands Agent Template

Thank you for your interest in contributing to the Strands Agent Template! This guide will help you get started with development and ensure your contributions align with our project standards.

## Getting Started

### Prerequisites

- **Python 3.13** (see `.python-version`)
- **[uv](https://docs.astral.sh/uv/)** (Python package manager)
- **Node.js 24** (see `.nvmrc`)
- **Docker** (for deployment)
- **AWS CLI** configured with appropriate permissions
- **Git** for version control

### Initial Setup

1. **Fork and clone the repository**

   ```bash
   git clone https://github.com/your-username/strands-agent.git
   cd strands-agent
   ```

2. **Set up the Python environment**

   ```bash
   cd agent
   uv sync --extra dev
   ```

3. **Set up the CDK environment**

   ```bash
   cd cdk
   npm install
   ```

4. **Configure environment variables**
   ```bash
   cd agent
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Development Workflow

### Python Agent Development

**Running the agent locally:**

```bash
cd agent
uv run python src/agentcore_app.py
```

**Quality checks (recommended before committing):**

```bash
./quality-check.sh  # Runs all checks with auto-fixes
```

**Manual quality validation:**

```bash
uv run pytest && uv run mypy src/ && uv run ruff check --fix . && uv run black .
```

### CDK Infrastructure Development

**Building and testing:**

```bash
cd cdk
npm run build
npm test
```

**Linting and formatting:**

```bash
npm run lint
npm run format
```

**Deploying to AWS:**

```bash
cdk synth    # Generate CloudFormation
cdk deploy   # Deploy to AWS
```

## Code Standards

### Python Code Style

- **Line length**: 100 characters
- **Formatter**: Black
- **Linter**: Ruff with auto-fix enabled
- **Type checker**: mypy in strict mode
- **Testing**: pytest

### TypeScript Code Style

- **Formatter**: Prettier
- **Linter**: ESLint
- **Testing**: Vitest with snapshot testing
- **Imports**: Use explicit imports, avoid wildcards

**Good TypeScript imports:**

```typescript
// ✅ Good
import { Stack, StackProps } from "aws-cdk-lib";
import { Function, Runtime } from "aws-cdk-lib/aws-lambda";

// ❌ Avoid
import * as cdk from "aws-cdk-lib";
```

## Project Structure

### Adding New Tools

1. **Create tool file** in `agent/src/tools/`
2. **Implement with `@tool` decorator** and proper type hints
3. **Export in `__init__.py`**
4. **Add tests** in `agent/tests/test_tools/`

Example tool structure:

```python
from strands import tool

@tool
def my_custom_tool(input_param: str) -> str:
    """Tool description for the agent."""
    return f"Processed: {input_param}"
```

### Testing Guidelines

**Python tests:**

- Mirror source structure in `tests/` directory
- Use pytest fixtures and parametrize for comprehensive coverage
- Test both success and error cases

**CDK tests:**

- Use Vitest with snapshot testing
- Test IAM policies, resource configurations, and security settings
- Update snapshots when infrastructure changes are intentional

## Contribution Process

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Follow the code standards outlined above
- Add tests for new functionality
- Update documentation as needed

### 3. Run Quality Checks

**For Python changes:**

```bash
cd agent
./quality-check.sh
```

**For CDK changes:**

```bash
cd cdk
npm run build && npm test && npm run lint
```

### 4. Commit Your Changes

Use conventional commit messages:

```bash
git commit -m "feat: add new custom tool for data processing"
git commit -m "fix: resolve memory leak in agent execution"
git commit -m "docs: update deployment instructions"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Create a pull request with:

- Clear description of changes
- Reference to any related issues
- Screenshots/examples if applicable

## CI/CD Pipeline

Our GitHub Actions workflows will automatically:

**Python Agent CI (`agent-ci.yml`):**

- Run pytest
- Type check with mypy
- Lint with ruff
- Format check with black

**CDK Infrastructure CI (`cdk-ci.yml`):**

- Build TypeScript
- Run Vitest tests
- Lint with ESLint
- Format check with Prettier

All checks must pass before merging.

## Community Tools

We use `strands-agents-tools` for common functionality. The template currently wires up `calculator` and `current_time`; additional tools (e.g. `http_request`, `browser`) are available in the same package:

```python
from strands_tools import calculator, current_time
# Also available: http_request, browser, file_read, ...
```

When adding tools, consider if they should be:

- **Custom tools** (domain-specific to your use case)
- **Community contributions** (general-purpose, consider contributing upstream)

## Getting Help

- **Issues**: Create GitHub issues for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Documentation**: Check README.md and DEPLOYMENT.md for guidance

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow our coding standards consistently

Thank you for contributing to make this template better for everyone!
