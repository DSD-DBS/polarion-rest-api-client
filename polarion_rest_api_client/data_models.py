# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Data model classes returned by the client."""
from __future__ import annotations

import dataclasses
import typing as t


@dataclasses.dataclass
class WorkItem:
    """A data class containing all relevant data of a Polarion WorkItem."""

    id: str | None = None
    title: str | None = None
    description_type: str | None = None
    description: str | None = None
    type: str | None = None
    status: str | None = None
    additional_attributes: dict[str, t.Any] = dataclasses.field(
        default_factory=dict
    )


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
