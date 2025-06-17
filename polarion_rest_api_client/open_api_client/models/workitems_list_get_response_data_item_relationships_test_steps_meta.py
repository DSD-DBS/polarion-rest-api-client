# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="WorkitemsListGetResponseDataItemRelationshipsTestStepsMeta"
)


@_attrs_define
class WorkitemsListGetResponseDataItemRelationshipsTestStepsMeta:
    """
    Attributes:
        total_count (Union[Unset, int]):
    """

    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        workitems_list_get_response_data_item_relationships_test_steps_meta_obj = cls(
            total_count=total_count,
        )

        workitems_list_get_response_data_item_relationships_test_steps_meta_obj.additional_properties = (
            d
        )
        return workitems_list_get_response_data_item_relationships_test_steps_meta_obj

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
