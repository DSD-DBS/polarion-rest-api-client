# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrunAttachmentsListPostRequestDataItemAttributes")


@_attrs_define
class TestrunAttachmentsListPostRequestDataItemAttributes:
    """
    Attributes:
        file_name (Union[Unset, str]):  Example: File Name.
        title (Union[Unset, str]):  Example: Title.
    """

    file_name: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("fileName", UNSET)

        title = d.pop("title", UNSET)

        testrun_attachments_list_post_request_data_item_attributes_obj = cls(
            file_name=file_name,
            title=title,
        )

        testrun_attachments_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return testrun_attachments_list_post_request_data_item_attributes_obj

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
