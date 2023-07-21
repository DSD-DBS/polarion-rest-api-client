# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

import os
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
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
    client: Client,
    multipart_data: PatchDocumentAttachmentsRequestBody,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/spaces/{spaceId}/documents/{documentName}/attachments/{attachmentId}".format(
        client.base_url,
        projectId=project_id,
        spaceId=space_id,
        documentName=document_name,
        attachmentId=attachment_id,
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
        return None
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        return None
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
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
    *, client: Client, response: httpx.Response
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
    client: Client,
    multipart_data: PatchDocumentAttachmentsRequestBody,
) -> Response[Any]:
    r"""Updates the specified instance.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        attachment_id (str):
        multipart_data (PatchDocumentAttachmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        proxies=os.getenv("PROXIES"),
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    attachment_id: str,
    *,
    client: Client,
    multipart_data: PatchDocumentAttachmentsRequestBody,
) -> Response[Any]:
    r"""Updates the specified instance.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        attachment_id (str):
        multipart_data (PatchDocumentAttachmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        attachment_id=attachment_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(
        verify=client.verify_ssl, proxies=os.getenv("PROXIES")
    ) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
