# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrun_attachments_list_delete_request_data_item_type import (
    TestrunAttachmentsListDeleteRequestDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrunAttachmentsListDeleteRequestDataItem")


@_attrs_define
class TestrunAttachmentsListDeleteRequestDataItem:
    """
    Attributes:
        type_ (Union[Unset, TestrunAttachmentsListDeleteRequestDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId/MyAttachmentId.
    """

    type_: Union[Unset, TestrunAttachmentsListDeleteRequestDataItemType] = (
        UNSET
    )
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TestrunAttachmentsListDeleteRequestDataItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TestrunAttachmentsListDeleteRequestDataItemType(_type_)

        id = d.pop("id", UNSET)

        testrun_attachments_list_delete_request_data_item_obj = cls(
            type_=type_,
            id=id,
        )

        testrun_attachments_list_delete_request_data_item_obj.additional_properties = d
        return testrun_attachments_list_delete_request_data_item_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
