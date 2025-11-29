"""AgentCore Runtime wrapper for the Strands agent."""

import logging
import os

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent, tool
from strands_tools import calculator, current_time  # type: ignore[import-untyped]

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, log_level),
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()],
)

logging.getLogger("strands").setLevel(log_level)

app = BedrockAgentCoreApp()


@tool
def letter_counter(word: str, letter: str) -> int:
    """Count how many times a letter appears in a word."""
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


def create_agent() -> Agent:
    """Create and configure the Strands agent."""
    return Agent(tools=[calculator, current_time, letter_counter])


@app.entrypoint
async def invoke(payload: dict[str, str] | None = None) -> dict[str, str]:
    """Main entrypoint for the agent invocation."""
    try:
        # Extract prompt from payload
        prompt = payload.get("prompt", "Hello!") if payload else "Hello!"
        logging.info(f"Received prompt: {prompt}")

        # Create and invoke the agent
        agent = create_agent()
        response = agent(prompt)

        response_text = response.message["content"][0]["text"]
        logging.info(f"Agent response: {response_text}")

        return {
            "status": "success",
            "response": response_text,
        }

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return {"status": "error", "error": str(e)}


if __name__ == "__main__":
    app.run()
