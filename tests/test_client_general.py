# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import warnings

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import TEST_PROJECT_RESPONSE_JSON


def test_api_authentication(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(
            match_headers={"Authorization": "Bearer PAT123"},
            json=json.load(f),
        )

    assert client.project_exists()


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
    httpx_mock.add_response(status_code=404, json={})

    assert not client.project_exists()


def test_check_deprecation_warning():
    with warnings.catch_warnings(record=True) as w:
        polarion_api.OpenAPIPolarionProjectClient(
            "P", False, "http://localhost", "123"
        )

        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
