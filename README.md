# Strands Agent Template

Template repo for deploying Strands AI agents to AWS Bedrock AgentCore Runtime using CDK.

> **Note**: This is a work in progress. See [open issues](https://github.com/deeheber/strands-agent/issues) for remaining work.

## Structure

```
strands-agent/
├── agent/    # Python 3.13 agent implementation
├── cdk/      # TypeScript CDK infrastructure
└── .github/  # CI/CD workflows
```

## Quick Start

### Local Testing

```bash
cd agent
source .venv/bin/activate
python src/agentcore_app.py

# In another terminal
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is 42 * 137?"}'
```

### Deploy to AWS

```bash
# Ensure AWS CLI is configured for us-west-2
aws configure set region us-west-2

cd cdk
npm install
npm run build
cdk deploy
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

**Note**: This project is configured for **us-west-2**. To use a different region, update the environment variables in `agent/Dockerfile`.

## CI/CD

Automated testing via GitHub Actions on every push/PR to `main`:

- `agent-ci.yml` - Python testing, type checking, linting
- `cdk-ci.yml` - TypeScript testing, type checking, linting
