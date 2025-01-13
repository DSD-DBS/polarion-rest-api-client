# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workitems_list_get_response_data_item_relationships_backlinked_work_items_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItem",
)


@_attrs_define
class WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItem:
    """Attributes id (Union[Unset, str]):  Example:
    MyProjectId/MyWorkItemId/parent/MyProjectId/MyLinkedWorkItemId.

    revision (Union[Unset, str]):  Example: 1234.
    type (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItemType]):
    """

    id: Unset | str = UNSET
    revision: Unset | str = UNSET
    type: (
        Unset
        | WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItemType
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        revision = self.revision

        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _type = d.pop("type", UNSET)
        type: (
            Unset
            | WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItemType
        )
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItemType(
                _type
            )

        workitems_list_get_response_data_item_relationships_backlinked_work_items_data_item_obj = cls(
            id=id,
            revision=revision,
            type=type,
        )

        workitems_list_get_response_data_item_relationships_backlinked_work_items_data_item_obj.additional_properties = d
        return workitems_list_get_response_data_item_relationships_backlinked_work_items_data_item_obj

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
