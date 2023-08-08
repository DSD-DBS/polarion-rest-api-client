# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    revision: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    return {
        "method": "get",
        "url": "/projects/{projectId}/spaces/{spaceId}/documents/{documentName}/attachments/{attachmentId}/content".format(
            projectId=project_id,
            spaceId=space_id,
            documentName=document_name,
            attachmentId=attachment_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Downloads the file content for a specified attachment.

    Parameters
    ----------
    project_id : str
    space_id : str
    document_name : str
    attachment_id : str
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Downloads the file content for a specified attachment.

    Parameters
    ----------
    project_id : str
    space_id : str
    document_name : str
    attachment_id : str
    revision : Union[Unset, None, str]

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
