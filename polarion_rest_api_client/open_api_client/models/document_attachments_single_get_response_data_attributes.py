# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentAttachmentsSingleGetResponseDataAttributes")


@_attrs_define
class DocumentAttachmentsSingleGetResponseDataAttributes:
    """
    Attributes:
        file_name (Union[Unset, str]):  Example: File Name.
        id (Union[Unset, str]):  Example: MyAttachmentId.
        length (Union[Unset, int]):
        title (Union[Unset, str]):  Example: Title.
        updated (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
    """

    file_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    length: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        id = self.id

        length = self.length

        title = self.title

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if id is not UNSET:
            field_dict["id"] = id
        if length is not UNSET:
            field_dict["length"] = length
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName", UNSET)

        id = d.pop("id", UNSET)

        length = d.pop("length", UNSET)

        title = d.pop("title", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        document_attachments_single_get_response_data_attributes_obj = cls(
            file_name=file_name,
            id=id,
            length=length,
            title=title,
            updated=updated,
        )

        document_attachments_single_get_response_data_attributes_obj.additional_properties = d
        return document_attachments_single_get_response_data_attributes_obj

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
