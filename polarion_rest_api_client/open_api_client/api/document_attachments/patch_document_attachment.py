# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.patch_document_attachments_request_body import (
    PatchDocumentAttachmentsRequestBody,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    body: PatchDocumentAttachmentsRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/projects/{projectId}/spaces/{spaceId}/documents/{documentName}/attachments/{attachmentId}".format(
            projectId=project_id,
            spaceId=space_id,
            documentName=document_name,
            attachmentId=attachment_id,
        ),
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Errors]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Errors.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = Errors.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = Errors.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Errors.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Errors]]:
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
    body: PatchDocumentAttachmentsRequestBody,
) -> Response[Union[Any, Errors]]:
    r"""Updates the specified Document Attachment.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20231017526942799.polarion_help_sc.xid2134849/xid2134871\" target=\"_blank\">REST
    API User Guide</a>.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        attachment_id (str):
        body (PatchDocumentAttachmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchDocumentAttachmentsRequestBody,
) -> Optional[Union[Any, Errors]]:
    r"""Updates the specified Document Attachment.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20231017526942799.polarion_help_sc.xid2134849/xid2134871\" target=\"_blank\">REST
    API User Guide</a>.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        attachment_id (str):
        body (PatchDocumentAttachmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchDocumentAttachmentsRequestBody,
) -> Response[Union[Any, Errors]]:
    r"""Updates the specified Document Attachment.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20231017526942799.polarion_help_sc.xid2134849/xid2134871\" target=\"_blank\">REST
    API User Guide</a>.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        attachment_id (str):
        body (PatchDocumentAttachmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchDocumentAttachmentsRequestBody,
) -> Optional[Union[Any, Errors]]:
    r"""Updates the specified Document Attachment.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20231017526942799.polarion_help_sc.xid2134849/xid2134871\" target=\"_blank\">REST
    API User Guide</a>.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        attachment_id (str):
        body (PatchDocumentAttachmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            space_id=space_id,
            document_name=document_name,
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
