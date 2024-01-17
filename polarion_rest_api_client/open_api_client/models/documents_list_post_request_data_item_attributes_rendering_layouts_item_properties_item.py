# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem",
)


@_attrs_define
class DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem:
    """
    Attributes:
        key (Union[Unset, str]):  Example: fieldsAtStart.
        value (Union[Unset, str]):  Example: id.
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        documents_list_post_request_data_item_attributes_rendering_layouts_item_properties_item_obj = cls(
            key=key,
            value=value,
        )

        documents_list_post_request_data_item_attributes_rendering_layouts_item_properties_item_obj.additional_properties = (
            d
        )
        return documents_list_post_request_data_item_attributes_rendering_layouts_item_properties_item_obj

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
