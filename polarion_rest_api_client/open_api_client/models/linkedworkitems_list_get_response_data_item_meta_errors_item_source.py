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
    from ..models.linkedworkitems_list_get_response_data_item_meta_errors_item_source_resource import (
        LinkedworkitemsListGetResponseDataItemMetaErrorsItemSourceResource,
    )


T = TypeVar(
    "T", bound="LinkedworkitemsListGetResponseDataItemMetaErrorsItemSource"
)


@_attrs_define
class LinkedworkitemsListGetResponseDataItemMetaErrorsItemSource:
    """
    Attributes:
        parameter (Union[Unset, str]): String indicating which URI query parameter caused the error. Example: revision.
        pointer (Union[Unset, str]): JSON Pointer to the associated entity in the request document. Example: $.data.
        resource (Union[Unset, LinkedworkitemsListGetResponseDataItemMetaErrorsItemSourceResource]): Resource causing
            the error.
    """

    parameter: Union[Unset, str] = UNSET
    pointer: Union[Unset, str] = UNSET
    resource: Union[
        Unset,
        "LinkedworkitemsListGetResponseDataItemMetaErrorsItemSourceResource",
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
        from ..models.linkedworkitems_list_get_response_data_item_meta_errors_item_source_resource import (
            LinkedworkitemsListGetResponseDataItemMetaErrorsItemSourceResource,
        )

        d = dict(src_dict)
        parameter = d.pop("parameter", UNSET)

        pointer = d.pop("pointer", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: Union[
            Unset,
            LinkedworkitemsListGetResponseDataItemMetaErrorsItemSourceResource,
        ]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = LinkedworkitemsListGetResponseDataItemMetaErrorsItemSourceResource.from_dict(
                _resource
            )

        linkedworkitems_list_get_response_data_item_meta_errors_item_source_obj = cls(
            parameter=parameter,
            pointer=pointer,
            resource=resource,
        )

        linkedworkitems_list_get_response_data_item_meta_errors_item_source_obj.additional_properties = d
        return linkedworkitems_list_get_response_data_item_meta_errors_item_source_obj

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
