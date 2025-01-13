# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_single_get_response_data_attributes_status_type import (
    JobsSingleGetResponseDataAttributesStatusType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsSingleGetResponseDataAttributesStatus")


@_attrs_define
class JobsSingleGetResponseDataAttributesStatus:
    """
    Attributes:
        message (Union[Unset, str]):  Example: message.
        type (Union[Unset, JobsSingleGetResponseDataAttributesStatusType]):
    """

    message: Union[Unset, str] = UNSET
    type: Union[Unset, JobsSingleGetResponseDataAttributesStatusType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, JobsSingleGetResponseDataAttributesStatusType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = JobsSingleGetResponseDataAttributesStatusType(_type)

        jobs_single_get_response_data_attributes_status_obj = cls(
            message=message,
            type=type,
        )

        jobs_single_get_response_data_attributes_status_obj.additional_properties = (
            d
        )
        return jobs_single_get_response_data_attributes_status_obj

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
