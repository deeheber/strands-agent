import logging
import os

from strands import Agent, tool
from strands_tools import calculator, current_time  # type: ignore[import-untyped]

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, log_level),
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()],
)

logging.getLogger("strands").setLevel(log_level)


@tool
def letter_counter(word: str, letter: str) -> int:
    """Count how many times a letter appears in a word."""
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


agent = Agent(tools=[calculator, current_time, letter_counter])


def main() -> None:
    message = """
I have 4 requests:

1. What is the time right now?
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓
"""
    agent(message)


if __name__ == "__main__":
    main()
