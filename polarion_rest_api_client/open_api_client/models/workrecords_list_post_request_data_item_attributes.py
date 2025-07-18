# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkrecordsListPostRequestDataItemAttributes")


@_attrs_define
class WorkrecordsListPostRequestDataItemAttributes:
    """
    Attributes:
        comment (Union[Unset, str]):  Example: Comment.
        date (Union[Unset, datetime.date]):  Example: 1970-01-01.
        time_spent (Union[Unset, str]):  Example: 5 1/2d.
        type_ (Union[Unset, str]):  Example: task.
    """

    comment: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    time_spent: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_spent = self.time_spent

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        time_spent = d.pop("timeSpent", UNSET)

        type_ = d.pop("type", UNSET)

        workrecords_list_post_request_data_item_attributes_obj = cls(
            comment=comment,
            date=date,
            time_spent=time_spent,
            type_=type_,
        )

        workrecords_list_post_request_data_item_attributes_obj.additional_properties = d
        return workrecords_list_post_request_data_item_attributes_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
