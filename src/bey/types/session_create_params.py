# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    avatar_id: Required[str]
    """The ID of the avatar to use in the session."""

    livekit_token: Required[str]
    """The LiveKit token used to join your LiveKit room."""

    livekit_url: Required[str]
    """The LiveKit URL you chose when creating your LiveKit project."""
