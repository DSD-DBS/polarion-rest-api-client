# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workitem_comments_list_post_request_data_item_relationships_parent_comment_data_type import (
    WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentData",
)


@_attrs_define
class WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentData:
    """
    Attributes:
        id (Union[Unset, str]):  Example: MyProjectId/MyWorkItemId/MyCommentId.
        type (Union[Unset, WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[
        Unset,
        WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType(
                _type
            )

        workitem_comments_list_post_request_data_item_relationships_parent_comment_data_obj = cls(
            id=id,
            type=type,
        )

        workitem_comments_list_post_request_data_item_relationships_parent_comment_data_obj.additional_properties = (
            d
        )
        return workitem_comments_list_post_request_data_item_relationships_parent_comment_data_obj

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
