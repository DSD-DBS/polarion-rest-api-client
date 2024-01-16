# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedoslcresourcesListPostRequestDataItemAttributes")


@_attrs_define
class LinkedoslcresourcesListPostRequestDataItemAttributes:
    """
    Attributes:
        label (Union[Unset, str]):  Example: Label.
        role (Union[Unset, str]):  Example: http://open-services.net/ns/cm#relatedChangeRequest.
        uri (Union[Unset, str]):  Example: Uri.
    """

    label: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        role = self.role

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if role is not UNSET:
            field_dict["role"] = role
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        role = d.pop("role", UNSET)

        uri = d.pop("uri", UNSET)

        linkedoslcresources_list_post_request_data_item_attributes_obj = cls(
            label=label,
            role=role,
            uri=uri,
        )

        linkedoslcresources_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return linkedoslcresources_list_post_request_data_item_attributes_obj

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
