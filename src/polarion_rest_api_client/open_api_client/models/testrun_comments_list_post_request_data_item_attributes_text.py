# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrun_comments_list_post_request_data_item_attributes_text_type import (
    TestrunCommentsListPostRequestDataItemAttributesTextType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrunCommentsListPostRequestDataItemAttributesText")


@_attrs_define
class TestrunCommentsListPostRequestDataItemAttributesText:
    """Attributes type (Union[Unset,
    TestrunCommentsListPostRequestDataItemAttributesTextType]):

    value (Union[Unset, str]):  Example: My text value.
    """

    type: Unset | TestrunCommentsListPostRequestDataItemAttributesTextType = (
        UNSET
    )
    value: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Unset | TestrunCommentsListPostRequestDataItemAttributesTextType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunCommentsListPostRequestDataItemAttributesTextType(
                _type
            )

        value = d.pop("value", UNSET)

        testrun_comments_list_post_request_data_item_attributes_text_obj = cls(
            type=type,
            value=value,
        )

        testrun_comments_list_post_request_data_item_attributes_text_obj.additional_properties = d
        return testrun_comments_list_post_request_data_item_attributes_text_obj

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
