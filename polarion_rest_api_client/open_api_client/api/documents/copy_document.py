# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.copy_document_request_body import CopyDocumentRequestBody
from ...models.documents_single_post_response import (
    DocumentsSinglePostResponse,
)
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    body: CopyDocumentRequestBody,
    revision: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/spaces/{space_id}/documents/{document_name}/actions/copy",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[DocumentsSinglePostResponse, Errors] | None:
    if response.status_code == 201:
        response_201 = DocumentsSinglePostResponse.from_dict(response.json())

        return response_201
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
    if response.status_code == 409:
        response_409 = Errors.from_dict(response.json())

        return response_409
    if response.status_code == 413:
        response_413 = Errors.from_dict(response.json())

        return response_413
    if response.status_code == 415:
        response_415 = Errors.from_dict(response.json())

        return response_415
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
) -> Response[Union[DocumentsSinglePostResponse, Errors]]:
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
    body: CopyDocumentRequestBody,
    revision: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentsSinglePostResponse, Errors]]:
    """Creates a copy of the Document.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        revision (Union[Unset, str]):
        body (CopyDocumentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentsSinglePostResponse, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        body=body,
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
    body: CopyDocumentRequestBody,
    revision: Union[Unset, str] = UNSET,
) -> Union[DocumentsSinglePostResponse, Errors] | None:
    """Creates a copy of the Document.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        revision (Union[Unset, str]):
        body (CopyDocumentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentsSinglePostResponse, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        client=client,
        body=body,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CopyDocumentRequestBody,
    revision: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentsSinglePostResponse, Errors]]:
    """Creates a copy of the Document.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        revision (Union[Unset, str]):
        body (CopyDocumentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentsSinglePostResponse, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        body=body,
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
    body: CopyDocumentRequestBody,
    revision: Union[Unset, str] = UNSET,
) -> Union[DocumentsSinglePostResponse, Errors] | None:
    """Creates a copy of the Document.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        revision (Union[Unset, str]):
        body (CopyDocumentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentsSinglePostResponse, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            space_id=space_id,
            document_name=document_name,
            client=client,
            body=body,
            revision=revision,
        )
    ).parsed
