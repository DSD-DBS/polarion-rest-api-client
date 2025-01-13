# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usergroups_single_get_response_data_attributes_description import (
        UsergroupsSingleGetResponseDataAttributesDescription,
    )


T = TypeVar("T", bound="UsergroupsSingleGetResponseDataAttributes")


@_attrs_define
class UsergroupsSingleGetResponseDataAttributes:
    """
    Attributes:
        description (Union[Unset, UsergroupsSingleGetResponseDataAttributesDescription]):
        id (Union[Unset, str]):  Example: MyUserGroupId.
        ldap_search_filter (Union[Unset, str]):  Example: LDAP Search Filter.
        name (Union[Unset, str]):  Example: Name.
        sso_synchronization_allowed (Union[Unset, bool]):
    """

    description: Union[
        Unset, "UsergroupsSingleGetResponseDataAttributesDescription"
    ] = UNSET
    id: Union[Unset, str] = UNSET
    ldap_search_filter: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    sso_synchronization_allowed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        id = self.id

        ldap_search_filter = self.ldap_search_filter

        name = self.name

        sso_synchronization_allowed = self.sso_synchronization_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if ldap_search_filter is not UNSET:
            field_dict["ldapSearchFilter"] = ldap_search_filter
        if name is not UNSET:
            field_dict["name"] = name
        if sso_synchronization_allowed is not UNSET:
            field_dict["ssoSynchronizationAllowed"] = (
                sso_synchronization_allowed
            )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.usergroups_single_get_response_data_attributes_description import (
            UsergroupsSingleGetResponseDataAttributesDescription,
        )

        d = src_dict.copy()
        _description = d.pop("description", UNSET)
        description: Union[
            Unset, UsergroupsSingleGetResponseDataAttributesDescription
        ]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                UsergroupsSingleGetResponseDataAttributesDescription.from_dict(
                    _description
                )
            )

        id = d.pop("id", UNSET)

        ldap_search_filter = d.pop("ldapSearchFilter", UNSET)

        name = d.pop("name", UNSET)

        sso_synchronization_allowed = d.pop("ssoSynchronizationAllowed", UNSET)

        usergroups_single_get_response_data_attributes_obj = cls(
            description=description,
            id=id,
            ldap_search_filter=ldap_search_filter,
            name=name,
            sso_synchronization_allowed=sso_synchronization_allowed,
        )

        usergroups_single_get_response_data_attributes_obj.additional_properties = (
            d
        )
        return usergroups_single_get_response_data_attributes_obj

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
