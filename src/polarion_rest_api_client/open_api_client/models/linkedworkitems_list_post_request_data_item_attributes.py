# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedworkitemsListPostRequestDataItemAttributes")


@_attrs_define
class LinkedworkitemsListPostRequestDataItemAttributes:
    """
    Attributes:
        revision (Union[Unset, str]):  Example: 1234.
        role (Union[Unset, str]):  Example: relates_to.
        suspect (Union[Unset, bool]):
    """

    revision: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    suspect: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        revision = self.revision

        role = self.role

        suspect = self.suspect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revision is not UNSET:
            field_dict["revision"] = revision
        if role is not UNSET:
            field_dict["role"] = role
        if suspect is not UNSET:
            field_dict["suspect"] = suspect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        revision = d.pop("revision", UNSET)

        role = d.pop("role", UNSET)

        suspect = d.pop("suspect", UNSET)

        linkedworkitems_list_post_request_data_item_attributes_obj = cls(
            revision=revision,
            role=role,
            suspect=suspect,
        )

        linkedworkitems_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return linkedworkitems_list_post_request_data_item_attributes_obj

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
