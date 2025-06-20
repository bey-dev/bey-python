# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .developer_agent_response import DeveloperAgentResponse

__all__ = ["AgentListResponse"]

AgentListResponse: TypeAlias = List[DeveloperAgentResponse]
