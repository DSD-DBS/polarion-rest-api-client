# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import copy
import json

import pytest
import pytest_httpx
import pytest_mock as mock

import polarion_rest_api_client as polarion_api
from polarion_rest_api_client.open_api_client import models as api_models
from tests import (
    TEST_ERROR_RESPONSE,
    TEST_WI_CREATED_RESPONSE,
    TEST_WI_DELETE_REQUEST,
    TEST_WI_ERROR_NEXT_PAGE_RESPONSE,
    TEST_WI_MULTI_POST_REQUEST,
    TEST_WI_NEXT_PAGE_RESPONSE,
    TEST_WI_NO_NEXT_PAGE_RESPONSE,
    TEST_WI_NOT_TRUNCATED_RESPONSE,
    TEST_WI_PATCH_COMPLETELY_REQUEST,
    TEST_WI_PATCH_DESCRIPTION_REQUEST,
    TEST_WI_PATCH_STATUS_DELETED_REQUEST,
    TEST_WI_PATCH_STATUS_REQUEST,
    TEST_WI_PATCH_TITLE_REQUEST,
    TEST_WI_POST_REQUEST,
    TEST_WI_SINGLE_RESPONSE,
)


def test_get_one_work_item(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_SINGLE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    work_item = client.get_work_item("MyWorkItemId")

    query = {
        "fields[workitems]": "@all",
        "fields[workitem_attachments]": "@all",
        "fields[linkedworkitems]": "@all",
    }
    reqs = httpx_mock.get_requests()

    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert len(reqs) == 1

    assert work_item is not None
    assert len(work_item.linked_work_items) == 1
    assert len(work_item.attachments) == 1
    assert "test_custom_field" in work_item.additional_attributes
    assert work_item.attachments_truncated is True
    assert work_item.linked_work_items_truncated is True


def test_get_one_work_item_not_truncated(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_NOT_TRUNCATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    work_item = client.get_work_item("MyWorkItemId")

    query = {
        "fields[workitems]": "@all",
        "fields[workitem_attachments]": "@all",
        "fields[linkedworkitems]": "@all",
    }
    reqs = httpx_mock.get_requests()

    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert len(reqs) == 1

    assert work_item is not None
    assert len(work_item.linked_work_items) == 1
    assert len(work_item.attachments) == 1
    assert "test_custom_field" in work_item.additional_attributes
    assert work_item.attachments_truncated is False
    assert work_item.linked_work_items_truncated is False


def test_get_all_work_items_multi_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_NEXT_PAGE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))
    with open(TEST_WI_NO_NEXT_PAGE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client.get_all_work_items(
        "",
        {"fields[workitems]": "id"},
    )
    query = {
        "fields[workitems]": "id",
        "page[size]": "100",
        "page[number]": "1",
        "query": "",
    }
    reqs = httpx_mock.get_requests()

    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert reqs[1].method == "GET"
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    assert len(work_items) == 2
    assert len(reqs) == 2
    assert work_items[0].status is None


def test_get_all_work_items_single_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_NO_NEXT_PAGE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client.default_fields.workitems = "@basic,description"

    work_items = client.get_all_work_items("")

    query = {
        "fields[workitems]": "@basic,description",
        "page[size]": "100",
        "page[number]": "1",
        "query": "",
    }
    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert len(work_items) == 1
    assert len(reqs) == 1
    assert dict(reqs[0].url.params) == query
    assert work_items[0] == polarion_api.WorkItem(
        "MyWorkItemId2",
        "Title",
        "text/html",
        "My text value",
        "task",
        "open",
        {"capella_uuid": "asdfgh"},
        [
            polarion_api.WorkItemLink(
                "MyWorkItemId2",
                "MyLinkedWorkItemId",
                "parent",
                False,
                "MyProjectId",
            )
        ],
        [polarion_api.WorkItemAttachment("MyWorkItemId2", "MyAttachmentId")],
    )


def test_get_all_work_items_faulty_item(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_ERROR_NEXT_PAGE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    with open(TEST_WI_NO_NEXT_PAGE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client.get_all_work_items("")
    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert len(work_items) == 1
    assert len(reqs) == 2


def test_create_work_item(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    client.create_work_item(work_item)

    req = httpx_mock.get_request()
    assert req is not None and req.method == "POST"
    with open(TEST_WI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_item_checksum(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    checksum = work_item.calculate_checksum()

    client.add_work_item_checksum = True
    client.create_work_item(work_item)

    req = httpx_mock.get_request()

    with open(TEST_WI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    expected["data"][0]["attributes"]["checksum"] = checksum
    assert json.loads(req.content.decode()) == expected


def test_create_work_items_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    mock_response["data"] *= 3
    httpx_mock.add_response(201, json=mock_response)

    client.create_work_items(3 * [work_item])

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    with open(TEST_WI_MULTI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_items_batch_exceed_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    mock_response["data"] *= 3
    httpx_mock.add_response(201, json=mock_response)
    httpx_mock.add_response(201, json=mock_response)

    client.create_work_items(6 * [work_item])

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0] is not None and reqs[0].method == "POST"
    assert reqs[1] is not None and reqs[1].method == "POST"
    with open(TEST_WI_MULTI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(reqs[0].content.decode()) == expected
    assert json.loads(reqs[1].content.decode()) == expected


def test_create_work_items_content_exceed_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    mock_response_data = mock_response["data"]
    mock_response["data"] = 3 * mock_response_data
    httpx_mock.add_response(201, json=mock_response)
    mock_response["data"] = 2 * mock_response_data
    httpx_mock.add_response(201, json=mock_response)
    mock_response["data"] = mock_response_data
    httpx_mock.add_response(201, json=mock_response)

    work_item_long = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="AB" * 512 * 1024,
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )

    work_items = [
        work_item,
        work_item_long,
        copy.deepcopy(work_item),
        copy.deepcopy(work_item_long),
        copy.deepcopy(work_item),
        copy.deepcopy(work_item_long),
    ]

    client.create_work_items(work_items)

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 3
    assert reqs[0] is not None and reqs[0].method == "POST"
    assert len(json.loads(reqs[0].content.decode("utf-8"))["data"]) == 3
    assert reqs[1] is not None and reqs[1].method == "POST"
    assert len(json.loads(reqs[1].content.decode("utf-8"))["data"]) == 2
    assert reqs[2] is not None and reqs[2].method == "POST"
    assert len(json.loads(reqs[2].content.decode("utf-8"))["data"]) == 1

    assert all([wi.id == "MyWorkItemId" for wi in work_items])


def test_create_work_items_content_exceed_error(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    work_item_long = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="AB" * 1024 * 1024,
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )
    with pytest.raises(polarion_api.PolarionWorkItemException) as exc_info:
        client.create_work_items(3 * [work_item, work_item_long])

    assert exc_info.value.work_item == work_item_long
    assert (
        exc_info.value.args[0]
        == "A WorkItem is too large to create. (WorkItem Title: Title)"
    )
    assert len(httpx_mock.get_requests()) == 0


def test_work_item_single_request_size(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)

    work_item_data = client._build_work_item_post_request(work_item)
    size, _ = client._calculate_post_work_item_request_sizes(work_item_data)

    client.create_work_items([work_item])

    req = httpx_mock.get_request()

    assert len(req.content) == size


def test_work_item_multi_request_size(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    mock_response["data"] *= 2
    httpx_mock.add_response(201, json=mock_response)

    size = len(
        json.dumps(api_models.WorkitemsListPostRequest([]).to_dict()).encode(
            "utf-8"
        )
    )

    work_item_data = client._build_work_item_post_request(work_item)

    size, _ = client._calculate_post_work_item_request_sizes(
        work_item_data, size
    )
    size, _ = client._calculate_post_work_item_request_sizes(
        work_item_data, size
    )

    client.create_work_items(2 * [work_item])

    req = httpx_mock.get_request()

    assert len(req.content) == size


def test_create_work_items_failed(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    expected = (
        "Unexpected token, BEGIN_ARRAY expected, but was"
        " : BEGIN_OBJECT (at $.data)"
    )
    with open(TEST_ERROR_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(400, json=json.load(f))

    with pytest.raises(polarion_api.PolarionApiException) as exc_info:
        client.create_work_items(3 * [work_item])

    assert exc_info.type is polarion_api.PolarionApiException
    assert exc_info.value.args[0][0] == "400"
    assert exc_info.value.args[0][1] == expected
    assert len(httpx_mock.get_requests()) == 2


def test_create_work_items_failed_no_error(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item: polarion_api.WorkItem,
):
    httpx_mock.add_response(501, content=b"asdfg")

    with pytest.raises(polarion_api.PolarionApiBaseException) as exc_info:
        client.create_work_items(3 * [work_item])

    assert exc_info.type is polarion_api.PolarionApiUnexpectedException
    assert exc_info.value.args[0] == 501
    assert exc_info.value.args[1] == b"asdfg"


def test_update_work_item_completely(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_patch: polarion_api.WorkItem,
):
    httpx_mock.add_response(204)

    client.update_work_item(work_item_patch)

    req = httpx_mock.get_request()

    assert req is not None
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_WI_PATCH_COMPLETELY_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_update_work_item_completely_checksum(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    work_item_patch: polarion_api.WorkItem,
    mocker: mock.MockerFixture,
):
    httpx_mock.add_response(204)

    spy = mocker.spy(work_item_patch, "calculate_checksum")

    checksum = work_item_patch.calculate_checksum()
    client.add_work_item_checksum = True
    client.update_work_item(work_item_patch)

    req = httpx_mock.get_request()

    with open(TEST_WI_PATCH_COMPLETELY_REQUEST, encoding="utf8") as f:
        request = json.load(f)

    request["data"]["attributes"]["checksum"] = checksum
    assert json.loads(req.content.decode()) == request
    spy.assert_called_once()


def test_update_work_item_description(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.update_work_item(
        polarion_api.WorkItem(
            id="MyWorkItemId",
            description_type="text/html",
            description="My text value",
        )
    )

    req = httpx_mock.get_request()

    assert req is not None
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_WI_PATCH_DESCRIPTION_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_update_work_item_title(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.update_work_item(
        polarion_api.WorkItem(
            id="MyWorkItemId",
            title="Title",
        )
    )

    req = httpx_mock.get_request()

    assert req is not None
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_WI_PATCH_TITLE_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_update_work_item_status(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.update_work_item(
        polarion_api.WorkItem(
            id="MyWorkItemId",
            status="open",
        )
    )

    req = httpx_mock.get_request()

    assert req is not None
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_WI_PATCH_STATUS_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_delete_work_item_status_mode(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_work_item("MyWorkItemId")

    req = httpx_mock.get_request()

    assert req is not None and req.method == "PATCH"
    with open(TEST_WI_PATCH_STATUS_DELETED_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_delete_work_item_delete_mode(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_polarion_work_items = True

    client.delete_work_item("MyWorkItemId")

    req = httpx_mock.get_request()

    assert req is not None and req.method == "DELETE"
    with open(TEST_WI_DELETE_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)
