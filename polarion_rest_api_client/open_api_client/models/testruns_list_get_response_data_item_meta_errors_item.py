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
    from ..models.testruns_list_get_response_data_item_meta_errors_item_source import (
        TestrunsListGetResponseDataItemMetaErrorsItemSource,
    )


T = TypeVar("T", bound="TestrunsListGetResponseDataItemMetaErrorsItem")


@_attrs_define
class TestrunsListGetResponseDataItemMetaErrorsItem:
    """
    Attributes:
        detail (Union[Unset, str]): Human-readable explanation specific to this occurrence of the problem. Example:
            Unexpected token, BEGIN_ARRAY expected, but was : BEGIN_OBJECT (at $.data).
        source (Union[Unset, TestrunsListGetResponseDataItemMetaErrorsItemSource]):
        status (Union[Unset, str]): HTTP status code applicable to this problem. Example: 400.
        title (Union[Unset, str]): Short, human-readable summary of the problem. Example: Bad Request.
    """

    detail: Union[Unset, str] = UNSET
    source: Union[
        Unset, "TestrunsListGetResponseDataItemMetaErrorsItemSource"
    ] = UNSET
    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        status = self.status

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testruns_list_get_response_data_item_meta_errors_item_source import (
            TestrunsListGetResponseDataItemMetaErrorsItemSource,
        )

        d = dict(src_dict)
        detail = d.pop("detail", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[
            Unset, TestrunsListGetResponseDataItemMetaErrorsItemSource
        ]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = (
                TestrunsListGetResponseDataItemMetaErrorsItemSource.from_dict(
                    _source
                )
            )

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        testruns_list_get_response_data_item_meta_errors_item_obj = cls(
            detail=detail,
            source=source,
            status=status,
            title=title,
        )

        testruns_list_get_response_data_item_meta_errors_item_obj.additional_properties = d
        return testruns_list_get_response_data_item_meta_errors_item_obj

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
