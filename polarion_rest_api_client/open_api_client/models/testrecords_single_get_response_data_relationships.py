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
    from ..models.testrecords_single_get_response_data_relationships_defect import (
        TestrecordsSingleGetResponseDataRelationshipsDefect,
    )
    from ..models.testrecords_single_get_response_data_relationships_executed_by import (
        TestrecordsSingleGetResponseDataRelationshipsExecutedBy,
    )
    from ..models.testrecords_single_get_response_data_relationships_test_case import (
        TestrecordsSingleGetResponseDataRelationshipsTestCase,
    )


T = TypeVar("T", bound="TestrecordsSingleGetResponseDataRelationships")


@_attrs_define
class TestrecordsSingleGetResponseDataRelationships:
    """
    Attributes:
        defect (Union[Unset, TestrecordsSingleGetResponseDataRelationshipsDefect]):
        executed_by (Union[Unset, TestrecordsSingleGetResponseDataRelationshipsExecutedBy]):
        test_case (Union[Unset, TestrecordsSingleGetResponseDataRelationshipsTestCase]):
    """

    defect: Union[
        Unset, "TestrecordsSingleGetResponseDataRelationshipsDefect"
    ] = UNSET
    executed_by: Union[
        Unset, "TestrecordsSingleGetResponseDataRelationshipsExecutedBy"
    ] = UNSET
    test_case: Union[
        Unset, "TestrecordsSingleGetResponseDataRelationshipsTestCase"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        defect: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defect, Unset):
            defect = self.defect.to_dict()

        executed_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.executed_by, Unset):
            executed_by = self.executed_by.to_dict()

        test_case: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.test_case, Unset):
            test_case = self.test_case.to_dict()

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testrecords_single_get_response_data_relationships_defect import (
            TestrecordsSingleGetResponseDataRelationshipsDefect,
        )
        from ..models.testrecords_single_get_response_data_relationships_executed_by import (
            TestrecordsSingleGetResponseDataRelationshipsExecutedBy,
        )
        from ..models.testrecords_single_get_response_data_relationships_test_case import (
            TestrecordsSingleGetResponseDataRelationshipsTestCase,
        )

        d = dict(src_dict)
        _defect = d.pop("defect", UNSET)
        defect: Union[
            Unset, TestrecordsSingleGetResponseDataRelationshipsDefect
        ]
        if isinstance(_defect, Unset):
            defect = UNSET
        else:
            defect = (
                TestrecordsSingleGetResponseDataRelationshipsDefect.from_dict(
                    _defect
                )
            )

        _executed_by = d.pop("executedBy", UNSET)
        executed_by: Union[
            Unset, TestrecordsSingleGetResponseDataRelationshipsExecutedBy
        ]
        if isinstance(_executed_by, Unset):
            executed_by = UNSET
        else:
            executed_by = TestrecordsSingleGetResponseDataRelationshipsExecutedBy.from_dict(
                _executed_by
            )

        _test_case = d.pop("testCase", UNSET)
        test_case: Union[
            Unset, TestrecordsSingleGetResponseDataRelationshipsTestCase
        ]
        if isinstance(_test_case, Unset):
            test_case = UNSET
        else:
            test_case = TestrecordsSingleGetResponseDataRelationshipsTestCase.from_dict(
                _test_case
            )

        testrecords_single_get_response_data_relationships_obj = cls(
            defect=defect,
            executed_by=executed_by,
            test_case=test_case,
        )

        testrecords_single_get_response_data_relationships_obj.additional_properties = d
        return testrecords_single_get_response_data_relationships_obj

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
