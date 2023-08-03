# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import pathlib

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from polarion_rest_api_client.open_api_client import models as api_models

TEST_DATA_ROOT = pathlib.Path(__file__).parent / "data"
TEST_RESPONSES = TEST_DATA_ROOT / "mock_api_responses"
TEST_REQUESTS = TEST_DATA_ROOT / "expected_requests"

TEST_WIL_MULTI_POST_REQUEST = TEST_REQUESTS / "post_work_item_links.json"
TEST_WIL_DELETE2_REQUEST = TEST_REQUESTS / "delete_work_item_link_2.json"
TEST_WIL_DELETE_REQUEST = TEST_REQUESTS / "delete_work_item_links.json"
TEST_WIL_DELETED_REQUEST = TEST_REQUESTS / "delete_work_item_link.json"
TEST_WIL_POSTED_REQUEST = TEST_REQUESTS / "post_work_item_link.json"

TEST_WI_DELETE_REQUEST = TEST_REQUESTS / "delete_work_item.json"
TEST_WI_PATCH_STATUS_DELETED_REQUEST = (
    TEST_REQUESTS / "patch_work_item_status_deleted.json"
)
TEST_WI_PATCH_STATUS_REQUEST = TEST_REQUESTS / "patch_work_item_status.json"
TEST_WI_PATCH_TITLE_REQUEST = TEST_REQUESTS / "patch_work_item_title.json"
TEST_WI_PATCH_DESCRIPTION_REQUEST = (
    TEST_REQUESTS / "patch_work_item_description.json"
)
TEST_WI_PATCH_COMPLETELY_REQUEST = (
    TEST_REQUESTS / "patch_work_item_completely.json"
)
TEST_WI_MULTI_POST_REQUEST = TEST_REQUESTS / "post_workitems.json"
TEST_WI_POST_REQUEST = TEST_REQUESTS / "post_workitem.json"

TEST_WIL_CREATED_RESPONSE = TEST_RESPONSES / "created_work_item_links.json"
TEST_WIL_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_linked_work_items_next_page.json"
)
TEST_WIL_NO_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_linked_work_items_no_next_page.json"
)

TEST_WI_NO_NEXT_PAGE_RESPONSE = TEST_RESPONSES / "workitems_no_next_page.json"
TEST_WI_CREATED_RESPONSE = TEST_RESPONSES / "created_work_items.json"
TEST_WI_ERROR_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "workitems_next_page_error.json"
)
TEST_WI_NEXT_PAGE_RESPONSE = TEST_RESPONSES / "workitems_next_page.json"

TEST_ERROR_RESPONSE = TEST_RESPONSES / "error.json"

TEST_PROJECT_RESPONSE_JSON = TEST_RESPONSES / "project.json"


class CustomWorkItem(polarion_api.WorkItem):
    capella_uuid: str | None


@pytest.fixture(name="client")
def fixture_client():
    yield polarion_api.OpenAPIPolarionProjectClient(
        project_id="PROJ",
        delete_polarion_work_items=False,
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3
    )


def get_dummy_work_item():
    return polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )


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
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))
    work_item = get_dummy_work_item()

    client.create_work_item(work_item)

    req = httpx_mock.get_request()
    assert req is not None and req.method == "POST"
    with open(TEST_WI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_items_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))
    work_item = get_dummy_work_item()

    client.create_work_items(3 * [work_item])

    req = httpx_mock.get_request()

    assert req is not None and req.method == "POST"
    with open(TEST_WI_MULTI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_items_batch_exceed_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)
    httpx_mock.add_response(201, json=mock_response)

    work_item = get_dummy_work_item()

    client.create_work_items(6 * [work_item])

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0] is not None and reqs[0].method == "POST"
    assert reqs[1] is not None and reqs[1].method == "POST"
    with open(TEST_WI_MULTI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(reqs[0].content.decode()) == expected
    assert json.loads(reqs[1].content.decode()) == expected


def test_create_work_items_content_big_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)
    httpx_mock.add_response(201, json=mock_response)

    work_item = get_dummy_work_item()

    work_item_long = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="AB" * 512 * 1024,
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )

    client.create_work_items(3 * [work_item, work_item_long])

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 3
    assert reqs[0] is not None and reqs[0].method == "POST"
    assert len(json.loads(reqs[0].content.decode("utf-8"))["data"]) == 3
    assert reqs[1] is not None and reqs[1].method == "POST"
    assert len(json.loads(reqs[1].content.decode("utf-8"))["data"]) == 2
    assert reqs[2] is not None and reqs[1].method == "POST"
    assert len(json.loads(reqs[2].content.decode("utf-8"))["data"]) == 1


def test_create_work_items_content_exceed_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)
    httpx_mock.add_response(201, json=mock_response)
    httpx_mock.add_response(201, json=mock_response)

    work_item = get_dummy_work_item()

    work_item_long = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="AB" * 512 * 1024,
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )

    client.create_work_items(3 * [work_item, work_item_long])

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 3
    assert reqs[0] is not None and reqs[0].method == "POST"
    assert len(json.loads(reqs[0].content.decode("utf-8"))["data"]) == 3
    assert reqs[1] is not None and reqs[1].method == "POST"
    assert len(json.loads(reqs[1].content.decode("utf-8"))["data"]) == 2
    assert reqs[2] is not None and reqs[1].method == "POST"
    assert len(json.loads(reqs[2].content.decode("utf-8"))["data"]) == 1


def test_create_work_items_content_exceed_error(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    caplog,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)

    work_item = get_dummy_work_item()

    work_item_long = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="AB" * 1024 * 1024,
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )

    client.create_work_items(3 * [work_item, work_item_long])

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 1
    assert reqs[0] is not None and reqs[0].method == "POST"
    with open(TEST_WI_MULTI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(reqs[0].content.decode()) == expected
    counter = 0
    for record in caplog.records:
        if record.levelname == "ERROR":
            counter += 1
            assert record.message == "A WorkItem is to large to create."

    assert counter == 3


def test_work_item_single_request_size(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)

    min_size = len(
        json.dumps(api_models.WorkitemsListPostRequest([]).to_dict()).encode(
            "utf-8"
        )
    )

    work_item = get_dummy_work_item()

    work_item_data = client._build_work_item_post_request(work_item)

    size, _ = client._calculate_post_work_item_request_sizes(
        work_item_data, min_size
    )

    client.create_work_items([work_item])

    req = httpx_mock.get_request()

    assert len(req.content) == size


def test_work_item_multi_request_size(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        mock_response = json.load(f)

    httpx_mock.add_response(201, json=mock_response)

    size = len(
        json.dumps(api_models.WorkitemsListPostRequest([]).to_dict()).encode(
            "utf-8"
        )
    )

    work_item = get_dummy_work_item()

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
):
    expected = (
        "Unexpected token, BEGIN_ARRAY expected, but was"
        " : BEGIN_OBJECT (at $.data)"
    )
    with open(TEST_ERROR_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(400, json=json.load(f))

    work_item = get_dummy_work_item()
    with pytest.raises(polarion_api.PolarionApiException) as exc_info:
        client.create_work_items(3 * [work_item])

    assert exc_info.type is polarion_api.PolarionApiException
    assert exc_info.value.args[0][0] == "400"
    assert exc_info.value.args[0][1] == expected


def test_create_work_items_failed_no_error(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(501, content=b"asdfg")

    work_item = get_dummy_work_item()
    with pytest.raises(polarion_api.PolarionApiBaseException) as exc_info:
        client.create_work_items(3 * [work_item])

    assert exc_info.type is polarion_api.PolarionApiUnexpectedException
    assert exc_info.value.args[0] == 501
    assert exc_info.value.args[1] == b"asdfg"


def test_update_work_item_completely(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.update_work_item(
        polarion_api.WorkItem(
            id="MyWorkItemId",
            description_type="text/html",
            description="My text value",
            title="Title",
            status="open",
            additional_attributes={"capella_uuid": "qwertz"},
        )
    )

    req = httpx_mock.get_request()

    assert req is not None
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_WI_PATCH_COMPLETELY_REQUEST, encoding="utf8") as f:
        assert json.loads(req.content.decode()) == json.load(f)


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
        assert json.loads(req.content.decode()) == json.load(f)


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

    assert len(reqs) == 2
    assert reqs[0].method == "DELETE"
    assert reqs[1].method == "DELETE"
    with open(TEST_WIL_DELETED_REQUEST, encoding="utf8") as f:
        assert json.loads(reqs[0].content.decode()) == json.load(f)
    with open(TEST_WIL_DELETE2_REQUEST, encoding="utf8") as f:
        assert json.loads(reqs[1].content.decode()) == json.load(f)


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


def test_get_all_work_items_single_page_custom_work_item(
    client_custom_work_item: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_NO_NEXT_PAGE_RESPONSE) as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client_custom_work_item.get_all_work_items("")
    assert isinstance(work_items[0], CustomWorkItem)
    assert work_items[0].capella_uuid == "asdfgh"


def test_create_work_item_custom_work_item(
    client_custom_work_item: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "created_work_items.json") as f:
        httpx_mock.add_response(201, json=json.load(f))
    work_item = CustomWorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        capella_uuid="asdfgh",
    )

    work_item.capella_uuid = "asdfg"

    client_custom_work_item.create_work_item(work_item)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    with open(TEST_REQUESTS / "post_workitem.json") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected
