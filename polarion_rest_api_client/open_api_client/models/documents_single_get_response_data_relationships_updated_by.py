# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_single_get_response_data_relationships_updated_by_data import (
        DocumentsSingleGetResponseDataRelationshipsUpdatedByData,
    )


T = TypeVar("T", bound="DocumentsSingleGetResponseDataRelationshipsUpdatedBy")


@attr.s(auto_attribs=True)
class DocumentsSingleGetResponseDataRelationshipsUpdatedBy:
    """
    Attributes:
        data (Union[Unset, DocumentsSingleGetResponseDataRelationshipsUpdatedByData]):
    """

    data: Union[
        Unset, "DocumentsSingleGetResponseDataRelationshipsUpdatedByData"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.documents_single_get_response_data_relationships_updated_by_data import (
            DocumentsSingleGetResponseDataRelationshipsUpdatedByData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[
            Unset, DocumentsSingleGetResponseDataRelationshipsUpdatedByData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DocumentsSingleGetResponseDataRelationshipsUpdatedByData.from_dict(
                _data
            )

        documents_single_get_response_data_relationships_updated_by = cls(
            data=data,
        )

        documents_single_get_response_data_relationships_updated_by.additional_properties = (
            d
        )
        return documents_single_get_response_data_relationships_updated_by

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
