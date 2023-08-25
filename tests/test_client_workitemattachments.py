# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests import (
    TEST_WIA_CREATED_RESPONSE,
    TEST_WIA_MULTI_POST_REQUEST,
    TEST_WIA_NEXT_PAGE_RESPONSE,
    TEST_WIA_NO_NEXT_PAGE_RESPONSE,
    TEST_WIA_POSTED_REQUEST,
)


def test_get_work_item_attachments_single_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(
        TEST_WIA_NO_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    work_item_attachments = client.get_all_work_item_attachments(
        "MyWorkItemId",
        fields={"fields[workitem_attachments]": "id,title"},
    )
    query = {
        "fields[workitem_attachments]": "id,title",
        "page[size]": "100",
        "page[number]": "1",
    }

    reqs = httpx_mock.get_requests()

    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert len(work_item_attachments) == 1
    assert len(reqs) == 1
    assert work_item_attachments[0] == polarion_api.WorkItemAttachment(
        "MyWorkItemId", "MyAttachmentId", "Title"
    )


def test_get_work_item_attachments_multi_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(
        TEST_WIA_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))
    with open(
        TEST_WIA_NO_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    work_items_attachments = client.get_all_work_item_attachments(
        "MyWorkItemId"
    )
    query = {
        "fields[workitem_attachments]": "@basic",
        "page[size]": "100",
        "page[number]": "1",
    }
    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert reqs[1].method == "GET"
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    assert len(work_items_attachments) == 2


def test_delete_work_item_attachment(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_work_item_attachment(
        polarion_api.WorkItemAttachment("MyWorkItemId", "Attachment", "Title")
    )

    req = httpx_mock.get_request()

    assert req is not None and req.method == "DELETE"
    assert req.url.path.endswith(
        "PROJ/workitems/MyWorkItemId/attachments/Attachment"
    )


def test_create_work_item_attachment(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WIA_CREATED_RESPONSE, encoding="utf8") as f:
        content = f.read()
        httpx_mock.add_response(201, json=json.loads(content))

    client.create_work_item_attachment(
        polarion_api.WorkItemAttachment(
            "MyWorkItemId",
            "Attachment",
            "Title",
            content.encode("utf-8"),
            "text/plain",
            "test.json",
        )
    )

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/linkedworkitems")
    with open(TEST_WIA_POSTED_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected
