# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrunsSingleGetResponseDataLinks")


@_attrs_define
class TestrunsSingleGetResponseDataLinks:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/testruns/MyTestRunId?revision=1234.
        portal (Union[Unset, str]):  Example: server-host-name/application-
            path/polarion/redirect/project/MyProjectId/testrun?id=MyTestRunId&revision=1234.
    """

    self_: Union[Unset, str] = UNSET
    portal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

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

        testruns_single_get_response_data_links_obj = cls(
            self_=self_,
            portal=portal,
        )

        testruns_single_get_response_data_links_obj.additional_properties = d
        return testruns_single_get_response_data_links_obj

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