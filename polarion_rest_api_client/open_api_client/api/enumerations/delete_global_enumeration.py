# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    enum_context: str,
    enum_name: str,
    target_type: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/enumerations/{enum_context}/{enum_name}/{target_type}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Errors] | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
    if response.status_code == 409:
        response_409 = Errors.from_dict(response.json())

        return response_409
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
) -> Response[Union[Any, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Errors]]:
    """Deletes the specified Enumeration from the Global context.

    Args:
        enum_context (str):
        enum_name (str):
        target_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Union[Any, Errors] | None:
    """Deletes the specified Enumeration from the Global context.

    Args:
        enum_context (str):
        enum_name (str):
        target_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return sync_detailed(
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Errors]]:
    """Deletes the specified Enumeration from the Global context.

    Args:
        enum_context (str):
        enum_name (str):
        target_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Union[Any, Errors] | None:
    """Deletes the specified Enumeration from the Global context.

    Args:
        enum_context (str):
        enum_name (str):
        target_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return (
        await asyncio_detailed(
            enum_context=enum_context,
            enum_name=enum_name,
            target_type=target_type,
            client=client,
        )
    ).parsed
