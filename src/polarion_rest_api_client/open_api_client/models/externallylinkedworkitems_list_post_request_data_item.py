# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.externallylinkedworkitems_list_post_request_data_item_type import (
    ExternallylinkedworkitemsListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.externallylinkedworkitems_list_post_request_data_item_attributes import (
        ExternallylinkedworkitemsListPostRequestDataItemAttributes,
    )


T = TypeVar("T", bound="ExternallylinkedworkitemsListPostRequestDataItem")


@_attrs_define
class ExternallylinkedworkitemsListPostRequestDataItem:
    """
    Attributes:
        type (Union[Unset, ExternallylinkedworkitemsListPostRequestDataItemType]):
        attributes (Union[Unset, ExternallylinkedworkitemsListPostRequestDataItemAttributes]):
    """

    type: Union[
        Unset, ExternallylinkedworkitemsListPostRequestDataItemType
    ] = UNSET
    attributes: Union[
        Unset, "ExternallylinkedworkitemsListPostRequestDataItemAttributes"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.externallylinkedworkitems_list_post_request_data_item_attributes import (
            ExternallylinkedworkitemsListPostRequestDataItemAttributes,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[
            Unset, ExternallylinkedworkitemsListPostRequestDataItemType
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ExternallylinkedworkitemsListPostRequestDataItemType(_type)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, ExternallylinkedworkitemsListPostRequestDataItemAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ExternallylinkedworkitemsListPostRequestDataItemAttributes.from_dict(
                _attributes
            )

        externallylinkedworkitems_list_post_request_data_item_obj = cls(
            type=type,
            attributes=attributes,
        )

        externallylinkedworkitems_list_post_request_data_item_obj.additional_properties = (
            d
        )
        return externallylinkedworkitems_list_post_request_data_item_obj

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
