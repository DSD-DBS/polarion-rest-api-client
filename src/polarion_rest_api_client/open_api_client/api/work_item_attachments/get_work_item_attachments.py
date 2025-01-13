# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.sparse_fields import SparseFields
from ...models.workitem_attachments_list_get_response import (
    WorkitemAttachmentsListGetResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    pagesize: Unset | int = UNSET,
    pagenumber: Unset | int = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Unset | str = UNSET,
    revision: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    json_fields: Unset | dict[str, Any] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/workitems/{work_item_id}/attachments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | WorkitemAttachmentsListGetResponse | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkitemAttachmentsListGetResponse.from_dict(
            response.json()
        )

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
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Errors | WorkitemAttachmentsListGetResponse]:
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
    client: AuthenticatedClient | Client,
    pagesize: Unset | int = UNSET,
    pagenumber: Unset | int = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Unset | str = UNSET,
    revision: Unset | str = UNSET,
) -> Response[Errors | WorkitemAttachmentsListGetResponse]:
    """Returns a list of  Work Item Attachments.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Response[Union[Errors, WorkitemAttachmentsListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: Unset | int = UNSET,
    pagenumber: Unset | int = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Unset | str = UNSET,
    revision: Unset | str = UNSET,
) -> Errors | WorkitemAttachmentsListGetResponse | None:
    """Returns a list of  Work Item Attachments.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Union[Errors, WorkitemAttachmentsListGetResponse]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: Unset | int = UNSET,
    pagenumber: Unset | int = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Unset | str = UNSET,
    revision: Unset | str = UNSET,
) -> Response[Errors | WorkitemAttachmentsListGetResponse]:
    """Returns a list of  Work Item Attachments.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Response[Union[Errors, WorkitemAttachmentsListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: Unset | int = UNSET,
    pagenumber: Unset | int = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Unset | str = UNSET,
    revision: Unset | str = UNSET,
) -> Errors | WorkitemAttachmentsListGetResponse | None:
    """Returns a list of  Work Item Attachments.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises
    ------
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns
    -------
        Union[Errors, WorkitemAttachmentsListGetResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            client=client,
            pagesize=pagesize,
            pagenumber=pagenumber,
            fields=fields,
            include=include,
            revision=revision,
        )
    ).parsed
