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

from ..models.teststeps_list_patch_request_data_item_type import (
    TeststepsListPatchRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststeps_list_patch_request_data_item_attributes import (
        TeststepsListPatchRequestDataItemAttributes,
    )


T = TypeVar("T", bound="TeststepsListPatchRequestDataItem")


@_attrs_define
class TeststepsListPatchRequestDataItem:
    """
    Attributes:
        type_ (Union[Unset, TeststepsListPatchRequestDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyWorkItemId/MyTestStepIndex.
        attributes (Union[Unset, TeststepsListPatchRequestDataItemAttributes]):
    """

    type_: Union[Unset, TeststepsListPatchRequestDataItemType] = UNSET
    id: Union[Unset, str] = UNSET
    attributes: Union[Unset, "TeststepsListPatchRequestDataItemAttributes"] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststeps_list_patch_request_data_item_attributes import (
            TeststepsListPatchRequestDataItemAttributes,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TeststepsListPatchRequestDataItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TeststepsListPatchRequestDataItemType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, TeststepsListPatchRequestDataItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TeststepsListPatchRequestDataItemAttributes.from_dict(
                _attributes
            )

        teststeps_list_patch_request_data_item_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
        )

        teststeps_list_patch_request_data_item_obj.additional_properties = d
        return teststeps_list_patch_request_data_item_obj

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
