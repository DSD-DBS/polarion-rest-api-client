# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkitemsListPostResponseDataItemLinks")


@attr.s(auto_attribs=True)
class WorkitemsListPostResponseDataItemLinks:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/workitems/MyWorkItemId?revision=1234.
        portal (Union[Unset, str]):  Example: server-host-name/application-
            path/polarion/redirect/project/MyProjectId/workitem?id=MyWorkItemId&revision=1234.
    """

    self_: Union[Unset, str] = UNSET
    portal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        portal = self.portal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if portal is not UNSET:
            field_dict["portal"] = portal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self", UNSET)

        portal = d.pop("portal", UNSET)

        workitems_list_post_response_data_item_links_obj = cls(
            self_=self_,
            portal=portal,
        )

        workitems_list_post_response_data_item_links_obj.additional_properties = (
            d
        )
        return workitems_list_post_response_data_item_links_obj

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
