# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["CallListResponse", "CallListResponseItem"]


class CallListResponseItem(BaseModel):
    id: str
    """The ID of the call."""

    agent_id: str
    """The ID of the agent handling the call."""

    ended_at: Optional[str] = None
    """The end time of the call in ISO 8601 format.

    If null, the call might still be ongoing.
    """

    started_at: str
    """The start time of the call in ISO 8601 format."""


CallListResponse: TypeAlias = List[CallListResponseItem]
