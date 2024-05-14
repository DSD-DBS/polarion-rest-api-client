# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.errors_errors_item_source_type_0_resource_type_0 import (
        ErrorsErrorsItemSourceType0ResourceType0,
    )


T = TypeVar("T", bound="ErrorsErrorsItemSourceType0")


@_attrs_define
class ErrorsErrorsItemSourceType0:
    """
    Attributes:
        parameter (Union[Unset, str]): String indicating which URI query parameter caused the error. Example: revision.
        pointer (Union[Unset, str]): JSON Pointer to the associated entity in the request document. Example: $.data.
        resource (Union['ErrorsErrorsItemSourceType0ResourceType0', None, Unset]): Resource causing the error.
    """

    parameter: Union[Unset, str] = UNSET
    pointer: Union[Unset, str] = UNSET
    resource: Union[
        "ErrorsErrorsItemSourceType0ResourceType0", None, Unset
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.errors_errors_item_source_type_0_resource_type_0 import (
            ErrorsErrorsItemSourceType0ResourceType0,
        )

        parameter = self.parameter

        pointer = self.pointer

        resource: Union[Dict[str, Any], None, Unset]
        if isinstance(self.resource, Unset):
            resource = UNSET
        elif isinstance(
            self.resource, ErrorsErrorsItemSourceType0ResourceType0
        ):
            resource = self.resource.to_dict()
        else:
            resource = self.resource

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.errors_errors_item_source_type_0_resource_type_0 import (
            ErrorsErrorsItemSourceType0ResourceType0,
        )

        d = src_dict.copy()
        parameter = d.pop("parameter", UNSET)

        pointer = d.pop("pointer", UNSET)

        def _parse_resource(
            data: object,
        ) -> Union["ErrorsErrorsItemSourceType0ResourceType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resource_type_0 = (
                    ErrorsErrorsItemSourceType0ResourceType0.from_dict(data)
                )

                return resource_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["ErrorsErrorsItemSourceType0ResourceType0", None, Unset],
                data,
            )

        resource = _parse_resource(d.pop("resource", UNSET))

        errors_errors_item_source_type_0_obj = cls(
            parameter=parameter,
            pointer=pointer,
            resource=resource,
        )

        errors_errors_item_source_type_0_obj.additional_properties = d
        return errors_errors_item_source_type_0_obj

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
