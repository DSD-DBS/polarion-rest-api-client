# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_single_get_response_data_attributes_rendering_layouts_item_properties_item import (
        DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem,
    )


T = TypeVar(
    "T", bound="DocumentsSingleGetResponseDataAttributesRenderingLayoutsItem"
)


@_attrs_define
class DocumentsSingleGetResponseDataAttributesRenderingLayoutsItem:
    """
    Attributes
    ----------
    type : Union[Unset, str]
    label : Union[Unset, str]
    layouter : Union[Unset, str]
    properties : Union[Unset, List['DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem']]
    """

    type: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    layouter: Union[Unset, str] = UNSET
    properties: Union[
        Unset,
        List[
            "DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem"
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        label = self.label
        layouter = self.layouter
        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()

                properties.append(properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if label is not UNSET:
            field_dict["label"] = label
        if layouter is not UNSET:
            field_dict["layouter"] = layouter
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.documents_single_get_response_data_attributes_rendering_layouts_item_properties_item import (
            DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem,
        )

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        layouter = d.pop("layouter", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem.from_dict(
                properties_item_data
            )

            properties.append(properties_item)

        documents_single_get_response_data_attributes_rendering_layouts_item_obj = cls(
            type=type,
            label=label,
            layouter=layouter,
            properties=properties,
        )

        documents_single_get_response_data_attributes_rendering_layouts_item_obj.additional_properties = (
            d
        )
        return documents_single_get_response_data_attributes_rendering_layouts_item_obj

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
