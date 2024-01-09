# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparseFields")


@_attrs_define
class SparseFields:
    """
    Attributes
    ----------
    categories : Union[Unset, str]
        Requested fields
    documents : Union[Unset, str]
        Requested fields
    document_attachments : Union[Unset, str]
        Requested fields
    document_comments : Union[Unset, str]
        Requested fields
    document_parts : Union[Unset, str]
        Requested fields
    enumerations : Union[Unset, str]
        Requested fields
    globalroles : Union[Unset, str]
        Requested fields
    icons : Union[Unset, str]
        Requested fields
    linkedworkitems : Union[Unset, str]
        Requested fields
    pages : Union[Unset, str]
        Requested fields
    page_attachments : Union[Unset, str]
        Requested fields
    plans : Union[Unset, str]
        Requested fields
    projectroles : Union[Unset, str]
        Requested fields
    projects : Union[Unset, str]
        Requested fields
    usergroups : Union[Unset, str]
        Requested fields
    users : Union[Unset, str]
        Requested fields
    workitems : Union[Unset, str]
        Requested fields
    workitem_attachments : Union[Unset, str]
        Requested fields
    workitem_comments : Union[Unset, str]
        Requested fields
    """

    categories: Union[Unset, str] = UNSET
    documents: Union[Unset, str] = UNSET
    document_attachments: Union[Unset, str] = UNSET
    document_comments: Union[Unset, str] = UNSET
    document_parts: Union[Unset, str] = UNSET
    enumerations: Union[Unset, str] = UNSET
    globalroles: Union[Unset, str] = UNSET
    icons: Union[Unset, str] = UNSET
    linkedworkitems: Union[Unset, str] = UNSET
    pages: Union[Unset, str] = UNSET
    page_attachments: Union[Unset, str] = UNSET
    plans: Union[Unset, str] = UNSET
    projectroles: Union[Unset, str] = UNSET
    projects: Union[Unset, str] = UNSET
    usergroups: Union[Unset, str] = UNSET
    users: Union[Unset, str] = UNSET
    workitems: Union[Unset, str] = UNSET
    workitem_attachments: Union[Unset, str] = UNSET
    workitem_comments: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        categories = self.categories
        documents = self.documents
        document_attachments = self.document_attachments
        document_comments = self.document_comments
        document_parts = self.document_parts
        enumerations = self.enumerations
        globalroles = self.globalroles
        icons = self.icons
        linkedworkitems = self.linkedworkitems
        pages = self.pages
        page_attachments = self.page_attachments
        plans = self.plans
        projectroles = self.projectroles
        projects = self.projects
        usergroups = self.usergroups
        users = self.users
        workitems = self.workitems
        workitem_attachments = self.workitem_attachments
        workitem_comments = self.workitem_comments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if documents is not UNSET:
            field_dict["documents"] = documents
        if document_attachments is not UNSET:
            field_dict["document_attachments"] = document_attachments
        if document_comments is not UNSET:
            field_dict["document_comments"] = document_comments
        if document_parts is not UNSET:
            field_dict["document_parts"] = document_parts
        if enumerations is not UNSET:
            field_dict["enumerations"] = enumerations
        if globalroles is not UNSET:
            field_dict["globalroles"] = globalroles
        if icons is not UNSET:
            field_dict["icons"] = icons
        if linkedworkitems is not UNSET:
            field_dict["linkedworkitems"] = linkedworkitems
        if pages is not UNSET:
            field_dict["pages"] = pages
        if page_attachments is not UNSET:
            field_dict["page_attachments"] = page_attachments
        if plans is not UNSET:
            field_dict["plans"] = plans
        if projectroles is not UNSET:
            field_dict["projectroles"] = projectroles
        if projects is not UNSET:
            field_dict["projects"] = projects
        if usergroups is not UNSET:
            field_dict["usergroups"] = usergroups
        if users is not UNSET:
            field_dict["users"] = users
        if workitems is not UNSET:
            field_dict["workitems"] = workitems
        if workitem_attachments is not UNSET:
            field_dict["workitem_attachments"] = workitem_attachments
        if workitem_comments is not UNSET:
            field_dict["workitem_comments"] = workitem_comments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        categories = d.pop("categories", UNSET)

        documents = d.pop("documents", UNSET)

        document_attachments = d.pop("document_attachments", UNSET)

        document_comments = d.pop("document_comments", UNSET)

        document_parts = d.pop("document_parts", UNSET)

        enumerations = d.pop("enumerations", UNSET)

        globalroles = d.pop("globalroles", UNSET)

        icons = d.pop("icons", UNSET)

        linkedworkitems = d.pop("linkedworkitems", UNSET)

        pages = d.pop("pages", UNSET)

        page_attachments = d.pop("page_attachments", UNSET)

        plans = d.pop("plans", UNSET)

        projectroles = d.pop("projectroles", UNSET)

        projects = d.pop("projects", UNSET)

        usergroups = d.pop("usergroups", UNSET)

        users = d.pop("users", UNSET)

        workitems = d.pop("workitems", UNSET)

        workitem_attachments = d.pop("workitem_attachments", UNSET)

        workitem_comments = d.pop("workitem_comments", UNSET)

        sparse_fields_obj = cls(
            categories=categories,
            documents=documents,
            document_attachments=document_attachments,
            document_comments=document_comments,
            document_parts=document_parts,
            enumerations=enumerations,
            globalroles=globalroles,
            icons=icons,
            linkedworkitems=linkedworkitems,
            pages=pages,
            page_attachments=page_attachments,
            plans=plans,
            projectroles=projectroles,
            projects=projects,
            usergroups=usergroups,
            users=users,
            workitems=workitems,
            workitem_attachments=workitem_attachments,
            workitem_comments=workitem_comments,
        )

        sparse_fields_obj.additional_properties = d
        return sparse_fields_obj

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
