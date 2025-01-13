# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="DocumentsSingleGetResponseDataAttributesOutlineNumbering"
)


@_attrs_define
class DocumentsSingleGetResponseDataAttributesOutlineNumbering:
    """
    Attributes:
        prefix (Union[Unset, str]):  Example: ABC.
    """

    prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prefix = d.pop("prefix", UNSET)

        documents_single_get_response_data_attributes_outline_numbering_obj = (
            cls(
                prefix=prefix,
            )
        )

        documents_single_get_response_data_attributes_outline_numbering_obj.additional_properties = (
            d
        )
        return (
            documents_single_get_response_data_attributes_outline_numbering_obj
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
