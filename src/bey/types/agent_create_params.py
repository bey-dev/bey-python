# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AgentCreateParams",
    "Capability",
    "CapabilityWebcamVision",
    "CapabilityWakeupMode",
    "Llm",
    "LlmOpenAI",
    "LlmOpenAICompatible",
]


class AgentCreateParams(TypedDict, total=False):
    avatar_id: Required[str]
    """The ID of the avatar to use."""

    system_prompt: Required[str]
    """The system prompt to use."""

    capabilities: Iterable[Capability]
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

    llm: Optional[Llm]
    """Configuration for the LLM to use."""

    max_session_length_minutes: Optional[int]
    """The maximum session length in minutes."""

    name: Optional[str]
    """The display name to use."""


class CapabilityWebcamVision(TypedDict, total=False):
    type: Literal["webcam_vision"]


class CapabilityWakeupMode(TypedDict, total=False):
    triggers: Required[List[str]]

    type: Literal["wakeup_mode"]


Capability: TypeAlias = Union[CapabilityWebcamVision, CapabilityWakeupMode]


class LlmOpenAI(TypedDict, total=False):
    type: Literal["openai"]


class LlmOpenAICompatible(TypedDict, total=False):
    api_id: Required[str]

    model: Required[str]

    temperature: Required[float]

    type: Literal["openai_compatible"]


Llm: TypeAlias = Union[LlmOpenAI, LlmOpenAICompatible]
