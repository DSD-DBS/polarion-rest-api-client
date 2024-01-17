# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitems_list_patch_request_data_item_relationships_assignee import (
        WorkitemsListPatchRequestDataItemRelationshipsAssignee,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_categories import (
        WorkitemsListPatchRequestDataItemRelationshipsCategories,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_linked_revisions import (
        WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_votes import (
        WorkitemsListPatchRequestDataItemRelationshipsVotes,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_watches import (
        WorkitemsListPatchRequestDataItemRelationshipsWatches,
    )


T = TypeVar("T", bound="WorkitemsListPatchRequestDataItemRelationships")


@_attrs_define
class WorkitemsListPatchRequestDataItemRelationships:
    """
    Attributes:
        assignee (Union[Unset, WorkitemsListPatchRequestDataItemRelationshipsAssignee]):
        categories (Union[Unset, WorkitemsListPatchRequestDataItemRelationshipsCategories]):
        linked_revisions (Union[Unset, WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions]):
        votes (Union[Unset, WorkitemsListPatchRequestDataItemRelationshipsVotes]):
        watches (Union[Unset, WorkitemsListPatchRequestDataItemRelationshipsWatches]):
    """

    assignee: Union[
        Unset, "WorkitemsListPatchRequestDataItemRelationshipsAssignee"
    ] = UNSET
    categories: Union[
        Unset, "WorkitemsListPatchRequestDataItemRelationshipsCategories"
    ] = UNSET
    linked_revisions: Union[
        Unset, "WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions"
    ] = UNSET
    votes: Union[
        Unset, "WorkitemsListPatchRequestDataItemRelationshipsVotes"
    ] = UNSET
    watches: Union[
        Unset, "WorkitemsListPatchRequestDataItemRelationshipsWatches"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        linked_revisions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linked_revisions, Unset):
            linked_revisions = self.linked_revisions.to_dict()

        votes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.votes, Unset):
            votes = self.votes.to_dict()

        watches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.watches, Unset):
            watches = self.watches.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if categories is not UNSET:
            field_dict["categories"] = categories
        if linked_revisions is not UNSET:
            field_dict["linkedRevisions"] = linked_revisions
        if votes is not UNSET:
            field_dict["votes"] = votes
        if watches is not UNSET:
            field_dict["watches"] = watches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitems_list_patch_request_data_item_relationships_assignee import (
            WorkitemsListPatchRequestDataItemRelationshipsAssignee,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_categories import (
            WorkitemsListPatchRequestDataItemRelationshipsCategories,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_linked_revisions import (
            WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_votes import (
            WorkitemsListPatchRequestDataItemRelationshipsVotes,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_watches import (
            WorkitemsListPatchRequestDataItemRelationshipsWatches,
        )

        d = src_dict.copy()
        _assignee = d.pop("assignee", UNSET)
        assignee: Union[
            Unset, WorkitemsListPatchRequestDataItemRelationshipsAssignee
        ]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = WorkitemsListPatchRequestDataItemRelationshipsAssignee.from_dict(
                _assignee
            )

        _categories = d.pop("categories", UNSET)
        categories: Union[
            Unset, WorkitemsListPatchRequestDataItemRelationshipsCategories
        ]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsListPatchRequestDataItemRelationshipsCategories.from_dict(
                _categories
            )

        _linked_revisions = d.pop("linkedRevisions", UNSET)
        linked_revisions: Union[
            Unset,
            WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions,
        ]
        if isinstance(_linked_revisions, Unset):
            linked_revisions = UNSET
        else:
            linked_revisions = WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions.from_dict(
                _linked_revisions
            )

        _votes = d.pop("votes", UNSET)
        votes: Union[
            Unset, WorkitemsListPatchRequestDataItemRelationshipsVotes
        ]
        if isinstance(_votes, Unset):
            votes = UNSET
        else:
            votes = (
                WorkitemsListPatchRequestDataItemRelationshipsVotes.from_dict(
                    _votes
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: Union[
            Unset, WorkitemsListPatchRequestDataItemRelationshipsWatches
        ]
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = WorkitemsListPatchRequestDataItemRelationshipsWatches.from_dict(
                _watches
            )

        workitems_list_patch_request_data_item_relationships_obj = cls(
            assignee=assignee,
            categories=categories,
            linked_revisions=linked_revisions,
            votes=votes,
            watches=watches,
        )

        workitems_list_patch_request_data_item_relationships_obj.additional_properties = (
            d
        )
        return workitems_list_patch_request_data_item_relationships_obj

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
