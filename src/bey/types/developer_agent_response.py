# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .developer_agent_capability import DeveloperAgentCapability

__all__ = ["DeveloperAgentResponse"]


class DeveloperAgentResponse(BaseModel):
    id: str
    """The unique identifier (ID) of the agent."""

    avatar_id: str
    """The ID of the avatar to use."""

    system_prompt: str
    """The system prompt to use."""

    capabilities: Optional[List[DeveloperAgentCapability]] = None
    """The agent capabilities."""

    greeting: Optional[str] = None
    """What to say at the start of the session."""

    language: Optional[str] = None
    """The language to use."""

    max_session_length_minutes: Optional[int] = None
    """The maximum session length in minutes."""

    name: Optional[str] = None
    """The agent name."""
