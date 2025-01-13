# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrecords_list_post_request_data_item_relationships_executed_by_data_type import (
    TestrecordsListPostRequestDataItemRelationshipsExecutedByDataType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="TestrecordsListPostRequestDataItemRelationshipsExecutedByData"
)


@_attrs_define
class TestrecordsListPostRequestDataItemRelationshipsExecutedByData:
    """
    Attributes:
        id (Union[Unset, str]):  Example: MyUserId.
        type (Union[Unset, TestrecordsListPostRequestDataItemRelationshipsExecutedByDataType]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[
        Unset,
        TestrecordsListPostRequestDataItemRelationshipsExecutedByDataType,
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            TestrecordsListPostRequestDataItemRelationshipsExecutedByDataType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrecordsListPostRequestDataItemRelationshipsExecutedByDataType(
                _type
            )

        testrecords_list_post_request_data_item_relationships_executed_by_data_obj = cls(
            id=id,
            type=type,
        )

        testrecords_list_post_request_data_item_relationships_executed_by_data_obj.additional_properties = (
            d
        )
        return testrecords_list_post_request_data_item_relationships_executed_by_data_obj

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
