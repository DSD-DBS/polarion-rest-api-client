# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testruns_list_post_request_data_item_relationships_document_data_type import (
    TestrunsListPostRequestDataItemRelationshipsDocumentDataType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="TestrunsListPostRequestDataItemRelationshipsDocumentData"
)


@_attrs_define
class TestrunsListPostRequestDataItemRelationshipsDocumentData:
    """
    Attributes:
        id (Union[Unset, str]):  Example: MyProjectId/MySpaceId/MyDocumentId.
        revision (Union[Unset, str]):  Example: 1234.
        type_ (Union[Unset, TestrunsListPostRequestDataItemRelationshipsDocumentDataType]):
    """

    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    type_: Union[
        Unset, TestrunsListPostRequestDataItemRelationshipsDocumentDataType
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        revision = self.revision

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[
            Unset, TestrunsListPostRequestDataItemRelationshipsDocumentDataType
        ]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = (
                TestrunsListPostRequestDataItemRelationshipsDocumentDataType(
                    _type_
                )
            )

        testruns_list_post_request_data_item_relationships_document_data_obj = cls(
            id=id,
            revision=revision,
            type_=type_,
        )

        testruns_list_post_request_data_item_relationships_document_data_obj.additional_properties = d
        return testruns_list_post_request_data_item_relationships_document_data_obj

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
