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

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentPartsListGetResponseDataItemAttributes")


@_attrs_define
class DocumentPartsListGetResponseDataItemAttributes:
    """
    Attributes:
        content (Union[Unset, str]):  Example: <div id="polarion_wiki macro name=module-
            workitem;params=id=workitem_MyWorkItemId"></div>.
        external (Union[Unset, bool]):
        id (Union[Unset, str]):  Example: workitem_MyWorkItemId.
        level (Union[Unset, int]):
        type_ (Union[Unset, str]):  Example: workitem.
    """

    content: Union[Unset, str] = UNSET
    external: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        external = self.external

        id = self.id

        level = self.level

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if external is not UNSET:
            field_dict["external"] = external
        if id is not UNSET:
            field_dict["id"] = id
        if level is not UNSET:
            field_dict["level"] = level
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        external = d.pop("external", UNSET)

        id = d.pop("id", UNSET)

        level = d.pop("level", UNSET)

        type_ = d.pop("type", UNSET)

        document_parts_list_get_response_data_item_attributes_obj = cls(
            content=content,
            external=external,
            id=id,
            level=level,
            type_=type_,
        )

        document_parts_list_get_response_data_item_attributes_obj.additional_properties = d
        return document_parts_list_get_response_data_item_attributes_obj

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
