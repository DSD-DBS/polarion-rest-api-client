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
    from ..models.projecttemplates_list_get_response_data_item_meta_errors_item import (
        ProjecttemplatesListGetResponseDataItemMetaErrorsItem,
    )


T = TypeVar("T", bound="ProjecttemplatesListGetResponseDataItemMeta")


@_attrs_define
class ProjecttemplatesListGetResponseDataItemMeta:
    """
    Attributes:
        errors (Union[Unset, list['ProjecttemplatesListGetResponseDataItemMetaErrorsItem']]):
    """

    errors: Union[
        Unset, list["ProjecttemplatesListGetResponseDataItemMetaErrorsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.projecttemplates_list_get_response_data_item_meta_errors_item import (
            ProjecttemplatesListGetResponseDataItemMetaErrorsItem,
        )

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ProjecttemplatesListGetResponseDataItemMetaErrorsItem.from_dict(
                errors_item_data
            )

            errors.append(errors_item)

        projecttemplates_list_get_response_data_item_meta_obj = cls(
            errors=errors,
        )

        projecttemplates_list_get_response_data_item_meta_obj.additional_properties = d
        return projecttemplates_list_get_response_data_item_meta_obj

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
