# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pages_single_get_response_data_relationships_attachments import (
        PagesSingleGetResponseDataRelationshipsAttachments,
    )
    from ..models.pages_single_get_response_data_relationships_author import (
        PagesSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.pages_single_get_response_data_relationships_project import (
        PagesSingleGetResponseDataRelationshipsProject,
    )
    from ..models.pages_single_get_response_data_relationships_updated_by import (
        PagesSingleGetResponseDataRelationshipsUpdatedBy,
    )


T = TypeVar("T", bound="PagesSingleGetResponseDataRelationships")


@_attrs_define
class PagesSingleGetResponseDataRelationships:
    """
    Attributes:
        attachments (Union[Unset, PagesSingleGetResponseDataRelationshipsAttachments]):
        author (Union[Unset, PagesSingleGetResponseDataRelationshipsAuthor]):
        project (Union[Unset, PagesSingleGetResponseDataRelationshipsProject]):
        updated_by (Union[Unset, PagesSingleGetResponseDataRelationshipsUpdatedBy]):
    """

    attachments: Union[
        Unset, "PagesSingleGetResponseDataRelationshipsAttachments"
    ] = UNSET
    author: Union[Unset, "PagesSingleGetResponseDataRelationshipsAuthor"] = (
        UNSET
    )
    project: Union[Unset, "PagesSingleGetResponseDataRelationshipsProject"] = (
        UNSET
    )
    updated_by: Union[
        Unset, "PagesSingleGetResponseDataRelationshipsUpdatedBy"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        updated_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if author is not UNSET:
            field_dict["author"] = author
        if project is not UNSET:
            field_dict["project"] = project
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pages_single_get_response_data_relationships_attachments import (
            PagesSingleGetResponseDataRelationshipsAttachments,
        )
        from ..models.pages_single_get_response_data_relationships_author import (
            PagesSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.pages_single_get_response_data_relationships_project import (
            PagesSingleGetResponseDataRelationshipsProject,
        )
        from ..models.pages_single_get_response_data_relationships_updated_by import (
            PagesSingleGetResponseDataRelationshipsUpdatedBy,
        )

        d = src_dict.copy()
        _attachments = d.pop("attachments", UNSET)
        attachments: Union[
            Unset, PagesSingleGetResponseDataRelationshipsAttachments
        ]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = (
                PagesSingleGetResponseDataRelationshipsAttachments.from_dict(
                    _attachments
                )
            )

        _author = d.pop("author", UNSET)
        author: Union[Unset, PagesSingleGetResponseDataRelationshipsAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PagesSingleGetResponseDataRelationshipsAuthor.from_dict(
                _author
            )

        _project = d.pop("project", UNSET)
        project: Union[Unset, PagesSingleGetResponseDataRelationshipsProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = PagesSingleGetResponseDataRelationshipsProject.from_dict(
                _project
            )

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: Union[
            Unset, PagesSingleGetResponseDataRelationshipsUpdatedBy
        ]
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = (
                PagesSingleGetResponseDataRelationshipsUpdatedBy.from_dict(
                    _updated_by
                )
            )

        pages_single_get_response_data_relationships_obj = cls(
            attachments=attachments,
            author=author,
            project=project,
            updated_by=updated_by,
        )

        pages_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return pages_single_get_response_data_relationships_obj

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
