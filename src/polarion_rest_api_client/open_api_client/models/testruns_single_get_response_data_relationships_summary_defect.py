# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_single_get_response_data_relationships_summary_defect_data import (
        TestrunsSingleGetResponseDataRelationshipsSummaryDefectData,
    )


T = TypeVar(
    "T", bound="TestrunsSingleGetResponseDataRelationshipsSummaryDefect"
)


@_attrs_define
class TestrunsSingleGetResponseDataRelationshipsSummaryDefect:
    """
    Attributes:
        data (Union[Unset, TestrunsSingleGetResponseDataRelationshipsSummaryDefectData]):
    """

    data: Union[
        Unset, "TestrunsSingleGetResponseDataRelationshipsSummaryDefectData"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testruns_single_get_response_data_relationships_summary_defect_data import (
            TestrunsSingleGetResponseDataRelationshipsSummaryDefectData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[
            Unset, TestrunsSingleGetResponseDataRelationshipsSummaryDefectData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TestrunsSingleGetResponseDataRelationshipsSummaryDefectData.from_dict(
                _data
            )

        testruns_single_get_response_data_relationships_summary_defect_obj = (
            cls(
                data=data,
            )
        )

        testruns_single_get_response_data_relationships_summary_defect_obj.additional_properties = (
            d
        )
        return (
            testruns_single_get_response_data_relationships_summary_defect_obj
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
