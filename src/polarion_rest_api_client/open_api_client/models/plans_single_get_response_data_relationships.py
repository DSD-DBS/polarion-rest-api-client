# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plans_single_get_response_data_relationships_author import (
        PlansSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.plans_single_get_response_data_relationships_parent import (
        PlansSingleGetResponseDataRelationshipsParent,
    )
    from ..models.plans_single_get_response_data_relationships_project import (
        PlansSingleGetResponseDataRelationshipsProject,
    )
    from ..models.plans_single_get_response_data_relationships_project_span import (
        PlansSingleGetResponseDataRelationshipsProjectSpan,
    )
    from ..models.plans_single_get_response_data_relationships_template import (
        PlansSingleGetResponseDataRelationshipsTemplate,
    )
    from ..models.plans_single_get_response_data_relationships_work_items import (
        PlansSingleGetResponseDataRelationshipsWorkItems,
    )


T = TypeVar("T", bound="PlansSingleGetResponseDataRelationships")


@_attrs_define
class PlansSingleGetResponseDataRelationships:
    """
    Attributes:
        author (Union[Unset, PlansSingleGetResponseDataRelationshipsAuthor]):
        parent (Union[Unset, PlansSingleGetResponseDataRelationshipsParent]):
        project (Union[Unset, PlansSingleGetResponseDataRelationshipsProject]):
        project_span (Union[Unset, PlansSingleGetResponseDataRelationshipsProjectSpan]):
        template (Union[Unset, PlansSingleGetResponseDataRelationshipsTemplate]):
        work_items (Union[Unset, PlansSingleGetResponseDataRelationshipsWorkItems]):
    """

    author: Union[Unset, "PlansSingleGetResponseDataRelationshipsAuthor"] = (
        UNSET
    )
    parent: Union[Unset, "PlansSingleGetResponseDataRelationshipsParent"] = (
        UNSET
    )
    project: Union[Unset, "PlansSingleGetResponseDataRelationshipsProject"] = (
        UNSET
    )
    project_span: Union[
        Unset, "PlansSingleGetResponseDataRelationshipsProjectSpan"
    ] = UNSET
    template: Union[
        Unset, "PlansSingleGetResponseDataRelationshipsTemplate"
    ] = UNSET
    work_items: Union[
        Unset, "PlansSingleGetResponseDataRelationshipsWorkItems"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        project_span: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_span, Unset):
            project_span = self.project_span.to_dict()

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        work_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_items, Unset):
            work_items = self.work_items.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if parent is not UNSET:
            field_dict["parent"] = parent
        if project is not UNSET:
            field_dict["project"] = project
        if project_span is not UNSET:
            field_dict["projectSpan"] = project_span
        if template is not UNSET:
            field_dict["template"] = template
        if work_items is not UNSET:
            field_dict["workItems"] = work_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plans_single_get_response_data_relationships_author import (
            PlansSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.plans_single_get_response_data_relationships_parent import (
            PlansSingleGetResponseDataRelationshipsParent,
        )
        from ..models.plans_single_get_response_data_relationships_project import (
            PlansSingleGetResponseDataRelationshipsProject,
        )
        from ..models.plans_single_get_response_data_relationships_project_span import (
            PlansSingleGetResponseDataRelationshipsProjectSpan,
        )
        from ..models.plans_single_get_response_data_relationships_template import (
            PlansSingleGetResponseDataRelationshipsTemplate,
        )
        from ..models.plans_single_get_response_data_relationships_work_items import (
            PlansSingleGetResponseDataRelationshipsWorkItems,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, PlansSingleGetResponseDataRelationshipsAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PlansSingleGetResponseDataRelationshipsAuthor.from_dict(
                _author
            )

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, PlansSingleGetResponseDataRelationshipsParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = PlansSingleGetResponseDataRelationshipsParent.from_dict(
                _parent
            )

        _project = d.pop("project", UNSET)
        project: Union[Unset, PlansSingleGetResponseDataRelationshipsProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = PlansSingleGetResponseDataRelationshipsProject.from_dict(
                _project
            )

        _project_span = d.pop("projectSpan", UNSET)
        project_span: Union[
            Unset, PlansSingleGetResponseDataRelationshipsProjectSpan
        ]
        if isinstance(_project_span, Unset):
            project_span = UNSET
        else:
            project_span = (
                PlansSingleGetResponseDataRelationshipsProjectSpan.from_dict(
                    _project_span
                )
            )

        _template = d.pop("template", UNSET)
        template: Union[Unset, PlansSingleGetResponseDataRelationshipsTemplate]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = (
                PlansSingleGetResponseDataRelationshipsTemplate.from_dict(
                    _template
                )
            )

        _work_items = d.pop("workItems", UNSET)
        work_items: Union[
            Unset, PlansSingleGetResponseDataRelationshipsWorkItems
        ]
        if isinstance(_work_items, Unset):
            work_items = UNSET
        else:
            work_items = (
                PlansSingleGetResponseDataRelationshipsWorkItems.from_dict(
                    _work_items
                )
            )

        plans_single_get_response_data_relationships_obj = cls(
            author=author,
            parent=parent,
            project=project,
            project_span=project_span,
            template=template,
            work_items=work_items,
        )

        plans_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return plans_single_get_response_data_relationships_obj

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
