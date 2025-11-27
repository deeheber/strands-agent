"""Main agent implementation."""

from strands_agents import Agent


def create_agent() -> Agent:
    """Create and configure the Strands agent."""
    agent = Agent(
        name="my-agent",
        instructions="You are a helpful AI assistant.",
    )
    
    return agent


if __name__ == "__main__":
    agent = create_agent()
    agent.run()
