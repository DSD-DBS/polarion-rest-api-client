# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import pytest

import polarion_rest_api_client as polarion_api
from tests import CustomWorkItem


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