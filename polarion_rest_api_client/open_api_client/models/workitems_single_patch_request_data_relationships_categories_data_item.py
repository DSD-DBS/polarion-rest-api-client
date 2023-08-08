# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.workitems_single_patch_request_data_relationships_categories_data_item_type import (
    WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItem"
)


@define
class WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItem:
    """
    Attributes
    ----------
    type : Union[Unset, WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType]
    id : Union[Unset, str]
    """

    type: Union[
        Unset,
        WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType,
    ] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType(
                _type
            )

        id = d.pop("id", UNSET)

        workitems_single_patch_request_data_relationships_categories_data_item_obj = cls(
            type=type,
            id=id,
        )

        workitems_single_patch_request_data_relationships_categories_data_item_obj.additional_properties = (
            d
        )
        return workitems_single_patch_request_data_relationships_categories_data_item_obj

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
