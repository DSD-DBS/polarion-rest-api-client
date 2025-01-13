# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_single_post_response_data_attributes_status_type import (
    JobsSinglePostResponseDataAttributesStatusType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsSinglePostResponseDataAttributesStatus")


@_attrs_define
class JobsSinglePostResponseDataAttributesStatus:
    """Attributes
    message (Union[Unset, str]):  Example: message.
    type (Union[Unset, JobsSinglePostResponseDataAttributesStatusType]):
    """

    message: Unset | str = UNSET
    type: Unset | JobsSinglePostResponseDataAttributesStatusType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _type = d.pop("type", UNSET)
        type: Unset | JobsSinglePostResponseDataAttributesStatusType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = JobsSinglePostResponseDataAttributesStatusType(_type)

        jobs_single_post_response_data_attributes_status_obj = cls(
            message=message,
            type=type,
        )

        jobs_single_post_response_data_attributes_status_obj.additional_properties = d
        return jobs_single_post_response_data_attributes_status_obj

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
