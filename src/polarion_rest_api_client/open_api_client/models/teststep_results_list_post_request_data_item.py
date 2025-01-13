# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.teststep_results_list_post_request_data_item_type import (
    TeststepResultsListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststep_results_list_post_request_data_item_attributes import (
        TeststepResultsListPostRequestDataItemAttributes,
    )


T = TypeVar("T", bound="TeststepResultsListPostRequestDataItem")


@_attrs_define
class TeststepResultsListPostRequestDataItem:
    """Attributes type (Union[Unset,
    TeststepResultsListPostRequestDataItemType]):

    attributes (Union[Unset, TeststepResultsListPostRequestDataItemAttributes]):
    """

    type: Unset | TeststepResultsListPostRequestDataItemType = UNSET
    attributes: Union[
        Unset, "TeststepResultsListPostRequestDataItemAttributes"
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
        from ..models.teststep_results_list_post_request_data_item_attributes import (
            TeststepResultsListPostRequestDataItemAttributes,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Unset | TeststepResultsListPostRequestDataItemType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TeststepResultsListPostRequestDataItemType(_type)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | TeststepResultsListPostRequestDataItemAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                TeststepResultsListPostRequestDataItemAttributes.from_dict(
                    _attributes
                )
            )

        teststep_results_list_post_request_data_item_obj = cls(
            type=type,
            attributes=attributes,
        )

        teststep_results_list_post_request_data_item_obj.additional_properties = d
        return teststep_results_list_post_request_data_item_obj

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
