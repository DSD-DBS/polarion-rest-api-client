# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Polarion API module serving all data classes, clients and errors."""

from importlib import metadata

import polarion_rest_api_client.data_models
import polarion_rest_api_client.errors
from polarion_rest_api_client.client import PolarionClient
from polarion_rest_api_client.clients.projects import ProjectClient
from polarion_rest_api_client.data_models import *
from polarion_rest_api_client.errors import *

__all__ = [
    "PolarionClient",
    "ProjectClient",
    *polarion_rest_api_client.data_models.__all__,
    *polarion_rest_api_client.errors.__all__,
]


try:
    __version__ = metadata.version("polarion_rest_api_client")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
del metadata
