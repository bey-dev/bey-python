# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .developer_agent_capability import DeveloperAgentCapability

__all__ = ["DeveloperAgentResponse"]


class DeveloperAgentResponse(BaseModel):
    id: str
    """Unique identifier of the object."""

    avatar_id: str
    """The ID of the avatar to use."""

    system_prompt: str
    """The system prompt to use."""

    capabilities: Optional[List[DeveloperAgentCapability]] = None
    """The extra capabilities to manage the call."""

    greeting: Optional[str] = None
    """What to say at the start of the session."""

    language: Optional[
        Literal[
            "bg",
            "zh",
            "cs",
            "da",
            "nl",
            "en",
            "en-AU",
            "en-GB",
            "en-US",
            "fi",
            "fr",
            "fr-CA",
            "fr-FR",
            "de",
            "el",
            "hi",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "ms",
            "no",
            "pl",
            "pt",
            "pt-BR",
            "pt-PT",
            "ro",
            "ru",
            "sk",
            "es",
            "sv",
            "tr",
            "uk",
            "vi",
        ]
    ] = None
    """Enum for languages with language codes as values."""

    max_session_length_minutes: Optional[int] = None
    """The maximum session length in minutes."""

    name: Optional[str] = None
    """The display name to use."""
