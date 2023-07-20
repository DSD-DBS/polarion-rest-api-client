# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pages_single_get_response_data_relationships_project_data_type import (
    PagesSingleGetResponseDataRelationshipsProjectDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PagesSingleGetResponseDataRelationshipsProjectData")


@attr.s(auto_attribs=True)
class PagesSingleGetResponseDataRelationshipsProjectData:
    """
    Attributes:
        type (Union[Unset, PagesSingleGetResponseDataRelationshipsProjectDataType]):
        id (Union[Unset, str]):  Example: MyProjectId.
        revision (Union[Unset, str]):  Example: 1234.
    """

    type: Union[
        Unset, PagesSingleGetResponseDataRelationshipsProjectDataType
    ] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id
        revision = self.revision

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[
            Unset, PagesSingleGetResponseDataRelationshipsProjectDataType
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PagesSingleGetResponseDataRelationshipsProjectDataType(
                _type
            )

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        pages_single_get_response_data_relationships_project_data = cls(
            type=type,
            id=id,
            revision=revision,
        )

        pages_single_get_response_data_relationships_project_data.additional_properties = (
            d
        )
        return pages_single_get_response_data_relationships_project_data

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
