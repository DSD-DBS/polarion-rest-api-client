# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportTestCasesRequestBody")


@_attrs_define
class ExportTestCasesRequestBody:
    """
    Attributes:
        query (Union[Unset, str]):  Example: exportExcelQueryString.
        sortby (Union[Unset, str]):  Example: exportExcelSortByString.
        template (Union[Unset, str]):  Example: exportExcelTemplateName.
    """

    query: Union[Unset, str] = UNSET
    sortby: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        sortby = self.sortby

        template = self.template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if sortby is not UNSET:
            field_dict["sortby"] = sortby
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query", UNSET)

        sortby = d.pop("sortby", UNSET)

        template = d.pop("template", UNSET)

        export_test_cases_request_body_obj = cls(
            query=query,
            sortby=sortby,
            template=template,
        )

        export_test_cases_request_body_obj.additional_properties = d
        return export_test_cases_request_body_obj

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
