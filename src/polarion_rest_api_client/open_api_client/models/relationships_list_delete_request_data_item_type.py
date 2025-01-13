# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class RelationshipsListDeleteRequestDataItemType(str, Enum):
    CATEGORIES = "categories"
    DOCUMENTS = "documents"
    DOCUMENT_ATTACHMENTS = "document_attachments"
    DOCUMENT_COMMENTS = "document_comments"
    DOCUMENT_PARTS = "document_parts"
    ENUMERATIONS = "enumerations"
    EXTERNALLYLINKEDWORKITEMS = "externallylinkedworkitems"
    FEATURESELECTIONS = "featureselections"
    GLOBALROLES = "globalroles"
    ICONS = "icons"
    JOBS = "jobs"
    LINKEDOSLCRESOURCES = "linkedoslcresources"
    LINKEDWORKITEMS = "linkedworkitems"
    PAGES = "pages"
    PAGE_ATTACHMENTS = "page_attachments"
    PLANS = "plans"
    PROJECTGROUPS = "projectgroups"
    PROJECTROLES = "projectroles"
    PROJECTS = "projects"
    PROJECTTEMPLATES = "projecttemplates"
    REVISIONS = "revisions"
    SPACES = "spaces"
    TESTPARAMETERS = "testparameters"
    TESTPARAMETER_DEFINITIONS = "testparameter_definitions"
    TESTRECORDS = "testrecords"
    TESTRECORD_ATTACHMENTS = "testrecord_attachments"
    TESTRUNS = "testruns"
    TESTRUN_ATTACHMENTS = "testrun_attachments"
    TESTRUN_COMMENTS = "testrun_comments"
    TESTSTEPRESULT_ATTACHMENTS = "teststepresult_attachments"
    TESTSTEPS = "teststeps"
    TESTSTEP_RESULTS = "teststep_results"
    USERGROUPS = "usergroups"
    USERS = "users"
    WORKITEMS = "workitems"
    WORKITEM_APPROVALS = "workitem_approvals"
    WORKITEM_ATTACHMENTS = "workitem_attachments"
    WORKITEM_COMMENTS = "workitem_comments"
    WORKRECORDS = "workrecords"

    def __str__(self) -> str:
        return str(self.value)
