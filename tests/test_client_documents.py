# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_DOCUMENT_PATCH_REQUEST,
    TEST_DOCUMENT_POST_REQUEST,
    TEST_DOCUMENT_RESPONSE,
)


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


def test_create_new_document(
    new_client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    document = polarion_api.Document(
        module_folder="folder",
        module_name="name",
        home_page_content=polarion_api.TextContent(
            type="text/html", value="super Value"
        ),
        title="Fancy Title",
    )

    httpx_mock.add_response(
        201,
        json={
            "data": [
                {
                    "type": "documents",
                    "id": "PROJ/folder/name",
                    "links": {
                        "self": "server-host-name/application-path/projects/PROJ/spaces/folder/documents/name?revision=1234"  # pylint: disable=line-too-long
                    },
                }
            ]
        },
    )
    new_client.documents.create(document)

    with open(TEST_DOCUMENT_POST_REQUEST, "r", encoding="utf-8") as f:
        expected_request = json.load(f)

    assert len(httpx_mock.get_requests()) == 1
    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert (
        req.url == "http://127.0.0.1/api/projects/PROJ/spaces/folder/documents"
    )
    assert json.loads(req.content.decode("utf-8")) == expected_request


def test_update_document(
    new_client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    document = polarion_api.Document(
        module_folder="folder",
        module_name="name",
        home_page_content=polarion_api.TextContent(
            type="text/html", value="super Value"
        ),
        title="Fancy Title",
    )

    httpx_mock.add_response(204)
    new_client.documents.update(document)

    with open(TEST_DOCUMENT_PATCH_REQUEST, "r", encoding="utf-8") as f:
        expected_request = json.load(f)

    assert len(httpx_mock.get_requests()) == 1
    req = httpx_mock.get_request()
    assert req.method == "PATCH"
    assert (
        req.url
        == "http://127.0.0.1/api/projects/PROJ/spaces/folder/documents/name"
    )
    assert json.loads(req.content.decode("utf-8")) == expected_request
