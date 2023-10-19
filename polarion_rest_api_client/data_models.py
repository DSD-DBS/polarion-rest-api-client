# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Data model classes returned by the client."""
from __future__ import annotations

import dataclasses
import hashlib
import json
import typing as t


class WorkItem:
    """A data class containing all relevant data of a Polarion WorkItem."""

    id: str | None = None
    title: str | None = None
    description_type: str | None = None
    description: str | None = None
    type: str | None = None
    status: str | None = None
    additional_attributes: dict[str, t.Any] = {}
    linked_work_items: list[WorkItemLink] = []
    attachments: list[WorkItemAttachment] = []
    _checksum: str | None = None

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
        **kwargs,
    ):
        self.id = id
        self.title = title
        self.description_type = description_type
        self.description = description
        self.type = type
        self.status = status
        self.additional_attributes = (additional_attributes or {}) | kwargs
        self._checksum = self.additional_attributes.pop("checksum", None)
        self.linked_work_items = linked_work_items or []
        self.attachments = attachments or []

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

        for at in data["attachments"]:
            del at["id"]

        data = dict(sorted(data.items()))

        converted = json.dumps(data).encode("utf8")
        self._checksum = hashlib.sha256(converted).hexdigest()
        return self._checksum

    def get_current_checksum(self) -> str | None:
        """Return the checksum currently set without calculation."""
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
