# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .developer_agent_capability import DeveloperAgentCapability

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    avatar_id: Required[str]
    """The ID of the avatar to use."""

    system_prompt: Required[str]
    """The system prompt to use."""

    capabilities: List[DeveloperAgentCapability]
    """The agent capabilities."""

    greeting: Optional[str]
    """What to say at the start of the session."""

    language: Optional[str]
    """The language to use."""

    max_session_length_minutes: Optional[int]
    """The maximum session length in minutes."""

    name: Optional[str]
    """The agent name."""
