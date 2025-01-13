# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plans_list_post_request_data_item_attributes_home_page_content_type import (
    PlansListPostRequestDataItemAttributesHomePageContentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlansListPostRequestDataItemAttributesHomePageContent")


@_attrs_define
class PlansListPostRequestDataItemAttributesHomePageContent:
    """
    Attributes:
        type (Union[Unset, PlansListPostRequestDataItemAttributesHomePageContentType]):
        value (Union[Unset, str]):  Example: My text value.
    """

    type: Union[
        Unset, PlansListPostRequestDataItemAttributesHomePageContentType
    ] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[
            Unset, PlansListPostRequestDataItemAttributesHomePageContentType
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PlansListPostRequestDataItemAttributesHomePageContentType(
                _type
            )

        value = d.pop("value", UNSET)

        plans_list_post_request_data_item_attributes_home_page_content_obj = (
            cls(
                type=type,
                value=value,
            )
        )

        plans_list_post_request_data_item_attributes_home_page_content_obj.additional_properties = (
            d
        )
        return (
            plans_list_post_request_data_item_attributes_home_page_content_obj
        )

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
