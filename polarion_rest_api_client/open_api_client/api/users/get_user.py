# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sparse_fields import SparseFields
from ...models.users_single_get_response import UsersSingleGetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
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

    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    return {
        "method": "get",
        "url": "/users/{userId}".format(
            userId=user_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UsersSingleGetResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersSingleGetResponse.from_dict(response.json())

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
) -> Response[Union[Any, UsersSingleGetResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, UsersSingleGetResponse]]:
    """Returns the specified instance.

    Parameters
    ----------
    user_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, UsersSingleGetResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, UsersSingleGetResponse]]:
    """Returns the specified instance.

    Parameters
    ----------
    user_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, UsersSingleGetResponse]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        fields=fields,
        include=include,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, UsersSingleGetResponse]]:
    """Returns the specified instance.

    Parameters
    ----------
    user_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, UsersSingleGetResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, "SparseFields"] = UNSET,
    include: Union[Unset, None, str] = UNSET,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, UsersSingleGetResponse]]:
    """Returns the specified instance.

    Parameters
    ----------
    user_id : str
    fields : Union[Unset, None, SparseFields]
    include : Union[Unset, None, str]
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, UsersSingleGetResponse]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            fields=fields,
            include=include,
            revision=revision,
        )
    ).parsed
