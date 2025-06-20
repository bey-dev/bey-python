# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str
    """The unique identifier (ID) of the session."""

    avatar_id: str
    """The ID of the avatar used in the session."""

    created_at: datetime
    """The timestamp of when the session was created."""

    livekit_token: str
    """The LiveKit token used to join your LiveKit room."""

    livekit_url: str
    """The LiveKit URL you chose when creating your LiveKit project."""
