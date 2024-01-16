# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_list_post_request_data_item_relationships_author_data import (
        DocumentCommentsListPostRequestDataItemRelationshipsAuthorData,
    )


T = TypeVar(
    "T", bound="DocumentCommentsListPostRequestDataItemRelationshipsAuthor"
)


@_attrs_define
class DocumentCommentsListPostRequestDataItemRelationshipsAuthor:
    """
    Attributes:
        data (Union[Unset, DocumentCommentsListPostRequestDataItemRelationshipsAuthorData]):
    """

    data: Union[
        Unset, "DocumentCommentsListPostRequestDataItemRelationshipsAuthorData"
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
        from ..models.document_comments_list_post_request_data_item_relationships_author_data import (
            DocumentCommentsListPostRequestDataItemRelationshipsAuthorData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[
            Unset,
            DocumentCommentsListPostRequestDataItemRelationshipsAuthorData,
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DocumentCommentsListPostRequestDataItemRelationshipsAuthorData.from_dict(
                _data
            )

        document_comments_list_post_request_data_item_relationships_author_obj = cls(
            data=data,
        )

        document_comments_list_post_request_data_item_relationships_author_obj.additional_properties = (
            d
        )
        return document_comments_list_post_request_data_item_relationships_author_obj

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
