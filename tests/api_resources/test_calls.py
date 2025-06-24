# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bey import BeyondPresence, AsyncBeyondPresence
from bey.types import CallListResponse, CallListMessagesResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: BeyondPresence) -> None:
        call = client.calls.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: BeyondPresence) -> None:
        response = client.calls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: BeyondPresence) -> None:
        with client.calls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_messages(self, client: BeyondPresence) -> None:
        call = client.calls.list_messages(
            "call_id",
        )
        assert_matches_type(CallListMessagesResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_messages(self, client: BeyondPresence) -> None:
        response = client.calls.with_raw_response.list_messages(
            "call_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListMessagesResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_messages(self, client: BeyondPresence) -> None:
        with client.calls.with_streaming_response.list_messages(
            "call_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListMessagesResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_messages(self, client: BeyondPresence) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.calls.with_raw_response.list_messages(
                "",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBeyondPresence) -> None:
        call = await async_client.calls.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.calls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.calls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncBeyondPresence) -> None:
        call = await async_client.calls.list_messages(
            "call_id",
        )
        assert_matches_type(CallListMessagesResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.calls.with_raw_response.list_messages(
            "call_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListMessagesResponse, call, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.calls.with_streaming_response.list_messages(
            "call_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListMessagesResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncBeyondPresence) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.calls.with_raw_response.list_messages(
                "",
            )
