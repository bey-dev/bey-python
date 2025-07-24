# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AvatarListParams"]


class AvatarListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination"""

    limit: int
    """The maximum number of avatars to return"""
