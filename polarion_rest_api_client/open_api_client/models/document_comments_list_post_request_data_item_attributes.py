# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_list_post_request_data_item_attributes_text import (
        DocumentCommentsListPostRequestDataItemAttributesText,
    )


T = TypeVar("T", bound="DocumentCommentsListPostRequestDataItemAttributes")


@_attrs_define
class DocumentCommentsListPostRequestDataItemAttributes:
    """
    Attributes:
        resolved (Union[Unset, bool]):
        text (Union[Unset, DocumentCommentsListPostRequestDataItemAttributesText]):
    """

    resolved: Union[Unset, bool] = UNSET
    text: Union[
        Unset, "DocumentCommentsListPostRequestDataItemAttributesText"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        resolved = self.resolved

        text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_comments_list_post_request_data_item_attributes_text import (
            DocumentCommentsListPostRequestDataItemAttributesText,
        )

        d = src_dict.copy()
        resolved = d.pop("resolved", UNSET)

        _text = d.pop("text", UNSET)
        text: Union[
            Unset, DocumentCommentsListPostRequestDataItemAttributesText
        ]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = DocumentCommentsListPostRequestDataItemAttributesText.from_dict(
                _text
            )

        document_comments_list_post_request_data_item_attributes_obj = cls(
            resolved=resolved,
            text=text,
        )

        document_comments_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return document_comments_list_post_request_data_item_attributes_obj

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
