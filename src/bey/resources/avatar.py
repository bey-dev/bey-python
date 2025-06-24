# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.avatar_list_response import AvatarListResponse

__all__ = ["AvatarResource", "AsyncAvatarResource"]


class AvatarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvatarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bey-dev/bey-python#accessing-raw-response-data-eg-headers
        """
        return AvatarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bey-dev/bey-python#with_streaming_response
        """
        return AvatarResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvatarListResponse:
        """
        List all avatars the owner of the API key has access to.

        See docs.bey.dev/avatar for more information on avatars.
        """
        return self._get(
            "/v1/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarListResponse,
        )


class AsyncAvatarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvatarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bey-dev/bey-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvatarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bey-dev/bey-python#with_streaming_response
        """
        return AsyncAvatarResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvatarListResponse:
        """
        List all avatars the owner of the API key has access to.

        See docs.bey.dev/avatar for more information on avatars.
        """
        return await self._get(
            "/v1/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarListResponse,
        )


class AvatarResourceWithRawResponse:
    def __init__(self, avatar: AvatarResource) -> None:
        self._avatar = avatar

        self.list = to_raw_response_wrapper(
            avatar.list,
        )


class AsyncAvatarResourceWithRawResponse:
    def __init__(self, avatar: AsyncAvatarResource) -> None:
        self._avatar = avatar

        self.list = async_to_raw_response_wrapper(
            avatar.list,
        )


class AvatarResourceWithStreamingResponse:
    def __init__(self, avatar: AvatarResource) -> None:
        self._avatar = avatar

        self.list = to_streamed_response_wrapper(
            avatar.list,
        )


class AsyncAvatarResourceWithStreamingResponse:
    def __init__(self, avatar: AsyncAvatarResource) -> None:
        self._avatar = avatar

        self.list = async_to_streamed_response_wrapper(
            avatar.list,
        )
