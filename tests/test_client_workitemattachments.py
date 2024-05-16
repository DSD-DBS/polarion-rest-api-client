# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import copy
import json

import pytest_httpx
from httpx import _multipart

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_WIA_CREATED_RESPONSE,
    TEST_WIA_MULTI_CREATED_RESPONSE,
    TEST_WIA_NEXT_PAGE_RESPONSE,
    TEST_WIA_NO_NEXT_PAGE_RESPONSE,
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
        "MyWorkItemId", "MyAttachmentId", "Title", file_name="File Name"
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


def test_create_single_work_item_attachment(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    with open(TEST_WIA_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    client.create_work_item_attachment(work_item_attachment)

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/attachments")
    assert work_item_attachment.id == "MyAttachmentId"

    body = req.stream
    assert isinstance(body, _multipart.MultipartStream)
    assert len(body.fields) == 2

    resource_index = None
    files_index = None
    for i in range(2):
        if body.fields[i].name == "resource":
            resource_index = i
        if body.fields[i].name == "files":
            files_index = i

    assert resource_index is not None
    assert files_index is not None

    assert body.fields[resource_index].headers["Content-Type"] == "text/plain"
    assert body.fields[resource_index].name == "resource"
    assert body.fields[resource_index].file == json.dumps(
        {
            "data": [
                {
                    "type": "workitem_attachments",
                    "attributes": {"fileName": "test.json", "title": "Title"},
                }
            ]
        }
    ).encode("utf-8")

    assert body.fields[files_index].headers["Content-Type"] == "text/plain"
    assert body.fields[files_index].filename == "test.json"
    assert body.fields[files_index].name == "files"
    assert (
        body.fields[files_index].file.read()
        == work_item_attachment.content_bytes
    )


def test_create_multiple_work_item_attachments(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    with open(TEST_WIA_MULTI_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    work_item_attachments = [
        work_item_attachment,
        copy.deepcopy(work_item_attachment),
        copy.deepcopy(work_item_attachment),
    ]

    client.create_work_item_attachments(work_item_attachments)

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/attachments")

    assert work_item_attachments[0].id == "MyAttachmentId1"
    assert work_item_attachments[1].id == "MyAttachmentId2"
    assert work_item_attachments[2].id == "MyAttachmentId3"

    body = req.stream
    assert isinstance(body, _multipart.MultipartStream)
    assert len(body.fields) == 4

    for i in range(0, 3):
        assert body.fields[i].headers["Content-Type"] == "text/plain"
        assert body.fields[i].filename == "test.json"
        assert body.fields[i].name == "files"
        assert (
            body.fields[i].file.read()
            == work_item_attachments[i - 1].content_bytes
        )

    assert body.fields[3].headers["Content-Type"] == "text/plain"
    assert body.fields[3].name == "resource"
    assert body.fields[3].file == json.dumps(
        {
            "data": 3
            * [
                {
                    "type": "workitem_attachments",
                    "attributes": {"fileName": "test.json", "title": "Title"},
                }
            ]
        }
    ).encode("utf-8")


def test_update_work_item_attachment_title(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    httpx_mock.add_response(204)

    work_item_attachment.id = "MyAttachmentId"
    work_item_attachment.title = "TestTitle"
    work_item_attachment.mime_type = None
    work_item_attachment.content_bytes = None
    work_item_attachment.file_name = None

    client.update_work_item_attachment(work_item_attachment)

    req = httpx_mock.get_request()

    body = req.stream
    assert isinstance(body, _multipart.MultipartStream)
    assert len(body.fields) == 1

    assert body.fields[0].headers["Content-Type"] == "text/plain"
    assert body.fields[0].name == "resource"
    assert body.fields[0].file == json.dumps(
        {
            "data": {
                "type": "workitem_attachments",
                "id": "PROJ/MyWorkItemId/MyAttachmentId",
                "attributes": {"title": "TestTitle"},
            }
        }
    ).encode("utf-8")


def test_update_work_item_attachment_content(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    httpx_mock.add_response(204)

    work_item_attachment.id = "MyAttachmentId"
    work_item_attachment.title = None

    client.update_work_item_attachment(work_item_attachment)

    req = httpx_mock.get_request()

    body = req.stream
    assert isinstance(body, _multipart.MultipartStream)
    assert len(body.fields) == 2

    assert body.fields[0].headers["Content-Type"] == "text/plain"
    assert body.fields[0].name == "resource"
    assert body.fields[0].file == json.dumps(
        {
            "data": {
                "type": "workitem_attachments",
                "id": "PROJ/MyWorkItemId/MyAttachmentId",
                "attributes": {},
            }
        }
    ).encode("utf-8")

    assert body.fields[1].headers["Content-Type"] == "text/plain"
    assert body.fields[1].filename == "test.json"
    assert body.fields[1].name == "content"
    assert body.fields[1].file.read() == work_item_attachment.content_bytes
