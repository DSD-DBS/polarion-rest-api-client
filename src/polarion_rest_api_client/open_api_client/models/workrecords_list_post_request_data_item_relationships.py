# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workrecords_list_post_request_data_item_relationships_user import (
        WorkrecordsListPostRequestDataItemRelationshipsUser,
    )


T = TypeVar("T", bound="WorkrecordsListPostRequestDataItemRelationships")


@_attrs_define
class WorkrecordsListPostRequestDataItemRelationships:
    """
    Attributes:
        user (Union[Unset, WorkrecordsListPostRequestDataItemRelationshipsUser]):
    """

    user: Union[
        Unset, "WorkrecordsListPostRequestDataItemRelationshipsUser"
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
        from ..models.workrecords_list_post_request_data_item_relationships_user import (
            WorkrecordsListPostRequestDataItemRelationshipsUser,
        )

        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, WorkrecordsListPostRequestDataItemRelationshipsUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = (
                WorkrecordsListPostRequestDataItemRelationshipsUser.from_dict(
                    _user
                )
            )

        workrecords_list_post_request_data_item_relationships_obj = cls(
            user=user,
        )

        workrecords_list_post_request_data_item_relationships_obj.additional_properties = (
            d
        )
        return workrecords_list_post_request_data_item_relationships_obj

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
