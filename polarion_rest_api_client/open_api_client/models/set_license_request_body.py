# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.set_license_request_body_license import (
    SetLicenseRequestBodyLicense,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetLicenseRequestBody")


@attr.s(auto_attribs=True)
class SetLicenseRequestBody:
    """
    Attributes:
        license_ (Union[Unset, SetLicenseRequestBodyLicense]): User's license type
        group (Union[Unset, str]): License group Example: Department.
        concurrent (Union[Unset, bool]): Is concurrent user Example: True.
    """

    license_: Union[Unset, SetLicenseRequestBodyLicense] = UNSET
    group: Union[Unset, str] = UNSET
    concurrent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        license_: Union[Unset, str] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.value

        group = self.group
        concurrent = self.concurrent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_ is not UNSET:
            field_dict["license"] = license_
        if group is not UNSET:
            field_dict["group"] = group
        if concurrent is not UNSET:
            field_dict["concurrent"] = concurrent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, SetLicenseRequestBodyLicense]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = SetLicenseRequestBodyLicense(_license_)

        group = d.pop("group", UNSET)

        concurrent = d.pop("concurrent", UNSET)

        set_license_request_body_obj = cls(
            license_=license_,
            group=group,
            concurrent=concurrent,
        )

        set_license_request_body_obj.additional_properties = d
        return set_license_request_body_obj

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
