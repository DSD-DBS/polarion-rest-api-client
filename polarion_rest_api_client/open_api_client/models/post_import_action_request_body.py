# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.import_test_results_request_body import (
        ImportTestResultsRequestBody,
    )


T = TypeVar("T", bound="PostImportActionRequestBody")


@_attrs_define
class PostImportActionRequestBody:
    """
    Attributes:
        file (File): excel file content
        resource (Union[Unset, ImportTestResultsRequestBody]):
    """

    file: File
    resource: Union[Unset, "ImportTestResultsRequestBody"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        resource: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    def to_multipart(self) -> list[tuple[str, Any]]:
        field_list: list[tuple[str, Any]] = []
        file = self.file.to_tuple()

        field_list.append(("file", file))
        resource: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = (
                None,
                json.dumps(self.resource.to_dict()).encode(),
                "text/plain",
            )

        if resource is not UNSET:
            field_list.append(("resource", resource))

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_list += list(field_dict.items())

        return field_list

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_test_results_request_body import (
            ImportTestResultsRequestBody,
        )

        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, ImportTestResultsRequestBody]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = ImportTestResultsRequestBody.from_dict(_resource)

        post_import_action_request_body_obj = cls(
            file=file,
            resource=resource,
        )

        post_import_action_request_body_obj.additional_properties = d
        return post_import_action_request_body_obj

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
