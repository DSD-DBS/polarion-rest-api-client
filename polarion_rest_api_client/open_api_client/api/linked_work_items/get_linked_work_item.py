# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

import os
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.linkedworkitems_single_get_response import (
    LinkedworkitemsSingleGetResponse,
)
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/workitems/{workItemId}/linkedworkitems/{roleId}/{targetProjectId}/{linkedWorkItemId}".format(
        client.base_url,
        projectId=project_id,
        workItemId=work_item_id,
        roleId=role_id,
        targetProjectId=target_project_id,
        linkedWorkItemId=linked_work_item_id,
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_fields: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict() if fields else None

    if not isinstance(json_fields, Unset) and json_fields is not None:
        params.update(json_fields)

    params["include"] = include

    params["revision"] = revision

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
) -> Optional[Union[Any, LinkedworkitemsSingleGetResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LinkedworkitemsSingleGetResponse.from_dict(
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
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, LinkedworkitemsSingleGetResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, LinkedworkitemsSingleGetResponse]]:
    """Returns the specified instance.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, None, SparseFields]):
        include (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LinkedworkitemsSingleGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        client=client,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        proxies=os.getenv("PROXIES"),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, LinkedworkitemsSingleGetResponse]]:
    """Returns the specified instance.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, None, SparseFields]):
        include (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LinkedworkitemsSingleGetResponse]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        client=client,
        fields=fields,
        include=include,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, LinkedworkitemsSingleGetResponse]]:
    """Returns the specified instance.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, None, SparseFields]):
        include (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LinkedworkitemsSingleGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        client=client,
        fields=fields,
        include=include,
        revision=revision,
    )

    async with httpx.AsyncClient(
        verify=client.verify_ssl, proxies=os.getenv("PROXIES")
    ) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Client,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, LinkedworkitemsSingleGetResponse]]:
    """Returns the specified instance.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, None, SparseFields]):
        include (Union[Unset, None, str]):
        revision (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LinkedworkitemsSingleGetResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            role_id=role_id,
            target_project_id=target_project_id,
            linked_work_item_id=linked_work_item_id,
            client=client,
            fields=fields,
            include=include,
            revision=revision,
        )
    ).parsed
