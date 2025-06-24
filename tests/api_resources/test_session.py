# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bey import BeyondPresence, AsyncBeyondPresence
from bey.types import Session, SessionListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: BeyondPresence) -> None:
        session = client.session.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            livekit_token="<your-livekit-token>",
            livekit_url="wss://<your-domain>.livekit.cloud",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: BeyondPresence) -> None:
        response = client.session.with_raw_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            livekit_token="<your-livekit-token>",
            livekit_url="wss://<your-domain>.livekit.cloud",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: BeyondPresence) -> None:
        with client.session.with_streaming_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            livekit_token="<your-livekit-token>",
            livekit_url="wss://<your-domain>.livekit.cloud",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: BeyondPresence) -> None:
        session = client.session.retrieve(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: BeyondPresence) -> None:
        response = client.session.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: BeyondPresence) -> None:
        with client.session.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: BeyondPresence) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: BeyondPresence) -> None:
        session = client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: BeyondPresence) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: BeyondPresence) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBeyondPresence) -> None:
        session = await async_client.session.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            livekit_token="<your-livekit-token>",
            livekit_url="wss://<your-domain>.livekit.cloud",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.session.with_raw_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            livekit_token="<your-livekit-token>",
            livekit_url="wss://<your-domain>.livekit.cloud",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.session.with_streaming_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            livekit_token="<your-livekit-token>",
            livekit_url="wss://<your-domain>.livekit.cloud",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeyondPresence) -> None:
        session = await async_client.session.retrieve(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.session.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.session.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeyondPresence) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBeyondPresence) -> None:
        session = await async_client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
