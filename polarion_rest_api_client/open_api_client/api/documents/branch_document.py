# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branch_document_request_body import BranchDocumentRequestBody
from ...models.documents_single_post_response import (
    DocumentsSinglePostResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    json_body: BranchDocumentRequestBody,
    revision: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectId}/spaces/{spaceId}/documents/{documentName}/actions/branch".format(
            projectId=project_id,
            spaceId=space_id,
            documentName=document_name,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DocumentsSinglePostResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DocumentsSinglePostResponse.from_dict(response.json())

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
) -> Response[Union[Any, DocumentsSinglePostResponse]]:
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
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BranchDocumentRequestBody,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, DocumentsSinglePostResponse]]:
    """Creates a branch of the document.

    Parameters
    ----------
    project_id : str
    space_id : str
    document_name : str
    revision : Union[Unset, None, str]
    json_body : BranchDocumentRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, DocumentsSinglePostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        json_body=json_body,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BranchDocumentRequestBody,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, DocumentsSinglePostResponse]]:
    """Creates a branch of the document.

    Parameters
    ----------
    project_id : str
    space_id : str
    document_name : str
    revision : Union[Unset, None, str]
    json_body : BranchDocumentRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, DocumentsSinglePostResponse]
    """

    return sync_detailed(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        client=client,
        json_body=json_body,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BranchDocumentRequestBody,
    revision: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, DocumentsSinglePostResponse]]:
    """Creates a branch of the document.

    Parameters
    ----------
    project_id : str
    space_id : str
    document_name : str
    revision : Union[Unset, None, str]
    json_body : BranchDocumentRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, DocumentsSinglePostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        json_body=json_body,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BranchDocumentRequestBody,
    revision: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, DocumentsSinglePostResponse]]:
    """Creates a branch of the document.

    Parameters
    ----------
    project_id : str
    space_id : str
    document_name : str
    revision : Union[Unset, None, str]
    json_body : BranchDocumentRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, DocumentsSinglePostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            space_id=space_id,
            document_name=document_name,
            client=client,
            json_body=json_body,
            revision=revision,
        )
    ).parsed
