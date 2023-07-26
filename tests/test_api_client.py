# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json
import pathlib

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api

TEST_DATA_ROOT = pathlib.Path(__file__).parent / "data"
TEST_RESPONSES = TEST_DATA_ROOT / "mock_api_responses"
TEST_REQUESTS = TEST_DATA_ROOT / "expected_requests"


@pytest.fixture()
def client():
    yield polarion_api.OpenAPIPolarionProjectClient(
        "PROJ", False, "http://127.0.0.1/api", "PAT123"
    )


def test_api_authentication(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "project.json") as f:
        httpx_mock.add_response(
            match_headers={"Authorization": "Bearer PAT123"},
            json=json.load(f),
        )
    client.project_exists()


def test_check_existing_project(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "project.json") as f:
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
    with open(TEST_RESPONSES / "workitems_next_page.json") as f:
        httpx_mock.add_response(json=json.load(f))
    with open(TEST_RESPONSES / "workitems_no_next_page.json") as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client.get_all_work_items(
        "",
        {"fields[workitems]": f"id"},
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
    with open(TEST_RESPONSES / "workitems_no_next_page.json") as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client.get_all_work_items("")
    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert len(work_items) == 1
    assert len(reqs) == 1
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
    with open(TEST_RESPONSES / "workitems_next_page_error.json") as f:
        httpx_mock.add_response(json=json.load(f))

    with open(TEST_RESPONSES / "workitems_no_next_page.json") as f:
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
    with open(TEST_RESPONSES / "created_work_items.json") as f:
        httpx_mock.add_response(201, json=json.load(f))
    work_item = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )

    client.create_work_item(work_item)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    with open(TEST_REQUESTS / "post_workitem.json") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_items_successfully(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "created_work_items.json") as f:
        httpx_mock.add_response(201, json=json.load(f))
    work_item = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )

    client.create_work_items(3 * [work_item])

    req = httpx_mock.get_request()

    assert req.method == "POST"
    with open(TEST_REQUESTS / "post_workitems.json") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_items_failed(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "error.json") as f:
        httpx_mock.add_response(400, json=json.load(f))
    work_item = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )
    with pytest.raises(polarion_api.PolarionApiException) as exc_info:
        client.create_work_items(3 * [work_item])

    assert exc_info.type is polarion_api.PolarionApiException
    assert exc_info.value.args[0][0] == "400"
    assert (
        exc_info.value.args[0][1]
        == "Unexpected token, BEGIN_ARRAY expected, but was : BEGIN_OBJECT (at $.data)"
    )


def test_create_work_items_failed_no_error(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(501, content=b"asdfg")

    work_item = polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )
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

    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_REQUESTS / "patch_work_item_completely.json") as f:
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

    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_REQUESTS / "patch_work_item_description.json") as f:
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

    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_REQUESTS / "patch_work_item_title.json") as f:
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

    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId")
    assert req.method == "PATCH"
    with open(TEST_REQUESTS / "patch_work_item_status.json") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_delete_work_item_status_mode(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_work_item("MyWorkItemId")

    req = httpx_mock.get_request()

    assert req.method == "PATCH"
    with open(TEST_REQUESTS / "patch_work_item_status_deleted.json") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_delete_work_item_delete_mode(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    client.delete_polarion_work_items = True

    client.delete_work_item("MyWorkItemId")

    req = httpx_mock.get_request()

    assert req.method == "DELETE"
    with open(TEST_REQUESTS / "delete_work_item.json") as f:
        assert json.loads(req.content.decode()) == json.load(f)


def test_get_work_item_links_single_page(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "get_linked_work_items_no_next_page.json") as f:
        httpx_mock.add_response(json=json.load(f))

    work_item_links = client.get_all_work_item_links(
        "MyWorkItemId", include="workitem"
    )
    query = {
        "fields[linkedworkitems]": "id,role,suspect",
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
    with open(TEST_RESPONSES / "get_linked_work_items_next_page.json") as f:
        httpx_mock.add_response(json=json.load(f))
    with open(TEST_RESPONSES / "get_linked_work_items_no_next_page.json") as f:
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

    assert req.method == "DELETE"
    with open(TEST_REQUESTS / "delete_work_item_link.json") as f:
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

    assert req.method == "DELETE"
    with open(TEST_REQUESTS / "delete_work_item_links.json") as f:
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
    with open(TEST_REQUESTS / "delete_work_item_link.json") as f:
        assert json.loads(reqs[0].content.decode()) == json.load(f)
    with open(TEST_REQUESTS / "delete_work_item_link_2.json") as f:
        assert json.loads(reqs[1].content.decode()) == json.load(f)


def test_create_work_item_link(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "created_work_item_links.json") as f:
        httpx_mock.add_response(201, json=json.load(f))

    client.create_work_item_link(
        polarion_api.WorkItemLink(
            "MyWorkItemId", "MyWorkItemId2", "relates_to", True
        )
    )

    req = httpx_mock.get_request()

    assert req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/linkedworkitems")
    with open(TEST_REQUESTS / "post_work_item_link.json") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected


def test_create_work_item_links_different_primaries(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "created_work_item_links.json") as f:
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

    with open(TEST_REQUESTS / "post_work_item_link.json") as f:
        expected = json.load(f)

    assert json.loads(reqs[0].content.decode()) == expected
    assert json.loads(reqs[1].content.decode()) == expected


def test_create_work_item_links_same_primaries(
    client: polarion_api.OpenAPIPolarionProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_RESPONSES / "created_work_item_links.json") as f:
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

    assert req.method == "POST"
    with open(TEST_REQUESTS / "post_work_item_links.json") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected
