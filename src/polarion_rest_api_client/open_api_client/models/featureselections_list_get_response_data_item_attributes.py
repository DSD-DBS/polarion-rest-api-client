# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.featureselections_list_get_response_data_item_attributes_selection_type import (
    FeatureselectionsListGetResponseDataItemAttributesSelectionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureselectionsListGetResponseDataItemAttributes")


@_attrs_define
class FeatureselectionsListGetResponseDataItemAttributes:
    """
    Attributes:
        selection_type (Union[Unset, FeatureselectionsListGetResponseDataItemAttributesSelectionType]):  Example:
            excluded.
    """

    selection_type: Union[
        Unset, FeatureselectionsListGetResponseDataItemAttributesSelectionType
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        selection_type: Union[Unset, str] = UNSET
        if not isinstance(self.selection_type, Unset):
            selection_type = self.selection_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selection_type is not UNSET:
            field_dict["selectionType"] = selection_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _selection_type = d.pop("selectionType", UNSET)
        selection_type: Union[
            Unset,
            FeatureselectionsListGetResponseDataItemAttributesSelectionType,
        ]
        if isinstance(_selection_type, Unset):
            selection_type = UNSET
        else:
            selection_type = FeatureselectionsListGetResponseDataItemAttributesSelectionType(
                _selection_type
            )

        featureselections_list_get_response_data_item_attributes_obj = cls(
            selection_type=selection_type,
        )

        featureselections_list_get_response_data_item_attributes_obj.additional_properties = (
            d
        )
        return featureselections_list_get_response_data_item_attributes_obj

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
