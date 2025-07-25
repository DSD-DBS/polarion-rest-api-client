# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.users_single_patch_request_data_type import (
    UsersSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.users_single_patch_request_data_attributes import (
        UsersSinglePatchRequestDataAttributes,
    )
    from ..models.users_single_patch_request_data_relationships import (
        UsersSinglePatchRequestDataRelationships,
    )


T = TypeVar("T", bound="UsersSinglePatchRequestData")


@_attrs_define
class UsersSinglePatchRequestData:
    """
    Attributes:
        type_ (Union[Unset, UsersSinglePatchRequestDataType]):
        id (Union[Unset, str]):  Example: MyUserId.
        attributes (Union[Unset, UsersSinglePatchRequestDataAttributes]):
        relationships (Union[Unset, UsersSinglePatchRequestDataRelationships]):
    """

    type_: Union[Unset, UsersSinglePatchRequestDataType] = UNSET
    id: Union[Unset, str] = UNSET
    attributes: Union[Unset, "UsersSinglePatchRequestDataAttributes"] = UNSET
    relationships: Union[Unset, "UsersSinglePatchRequestDataRelationships"] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_single_patch_request_data_attributes import (
            UsersSinglePatchRequestDataAttributes,
        )
        from ..models.users_single_patch_request_data_relationships import (
            UsersSinglePatchRequestDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, UsersSinglePatchRequestDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UsersSinglePatchRequestDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, UsersSinglePatchRequestDataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UsersSinglePatchRequestDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, UsersSinglePatchRequestDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = UsersSinglePatchRequestDataRelationships.from_dict(
                _relationships
            )

        users_single_patch_request_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        users_single_patch_request_data_obj.additional_properties = d
        return users_single_patch_request_data_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
