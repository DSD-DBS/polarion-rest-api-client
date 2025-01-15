# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plans_list_delete_request_data_item_type import (
    PlansListDeleteRequestDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlansListDeleteRequestDataItem")


@_attrs_define
class PlansListDeleteRequestDataItem:
    """Attributes type (Union[Unset, PlansListDeleteRequestDataItemType]):

    id (Union[Unset, str]):  Example: MyProjectId/MyPlanId.
    """

    type: Unset | PlansListDeleteRequestDataItemType = UNSET
    id: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Unset | PlansListDeleteRequestDataItemType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PlansListDeleteRequestDataItemType(_type)

        id = d.pop("id", UNSET)

        plans_list_delete_request_data_item_obj = cls(
            type=type,
            id=id,
        )

        plans_list_delete_request_data_item_obj.additional_properties = d
        return plans_list_delete_request_data_item_obj

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
