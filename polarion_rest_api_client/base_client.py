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
    def all_types(self):
        """Return all fields dicts merged together."""
        return (
            self.workitem_attachments
            | self.workitems
            | self.linkedworkitems
            | self.documents
        )


class AbstractPolarionProjectApi(abc.ABC, t.Generic[WorkItemType]):
    """An abstract base class for a Polarion API client."""

    delete_polarion_work_items: bool
    add_work_item_checksum: bool
    project_id: str
    delete_status: str = "deleted"
    default_fields: DefaultFields
    _page_size: int = 100
    _batch_size: int = 5
    _work_item: type[WorkItemType]

    def __init__(
        self,
        project_id: str,
        delete_polarion_work_items: bool,
        custom_work_item: type[WorkItemType],
        batch_size: int = 5,
        page_size: int = 100,
        add_work_item_checksum: bool = False,
    ):
        self.project_id = project_id
        self.delete_polarion_work_items = delete_polarion_work_items
        self.default_fields = DefaultFields()
        self._batch_size = batch_size
        self._page_size = page_size
        self._work_item = custom_work_item
        self.add_work_item_checksum = add_work_item_checksum

    @abc.abstractmethod
    def project_exists(self) -> bool:
        """Return True if self.project_id exists and False if not."""
        raise NotImplementedError

    def _request_all_items(self, call: t.Callable, **kwargs) -> list[t.Any]:
        page = 1
        items, next_page = call(
            **kwargs, page_size=self._page_size, page_number=page
        )
        while next_page:
            page += 1
            _items, next_page = call(
                **kwargs, page_size=self._page_size, page_number=page
            )
            items += _items
        return items

    def get_all_work_item_attachments(
        self, work_item_id: str, fields: dict[str, str] | None = None
    ) -> list[dm.WorkItemAttachment]:
        """Get all work item attachments for a given work item.

        Will handle pagination automatically. Define a fields dictionary
        as described in the Polarion API documentation to get certain
        fields.
        """
        return self._request_all_items(
            self.get_work_item_attachments,
            fields=fields,
            work_item_id=work_item_id,
        )

    @abc.abstractmethod
    def delete_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment, retry: bool = True
    ):
        """Delete the given work item attachment."""
        raise NotImplementedError

    @abc.abstractmethod
    def update_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment, retry: bool = True
    ):
        """Update the given work item attachment in Polarion."""
        raise NotImplementedError

    @abc.abstractmethod
    def create_work_item_attachments(
        self,
        work_item_attachments: list[dm.WorkItemAttachment],
        retry: bool = True,
    ):
        """Update the given work item attachment in Polarion."""
        raise NotImplementedError

    def create_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment, retry: bool = True
    ):
        """Update the given work item attachment in Polarion."""
        self.create_work_item_attachments([work_item_attachment], retry)

    @abc.abstractmethod
    def get_work_item_attachments(
        self,
        work_item_id: str,
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[dm.WorkItemAttachment], bool]:
        """Return the attachments for a given work item on a defined page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        raise NotImplementedError

    def get_all_work_items(
        self, query: str, fields: dict[str, str] | None = None
    ) -> list[WorkItemType]:
        """Get all work items matching the given query.

        Will handle pagination automatically. Define a fields dictionary
        as described in the Polarion API documentation to get certain
        fields.
        """
        return self._request_all_items(
            self.get_work_items, fields=fields, query=query
        )

    @abc.abstractmethod
    def get_work_items(
        self,
        query: str,
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[WorkItemType], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        raise NotImplementedError

    def create_work_item(self, work_item: WorkItemType):
        """Create a single given work item."""
        self.create_work_items([work_item])

    @abc.abstractmethod
    def create_work_items(self, work_items: list[WorkItemType]):
        """Create the given list of work items."""
        raise NotImplementedError

    def delete_work_item(self, work_item_id: str):
        """Delete or mark the defined work item as deleted."""
        return self.delete_work_items([work_item_id])

    def delete_work_items(self, work_item_ids: list[str]):
        """Delete or mark the defined work items as deleted."""
        if self.delete_polarion_work_items:
            return self._delete_work_items(work_item_ids)
        return self._mark_delete_work_items(work_item_ids)

    @abc.abstractmethod
    def _delete_work_items(self, work_item_ids: list[str], retry: bool = True):
        """Actually perform a delete request for the given work items."""
        raise NotImplementedError

    def _mark_delete_work_items(self, work_item_ids: list[str]):
        """Set the status for all given work items to self.delete_status."""
        for work_item_id in work_item_ids:
            self.update_work_item(
                self._work_item(id=work_item_id, status=self.delete_status)
            )

    @abc.abstractmethod
    def update_work_item(self, work_item: WorkItemType, retry: bool = True):
        """Update the given work item in Polarion.

        Only fields not set to None will be updated in Polarion. None
        fields will stay untouched.
        """
        raise NotImplementedError

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
        return self._request_all_items(
            self.get_work_item_links,
            work_item_id=work_item_id,
            fields=fields,
            include=include,
        )

    @abc.abstractmethod
    def get_work_item_links(
        self,
        work_item_id: str,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        raise NotImplementedError

    def create_work_item_links(self, work_item_links: list[dm.WorkItemLink]):
        """Create the links between the work items in work_item_links."""
        for split_work_item_links in self._group_links(
            work_item_links
        ).values():
            for i in range(0, len(split_work_item_links), self._batch_size):
                self._create_work_item_links(
                    split_work_item_links[i : i + self._batch_size]
                )

    @abc.abstractmethod
    def _create_work_item_links(
        self, work_item_links: list[dm.WorkItemLink], retry: bool = True
    ):
        """Create the links between the work items in work_item_links.

        All work item links must have the same primary work item.
        """
        raise NotImplementedError

    def _set_project(self, work_item_link: dm.WorkItemLink):
        if work_item_link.secondary_work_item_project is None:
            work_item_link.secondary_work_item_project = self.project_id

    def _group_links(
        self,
        work_item_links: list[dm.WorkItemLink],
    ) -> dict[str, list[dm.WorkItemLink]]:
        """Group a list of work item links by their primary work item.

        Returns a dict with the primary work items as keys.
        """
        work_item_link_dict: dict[str, list[dm.WorkItemLink]] = {}
        for work_item_link in work_item_links:
            self._set_project(work_item_link)
            if work_item_link.primary_work_item_id not in work_item_link_dict:
                work_item_link_dict[work_item_link.primary_work_item_id] = []

            work_item_link_dict[work_item_link.primary_work_item_id].append(
                work_item_link
            )
        return work_item_link_dict

    def create_work_item_link(self, work_item_link: dm.WorkItemLink):
        """Create the link between the work items in work_item_link."""
        self._set_project(work_item_link)
        self._create_work_item_links([work_item_link])

    def delete_work_item_links(self, work_item_links: list[dm.WorkItemLink]):
        """Delete the links between the work items in work_item_link."""
        for split_work_item_links in self._group_links(
            work_item_links
        ).values():
            self._delete_work_item_links(split_work_item_links)

    @abc.abstractmethod
    def _delete_work_item_links(
        self, work_item_links: list[dm.WorkItemLink], retry: bool = True
    ):
        """Delete the links between the work items in work_item_link.

        All work item links have to have the same primary work item.
        """
        raise NotImplementedError

    def delete_work_item_link(self, work_item_link: dm.WorkItemLink):
        """Delete the links between the work items in work_item_link."""
        self._set_project(work_item_link)
        self._delete_work_item_links([work_item_link])
