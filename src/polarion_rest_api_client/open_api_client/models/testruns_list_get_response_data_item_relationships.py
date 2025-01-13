# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_list_get_response_data_item_relationships_author import (
        TestrunsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.testruns_list_get_response_data_item_relationships_document import (
        TestrunsListGetResponseDataItemRelationshipsDocument,
    )
    from ..models.testruns_list_get_response_data_item_relationships_project import (
        TestrunsListGetResponseDataItemRelationshipsProject,
    )
    from ..models.testruns_list_get_response_data_item_relationships_project_span import (
        TestrunsListGetResponseDataItemRelationshipsProjectSpan,
    )
    from ..models.testruns_list_get_response_data_item_relationships_summary_defect import (
        TestrunsListGetResponseDataItemRelationshipsSummaryDefect,
    )
    from ..models.testruns_list_get_response_data_item_relationships_template import (
        TestrunsListGetResponseDataItemRelationshipsTemplate,
    )


T = TypeVar("T", bound="TestrunsListGetResponseDataItemRelationships")


@_attrs_define
class TestrunsListGetResponseDataItemRelationships:
    """
    Attributes:
        author (Union[Unset, TestrunsListGetResponseDataItemRelationshipsAuthor]):
        document (Union[Unset, TestrunsListGetResponseDataItemRelationshipsDocument]):
        project (Union[Unset, TestrunsListGetResponseDataItemRelationshipsProject]):
        project_span (Union[Unset, TestrunsListGetResponseDataItemRelationshipsProjectSpan]):
        summary_defect (Union[Unset, TestrunsListGetResponseDataItemRelationshipsSummaryDefect]):
        template (Union[Unset, TestrunsListGetResponseDataItemRelationshipsTemplate]):
    """

    author: Union[
        Unset, "TestrunsListGetResponseDataItemRelationshipsAuthor"
    ] = UNSET
    document: Union[
        Unset, "TestrunsListGetResponseDataItemRelationshipsDocument"
    ] = UNSET
    project: Union[
        Unset, "TestrunsListGetResponseDataItemRelationshipsProject"
    ] = UNSET
    project_span: Union[
        Unset, "TestrunsListGetResponseDataItemRelationshipsProjectSpan"
    ] = UNSET
    summary_defect: Union[
        Unset, "TestrunsListGetResponseDataItemRelationshipsSummaryDefect"
    ] = UNSET
    template: Union[
        Unset, "TestrunsListGetResponseDataItemRelationshipsTemplate"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        project_span: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_span, Unset):
            project_span = self.project_span.to_dict()

        summary_defect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.summary_defect, Unset):
            summary_defect = self.summary_defect.to_dict()

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if document is not UNSET:
            field_dict["document"] = document
        if project is not UNSET:
            field_dict["project"] = project
        if project_span is not UNSET:
            field_dict["projectSpan"] = project_span
        if summary_defect is not UNSET:
            field_dict["summaryDefect"] = summary_defect
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testruns_list_get_response_data_item_relationships_author import (
            TestrunsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.testruns_list_get_response_data_item_relationships_document import (
            TestrunsListGetResponseDataItemRelationshipsDocument,
        )
        from ..models.testruns_list_get_response_data_item_relationships_project import (
            TestrunsListGetResponseDataItemRelationshipsProject,
        )
        from ..models.testruns_list_get_response_data_item_relationships_project_span import (
            TestrunsListGetResponseDataItemRelationshipsProjectSpan,
        )
        from ..models.testruns_list_get_response_data_item_relationships_summary_defect import (
            TestrunsListGetResponseDataItemRelationshipsSummaryDefect,
        )
        from ..models.testruns_list_get_response_data_item_relationships_template import (
            TestrunsListGetResponseDataItemRelationshipsTemplate,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[
            Unset, TestrunsListGetResponseDataItemRelationshipsAuthor
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                TestrunsListGetResponseDataItemRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _document = d.pop("document", UNSET)
        document: Union[
            Unset, TestrunsListGetResponseDataItemRelationshipsDocument
        ]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = (
                TestrunsListGetResponseDataItemRelationshipsDocument.from_dict(
                    _document
                )
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, TestrunsListGetResponseDataItemRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                TestrunsListGetResponseDataItemRelationshipsProject.from_dict(
                    _project
                )
            )

        _project_span = d.pop("projectSpan", UNSET)
        project_span: Union[
            Unset, TestrunsListGetResponseDataItemRelationshipsProjectSpan
        ]
        if isinstance(_project_span, Unset):
            project_span = UNSET
        else:
            project_span = TestrunsListGetResponseDataItemRelationshipsProjectSpan.from_dict(
                _project_span
            )

        _summary_defect = d.pop("summaryDefect", UNSET)
        summary_defect: Union[
            Unset, TestrunsListGetResponseDataItemRelationshipsSummaryDefect
        ]
        if isinstance(_summary_defect, Unset):
            summary_defect = UNSET
        else:
            summary_defect = TestrunsListGetResponseDataItemRelationshipsSummaryDefect.from_dict(
                _summary_defect
            )

        _template = d.pop("template", UNSET)
        template: Union[
            Unset, TestrunsListGetResponseDataItemRelationshipsTemplate
        ]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = (
                TestrunsListGetResponseDataItemRelationshipsTemplate.from_dict(
                    _template
                )
            )

        testruns_list_get_response_data_item_relationships_obj = cls(
            author=author,
            document=document,
            project=project,
            project_span=project_span,
            summary_defect=summary_defect,
            template=template,
        )

        testruns_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return testruns_list_get_response_data_item_relationships_obj

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
