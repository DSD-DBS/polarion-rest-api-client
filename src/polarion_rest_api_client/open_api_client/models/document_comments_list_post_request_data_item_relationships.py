# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_list_post_request_data_item_relationships_author import (
        DocumentCommentsListPostRequestDataItemRelationshipsAuthor,
    )
    from ..models.document_comments_list_post_request_data_item_relationships_parent_comment import (
        DocumentCommentsListPostRequestDataItemRelationshipsParentComment,
    )


T = TypeVar("T", bound="DocumentCommentsListPostRequestDataItemRelationships")


@_attrs_define
class DocumentCommentsListPostRequestDataItemRelationships:
    """
    Attributes:
        author (Union[Unset, DocumentCommentsListPostRequestDataItemRelationshipsAuthor]):
        parent_comment (Union[Unset, DocumentCommentsListPostRequestDataItemRelationshipsParentComment]):
    """

    author: Union[
        Unset, "DocumentCommentsListPostRequestDataItemRelationshipsAuthor"
    ] = UNSET
    parent_comment: Union[
        Unset,
        "DocumentCommentsListPostRequestDataItemRelationshipsParentComment",
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        parent_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_comment, Unset):
            parent_comment = self.parent_comment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if parent_comment is not UNSET:
            field_dict["parentComment"] = parent_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_comments_list_post_request_data_item_relationships_author import (
            DocumentCommentsListPostRequestDataItemRelationshipsAuthor,
        )
        from ..models.document_comments_list_post_request_data_item_relationships_parent_comment import (
            DocumentCommentsListPostRequestDataItemRelationshipsParentComment,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[
            Unset, DocumentCommentsListPostRequestDataItemRelationshipsAuthor
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = DocumentCommentsListPostRequestDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _parent_comment = d.pop("parentComment", UNSET)
        parent_comment: Union[
            Unset,
            DocumentCommentsListPostRequestDataItemRelationshipsParentComment,
        ]
        if isinstance(_parent_comment, Unset):
            parent_comment = UNSET
        else:
            parent_comment = DocumentCommentsListPostRequestDataItemRelationshipsParentComment.from_dict(
                _parent_comment
            )

        document_comments_list_post_request_data_item_relationships_obj = cls(
            author=author,
            parent_comment=parent_comment,
        )

        document_comments_list_post_request_data_item_relationships_obj.additional_properties = (
            d
        )
        return document_comments_list_post_request_data_item_relationships_obj

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
