# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""The old client, which is deprecated, but uses the new client."""
from __future__ import annotations

import typing as t
import warnings

from polarion_rest_api_client import client
from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.client import WorkItemType


class OpenAPIPolarionProjectClient(t.Generic[WorkItemType]):
    """A Polarion Project Client using an auto generated OpenAPI-Client."""

    delete_status: str = "deleted"

    @t.overload
    def __init__(
        self: "OpenAPIPolarionProjectClient[client.WorkItemType]",
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        *,
        custom_work_item: type[client.WorkItemType],
        batch_size: int = ...,
        page_size: int = ...,
        add_work_item_checksum: bool = False,
        max_content_size: int = ...,
        httpx_args: t.Optional[dict[str, t.Any]] = ...,
    ): ...

    @t.overload
    def __init__(
        self: "OpenAPIPolarionProjectClient[dm.WorkItem]",
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        *,
        batch_size: int = ...,
        page_size: int = ...,
        add_work_item_checksum: bool = False,
        max_content_size: int = ...,
        httpx_args: t.Optional[dict[str, t.Any]] = ...,
    ): ...

    def __init__(
        self,
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        *,
        custom_work_item=dm.WorkItem,
        batch_size: int = 100,
        page_size: int = 100,
        add_work_item_checksum: bool = False,
        max_content_size: int = 2 * 1024**2,
        httpx_args: t.Optional[dict[str, t.Any]] = None,
    ):
        """Initialize the client for project and endpoint using a token.

        Parameters
        ----------
        project_id : str
            ID of the project to create a client for.
        delete_polarion_work_items : bool
            Flag indicating whether to delete work items or set a status.
        polarion_api_endpoint : str
            The URL of the Polarion API endpoint.
        polarion_access_token : str
            A personal access token to access the API.
        custom_work_item : default dm.WorkItem
            Custom WorkItem class with additional attributes.
        batch_size : int, default 100
            Maximum amount of items created in one POST request.
        page_size : int, default 100
            Default size of a page when getting items from the API.
        add_work_item_checksum : bool, default False
            Flag whether post WorkItem checksums.
        max_content_size : int, default 2 * 1024**2
            Maximum content-length of the API (default: 2MB).
        httpx_args: t.Optional[dict[str, t.Any]], default None
            Additional parameters, which will be passed to the httpx client.
        """
        warnings.warn(
            f"{self.__class__.__name__} will be deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )

        polarion_client = client.PolarionClient(
            polarion_api_endpoint,
            polarion_access_token,
            httpx_args,
            batch_size,
            page_size,
            max_content_size,
        )
        self.project_client = polarion_client.generate_project_client(
            project_id,
            None if delete_polarion_work_items else "deleted",
            add_work_item_checksum,
        )
        self.project_id = project_id
        self.custom_work_item = custom_work_item

    def project_exists(self) -> bool:
        """Return True if self.project_id exists and False if not."""
        return self.project_client.exists()

    def delete_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment
    ):
        """Delete the given work item attachment."""
        self.project_client.work_items.attachments.delete(work_item_attachment)

    def update_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment
    ):
        """Update the given work item attachment in Polarion."""
        self.project_client.work_items.attachments.update(work_item_attachment)

    def create_work_item_attachments(
        self,
        work_item_attachments: list[dm.WorkItemAttachment],
    ):
        """Create the given work item attachment in Polarion."""
        self.project_client.work_items.attachments.create(
            work_item_attachments
        )

    def get_work_item(
        self,
        work_item_id: str,
    ) -> client.WorkItemType | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True.
        """
        return self.project_client.work_items.get(
            work_item_id, self.custom_work_item
        )

    def get_document(
        self,
        space_id: str,
        document_name: str,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        revision: str | None = None,
    ) -> dm.Document | None:
        """Return the document with the given document_name and space_id."""
        return self.project_client.documents.get(
            space_id,
            document_name,
            fields=fields,
            include=include,
            revision=revision,
        )

    def create_work_items(self, work_items: list[client.WorkItemType]):
        """Create the given list of work items."""
        self.project_client.work_items.create(work_items)

    def update_work_item(self, work_item: client.WorkItemType):
        """Update the given work item in Polarion.

        Only fields not set to None will be updated in Polarion. None
        fields will stay untouched.
        """
        self.project_client.work_items.update(work_item)

    def get_work_item_links(
        self,
        work_item_id: str,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        page_size: int = 100,
        page_number: int = 1,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        return self.project_client.work_items.links.get_multi(
            work_item_id,
            page_size=page_size,
            page_number=page_number,
            fields=fields,
            include=include,
        )

    def get_test_records(
        self,
        test_run_id: str,
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
    ) -> tuple[list[dm.TestRecord], bool]:
        """Return the test records on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        return self.project_client.test_runs.records.get_multi(
            test_run_id,
            fields=fields,
            page_size=page_size,
            page_number=page_number,
        )

    def get_test_runs(
        self,
        query: str = "",
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
    ) -> tuple[list[dm.TestRun], bool]:
        """Return the test runs on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        return self.project_client.test_runs.get_multi(
            query, fields=fields, page_size=page_size, page_number=page_number
        )

    def create_test_runs(self, test_runs: list[dm.TestRun]):
        """Create the given list of test runs."""
        self.project_client.test_runs.create(test_runs)

    def update_test_run(self, test_run: dm.TestRun):
        """Create the given list of test runs."""
        self.project_client.test_runs.update(test_run)

    def create_test_records(
        self,
        test_run_id: str,
        test_records: list[dm.TestRecord],
    ):
        """Create the given list of test records."""
        for rec in test_records:
            rec.test_run_id = test_run_id
        self.project_client.test_runs.records.create(test_records)

    def update_test_record(self, test_run_id: str, test_record: dm.TestRecord):
        """Create the given list of test records."""
        test_record.test_run_id = test_run_id
        self.project_client.test_runs.records.update(test_record)

    def get_all_work_item_attachments(
        self, work_item_id: str, fields: dict[str, str] | None = None
    ) -> list[dm.WorkItemAttachment]:
        """Get all work item attachments for a given work item.

        Will handle pagination automatically. Define a fields dictionary
        as described in the Polarion API documentation to get certain
        fields.
        """
        return self.project_client.work_items.attachments.get_all(
            work_item_id, fields=fields
        )

    def create_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment
    ):
        """Update the given work item attachment in Polarion."""
        self.project_client.work_items.attachments.create(work_item_attachment)

    def get_all_work_items(
        self, query: str = "", fields: dict[str, str] | None = None
    ) -> list[WorkItemType]:
        """Get all work items matching the given query.

        Will handle pagination automatically. Define a fields dictionary
        as described in the Polarion API documentation to get certain
        fields.
        """
        return self.project_client.work_items.get_all(
            query, fields=fields, work_item_cls=self.custom_work_item
        )

    def create_work_item(self, work_item: WorkItemType):
        """Create a single given work item."""
        self.create_work_items([work_item])

    def delete_work_items(self, work_item_ids: list[str]):
        """Delete or mark the defined work items as deleted."""
        self.project_client.work_items.delete(
            [dm.WorkItem(wid) for wid in work_item_ids]
        )

    def delete_work_item(self, work_item_id: str):
        """Delete or mark the defined work item as deleted."""
        return self.delete_work_items([work_item_id])

    def get_all_work_item_links(
        self,
        work_item_id: str,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> list[dm.WorkItemLink]:
        """Get all work item links for the given work item.

        Define a fields dictionary as described in the Polarion API
        documentation to get certain fields.
        """
        return self.project_client.work_items.links.get_all(
            work_item_id=work_item_id,
            fields=fields,
            include=include,
        )

    def create_work_item_links(self, work_item_links: list[dm.WorkItemLink]):
        """Create the links between the work items in work_item_links."""
        self.project_client.work_items.links.create(work_item_links)

    def create_work_item_link(self, work_item_link: dm.WorkItemLink):
        """Create the link between the work items in work_item_link."""
        self.create_work_item_links([work_item_link])

    def delete_work_item_links(self, work_item_links: list[dm.WorkItemLink]):
        """Delete the links between the work items in work_item_link."""
        self.project_client.work_items.links.delete(work_item_links)

    def delete_work_item_link(self, work_item_link: dm.WorkItemLink):
        """Delete the links between the work items in work_item_link."""
        self.delete_work_item_links([work_item_link])

    def get_all_test_runs(
        self,
        query: str = "",
        fields: dict[str, str] | None = None,
    ) -> list[dm.TestRun]:
        """Get all test runs matching the given query.

        Will handle pagination automatically. Define a fields dictionary
        as described in the Polarion API documentation to get certain
        fields.
        """
        return self.project_client.test_runs.get_all(query, fields=fields)

    def get_all_test_records(
        self,
        test_run_id: str,
        fields: dict[str, str] | None = None,
    ) -> list[dm.TestRecord]:
        """Get all test records matching the given query.

        Will handle pagination automatically. Define a fields dictionary
        as described in the Polarion API documentation to get certain
        fields.
        """
        return self.project_client.test_runs.records.get_all(
            test_run_id, fields=fields
        )

    def create_test_run(self, test_run: dm.TestRun):
        """Create the given test run."""
        self.create_test_runs([test_run])

    def create_test_record(self, test_run_id: str, test_record: dm.TestRecord):
        """Create the given list of test records."""
        self.create_test_records(test_run_id, [test_record])
