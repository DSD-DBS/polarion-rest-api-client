# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plans_list_get_response_data_item_relationships_project_span_data_item import (
        PlansListGetResponseDataItemRelationshipsProjectSpanDataItem,
    )
    from ..models.plans_list_get_response_data_item_relationships_project_span_meta import (
        PlansListGetResponseDataItemRelationshipsProjectSpanMeta,
    )


T = TypeVar("T", bound="PlansListGetResponseDataItemRelationshipsProjectSpan")


@_attrs_define
class PlansListGetResponseDataItemRelationshipsProjectSpan:
    """
    Attributes:
        data (Union[Unset, List['PlansListGetResponseDataItemRelationshipsProjectSpanDataItem']]):
        meta (Union[Unset, PlansListGetResponseDataItemRelationshipsProjectSpanMeta]):
    """

    data: Union[
        Unset,
        List["PlansListGetResponseDataItemRelationshipsProjectSpanDataItem"],
    ] = UNSET
    meta: Union[
        Unset, "PlansListGetResponseDataItemRelationshipsProjectSpanMeta"
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
        from ..models.plans_list_get_response_data_item_relationships_project_span_data_item import (
            PlansListGetResponseDataItemRelationshipsProjectSpanDataItem,
        )
        from ..models.plans_list_get_response_data_item_relationships_project_span_meta import (
            PlansListGetResponseDataItemRelationshipsProjectSpanMeta,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = PlansListGetResponseDataItemRelationshipsProjectSpanDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[
            Unset, PlansListGetResponseDataItemRelationshipsProjectSpanMeta
        ]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PlansListGetResponseDataItemRelationshipsProjectSpanMeta.from_dict(
                _meta
            )

        plans_list_get_response_data_item_relationships_project_span_obj = cls(
            data=data,
            meta=meta,
        )

        plans_list_get_response_data_item_relationships_project_span_obj.additional_properties = (
            d
        )
        return plans_list_get_response_data_item_relationships_project_span_obj

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
