# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.projects_single_patch_request_data_relationships_lead_data_type import (
    ProjectsSinglePatchRequestDataRelationshipsLeadDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsSinglePatchRequestDataRelationshipsLeadData")


@_attrs_define
class ProjectsSinglePatchRequestDataRelationshipsLeadData:
    """Attributes
    id (Union[Unset, str]):  Example: MyUserId.
    type (Union[Unset, ProjectsSinglePatchRequestDataRelationshipsLeadDataType]):
    """

    id: Unset | str = UNSET
    type: Unset | ProjectsSinglePatchRequestDataRelationshipsLeadDataType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Unset | ProjectsSinglePatchRequestDataRelationshipsLeadDataType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ProjectsSinglePatchRequestDataRelationshipsLeadDataType(
                _type
            )

        projects_single_patch_request_data_relationships_lead_data_obj = cls(
            id=id,
            type=type,
        )

        projects_single_patch_request_data_relationships_lead_data_obj.additional_properties = d
        return projects_single_patch_request_data_relationships_lead_data_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
