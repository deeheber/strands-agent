"""Tests for the agent."""

import pytest

from src.agentcore_app import create_agent, letter_counter


def test_create_agent() -> None:
    """Test agent creation."""
    agent = create_agent()
    assert agent is not None


def test_agent_has_tools() -> None:
    """Test agent has expected tools registered."""
    agent = create_agent()
    tool_names = agent.tool_names
    assert "calculator" in tool_names
    assert "current_time" in tool_names
    assert "letter_counter" in tool_names


def test_letter_counter_basic() -> None:
    """Test letter_counter counts correctly."""
    assert letter_counter("strawberry", "r") == 3
    assert letter_counter("hello", "l") == 2
    assert letter_counter("python", "p") == 1


def test_letter_counter_case_insensitive() -> None:
    """Test letter_counter is case-insensitive."""
    assert letter_counter("Hello", "h") == 1
    assert letter_counter("HELLO", "h") == 1
    assert letter_counter("hello", "H") == 1


def test_letter_counter_letter_not_found() -> None:
    """Test letter_counter returns 0 when letter not in word."""
    assert letter_counter("hello", "z") == 0
    assert letter_counter("python", "x") == 0


def test_letter_counter_empty_string() -> None:
    """Test letter_counter handles empty strings."""
    assert letter_counter("", "a") == 0
    with pytest.raises(ValueError, match="must be a single character"):
        letter_counter("hello", "")


def test_letter_counter_invalid_input() -> None:
    """Test letter_counter validates single character input."""
    with pytest.raises(ValueError, match="must be a single character"):
        letter_counter("hello", "ab")

    with pytest.raises(ValueError, match="must be a single character"):
        letter_counter("hello", "abc")


def test_letter_counter_type_validation() -> None:
    """Test letter_counter handles invalid types."""
    assert letter_counter(123, "a") == 0  # type: ignore[arg-type]
    assert letter_counter("hello", 123) == 0  # type: ignore[arg-type]


def test_agent_callable() -> None:
    """Test agent is callable (basic smoke test without LLM call)."""
    agent = create_agent()
    assert callable(agent)
    assert hasattr(agent, "invoke_async")
    assert agent.name is not None


def test_invoke_payload_extraction() -> None:
    """Test payload extraction logic."""
    # Test with prompt
    payload = {"prompt": "What is the answer?"}
    prompt = payload.get("prompt", "Hello!")
    assert prompt == "What is the answer?"

    # Test with None
    payload = None
    prompt = payload.get("prompt", "Hello!") if payload else "Hello!"
    assert prompt == "Hello!"

    # Test with empty dict
    payload = {}
    prompt = payload.get("prompt", "Hello!")
    assert prompt == "Hello!"
