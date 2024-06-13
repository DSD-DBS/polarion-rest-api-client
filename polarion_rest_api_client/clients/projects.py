# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""A client for a specific project, using the session of PolarionClient."""
import typing as t

from polarion_rest_api_client.clients import base_classes as bc
from polarion_rest_api_client.open_api_client.api.projects import get_project

from . import documents, test_runs, work_items

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client


class ProjectClient(bc.BaseClient):
    """A client for a specific project."""

    def __init__(
        self,
        project_id: str,
        client: "polarion_client.PolarionClient",
        delete_status: str | None = None,
        add_work_item_checksum: bool = False,
    ):
        super().__init__(project_id, client)

        self.work_items = work_items.WorkItems(
            project_id, client, delete_status, add_work_item_checksum
        )
        self.test_runs = test_runs.TestRuns(project_id, client)
        self.documents = documents.Documents(project_id, client)

    def exists(self):
        """Return True, if the clients project exists."""
        response = get_project.sync_detailed(
            self._project_id, client=self._client.client
        )
        if response.status_code == 200:
            return True
        return False
