# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import pytest

import polarion_rest_api_client as polarion_api
from tests import TEST_WIA_CREATED_RESPONSE, CustomWorkItem


@pytest.fixture(name="client")
def fixture_client():
    yield polarion_api.OpenAPIPolarionProjectClient(
        project_id="PROJ",
        delete_polarion_work_items=False,
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )


@pytest.fixture(name="client_custom_work_item")
def fixture_client_custom_work_item():
    yield polarion_api.OpenAPIPolarionProjectClient(
        project_id="PROJ",
        delete_polarion_work_items=False,
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
        custom_work_item=CustomWorkItem,
    )


@pytest.fixture(name="work_item")
def fixture_dummy_work_item():
    return polarion_api.WorkItem(
        title="Title",
        description_type="text/html",
        description="My text value",
        status="open",
        type="task",
        additional_attributes={"capella_uuid": "asdfg"},
    )


@pytest.fixture(name="work_item_patch")
def fixture_dummy_work_item_patch():
    return polarion_api.WorkItem(
        id="MyWorkItemId",
        description_type="text/html",
        description="My text value",
        title="Title",
        status="open",
        additional_attributes={"capella_uuid": "qwertz"},
    )


@pytest.fixture(name="work_item_attachment")
def fixture_dummy_work_item_attachment():
    with open(TEST_WIA_CREATED_RESPONSE, encoding="utf8") as f:
        attachment_content = f.read()

    return polarion_api.WorkItemAttachment(
        "MyWorkItemId",
        "Attachment",
        "Title",
        attachment_content.encode("utf-8"),
        "text/plain",
        "test.json",
    )
