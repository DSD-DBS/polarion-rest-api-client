# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_single_get_response_data_attributes_status import (
        JobsSingleGetResponseDataAttributesStatus,
    )


T = TypeVar("T", bound="JobsSingleGetResponseDataAttributes")


@_attrs_define
class JobsSingleGetResponseDataAttributes:
    """
    Attributes:
        job_id (Union[Unset, str]):  Example: example.
        name (Union[Unset, str]):  Example: example.
        state (Union[Unset, str]):  Example: example.
        status (Union[Unset, JobsSingleGetResponseDataAttributesStatus]):
    """

    job_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    status: Union[Unset, "JobsSingleGetResponseDataAttributesStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id

        name = self.name

        state = self.state

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jobs_single_get_response_data_attributes_status import (
            JobsSingleGetResponseDataAttributesStatus,
        )

        d = src_dict.copy()
        job_id = d.pop("jobId", UNSET)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, JobsSingleGetResponseDataAttributesStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobsSingleGetResponseDataAttributesStatus.from_dict(
                _status
            )

        jobs_single_get_response_data_attributes_obj = cls(
            job_id=job_id,
            name=name,
            state=state,
            status=status,
        )

        jobs_single_get_response_data_attributes_obj.additional_properties = d
        return jobs_single_get_response_data_attributes_obj

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
