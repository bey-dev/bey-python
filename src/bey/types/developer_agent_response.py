# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "DeveloperAgentResponse",
    "Capability",
    "CapabilityWebcamVision",
    "CapabilityWakeupMode",
    "Llm",
    "LlmOpenAI",
    "LlmOpenAICompatible",
]


class CapabilityWebcamVision(BaseModel):
    type: Optional[Literal["webcam_vision"]] = None


class CapabilityWakeupMode(BaseModel):
    triggers: List[str]

    type: Optional[Literal["wakeup_mode"]] = None


Capability: TypeAlias = Annotated[
    Union[CapabilityWebcamVision, CapabilityWakeupMode], PropertyInfo(discriminator="type")
]


class LlmOpenAI(BaseModel):
    type: Optional[Literal["openai"]] = None


class LlmOpenAICompatible(BaseModel):
    api_id: str

    model: str

    temperature: float

    type: Optional[Literal["openai_compatible"]] = None


Llm: TypeAlias = Annotated[Union[LlmOpenAI, LlmOpenAICompatible, None], PropertyInfo(discriminator="type")]


class DeveloperAgentResponse(BaseModel):
    id: str
    """Unique identifier of the object in the database."""

    avatar_id: str
    """The ID of the avatar to use."""

    system_prompt: str
    """The system prompt to use."""

    capabilities: Optional[List[Capability]] = None
    """The extra capabilities to manage the call."""

    greeting: Optional[str] = None
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
    ] = None
    """Enum for languages with language codes as values."""

    llm: Optional[Llm] = None
    """Configuration for the LLM to use."""

    max_session_length_minutes: Optional[int] = None
    """The maximum session length in minutes."""

    name: Optional[str] = None
    """The display name to use."""
