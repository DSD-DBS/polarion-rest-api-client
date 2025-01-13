# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Polarion API related errors."""
from __future__ import annotations

from . import data_models as dm

__all__ = [
    "PolarionApiBaseException",
    "PolarionApiException",
    "PolarionApiInternalException",
    "PolarionApiUnexpectedException",
    "PolarionWorkItemException",
]


class PolarionApiBaseException(Exception):
    """Base exception, which is raised, if an API error occurs."""


class PolarionApiInternalException(Exception):
    """Exception being raised, if an error occurs in the client itself."""


class PolarionWorkItemException(PolarionApiInternalException):
    """Exception being raised, if a WorkItem related error occurs."""

    def __init__(self, message: str, work_item: dm.WorkItem):
        self.work_item = work_item
        message = f"{message} (WorkItem Title: {work_item.title})"
        super().__init__(message)


class PolarionApiException(PolarionApiBaseException):
    """Exception, which is raised, if an error is raised by the API."""


class PolarionApiUnexpectedException(PolarionApiBaseException):
    """Exception, which is raised, if an unexpected error is raised."""
