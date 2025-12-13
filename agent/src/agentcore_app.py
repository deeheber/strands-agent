"""AgentCore Runtime wrapper for the Strands agent."""

import logging
import os
from typing import Any

# Initialize OpenTelemetry only when running in AgentCore (not local development)
# Check for AgentCore environment indicators
is_agentcore = bool(
    os.getenv("AWS_EXECUTION_ENV") or 
    os.getenv("AWS_LAMBDA_FUNCTION_NAME") or 
    os.getenv("BEDROCK_AGENTCORE_RUNTIME_ID")
)

if is_agentcore:
    from aws_opentelemetry_distro.auto_instrumentation import AwsOpenTelemetryDistro
    # Initialize OTEL auto-instrumentation only in AgentCore
    AwsOpenTelemetryDistro().instrument()

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands_tools import calculator, current_time  # type: ignore[import-untyped]

from tools import letter_counter

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, log_level),
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()],
)

logging.getLogger("strands").setLevel(log_level)

app = BedrockAgentCoreApp()


def get_agent() -> Agent:
    """Create and return a Strands agent with configured tools."""
    return Agent(tools=[calculator, current_time, letter_counter])


@app.entrypoint
async def invoke(payload: dict[str, Any] | None = None) -> dict[str, Any]:
    """Main entrypoint for the agent invocation."""
    try:
        prompt = payload.get("prompt", "Hello!") if payload else "Hello!"
        logging.info(f"Received prompt: {prompt}")

        agent = get_agent()
        response = agent(prompt)
        response_text = response.message["content"][0]["text"]

        logging.info(f"Agent response: {response_text}")
        return {"status": "success", "response": response_text}

    except Exception as e:
        logging.error(f"Error processing request: {e}", exc_info=True)
        return {"status": "error", "error": "Internal processing error"}


if __name__ == "__main__":
    app.run()
