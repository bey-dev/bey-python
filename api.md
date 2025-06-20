# Agent

Types:

```python
from bey.types import DeveloperAgentCapability, DeveloperAgentResponse, AgentListResponse
```

Methods:

- <code title="post /v1/agent">client.agent.<a href="./src/bey/resources/agent.py">create</a>(\*\*<a href="src/bey/types/agent_create_params.py">params</a>) -> <a href="./src/bey/types/developer_agent_response.py">DeveloperAgentResponse</a></code>
- <code title="get /v1/agent">client.agent.<a href="./src/bey/resources/agent.py">list</a>() -> <a href="./src/bey/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agent/{agent_id}">client.agent.<a href="./src/bey/resources/agent.py">delete</a>(agent_id) -> object</code>

# Auth

Methods:

- <code title="get /v1/auth/verify">client.auth.<a href="./src/bey/resources/auth.py">verify</a>() -> object</code>

# Avatar

Types:

```python
from bey.types import AvatarListResponse
```

Methods:

- <code title="get /v1/avatar">client.avatar.<a href="./src/bey/resources/avatar.py">list</a>() -> <a href="./src/bey/types/avatar_list_response.py">AvatarListResponse</a></code>

# Calls

Types:

```python
from bey.types import CallListResponse, CallListMessagesResponse
```

Methods:

- <code title="get /v1/calls">client.calls.<a href="./src/bey/resources/calls.py">list</a>() -> <a href="./src/bey/types/call_list_response.py">CallListResponse</a></code>
- <code title="get /v1/calls/{call_id}/messages">client.calls.<a href="./src/bey/resources/calls.py">list_messages</a>(call_id) -> <a href="./src/bey/types/call_list_messages_response.py">CallListMessagesResponse</a></code>

# Session

Types:

```python
from bey.types import Session, SessionListResponse
```

Methods:

- <code title="post /v1/session">client.session.<a href="./src/bey/resources/session.py">create</a>(\*\*<a href="src/bey/types/session_create_params.py">params</a>) -> <a href="./src/bey/types/session.py">Session</a></code>
- <code title="get /v1/session/{id}">client.session.<a href="./src/bey/resources/session.py">retrieve</a>(id) -> <a href="./src/bey/types/session.py">Session</a></code>
- <code title="get /v1/session">client.session.<a href="./src/bey/resources/session.py">list</a>() -> <a href="./src/bey/types/session_list_response.py">SessionListResponse</a></code>
