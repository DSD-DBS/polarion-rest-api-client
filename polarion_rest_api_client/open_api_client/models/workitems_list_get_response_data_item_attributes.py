# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitems_list_get_response_data_item_attributes_description import (
        WorkitemsListGetResponseDataItemAttributesDescription,
    )
    from ..models.workitems_list_get_response_data_item_attributes_hyperlinks_item import (
        WorkitemsListGetResponseDataItemAttributesHyperlinksItem,
    )


T = TypeVar("T", bound="WorkitemsListGetResponseDataItemAttributes")


@_attrs_define
class WorkitemsListGetResponseDataItemAttributes:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        description (Union[Unset, WorkitemsListGetResponseDataItemAttributesDescription]):
        due_date (Union[Unset, datetime.date]):  Example: 1970-01-01.
        hyperlinks (Union[Unset, List['WorkitemsListGetResponseDataItemAttributesHyperlinksItem']]):
        id (Union[Unset, str]):  Example: MyWorkItemId.
        initial_estimate (Union[Unset, str]):  Example: 5 1/2d.
        outline_number (Union[Unset, str]):  Example: 1.11.
        planned_end (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        planned_start (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        priority (Union[Unset, str]):  Example: 90.0.
        remaining_estimate (Union[Unset, str]):  Example: 5 1/2d.
        resolution (Union[Unset, str]):  Example: done.
        resolved_on (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        severity (Union[Unset, str]):  Example: blocker.
        status (Union[Unset, str]):  Example: open.
        time_spent (Union[Unset, str]):  Example: 5 1/2d.
        title (Union[Unset, str]):  Example: Title.
        type (Union[Unset, str]):  Example: task.
        updated (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
    """

    created: Union[Unset, datetime.datetime] = UNSET
    description: Union[
        Unset, "WorkitemsListGetResponseDataItemAttributesDescription"
    ] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    hyperlinks: Union[
        Unset, List["WorkitemsListGetResponseDataItemAttributesHyperlinksItem"]
    ] = UNSET
    id: Union[Unset, str] = UNSET
    initial_estimate: Union[Unset, str] = UNSET
    outline_number: Union[Unset, str] = UNSET
    planned_end: Union[Unset, datetime.datetime] = UNSET
    planned_start: Union[Unset, datetime.datetime] = UNSET
    priority: Union[Unset, str] = UNSET
    remaining_estimate: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    resolved_on: Union[Unset, datetime.datetime] = UNSET
    severity: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    time_spent: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        hyperlinks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hyperlinks, Unset):
            hyperlinks = []
            for hyperlinks_item_data in self.hyperlinks:
                hyperlinks_item = hyperlinks_item_data.to_dict()
                hyperlinks.append(hyperlinks_item)

        id = self.id

        initial_estimate = self.initial_estimate

        outline_number = self.outline_number

        planned_end: Union[Unset, str] = UNSET
        if not isinstance(self.planned_end, Unset):
            planned_end = self.planned_end.isoformat()

        planned_start: Union[Unset, str] = UNSET
        if not isinstance(self.planned_start, Unset):
            planned_start = self.planned_start.isoformat()

        priority = self.priority

        remaining_estimate = self.remaining_estimate

        resolution = self.resolution

        resolved_on: Union[Unset, str] = UNSET
        if not isinstance(self.resolved_on, Unset):
            resolved_on = self.resolved_on.isoformat()

        severity = self.severity

        status = self.status

        time_spent = self.time_spent

        title = self.title

        type = self.type

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if hyperlinks is not UNSET:
            field_dict["hyperlinks"] = hyperlinks
        if id is not UNSET:
            field_dict["id"] = id
        if initial_estimate is not UNSET:
            field_dict["initialEstimate"] = initial_estimate
        if outline_number is not UNSET:
            field_dict["outlineNumber"] = outline_number
        if planned_end is not UNSET:
            field_dict["plannedEnd"] = planned_end
        if planned_start is not UNSET:
            field_dict["plannedStart"] = planned_start
        if priority is not UNSET:
            field_dict["priority"] = priority
        if remaining_estimate is not UNSET:
            field_dict["remainingEstimate"] = remaining_estimate
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if resolved_on is not UNSET:
            field_dict["resolvedOn"] = resolved_on
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitems_list_get_response_data_item_attributes_description import (
            WorkitemsListGetResponseDataItemAttributesDescription,
        )
        from ..models.workitems_list_get_response_data_item_attributes_hyperlinks_item import (
            WorkitemsListGetResponseDataItemAttributesHyperlinksItem,
        )

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _description = d.pop("description", UNSET)
        description: Union[
            Unset, WorkitemsListGetResponseDataItemAttributesDescription
        ]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = WorkitemsListGetResponseDataItemAttributesDescription.from_dict(
                _description
            )

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        hyperlinks = []
        _hyperlinks = d.pop("hyperlinks", UNSET)
        for hyperlinks_item_data in _hyperlinks or []:
            hyperlinks_item = WorkitemsListGetResponseDataItemAttributesHyperlinksItem.from_dict(
                hyperlinks_item_data
            )

            hyperlinks.append(hyperlinks_item)

        id = d.pop("id", UNSET)

        initial_estimate = d.pop("initialEstimate", UNSET)

        outline_number = d.pop("outlineNumber", UNSET)

        _planned_end = d.pop("plannedEnd", UNSET)
        planned_end: Union[Unset, datetime.datetime]
        if isinstance(_planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = isoparse(_planned_end)

        _planned_start = d.pop("plannedStart", UNSET)
        planned_start: Union[Unset, datetime.datetime]
        if isinstance(_planned_start, Unset):
            planned_start = UNSET
        else:
            planned_start = isoparse(_planned_start)

        priority = d.pop("priority", UNSET)

        remaining_estimate = d.pop("remainingEstimate", UNSET)

        resolution = d.pop("resolution", UNSET)

        _resolved_on = d.pop("resolvedOn", UNSET)
        resolved_on: Union[Unset, datetime.datetime]
        if isinstance(_resolved_on, Unset):
            resolved_on = UNSET
        else:
            resolved_on = isoparse(_resolved_on)

        severity = d.pop("severity", UNSET)

        status = d.pop("status", UNSET)

        time_spent = d.pop("timeSpent", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        workitems_list_get_response_data_item_attributes_obj = cls(
            created=created,
            description=description,
            due_date=due_date,
            hyperlinks=hyperlinks,
            id=id,
            initial_estimate=initial_estimate,
            outline_number=outline_number,
            planned_end=planned_end,
            planned_start=planned_start,
            priority=priority,
            remaining_estimate=remaining_estimate,
            resolution=resolution,
            resolved_on=resolved_on,
            severity=severity,
            status=status,
            time_spent=time_spent,
            title=title,
            type=type,
            updated=updated,
        )

        workitems_list_get_response_data_item_attributes_obj.additional_properties = (
            d
        )
        return workitems_list_get_response_data_item_attributes_obj

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
