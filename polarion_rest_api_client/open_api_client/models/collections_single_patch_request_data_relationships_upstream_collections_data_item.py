# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collections_single_patch_request_data_relationships_upstream_collections_data_item_type import (
    CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItem",
)


@_attrs_define
class CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: MyProjectId/MyCollectionId.
        revision (Union[Unset, str]):  Example: 1234.
        type (Union[Unset, CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItemType]):
    """

    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    type: Union[
        Unset,
        CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItemType,
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        revision = self.revision

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItemType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CollectionsSinglePatchRequestDataRelationshipsUpstreamCollectionsDataItemType(
                _type
            )

        collections_single_patch_request_data_relationships_upstream_collections_data_item_obj = cls(
            id=id,
            revision=revision,
            type=type,
        )

        collections_single_patch_request_data_relationships_upstream_collections_data_item_obj.additional_properties = (
            d
        )
        return collections_single_patch_request_data_relationships_upstream_collections_data_item_obj

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
