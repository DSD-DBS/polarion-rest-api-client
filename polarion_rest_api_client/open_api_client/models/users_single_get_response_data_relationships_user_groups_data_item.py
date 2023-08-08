# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.users_single_get_response_data_relationships_user_groups_data_item_type import (
    UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="UsersSingleGetResponseDataRelationshipsUserGroupsDataItem"
)


@define
class UsersSingleGetResponseDataRelationshipsUserGroupsDataItem:
    """
    Attributes
    ----------
    type : Union[Unset, UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType]
    id : Union[Unset, str]
    revision : Union[Unset, str]
    """

    type: Union[
        Unset, UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType
    ] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id
        revision = self.revision

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = (
                UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType(
                    _type
                )
            )

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        users_single_get_response_data_relationships_user_groups_data_item_obj = cls(
            type=type,
            id=id,
            revision=revision,
        )

        users_single_get_response_data_relationships_user_groups_data_item_obj.additional_properties = (
            d
        )
        return users_single_get_response_data_relationships_user_groups_data_item_obj

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
