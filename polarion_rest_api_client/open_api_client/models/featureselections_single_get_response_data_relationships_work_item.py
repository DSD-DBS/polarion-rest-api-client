# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.featureselections_single_get_response_data_relationships_work_item_data import (
        FeatureselectionsSingleGetResponseDataRelationshipsWorkItemData,
    )


T = TypeVar(
    "T", bound="FeatureselectionsSingleGetResponseDataRelationshipsWorkItem"
)


@_attrs_define
class FeatureselectionsSingleGetResponseDataRelationshipsWorkItem:
    """
    Attributes:
        data (Union[Unset, FeatureselectionsSingleGetResponseDataRelationshipsWorkItemData]):
    """

    data: Union[
        Unset,
        "FeatureselectionsSingleGetResponseDataRelationshipsWorkItemData",
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.featureselections_single_get_response_data_relationships_work_item_data import (
            FeatureselectionsSingleGetResponseDataRelationshipsWorkItemData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[
            Unset,
            FeatureselectionsSingleGetResponseDataRelationshipsWorkItemData,
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = FeatureselectionsSingleGetResponseDataRelationshipsWorkItemData.from_dict(
                _data
            )

        featureselections_single_get_response_data_relationships_work_item_obj = cls(
            data=data,
        )

        featureselections_single_get_response_data_relationships_work_item_obj.additional_properties = (
            d
        )
        return featureselections_single_get_response_data_relationships_work_item_obj

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