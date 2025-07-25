# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.linkedoslcresources_list_post_request import (
    LinkedoslcresourcesListPostRequest,
)
from ...models.linkedoslcresources_list_post_response import (
    LinkedoslcresourcesListPostResponse,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    body: LinkedoslcresourcesListPostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/workitems/{work_item_id}/linkedoslcresources",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Errors, LinkedoslcresourcesListPostResponse] | None:
    if response.status_code == 201:
        response_201 = LinkedoslcresourcesListPostResponse.from_dict(
            response.json()
        )

        return response_201
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if response.status_code == 406:
        response_406 = Errors.from_dict(response.json())

        return response_406
    if response.status_code == 409:
        response_409 = Errors.from_dict(response.json())

        return response_409
    if response.status_code == 413:
        response_413 = Errors.from_dict(response.json())

        return response_413
    if response.status_code == 415:
        response_415 = Errors.from_dict(response.json())

        return response_415
    if response.status_code == 500:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = Errors.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, LinkedoslcresourcesListPostResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LinkedoslcresourcesListPostRequest,
) -> Response[Union[Errors, LinkedoslcresourcesListPostResponse]]:
    """Creates a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        body (LinkedoslcresourcesListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, LinkedoslcresourcesListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LinkedoslcresourcesListPostRequest,
) -> Union[Errors, LinkedoslcresourcesListPostResponse] | None:
    """Creates a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        body (LinkedoslcresourcesListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, LinkedoslcresourcesListPostResponse]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LinkedoslcresourcesListPostRequest,
) -> Response[Union[Errors, LinkedoslcresourcesListPostResponse]]:
    """Creates a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        body (LinkedoslcresourcesListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, LinkedoslcresourcesListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LinkedoslcresourcesListPostRequest,
) -> Union[Errors, LinkedoslcresourcesListPostResponse] | None:
    """Creates a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        body (LinkedoslcresourcesListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, LinkedoslcresourcesListPostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
