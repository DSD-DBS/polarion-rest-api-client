# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import copy
import email
import json
from email import message

import httpx
import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_WIA_CREATED_RESPONSE,
    TEST_WIA_MULTI_CREATED_RESPONSE,
    TEST_WIA_NEXT_PAGE_RESPONSE,
    TEST_WIA_NO_NEXT_PAGE_RESPONSE,
)


def _extract_data_from_request(
    req: httpx.Request,
) -> dict[str, list[message.Message]]:
    headers = f"Content-Type: {req.headers['Content-Type']}\r\n\r\n"
    msg = email.message_from_bytes(
        headers.encode(req.headers.encoding) + req.content
    )
    fields: dict[str, list[message.Message]] = {}
    for part in msg.walk():
        field_name = part.get_param("name", header="Content-Disposition")
        if isinstance(field_name, str):
            fields.setdefault(field_name, []).append(part)
    return fields


@pytest.mark.parametrize(
    ("revision", "query"),
    [
        (
            None,
            {
                "fields[workitem_attachments]": "id,title",
                "page[size]": "100",
                "page[number]": "1",
            },
        ),
        (
            "12345",
            {
                "fields[workitem_attachments]": "id,title",
                "page[size]": "100",
                "page[number]": "1",
                "revision": "12345",
            },
        ),
    ],
    ids=["no_revision", "with_revision"],
)
def test_get_work_item_attachments_single_page(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    revision: str | None,
    query: dict,
):
    with open(
        TEST_WIA_NO_NEXT_PAGE_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    work_item_attachments = client.work_items.attachments.get_all(
        "MyWorkItemId",
        fields={"fields[workitem_attachments]": "id,title"},
        revision=revision,
    )

    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert len(work_item_attachments) == 1
    assert len(reqs) == 1
    assert work_item_attachments[0] == polarion_api.WorkItemAttachment(
        "MyWorkItemId", "MyAttachmentId", "Title", file_name="File Name"
    )


def test_get_work_item_attachments_multi_page(
    client: polarion_api.ProjectClient,
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

    work_items_attachments = client.work_items.attachments.get_all(
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
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.work_items.attachments.delete(
        polarion_api.WorkItemAttachment("MyWorkItemId", "Attachment", "Title")
    )

    req = httpx_mock.get_request()

    assert req is not None
    assert req.method == "DELETE"
    assert req.url.path.endswith(
        "PROJ/workitems/MyWorkItemId/attachments/Attachment"
    )


def test_create_single_work_item_attachment(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    with open(TEST_WIA_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    client.work_items.attachments.create(work_item_attachment)

    req = httpx_mock.get_request()
    fields = _extract_data_from_request(req)
    resource = fields["resource"][0]
    files = fields["files"]

    assert req is not None
    assert req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/attachments")
    assert work_item_attachment.id == "MyAttachmentId"
    assert work_item_attachment.content_bytes is not None

    assert resource is not None
    assert len(files) == 1

    assert resource.get_content_type() == "text/plain"
    assert resource.get_payload() == json.dumps(
        {
            "data": [
                {
                    "type": "workitem_attachments",
                    "attributes": {"fileName": "test.json", "title": "Title"},
                }
            ]
        }
    )

    assert files[0].get_content_type() == "text/plain"
    assert files[0].get_filename() == "test.json"
    assert files[0].get_payload() == work_item_attachment.content_bytes.decode(
        "utf-8"
    )


def test_create_multiple_work_item_attachments(
    client: polarion_api.ProjectClient,
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

    client.work_items.attachments.create(work_item_attachments)

    req = httpx_mock.get_request()

    assert req is not None
    assert req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/attachments")

    assert work_item_attachments[0].id == "MyAttachmentId1"
    assert work_item_attachments[1].id == "MyAttachmentId2"
    assert work_item_attachments[2].id == "MyAttachmentId3"

    fields = _extract_data_from_request(req)
    resource = fields["resource"][0]
    files = fields["files"]

    assert len(files) == 3

    for index, file in enumerate(files):
        assert (
            content := work_item_attachments[index - 1].content_bytes
        ) is not None
        assert file.get_content_type() == "text/plain"
        assert file.get_filename() == "test.json"
        assert content.decode("utf-8")

    assert resource.get_content_type() == "text/plain"
    assert resource.get_payload() == json.dumps(
        {
            "data": 3
            * [
                {
                    "type": "workitem_attachments",
                    "attributes": {"fileName": "test.json", "title": "Title"},
                }
            ]
        }
    )


def test_update_work_item_attachment_title(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    httpx_mock.add_response(204)

    work_item_attachment.id = "MyAttachmentId"
    work_item_attachment.title = "TestTitle"
    work_item_attachment.mime_type = None
    work_item_attachment.content_bytes = None
    work_item_attachment.file_name = None

    client.work_items.attachments.update(work_item_attachment)

    req = httpx_mock.get_request()

    fields = _extract_data_from_request(req)
    resource = fields["resource"][0]

    assert "files" not in fields
    assert resource.get_content_type() == "text/plain"
    assert resource.get_payload() == json.dumps(
        {
            "data": {
                "type": "workitem_attachments",
                "id": "PROJ/MyWorkItemId/MyAttachmentId",
                "attributes": {"title": "TestTitle"},
            }
        }
    )


def test_update_work_item_attachment_content(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_attachment: polarion_api.WorkItemAttachment,
):
    httpx_mock.add_response(204)

    work_item_attachment.id = "MyAttachmentId"
    work_item_attachment.title = None

    client.work_items.attachments.update(work_item_attachment)

    req = httpx_mock.get_request()

    fields = _extract_data_from_request(req)
    resource = fields["resource"][0]
    content = fields["content"][0]

    assert resource.get_content_type() == "text/plain"
    assert resource.get_payload() == json.dumps(
        {
            "data": {
                "type": "workitem_attachments",
                "id": "PROJ/MyWorkItemId/MyAttachmentId",
                "attributes": {},
            }
        }
    )

    assert content.get_content_type() == "text/plain"
    assert content.get_filename() == "test.json"
    assert work_item_attachment.content_bytes is not None
    assert content.get_payload() == work_item_attachment.content_bytes.decode(
        "utf-8"
    )
