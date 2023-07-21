# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

import os
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/workitems/{workItemId}/linkedworkitems/{roleId}/{targetProjectId}/{linkedWorkItemId}".format(
        client.base_url,
        projectId=project_id,
        workItemId=work_item_id,
        roleId=role_id,
        targetProjectId=target_project_id,
        linkedWorkItemId=linked_work_item_id,
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
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
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
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
    *, client: Client, response: httpx.Response
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
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Deletes the specified instance.

     Deletes the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
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
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        proxies=os.getenv("PROXIES"),
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Deletes the specified instance.

     Deletes the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
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
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        client=client,
    )

    async with httpx.AsyncClient(
        verify=client.verify_ssl, proxies=os.getenv("PROXIES")
    ) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
