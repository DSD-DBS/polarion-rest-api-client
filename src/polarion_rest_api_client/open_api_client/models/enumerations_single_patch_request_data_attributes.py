# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enumerations_single_patch_request_data_attributes_options_item import (
        EnumerationsSinglePatchRequestDataAttributesOptionsItem,
    )


T = TypeVar("T", bound="EnumerationsSinglePatchRequestDataAttributes")


@_attrs_define
class EnumerationsSinglePatchRequestDataAttributes:
    """
    Attributes:
        options (Union[Unset, List['EnumerationsSinglePatchRequestDataAttributesOptionsItem']]):
    """

    options: Union[
        Unset, List["EnumerationsSinglePatchRequestDataAttributesOptionsItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enumerations_single_patch_request_data_attributes_options_item import (
            EnumerationsSinglePatchRequestDataAttributesOptionsItem,
        )

        d = src_dict.copy()
        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = EnumerationsSinglePatchRequestDataAttributesOptionsItem.from_dict(
                options_item_data
            )

            options.append(options_item)

        enumerations_single_patch_request_data_attributes_obj = cls(
            options=options,
        )

        enumerations_single_patch_request_data_attributes_obj.additional_properties = (
            d
        )
        return enumerations_single_patch_request_data_attributes_obj

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
