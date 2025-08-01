# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="TestparameterDefinitionsListGetResponseDataItemMetaErrorsItemSourceResource",
)


@_attrs_define
class TestparameterDefinitionsListGetResponseDataItemMetaErrorsItemSourceResource:
    """Resource causing the error.

    Attributes:
        id (Union[Unset, str]):  Example: MyProjectId/id.
        type_ (Union[Unset, str]):  Example: type.
    """

    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        testparameter_definitions_list_get_response_data_item_meta_errors_item_source_resource_obj = cls(
            id=id,
            type_=type_,
        )

        testparameter_definitions_list_get_response_data_item_meta_errors_item_source_resource_obj.additional_properties = d
        return testparameter_definitions_list_get_response_data_item_meta_errors_item_source_resource_obj

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
