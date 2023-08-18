# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sparse_fields import SparseFields
from ...models.workitem_attachments_list_get_response import (
    WorkitemAttachmentsListGetResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_fields: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict() if fields else None

    if not isinstance(json_fields, Unset) and json_fields is not None:
        params.update(json_fields)

    params["include"] = include

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    return {
        "method": "get",
        "url": "/projects/{projectId}/workitems/{workItemId}/attachments".format(
            projectId=project_id,
            workItemId=work_item_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WorkitemAttachmentsListGetResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkitemAttachmentsListGetResponse.from_dict(
            response.json()
        )

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
) -> Response[Union[Any, WorkitemAttachmentsListGetResponse]]:
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
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, WorkitemAttachmentsListGetResponse]]:
    """Returns a list of instances.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    pagesize : Union[Unset, None, int]
    pagenumber : Union[Unset, None, int]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, WorkitemAttachmentsListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        fields=fields,
        include=include,
        pagesize=pagesize,
        pagenumber=pagenumber,
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
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, WorkitemAttachmentsListGetResponse]]:
    """Returns a list of instances.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    pagesize : Union[Unset, None, int]
    pagenumber : Union[Unset, None, int]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, WorkitemAttachmentsListGetResponse]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        client=client,
        fields=fields,
        include=include,
        pagesize=pagesize,
        pagenumber=pagenumber,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, WorkitemAttachmentsListGetResponse]]:
    """Returns a list of instances.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    pagesize : Union[Unset, None, int]
    pagenumber : Union[Unset, None, int]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, WorkitemAttachmentsListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        fields=fields,
        include=include,
        pagesize=pagesize,
        pagenumber=pagenumber,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
    pagenumber: Union[Unset, None, int] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, WorkitemAttachmentsListGetResponse]]:
    """Returns a list of instances.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    pagesize : Union[Unset, None, int]
    pagenumber : Union[Unset, None, int]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, WorkitemAttachmentsListGetResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            client=client,
            fields=fields,
            include=include,
            pagesize=pagesize,
            pagenumber=pagenumber,
            revision=revision,
        )
    ).parsed
