# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workitem_approvals_single_get_response_data_attributes_status import (
    WorkitemApprovalsSingleGetResponseDataAttributesStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkitemApprovalsSingleGetResponseDataAttributes")


@_attrs_define
class WorkitemApprovalsSingleGetResponseDataAttributes:
    """
    Attributes:
        status (Union[Unset, WorkitemApprovalsSingleGetResponseDataAttributesStatus]):  Example: waiting.
    """

    status: Union[
        Unset, WorkitemApprovalsSingleGetResponseDataAttributesStatus
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[
            Unset, WorkitemApprovalsSingleGetResponseDataAttributesStatus
        ]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WorkitemApprovalsSingleGetResponseDataAttributesStatus(
                _status
            )

        workitem_approvals_single_get_response_data_attributes_obj = cls(
            status=status,
        )

        workitem_approvals_single_get_response_data_attributes_obj.additional_properties = (
            d
        )
        return workitem_approvals_single_get_response_data_attributes_obj

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