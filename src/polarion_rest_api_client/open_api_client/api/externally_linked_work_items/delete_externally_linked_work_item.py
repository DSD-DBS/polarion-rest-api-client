# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/projects/{project_id}/workitems/{work_item_id}/externallylinkedworkitems/{role_id}/{hostname}/{target_project_id}/{linked_work_item_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Errors | None:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Errors.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Errors.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Errors]:
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
    client: AuthenticatedClient | Client,
) -> Response[Any | Errors]:
    """Deletes the specified Externally Linked Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        hostname (str):
        target_project_id (str):
        linked_work_item_id (str):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Response[Union[Any, Errors]]
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


def sync(
    project_id: str,
    work_item_id: str,
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Errors | None:
    """Deletes the specified Externally Linked Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        hostname (str):
        target_project_id (str):
        linked_work_item_id (str):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Union[Any, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        hostname=hostname,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Errors]:
    """Deletes the specified Externally Linked Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        hostname (str):
        target_project_id (str):
        linked_work_item_id (str):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Response[Union[Any, Errors]]
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


async def asyncio(
    project_id: str,
    work_item_id: str,
    role_id: str,
    hostname: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Errors | None:
    """Deletes the specified Externally Linked Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        hostname (str):
        target_project_id (str):
        linked_work_item_id (str):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Union[Any, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            role_id=role_id,
            hostname=hostname,
            target_project_id=target_project_id,
            linked_work_item_id=linked_work_item_id,
            client=client,
        )
    ).parsed
