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
    from ..models.teststep_results_list_get_response_data_item_attributes_comment import (
        TeststepResultsListGetResponseDataItemAttributesComment,
    )


T = TypeVar("T", bound="TeststepResultsListGetResponseDataItemAttributes")


@_attrs_define
class TeststepResultsListGetResponseDataItemAttributes:
    """
    Attributes:
        comment (Union[Unset, TeststepResultsListGetResponseDataItemAttributesComment]):
        result (Union[Unset, str]):  Example: passed.
    """

    comment: Union[
        Unset, "TeststepResultsListGetResponseDataItemAttributesComment"
    ] = UNSET
    result: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        comment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststep_results_list_get_response_data_item_attributes_comment import (
            TeststepResultsListGetResponseDataItemAttributesComment,
        )

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: Union[
            Unset, TeststepResultsListGetResponseDataItemAttributesComment
        ]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = TeststepResultsListGetResponseDataItemAttributesComment.from_dict(
                _comment
            )

        result = d.pop("result", UNSET)

        teststep_results_list_get_response_data_item_attributes_obj = cls(
            comment=comment,
            result=result,
        )

        teststep_results_list_get_response_data_item_attributes_obj.additional_properties = d
        return teststep_results_list_get_response_data_item_attributes_obj

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
