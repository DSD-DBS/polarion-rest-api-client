# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
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
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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
        "url": f"/projects/{project_id}/workitems/{work_item_id}/linkedworkitems/{role_id}/{target_project_id}/{linked_work_item_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Errors, LinkedworkitemsSingleGetResponse] | None:
    if response.status_code == 200:
        response_200 = LinkedworkitemsSingleGetResponse.from_dict(
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
) -> Response[Union[Errors, LinkedworkitemsSingleGetResponse]]:
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
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, LinkedworkitemsSingleGetResponse]]:
    """Returns the specified Linked Work Item.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, LinkedworkitemsSingleGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
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
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Union[Errors, LinkedworkitemsSingleGetResponse] | None:
    """Returns the specified Linked Work Item.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, LinkedworkitemsSingleGetResponse]
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
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, LinkedworkitemsSingleGetResponse]]:
    """Returns the specified Linked Work Item.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, LinkedworkitemsSingleGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        role_id=role_id,
        target_project_id=target_project_id,
        linked_work_item_id=linked_work_item_id,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    role_id: str,
    target_project_id: str,
    linked_work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Union[Errors, LinkedworkitemsSingleGetResponse] | None:
    """Returns the specified Linked Work Item.

     Returns the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Args:
        project_id (str):
        work_item_id (str):
        role_id (str):
        target_project_id (str):
        linked_work_item_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, LinkedworkitemsSingleGetResponse]
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
