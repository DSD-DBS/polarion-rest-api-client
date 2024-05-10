# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionsActionResponseBodyDataItem")


@_attrs_define
class WorkflowActionsActionResponseBodyDataItem:
    """
    Attributes:
        id (Union[Unset, str]):
        available (Union[Unset, bool]):
        cleared_fields (Union[Unset, List[str]]):
        is_adding_signature (Union[Unset, bool]):
        is_signature_required (Union[Unset, bool]):
        name (Union[Unset, str]):
        native_action_id (Union[Unset, str]):
        required_fields (Union[Unset, List[str]]):
        required_roles (Union[Unset, List[str]]):
        target_status (Union[Unset, str]):
        unavailable_reason (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    available: Union[Unset, bool] = UNSET
    cleared_fields: Union[Unset, List[str]] = UNSET
    is_adding_signature: Union[Unset, bool] = UNSET
    is_signature_required: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    native_action_id: Union[Unset, str] = UNSET
    required_fields: Union[Unset, List[str]] = UNSET
    required_roles: Union[Unset, List[str]] = UNSET
    target_status: Union[Unset, str] = UNSET
    unavailable_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        available = self.available

        cleared_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cleared_fields, Unset):
            cleared_fields = self.cleared_fields

        is_adding_signature = self.is_adding_signature

        is_signature_required = self.is_signature_required

        name = self.name

        native_action_id = self.native_action_id

        required_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_fields, Unset):
            required_fields = self.required_fields

        required_roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_roles, Unset):
            required_roles = self.required_roles

        target_status = self.target_status

        unavailable_reason = self.unavailable_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if available is not UNSET:
            field_dict["available"] = available
        if cleared_fields is not UNSET:
            field_dict["clearedFields"] = cleared_fields
        if is_adding_signature is not UNSET:
            field_dict["isAddingSignature"] = is_adding_signature
        if is_signature_required is not UNSET:
            field_dict["isSignatureRequired"] = is_signature_required
        if name is not UNSET:
            field_dict["name"] = name
        if native_action_id is not UNSET:
            field_dict["nativeActionId"] = native_action_id
        if required_fields is not UNSET:
            field_dict["requiredFields"] = required_fields
        if required_roles is not UNSET:
            field_dict["requiredRoles"] = required_roles
        if target_status is not UNSET:
            field_dict["targetStatus"] = target_status
        if unavailable_reason is not UNSET:
            field_dict["unavailableReason"] = unavailable_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        available = d.pop("available", UNSET)

        cleared_fields = cast(List[str], d.pop("clearedFields", UNSET))

        is_adding_signature = d.pop("isAddingSignature", UNSET)

        is_signature_required = d.pop("isSignatureRequired", UNSET)

        name = d.pop("name", UNSET)

        native_action_id = d.pop("nativeActionId", UNSET)

        required_fields = cast(List[str], d.pop("requiredFields", UNSET))

        required_roles = cast(List[str], d.pop("requiredRoles", UNSET))

        target_status = d.pop("targetStatus", UNSET)

        unavailable_reason = d.pop("unavailableReason", UNSET)

        workflow_actions_action_response_body_data_item_obj = cls(
            id=id,
            available=available,
            cleared_fields=cleared_fields,
            is_adding_signature=is_adding_signature,
            is_signature_required=is_signature_required,
            name=name,
            native_action_id=native_action_id,
            required_fields=required_fields,
            required_roles=required_roles,
            target_status=target_status,
            unavailable_reason=unavailable_reason,
        )

        workflow_actions_action_response_body_data_item_obj.additional_properties = (
            d
        )
        return workflow_actions_action_response_body_data_item_obj

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
