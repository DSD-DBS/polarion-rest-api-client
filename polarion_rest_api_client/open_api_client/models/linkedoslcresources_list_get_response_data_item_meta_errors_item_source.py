# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linkedoslcresources_list_get_response_data_item_meta_errors_item_source_resource import (
        LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSourceResource,
    )


T = TypeVar(
    "T", bound="LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSource"
)


@_attrs_define
class LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSource:
    """
    Attributes:
        parameter (Union[Unset, str]): String indicating which URI query parameter caused the error. Example: revision.
        pointer (Union[Unset, str]): JSON Pointer to the associated entity in the request document. Example: $.data.
        resource (Union[Unset, LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSourceResource]): Resource
            causing the error.
    """

    parameter: Union[Unset, str] = UNSET
    pointer: Union[Unset, str] = UNSET
    resource: Union[
        Unset,
        "LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSourceResource",
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        parameter = self.parameter

        pointer = self.pointer

        resource: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linkedoslcresources_list_get_response_data_item_meta_errors_item_source_resource import (
            LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSourceResource,
        )

        d = dict(src_dict)
        parameter = d.pop("parameter", UNSET)

        pointer = d.pop("pointer", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: Union[
            Unset,
            LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSourceResource,
        ]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = LinkedoslcresourcesListGetResponseDataItemMetaErrorsItemSourceResource.from_dict(
                _resource
            )

        linkedoslcresources_list_get_response_data_item_meta_errors_item_source_obj = cls(
            parameter=parameter,
            pointer=pointer,
            resource=resource,
        )

        linkedoslcresources_list_get_response_data_item_meta_errors_item_source_obj.additional_properties = d
        return linkedoslcresources_list_get_response_data_item_meta_errors_item_source_obj

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
