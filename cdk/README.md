# CDK Infrastructure

TypeScript CDK infrastructure for deploying Strands agents to AWS.

## Quick Start

```bash
npm install
npm run build
npm run cdk:deploy
```

## Prerequisites

- Node.js 24 (from `.nvmrc`)
- AWS CLI configured (`aws configure` or `AWS_PROFILE`)

## Common Commands

```bash
# Development
npm run build          # Compile TypeScript
npm run watch          # Watch mode
npm test               # Run tests

# Code Quality
npm run fix            # Auto-fix lint + format
npm run check          # Check lint + format (CI)

# Deployment
npm run cdk:deploy     # Deploy stacks
npm run cdk:diff       # Show changes
npm run cdk:destroy    # Destroy stacks
```

## CI/CD

Automated testing runs on every push/PR via `.github/workflows/cdk-ci.yml`
