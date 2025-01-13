# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationship_data_body import RelationshipDataBody


T = TypeVar("T", bound="RelationshipDataSingleResponse")


@_attrs_define
class RelationshipDataSingleResponse:
    """
    Attributes:
        data (Union[Unset, RelationshipDataBody]):
    """

    data: Union[Unset, "RelationshipDataBody"] = UNSET
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
        from ..models.relationship_data_body import RelationshipDataBody

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, RelationshipDataBody]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RelationshipDataBody.from_dict(_data)

        relationship_data_single_response_obj = cls(
            data=data,
        )

        relationship_data_single_response_obj.additional_properties = d
        return relationship_data_single_response_obj

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
