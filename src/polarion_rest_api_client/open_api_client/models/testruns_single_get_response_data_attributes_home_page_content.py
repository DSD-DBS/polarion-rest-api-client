# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testruns_single_get_response_data_attributes_home_page_content_type import (
    TestrunsSingleGetResponseDataAttributesHomePageContentType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="TestrunsSingleGetResponseDataAttributesHomePageContent"
)


@_attrs_define
class TestrunsSingleGetResponseDataAttributesHomePageContent:
    """Attributes type (Union[Unset,
    TestrunsSingleGetResponseDataAttributesHomePageContentType]):

    value (Union[Unset, str]):  Example: My text value.
    """

    type: (
        Unset | TestrunsSingleGetResponseDataAttributesHomePageContentType
    ) = UNSET
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
        type: (
            Unset | TestrunsSingleGetResponseDataAttributesHomePageContentType
        )
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunsSingleGetResponseDataAttributesHomePageContentType(
                _type
            )

        value = d.pop("value", UNSET)

        testruns_single_get_response_data_attributes_home_page_content_obj = (
            cls(
                type=type,
                value=value,
            )
        )

        testruns_single_get_response_data_attributes_home_page_content_obj.additional_properties = d
        return (
            testruns_single_get_response_data_attributes_home_page_content_obj
        )

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
