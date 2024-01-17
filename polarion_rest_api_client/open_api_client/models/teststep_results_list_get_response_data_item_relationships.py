# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststep_results_list_get_response_data_item_relationships_test_step import (
        TeststepResultsListGetResponseDataItemRelationshipsTestStep,
    )


T = TypeVar("T", bound="TeststepResultsListGetResponseDataItemRelationships")


@_attrs_define
class TeststepResultsListGetResponseDataItemRelationships:
    """
    Attributes:
        test_step (Union[Unset, TeststepResultsListGetResponseDataItemRelationshipsTestStep]):
    """

    test_step: Union[
        Unset, "TeststepResultsListGetResponseDataItemRelationshipsTestStep"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        test_step: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.test_step, Unset):
            test_step = self.test_step.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test_step is not UNSET:
            field_dict["testStep"] = test_step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.teststep_results_list_get_response_data_item_relationships_test_step import (
            TeststepResultsListGetResponseDataItemRelationshipsTestStep,
        )

        d = src_dict.copy()
        _test_step = d.pop("testStep", UNSET)
        test_step: Union[
            Unset, TeststepResultsListGetResponseDataItemRelationshipsTestStep
        ]
        if isinstance(_test_step, Unset):
            test_step = UNSET
        else:
            test_step = TeststepResultsListGetResponseDataItemRelationshipsTestStep.from_dict(
                _test_step
            )

        teststep_results_list_get_response_data_item_relationships_obj = cls(
            test_step=test_step,
        )

        teststep_results_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return teststep_results_list_get_response_data_item_relationships_obj

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
