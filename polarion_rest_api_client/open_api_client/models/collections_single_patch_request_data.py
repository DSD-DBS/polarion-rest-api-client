# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collections_single_patch_request_data_type import (
    CollectionsSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collections_single_patch_request_data_attributes import (
        CollectionsSinglePatchRequestDataAttributes,
    )
    from ..models.collections_single_patch_request_data_relationships import (
        CollectionsSinglePatchRequestDataRelationships,
    )


T = TypeVar("T", bound="CollectionsSinglePatchRequestData")


@_attrs_define
class CollectionsSinglePatchRequestData:
    """
    Attributes:
        type (Union[Unset, CollectionsSinglePatchRequestDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyCollectionId.
        attributes (Union[Unset, CollectionsSinglePatchRequestDataAttributes]):
        relationships (Union[Unset, CollectionsSinglePatchRequestDataRelationships]):
    """

    type: Union[Unset, CollectionsSinglePatchRequestDataType] = UNSET
    id: Union[Unset, str] = UNSET
    attributes: Union[Unset, "CollectionsSinglePatchRequestDataAttributes"] = (
        UNSET
    )
    relationships: Union[
        Unset, "CollectionsSinglePatchRequestDataRelationships"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

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
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collections_single_patch_request_data_attributes import (
            CollectionsSinglePatchRequestDataAttributes,
        )
        from ..models.collections_single_patch_request_data_relationships import (
            CollectionsSinglePatchRequestDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CollectionsSinglePatchRequestDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CollectionsSinglePatchRequestDataType(_type)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, CollectionsSinglePatchRequestDataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CollectionsSinglePatchRequestDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, CollectionsSinglePatchRequestDataRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                CollectionsSinglePatchRequestDataRelationships.from_dict(
                    _relationships
                )
            )

        collections_single_patch_request_data_obj = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        collections_single_patch_request_data_obj.additional_properties = d
        return collections_single_patch_request_data_obj

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
