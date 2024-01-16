# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkrecordsListGetResponseDataItemAttributes")


@_attrs_define
class WorkrecordsListGetResponseDataItemAttributes:
    """
    Attributes:
        comment (Union[Unset, str]):  Example: Comment.
        date (Union[Unset, datetime.date]):  Example: 1970-01-01.
        id (Union[Unset, str]):
        time_spent (Union[Unset, str]):  Example: 5 1/2d.
        type (Union[Unset, str]):  Example: task.
    """

    comment: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    id: Union[Unset, str] = UNSET
    time_spent: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        comment = self.comment

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        id = self.id

        time_spent = self.time_spent

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        id = d.pop("id", UNSET)

        time_spent = d.pop("timeSpent", UNSET)

        type = d.pop("type", UNSET)

        workrecords_list_get_response_data_item_attributes_obj = cls(
            comment=comment,
            date=date,
            id=id,
            time_spent=time_spent,
            type=type,
        )

        workrecords_list_get_response_data_item_attributes_obj.additional_properties = (
            d
        )
        return workrecords_list_get_response_data_item_attributes_obj

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
