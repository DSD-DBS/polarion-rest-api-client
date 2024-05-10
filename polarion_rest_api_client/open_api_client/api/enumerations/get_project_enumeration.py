# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enumerations_single_get_response import (
    EnumerationsSingleGetResponse,
)
from ...models.errors import Errors
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_fields: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{projectId}/enumerations/{enumContext}/{enumName}/{targetType}".format(
            projectId=project_id,
            enumContext=enum_context,
            enumName=enum_name,
            targetType=target_type,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EnumerationsSingleGetResponse, Errors]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EnumerationsSingleGetResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[EnumerationsSingleGetResponse, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[EnumerationsSingleGetResponse, Errors]]:
    """Returns the specified Enumeration from the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnumerationsSingleGetResponse, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        fields=fields,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[EnumerationsSingleGetResponse, Errors]]:
    """Returns the specified Enumeration from the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnumerationsSingleGetResponse, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        client=client,
        fields=fields,
        include=include,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[EnumerationsSingleGetResponse, Errors]]:
    """Returns the specified Enumeration from the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnumerationsSingleGetResponse, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        fields=fields,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[EnumerationsSingleGetResponse, Errors]]:
    """Returns the specified Enumeration from the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnumerationsSingleGetResponse, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            enum_context=enum_context,
            enum_name=enum_name,
            target_type=target_type,
            client=client,
            fields=fields,
            include=include,
        )
    ).parsed
