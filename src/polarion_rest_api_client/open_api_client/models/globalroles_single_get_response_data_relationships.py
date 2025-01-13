# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.globalroles_single_get_response_data_relationships_users import (
        GlobalrolesSingleGetResponseDataRelationshipsUsers,
    )


T = TypeVar("T", bound="GlobalrolesSingleGetResponseDataRelationships")


@_attrs_define
class GlobalrolesSingleGetResponseDataRelationships:
    """
    Attributes:
        users (Union[Unset, GlobalrolesSingleGetResponseDataRelationshipsUsers]):
    """

    users: Union[
        Unset, "GlobalrolesSingleGetResponseDataRelationshipsUsers"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.globalroles_single_get_response_data_relationships_users import (
            GlobalrolesSingleGetResponseDataRelationshipsUsers,
        )

        d = src_dict.copy()
        _users = d.pop("users", UNSET)
        users: Union[Unset, GlobalrolesSingleGetResponseDataRelationshipsUsers]
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = (
                GlobalrolesSingleGetResponseDataRelationshipsUsers.from_dict(
                    _users
                )
            )

        globalroles_single_get_response_data_relationships_obj = cls(
            users=users,
        )

        globalroles_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return globalroles_single_get_response_data_relationships_obj

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
