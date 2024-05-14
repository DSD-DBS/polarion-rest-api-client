# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.jobs_single_post_response import JobsSinglePostResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    test_run_id: str,
    *,
    query: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    template: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["sortBy"] = sort_by

    params["template"] = template

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{projectId}/testruns/{testRunId}/actions/exportTestsToExcel".format(
            projectId=project_id,
            testRunId=test_run_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, JobsSinglePostResponse]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = JobsSinglePostResponse.from_dict(response.json())

        return response_202
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
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = Errors.from_dict(response.json())

        return response_406
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
) -> Response[Union[Errors, JobsSinglePostResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    test_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    template: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, JobsSinglePostResponse]]:
    """Exports tests to Excel.

    Args:
        project_id (str):
        test_run_id (str):
        query (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        template (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, JobsSinglePostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_run_id=test_run_id,
        query=query,
        sort_by=sort_by,
        template=template,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    test_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    template: Union[Unset, str] = UNSET,
) -> Optional[Union[Errors, JobsSinglePostResponse]]:
    """Exports tests to Excel.

    Args:
        project_id (str):
        test_run_id (str):
        query (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        template (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, JobsSinglePostResponse]
    """

    return sync_detailed(
        project_id=project_id,
        test_run_id=test_run_id,
        client=client,
        query=query,
        sort_by=sort_by,
        template=template,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    test_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    template: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, JobsSinglePostResponse]]:
    """Exports tests to Excel.

    Args:
        project_id (str):
        test_run_id (str):
        query (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        template (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, JobsSinglePostResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_run_id=test_run_id,
        query=query,
        sort_by=sort_by,
        template=template,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    test_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    template: Union[Unset, str] = UNSET,
) -> Optional[Union[Errors, JobsSinglePostResponse]]:
    """Exports tests to Excel.

    Args:
        project_id (str):
        test_run_id (str):
        query (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        template (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, JobsSinglePostResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            test_run_id=test_run_id,
            client=client,
            query=query,
            sort_by=sort_by,
            template=template,
        )
    ).parsed
