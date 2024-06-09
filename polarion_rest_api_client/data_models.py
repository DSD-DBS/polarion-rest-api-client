# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Data model classes returned by the client."""
from __future__ import annotations

import base64
import dataclasses
import datetime
import enum
import hashlib
import json
import typing as t


@dataclasses.dataclass
class StatusItem:
    """A parent data class for WorkItem and Document."""

    id: str | None = None
    type: str | None = None
    status: str | None = None
    _checksum: str | None = dataclasses.field(init=False, default=None)

    def __eq__(self, other: object) -> bool:
        """Compare only StatusItem attributes."""
        if not isinstance(other, StatusItem):
            return NotImplemented
        if self.get_current_checksum() is None:
            self.calculate_checksum()
        if other.get_current_checksum() is None:
            other.calculate_checksum()

        return self.get_current_checksum() == other.get_current_checksum()

    def to_dict(self) -> dict[str, t.Any]:
        """Return the content of the StatusItem as dictionary."""
        return {
            "id": self.id,
            "type": self.type,
            "status": self.status,
            "checksum": self._checksum,
        }

    def calculate_checksum(self) -> str:
        """Calculate and return a checksum for this StatusItem.

        In addition, the checksum will be written to self._checksum.
        """
        data = self.to_dict()
        del data["checksum"]
        del data["id"]

        data = dict(sorted(data.items()))

        converted = json.dumps(data).encode("utf8")
        self._checksum = hashlib.sha256(converted).hexdigest()
        return self._checksum

    def get_current_checksum(self) -> str | None:
        """Return the checksum currently set without calculation."""
        return self._checksum


class WorkItem(StatusItem):
    """A data class containing all relevant data of a Polarion WorkItem."""

    title: str | None = None
    description_type: str | None = None
    description: str | None = None
    additional_attributes: dict[str, t.Any] = {}
    linked_work_items: list[WorkItemLink] = []
    attachments: list[WorkItemAttachment] = []
    linked_work_items_truncated: bool = False
    attachments_truncated: bool = False

    def __init__(
        self,
        id: str | None = None,
        title: str | None = None,
        description_type: str | None = None,
        description: str | None = None,
        type: str | None = None,
        status: str | None = None,
        additional_attributes: dict[str, t.Any] | None = None,
        linked_work_items: list[WorkItemLink] | None = None,
        attachments: list[WorkItemAttachment] | None = None,
        linked_work_items_truncated: bool = False,
        attachments_truncated: bool = False,
        **kwargs,
    ):
        super().__init__(id, type, status)
        self.title = title
        self.description_type = description_type
        self.description = description
        self.additional_attributes = (additional_attributes or {}) | kwargs
        self._checksum = self.additional_attributes.pop("checksum", None)
        self.linked_work_items = linked_work_items or []
        self.attachments = attachments or []
        self.linked_work_items_truncated = linked_work_items_truncated
        self.attachments_truncated = attachments_truncated

    def __getattribute__(self, item: str) -> t.Any:
        """Return all non WorkItem attributes from additional_properties."""
        if item.startswith("__") or item in dir(WorkItem):
            return super().__getattribute__(item)
        return self.additional_attributes.get(item)

    def __setattr__(self, key: str, value: t.Any):
        """Set all non WorkItem attributes in additional_properties."""
        if key in dir(WorkItem):
            super().__setattr__(key, value)
        else:
            self.additional_attributes[key] = value

    def __eq__(self, other: object) -> bool:
        """Compare only WorkItem attributes."""
        if not isinstance(other, WorkItem):
            return NotImplemented
        if self.get_current_checksum() is None:
            self.calculate_checksum()
        if other.get_current_checksum() is None:
            other.calculate_checksum()

        return self.get_current_checksum() == other.get_current_checksum()

    def to_dict(self) -> dict[str, t.Any]:
        """Return the content of the WorkItem as dictionary."""
        sorted_links = sorted(
            self.linked_work_items,
            key=lambda x: f"{x.role}/{x.secondary_work_item_project}/{x.secondary_work_item_id}",  # pylint: disable=line-too-long
        )

        sorted_attachments = sorted(
            self.attachments, key=lambda x: x.file_name or ""
        )

        return {
            "id": self.id,
            "title": self.title,
            "description_type": self.description_type,
            "description": self.description,
            "type": self.type,
            "status": self.status,
            "additional_attributes": dict(
                sorted(self.additional_attributes.items())
            ),
            "checksum": self._checksum,
            "linked_work_items": [
                dataclasses.asdict(lwi) for lwi in sorted_links
            ],
            "attachments": [
                dataclasses.asdict(at) for at in sorted_attachments
            ],
        }

    def calculate_checksum(self) -> str:
        """Calculate and return a checksum for this WorkItem.

        In addition, the checksum will be written to self._checksum.
        """
        data = self.to_dict()
        del data["checksum"]
        del data["id"]

        for attachment in data["attachments"]:
            try:
                attachment["content_bytes"] = base64.b64encode(
                    attachment["content_bytes"]
                ).decode("utf8")
            except TypeError:
                pass

            del attachment["id"]

        data = dict(sorted(data.items()))

        converted = json.dumps(data).encode("utf8")
        self._checksum = hashlib.sha256(converted).hexdigest()
        return self._checksum


@dataclasses.dataclass
class WorkItemLink:
    """A link between multiple Polarion WorkItems.

    The primary_work_item_id is the ID of the owner of the link, the
    secondary_work_item_id represents the linked workitem.
    """

    primary_work_item_id: str
    secondary_work_item_id: str
    role: str
    suspect: bool | None = None
    secondary_work_item_project: str | None = (
        None  # Use to set differing project
    )


@dataclasses.dataclass
class WorkItemAttachment:
    """An Attachment of a WorkItem."""

    work_item_id: str
    id: str
    title: str | None = None
    content_bytes: bytes | None = None
    mime_type: str | None = None
    file_name: str | None = None


class Document(StatusItem):
    """A data class containing all relevant data of a Polarion Document."""

    module_folder: str | None = None
    module_name: str | None = None
    home_page_content: TextContent | None = None

    def __init__(
        self,
        id: str | None = None,
        module_folder: str | None = None,
        module_name: str | None = None,
        type: str | None = None,
        status: str | None = None,
        home_page_content: TextContent | None = None,
    ):
        super().__init__(id, type, status)
        self.module_folder = module_folder
        self.module_name = module_name
        self.home_page_content = home_page_content


@dataclasses.dataclass
class TestRun(StatusItem):
    """A data class for all data of a test run."""

    title: str | None = None
    home_page_content: TextContent | None = None
    finished_on: datetime.datetime | None = None
    group_id: str | None = None
    id_prefix: str | None = None
    is_template: bool | None = None
    keep_in_history: bool | None = None
    query: str | None = None
    use_report_from_template: bool | None = None
    select_test_cases_by: SelectTestCasesBy | None = None
    additional_attributes: dict[str, t.Any] = dataclasses.field(
        default_factory=dict
    )


@dataclasses.dataclass
class TestRecord:
    """A data class for test record data."""

    test_run_id: str
    work_item_project_id: str
    work_item_id: str
    work_item_revision: str | None = None
    iteration: int = -1
    duration: float = -1
    result: str | None = None
    comment: TextContent | None = None
    executed: datetime.datetime | None = None
    additional_attributes: dict[str, t.Any] = dataclasses.field(
        default_factory=dict
    )


@dataclasses.dataclass
class TextContent:
    """A data class for home_page_content of a Polarion Document."""

    type: str | None = None
    value: str | None = None


class SelectTestCasesBy(str, enum.Enum):
    """Test case selection mode enum."""

    AUTOMATEDPROCESS = "automatedProcess"
    DYNAMICLIVEDOC = "dynamicLiveDoc"
    DYNAMICQUERYRESULT = "dynamicQueryResult"
    MANUALSELECTION = "manualSelection"
    STATICLIVEDOC = "staticLiveDoc"
    STATICQUERYRESULT = "staticQueryResult"
