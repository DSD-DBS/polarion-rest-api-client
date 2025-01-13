# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enumerations_list_post_request_data_item_attributes_options_item import (
        EnumerationsListPostRequestDataItemAttributesOptionsItem,
    )


T = TypeVar("T", bound="EnumerationsListPostRequestDataItemAttributes")


@_attrs_define
class EnumerationsListPostRequestDataItemAttributes:
    """
    Attributes:
        enum_context (Union[Unset, str]):  Example: id.
        enum_name (Union[Unset, str]):  Example: id.
        options (Union[Unset, List['EnumerationsListPostRequestDataItemAttributesOptionsItem']]):
        target_type (Union[Unset, str]):  Example: id.
    """

    enum_context: Union[Unset, str] = UNSET
    enum_name: Union[Unset, str] = UNSET
    options: Union[
        Unset, List["EnumerationsListPostRequestDataItemAttributesOptionsItem"]
    ] = UNSET
    target_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        enum_context = self.enum_context

        enum_name = self.enum_name

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        target_type = self.target_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum_context is not UNSET:
            field_dict["enumContext"] = enum_context
        if enum_name is not UNSET:
            field_dict["enumName"] = enum_name
        if options is not UNSET:
            field_dict["options"] = options
        if target_type is not UNSET:
            field_dict["targetType"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enumerations_list_post_request_data_item_attributes_options_item import (
            EnumerationsListPostRequestDataItemAttributesOptionsItem,
        )

        d = src_dict.copy()
        enum_context = d.pop("enumContext", UNSET)

        enum_name = d.pop("enumName", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = EnumerationsListPostRequestDataItemAttributesOptionsItem.from_dict(
                options_item_data
            )

            options.append(options_item)

        target_type = d.pop("targetType", UNSET)

        enumerations_list_post_request_data_item_attributes_obj = cls(
            enum_context=enum_context,
            enum_name=enum_name,
            options=options,
            target_type=target_type,
        )

        enumerations_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return enumerations_list_post_request_data_item_attributes_obj

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
