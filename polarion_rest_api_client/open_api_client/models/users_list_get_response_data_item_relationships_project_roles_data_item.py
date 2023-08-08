# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.users_list_get_response_data_item_relationships_project_roles_data_item_type import (
    UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="UsersListGetResponseDataItemRelationshipsProjectRolesDataItem"
)


@define
class UsersListGetResponseDataItemRelationshipsProjectRolesDataItem:
    """
    Attributes
    ----------
    type : Union[Unset, UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType]
    id : Union[Unset, str]
    """

    type: Union[
        Unset,
        UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType,
    ] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType(
                _type
            )

        id = d.pop("id", UNSET)

        users_list_get_response_data_item_relationships_project_roles_data_item_obj = cls(
            type=type,
            id=id,
        )

        users_list_get_response_data_item_relationships_project_roles_data_item_obj.additional_properties = (
            d
        )
        return users_list_get_response_data_item_relationships_project_roles_data_item_obj

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
