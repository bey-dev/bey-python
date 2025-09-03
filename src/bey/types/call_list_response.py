# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "CallListResponse",
    "HasMorePageCallResponse",
    "HasMorePageCallResponseData",
    "NoMorePageCallResponse",
    "NoMorePageCallResponseData",
]


class HasMorePageCallResponseData(BaseModel):
    id: str
    """Unique identifier of the object in the database."""

    agent_id: str
    """ID of managing agent."""

    ended_at: Optional[str] = None
    """End time in ISO 8601 format. If null, call might still be ongoing."""

    started_at: str
    """Start time in ISO 8601 format."""


class HasMorePageCallResponse(BaseModel):
    data: List[HasMorePageCallResponseData]
    """List of objects."""

    next_cursor: str
    """The cursor for the next page of objects."""

    has_more: Optional[Literal[True]] = None
    """Whether there are more objects to fetch."""


class NoMorePageCallResponseData(BaseModel):
    id: str
    """Unique identifier of the object in the database."""

    agent_id: str
    """ID of managing agent."""

    ended_at: Optional[str] = None
    """End time in ISO 8601 format. If null, call might still be ongoing."""

    started_at: str
    """Start time in ISO 8601 format."""


class NoMorePageCallResponse(BaseModel):
    data: List[NoMorePageCallResponseData]
    """List of objects."""

    has_more: Optional[bool] = None
    """Whether there are more objects to fetch."""


CallListResponse: TypeAlias = Union[HasMorePageCallResponse, NoMorePageCallResponse]
