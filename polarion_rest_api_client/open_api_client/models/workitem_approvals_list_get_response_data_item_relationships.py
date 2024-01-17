# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_approvals_list_get_response_data_item_relationships_user import (
        WorkitemApprovalsListGetResponseDataItemRelationshipsUser,
    )


T = TypeVar("T", bound="WorkitemApprovalsListGetResponseDataItemRelationships")


@_attrs_define
class WorkitemApprovalsListGetResponseDataItemRelationships:
    """
    Attributes:
        user (Union[Unset, WorkitemApprovalsListGetResponseDataItemRelationshipsUser]):
    """

    user: Union[
        Unset, "WorkitemApprovalsListGetResponseDataItemRelationshipsUser"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitem_approvals_list_get_response_data_item_relationships_user import (
            WorkitemApprovalsListGetResponseDataItemRelationshipsUser,
        )

        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[
            Unset, WorkitemApprovalsListGetResponseDataItemRelationshipsUser
        ]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = WorkitemApprovalsListGetResponseDataItemRelationshipsUser.from_dict(
                _user
            )

        workitem_approvals_list_get_response_data_item_relationships_obj = cls(
            user=user,
        )

        workitem_approvals_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return workitem_approvals_list_get_response_data_item_relationships_obj

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
