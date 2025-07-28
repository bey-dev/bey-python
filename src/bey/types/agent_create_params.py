# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .developer_agent_capability import DeveloperAgentCapability

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    avatar_id: Required[str]
    """The ID of the avatar to use."""

    system_prompt: Required[str]
    """The system prompt to use."""

    capabilities: List[DeveloperAgentCapability]
    """The extra capabilities to manage the call."""

    greeting: Optional[str]
    """What to say at the start of the session."""

    language: Optional[
        Literal[
            "ar",
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
            "ur",
            "vi",
        ]
    ]
    """Enum for languages with language codes as values."""

    max_session_length_minutes: Optional[int]
    """The maximum session length in minutes."""

    name: Optional[str]
    """The display name to use."""
