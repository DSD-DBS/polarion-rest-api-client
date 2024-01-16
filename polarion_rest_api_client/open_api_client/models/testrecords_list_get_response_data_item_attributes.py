# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrecords_list_get_response_data_item_attributes_comment import (
        TestrecordsListGetResponseDataItemAttributesComment,
    )


T = TypeVar("T", bound="TestrecordsListGetResponseDataItemAttributes")


@_attrs_define
class TestrecordsListGetResponseDataItemAttributes:
    """
    Attributes:
        comment (Union[Unset, TestrecordsListGetResponseDataItemAttributesComment]):
        duration (Union[Unset, float]):
        executed (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        iteration (Union[Unset, int]):
        result (Union[Unset, str]):  Example: passed.
        test_case_revision (Union[Unset, str]):  Example: Test Case Revision.
    """

    comment: Union[
        Unset, "TestrecordsListGetResponseDataItemAttributesComment"
    ] = UNSET
    duration: Union[Unset, float] = UNSET
    executed: Union[Unset, datetime.datetime] = UNSET
    iteration: Union[Unset, int] = UNSET
    result: Union[Unset, str] = UNSET
    test_case_revision: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        duration = self.duration

        executed: Union[Unset, str] = UNSET
        if not isinstance(self.executed, Unset):
            executed = self.executed.isoformat()

        iteration = self.iteration

        result = self.result

        test_case_revision = self.test_case_revision

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if duration is not UNSET:
            field_dict["duration"] = duration
        if executed is not UNSET:
            field_dict["executed"] = executed
        if iteration is not UNSET:
            field_dict["iteration"] = iteration
        if result is not UNSET:
            field_dict["result"] = result
        if test_case_revision is not UNSET:
            field_dict["testCaseRevision"] = test_case_revision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrecords_list_get_response_data_item_attributes_comment import (
            TestrecordsListGetResponseDataItemAttributesComment,
        )

        d = src_dict.copy()
        _comment = d.pop("comment", UNSET)
        comment: Union[
            Unset, TestrecordsListGetResponseDataItemAttributesComment
        ]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = (
                TestrecordsListGetResponseDataItemAttributesComment.from_dict(
                    _comment
                )
            )

        duration = d.pop("duration", UNSET)

        _executed = d.pop("executed", UNSET)
        executed: Union[Unset, datetime.datetime]
        if isinstance(_executed, Unset):
            executed = UNSET
        else:
            executed = isoparse(_executed)

        iteration = d.pop("iteration", UNSET)

        result = d.pop("result", UNSET)

        test_case_revision = d.pop("testCaseRevision", UNSET)

        testrecords_list_get_response_data_item_attributes_obj = cls(
            comment=comment,
            duration=duration,
            executed=executed,
            iteration=iteration,
            result=result,
            test_case_revision=test_case_revision,
        )

        testrecords_list_get_response_data_item_attributes_obj.additional_properties = (
            d
        )
        return testrecords_list_get_response_data_item_attributes_obj

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
