# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.testrun_attachments_list_post_request import (
        TestrunAttachmentsListPostRequest,
    )


T = TypeVar("T", bound="PostTestRunAttachmentsRequestBody")


@_attrs_define
class PostTestRunAttachmentsRequestBody:
    """
    Attributes:
        resource (Union[Unset, TestrunAttachmentsListPostRequest]):
        files (Union[Unset, List[File]]):
    """

    resource: Union[Unset, "TestrunAttachmentsListPostRequest"] = UNSET
    files: Union[Unset, List[File]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        files: Union[Unset, List[FileJsonType]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                files.append(files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource is not UNSET:
            field_dict["resource"] = resource
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    def to_multipart(self) -> List[Tuple[str, Any]]:
        field_list: List[Tuple[str, Any]] = []
        resource: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = (
                None,
                json.dumps(self.resource.to_dict()).encode(),
                "text/plain",
            )

        if resource is not UNSET:
            field_list.append(("resource", resource))
        for cont in self.files or []:
            files_item = cont.to_tuple()

            field_list.append(("files", files_item))

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )

        field_list += list(field_dict.items())

        return field_list

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrun_attachments_list_post_request import (
            TestrunAttachmentsListPostRequest,
        )

        d = src_dict.copy()
        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, TestrunAttachmentsListPostRequest]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = TestrunAttachmentsListPostRequest.from_dict(_resource)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File(payload=BytesIO(files_item_data))

            files.append(files_item)

        post_test_run_attachments_request_body_obj = cls(
            resource=resource,
            files=files,
        )

        post_test_run_attachments_request_body_obj.additional_properties = d
        return post_test_run_attachments_request_body_obj

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