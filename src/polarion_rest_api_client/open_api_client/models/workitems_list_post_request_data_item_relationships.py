# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitems_list_post_request_data_item_relationships_assignee import (
        WorkitemsListPostRequestDataItemRelationshipsAssignee,
    )
    from ..models.workitems_list_post_request_data_item_relationships_author import (
        WorkitemsListPostRequestDataItemRelationshipsAuthor,
    )
    from ..models.workitems_list_post_request_data_item_relationships_categories import (
        WorkitemsListPostRequestDataItemRelationshipsCategories,
    )
    from ..models.workitems_list_post_request_data_item_relationships_linked_revisions import (
        WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions,
    )
    from ..models.workitems_list_post_request_data_item_relationships_module import (
        WorkitemsListPostRequestDataItemRelationshipsModule,
    )


T = TypeVar("T", bound="WorkitemsListPostRequestDataItemRelationships")


@_attrs_define
class WorkitemsListPostRequestDataItemRelationships:
    """
    Attributes:
        assignee (Union[Unset, WorkitemsListPostRequestDataItemRelationshipsAssignee]):
        author (Union[Unset, WorkitemsListPostRequestDataItemRelationshipsAuthor]):
        categories (Union[Unset, WorkitemsListPostRequestDataItemRelationshipsCategories]):
        linked_revisions (Union[Unset, WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions]):
        module (Union[Unset, WorkitemsListPostRequestDataItemRelationshipsModule]):
    """

    assignee: Union[
        Unset, "WorkitemsListPostRequestDataItemRelationshipsAssignee"
    ] = UNSET
    author: Union[
        Unset, "WorkitemsListPostRequestDataItemRelationshipsAuthor"
    ] = UNSET
    categories: Union[
        Unset, "WorkitemsListPostRequestDataItemRelationshipsCategories"
    ] = UNSET
    linked_revisions: Union[
        Unset, "WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions"
    ] = UNSET
    module: Union[
        Unset, "WorkitemsListPostRequestDataItemRelationshipsModule"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        linked_revisions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linked_revisions, Unset):
            linked_revisions = self.linked_revisions.to_dict()

        module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.module, Unset):
            module = self.module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if author is not UNSET:
            field_dict["author"] = author
        if categories is not UNSET:
            field_dict["categories"] = categories
        if linked_revisions is not UNSET:
            field_dict["linkedRevisions"] = linked_revisions
        if module is not UNSET:
            field_dict["module"] = module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitems_list_post_request_data_item_relationships_assignee import (
            WorkitemsListPostRequestDataItemRelationshipsAssignee,
        )
        from ..models.workitems_list_post_request_data_item_relationships_author import (
            WorkitemsListPostRequestDataItemRelationshipsAuthor,
        )
        from ..models.workitems_list_post_request_data_item_relationships_categories import (
            WorkitemsListPostRequestDataItemRelationshipsCategories,
        )
        from ..models.workitems_list_post_request_data_item_relationships_linked_revisions import (
            WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions,
        )
        from ..models.workitems_list_post_request_data_item_relationships_module import (
            WorkitemsListPostRequestDataItemRelationshipsModule,
        )

        d = src_dict.copy()
        _assignee = d.pop("assignee", UNSET)
        assignee: Union[
            Unset, WorkitemsListPostRequestDataItemRelationshipsAssignee
        ]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = WorkitemsListPostRequestDataItemRelationshipsAssignee.from_dict(
                _assignee
            )

        _author = d.pop("author", UNSET)
        author: Union[
            Unset, WorkitemsListPostRequestDataItemRelationshipsAuthor
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                WorkitemsListPostRequestDataItemRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _categories = d.pop("categories", UNSET)
        categories: Union[
            Unset, WorkitemsListPostRequestDataItemRelationshipsCategories
        ]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsListPostRequestDataItemRelationshipsCategories.from_dict(
                _categories
            )

        _linked_revisions = d.pop("linkedRevisions", UNSET)
        linked_revisions: Union[
            Unset, WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions
        ]
        if isinstance(_linked_revisions, Unset):
            linked_revisions = UNSET
        else:
            linked_revisions = WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions.from_dict(
                _linked_revisions
            )

        _module = d.pop("module", UNSET)
        module: Union[
            Unset, WorkitemsListPostRequestDataItemRelationshipsModule
        ]
        if isinstance(_module, Unset):
            module = UNSET
        else:
            module = (
                WorkitemsListPostRequestDataItemRelationshipsModule.from_dict(
                    _module
                )
            )

        workitems_list_post_request_data_item_relationships_obj = cls(
            assignee=assignee,
            author=author,
            categories=categories,
            linked_revisions=linked_revisions,
            module=module,
        )

        workitems_list_post_request_data_item_relationships_obj.additional_properties = (
            d
        )
        return workitems_list_post_request_data_item_relationships_obj

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
