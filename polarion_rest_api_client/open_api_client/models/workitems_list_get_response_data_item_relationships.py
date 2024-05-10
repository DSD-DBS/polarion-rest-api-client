# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitems_list_get_response_data_item_relationships_approvals import (
        WorkitemsListGetResponseDataItemRelationshipsApprovals,
    )
    from ..models.workitems_list_get_response_data_item_relationships_assignee import (
        WorkitemsListGetResponseDataItemRelationshipsAssignee,
    )
    from ..models.workitems_list_get_response_data_item_relationships_attachments import (
        WorkitemsListGetResponseDataItemRelationshipsAttachments,
    )
    from ..models.workitems_list_get_response_data_item_relationships_author import (
        WorkitemsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.workitems_list_get_response_data_item_relationships_backlinked_work_items import (
        WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItems,
    )
    from ..models.workitems_list_get_response_data_item_relationships_categories import (
        WorkitemsListGetResponseDataItemRelationshipsCategories,
    )
    from ..models.workitems_list_get_response_data_item_relationships_comments import (
        WorkitemsListGetResponseDataItemRelationshipsComments,
    )
    from ..models.workitems_list_get_response_data_item_relationships_externally_linked_work_items import (
        WorkitemsListGetResponseDataItemRelationshipsExternallyLinkedWorkItems,
    )
    from ..models.workitems_list_get_response_data_item_relationships_linked_oslc_resources import (
        WorkitemsListGetResponseDataItemRelationshipsLinkedOslcResources,
    )
    from ..models.workitems_list_get_response_data_item_relationships_linked_revisions import (
        WorkitemsListGetResponseDataItemRelationshipsLinkedRevisions,
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
    from ..models.workitems_list_get_response_data_item_relationships_test_steps import (
        WorkitemsListGetResponseDataItemRelationshipsTestSteps,
    )
    from ..models.workitems_list_get_response_data_item_relationships_votes import (
        WorkitemsListGetResponseDataItemRelationshipsVotes,
    )
    from ..models.workitems_list_get_response_data_item_relationships_watches import (
        WorkitemsListGetResponseDataItemRelationshipsWatches,
    )
    from ..models.workitems_list_get_response_data_item_relationships_work_records import (
        WorkitemsListGetResponseDataItemRelationshipsWorkRecords,
    )


T = TypeVar("T", bound="WorkitemsListGetResponseDataItemRelationships")


@_attrs_define
class WorkitemsListGetResponseDataItemRelationships:
    """
    Attributes:
        approvals (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsApprovals]):
        assignee (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsAssignee]):
        attachments (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsAttachments]):
        author (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsAuthor]):
        backlinked_work_items (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItems]):
        categories (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsCategories]):
        comments (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsComments]):
        externally_linked_work_items (Union[Unset,
            WorkitemsListGetResponseDataItemRelationshipsExternallyLinkedWorkItems]):
        linked_oslc_resources (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsLinkedOslcResources]):
        linked_revisions (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsLinkedRevisions]):
        linked_work_items (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems]):
        module (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsModule]):
        planned_in (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsPlannedIn]):
        project (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsProject]):
        test_steps (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsTestSteps]):
        votes (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsVotes]):
        watches (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsWatches]):
        work_records (Union[Unset, WorkitemsListGetResponseDataItemRelationshipsWorkRecords]):
    """

    approvals: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsApprovals"
    ] = UNSET
    assignee: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsAssignee"
    ] = UNSET
    attachments: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsAttachments"
    ] = UNSET
    author: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsAuthor"
    ] = UNSET
    backlinked_work_items: Union[
        Unset,
        "WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItems",
    ] = UNSET
    categories: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsCategories"
    ] = UNSET
    comments: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsComments"
    ] = UNSET
    externally_linked_work_items: Union[
        Unset,
        "WorkitemsListGetResponseDataItemRelationshipsExternallyLinkedWorkItems",
    ] = UNSET
    linked_oslc_resources: Union[
        Unset,
        "WorkitemsListGetResponseDataItemRelationshipsLinkedOslcResources",
    ] = UNSET
    linked_revisions: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsLinkedRevisions"
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
    test_steps: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsTestSteps"
    ] = UNSET
    votes: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsVotes"
    ] = UNSET
    watches: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsWatches"
    ] = UNSET
    work_records: Union[
        Unset, "WorkitemsListGetResponseDataItemRelationshipsWorkRecords"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        approvals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approvals, Unset):
            approvals = self.approvals.to_dict()

        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        backlinked_work_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backlinked_work_items, Unset):
            backlinked_work_items = self.backlinked_work_items.to_dict()

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        comments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        externally_linked_work_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.externally_linked_work_items, Unset):
            externally_linked_work_items = (
                self.externally_linked_work_items.to_dict()
            )

        linked_oslc_resources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linked_oslc_resources, Unset):
            linked_oslc_resources = self.linked_oslc_resources.to_dict()

        linked_revisions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linked_revisions, Unset):
            linked_revisions = self.linked_revisions.to_dict()

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

        test_steps: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.test_steps, Unset):
            test_steps = self.test_steps.to_dict()

        votes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.votes, Unset):
            votes = self.votes.to_dict()

        watches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.watches, Unset):
            watches = self.watches.to_dict()

        work_records: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_records, Unset):
            work_records = self.work_records.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approvals is not UNSET:
            field_dict["approvals"] = approvals
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if author is not UNSET:
            field_dict["author"] = author
        if backlinked_work_items is not UNSET:
            field_dict["backlinkedWorkItems"] = backlinked_work_items
        if categories is not UNSET:
            field_dict["categories"] = categories
        if comments is not UNSET:
            field_dict["comments"] = comments
        if externally_linked_work_items is not UNSET:
            field_dict["externallyLinkedWorkItems"] = (
                externally_linked_work_items
            )
        if linked_oslc_resources is not UNSET:
            field_dict["linkedOslcResources"] = linked_oslc_resources
        if linked_revisions is not UNSET:
            field_dict["linkedRevisions"] = linked_revisions
        if linked_work_items is not UNSET:
            field_dict["linkedWorkItems"] = linked_work_items
        if module is not UNSET:
            field_dict["module"] = module
        if planned_in is not UNSET:
            field_dict["plannedIn"] = planned_in
        if project is not UNSET:
            field_dict["project"] = project
        if test_steps is not UNSET:
            field_dict["testSteps"] = test_steps
        if votes is not UNSET:
            field_dict["votes"] = votes
        if watches is not UNSET:
            field_dict["watches"] = watches
        if work_records is not UNSET:
            field_dict["workRecords"] = work_records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitems_list_get_response_data_item_relationships_approvals import (
            WorkitemsListGetResponseDataItemRelationshipsApprovals,
        )
        from ..models.workitems_list_get_response_data_item_relationships_assignee import (
            WorkitemsListGetResponseDataItemRelationshipsAssignee,
        )
        from ..models.workitems_list_get_response_data_item_relationships_attachments import (
            WorkitemsListGetResponseDataItemRelationshipsAttachments,
        )
        from ..models.workitems_list_get_response_data_item_relationships_author import (
            WorkitemsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.workitems_list_get_response_data_item_relationships_backlinked_work_items import (
            WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItems,
        )
        from ..models.workitems_list_get_response_data_item_relationships_categories import (
            WorkitemsListGetResponseDataItemRelationshipsCategories,
        )
        from ..models.workitems_list_get_response_data_item_relationships_comments import (
            WorkitemsListGetResponseDataItemRelationshipsComments,
        )
        from ..models.workitems_list_get_response_data_item_relationships_externally_linked_work_items import (
            WorkitemsListGetResponseDataItemRelationshipsExternallyLinkedWorkItems,
        )
        from ..models.workitems_list_get_response_data_item_relationships_linked_oslc_resources import (
            WorkitemsListGetResponseDataItemRelationshipsLinkedOslcResources,
        )
        from ..models.workitems_list_get_response_data_item_relationships_linked_revisions import (
            WorkitemsListGetResponseDataItemRelationshipsLinkedRevisions,
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
        from ..models.workitems_list_get_response_data_item_relationships_test_steps import (
            WorkitemsListGetResponseDataItemRelationshipsTestSteps,
        )
        from ..models.workitems_list_get_response_data_item_relationships_votes import (
            WorkitemsListGetResponseDataItemRelationshipsVotes,
        )
        from ..models.workitems_list_get_response_data_item_relationships_watches import (
            WorkitemsListGetResponseDataItemRelationshipsWatches,
        )
        from ..models.workitems_list_get_response_data_item_relationships_work_records import (
            WorkitemsListGetResponseDataItemRelationshipsWorkRecords,
        )

        d = src_dict.copy()
        _approvals = d.pop("approvals", UNSET)
        approvals: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsApprovals
        ]
        if isinstance(_approvals, Unset):
            approvals = UNSET
        else:
            approvals = WorkitemsListGetResponseDataItemRelationshipsApprovals.from_dict(
                _approvals
            )

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

        _backlinked_work_items = d.pop("backlinkedWorkItems", UNSET)
        backlinked_work_items: Union[
            Unset,
            WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItems,
        ]
        if isinstance(_backlinked_work_items, Unset):
            backlinked_work_items = UNSET
        else:
            backlinked_work_items = WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItems.from_dict(
                _backlinked_work_items
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

        _externally_linked_work_items = d.pop(
            "externallyLinkedWorkItems", UNSET
        )
        externally_linked_work_items: Union[
            Unset,
            WorkitemsListGetResponseDataItemRelationshipsExternallyLinkedWorkItems,
        ]
        if isinstance(_externally_linked_work_items, Unset):
            externally_linked_work_items = UNSET
        else:
            externally_linked_work_items = WorkitemsListGetResponseDataItemRelationshipsExternallyLinkedWorkItems.from_dict(
                _externally_linked_work_items
            )

        _linked_oslc_resources = d.pop("linkedOslcResources", UNSET)
        linked_oslc_resources: Union[
            Unset,
            WorkitemsListGetResponseDataItemRelationshipsLinkedOslcResources,
        ]
        if isinstance(_linked_oslc_resources, Unset):
            linked_oslc_resources = UNSET
        else:
            linked_oslc_resources = WorkitemsListGetResponseDataItemRelationshipsLinkedOslcResources.from_dict(
                _linked_oslc_resources
            )

        _linked_revisions = d.pop("linkedRevisions", UNSET)
        linked_revisions: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsLinkedRevisions
        ]
        if isinstance(_linked_revisions, Unset):
            linked_revisions = UNSET
        else:
            linked_revisions = WorkitemsListGetResponseDataItemRelationshipsLinkedRevisions.from_dict(
                _linked_revisions
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

        _test_steps = d.pop("testSteps", UNSET)
        test_steps: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsTestSteps
        ]
        if isinstance(_test_steps, Unset):
            test_steps = UNSET
        else:
            test_steps = WorkitemsListGetResponseDataItemRelationshipsTestSteps.from_dict(
                _test_steps
            )

        _votes = d.pop("votes", UNSET)
        votes: Union[Unset, WorkitemsListGetResponseDataItemRelationshipsVotes]
        if isinstance(_votes, Unset):
            votes = UNSET
        else:
            votes = (
                WorkitemsListGetResponseDataItemRelationshipsVotes.from_dict(
                    _votes
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

        _work_records = d.pop("workRecords", UNSET)
        work_records: Union[
            Unset, WorkitemsListGetResponseDataItemRelationshipsWorkRecords
        ]
        if isinstance(_work_records, Unset):
            work_records = UNSET
        else:
            work_records = WorkitemsListGetResponseDataItemRelationshipsWorkRecords.from_dict(
                _work_records
            )

        workitems_list_get_response_data_item_relationships_obj = cls(
            approvals=approvals,
            assignee=assignee,
            attachments=attachments,
            author=author,
            backlinked_work_items=backlinked_work_items,
            categories=categories,
            comments=comments,
            externally_linked_work_items=externally_linked_work_items,
            linked_oslc_resources=linked_oslc_resources,
            linked_revisions=linked_revisions,
            linked_work_items=linked_work_items,
            module=module,
            planned_in=planned_in,
            project=project,
            test_steps=test_steps,
            votes=votes,
            watches=watches,
            work_records=work_records,
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
