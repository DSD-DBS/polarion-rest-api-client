# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.plans_list_get_response import PlansListGetResponse
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_fields: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    params["query"] = query

    params["sort"] = sort

    params["templates"] = templates

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{projectId}/plans".format(
            projectId=project_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PlansListGetResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlansListGetResponse.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PlansListGetResponse]]:
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
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, PlansListGetResponse]]:
    """Returns a list of Plans.

    Args:
        project_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlansListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        fields=fields,
        include=include,
        pagesize=pagesize,
        pagenumber=pagenumber,
        query=query,
        sort=sort,
        templates=templates,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, PlansListGetResponse]]:
    """Returns a list of Plans.

    Args:
        project_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlansListGetResponse]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        fields=fields,
        include=include,
        pagesize=pagesize,
        pagenumber=pagenumber,
        query=query,
        sort=sort,
        templates=templates,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, PlansListGetResponse]]:
    """Returns a list of Plans.

    Args:
        project_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlansListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        fields=fields,
        include=include,
        pagesize=pagesize,
        pagenumber=pagenumber,
        query=query,
        sort=sort,
        templates=templates,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, PlansListGetResponse]]:
    """Returns a list of Plans.

    Args:
        project_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlansListGetResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            fields=fields,
            include=include,
            pagesize=pagesize,
            pagenumber=pagenumber,
            query=query,
            sort=sort,
            templates=templates,
        )
    ).parsed