# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_single_get_response_data_relationships_document import (
        JobsSingleGetResponseDataRelationshipsDocument,
    )
    from ..models.jobs_single_get_response_data_relationships_documents import (
        JobsSingleGetResponseDataRelationshipsDocuments,
    )
    from ..models.jobs_single_get_response_data_relationships_project import (
        JobsSingleGetResponseDataRelationshipsProject,
    )


T = TypeVar("T", bound="JobsSingleGetResponseDataRelationships")


@_attrs_define
class JobsSingleGetResponseDataRelationships:
    """
    Attributes:
        document (Union[Unset, JobsSingleGetResponseDataRelationshipsDocument]):
        documents (Union[Unset, JobsSingleGetResponseDataRelationshipsDocuments]):
        project (Union[Unset, JobsSingleGetResponseDataRelationshipsProject]):
    """

    document: Union[
        Unset, "JobsSingleGetResponseDataRelationshipsDocument"
    ] = UNSET
    documents: Union[
        Unset, "JobsSingleGetResponseDataRelationshipsDocuments"
    ] = UNSET
    project: Union[Unset, "JobsSingleGetResponseDataRelationshipsProject"] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        documents: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if documents is not UNSET:
            field_dict["documents"] = documents
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jobs_single_get_response_data_relationships_document import (
            JobsSingleGetResponseDataRelationshipsDocument,
        )
        from ..models.jobs_single_get_response_data_relationships_documents import (
            JobsSingleGetResponseDataRelationshipsDocuments,
        )
        from ..models.jobs_single_get_response_data_relationships_project import (
            JobsSingleGetResponseDataRelationshipsProject,
        )

        d = src_dict.copy()
        _document = d.pop("document", UNSET)
        document: Union[Unset, JobsSingleGetResponseDataRelationshipsDocument]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = (
                JobsSingleGetResponseDataRelationshipsDocument.from_dict(
                    _document
                )
            )

        _documents = d.pop("documents", UNSET)
        documents: Union[
            Unset, JobsSingleGetResponseDataRelationshipsDocuments
        ]
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = (
                JobsSingleGetResponseDataRelationshipsDocuments.from_dict(
                    _documents
                )
            )

        _project = d.pop("project", UNSET)
        project: Union[Unset, JobsSingleGetResponseDataRelationshipsProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = JobsSingleGetResponseDataRelationshipsProject.from_dict(
                _project
            )

        jobs_single_get_response_data_relationships_obj = cls(
            document=document,
            documents=documents,
            project=project,
        )

        jobs_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return jobs_single_get_response_data_relationships_obj

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
