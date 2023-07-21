# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.document_comments_list_post_request_data_item_relationships_parent_comment_data_type import (
    DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="DocumentCommentsListPostRequestDataItemRelationshipsParentCommentData",
)


@attr.s(auto_attribs=True)
class DocumentCommentsListPostRequestDataItemRelationshipsParentCommentData:
    """
    Attributes:
        type (Union[Unset, DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MySpaceId/MyDocumentId/MyCommentId.
    """

    type: Union[
        Unset,
        DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
    ] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
            DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType(
                _type
            )

        id = d.pop("id", UNSET)

        document_comments_list_post_request_data_item_relationships_parent_comment_data = cls(
            type=type,
            id=id,
        )

        document_comments_list_post_request_data_item_relationships_parent_comment_data.additional_properties = (
            d
        )
        return document_comments_list_post_request_data_item_relationships_parent_comment_data

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
