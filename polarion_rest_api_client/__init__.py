# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Polarion API module with data classes and an abstract API client."""
import abc
import dataclasses
import typing as t


@dataclasses.dataclass
class WorkItem:
    """A data class containing all relevant data of a Polarion WorkItem."""

    id: str | None = None
    title: str | None = None
    description_type: str | None = None
    description: str | None = None
    type: str | None = None
    status: str | None = None
    additional_attributes: dict[str, t.Any] = dataclasses.field(
        default_factory=dict
    )


@dataclasses.dataclass
class WorkItemLink:
    """A link between multiple Polarion WorkItems.

    The primary_work_item_id is the ID of the owner of the link, the
    secondary_work_item_id represents the linked workitem.
    """

    primary_work_item_id: str
    secondary_work_item_id: str
    role: str
    suspect: bool | None = None
    secondary_work_item_project: str | None = (
        None  # Use to set differing project
    )


class PolarionApiBaseException(Exception):
    """Base exception, which is raised, if an API error occurs."""


class PolarionApiException(PolarionApiBaseException):
    """Exception, which is raised, if an error is raised by the API."""


class PolarionApiUnexpectedException(PolarionApiBaseException):
    """Exception, which is raised, if an unexpected error is raised."""


class AbstractPolarionProjectApi(abc.ABC):
    """An abstract base class for a Polarion API client."""

    delete_polarion_work_items: bool
    project_id: str
    delete_status: str = "deleted"
    _page_size: int = 100
    _batch_size: int = 5

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

    def get_all_work_items(
        self, query: str, fields: dict[str, str] | None = None
    ) -> list[WorkItem]:
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
    ) -> tuple[list[WorkItem], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        raise NotImplementedError

    def create_work_item(self, work_item: WorkItem):
        """Create a single given work item."""
        return self.create_work_items([work_item])

    def create_work_items(self, work_items: list[WorkItem]):
        """Create the given list of work items."""
        for i in range(0, len(work_items), self._batch_size):
            self._create_work_items(work_items[i : i + self._batch_size])

    @abc.abstractmethod
    def _create_work_items(self, work_items: list[WorkItem]):
        """Create the given list of work items.

        A maximum of 5 items is allowed only at once.
        """
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
    def _delete_work_items(self, work_item_ids: list[str]):
        """Actually perform a delete request for the given work items."""
        raise NotImplementedError

    def _mark_delete_work_items(self, work_item_ids: list[str]):
        """Set the status for all given work items to self.delete_status."""
        for work_item_id in work_item_ids:
            self.update_work_item(
                WorkItem(id=work_item_id, status=self.delete_status)
            )

    @abc.abstractmethod
    def update_work_item(self, work_item: WorkItem):
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
    ) -> list[WorkItemLink]:
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
    ) -> tuple[list[WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        raise NotImplementedError

    def create_work_item_links(self, work_item_links: list[WorkItemLink]):
        """Create the links between the work items in work_item_links."""
        for split_work_item_links in self._group_links(
            work_item_links
        ).values():
            for i in range(0, len(split_work_item_links), self._batch_size):
                self._create_work_item_links(
                    split_work_item_links[i : i + self._batch_size]
                )

    @abc.abstractmethod
    def _create_work_item_links(self, work_item_links: list[WorkItemLink]):
        """Create the links between the work items in work_item_links.

        All work item links must have the same primary work item.
        """
        raise NotImplementedError

    def _set_project(self, work_item_link: WorkItemLink):
        if work_item_link.secondary_work_item_project is None:
            work_item_link.secondary_work_item_project = self.project_id

    def _group_links(
        self,
        work_item_links: list[WorkItemLink],
    ) -> dict[str, list[WorkItemLink]]:
        """Group a list of work item links by their primary work item.

        Returns a dict with the primary work items as keys.
        """
        work_item_link_dict: dict[str, list[WorkItemLink]] = {}
        for work_item_link in work_item_links:
            self._set_project(work_item_link)
            if work_item_link.primary_work_item_id not in work_item_link_dict:
                work_item_link_dict[work_item_link.primary_work_item_id] = []

            work_item_link_dict[work_item_link.primary_work_item_id].append(
                work_item_link
            )
        return work_item_link_dict

    def create_work_item_link(self, work_item_link: WorkItemLink):
        """Create the link between the work items in work_item_link."""
        self._set_project(work_item_link)
        self._create_work_item_links([work_item_link])

    def delete_work_item_links(self, work_item_links: list[WorkItemLink]):
        """Delete the links between the work items in work_item_link."""
        for split_work_item_links in self._group_links(
            work_item_links
        ).values():
            self._delete_work_item_links(split_work_item_links)

    @abc.abstractmethod
    def _delete_work_item_links(self, work_item_links: list[WorkItemLink]):
        """Delete the links between the work items in work_item_link.

        All work item links have to have the same primary work item.
        """
        raise NotImplementedError

    def delete_work_item_link(self, work_item_link: WorkItemLink):
        """Delete the links between the work items in work_item_link."""
        self._set_project(work_item_link)
        self._delete_work_item_links([work_item_link])


from polarion_rest_api_client.client import *
