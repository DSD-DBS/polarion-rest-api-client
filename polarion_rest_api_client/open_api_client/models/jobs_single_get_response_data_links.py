# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsSingleGetResponseDataLinks")


@_attrs_define
class JobsSingleGetResponseDataLinks:
    """
    Attributes:
        downloads (Union[Unset, list[str]]):  Example: ['https://example.com/polarion/download/filename1',
            'https://example.com/polarion/download/filename2'].
        log (Union[Unset, str]):  Example: server-host-name/application-path/polarion/job-report?jobId=MyJobId.
        self_ (Union[Unset, str]):  Example: server-host-name/application-path/jobs/MyJobId.
    """

    downloads: Union[Unset, list[str]] = UNSET
    log: Union[Unset, str] = UNSET
    self_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        downloads: Union[Unset, list[str]] = UNSET
        if not isinstance(self.downloads, Unset):
            downloads = self.downloads

        log = self.log

        self_ = self.self_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if log is not UNSET:
            field_dict["log"] = log
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        downloads = cast(list[str], d.pop("downloads", UNSET))

        log = d.pop("log", UNSET)

        self_ = d.pop("self", UNSET)

        jobs_single_get_response_data_links_obj = cls(
            downloads=downloads,
            log=log,
            self_=self_,
        )

        jobs_single_get_response_data_links_obj.additional_properties = d
        return jobs_single_get_response_data_links_obj

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
