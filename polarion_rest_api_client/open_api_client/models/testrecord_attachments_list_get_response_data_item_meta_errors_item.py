# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrecord_attachments_list_get_response_data_item_meta_errors_item_source import (
        TestrecordAttachmentsListGetResponseDataItemMetaErrorsItemSource,
    )


T = TypeVar(
    "T", bound="TestrecordAttachmentsListGetResponseDataItemMetaErrorsItem"
)


@_attrs_define
class TestrecordAttachmentsListGetResponseDataItemMetaErrorsItem:
    """
    Attributes:
        status (Union[Unset, str]): HTTP status code applicable to this problem. Example: 400.
        title (Union[Unset, str]): Short, human-readable summary of the problem. Example: Bad Request.
        detail (Union[Unset, str]): Human-readable explanation specific to this occurrence of the problem. Example:
            Unexpected token, BEGIN_ARRAY expected, but was : BEGIN_OBJECT (at $.data).
        source (Union[Unset, TestrecordAttachmentsListGetResponseDataItemMetaErrorsItemSource]):
    """

    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    source: Union[
        Unset,
        "TestrecordAttachmentsListGetResponseDataItemMetaErrorsItemSource",
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        title = self.title

        detail = self.detail

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrecord_attachments_list_get_response_data_item_meta_errors_item_source import (
            TestrecordAttachmentsListGetResponseDataItemMetaErrorsItemSource,
        )

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        detail = d.pop("detail", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[
            Unset,
            TestrecordAttachmentsListGetResponseDataItemMetaErrorsItemSource,
        ]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = TestrecordAttachmentsListGetResponseDataItemMetaErrorsItemSource.from_dict(
                _source
            )

        testrecord_attachments_list_get_response_data_item_meta_errors_item_obj = cls(
            status=status,
            title=title,
            detail=detail,
            source=source,
        )

        testrecord_attachments_list_get_response_data_item_meta_errors_item_obj.additional_properties = (
            d
        )
        return testrecord_attachments_list_get_response_data_item_meta_errors_item_obj

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