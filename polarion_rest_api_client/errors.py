# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Polarion API related errors."""
from __future__ import annotations


class PolarionApiBaseException(Exception):
    """Base exception, which is raised, if an API error occurs."""


class PolarionApiException(PolarionApiBaseException):
    """Exception, which is raised, if an error is raised by the API."""


class PolarionApiUnexpectedException(PolarionApiBaseException):
    """Exception, which is raised, if an unexpected error is raised."""
