# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.relationship_data_list_response import (
    RelationshipDataListResponse,
)
from ...models.relationship_data_single_response import (
    RelationshipDataSingleResponse,
)
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    relationship_id: str,
    *,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    revision: Union[Unset, str] = UNSET,
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

    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{projectId}/workitems/{workItemId}/relationships/{relationshipId}".format(
            projectId=project_id,
            workItemId=work_item_id,
            relationshipId=relationship_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_response_body_type_0 = (
                    RelationshipDataSingleResponse.from_dict(data)
                )

                return componentsschemas_relationship_response_body_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_relationship_response_body_type_1 = (
                RelationshipDataListResponse.from_dict(data)
            )

            return componentsschemas_relationship_response_body_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    Union[
        Any,
        Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    work_item_id: str,
    relationship_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ],
    ]
]:
    """Returns a list of Work Item Relationships.

    Args:
        project_id (str):
        work_item_id (str):
        relationship_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['RelationshipDataListResponse', 'RelationshipDataSingleResponse']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        relationship_id=relationship_id,
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
    relationship_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ],
    ]
]:
    """Returns a list of Work Item Relationships.

    Args:
        project_id (str):
        work_item_id (str):
        relationship_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['RelationshipDataListResponse', 'RelationshipDataSingleResponse']]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        relationship_id=relationship_id,
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
    relationship_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ],
    ]
]:
    """Returns a list of Work Item Relationships.

    Args:
        project_id (str):
        work_item_id (str):
        relationship_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['RelationshipDataListResponse', 'RelationshipDataSingleResponse']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        relationship_id=relationship_id,
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
    relationship_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    revision: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        Union[
            "RelationshipDataListResponse", "RelationshipDataSingleResponse"
        ],
    ]
]:
    """Returns a list of Work Item Relationships.

    Args:
        project_id (str):
        work_item_id (str):
        relationship_id (str):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        revision (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['RelationshipDataListResponse', 'RelationshipDataSingleResponse']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            relationship_id=relationship_id,
            client=client,
            fields=fields,
            include=include,
            pagesize=pagesize,
            pagenumber=pagenumber,
            revision=revision,
        )
    ).parsed