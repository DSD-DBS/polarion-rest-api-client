# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_single_get_response_data_relationships_author import (
        TestrunsSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.testruns_single_get_response_data_relationships_document import (
        TestrunsSingleGetResponseDataRelationshipsDocument,
    )
    from ..models.testruns_single_get_response_data_relationships_project import (
        TestrunsSingleGetResponseDataRelationshipsProject,
    )
    from ..models.testruns_single_get_response_data_relationships_project_span import (
        TestrunsSingleGetResponseDataRelationshipsProjectSpan,
    )
    from ..models.testruns_single_get_response_data_relationships_summary_defect import (
        TestrunsSingleGetResponseDataRelationshipsSummaryDefect,
    )
    from ..models.testruns_single_get_response_data_relationships_template import (
        TestrunsSingleGetResponseDataRelationshipsTemplate,
    )


T = TypeVar("T", bound="TestrunsSingleGetResponseDataRelationships")


@_attrs_define
class TestrunsSingleGetResponseDataRelationships:
    """
    Attributes:
        author (Union[Unset, TestrunsSingleGetResponseDataRelationshipsAuthor]):
        document (Union[Unset, TestrunsSingleGetResponseDataRelationshipsDocument]):
        project (Union[Unset, TestrunsSingleGetResponseDataRelationshipsProject]):
        project_span (Union[Unset, TestrunsSingleGetResponseDataRelationshipsProjectSpan]):
        summary_defect (Union[Unset, TestrunsSingleGetResponseDataRelationshipsSummaryDefect]):
        template (Union[Unset, TestrunsSingleGetResponseDataRelationshipsTemplate]):
    """

    author: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsAuthor"
    ] = UNSET
    document: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsDocument"
    ] = UNSET
    project: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsProject"
    ] = UNSET
    project_span: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsProjectSpan"
    ] = UNSET
    summary_defect: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsSummaryDefect"
    ] = UNSET
    template: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsTemplate"
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
        from ..models.testruns_single_get_response_data_relationships_author import (
            TestrunsSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.testruns_single_get_response_data_relationships_document import (
            TestrunsSingleGetResponseDataRelationshipsDocument,
        )
        from ..models.testruns_single_get_response_data_relationships_project import (
            TestrunsSingleGetResponseDataRelationshipsProject,
        )
        from ..models.testruns_single_get_response_data_relationships_project_span import (
            TestrunsSingleGetResponseDataRelationshipsProjectSpan,
        )
        from ..models.testruns_single_get_response_data_relationships_summary_defect import (
            TestrunsSingleGetResponseDataRelationshipsSummaryDefect,
        )
        from ..models.testruns_single_get_response_data_relationships_template import (
            TestrunsSingleGetResponseDataRelationshipsTemplate,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, TestrunsSingleGetResponseDataRelationshipsAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                TestrunsSingleGetResponseDataRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _document = d.pop("document", UNSET)
        document: Union[
            Unset, TestrunsSingleGetResponseDataRelationshipsDocument
        ]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = (
                TestrunsSingleGetResponseDataRelationshipsDocument.from_dict(
                    _document
                )
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, TestrunsSingleGetResponseDataRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                TestrunsSingleGetResponseDataRelationshipsProject.from_dict(
                    _project
                )
            )

        _project_span = d.pop("projectSpan", UNSET)
        project_span: Union[
            Unset, TestrunsSingleGetResponseDataRelationshipsProjectSpan
        ]
        if isinstance(_project_span, Unset):
            project_span = UNSET
        else:
            project_span = TestrunsSingleGetResponseDataRelationshipsProjectSpan.from_dict(
                _project_span
            )

        _summary_defect = d.pop("summaryDefect", UNSET)
        summary_defect: Union[
            Unset, TestrunsSingleGetResponseDataRelationshipsSummaryDefect
        ]
        if isinstance(_summary_defect, Unset):
            summary_defect = UNSET
        else:
            summary_defect = TestrunsSingleGetResponseDataRelationshipsSummaryDefect.from_dict(
                _summary_defect
            )

        _template = d.pop("template", UNSET)
        template: Union[
            Unset, TestrunsSingleGetResponseDataRelationshipsTemplate
        ]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = (
                TestrunsSingleGetResponseDataRelationshipsTemplate.from_dict(
                    _template
                )
            )

        testruns_single_get_response_data_relationships_obj = cls(
            author=author,
            document=document,
            project=project,
            project_span=project_span,
            summary_defect=summary_defect,
            template=template,
        )

        testruns_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return testruns_single_get_response_data_relationships_obj

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
