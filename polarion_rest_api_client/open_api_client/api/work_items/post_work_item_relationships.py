# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.relationship_data_list_request import (
    RelationshipDataListRequest,
)
from ...models.relationship_data_single_request import (
    RelationshipDataSingleRequest,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    relationship_id: str,
    *,
    body: Union[
        "RelationshipDataListRequest", "RelationshipDataSingleRequest"
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/{projectId}/workitems/{workItemId}/relationships/{relationshipId}".format(
            projectId=project_id,
            workItemId=work_item_id,
            relationshipId=relationship_id,
        ),
    }

    _body: Dict[str, Any]
    if isinstance(body, RelationshipDataSingleRequest):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        return None
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        return None
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    work_item_id: str,
    relationship_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "RelationshipDataListRequest", "RelationshipDataSingleRequest"
    ],
) -> Response[Any]:
    """Creates a list of Work Item Relationships.

    Args:
        project_id (str):
        work_item_id (str):
        relationship_id (str):
        body (Union['RelationshipDataListRequest', 'RelationshipDataSingleRequest']): List of
            generic contents Example: {'data': [{'type': 'plans', 'id': 'MyProjectId/MyResourceId'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        relationship_id=relationship_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    relationship_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "RelationshipDataListRequest", "RelationshipDataSingleRequest"
    ],
) -> Response[Any]:
    """Creates a list of Work Item Relationships.

    Args:
        project_id (str):
        work_item_id (str):
        relationship_id (str):
        body (Union['RelationshipDataListRequest', 'RelationshipDataSingleRequest']): List of
            generic contents Example: {'data': [{'type': 'plans', 'id': 'MyProjectId/MyResourceId'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        relationship_id=relationship_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
