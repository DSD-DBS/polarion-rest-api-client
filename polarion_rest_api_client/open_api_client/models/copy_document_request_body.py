# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyDocumentRequestBody")


@_attrs_define
class CopyDocumentRequestBody:
    """
    Attributes:
        link_original_items_with_role (Union[Unset, str]): Link a copy of the document to the original. Example:
            duplicates.
        remove_outgoing_links (Union[Unset, bool]): Should outgoing links be removed? Example: True.
        target_document_name (Union[Unset, str]): Name for new Document. Example: MyDocumentId.
        target_project_id (Union[Unset, str]): Project where new document will be created. Example: MyProjectId.
        target_space_id (Union[Unset, str]): Space where new document will be created. Example: MySpaceId.
    """

    link_original_items_with_role: Union[Unset, str] = UNSET
    remove_outgoing_links: Union[Unset, bool] = UNSET
    target_document_name: Union[Unset, str] = UNSET
    target_project_id: Union[Unset, str] = UNSET
    target_space_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        link_original_items_with_role = self.link_original_items_with_role

        remove_outgoing_links = self.remove_outgoing_links

        target_document_name = self.target_document_name

        target_project_id = self.target_project_id

        target_space_id = self.target_space_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_original_items_with_role is not UNSET:
            field_dict["linkOriginalItemsWithRole"] = (
                link_original_items_with_role
            )
        if remove_outgoing_links is not UNSET:
            field_dict["removeOutgoingLinks"] = remove_outgoing_links
        if target_document_name is not UNSET:
            field_dict["targetDocumentName"] = target_document_name
        if target_project_id is not UNSET:
            field_dict["targetProjectId"] = target_project_id
        if target_space_id is not UNSET:
            field_dict["targetSpaceId"] = target_space_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        link_original_items_with_role = d.pop(
            "linkOriginalItemsWithRole", UNSET
        )

        remove_outgoing_links = d.pop("removeOutgoingLinks", UNSET)

        target_document_name = d.pop("targetDocumentName", UNSET)

        target_project_id = d.pop("targetProjectId", UNSET)

        target_space_id = d.pop("targetSpaceId", UNSET)

        copy_document_request_body_obj = cls(
            link_original_items_with_role=link_original_items_with_role,
            remove_outgoing_links=remove_outgoing_links,
            target_document_name=target_document_name,
            target_project_id=target_project_id,
            target_space_id=target_space_id,
        )

        copy_document_request_body_obj.additional_properties = d
        return copy_document_request_body_obj

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
