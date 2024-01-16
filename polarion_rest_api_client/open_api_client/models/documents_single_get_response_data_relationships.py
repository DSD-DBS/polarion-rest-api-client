# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_single_get_response_data_relationships_attachments import (
        DocumentsSingleGetResponseDataRelationshipsAttachments,
    )
    from ..models.documents_single_get_response_data_relationships_author import (
        DocumentsSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.documents_single_get_response_data_relationships_branched_from import (
        DocumentsSingleGetResponseDataRelationshipsBranchedFrom,
    )
    from ..models.documents_single_get_response_data_relationships_comments import (
        DocumentsSingleGetResponseDataRelationshipsComments,
    )
    from ..models.documents_single_get_response_data_relationships_derived_from import (
        DocumentsSingleGetResponseDataRelationshipsDerivedFrom,
    )
    from ..models.documents_single_get_response_data_relationships_project import (
        DocumentsSingleGetResponseDataRelationshipsProject,
    )
    from ..models.documents_single_get_response_data_relationships_updated_by import (
        DocumentsSingleGetResponseDataRelationshipsUpdatedBy,
    )
    from ..models.documents_single_get_response_data_relationships_variant import (
        DocumentsSingleGetResponseDataRelationshipsVariant,
    )


T = TypeVar("T", bound="DocumentsSingleGetResponseDataRelationships")


@_attrs_define
class DocumentsSingleGetResponseDataRelationships:
    """
    Attributes:
        attachments (Union[Unset, DocumentsSingleGetResponseDataRelationshipsAttachments]):
        author (Union[Unset, DocumentsSingleGetResponseDataRelationshipsAuthor]):
        branched_from (Union[Unset, DocumentsSingleGetResponseDataRelationshipsBranchedFrom]):
        comments (Union[Unset, DocumentsSingleGetResponseDataRelationshipsComments]):
        derived_from (Union[Unset, DocumentsSingleGetResponseDataRelationshipsDerivedFrom]):
        project (Union[Unset, DocumentsSingleGetResponseDataRelationshipsProject]):
        updated_by (Union[Unset, DocumentsSingleGetResponseDataRelationshipsUpdatedBy]):
        variant (Union[Unset, DocumentsSingleGetResponseDataRelationshipsVariant]):
    """

    attachments: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsAttachments"
    ] = UNSET
    author: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsAuthor"
    ] = UNSET
    branched_from: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsBranchedFrom"
    ] = UNSET
    comments: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsComments"
    ] = UNSET
    derived_from: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsDerivedFrom"
    ] = UNSET
    project: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsProject"
    ] = UNSET
    updated_by: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsUpdatedBy"
    ] = UNSET
    variant: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsVariant"
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

        branched_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branched_from, Unset):
            branched_from = self.branched_from.to_dict()

        comments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        derived_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.derived_from, Unset):
            derived_from = self.derived_from.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        updated_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict()

        variant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if author is not UNSET:
            field_dict["author"] = author
        if branched_from is not UNSET:
            field_dict["branchedFrom"] = branched_from
        if comments is not UNSET:
            field_dict["comments"] = comments
        if derived_from is not UNSET:
            field_dict["derivedFrom"] = derived_from
        if project is not UNSET:
            field_dict["project"] = project
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.documents_single_get_response_data_relationships_attachments import (
            DocumentsSingleGetResponseDataRelationshipsAttachments,
        )
        from ..models.documents_single_get_response_data_relationships_author import (
            DocumentsSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.documents_single_get_response_data_relationships_branched_from import (
            DocumentsSingleGetResponseDataRelationshipsBranchedFrom,
        )
        from ..models.documents_single_get_response_data_relationships_comments import (
            DocumentsSingleGetResponseDataRelationshipsComments,
        )
        from ..models.documents_single_get_response_data_relationships_derived_from import (
            DocumentsSingleGetResponseDataRelationshipsDerivedFrom,
        )
        from ..models.documents_single_get_response_data_relationships_project import (
            DocumentsSingleGetResponseDataRelationshipsProject,
        )
        from ..models.documents_single_get_response_data_relationships_updated_by import (
            DocumentsSingleGetResponseDataRelationshipsUpdatedBy,
        )
        from ..models.documents_single_get_response_data_relationships_variant import (
            DocumentsSingleGetResponseDataRelationshipsVariant,
        )

        d = src_dict.copy()
        _attachments = d.pop("attachments", UNSET)
        attachments: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsAttachments
        ]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = DocumentsSingleGetResponseDataRelationshipsAttachments.from_dict(
                _attachments
            )

        _author = d.pop("author", UNSET)
        author: Union[Unset, DocumentsSingleGetResponseDataRelationshipsAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                DocumentsSingleGetResponseDataRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _branched_from = d.pop("branchedFrom", UNSET)
        branched_from: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsBranchedFrom
        ]
        if isinstance(_branched_from, Unset):
            branched_from = UNSET
        else:
            branched_from = DocumentsSingleGetResponseDataRelationshipsBranchedFrom.from_dict(
                _branched_from
            )

        _comments = d.pop("comments", UNSET)
        comments: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsComments
        ]
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = (
                DocumentsSingleGetResponseDataRelationshipsComments.from_dict(
                    _comments
                )
            )

        _derived_from = d.pop("derivedFrom", UNSET)
        derived_from: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsDerivedFrom
        ]
        if isinstance(_derived_from, Unset):
            derived_from = UNSET
        else:
            derived_from = DocumentsSingleGetResponseDataRelationshipsDerivedFrom.from_dict(
                _derived_from
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                DocumentsSingleGetResponseDataRelationshipsProject.from_dict(
                    _project
                )
            )

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsUpdatedBy
        ]
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = (
                DocumentsSingleGetResponseDataRelationshipsUpdatedBy.from_dict(
                    _updated_by
                )
            )

        _variant = d.pop("variant", UNSET)
        variant: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsVariant
        ]
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = (
                DocumentsSingleGetResponseDataRelationshipsVariant.from_dict(
                    _variant
                )
            )

        documents_single_get_response_data_relationships_obj = cls(
            attachments=attachments,
            author=author,
            branched_from=branched_from,
            comments=comments,
            derived_from=derived_from,
            project=project,
            updated_by=updated_by,
            variant=variant,
        )

        documents_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return documents_single_get_response_data_relationships_obj

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
