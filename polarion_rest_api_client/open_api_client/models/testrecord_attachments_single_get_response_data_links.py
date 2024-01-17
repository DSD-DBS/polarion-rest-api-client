# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestrecordAttachmentsSingleGetResponseDataLinks")


@_attrs_define
class TestrecordAttachmentsSingleGetResponseDataLinks:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/testruns/MyTestRunId
            /testrecords/MyProjectId/MyTestcaseId/0/attachments/MyAttachmentId?revision=1234.
        content (Union[Unset, str]):  Example: server-host-name/application-path/projects/MyProjectId/testruns/MyTestRun
            Id/testrecords/MyProjectId/MyTestcaseId/0/attachments/MyAttachmentId/content?revision=1234.
    """

    self_: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self", UNSET)

        content = d.pop("content", UNSET)

        testrecord_attachments_single_get_response_data_links_obj = cls(
            self_=self_,
            content=content,
        )

        testrecord_attachments_single_get_response_data_links_obj.additional_properties = (
            d
        )
        return testrecord_attachments_single_get_response_data_links_obj

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
