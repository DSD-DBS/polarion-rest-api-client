# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportTestResultsRequestBody")


@_attrs_define
class ImportTestResultsRequestBody:
    """
    Attributes:
        retest (Union[Unset, bool]):
        defect_template_id (Union[Unset, str]):  Example: MyProjectId/MyDefectId.
    """

    retest: Union[Unset, bool] = UNSET
    defect_template_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        retest = self.retest

        defect_template_id = self.defect_template_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retest is not UNSET:
            field_dict["retest"] = retest
        if defect_template_id is not UNSET:
            field_dict["defectTemplateId"] = defect_template_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        retest = d.pop("retest", UNSET)

        defect_template_id = d.pop("defectTemplateId", UNSET)

        import_test_results_request_body_obj = cls(
            retest=retest,
            defect_template_id=defect_template_id,
        )

        import_test_results_request_body_obj.additional_properties = d
        return import_test_results_request_body_obj

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
