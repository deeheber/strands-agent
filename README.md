# Strands Agent Template

Template repo for Strands AI agents. Intended to be used as a starter for new projects.

## Structure

```
strands-agent/
├── agent/    # Python 3.13 agent implementation
├── cdk/      # TypeScript CDK infrastructure
└── .github/  # CI/CD workflows
```

## Quick Start

**Python Agent**

```bash
cd agent
# See agent/README.md for setup
```

**CDK Infrastructure**

```bash
cd cdk
npm install
# See cdk/README.md for deployment
```

## CI/CD

Automated testing via GitHub Actions on every push/PR to `main`:

- `agent-ci.yml` - Python testing, type checking, linting
- `cdk-ci.yml` - TypeScript testing, type checking, linting
