# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests import TEST_PROJECT_RESPONSE_JSON


def test_api_authentication(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(
            match_headers={"Authorization": "Bearer PAT123"},
            json=json.load(f),
        )
    client.project_exists()


def test_check_existing_project(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))
    assert client.project_exists()


def test_check_non_existing_project(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(status_code=404)
    assert not client.project_exists()