# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrun_comments_list_get_response_data_item_attributes_text_type import (
    TestrunCommentsListGetResponseDataItemAttributesTextType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrunCommentsListGetResponseDataItemAttributesText")


@_attrs_define
class TestrunCommentsListGetResponseDataItemAttributesText:
    """
    Attributes:
        type (Union[Unset, TestrunCommentsListGetResponseDataItemAttributesTextType]):
        value (Union[Unset, str]):  Example: My text value.
    """

    type: Union[
        Unset, TestrunCommentsListGetResponseDataItemAttributesTextType
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
            Unset, TestrunCommentsListGetResponseDataItemAttributesTextType
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunCommentsListGetResponseDataItemAttributesTextType(
                _type
            )

        value = d.pop("value", UNSET)

        testrun_comments_list_get_response_data_item_attributes_text_obj = cls(
            type=type,
            value=value,
        )

        testrun_comments_list_get_response_data_item_attributes_text_obj.additional_properties = (
            d
        )
        return testrun_comments_list_get_response_data_item_attributes_text_obj

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