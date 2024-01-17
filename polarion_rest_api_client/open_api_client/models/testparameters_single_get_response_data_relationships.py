# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testparameters_single_get_response_data_relationships_definition import (
        TestparametersSingleGetResponseDataRelationshipsDefinition,
    )


T = TypeVar("T", bound="TestparametersSingleGetResponseDataRelationships")


@_attrs_define
class TestparametersSingleGetResponseDataRelationships:
    """
    Attributes:
        definition (Union[Unset, TestparametersSingleGetResponseDataRelationshipsDefinition]):
    """

    definition: Union[
        Unset, "TestparametersSingleGetResponseDataRelationshipsDefinition"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if definition is not UNSET:
            field_dict["definition"] = definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testparameters_single_get_response_data_relationships_definition import (
            TestparametersSingleGetResponseDataRelationshipsDefinition,
        )

        d = src_dict.copy()
        _definition = d.pop("definition", UNSET)
        definition: Union[
            Unset, TestparametersSingleGetResponseDataRelationshipsDefinition
        ]
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = TestparametersSingleGetResponseDataRelationshipsDefinition.from_dict(
                _definition
            )

        testparameters_single_get_response_data_relationships_obj = cls(
            definition=definition,
        )

        testparameters_single_get_response_data_relationships_obj.additional_properties = (
            d
        )
        return testparameters_single_get_response_data_relationships_obj

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
