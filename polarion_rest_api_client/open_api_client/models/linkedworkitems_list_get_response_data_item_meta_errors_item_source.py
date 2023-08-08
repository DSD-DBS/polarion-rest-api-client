# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="LinkedworkitemsListGetResponseDataItemMetaErrorsItemSource"
)


@define
class LinkedworkitemsListGetResponseDataItemMetaErrorsItemSource:
    """
    Attributes
    ----------
    pointer : Union[Unset, str]
        JSON Pointer to the associated entity in the request document.
    parameter : Union[Unset, str]
        String indicating which URI query parameter caused the error.
    """

    pointer: Union[Unset, str] = UNSET
    parameter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pointer = self.pointer
        parameter = self.parameter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pointer = d.pop("pointer", UNSET)

        parameter = d.pop("parameter", UNSET)

        linkedworkitems_list_get_response_data_item_meta_errors_item_source_obj = cls(
            pointer=pointer,
            parameter=parameter,
        )

        linkedworkitems_list_get_response_data_item_meta_errors_item_source_obj.additional_properties = (
            d
        )
        return linkedworkitems_list_get_response_data_item_meta_errors_item_source_obj

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
