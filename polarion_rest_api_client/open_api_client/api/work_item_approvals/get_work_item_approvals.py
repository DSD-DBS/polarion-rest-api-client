# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.sparse_fields import SparseFields
from ...models.workitem_approvals_list_get_response import (
    WorkitemApprovalsListGetResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    json_fields: Union[Unset, dict[str, Any]] = UNSET
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
        "url": f"/projects/{project_id}/workitems/{work_item_id}/approvals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Errors, WorkitemApprovalsListGetResponse] | None:
    if response.status_code == 200:
        response_200 = WorkitemApprovalsListGetResponse.from_dict(
            response.json()
        )

        return response_200
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
) -> Response[Union[Errors, WorkitemApprovalsListGetResponse]]:
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
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, WorkitemApprovalsListGetResponse]]:
    """Returns a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, WorkitemApprovalsListGetResponse]]
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
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Union[Errors, WorkitemApprovalsListGetResponse] | None:
    """Returns a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, WorkitemApprovalsListGetResponse]
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
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, WorkitemApprovalsListGetResponse]]:
    """Returns a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, WorkitemApprovalsListGetResponse]]
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
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Union[Errors, WorkitemApprovalsListGetResponse] | None:
    """Returns a list of instances.

    Args:
        project_id (str):
        work_item_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, WorkitemApprovalsListGetResponse]
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
