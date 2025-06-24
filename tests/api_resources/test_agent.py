# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bey import BeyondPresence, AsyncBeyondPresence
from bey.types import AgentListResponse, DeveloperAgentResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: BeyondPresence) -> None:
        agent = client.agent.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
        )
        assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: BeyondPresence) -> None:
        agent = client.agent.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
            capabilities=["webcam_vision"],
            greeting="Hello!",
            language="en",
            max_session_length_minutes=30,
            name="John Doe",
        )
        assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: BeyondPresence) -> None:
        response = client.agent.with_raw_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: BeyondPresence) -> None:
        with client.agent.with_streaming_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: BeyondPresence) -> None:
        agent = client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: BeyondPresence) -> None:
        response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: BeyondPresence) -> None:
        with client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: BeyondPresence) -> None:
        agent = client.agent.delete(
            "agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: BeyondPresence) -> None:
        response = client.agent.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: BeyondPresence) -> None:
        with client.agent.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: BeyondPresence) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.delete(
                "",
            )


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBeyondPresence) -> None:
        agent = await async_client.agent.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
        )
        assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeyondPresence) -> None:
        agent = await async_client.agent.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
            capabilities=["webcam_vision"],
            greeting="Hello!",
            language="en",
            max_session_length_minutes=30,
            name="John Doe",
        )
        assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.agent.with_raw_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.agent.with_streaming_response.create(
            avatar_id="01234567-89ab-cdef-0123-456789abcdef",
            system_prompt="You are a helpful assistant.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(DeveloperAgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBeyondPresence) -> None:
        agent = await async_client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncBeyondPresence) -> None:
        agent = await async_client.agent.delete(
            "agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBeyondPresence) -> None:
        response = await async_client.agent.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBeyondPresence) -> None:
        async with async_client.agent.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBeyondPresence) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.delete(
                "",
            )
