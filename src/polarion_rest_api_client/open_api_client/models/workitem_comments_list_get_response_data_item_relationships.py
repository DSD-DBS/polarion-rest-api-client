# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_comments_list_get_response_data_item_relationships_author import (
        WorkitemCommentsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.workitem_comments_list_get_response_data_item_relationships_child_comments import (
        WorkitemCommentsListGetResponseDataItemRelationshipsChildComments,
    )
    from ..models.workitem_comments_list_get_response_data_item_relationships_parent_comment import (
        WorkitemCommentsListGetResponseDataItemRelationshipsParentComment,
    )
    from ..models.workitem_comments_list_get_response_data_item_relationships_project import (
        WorkitemCommentsListGetResponseDataItemRelationshipsProject,
    )


T = TypeVar("T", bound="WorkitemCommentsListGetResponseDataItemRelationships")


@_attrs_define
class WorkitemCommentsListGetResponseDataItemRelationships:
    """
    Attributes:
        author (Union[Unset, WorkitemCommentsListGetResponseDataItemRelationshipsAuthor]):
        child_comments (Union[Unset, WorkitemCommentsListGetResponseDataItemRelationshipsChildComments]):
        parent_comment (Union[Unset, WorkitemCommentsListGetResponseDataItemRelationshipsParentComment]):
        project (Union[Unset, WorkitemCommentsListGetResponseDataItemRelationshipsProject]):
    """

    author: Union[
        Unset, "WorkitemCommentsListGetResponseDataItemRelationshipsAuthor"
    ] = UNSET
    child_comments: Union[
        Unset,
        "WorkitemCommentsListGetResponseDataItemRelationshipsChildComments",
    ] = UNSET
    parent_comment: Union[
        Unset,
        "WorkitemCommentsListGetResponseDataItemRelationshipsParentComment",
    ] = UNSET
    project: Union[
        Unset, "WorkitemCommentsListGetResponseDataItemRelationshipsProject"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        child_comments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.child_comments, Unset):
            child_comments = self.child_comments.to_dict()

        parent_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_comment, Unset):
            parent_comment = self.parent_comment.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if child_comments is not UNSET:
            field_dict["childComments"] = child_comments
        if parent_comment is not UNSET:
            field_dict["parentComment"] = parent_comment
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitem_comments_list_get_response_data_item_relationships_author import (
            WorkitemCommentsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.workitem_comments_list_get_response_data_item_relationships_child_comments import (
            WorkitemCommentsListGetResponseDataItemRelationshipsChildComments,
        )
        from ..models.workitem_comments_list_get_response_data_item_relationships_parent_comment import (
            WorkitemCommentsListGetResponseDataItemRelationshipsParentComment,
        )
        from ..models.workitem_comments_list_get_response_data_item_relationships_project import (
            WorkitemCommentsListGetResponseDataItemRelationshipsProject,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[
            Unset, WorkitemCommentsListGetResponseDataItemRelationshipsAuthor
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = WorkitemCommentsListGetResponseDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _child_comments = d.pop("childComments", UNSET)
        child_comments: Union[
            Unset,
            WorkitemCommentsListGetResponseDataItemRelationshipsChildComments,
        ]
        if isinstance(_child_comments, Unset):
            child_comments = UNSET
        else:
            child_comments = WorkitemCommentsListGetResponseDataItemRelationshipsChildComments.from_dict(
                _child_comments
            )

        _parent_comment = d.pop("parentComment", UNSET)
        parent_comment: Union[
            Unset,
            WorkitemCommentsListGetResponseDataItemRelationshipsParentComment,
        ]
        if isinstance(_parent_comment, Unset):
            parent_comment = UNSET
        else:
            parent_comment = WorkitemCommentsListGetResponseDataItemRelationshipsParentComment.from_dict(
                _parent_comment
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, WorkitemCommentsListGetResponseDataItemRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = WorkitemCommentsListGetResponseDataItemRelationshipsProject.from_dict(
                _project
            )

        workitem_comments_list_get_response_data_item_relationships_obj = cls(
            author=author,
            child_comments=child_comments,
            parent_comment=parent_comment,
            project=project,
        )

        workitem_comments_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return workitem_comments_list_get_response_data_item_relationships_obj

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
