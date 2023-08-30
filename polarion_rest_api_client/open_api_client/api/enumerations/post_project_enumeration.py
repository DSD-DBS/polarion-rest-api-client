# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enumerations_list_post_request import (
    EnumerationsListPostRequest,
)
from ...models.enumerations_list_post_response import (
    EnumerationsListPostResponse,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    json_body: EnumerationsListPostRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectId}/enumerations".format(
            projectId=project_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EnumerationsListPostResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = EnumerationsListPostResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EnumerationsListPostResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EnumerationsListPostRequest,
) -> Response[Union[Any, EnumerationsListPostResponse]]:
    """Creates a list of instances.

    Parameters
    ----------
    project_id : str
    json_body : EnumerationsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, EnumerationsListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EnumerationsListPostRequest,
) -> Optional[Union[Any, EnumerationsListPostResponse]]:
    """Creates a list of instances.

    Parameters
    ----------
    project_id : str
    json_body : EnumerationsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, EnumerationsListPostResponse]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EnumerationsListPostRequest,
) -> Response[Union[Any, EnumerationsListPostResponse]]:
    """Creates a list of instances.

    Parameters
    ----------
    project_id : str
    json_body : EnumerationsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, EnumerationsListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EnumerationsListPostRequest,
) -> Optional[Union[Any, EnumerationsListPostResponse]]:
    """Creates a list of instances.

    Parameters
    ----------
    project_id : str
    json_body : EnumerationsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, EnumerationsListPostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
