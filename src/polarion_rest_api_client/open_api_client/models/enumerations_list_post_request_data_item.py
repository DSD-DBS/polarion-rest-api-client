# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enumerations_list_post_request_data_item_type import (
    EnumerationsListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enumerations_list_post_request_data_item_attributes import (
        EnumerationsListPostRequestDataItemAttributes,
    )


T = TypeVar("T", bound="EnumerationsListPostRequestDataItem")


@_attrs_define
class EnumerationsListPostRequestDataItem:
    """Attributes
    type (Union[Unset, EnumerationsListPostRequestDataItemType]):
    attributes (Union[Unset, EnumerationsListPostRequestDataItemAttributes]):
    """

    type: Unset | EnumerationsListPostRequestDataItemType = UNSET
    attributes: Union[
        Unset, "EnumerationsListPostRequestDataItemAttributes"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        from ..models.enumerations_list_post_request_data_item_attributes import (
            EnumerationsListPostRequestDataItemAttributes,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Unset | EnumerationsListPostRequestDataItemType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EnumerationsListPostRequestDataItemType(_type)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | EnumerationsListPostRequestDataItemAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                EnumerationsListPostRequestDataItemAttributes.from_dict(
                    _attributes
                )
            )

        enumerations_list_post_request_data_item_obj = cls(
            type=type,
            attributes=attributes,
        )

        enumerations_list_post_request_data_item_obj.additional_properties = d
        return enumerations_list_post_request_data_item_obj

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
