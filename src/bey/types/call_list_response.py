# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "CallListResponse",
    "HasMorePageCallResponse",
    "HasMorePageCallResponseData",
    "HasMorePageCallResponseDataStatus",
    "HasMorePageCallResponseDataStatusToStartCallStatus",
    "HasMorePageCallResponseDataStatusOngoingCallStatus",
    "HasMorePageCallResponseDataStatusCompletedCallStatus",
    "NoMorePageCallResponse",
    "NoMorePageCallResponseData",
    "NoMorePageCallResponseDataStatus",
    "NoMorePageCallResponseDataStatusToStartCallStatus",
    "NoMorePageCallResponseDataStatusOngoingCallStatus",
    "NoMorePageCallResponseDataStatusCompletedCallStatus",
]


class HasMorePageCallResponseDataStatusToStartCallStatus(BaseModel):
    """Status for call that has not yet started."""

    type: Optional[Literal["to_start"]] = None


class HasMorePageCallResponseDataStatusOngoingCallStatus(BaseModel):
    """Status for call that is currently ongoing."""

    started_at: str
    """Start time in ISO 8601 format."""

    type: Optional[Literal["ongoing"]] = None


class HasMorePageCallResponseDataStatusCompletedCallStatus(BaseModel):
    """Status for call that has completed."""

    ended_at: str
    """End time in ISO 8601 format."""

    started_at: str
    """Start time in ISO 8601 format."""

    type: Optional[Literal["completed"]] = None


HasMorePageCallResponseDataStatus: TypeAlias = Annotated[
    Union[
        HasMorePageCallResponseDataStatusToStartCallStatus,
        HasMorePageCallResponseDataStatusOngoingCallStatus,
        HasMorePageCallResponseDataStatusCompletedCallStatus,
    ],
    PropertyInfo(discriminator="type"),
]


class HasMorePageCallResponseData(BaseModel):
    """Response model for a call."""

    id: str
    """Unique identifier of the object in the database."""

    agent_id: str
    """ID of agent managing the call."""

    status: HasMorePageCallResponseDataStatus
    """Status for call that has not yet started."""

    tags: Optional[Dict[str, str]] = None
    """Tags for the call"""


class HasMorePageCallResponse(BaseModel):
    data: List[HasMorePageCallResponseData]
    """List of objects."""

    next_cursor: str
    """The cursor for the next page of objects."""

    has_more: Optional[Literal[True]] = None
    """Whether there are more objects to fetch."""


class NoMorePageCallResponseDataStatusToStartCallStatus(BaseModel):
    """Status for call that has not yet started."""

    type: Optional[Literal["to_start"]] = None


class NoMorePageCallResponseDataStatusOngoingCallStatus(BaseModel):
    """Status for call that is currently ongoing."""

    started_at: str
    """Start time in ISO 8601 format."""

    type: Optional[Literal["ongoing"]] = None


class NoMorePageCallResponseDataStatusCompletedCallStatus(BaseModel):
    """Status for call that has completed."""

    ended_at: str
    """End time in ISO 8601 format."""

    started_at: str
    """Start time in ISO 8601 format."""

    type: Optional[Literal["completed"]] = None


NoMorePageCallResponseDataStatus: TypeAlias = Annotated[
    Union[
        NoMorePageCallResponseDataStatusToStartCallStatus,
        NoMorePageCallResponseDataStatusOngoingCallStatus,
        NoMorePageCallResponseDataStatusCompletedCallStatus,
    ],
    PropertyInfo(discriminator="type"),
]


class NoMorePageCallResponseData(BaseModel):
    """Response model for a call."""

    id: str
    """Unique identifier of the object in the database."""

    agent_id: str
    """ID of agent managing the call."""

    status: NoMorePageCallResponseDataStatus
    """Status for call that has not yet started."""

    tags: Optional[Dict[str, str]] = None
    """Tags for the call"""


class NoMorePageCallResponse(BaseModel):
    data: List[NoMorePageCallResponseData]
    """List of objects."""

    has_more: Optional[Literal[False]] = None
    """Whether there are more objects to fetch."""


CallListResponse: TypeAlias = Union[HasMorePageCallResponse, NoMorePageCallResponse]
