# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentCommentsListGetResponseLinks")


@attr.s(auto_attribs=True)
class DocumentCommentsListGetResponseLinks:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/spaces/MySpaceId/documents/MyDocumentId/comments?page%5Bsize%5D=10&page%5Bnumber%5D=5.
        first (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/spaces/MySpaceId/documents/MyDocumentId/comments?page%5Bsize%5D=10&page%5Bnumber%5D=1.
        prev (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/spaces/MySpaceId/documents/MyDocumentId/comments?page%5Bsize%5D=10&page%5Bnumber%5D=4.
        next_ (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/spaces/MySpaceId/documents/MyDocumentId/comments?page%5Bsize%5D=10&page%5Bnumber%5D=6.
        last (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/spaces/MySpaceId/documents/MyDocumentId/comments?page%5Bsize%5D=10&page%5Bnumber%5D=9.
    """

    self_: Union[Unset, str] = UNSET
    first: Union[Unset, str] = UNSET
    prev: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        first = self.first
        prev = self.prev
        next_ = self.next_
        last = self.last

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if first is not UNSET:
            field_dict["first"] = first
        if prev is not UNSET:
            field_dict["prev"] = prev
        if next_ is not UNSET:
            field_dict["next"] = next_
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self", UNSET)

        first = d.pop("first", UNSET)

        prev = d.pop("prev", UNSET)

        next_ = d.pop("next", UNSET)

        last = d.pop("last", UNSET)

        document_comments_list_get_response_links = cls(
            self_=self_,
            first=first,
            prev=prev,
            next_=next_,
            last=last,
        )

        document_comments_list_get_response_links.additional_properties = d
        return document_comments_list_get_response_links

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
