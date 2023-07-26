# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyDocumentRequestBody")


@attr.s(auto_attribs=True)
class CopyDocumentRequestBody:
    """
    Attributes:
        target_project_id (Union[Unset, str]): Project where new document will be created. Example: MyProjectId.
        target_space_id (Union[Unset, str]): Space where new document will be created. Example: MySpaceId.
        target_document_name (Union[Unset, str]): Name for new document. Example: MyDocumentId.
        remove_outgoing_links (Union[Unset, bool]): Should outgoing links be removed? Example: True.
        link_original_items_with_role (Union[Unset, str]): Link a copy of the document to the original. Example:
            duplicates.
    """

    target_project_id: Union[Unset, str] = UNSET
    target_space_id: Union[Unset, str] = UNSET
    target_document_name: Union[Unset, str] = UNSET
    remove_outgoing_links: Union[Unset, bool] = UNSET
    link_original_items_with_role: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_project_id = self.target_project_id
        target_space_id = self.target_space_id
        target_document_name = self.target_document_name
        remove_outgoing_links = self.remove_outgoing_links
        link_original_items_with_role = self.link_original_items_with_role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_project_id is not UNSET:
            field_dict["targetProjectId"] = target_project_id
        if target_space_id is not UNSET:
            field_dict["targetSpaceId"] = target_space_id
        if target_document_name is not UNSET:
            field_dict["targetDocumentName"] = target_document_name
        if remove_outgoing_links is not UNSET:
            field_dict["removeOutgoingLinks"] = remove_outgoing_links
        if link_original_items_with_role is not UNSET:
            field_dict[
                "linkOriginalItemsWithRole"
            ] = link_original_items_with_role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_project_id = d.pop("targetProjectId", UNSET)

        target_space_id = d.pop("targetSpaceId", UNSET)

        target_document_name = d.pop("targetDocumentName", UNSET)

        remove_outgoing_links = d.pop("removeOutgoingLinks", UNSET)

        link_original_items_with_role = d.pop(
            "linkOriginalItemsWithRole", UNSET
        )

        copy_document_request_body_obj = cls(
            target_project_id=target_project_id,
            target_space_id=target_space_id,
            target_document_name=target_document_name,
            remove_outgoing_links=remove_outgoing_links,
            link_original_items_with_role=link_original_items_with_role,
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
