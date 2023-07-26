# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitems_list_get_response_data_item_relationships_assignee import (
        WorkitemsListGetResponseDataItemRelationshipsAssignee,
    )
    from ..models.workitems_list_get_response_data_item_relationships_attachments import (
        WorkitemsListGetResponseDataItemRelationshipsAttachments,
    )
    from ..models.workitems_list_get_response_data_item_relationships_author import (
        WorkitemsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.workitems_list_get_response_data_item_relationships_categories import (
        WorkitemsListGetResponseDataItemRelationshipsCategories,
    )
    from ..models.workitems_list_get_response_data_item_relationships_comments import (
        WorkitemsListGetResponseDataItemRelationshipsComments,
    )
    from ..models.workitems_list_get_response_data_item_relationships_linked_work_items import (
        WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems,
    )
    from ..models.workitems_list_get_response_data_item_relationships_module import (
        WorkitemsListGetResponseDataItemRelationshipsModule,
    )
    from ..models.workitems_list_get_response_data_item_relationships_planned_in import (
        WorkitemsListGetResponseDataItemRelationshipsPlannedIn,
    )
    from ..models.workitems_list_get_response_data_item_relationships_project import (
        WorkitemsListGetResponseDataItemRelationshipsProject,
    )
    from ..models.workitems_list_get_response_data_item_relationships_watches import (
        WorkitemsListGetResponseDataItemRelationshipsWatches,
    )


T = TypeVar("T", bound="WorkitemsListGetResponseDataItemRelationships")


@attr.s(auto_attribs=True)
class WorkitemsListGetResponseDataItemRelationships:
    """
    Attributes:
        assignee (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsAssignee]):
        attachments (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsAttachments]):
        author (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsAuthor]):
        categories (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsCategories]):
        comments (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsComments]):
        linked_work_items (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems]):
        module (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsModule]):
        planned_in (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsPlannedIn]):
        project (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsProject]):
        watches (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsWatches]):
    """

    assignee: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsAssignee"
    ] = UNSET
    attachments: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsAttachments"
    ] = UNSET
    author: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsAuthor"
    ] = UNSET
    categories: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsCategories"
    ] = UNSET
    comments: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsComments"
    ] = UNSET
    linked_work_items: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems"
    ] = UNSET
    module: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsModule"
    ] = UNSET
    planned_in: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsPlannedIn"
    ] = UNSET
    project: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsProject"
    ] = UNSET
    watches: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsWatches"
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
        from ..models.workitems_list_get_response_data_item_relationships_assignee import (
            WorkitemsListGetResponseDataItemRelationshipsAssignee,
        )
        from ..models.workitems_list_get_response_data_item_relationships_attachments import (
            WorkitemsListGetResponseDataItemRelationshipsAttachments,
        )
        from ..models.workitems_list_get_response_data_item_relationships_author import (
            WorkitemsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.workitems_list_get_response_data_item_relationships_categories import (
            WorkitemsListGetResponseDataItemRelationshipsCategories,
        )
        from ..models.workitems_list_get_response_data_item_relationships_comments import (
            WorkitemsListGetResponseDataItemRelationshipsComments,
        )
        from ..models.workitems_list_get_response_data_item_relationships_linked_work_items import (
            WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems,
        )
        from ..models.workitems_list_get_response_data_item_relationships_module import (
            WorkitemsListGetResponseDataItemRelationshipsModule,
        )
        from ..models.workitems_list_get_response_data_item_relationships_planned_in import (
            WorkitemsListGetResponseDataItemRelationshipsPlannedIn,
        )
        from ..models.workitems_list_get_response_data_item_relationships_project import (
            WorkitemsListGetResponseDataItemRelationshipsProject,
        )
        from ..models.workitems_list_get_response_data_item_relationships_watches import (
            WorkitemsListGetResponseDataItemRelationshipsWatches,
        )

        d = src_dict.copy()
        _assignee = d.pop("assignee", UNSET)
        assignee: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsAssignee
        ]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = WorkitemsListGetResponseDataItemRelationshipsAssignee.from_dict(
                _assignee
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsAttachments
        ]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = WorkitemsListGetResponseDataItemRelationshipsAttachments.from_dict(
                _attachments
            )

        _author = d.pop("author", UNSET)
        author: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsAuthor
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                WorkitemsListGetResponseDataItemRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _categories = d.pop("categories", UNSET)
        categories: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsCategories
        ]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsListGetResponseDataItemRelationshipsCategories.from_dict(
                _categories
            )

        _comments = d.pop("comments", UNSET)
        comments: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsComments
        ]
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = WorkitemsListGetResponseDataItemRelationshipsComments.from_dict(
                _comments
            )

        _linked_work_items = d.pop("linkedWorkItems", UNSET)
        linked_work_items: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems
        ]
        if isinstance(_linked_work_items, Unset):
            linked_work_items = UNSET
        else:
            linked_work_items = WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems.from_dict(
                _linked_work_items
            )

        _module = d.pop("module", UNSET)
        module: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsModule
        ]
        if isinstance(_module, Unset):
            module = UNSET
        else:
            module = (
                WorkitemsListGetResponseDataItemRelationshipsModule.from_dict(
                    _module
                )
            )

        _planned_in = d.pop("plannedIn", UNSET)
        planned_in: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsPlannedIn
        ]
        if isinstance(_planned_in, Unset):
            planned_in = UNSET
        else:
            planned_in = WorkitemsListGetResponseDataItemRelationshipsPlannedIn.from_dict(
                _planned_in
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                WorkitemsListGetResponseDataItemRelationshipsProject.from_dict(
                    _project
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsWatches
        ]
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = (
                WorkitemsListGetResponseDataItemRelationshipsWatches.from_dict(
                    _watches
                )
            )

        workitems_list_get_response_data_item_relationships_obj = cls(
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

        workitems_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return workitems_list_get_response_data_item_relationships_obj

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
