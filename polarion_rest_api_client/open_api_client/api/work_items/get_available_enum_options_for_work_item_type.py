# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

import os
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.enum_options_action_response_body import (
    EnumOptionsActionResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    field_id: str,
    *,
    client: Client,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/workitems/fields/{fieldId}/actions/getAvailableOptions".format(
        client.base_url, projectId=project_id, fieldId=field_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    params["type"] = type

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, EnumOptionsActionResponseBody]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EnumOptionsActionResponseBody.from_dict(response.json())

        return response_200
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
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, EnumOptionsActionResponseBody]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    field_id: str,
    *,
    client: Client,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, EnumOptionsActionResponseBody]]:
    """Returns a list of instances.

    Args:
        project_id (str):
        field_id (str):
        pagesize (Union[Unset, None, int]):
        pagenumber (Union[Unset, None, int]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EnumOptionsActionResponseBody]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        field_id=field_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        type=type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        proxies=os.getenv("PROXIES"),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    field_id: str,
    *,
    client: Client,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, EnumOptionsActionResponseBody]]:
    """Returns a list of instances.

    Args:
        project_id (str):
        field_id (str):
        pagesize (Union[Unset, None, int]):
        pagenumber (Union[Unset, None, int]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EnumOptionsActionResponseBody]
    """

    return sync_detailed(
        project_id=project_id,
        field_id=field_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        type=type,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    field_id: str,
    *,
    client: Client,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, EnumOptionsActionResponseBody]]:
    """Returns a list of instances.

    Args:
        project_id (str):
        field_id (str):
        pagesize (Union[Unset, None, int]):
        pagenumber (Union[Unset, None, int]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EnumOptionsActionResponseBody]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        field_id=field_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        type=type,
    )

    async with httpx.AsyncClient(
        verify=client.verify_ssl, proxies=os.getenv("PROXIES")
    ) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    field_id: str,
    *,
    client: Client,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, EnumOptionsActionResponseBody]]:
    """Returns a list of instances.

    Args:
        project_id (str):
        field_id (str):
        pagesize (Union[Unset, None, int]):
        pagenumber (Union[Unset, None, int]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EnumOptionsActionResponseBody]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            field_id=field_id,
            client=client,
            pagesize=pagesize,
            pagenumber=pagenumber,
            type=type,
        )
    ).parsed
