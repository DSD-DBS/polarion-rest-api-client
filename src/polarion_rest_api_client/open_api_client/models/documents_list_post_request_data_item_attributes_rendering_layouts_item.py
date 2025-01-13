# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_list_post_request_data_item_attributes_rendering_layouts_item_properties_item import (
        DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem,
    )


T = TypeVar(
    "T", bound="DocumentsListPostRequestDataItemAttributesRenderingLayoutsItem"
)


@_attrs_define
class DocumentsListPostRequestDataItemAttributesRenderingLayoutsItem:
    """
    Attributes:
        label (Union[Unset, str]):  Example: My label.
        layouter (Union[Unset, str]):  Example: paragraph.
        properties (Union[Unset, List['DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem']]):
        type (Union[Unset, str]):  Example: task.
    """

    label: Union[Unset, str] = UNSET
    layouter: Union[Unset, str] = UNSET
    properties: Union[
        Unset,
        List[
            "DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem"
        ],
    ] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        layouter = self.layouter

        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if layouter is not UNSET:
            field_dict["layouter"] = layouter
        if properties is not UNSET:
            field_dict["properties"] = properties
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.documents_list_post_request_data_item_attributes_rendering_layouts_item_properties_item import (
            DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem,
        )

        d = src_dict.copy()
        label = d.pop("label", UNSET)

        layouter = d.pop("layouter", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem.from_dict(
                properties_item_data
            )

            properties.append(properties_item)

        type = d.pop("type", UNSET)

        documents_list_post_request_data_item_attributes_rendering_layouts_item_obj = cls(
            label=label,
            layouter=layouter,
            properties=properties,
            type=type,
        )

        documents_list_post_request_data_item_attributes_rendering_layouts_item_obj.additional_properties = (
            d
        )
        return documents_list_post_request_data_item_attributes_rendering_layouts_item_obj

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
