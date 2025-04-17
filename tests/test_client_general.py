# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import ssl
from unittest import mock

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import TEST_PROJECT_RESPONSE_JSON


@mock.patch("httpx.Client")
@pytest.mark.parametrize("verify_ssl", [False, True])
def test_verify_ssl_boolean(mock_httpx_client, verify_ssl: bool | None):
    polarion_client = polarion_api.PolarionClient(
        polarion_api_endpoint="https://example.com",
        polarion_access_token="fake_token",
        verify_ssl=verify_ssl,
    )

    polarion_client.client.get_httpx_client()

    _, kwargs = mock_httpx_client.call_args
    assert kwargs["verify"] is verify_ssl


@mock.patch("httpx.Client")
def test_default_verify_ssl(mock_httpx_client):
    polarion_client = polarion_api.PolarionClient(
        polarion_api_endpoint="https://example.com",
        polarion_access_token="fake_token",
    )

    polarion_client.client.get_httpx_client()

    _, kwargs = mock_httpx_client.call_args
    assert isinstance(kwargs["verify"], ssl.SSLContext)
    assert kwargs["verify"].protocol == ssl.PROTOCOL_TLS_CLIENT


@mock.patch("httpx.Client")
def test_custom_ssl_context(mock_httpx_client):
    custom_ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    polarion_client = polarion_api.PolarionClient(
        polarion_api_endpoint="https://example.com",
        polarion_access_token="fake_token",
        verify_ssl=custom_ssl_context,
    )

    polarion_client.client.get_httpx_client()

    _, kwargs = mock_httpx_client.call_args
    assert kwargs["verify"] is custom_ssl_context


def test_api_authentication(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(
            match_headers={"Authorization": "Bearer PAT123"},
            json=json.load(f),
        )

    assert client.exists()


def test_check_existing_project(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    assert client.exists()


def test_check_non_existing_project(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(status_code=404, json={})

    assert not client.exists()
