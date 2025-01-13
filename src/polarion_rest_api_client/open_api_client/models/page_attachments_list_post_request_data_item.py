# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.page_attachments_list_post_request_data_item_type import (
    PageAttachmentsListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_attachments_list_post_request_data_item_attributes import (
        PageAttachmentsListPostRequestDataItemAttributes,
    )


T = TypeVar("T", bound="PageAttachmentsListPostRequestDataItem")


@_attrs_define
class PageAttachmentsListPostRequestDataItem:
    """Attributes
    type (Union[Unset, PageAttachmentsListPostRequestDataItemType]):
    attributes (Union[Unset, PageAttachmentsListPostRequestDataItemAttributes]):
    lid (Union[Unset, str]):
    """

    type: Unset | PageAttachmentsListPostRequestDataItemType = UNSET
    attributes: Union[
        Unset, "PageAttachmentsListPostRequestDataItemAttributes"
    ] = UNSET
    lid: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        lid = self.lid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if lid is not UNSET:
            field_dict["lid"] = lid

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        from ..models.page_attachments_list_post_request_data_item_attributes import (
            PageAttachmentsListPostRequestDataItemAttributes,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Unset | PageAttachmentsListPostRequestDataItemType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PageAttachmentsListPostRequestDataItemType(_type)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | PageAttachmentsListPostRequestDataItemAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                PageAttachmentsListPostRequestDataItemAttributes.from_dict(
                    _attributes
                )
            )

        lid = d.pop("lid", UNSET)

        page_attachments_list_post_request_data_item_obj = cls(
            type=type,
            attributes=attributes,
            lid=lid,
        )

        page_attachments_list_post_request_data_item_obj.additional_properties = d
        return page_attachments_list_post_request_data_item_obj

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
