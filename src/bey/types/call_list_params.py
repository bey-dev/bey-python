# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CallListParams"]


class CallListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination."""

    limit: int
    """Maximum number of objects to return."""
