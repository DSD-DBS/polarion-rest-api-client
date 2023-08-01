# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Data model classes returned by the client."""
from __future__ import annotations

import dataclasses
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

    def __init__(
        self,
        id: str | None = None,
        title: str | None = None,
        description_type: str | None = None,
        description: str | None = None,
        type: str | None = None,
        status: str | None = None,
        additional_attributes: dict[str, t.Any] | None = None,
        **kwargs,
    ):
        if not additional_attributes:
            additional_attributes = kwargs
        else:
            additional_attributes.update(kwargs)

        self.id = id
        self.title = title
        self.description_type = description_type
        self.description = description
        self.type = type
        self.status = status
        self.additional_attributes = additional_attributes

    def __getattribute__(self, item: str) -> t.Any:
        """Return all non WorkItem attributes from additional_properties."""
        if item.startswith("__"):
            return super(WorkItem, self).__getattribute__(item)

        if item in dir(WorkItem):
            return super(WorkItem, self).__getattribute__(item)

        return self.additional_attributes.get(item)

    def __setattr__(self, key: str, value: t.Any):
        """Set all non WorkItem attributes in additional_properties."""
        if key in dir(WorkItem):
            super(WorkItem, self).__setattr__(key, value)
        else:
            self.additional_attributes[key] = value

    def __eq__(self, other: object) -> bool:
        """Compare only WorkItem attributes."""
        if not isinstance(other, WorkItem):
            return NotImplemented
        return {
            k: v for k, v in self.__dict__.items() if k in dir(WorkItem)
        } == {k: v for k, v in other.__dict__.items() if k in dir(WorkItem)}


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
