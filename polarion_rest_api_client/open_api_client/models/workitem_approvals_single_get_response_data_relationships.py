# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_approvals_single_get_response_data_relationships_user import (
        WorkitemApprovalsSingleGetResponseDataRelationshipsUser,
    )


T = TypeVar("T", bound="WorkitemApprovalsSingleGetResponseDataRelationships")


@_attrs_define
class WorkitemApprovalsSingleGetResponseDataRelationships:
    """
    Attributes:
        user (Union[Unset, WorkitemApprovalsSingleGetResponseDataRelationshipsUser]):
    """

    user: Union[
        Unset, "WorkitemApprovalsSingleGetResponseDataRelationshipsUser"
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
        from ..models.workitem_approvals_single_get_response_data_relationships_user import (
            WorkitemApprovalsSingleGetResponseDataRelationshipsUser,
        )

        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[
            Unset, WorkitemApprovalsSingleGetResponseDataRelationshipsUser
        ]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = WorkitemApprovalsSingleGetResponseDataRelationshipsUser.from_dict(
                _user
            )

        workitem_approvals_single_get_response_data_relationships_obj = cls(
            user=user,
        )

        workitem_approvals_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return workitem_approvals_single_get_response_data_relationships_obj

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
