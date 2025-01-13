# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pages_single_get_response_data_relationships_updated_by_data import (
        PagesSingleGetResponseDataRelationshipsUpdatedByData,
    )


T = TypeVar("T", bound="PagesSingleGetResponseDataRelationshipsUpdatedBy")


@_attrs_define
class PagesSingleGetResponseDataRelationshipsUpdatedBy:
    """
    Attributes:
        data (Union[Unset, PagesSingleGetResponseDataRelationshipsUpdatedByData]):
    """

    data: Union[
        Unset, "PagesSingleGetResponseDataRelationshipsUpdatedByData"
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
        from ..models.pages_single_get_response_data_relationships_updated_by_data import (
            PagesSingleGetResponseDataRelationshipsUpdatedByData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[
            Unset, PagesSingleGetResponseDataRelationshipsUpdatedByData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = (
                PagesSingleGetResponseDataRelationshipsUpdatedByData.from_dict(
                    _data
                )
            )

        pages_single_get_response_data_relationships_updated_by_obj = cls(
            data=data,
        )

        pages_single_get_response_data_relationships_updated_by_obj.additional_properties = (
            d
        )
        return pages_single_get_response_data_relationships_updated_by_obj

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
