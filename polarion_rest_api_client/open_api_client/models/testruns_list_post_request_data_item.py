# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testruns_list_post_request_data_item_type import (
    TestrunsListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_list_post_request_data_item_attributes import (
        TestrunsListPostRequestDataItemAttributes,
    )
    from ..models.testruns_list_post_request_data_item_relationships import (
        TestrunsListPostRequestDataItemRelationships,
    )


T = TypeVar("T", bound="TestrunsListPostRequestDataItem")


@_attrs_define
class TestrunsListPostRequestDataItem:
    """
    Attributes:
        type (Union[Unset, TestrunsListPostRequestDataItemType]):
        attributes (Union[Unset, TestrunsListPostRequestDataItemAttributes]):
        relationships (Union[Unset, TestrunsListPostRequestDataItemRelationships]):
    """

    type: Union[Unset, TestrunsListPostRequestDataItemType] = UNSET
    attributes: Union[
        Unset, "TestrunsListPostRequestDataItemAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "TestrunsListPostRequestDataItemRelationships"
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

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testruns_list_post_request_data_item_attributes import (
            TestrunsListPostRequestDataItemAttributes,
        )
        from ..models.testruns_list_post_request_data_item_relationships import (
            TestrunsListPostRequestDataItemRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, TestrunsListPostRequestDataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunsListPostRequestDataItemType(_type)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, TestrunsListPostRequestDataItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TestrunsListPostRequestDataItemAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, TestrunsListPostRequestDataItemRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                TestrunsListPostRequestDataItemRelationships.from_dict(
                    _relationships
                )
            )

        testruns_list_post_request_data_item_obj = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        testruns_list_post_request_data_item_obj.additional_properties = d
        return testruns_list_post_request_data_item_obj

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