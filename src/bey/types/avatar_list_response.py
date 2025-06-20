# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AvatarListResponse", "AvatarListResponseItem"]


class AvatarListResponseItem(BaseModel):
    id: str
    """The unique identifier (ID) of the avatar."""

    name: str
    """The name of the avatar."""


AvatarListResponse: TypeAlias = List[AvatarListResponseItem]
