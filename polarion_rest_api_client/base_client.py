# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Base class for a polarion project client to easily rewrite the client."""
from __future__ import annotations

import abc
import typing as t

from polarion_rest_api_client import data_models as dm

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
