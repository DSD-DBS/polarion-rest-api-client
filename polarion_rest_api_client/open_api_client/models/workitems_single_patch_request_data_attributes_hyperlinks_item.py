# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="WorkitemsSinglePatchRequestDataAttributesHyperlinksItem"
)


@_attrs_define
class WorkitemsSinglePatchRequestDataAttributesHyperlinksItem:
    """
    Attributes:
        role (Union[Unset, str]):  Example: ref_ext.
        uri (Union[Unset, str]):  Example: https://polarion.plm.automation.siemens.com.
    """

    role: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        role = self.role

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = d.pop("role", UNSET)

        uri = d.pop("uri", UNSET)

        workitems_single_patch_request_data_attributes_hyperlinks_item_obj = (
            cls(
                role=role,
                uri=uri,
            )
        )

        workitems_single_patch_request_data_attributes_hyperlinks_item_obj.additional_properties = (
            d
        )
        return (
            workitems_single_patch_request_data_attributes_hyperlinks_item_obj
        )

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
