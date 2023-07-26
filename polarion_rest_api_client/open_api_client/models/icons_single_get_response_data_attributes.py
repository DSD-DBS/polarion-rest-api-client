# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IconsSingleGetResponseDataAttributes")


@attr.s(auto_attribs=True)
class IconsSingleGetResponseDataAttributes:
    """
    Attributes:
        icon_url (Union[Unset, str]):  Example: pathexample.
        path (Union[Unset, str]):  Example: pathexample.
    """

    icon_url: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        icon_url = self.icon_url
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        icon_url = d.pop("iconUrl", UNSET)

        path = d.pop("path", UNSET)

        icons_single_get_response_data_attributes_obj = cls(
            icon_url=icon_url,
            path=path,
        )

        icons_single_get_response_data_attributes_obj.additional_properties = d
        return icons_single_get_response_data_attributes_obj

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
