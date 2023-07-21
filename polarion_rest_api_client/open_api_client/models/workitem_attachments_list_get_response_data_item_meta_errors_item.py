# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_attachments_list_get_response_data_item_meta_errors_item_source import (
        WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource,
    )


T = TypeVar(
    "T", bound="WorkitemAttachmentsListGetResponseDataItemMetaErrorsItem"
)


@attr.s(auto_attribs=True)
class WorkitemAttachmentsListGetResponseDataItemMetaErrorsItem:
    """
    Attributes:
        status (Union[Unset, str]): HTTP status code applicable to this problem. Example: 400.
        title (Union[Unset, str]): Short, human-readable summary of the problem. Example: Bad Request.
        detail (Union[Unset, str]): Human-readable explanation specific to this occurrence of the problem. Example:
            Unexpected token, BEGIN_ARRAY expected, but was : BEGIN_OBJECT (at $.data).
        source (Union[Unset, WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource]):
    """

    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    source: Union[
        Unset, "WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.workitem_attachments_list_get_response_data_item_meta_errors_item_source import (
            WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource,
        )

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        detail = d.pop("detail", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[
            Unset,
            WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource,
        ]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource.from_dict(
                _source
            )

        workitem_attachments_list_get_response_data_item_meta_errors_item = (
            cls(
                status=status,
                title=title,
                detail=detail,
                source=source,
            )
        )

        workitem_attachments_list_get_response_data_item_meta_errors_item.additional_properties = (
            d
        )
        return (
            workitem_attachments_list_get_response_data_item_meta_errors_item
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
