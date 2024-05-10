# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchDocumentRequestBody")


@_attrs_define
class BranchDocumentRequestBody:
    """
    Attributes:
        target_project_id (Union[Unset, str]): Project where new document will be created. Example: MyProjectId.
        target_space_id (Union[Unset, str]): Space where new document will be created. Example: MySpaceId.
        target_document_name (Union[Unset, str]): Name for new Document. Example: MyDocumentId.
        copy_workflow_status_and_signatures (Union[Unset, bool]): Specifies that workflow status and signatures should
            be copied to the branched document.
        query (Union[Unset, str]): Specifies optional filtering query. Example: status:open.
    """

    target_project_id: Union[Unset, str] = UNSET
    target_space_id: Union[Unset, str] = UNSET
    target_document_name: Union[Unset, str] = UNSET
    copy_workflow_status_and_signatures: Union[Unset, bool] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        target_project_id = self.target_project_id

        target_space_id = self.target_space_id

        target_document_name = self.target_document_name

        copy_workflow_status_and_signatures = (
            self.copy_workflow_status_and_signatures
        )

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_project_id is not UNSET:
            field_dict["targetProjectId"] = target_project_id
        if target_space_id is not UNSET:
            field_dict["targetSpaceId"] = target_space_id
        if target_document_name is not UNSET:
            field_dict["targetDocumentName"] = target_document_name
        if copy_workflow_status_and_signatures is not UNSET:
            field_dict["copyWorkflowStatusAndSignatures"] = (
                copy_workflow_status_and_signatures
            )
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_project_id = d.pop("targetProjectId", UNSET)

        target_space_id = d.pop("targetSpaceId", UNSET)

        target_document_name = d.pop("targetDocumentName", UNSET)

        copy_workflow_status_and_signatures = d.pop(
            "copyWorkflowStatusAndSignatures", UNSET
        )

        query = d.pop("query", UNSET)

        branch_document_request_body_obj = cls(
            target_project_id=target_project_id,
            target_space_id=target_space_id,
            target_document_name=target_document_name,
            copy_workflow_status_and_signatures=copy_workflow_status_and_signatures,
            query=query,
        )

        branch_document_request_body_obj.additional_properties = d
        return branch_document_request_body_obj

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
