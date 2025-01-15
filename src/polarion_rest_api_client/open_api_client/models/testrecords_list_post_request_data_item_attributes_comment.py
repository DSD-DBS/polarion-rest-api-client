# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrecords_list_post_request_data_item_attributes_comment_type import (
    TestrecordsListPostRequestDataItemAttributesCommentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrecordsListPostRequestDataItemAttributesComment")


@_attrs_define
class TestrecordsListPostRequestDataItemAttributesComment:
    """Attributes type (Union[Unset,
    TestrecordsListPostRequestDataItemAttributesCommentType]):

    value (Union[Unset, str]):  Example: My text value.
    """

    type: Unset | TestrecordsListPostRequestDataItemAttributesCommentType = (
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
        type: Unset | TestrecordsListPostRequestDataItemAttributesCommentType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrecordsListPostRequestDataItemAttributesCommentType(
                _type
            )

        value = d.pop("value", UNSET)

        testrecords_list_post_request_data_item_attributes_comment_obj = cls(
            type=type,
            value=value,
        )

        testrecords_list_post_request_data_item_attributes_comment_obj.additional_properties = d
        return testrecords_list_post_request_data_item_attributes_comment_obj

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
