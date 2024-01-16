# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_attachments_list_get_response_data_item_relationships_author import (
        DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.document_attachments_list_get_response_data_item_relationships_project import (
        DocumentAttachmentsListGetResponseDataItemRelationshipsProject,
    )


T = TypeVar(
    "T", bound="DocumentAttachmentsListGetResponseDataItemRelationships"
)


@_attrs_define
class DocumentAttachmentsListGetResponseDataItemRelationships:
    """
    Attributes:
        author (Union[Unset, DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor]):
        project (Union[Unset, DocumentAttachmentsListGetResponseDataItemRelationshipsProject]):
    """

    author: Union[
        Unset, "DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor"
    ] = UNSET
    project: Union[
        Unset, "DocumentAttachmentsListGetResponseDataItemRelationshipsProject"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_attachments_list_get_response_data_item_relationships_author import (
            DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.document_attachments_list_get_response_data_item_relationships_project import (
            DocumentAttachmentsListGetResponseDataItemRelationshipsProject,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[
            Unset,
            DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor,
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset,
            DocumentAttachmentsListGetResponseDataItemRelationshipsProject,
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = DocumentAttachmentsListGetResponseDataItemRelationshipsProject.from_dict(
                _project
            )

        document_attachments_list_get_response_data_item_relationships_obj = (
            cls(
                author=author,
                project=project,
            )
        )

        document_attachments_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return (
            document_attachments_list_get_response_data_item_relationships_obj
        )

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
