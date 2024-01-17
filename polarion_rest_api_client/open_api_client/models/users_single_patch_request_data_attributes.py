# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.users_single_patch_request_data_attributes_description import (
        UsersSinglePatchRequestDataAttributesDescription,
    )


T = TypeVar("T", bound="UsersSinglePatchRequestDataAttributes")


@_attrs_define
class UsersSinglePatchRequestDataAttributes:
    """
    Attributes:
        description (Union[Unset, UsersSinglePatchRequestDataAttributesDescription]):
        disabled_notifications (Union[Unset, bool]):
        email (Union[Unset, str]):  Example: Email.
        initials (Union[Unset, str]):  Example: Initials.
        name (Union[Unset, str]):  Example: Name.
    """

    description: Union[
        Unset, "UsersSinglePatchRequestDataAttributesDescription"
    ] = UNSET
    disabled_notifications: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        disabled_notifications = self.disabled_notifications

        email = self.email

        initials = self.initials

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if disabled_notifications is not UNSET:
            field_dict["disabledNotifications"] = disabled_notifications
        if email is not UNSET:
            field_dict["email"] = email
        if initials is not UNSET:
            field_dict["initials"] = initials
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.users_single_patch_request_data_attributes_description import (
            UsersSinglePatchRequestDataAttributesDescription,
        )

        d = src_dict.copy()
        _description = d.pop("description", UNSET)
        description: Union[
            Unset, UsersSinglePatchRequestDataAttributesDescription
        ]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                UsersSinglePatchRequestDataAttributesDescription.from_dict(
                    _description
                )
            )

        disabled_notifications = d.pop("disabledNotifications", UNSET)

        email = d.pop("email", UNSET)

        initials = d.pop("initials", UNSET)

        name = d.pop("name", UNSET)

        users_single_patch_request_data_attributes_obj = cls(
            description=description,
            disabled_notifications=disabled_notifications,
            email=email,
            initials=initials,
            name=name,
        )

        users_single_patch_request_data_attributes_obj.additional_properties = (
            d
        )
        return users_single_patch_request_data_attributes_obj

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
