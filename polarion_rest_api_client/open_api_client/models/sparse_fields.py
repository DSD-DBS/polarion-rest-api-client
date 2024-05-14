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
    Attributes:
        categories (Union[Unset, str]): Requested fields Example: @all.
        document_attachments (Union[Unset, str]): Requested fields Example: @all.
        document_comments (Union[Unset, str]): Requested fields Example: @all.
        document_parts (Union[Unset, str]): Requested fields Example: @all.
        documents (Union[Unset, str]): Requested fields Example: @all.
        enumerations (Union[Unset, str]): Requested fields Example: @all.
        externallylinkedworkitems (Union[Unset, str]): Requested fields Example: @all.
        featureselections (Union[Unset, str]): Requested fields Example: @all.
        globalroles (Union[Unset, str]): Requested fields Example: @all.
        icons (Union[Unset, str]): Requested fields Example: @all.
        jobs (Union[Unset, str]): Requested fields Example: @all.
        linkedoslcresources (Union[Unset, str]): Requested fields Example: @all.
        linkedworkitems (Union[Unset, str]): Requested fields Example: @all.
        page_attachments (Union[Unset, str]): Requested fields Example: @all.
        pages (Union[Unset, str]): Requested fields Example: @all.
        plans (Union[Unset, str]): Requested fields Example: @all.
        projectroles (Union[Unset, str]): Requested fields Example: @all.
        projects (Union[Unset, str]): Requested fields Example: @all.
        projecttemplates (Union[Unset, str]): Requested fields Example: @all.
        revisions (Union[Unset, str]): Requested fields Example: @all.
        testparameter_definitions (Union[Unset, str]): Requested fields Example: @all.
        testparameters (Union[Unset, str]): Requested fields Example: @all.
        testrecord_attachments (Union[Unset, str]): Requested fields Example: @all.
        testrecords (Union[Unset, str]): Requested fields Example: @all.
        testrun_attachments (Union[Unset, str]): Requested fields Example: @all.
        testrun_comments (Union[Unset, str]): Requested fields Example: @all.
        testruns (Union[Unset, str]): Requested fields Example: @all.
        teststep_results (Union[Unset, str]): Requested fields Example: @all.
        teststepresult_attachments (Union[Unset, str]): Requested fields Example: @all.
        teststeps (Union[Unset, str]): Requested fields Example: @all.
        usergroups (Union[Unset, str]): Requested fields Example: @all.
        users (Union[Unset, str]): Requested fields Example: @all.
        workitem_approvals (Union[Unset, str]): Requested fields Example: @all.
        workitem_attachments (Union[Unset, str]): Requested fields Example: @all.
        workitem_comments (Union[Unset, str]): Requested fields Example: @all.
        workitems (Union[Unset, str]): Requested fields Example: @all.
        workrecords (Union[Unset, str]): Requested fields Example: @all.
    """

    categories: Union[Unset, str] = UNSET
    document_attachments: Union[Unset, str] = UNSET
    document_comments: Union[Unset, str] = UNSET
    document_parts: Union[Unset, str] = UNSET
    documents: Union[Unset, str] = UNSET
    enumerations: Union[Unset, str] = UNSET
    externallylinkedworkitems: Union[Unset, str] = UNSET
    featureselections: Union[Unset, str] = UNSET
    globalroles: Union[Unset, str] = UNSET
    icons: Union[Unset, str] = UNSET
    jobs: Union[Unset, str] = UNSET
    linkedoslcresources: Union[Unset, str] = UNSET
    linkedworkitems: Union[Unset, str] = UNSET
    page_attachments: Union[Unset, str] = UNSET
    pages: Union[Unset, str] = UNSET
    plans: Union[Unset, str] = UNSET
    projectroles: Union[Unset, str] = UNSET
    projects: Union[Unset, str] = UNSET
    projecttemplates: Union[Unset, str] = UNSET
    revisions: Union[Unset, str] = UNSET
    testparameter_definitions: Union[Unset, str] = UNSET
    testparameters: Union[Unset, str] = UNSET
    testrecord_attachments: Union[Unset, str] = UNSET
    testrecords: Union[Unset, str] = UNSET
    testrun_attachments: Union[Unset, str] = UNSET
    testrun_comments: Union[Unset, str] = UNSET
    testruns: Union[Unset, str] = UNSET
    teststep_results: Union[Unset, str] = UNSET
    teststepresult_attachments: Union[Unset, str] = UNSET
    teststeps: Union[Unset, str] = UNSET
    usergroups: Union[Unset, str] = UNSET
    users: Union[Unset, str] = UNSET
    workitem_approvals: Union[Unset, str] = UNSET
    workitem_attachments: Union[Unset, str] = UNSET
    workitem_comments: Union[Unset, str] = UNSET
    workitems: Union[Unset, str] = UNSET
    workrecords: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        categories = self.categories

        document_attachments = self.document_attachments

        document_comments = self.document_comments

        document_parts = self.document_parts

        documents = self.documents

        enumerations = self.enumerations

        externallylinkedworkitems = self.externallylinkedworkitems

        featureselections = self.featureselections

        globalroles = self.globalroles

        icons = self.icons

        jobs = self.jobs

        linkedoslcresources = self.linkedoslcresources

        linkedworkitems = self.linkedworkitems

        page_attachments = self.page_attachments

        pages = self.pages

        plans = self.plans

        projectroles = self.projectroles

        projects = self.projects

        projecttemplates = self.projecttemplates

        revisions = self.revisions

        testparameter_definitions = self.testparameter_definitions

        testparameters = self.testparameters

        testrecord_attachments = self.testrecord_attachments

        testrecords = self.testrecords

        testrun_attachments = self.testrun_attachments

        testrun_comments = self.testrun_comments

        testruns = self.testruns

        teststep_results = self.teststep_results

        teststepresult_attachments = self.teststepresult_attachments

        teststeps = self.teststeps

        usergroups = self.usergroups

        users = self.users

        workitem_approvals = self.workitem_approvals

        workitem_attachments = self.workitem_attachments

        workitem_comments = self.workitem_comments

        workitems = self.workitems

        workrecords = self.workrecords

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if document_attachments is not UNSET:
            field_dict["document_attachments"] = document_attachments
        if document_comments is not UNSET:
            field_dict["document_comments"] = document_comments
        if document_parts is not UNSET:
            field_dict["document_parts"] = document_parts
        if documents is not UNSET:
            field_dict["documents"] = documents
        if enumerations is not UNSET:
            field_dict["enumerations"] = enumerations
        if externallylinkedworkitems is not UNSET:
            field_dict["externallylinkedworkitems"] = externallylinkedworkitems
        if featureselections is not UNSET:
            field_dict["featureselections"] = featureselections
        if globalroles is not UNSET:
            field_dict["globalroles"] = globalroles
        if icons is not UNSET:
            field_dict["icons"] = icons
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if linkedoslcresources is not UNSET:
            field_dict["linkedoslcresources"] = linkedoslcresources
        if linkedworkitems is not UNSET:
            field_dict["linkedworkitems"] = linkedworkitems
        if page_attachments is not UNSET:
            field_dict["page_attachments"] = page_attachments
        if pages is not UNSET:
            field_dict["pages"] = pages
        if plans is not UNSET:
            field_dict["plans"] = plans
        if projectroles is not UNSET:
            field_dict["projectroles"] = projectroles
        if projects is not UNSET:
            field_dict["projects"] = projects
        if projecttemplates is not UNSET:
            field_dict["projecttemplates"] = projecttemplates
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if testparameter_definitions is not UNSET:
            field_dict["testparameter_definitions"] = testparameter_definitions
        if testparameters is not UNSET:
            field_dict["testparameters"] = testparameters
        if testrecord_attachments is not UNSET:
            field_dict["testrecord_attachments"] = testrecord_attachments
        if testrecords is not UNSET:
            field_dict["testrecords"] = testrecords
        if testrun_attachments is not UNSET:
            field_dict["testrun_attachments"] = testrun_attachments
        if testrun_comments is not UNSET:
            field_dict["testrun_comments"] = testrun_comments
        if testruns is not UNSET:
            field_dict["testruns"] = testruns
        if teststep_results is not UNSET:
            field_dict["teststep_results"] = teststep_results
        if teststepresult_attachments is not UNSET:
            field_dict["teststepresult_attachments"] = (
                teststepresult_attachments
            )
        if teststeps is not UNSET:
            field_dict["teststeps"] = teststeps
        if usergroups is not UNSET:
            field_dict["usergroups"] = usergroups
        if users is not UNSET:
            field_dict["users"] = users
        if workitem_approvals is not UNSET:
            field_dict["workitem_approvals"] = workitem_approvals
        if workitem_attachments is not UNSET:
            field_dict["workitem_attachments"] = workitem_attachments
        if workitem_comments is not UNSET:
            field_dict["workitem_comments"] = workitem_comments
        if workitems is not UNSET:
            field_dict["workitems"] = workitems
        if workrecords is not UNSET:
            field_dict["workrecords"] = workrecords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        categories = d.pop("categories", UNSET)

        document_attachments = d.pop("document_attachments", UNSET)

        document_comments = d.pop("document_comments", UNSET)

        document_parts = d.pop("document_parts", UNSET)

        documents = d.pop("documents", UNSET)

        enumerations = d.pop("enumerations", UNSET)

        externallylinkedworkitems = d.pop("externallylinkedworkitems", UNSET)

        featureselections = d.pop("featureselections", UNSET)

        globalroles = d.pop("globalroles", UNSET)

        icons = d.pop("icons", UNSET)

        jobs = d.pop("jobs", UNSET)

        linkedoslcresources = d.pop("linkedoslcresources", UNSET)

        linkedworkitems = d.pop("linkedworkitems", UNSET)

        page_attachments = d.pop("page_attachments", UNSET)

        pages = d.pop("pages", UNSET)

        plans = d.pop("plans", UNSET)

        projectroles = d.pop("projectroles", UNSET)

        projects = d.pop("projects", UNSET)

        projecttemplates = d.pop("projecttemplates", UNSET)

        revisions = d.pop("revisions", UNSET)

        testparameter_definitions = d.pop("testparameter_definitions", UNSET)

        testparameters = d.pop("testparameters", UNSET)

        testrecord_attachments = d.pop("testrecord_attachments", UNSET)

        testrecords = d.pop("testrecords", UNSET)

        testrun_attachments = d.pop("testrun_attachments", UNSET)

        testrun_comments = d.pop("testrun_comments", UNSET)

        testruns = d.pop("testruns", UNSET)

        teststep_results = d.pop("teststep_results", UNSET)

        teststepresult_attachments = d.pop("teststepresult_attachments", UNSET)

        teststeps = d.pop("teststeps", UNSET)

        usergroups = d.pop("usergroups", UNSET)

        users = d.pop("users", UNSET)

        workitem_approvals = d.pop("workitem_approvals", UNSET)

        workitem_attachments = d.pop("workitem_attachments", UNSET)

        workitem_comments = d.pop("workitem_comments", UNSET)

        workitems = d.pop("workitems", UNSET)

        workrecords = d.pop("workrecords", UNSET)

        sparse_fields_obj = cls(
            categories=categories,
            document_attachments=document_attachments,
            document_comments=document_comments,
            document_parts=document_parts,
            documents=documents,
            enumerations=enumerations,
            externallylinkedworkitems=externallylinkedworkitems,
            featureselections=featureselections,
            globalroles=globalroles,
            icons=icons,
            jobs=jobs,
            linkedoslcresources=linkedoslcresources,
            linkedworkitems=linkedworkitems,
            page_attachments=page_attachments,
            pages=pages,
            plans=plans,
            projectroles=projectroles,
            projects=projects,
            projecttemplates=projecttemplates,
            revisions=revisions,
            testparameter_definitions=testparameter_definitions,
            testparameters=testparameters,
            testrecord_attachments=testrecord_attachments,
            testrecords=testrecords,
            testrun_attachments=testrun_attachments,
            testrun_comments=testrun_comments,
            testruns=testruns,
            teststep_results=teststep_results,
            teststepresult_attachments=teststepresult_attachments,
            teststeps=teststeps,
            usergroups=usergroups,
            users=users,
            workitem_approvals=workitem_approvals,
            workitem_attachments=workitem_attachments,
            workitem_comments=workitem_comments,
            workitems=workitems,
            workrecords=workrecords,
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
