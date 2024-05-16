# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import TEST_FAULTS_ERROR_RESPONSES


def test_faulty_error_message(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_FAULTS_ERROR_RESPONSES, encoding="utf8") as f:
        httpx_mock.add_response(400, json=json.load(f))

    with pytest.raises(polarion_api.PolarionApiException) as e_info:
        client.get_document(
            "MySpaceId", "MyDocumentName", {"fields[documents]": "@all"}
        )

    e = e_info.value
    assert len(e.args) == 5
    assert e.args[0][0] == "400"
    assert (
        e.args[0][1] == "Unexpected token, BEGIN_ARRAY expected, but was : "
        "BEGIN_OBJECT (at $.data)"
    )
