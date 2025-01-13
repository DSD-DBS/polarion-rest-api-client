# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        calculated_offset (Union[Unset, int]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):
    """

    calculated_offset: Union[Unset, int] = UNSET
    page_number: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        calculated_offset = self.calculated_offset

        page_number = self.page_number

        page_size = self.page_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calculated_offset is not UNSET:
            field_dict["calculatedOffset"] = calculated_offset
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        calculated_offset = d.pop("calculatedOffset", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        page_size = d.pop("pageSize", UNSET)

        pagination_obj = cls(
            calculated_offset=calculated_offset,
            page_number=page_number,
            page_size=page_size,
        )

        pagination_obj.additional_properties = d
        return pagination_obj

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
