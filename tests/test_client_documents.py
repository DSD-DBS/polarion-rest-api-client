# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import TEST_DOCUMENT_RESPONSE


def test_get_document_with_all_fields(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_DOCUMENT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    document = client.get_document(
        "MySpaceId", "MyDocumentName", {"fields[documents]": "@all"}
    )

    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert isinstance(document, polarion_api.data_models.Document)
    assert len(reqs) == 1
    assert document == polarion_api.data_models.Document(
        "MyProjectId/MySpaceId/MyDocumentName",
        "MySpaceId",
        "MyDocumentName",
        "standardSpecification",
        "open",
        polarion_api.data_models.TextContent(
            type="text/html", value="<h1>My text value</h1>"
        ),
    )
