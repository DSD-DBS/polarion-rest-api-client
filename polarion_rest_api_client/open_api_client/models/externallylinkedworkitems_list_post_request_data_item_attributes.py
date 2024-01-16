# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ExternallylinkedworkitemsListPostRequestDataItemAttributes"
)


@_attrs_define
class ExternallylinkedworkitemsListPostRequestDataItemAttributes:
    """
    Attributes:
        role (Union[Unset, str]):  Example: relates_to.
        work_item_uri (Union[Unset, str]):
    """

    role: Union[Unset, str] = UNSET
    work_item_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        role = self.role

        work_item_uri = self.work_item_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if work_item_uri is not UNSET:
            field_dict["workItemURI"] = work_item_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = d.pop("role", UNSET)

        work_item_uri = d.pop("workItemURI", UNSET)

        externallylinkedworkitems_list_post_request_data_item_attributes_obj = cls(
            role=role,
            work_item_uri=work_item_uri,
        )

        externallylinkedworkitems_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return externallylinkedworkitems_list_post_request_data_item_attributes_obj

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
