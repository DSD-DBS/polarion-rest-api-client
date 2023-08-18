# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.linkedworkitems_list_post_request import (
    LinkedworkitemsListPostRequest,
)
from ...models.linkedworkitems_list_post_response import (
    LinkedworkitemsListPostResponse,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    json_body: LinkedworkitemsListPostRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectId}/workitems/{workItemId}/linkedworkitems".format(
            projectId=project_id,
            workItemId=work_item_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LinkedworkitemsListPostResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = LinkedworkitemsListPostResponse.from_dict(
            response.json()
        )

        return response_201
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
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
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
) -> Response[Union[Any, LinkedworkitemsListPostResponse]]:
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
    json_body: LinkedworkitemsListPostRequest,
) -> Response[Union[Any, LinkedworkitemsListPostResponse]]:
    """Creates a list of instances.

     Creates the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    json_body : LinkedworkitemsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, LinkedworkitemsListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        json_body=json_body,
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
    json_body: LinkedworkitemsListPostRequest,
) -> Optional[Union[Any, LinkedworkitemsListPostResponse]]:
    """Creates a list of instances.

     Creates the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    json_body : LinkedworkitemsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, LinkedworkitemsListPostResponse]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LinkedworkitemsListPostRequest,
) -> Response[Union[Any, LinkedworkitemsListPostResponse]]:
    """Creates a list of instances.

     Creates the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    json_body : LinkedworkitemsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, LinkedworkitemsListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LinkedworkitemsListPostRequest,
) -> Optional[Union[Any, LinkedworkitemsListPostResponse]]:
    """Creates a list of instances.

     Creates the direct outgoing links to other Work Items. (The same as the corresponding Java API
    method.)  Does not pertain to external links or backlinks.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    json_body : LinkedworkitemsListPostRequest

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, LinkedworkitemsListPostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
