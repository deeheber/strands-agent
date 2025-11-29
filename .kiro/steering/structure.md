# Project Structure

## Repository Layout

```
strands-agent/
├── agent/              # Python agent implementation
│   ├── src/           # Source code
│   ├── tests/         # Test files
│   ├── .venv/         # Virtual environment (gitignored)
│   ├── .env.example   # Environment variable template
│   ├── pyproject.toml # Project config & dependencies
│   └── README.md      # Agent-specific documentation
├── cdk/                # TypeScript CDK infrastructure
│   ├── bin/           # CDK app entry point
│   ├── lib/           # Stack definitions
│   ├── test/          # CDK tests
│   ├── cdk.json       # CDK configuration
│   ├── package.json   # Node dependencies and scripts
│   └── README.md      # CDK-specific documentation
├── .github/
│   └── workflows/     # GitHub Actions CI/CD pipelines
│       ├── agent-ci.yml  # Python agent CI
│       └── cdk-ci.yml    # CDK infrastructure CI
├── .kiro/             # Kiro IDE configuration
│   └── steering/      # AI assistant guidance documents
└── README.md          # Root documentation
```

## Agent Directory (`agent/`)

### Source Code (`src/`)

- `agentcore_app.py` - Agent implementation (runs locally and in cloud)
- `__init__.py` - Package initialization

### Tests (`tests/`)

- `test_agent.py` - Agent test suite
- Test files should mirror source structure

### Configuration Files

- `pyproject.toml` - Single source of truth for dependencies, build config, tool settings, and Docker deployment
- `Dockerfile` - Container definition for AgentCore Runtime
- `.python-version` - Python version specification (3.13)
- `.env.example` - Template for environment variables (copy to `.env` for local config)

## Code Organization Patterns

### Agent Definition

- Agents are created using the `Agent` class from `strands`
- Tools are registered via the `tools` parameter
- Custom tools use the `@tool` decorator
- Agent execution should be wrapped in `if __name__ == "__main__":` to prevent running during imports

### AgentCore Integration

- AgentCore apps use `BedrockAgentCoreApp` from `bedrock_agentcore.runtime`
- Entry point decorated with `@app.entrypoint`
- Accepts payload with `prompt` field
- Returns dict with `status` and `response` or `error`
- Runs with `app.run()` for local testing or cloud deployment

### Tool Implementation

- Custom tools are Python functions decorated with `@tool`
- Include comprehensive docstrings with Args and Returns sections
- Type hints are required (enforced by mypy strict mode)
- Input validation should be explicit

### Logging

- Use Python's `logging` module
- Log level configurable via `LOG_LEVEL` environment variable
- Default level: INFO
- Format: `%(levelname)s | %(name)s | %(message)s`

## CDK Directory (`cdk/`)

### Infrastructure Code (`lib/`)

- `strands-agent-stack.ts` - CDK stack for deploying Strands agents to AgentCore Runtime
- Defines AgentCore Runtime resource, IAM execution roles, and Docker image build from local assets
- Uses `@aws-cdk/aws-bedrock-agentcore-alpha` constructs for AgentCore-specific resources
- Builds ARM64 container images locally and deploys to AgentCore

### Entry Point (`bin/`)

- `cdk.ts` - CDK app entry point
- Validates AWS credentials and instantiates stacks

### Tests (`test/`)

- `cdk.test.ts` - CDK stack tests
- Test files should validate synthesized CloudFormation templates

### Configuration Files

- `package.json` - Node dependencies and npm scripts
- `tsconfig.json` - TypeScript compiler configuration (ES2023, strict mode)
- `jest.config.ts` - Jest testing configuration
- `eslint.config.mjs` - ESLint linting rules (flat config)
- `.prettierrc` - Prettier formatting rules
- `cdk.json` - CDK app configuration and feature flags

## CI/CD

- GitHub Actions workflows in `.github/workflows/`
- **agent-ci.yml** - Python agent testing, type checking, linting, and formatting
- **cdk-ci.yml** - CDK testing, type checking, linting, and formatting
- Both run on every push/PR to main branch
