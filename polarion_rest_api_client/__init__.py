# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Polarion API module serving all data classes, clients and errors."""
from importlib import metadata

try:
    __version__ = metadata.version("polarion_rest_api_client")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
del metadata

from polarion_rest_api_client.client import PolarionClient
from polarion_rest_api_client.clients.projects import ProjectClient
from polarion_rest_api_client.data_models import *
from polarion_rest_api_client.errors import *
from polarion_rest_api_client.old_client import OpenAPIPolarionProjectClient
