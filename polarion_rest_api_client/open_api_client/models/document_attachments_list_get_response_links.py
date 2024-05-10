# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentAttachmentsListGetResponseLinks")


@_attrs_define
class DocumentAttachmentsListGetResponseLinks:
    """
    Attributes:
        first (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/spaces/MySpaceId/doc
            uments/MyDocumentId/attachments?page%5Bsize%5D=10&page%5Bnumber%5D=1.
        last (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/spaces/MySpaceId/docu
            ments/MyDocumentId/attachments?page%5Bsize%5D=10&page%5Bnumber%5D=9.
        next_ (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/spaces/MySpaceId/doc
            uments/MyDocumentId/attachments?page%5Bsize%5D=10&page%5Bnumber%5D=6.
        prev (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/spaces/MySpaceId/docu
            ments/MyDocumentId/attachments?page%5Bsize%5D=10&page%5Bnumber%5D=4.
        self_ (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/spaces/MySpaceId/doc
            uments/MyDocumentId/attachments?page%5Bsize%5D=10&page%5Bnumber%5D=5.
    """

    first: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    prev: Union[Unset, str] = UNSET
    self_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        first = self.first

        last = self.last

        next_ = self.next_

        prev = self.prev

        self_ = self.self_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        next_ = d.pop("next", UNSET)

        prev = d.pop("prev", UNSET)

        self_ = d.pop("self", UNSET)

        document_attachments_list_get_response_links_obj = cls(
            first=first,
            last=last,
            next_=next_,
            prev=prev,
            self_=self_,
        )

        document_attachments_list_get_response_links_obj.additional_properties = (
            d
        )
        return document_attachments_list_get_response_links_obj

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
