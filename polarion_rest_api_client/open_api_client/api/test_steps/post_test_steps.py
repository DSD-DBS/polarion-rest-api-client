# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.teststeps_list_post_request import TeststepsListPostRequest
from ...models.teststeps_list_post_response import TeststepsListPostResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    body: TeststepsListPostRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/workitems/{work_item_id}/teststeps".format(
            project_id=project_id,
            work_item_id=work_item_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, TeststepsListPostResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = TeststepsListPostResponse.from_dict(response.json())

        return response_201
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
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = Errors.from_dict(response.json())

        return response_406
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Errors.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = Errors.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = Errors.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Errors.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, TeststepsListPostResponse]]:
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
    body: TeststepsListPostRequest,
) -> Response[Union[Errors, TeststepsListPostResponse]]:
    """Creates a list of Test Steps.

    Args:
        project_id (str):
        work_item_id (str):
        body (TeststepsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, TeststepsListPostResponse]]
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
    body: TeststepsListPostRequest,
) -> Optional[Union[Errors, TeststepsListPostResponse]]:
    """Creates a list of Test Steps.

    Args:
        project_id (str):
        work_item_id (str):
        body (TeststepsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, TeststepsListPostResponse]
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
    body: TeststepsListPostRequest,
) -> Response[Union[Errors, TeststepsListPostResponse]]:
    """Creates a list of Test Steps.

    Args:
        project_id (str):
        work_item_id (str):
        body (TeststepsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, TeststepsListPostResponse]]
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
    body: TeststepsListPostRequest,
) -> Optional[Union[Errors, TeststepsListPostResponse]]:
    """Creates a list of Test Steps.

    Args:
        project_id (str):
        work_item_id (str):
        body (TeststepsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, TeststepsListPostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
