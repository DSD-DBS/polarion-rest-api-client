# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.projects_single_patch_request_data_attributes_description import (
        ProjectsSinglePatchRequestDataAttributesDescription,
    )


T = TypeVar("T", bound="ProjectsSinglePatchRequestDataAttributes")


@_attrs_define
class ProjectsSinglePatchRequestDataAttributes:
    """
    Attributes:
        active (Union[Unset, bool]):
        color (Union[Unset, str]):  Example: Color.
        description (Union[Unset, ProjectsSinglePatchRequestDataAttributesDescription]):
        finish (Union[Unset, datetime.date]):  Example: 1970-01-01.
        icon (Union[Unset, str]):  Example: Icon.
        lock_work_records_date (Union[Unset, datetime.date]):  Example: 1970-01-01.
        name (Union[Unset, str]):  Example: Name.
        start (Union[Unset, datetime.date]):  Example: 1970-01-01.
        tracker_prefix (Union[Unset, str]):  Example: Tracker Prefix.
    """

    active: Union[Unset, bool] = UNSET
    color: Union[Unset, str] = UNSET
    description: Union[
        Unset, "ProjectsSinglePatchRequestDataAttributesDescription"
    ] = UNSET
    finish: Union[Unset, datetime.date] = UNSET
    icon: Union[Unset, str] = UNSET
    lock_work_records_date: Union[Unset, datetime.date] = UNSET
    name: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.date] = UNSET
    tracker_prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        active = self.active

        color = self.color

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        finish: Union[Unset, str] = UNSET
        if not isinstance(self.finish, Unset):
            finish = self.finish.isoformat()

        icon = self.icon

        lock_work_records_date: Union[Unset, str] = UNSET
        if not isinstance(self.lock_work_records_date, Unset):
            lock_work_records_date = self.lock_work_records_date.isoformat()

        name = self.name

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        tracker_prefix = self.tracker_prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if finish is not UNSET:
            field_dict["finish"] = finish
        if icon is not UNSET:
            field_dict["icon"] = icon
        if lock_work_records_date is not UNSET:
            field_dict["lockWorkRecordsDate"] = lock_work_records_date
        if name is not UNSET:
            field_dict["name"] = name
        if start is not UNSET:
            field_dict["start"] = start
        if tracker_prefix is not UNSET:
            field_dict["trackerPrefix"] = tracker_prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.projects_single_patch_request_data_attributes_description import (
            ProjectsSinglePatchRequestDataAttributesDescription,
        )

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        color = d.pop("color", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[
            Unset, ProjectsSinglePatchRequestDataAttributesDescription
        ]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                ProjectsSinglePatchRequestDataAttributesDescription.from_dict(
                    _description
                )
            )

        _finish = d.pop("finish", UNSET)
        finish: Union[Unset, datetime.date]
        if isinstance(_finish, Unset):
            finish = UNSET
        else:
            finish = isoparse(_finish).date()

        icon = d.pop("icon", UNSET)

        _lock_work_records_date = d.pop("lockWorkRecordsDate", UNSET)
        lock_work_records_date: Union[Unset, datetime.date]
        if isinstance(_lock_work_records_date, Unset):
            lock_work_records_date = UNSET
        else:
            lock_work_records_date = isoparse(_lock_work_records_date).date()

        name = d.pop("name", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.date]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start).date()

        tracker_prefix = d.pop("trackerPrefix", UNSET)

        projects_single_patch_request_data_attributes_obj = cls(
            active=active,
            color=color,
            description=description,
            finish=finish,
            icon=icon,
            lock_work_records_date=lock_work_records_date,
            name=name,
            start=start,
            tracker_prefix=tracker_prefix,
        )

        projects_single_patch_request_data_attributes_obj.additional_properties = (
            d
        )
        return projects_single_patch_request_data_attributes_obj

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
