# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentPartsSingleGetResponseDataAttributes")


@_attrs_define
class DocumentPartsSingleGetResponseDataAttributes:
    """
    Attributes:
        content (Union[Unset, str]):  Example: <div id="polarion_wiki macro name=module-
            workitem;params=id=workitem_MyWorkItemId"></div>.
        external (Union[Unset, bool]):
        id (Union[Unset, str]):  Example: workitem_MyWorkItemId.
        level (Union[Unset, int]):
        type (Union[Unset, str]):  Example: workitem.
    """

    content: Union[Unset, str] = UNSET
    external: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        external = self.external

        id = self.id

        level = self.level

        type = self.type

        field_dict: Dict[str, Any] = {}
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
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        external = d.pop("external", UNSET)

        id = d.pop("id", UNSET)

        level = d.pop("level", UNSET)

        type = d.pop("type", UNSET)

        document_parts_single_get_response_data_attributes_obj = cls(
            content=content,
            external=external,
            id=id,
            level=level,
            type=type,
        )

        document_parts_single_get_response_data_attributes_obj.additional_properties = (
            d
        )
        return document_parts_single_get_response_data_attributes_obj

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
