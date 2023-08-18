# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_work_item_attachments_request_body import (
    PatchWorkItemAttachmentsRequestBody,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    attachment_id: str,
    *,
    multipart_data: PatchWorkItemAttachmentsRequestBody,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": "/projects/{projectId}/workitems/{workItemId}/attachments/{attachmentId}".format(
            projectId=project_id,
            workItemId=work_item_id,
            attachmentId=attachment_id,
        ),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    work_item_id: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PatchWorkItemAttachmentsRequestBody,
) -> Response[Any]:
    r"""Updates the specified instance.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    attachment_id : str
    multipart_data : PatchWorkItemAttachmentsRequestBody

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
        work_item_id=work_item_id,
        attachment_id=attachment_id,
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PatchWorkItemAttachmentsRequestBody,
) -> Response[Any]:
    r"""Updates the specified instance.

     See more in the <a href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    attachment_id : str
    multipart_data : PatchWorkItemAttachmentsRequestBody

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
        work_item_id=work_item_id,
        attachment_id=attachment_id,
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
