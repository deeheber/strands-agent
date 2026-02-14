# Strands Agent Template

CDK-based deployment template for Strands AI agents to AWS Bedrock AgentCore Runtime.

**Input**: Natural language prompts via AgentCore entrypoint
**Output**: Agent responses using Strands tools (calculator, current_time, letter_counter, etc.)

## Quick Reference

```bash
# Agent: cd agent && source .venv/bin/activate
python src/agentcore_app.py     # Run locally
./quality-check.sh              # All checks (auto-fix)

# CDK: cd cdk
npm run cdk:deploy              # Deploy
npm run fix                     # Auto-fix linting
```

## Key Files

- `agent/src/agentcore_app.py` - Agent implementation (local + cloud)
- `agent/src/tools/custom_tools.py` - Custom tool definitions
- `cdk/lib/strands-agent-stack.ts` - Infrastructure

## Detailed Standards

See `.kiro/steering/` for comprehensive guidance (shared with Kiro):
- `product.md` - Purpose and roadmap
- `tech.md` - Stack, commands, configuration
- `structure.md` - File organization
- `python-agent.md` - Python patterns (applies to `agent/**`)
- `typescript-cdk.md` - CDK patterns (applies to `cdk/**`)
