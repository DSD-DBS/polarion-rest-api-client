# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{projectId}/workitems/{workItemId}/externallylinkedworkitems/{roleId}/{hostname}/{targetProjectId}/{linkedWorkItemId}".format(
            projectId=project_id,
            workItemId=work_item_id,
            roleId=role_id,
            hostname=hostname,
            targetProjectId=target_project_id,
            linkedWorkItemId=linked_work_item_id,
        ),
    }

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
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Deletes the specified Externally Linked Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        hostname (str):
        target_project_id (str):
        linked_work_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        hostname=hostname,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Deletes the specified Externally Linked Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        hostname (str):
        target_project_id (str):
        linked_work_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        hostname=hostname,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)