# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrunsListGetResponseLinks")


@_attrs_define
class TestrunsListGetResponseLinks:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/testruns?page%5Bsize%5D=10&page%5Bnumber%5D=5.
        first (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/testruns?page%5Bsize%5D=10&page%5Bnumber%5D=1.
        prev (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/testruns?page%5Bsize%5D=10&page%5Bnumber%5D=4.
        next_ (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/testruns?page%5Bsize%5D=10&page%5Bnumber%5D=6.
        last (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/testruns?page%5Bsize%5D=10&page%5Bnumber%5D=9.
        portal (Union[Unset, str]):  Example: server-host-name/application-
            path/polarion/redirect/project/MyProjectId/testruns.
    """

    self_: Union[Unset, str] = UNSET
    first: Union[Unset, str] = UNSET
    prev: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    portal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_

        first = self.first

        prev = self.prev

        next_ = self.next_

        last = self.last

        portal = self.portal

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
        if portal is not UNSET:
            field_dict["portal"] = portal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self", UNSET)

        first = d.pop("first", UNSET)

        prev = d.pop("prev", UNSET)

        next_ = d.pop("next", UNSET)

        last = d.pop("last", UNSET)

        portal = d.pop("portal", UNSET)

        testruns_list_get_response_links_obj = cls(
            self_=self_,
            first=first,
            prev=prev,
            next_=next_,
            last=last,
            portal=portal,
        )

        testruns_list_get_response_links_obj.additional_properties = d
        return testruns_list_get_response_links_obj

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