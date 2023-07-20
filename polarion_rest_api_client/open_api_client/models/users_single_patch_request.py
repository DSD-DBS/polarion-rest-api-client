# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.users_single_patch_request_data import (
        UsersSinglePatchRequestData,
    )


T = TypeVar("T", bound="UsersSinglePatchRequest")


@attr.s(auto_attribs=True)
class UsersSinglePatchRequest:
    """
    Attributes:
        data (Union[Unset, UsersSinglePatchRequestData]):
    """

    data: Union[Unset, "UsersSinglePatchRequestData"] = UNSET
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
        from ..models.users_single_patch_request_data import (
            UsersSinglePatchRequestData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, UsersSinglePatchRequestData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UsersSinglePatchRequestData.from_dict(_data)

        users_single_patch_request = cls(
            data=data,
        )

        users_single_patch_request.additional_properties = d
        return users_single_patch_request

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
