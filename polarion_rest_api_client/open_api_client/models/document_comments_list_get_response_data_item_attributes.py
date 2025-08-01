# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_list_get_response_data_item_attributes_text import (
        DocumentCommentsListGetResponseDataItemAttributesText,
    )


T = TypeVar("T", bound="DocumentCommentsListGetResponseDataItemAttributes")


@_attrs_define
class DocumentCommentsListGetResponseDataItemAttributes:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        id (Union[Unset, str]):  Example: MyCommentId.
        resolved (Union[Unset, bool]):
        text (Union[Unset, DocumentCommentsListGetResponseDataItemAttributesText]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    resolved: Union[Unset, bool] = UNSET
    text: Union[
        Unset, "DocumentCommentsListGetResponseDataItemAttributesText"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        resolved = self.resolved

        text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_comments_list_get_response_data_item_attributes_text import (
            DocumentCommentsListGetResponseDataItemAttributesText,
        )

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        id = d.pop("id", UNSET)

        resolved = d.pop("resolved", UNSET)

        _text = d.pop("text", UNSET)
        text: Union[
            Unset, DocumentCommentsListGetResponseDataItemAttributesText
        ]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = DocumentCommentsListGetResponseDataItemAttributesText.from_dict(
                _text
            )

        document_comments_list_get_response_data_item_attributes_obj = cls(
            created=created,
            id=id,
            resolved=resolved,
            text=text,
        )

        document_comments_list_get_response_data_item_attributes_obj.additional_properties = d
        return document_comments_list_get_response_data_item_attributes_obj

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
