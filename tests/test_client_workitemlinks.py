# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_WIL_CREATED_RESPONSE,
    TEST_WIL_DELETE2_REQUEST,
    TEST_WIL_DELETE_REQUEST,
    TEST_WIL_DELETED_REQUEST,
    TEST_WIL_MULTI_POST_REQUEST,
    TEST_WIL_NEXT_PAGE_RESPONSE,
    TEST_WIL_NO_NEXT_PAGE_RESPONSE,
    TEST_WIL_POSTED_REQUEST,
)


def test_get_work_item_links_single_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(
        TEST_WIL_NO_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    work_item_links = client.get_all_work_item_links(
        "MyWorkItemId",
        include="workitem",
        fields={"fields[linkedworkitems]": "id,role"},
    )

    query = {
        "fields[linkedworkitems]": "id,role",
        "page[size]": "100",
        "page[number]": "1",
        "include": "workitem",
    }
    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert len(work_item_links) == 1
    assert len(reqs) == 1
    assert work_item_links[0] == polarion_api.WorkItemLink(
        "MyWorkItemId", "MyWorkItemId2", "relates_to", True, "MyProjectId"
    )


def test_get_work_item_links_multi_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(
        TEST_WIL_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))
    with open(
        TEST_WIL_NO_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client.get_all_work_item_links("MyWorkItemId")
    query = {
        "fields[linkedworkitems]": "id,role,suspect",
        "page[size]": "100",
        "page[number]": "1",
    }
    reqs = httpx_mock.get_requests()

    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert reqs[1].method == "GET"
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    assert len(work_items) == 2
    assert len(reqs) == 2
    assert work_items[0].suspect is False


def test_delete_work_item_link(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_work_item_link(
        polarion_api.WorkItemLink(
            "MyWorkItemId", "MyWorkItemId2", "parent", True, "MyProjectId"
        )
    )

    req = httpx_mock.get_request()

    assert req is not None and req.method == "DELETE"
    with open(TEST_WIL_DELETED_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_delete_work_item_links(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_work_item_links(
        [
            polarion_api.WorkItemLink(
                "MyWorkItemId", "MyWorkItemId2", "parent", True, "MyProjectId"
            ),
            polarion_api.WorkItemLink(
                "MyWorkItemId", "MyWorkItemId3", "parent", True
            ),
        ]
    )

    req = httpx_mock.get_request()

    assert req is not None and req.method == "DELETE"
    with open(TEST_WIL_DELETE_REQUEST, encoding="utf8") as f:
        expected_request = json.load(f)

    assert json.loads(req.content.decode()) == expected_request


def test_delete_work_item_links_multi_primary(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_work_item_links(
        [
            polarion_api.WorkItemLink(
                "MyWorkItemId", "MyWorkItemId2", "parent", True, "MyProjectId"
            ),
            polarion_api.WorkItemLink(
                "MyWorkItemId2", "MyWorkItemId3", "parent", True
            ),
        ]
    )

    reqs = httpx_mock.get_requests()
    with open(TEST_WIL_DELETED_REQUEST, encoding="utf8") as f:
        expected_request = json.load(f)

    with open(TEST_WIL_DELETE2_REQUEST, encoding="utf8") as f:
        expected_request2 = json.load(f)

    assert len(reqs) == 2
    assert reqs[0].method == "DELETE"
    assert reqs[1].method == "DELETE"
    assert json.loads(reqs[0].content.decode()) == expected_request
    assert json.loads(reqs[1].content.decode()) == expected_request2


def test_create_work_item_link(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WIL_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    client.create_work_item_link(
        polarion_api.WorkItemLink(
            "MyWorkItemId", "MyWorkItemId2", "relates_to", True
        )
    )

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/linkedworkitems")
    with open(TEST_WIL_POSTED_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_item_links_different_primaries(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WIL_CREATED_RESPONSE, encoding="utf8") as f:
        content = json.load(f)

    httpx_mock.add_response(201, json=content)
    httpx_mock.add_response(201, json=content)

    client.create_work_item_links(
        [
            polarion_api.WorkItemLink(
                "MyWorkItemId", "MyWorkItemId2", "relates_to", True
            ),
            polarion_api.WorkItemLink(
                "MyWorkItemId3", "MyWorkItemId2", "relates_to", True
            ),
        ]
    )

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0].method == "POST"
    assert reqs[1].method == "POST"

    assert reqs[0].url.path.endswith(
        "PROJ/workitems/MyWorkItemId/linkedworkitems"
    )
    assert reqs[1].url.path.endswith(
        "PROJ/workitems/MyWorkItemId3/linkedworkitems"
    )

    with open(TEST_WIL_POSTED_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(reqs[0].content.decode()) == expected
    assert json.loads(reqs[1].content.decode()) == expected


def test_create_work_item_links_same_primaries(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WIL_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    client.create_work_item_links(
        [
            polarion_api.WorkItemLink(
                "MyWorkItemId",
                "MyWorkItemId2",
                "relates_to",
                True,
                "MyProjectId",
            ),
            polarion_api.WorkItemLink(
                "MyWorkItemId", "MyWorkItemId3", "parent", False
            ),
        ]
    )

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    with open(TEST_WIL_MULTI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_get_work_item_links_error_first_request(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    caplog: pytest.LogCaptureFixture,
):
    httpx_mock.add_response(502, content=b"Test")
    with open(
        TEST_WIL_NO_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    work_item_links = client.get_all_work_item_links(
        "MyWorkItemId",
    )

    reqs = httpx_mock.get_requests()
    assert len(caplog.record_tuples) == 1
    _, level, message = caplog.record_tuples[0]
    assert level == 30
    assert (
        message == "Will retry after failing on first attempt, due to "
        "the following error "
        "(<HTTPStatus.BAD_GATEWAY: 502>, b'Test')"
    )
    assert len(reqs) == 2
    assert work_item_links[0] == polarion_api.WorkItemLink(
        "MyWorkItemId", "MyWorkItemId2", "relates_to", True, "MyProjectId"
    )
