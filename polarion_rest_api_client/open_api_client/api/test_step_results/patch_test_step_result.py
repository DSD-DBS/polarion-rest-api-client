# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.teststep_results_single_patch_request import (
    TeststepResultsSinglePatchRequest,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    test_step_index: str,
    *,
    body: TeststepResultsSinglePatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/projects/{project_id}/testruns/{test_run_id}/testrecords/{test_case_project_id}/{test_case_id}/{iteration}/teststepresults/{test_step_index}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Errors] | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    test_step_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TeststepResultsSinglePatchRequest,
) -> Response[Union[Any, Errors]]:
    """Updates the specified Test Step Result.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):
        test_step_index (str):
        body (TeststepResultsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_run_id=test_run_id,
        test_case_project_id=test_case_project_id,
        test_case_id=test_case_id,
        iteration=iteration,
        test_step_index=test_step_index,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    test_step_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TeststepResultsSinglePatchRequest,
) -> Union[Any, Errors] | None:
    """Updates the specified Test Step Result.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):
        test_step_index (str):
        body (TeststepResultsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        test_run_id=test_run_id,
        test_case_project_id=test_case_project_id,
        test_case_id=test_case_id,
        iteration=iteration,
        test_step_index=test_step_index,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    test_step_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TeststepResultsSinglePatchRequest,
) -> Response[Union[Any, Errors]]:
    """Updates the specified Test Step Result.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):
        test_step_index (str):
        body (TeststepResultsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_run_id=test_run_id,
        test_case_project_id=test_case_project_id,
        test_case_id=test_case_id,
        iteration=iteration,
        test_step_index=test_step_index,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    test_step_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TeststepResultsSinglePatchRequest,
) -> Union[Any, Errors] | None:
    """Updates the specified Test Step Result.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):
        test_step_index (str):
        body (TeststepResultsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            test_run_id=test_run_id,
            test_case_project_id=test_case_project_id,
            test_case_id=test_case_id,
            iteration=iteration,
            test_step_index=test_step_index,
            client=client,
            body=body,
        )
    ).parsed
