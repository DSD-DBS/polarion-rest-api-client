# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enum_options_action_response_body import (
    EnumOptionsActionResponseBody,
)
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    field_id: str,
    *,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{projectId}/workitems/{workItemId}/fields/{fieldId}/actions/getAvailableOptions".format(
            projectId=project_id,
            workItemId=work_item_id,
            fieldId=field_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EnumOptionsActionResponseBody, Errors]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EnumOptionsActionResponseBody.from_dict(response.json())

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
) -> Response[Union[EnumOptionsActionResponseBody, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    work_item_id: str,
    field_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
) -> Response[Union[EnumOptionsActionResponseBody, Errors]]:
    """Returns a list of available options for the requested field for the
    specified Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        field_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnumOptionsActionResponseBody, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        field_id=field_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    work_item_id: str,
    field_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
) -> Optional[Union[EnumOptionsActionResponseBody, Errors]]:
    """Returns a list of available options for the requested field for the
    specified Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        field_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnumOptionsActionResponseBody, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        field_id=field_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    field_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
) -> Response[Union[EnumOptionsActionResponseBody, Errors]]:
    """Returns a list of available options for the requested field for the
    specified Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        field_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnumOptionsActionResponseBody, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        field_id=field_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    field_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
) -> Optional[Union[EnumOptionsActionResponseBody, Errors]]:
    """Returns a list of available options for the requested field for the
    specified Work Item.

    Args:
        project_id (str):
        work_item_id (str):
        field_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnumOptionsActionResponseBody, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            field_id=field_id,
            client=client,
            pagesize=pagesize,
            pagenumber=pagenumber,
        )
    ).parsed
