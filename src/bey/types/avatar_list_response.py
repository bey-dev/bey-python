# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AvatarListResponse",
    "_HasMorePaginationModel",
    "HasMorePaginationModelData",
    "_NoMorePaginationModel",
    "NoMorePaginationModelData",
]


class HasMorePaginationModelData(BaseModel):
    id: str
    """Unique identifier of the object in the database."""


class _HasMorePaginationModel(BaseModel):
    data: List[HasMorePaginationModelData]
    """The list of results."""

    next_cursor: str
    """The cursor for the next page of results."""

    has_more: Optional[Literal[True]] = None
    """Whether there are more results to fetch."""


class NoMorePaginationModelData(BaseModel):
    id: str
    """Unique identifier of the object in the database."""


class _NoMorePaginationModel(BaseModel):
    data: List[NoMorePaginationModelData]
    """The list of results."""

    has_more: Optional[bool] = None
    """Whether there are more results to fetch."""


AvatarListResponse: TypeAlias = Union[_HasMorePaginationModel, _NoMorePaginationModel]
