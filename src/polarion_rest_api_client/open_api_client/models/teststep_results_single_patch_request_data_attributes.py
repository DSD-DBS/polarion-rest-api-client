# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststep_results_single_patch_request_data_attributes_comment import (
        TeststepResultsSinglePatchRequestDataAttributesComment,
    )


T = TypeVar("T", bound="TeststepResultsSinglePatchRequestDataAttributes")


@_attrs_define
class TeststepResultsSinglePatchRequestDataAttributes:
    """
    Attributes:
        comment (Union[Unset, TeststepResultsSinglePatchRequestDataAttributesComment]):
        result (Union[Unset, str]):  Example: passed.
    """

    comment: Union[
        Unset, "TeststepResultsSinglePatchRequestDataAttributesComment"
    ] = UNSET
    result: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.teststep_results_single_patch_request_data_attributes_comment import (
            TeststepResultsSinglePatchRequestDataAttributesComment,
        )

        d = src_dict.copy()
        _comment = d.pop("comment", UNSET)
        comment: Union[
            Unset, TeststepResultsSinglePatchRequestDataAttributesComment
        ]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = TeststepResultsSinglePatchRequestDataAttributesComment.from_dict(
                _comment
            )

        result = d.pop("result", UNSET)

        teststep_results_single_patch_request_data_attributes_obj = cls(
            comment=comment,
            result=result,
        )

        teststep_results_single_patch_request_data_attributes_obj.additional_properties = (
            d
        )
        return teststep_results_single_patch_request_data_attributes_obj

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
