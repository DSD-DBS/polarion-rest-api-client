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

from ..models.plans_single_get_response_data_attributes_home_page_content_type import (
    PlansSingleGetResponseDataAttributesHomePageContentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlansSingleGetResponseDataAttributesHomePageContent")


@_attrs_define
class PlansSingleGetResponseDataAttributesHomePageContent:
    """
    Attributes:
        type_ (Union[Unset, PlansSingleGetResponseDataAttributesHomePageContentType]):
        value (Union[Unset, str]):  Example: My text value.
    """

    type_: Union[
        Unset, PlansSingleGetResponseDataAttributesHomePageContentType
    ] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[
            Unset, PlansSingleGetResponseDataAttributesHomePageContentType
        ]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PlansSingleGetResponseDataAttributesHomePageContentType(
                _type_
            )

        value = d.pop("value", UNSET)

        plans_single_get_response_data_attributes_home_page_content_obj = cls(
            type_=type_,
            value=value,
        )

        plans_single_get_response_data_attributes_home_page_content_obj.additional_properties = d
        return plans_single_get_response_data_attributes_home_page_content_obj

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
