# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_work_item_attachments_request_body import (
    PostWorkItemAttachmentsRequestBody,
)
from ...models.workitem_attachments_list_post_response import (
    WorkitemAttachmentsListPostResponse,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    *,
    multipart_data: PostWorkItemAttachmentsRequestBody,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/projects/{projectId}/workitems/{workItemId}/attachments".format(
            projectId=project_id,
            workItemId=work_item_id,
        ),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WorkitemAttachmentsListPostResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = WorkitemAttachmentsListPostResponse.from_dict(
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
) -> Response[Union[Any, WorkitemAttachmentsListPostResponse]]:
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
    multipart_data: PostWorkItemAttachmentsRequestBody,
) -> Response[Union[Any, WorkitemAttachmentsListPostResponse]]:
    r"""Creates a list of instances.

     Files are identified by order or optionally by the 'lid' attribute. See more in the <a
    href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    multipart_data : PostWorkItemAttachmentsRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, WorkitemAttachmentsListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        multipart_data=multipart_data,
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
    multipart_data: PostWorkItemAttachmentsRequestBody,
) -> Optional[Union[Any, WorkitemAttachmentsListPostResponse]]:
    r"""Creates a list of instances.

     Files are identified by order or optionally by the 'lid' attribute. See more in the <a
    href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    multipart_data : PostWorkItemAttachmentsRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, WorkitemAttachmentsListPostResponse]
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PostWorkItemAttachmentsRequestBody,
) -> Response[Union[Any, WorkitemAttachmentsListPostResponse]]:
    r"""Creates a list of instances.

     Files are identified by order or optionally by the 'lid' attribute. See more in the <a
    href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    multipart_data : PostWorkItemAttachmentsRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Response[Union[Any, WorkitemAttachmentsListPostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: PostWorkItemAttachmentsRequestBody,
) -> Optional[Union[Any, WorkitemAttachmentsListPostResponse]]:
    r"""Creates a list of instances.

     Files are identified by order or optionally by the 'lid' attribute. See more in the <a
    href=\"https://docs.sw.siemens.com/en-
    US/doc/230235217/PL20221020258116340.xid2134849/xid2134871\">Rest API User Guide</a>.

    Parameters
    ----------
    project_id : str
    work_item_id : str
    multipart_data : PostWorkItemAttachmentsRequestBody

    Raises
    ------
    errors.UnexpectedStatus:
        If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
    httpx.TimeoutException:
        If the request takes longer than Client.timeout.

    Returns
    -------
    Union[Any, WorkitemAttachmentsListPostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
