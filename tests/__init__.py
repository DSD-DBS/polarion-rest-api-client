# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import pathlib

import polarion_rest_api_client as polarion_api

TEST_DATA_ROOT = pathlib.Path(__file__).parent / "data"
TEST_RESPONSES = TEST_DATA_ROOT / "mock_api_responses"
TEST_REQUESTS = TEST_DATA_ROOT / "expected_requests"

TEST_WIA_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_work_item_attachments_next_page.json"
)
TEST_WIA_NO_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_work_item_attachments_no_next_page.json"
)
TEST_WIA_CREATED_RESPONSE = (
    TEST_RESPONSES / "created_work_item_attachment.json"
)
TEST_WIA_MULTI_CREATED_RESPONSE = (
    TEST_RESPONSES / "created_work_item_attachments.json"
)

TEST_WIL_MULTI_POST_REQUEST = TEST_REQUESTS / "post_work_item_links.json"
TEST_WIL_DELETE2_REQUEST = TEST_REQUESTS / "delete_work_item_link_2.json"
TEST_WIL_DELETE_REQUEST = TEST_REQUESTS / "delete_work_item_links.json"
TEST_WIL_DELETED_REQUEST = TEST_REQUESTS / "delete_work_item_link.json"
TEST_WIL_POSTED_REQUEST = TEST_REQUESTS / "post_work_item_link.json"

TEST_WIL_CREATED_RESPONSE = TEST_RESPONSES / "created_work_item_links.json"
TEST_WIL_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_linked_work_items_next_page.json"
)
TEST_WIL_NO_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_linked_work_items_no_next_page.json"
)

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
