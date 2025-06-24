# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bey import BeyondPresence, AsyncBeyondPresence
from bey.types import AvatarListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: BeyondPresence) -> None:
        avatar = client.avatar.list()
        assert_matches_type(AvatarListResponse, avatar, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: BeyondPresence) -> None:
        response = client.avatar.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarListResponse, avatar, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: BeyondPresence) -> None:
        with client.avatar.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarListResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvatar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBeyondPresence) -> None:
        avatar = await async_client.avatar.list()
        assert_matches_type(AvatarListResponse, avatar, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.avatar.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarListResponse, avatar, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.avatar.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarListResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True
