# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""The overall Polarion Client which handles the HTTP session, auth etc."""
from __future__ import annotations

import typing as t

import polarion_rest_api_client.open_api_client as oa_client
from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.clients import projects

WorkItemType = t.TypeVar("WorkItemType", bound=dm.WorkItem)


class DefaultFields:
    """A class to define default values for the fields parameter."""

    _workitems: str = "@basic"
    _linkedworkitems: str = "id,role,suspect"
    _workitem_attachments: str = "@basic"
    _documents: str = "@basic"
    _testrecords: str = "@basic"
    _testruns: str = "@basic"

    @property
    def workitems(self):
        """Return the fields dict for workitems."""
        return {"workitems": self._workitems}

    @workitems.setter
    def workitems(self, value):
        self._workitems = value

    @property
    def linkedworkitems(self):
        """Return the fields dict for linkedworkitems."""
        return {"linkedworkitems": self._linkedworkitems}

    @linkedworkitems.setter
    def linkedworkitems(self, value):
        self._linkedworkitems = value

    @property
    def workitem_attachments(self):
        """Return the fields dict for workitem_attachments."""
        return {"workitem_attachments": self._workitem_attachments}

    @workitem_attachments.setter
    def workitem_attachments(self, value):
        self._workitem_attachments = value

    @property
    def documents(self):
        """Return the fields dict for document."""
        return {"documents": self._documents}

    @documents.setter
    def documents(self, value):
        self._documents = value

    @property
    def testruns(self):
        """Return the fields dict for document."""
        return {"testruns": self._testruns}

    @testruns.setter
    def testruns(self, value):
        self._testruns = value

    @property
    def testrecords(self):
        """Return the fields dict for document."""
        return {"testrecords": self._testrecords}

    @testrecords.setter
    def testrecords(self, value):
        self._testrecords = value

    @property
    def all_types(self):
        """Return all fields dicts merged together."""
        return (
            self.workitem_attachments
            | self.workitems
            | self.linkedworkitems
            | self.documents
            | self.testruns
            | self.testrecords
        )


class PolarionClient:
    """The overall, project independent Polarion client."""

    def __init__(
        self,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        httpx_args: t.Optional[dict[str, t.Any]] = None,
        batch_size: int = 100,
        page_size: int = 100,
        max_content_size: int = 2 * 1024**2,
    ):
        self.client = oa_client.AuthenticatedClient(
            polarion_api_endpoint,
            polarion_access_token,
            httpx_args=httpx_args or {},
        )
        self.batch_size = batch_size
        self.page_size = page_size
        self.max_content_size = max_content_size
        self.default_fields = DefaultFields()

    def generate_project_client(
        self,
        project_id: str,
        delete_status: str | None = None,
        add_work_item_checksum: bool = False,
    ):
        """Return a client for a specific project."""
        return projects.ProjectClient(
            project_id, self, delete_status, add_work_item_checksum
        )
