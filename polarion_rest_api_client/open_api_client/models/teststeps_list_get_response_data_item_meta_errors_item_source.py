# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststeps_list_get_response_data_item_meta_errors_item_source_resource import (
        TeststepsListGetResponseDataItemMetaErrorsItemSourceResource,
    )


T = TypeVar("T", bound="TeststepsListGetResponseDataItemMetaErrorsItemSource")


@_attrs_define
class TeststepsListGetResponseDataItemMetaErrorsItemSource:
    """
    Attributes:
        pointer (Union[Unset, str]): JSON Pointer to the associated entity in the request document. Example: $.data.
        parameter (Union[Unset, str]): String indicating which URI query parameter caused the error. Example: revision.
        resource (Union[Unset, TeststepsListGetResponseDataItemMetaErrorsItemSourceResource]): Resource causing the
            error.
    """

    pointer: Union[Unset, str] = UNSET
    parameter: Union[Unset, str] = UNSET
    resource: Union[
        Unset, "TeststepsListGetResponseDataItemMetaErrorsItemSourceResource"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pointer = self.pointer

        parameter = self.parameter

        resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.teststeps_list_get_response_data_item_meta_errors_item_source_resource import (
            TeststepsListGetResponseDataItemMetaErrorsItemSourceResource,
        )

        d = src_dict.copy()
        pointer = d.pop("pointer", UNSET)

        parameter = d.pop("parameter", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: Union[
            Unset, TeststepsListGetResponseDataItemMetaErrorsItemSourceResource
        ]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = TeststepsListGetResponseDataItemMetaErrorsItemSourceResource.from_dict(
                _resource
            )

        teststeps_list_get_response_data_item_meta_errors_item_source_obj = (
            cls(
                pointer=pointer,
                parameter=parameter,
                resource=resource,
            )
        )

        teststeps_list_get_response_data_item_meta_errors_item_source_obj.additional_properties = (
            d
        )
        return (
            teststeps_list_get_response_data_item_meta_errors_item_source_obj
        )

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