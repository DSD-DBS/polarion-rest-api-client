# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrecords_list_patch_request_data_item_relationships_defect import (
        TestrecordsListPatchRequestDataItemRelationshipsDefect,
    )
    from ..models.testrecords_list_patch_request_data_item_relationships_executed_by import (
        TestrecordsListPatchRequestDataItemRelationshipsExecutedBy,
    )


T = TypeVar("T", bound="TestrecordsListPatchRequestDataItemRelationships")


@_attrs_define
class TestrecordsListPatchRequestDataItemRelationships:
    """
    Attributes:
        defect (Union[Unset, TestrecordsListPatchRequestDataItemRelationshipsDefect]):
        executed_by (Union[Unset, TestrecordsListPatchRequestDataItemRelationshipsExecutedBy]):
    """

    defect: Union[
        Unset, "TestrecordsListPatchRequestDataItemRelationshipsDefect"
    ] = UNSET
    executed_by: Union[
        Unset, "TestrecordsListPatchRequestDataItemRelationshipsExecutedBy"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        defect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defect, Unset):
            defect = self.defect.to_dict()

        executed_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.executed_by, Unset):
            executed_by = self.executed_by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defect is not UNSET:
            field_dict["defect"] = defect
        if executed_by is not UNSET:
            field_dict["executedBy"] = executed_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrecords_list_patch_request_data_item_relationships_defect import (
            TestrecordsListPatchRequestDataItemRelationshipsDefect,
        )
        from ..models.testrecords_list_patch_request_data_item_relationships_executed_by import (
            TestrecordsListPatchRequestDataItemRelationshipsExecutedBy,
        )

        d = src_dict.copy()
        _defect = d.pop("defect", UNSET)
        defect: Union[
            Unset, TestrecordsListPatchRequestDataItemRelationshipsDefect
        ]
        if isinstance(_defect, Unset):
            defect = UNSET
        else:
            defect = TestrecordsListPatchRequestDataItemRelationshipsDefect.from_dict(
                _defect
            )

        _executed_by = d.pop("executedBy", UNSET)
        executed_by: Union[
            Unset, TestrecordsListPatchRequestDataItemRelationshipsExecutedBy
        ]
        if isinstance(_executed_by, Unset):
            executed_by = UNSET
        else:
            executed_by = TestrecordsListPatchRequestDataItemRelationshipsExecutedBy.from_dict(
                _executed_by
            )

        testrecords_list_patch_request_data_item_relationships_obj = cls(
            defect=defect,
            executed_by=executed_by,
        )

        testrecords_list_patch_request_data_item_relationships_obj.additional_properties = (
            d
        )
        return testrecords_list_patch_request_data_item_relationships_obj

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
