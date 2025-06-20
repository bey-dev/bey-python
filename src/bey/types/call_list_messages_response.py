# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["CallListMessagesResponse", "CallListMessagesResponseItem"]


class CallListMessagesResponseItem(BaseModel):
    message: str
    """The message content."""

    sender: Literal["ai", "user"]
    """The sender of the message."""

    sent_at: str
    """The time the message was sent in ISO 8601 format."""


CallListMessagesResponse: TypeAlias = List[CallListMessagesResponseItem]
