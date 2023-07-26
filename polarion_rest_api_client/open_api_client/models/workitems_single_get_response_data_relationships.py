# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitems_single_get_response_data_relationships_assignee import (
        WorkitemsSingleGetResponseDataRelationshipsAssignee,
    )
    from ..models.workitems_single_get_response_data_relationships_attachments import (
        WorkitemsSingleGetResponseDataRelationshipsAttachments,
    )
    from ..models.workitems_single_get_response_data_relationships_author import (
        WorkitemsSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.workitems_single_get_response_data_relationships_categories import (
        WorkitemsSingleGetResponseDataRelationshipsCategories,
    )
    from ..models.workitems_single_get_response_data_relationships_comments import (
        WorkitemsSingleGetResponseDataRelationshipsComments,
    )
    from ..models.workitems_single_get_response_data_relationships_linked_work_items import (
        WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems,
    )
    from ..models.workitems_single_get_response_data_relationships_module import (
        WorkitemsSingleGetResponseDataRelationshipsModule,
    )
    from ..models.workitems_single_get_response_data_relationships_planned_in import (
        WorkitemsSingleGetResponseDataRelationshipsPlannedIn,
    )
    from ..models.workitems_single_get_response_data_relationships_project import (
        WorkitemsSingleGetResponseDataRelationshipsProject,
    )
    from ..models.workitems_single_get_response_data_relationships_watches import (
        WorkitemsSingleGetResponseDataRelationshipsWatches,
    )


T = TypeVar("T", bound="WorkitemsSingleGetResponseDataRelationships")


@attr.s(auto_attribs=True)
class WorkitemsSingleGetResponseDataRelationships:
    """
    Attributes:
        assignee (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsAssignee]):
        attachments (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsAttachments]):
        author (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsAuthor]):
        categories (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsCategories]):
        comments (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsComments]):
        linked_work_items (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems]):
        module (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsModule]):
        planned_in (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsPlannedIn]):
        project (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsProject]):
        watches (Union[Unset, WorkitemsSingleGetResponseDataRelationshipsWatches]):
    """

    assignee: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsAssignee"
    ] = UNSET
    attachments: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsAttachments"
    ] = UNSET
    author: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsAuthor"
    ] = UNSET
    categories: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsCategories"
    ] = UNSET
    comments: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsComments"
    ] = UNSET
    linked_work_items: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems"
    ] = UNSET
    module: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsModule"
    ] = UNSET
    planned_in: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsPlannedIn"
    ] = UNSET
    project: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsProject"
    ] = UNSET
    watches: Union[
        Unset, "WorkitemsSingleGetResponseDataRelationshipsWatches"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        comments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        linked_work_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linked_work_items, Unset):
            linked_work_items = self.linked_work_items.to_dict()

        module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.module, Unset):
            module = self.module.to_dict()

        planned_in: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.planned_in, Unset):
            planned_in = self.planned_in.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        watches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.watches, Unset):
            watches = self.watches.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if author is not UNSET:
            field_dict["author"] = author
        if categories is not UNSET:
            field_dict["categories"] = categories
        if comments is not UNSET:
            field_dict["comments"] = comments
        if linked_work_items is not UNSET:
            field_dict["linkedWorkItems"] = linked_work_items
        if module is not UNSET:
            field_dict["module"] = module
        if planned_in is not UNSET:
            field_dict["plannedIn"] = planned_in
        if project is not UNSET:
            field_dict["project"] = project
        if watches is not UNSET:
            field_dict["watches"] = watches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitems_single_get_response_data_relationships_assignee import (
            WorkitemsSingleGetResponseDataRelationshipsAssignee,
        )
        from ..models.workitems_single_get_response_data_relationships_attachments import (
            WorkitemsSingleGetResponseDataRelationshipsAttachments,
        )
        from ..models.workitems_single_get_response_data_relationships_author import (
            WorkitemsSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.workitems_single_get_response_data_relationships_categories import (
            WorkitemsSingleGetResponseDataRelationshipsCategories,
        )
        from ..models.workitems_single_get_response_data_relationships_comments import (
            WorkitemsSingleGetResponseDataRelationshipsComments,
        )
        from ..models.workitems_single_get_response_data_relationships_linked_work_items import (
            WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems,
        )
        from ..models.workitems_single_get_response_data_relationships_module import (
            WorkitemsSingleGetResponseDataRelationshipsModule,
        )
        from ..models.workitems_single_get_response_data_relationships_planned_in import (
            WorkitemsSingleGetResponseDataRelationshipsPlannedIn,
        )
        from ..models.workitems_single_get_response_data_relationships_project import (
            WorkitemsSingleGetResponseDataRelationshipsProject,
        )
        from ..models.workitems_single_get_response_data_relationships_watches import (
            WorkitemsSingleGetResponseDataRelationshipsWatches,
        )

        d = src_dict.copy()
        _assignee = d.pop("assignee", UNSET)
        assignee: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsAssignee
        ]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = (
                WorkitemsSingleGetResponseDataRelationshipsAssignee.from_dict(
                    _assignee
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsAttachments
        ]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = WorkitemsSingleGetResponseDataRelationshipsAttachments.from_dict(
                _attachments
            )

        _author = d.pop("author", UNSET)
        author: Union[Unset, WorkitemsSingleGetResponseDataRelationshipsAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                WorkitemsSingleGetResponseDataRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _categories = d.pop("categories", UNSET)
        categories: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsCategories
        ]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsSingleGetResponseDataRelationshipsCategories.from_dict(
                _categories
            )

        _comments = d.pop("comments", UNSET)
        comments: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsComments
        ]
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = (
                WorkitemsSingleGetResponseDataRelationshipsComments.from_dict(
                    _comments
                )
            )

        _linked_work_items = d.pop("linkedWorkItems", UNSET)
        linked_work_items: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems
        ]
        if isinstance(_linked_work_items, Unset):
            linked_work_items = UNSET
        else:
            linked_work_items = WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems.from_dict(
                _linked_work_items
            )

        _module = d.pop("module", UNSET)
        module: Union[Unset, WorkitemsSingleGetResponseDataRelationshipsModule]
        if isinstance(_module, Unset):
            module = UNSET
        else:
            module = (
                WorkitemsSingleGetResponseDataRelationshipsModule.from_dict(
                    _module
                )
            )

        _planned_in = d.pop("plannedIn", UNSET)
        planned_in: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsPlannedIn
        ]
        if isinstance(_planned_in, Unset):
            planned_in = UNSET
        else:
            planned_in = (
                WorkitemsSingleGetResponseDataRelationshipsPlannedIn.from_dict(
                    _planned_in
                )
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                WorkitemsSingleGetResponseDataRelationshipsProject.from_dict(
                    _project
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: Union[
            Unset, WorkitemsSingleGetResponseDataRelationshipsWatches
        ]
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = (
                WorkitemsSingleGetResponseDataRelationshipsWatches.from_dict(
                    _watches
                )
            )

        workitems_single_get_response_data_relationships_obj = cls(
            assignee=assignee,
            attachments=attachments,
            author=author,
            categories=categories,
            comments=comments,
            linked_work_items=linked_work_items,
            module=module,
            planned_in=planned_in,
            project=project,
            watches=watches,
        )

        workitems_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return workitems_single_get_response_data_relationships_obj

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
