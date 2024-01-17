# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrecords_list_post_request_data_item_relationships_defect import (
        TestrecordsListPostRequestDataItemRelationshipsDefect,
    )
    from ..models.testrecords_list_post_request_data_item_relationships_executed_by import (
        TestrecordsListPostRequestDataItemRelationshipsExecutedBy,
    )
    from ..models.testrecords_list_post_request_data_item_relationships_test_case import (
        TestrecordsListPostRequestDataItemRelationshipsTestCase,
    )


T = TypeVar("T", bound="TestrecordsListPostRequestDataItemRelationships")


@_attrs_define
class TestrecordsListPostRequestDataItemRelationships:
    """
    Attributes:
        defect (Union[Unset, TestrecordsListPostRequestDataItemRelationshipsDefect]):
        executed_by (Union[Unset, TestrecordsListPostRequestDataItemRelationshipsExecutedBy]):
        test_case (Union[Unset, TestrecordsListPostRequestDataItemRelationshipsTestCase]):
    """

    defect: Union[
        Unset, "TestrecordsListPostRequestDataItemRelationshipsDefect"
    ] = UNSET
    executed_by: Union[
        Unset, "TestrecordsListPostRequestDataItemRelationshipsExecutedBy"
    ] = UNSET
    test_case: Union[
        Unset, "TestrecordsListPostRequestDataItemRelationshipsTestCase"
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

        test_case: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.test_case, Unset):
            test_case = self.test_case.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defect is not UNSET:
            field_dict["defect"] = defect
        if executed_by is not UNSET:
            field_dict["executedBy"] = executed_by
        if test_case is not UNSET:
            field_dict["testCase"] = test_case

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrecords_list_post_request_data_item_relationships_defect import (
            TestrecordsListPostRequestDataItemRelationshipsDefect,
        )
        from ..models.testrecords_list_post_request_data_item_relationships_executed_by import (
            TestrecordsListPostRequestDataItemRelationshipsExecutedBy,
        )
        from ..models.testrecords_list_post_request_data_item_relationships_test_case import (
            TestrecordsListPostRequestDataItemRelationshipsTestCase,
        )

        d = src_dict.copy()
        _defect = d.pop("defect", UNSET)
        defect: Union[
            Unset, TestrecordsListPostRequestDataItemRelationshipsDefect
        ]
        if isinstance(_defect, Unset):
            defect = UNSET
        else:
            defect = TestrecordsListPostRequestDataItemRelationshipsDefect.from_dict(
                _defect
            )

        _executed_by = d.pop("executedBy", UNSET)
        executed_by: Union[
            Unset, TestrecordsListPostRequestDataItemRelationshipsExecutedBy
        ]
        if isinstance(_executed_by, Unset):
            executed_by = UNSET
        else:
            executed_by = TestrecordsListPostRequestDataItemRelationshipsExecutedBy.from_dict(
                _executed_by
            )

        _test_case = d.pop("testCase", UNSET)
        test_case: Union[
            Unset, TestrecordsListPostRequestDataItemRelationshipsTestCase
        ]
        if isinstance(_test_case, Unset):
            test_case = UNSET
        else:
            test_case = TestrecordsListPostRequestDataItemRelationshipsTestCase.from_dict(
                _test_case
            )

        testrecords_list_post_request_data_item_relationships_obj = cls(
            defect=defect,
            executed_by=executed_by,
            test_case=test_case,
        )

        testrecords_list_post_request_data_item_relationships_obj.additional_properties = (
            d
        )
        return testrecords_list_post_request_data_item_relationships_obj

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
