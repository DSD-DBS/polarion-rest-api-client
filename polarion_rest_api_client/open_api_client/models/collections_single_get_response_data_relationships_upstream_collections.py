# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collections_single_get_response_data_relationships_upstream_collections_data_item import (
        CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsDataItem,
    )
    from ..models.collections_single_get_response_data_relationships_upstream_collections_meta import (
        CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsMeta,
    )


T = TypeVar(
    "T",
    bound="CollectionsSingleGetResponseDataRelationshipsUpstreamCollections",
)


@_attrs_define
class CollectionsSingleGetResponseDataRelationshipsUpstreamCollections:
    """
    Attributes:
        data (Union[Unset, List['CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsDataItem']]):
        meta (Union[Unset, CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsMeta]):
    """

    data: Union[
        Unset,
        List[
            "CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsDataItem"
        ],
    ] = UNSET
    meta: Union[
        Unset,
        "CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsMeta",
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collections_single_get_response_data_relationships_upstream_collections_data_item import (
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsDataItem,
        )
        from ..models.collections_single_get_response_data_relationships_upstream_collections_meta import (
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsMeta,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[
            Unset,
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsMeta,
        ]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = CollectionsSingleGetResponseDataRelationshipsUpstreamCollectionsMeta.from_dict(
                _meta
            )

        collections_single_get_response_data_relationships_upstream_collections_obj = cls(
            data=data,
            meta=meta,
        )

        collections_single_get_response_data_relationships_upstream_collections_obj.additional_properties = (
            d
        )
        return collections_single_get_response_data_relationships_upstream_collections_obj

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
