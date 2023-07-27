# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""The actual implementation of the API client using an OpenAPIClient."""
from __future__ import annotations

import json
import logging
import typing

from polarion_rest_api_client import base_client
from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client import errors
from polarion_rest_api_client.open_api_client import client as oa_client
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.linked_work_items import (
    delete_linked_work_items,
    get_linked_work_items,
    post_linked_work_items,
)
from polarion_rest_api_client.open_api_client.api.projects import get_project
from polarion_rest_api_client.open_api_client.api.work_items import (
    delete_work_items,
    get_work_items,
    patch_work_item,
    post_work_items,
)

logger = logging.getLogger(__name__)


def _build_sparse_fields(
    fields_dict: dict[str, str] | None
) -> api_models.SparseFields | oa_types.Unset:
    """Build the SparseFields object based on a dict.

    Ensure that every key follow the pattern 'fields[XXX]'.
    """
    if fields_dict is None:
        return oa_types.Unset()
    new_field_dict: dict[str, str] = {}
    for key, value in fields_dict.items():
        if key.startswith("fields["):
            new_field_dict[key] = value
        else:
            new_field_dict[f"fields[{key}]"] = value
    return api_models.SparseFields.from_dict(new_field_dict)


def unset_str_builder(value: str | oa_types.Unset) -> str | None:
    """Return None if value is Unset, else the value."""
    if isinstance(value, oa_types.Unset):
        return None
    return value


class OpenAPIPolarionProjectClient(
    base_client.AbstractPolarionProjectApi[base_client.WIT]
):
    """A Polarion Project Client using an auto generated OpenAPI-Client."""

    client: oa_client.AuthenticatedClient

    @typing.overload
    def __init__(
        self: "OpenAPIPolarionProjectClient[base_client.WIT]",
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        custom_work_item: type[base_client.WIT],
        batch_size: int = 5,
        page_size: int = 100,
    ):
        ...

    @typing.overload
    def __init__(
        self: "OpenAPIPolarionProjectClient[dm.WorkItem]",
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        custom_work_item: type[dm.WorkItem] = dm.WorkItem,
        batch_size: int = 5,
        page_size: int = 100,
    ):
        ...

    def __init__(
        self,
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        custom_work_item=dm.WorkItem,
        batch_size: int = 5,
        page_size: int = 100,
    ):
        """Initialize the client for project and endpoint using a token."""
        super().__init__(
            project_id,
            delete_polarion_work_items,
            custom_work_item,
            batch_size,
            page_size,
        )
        self.client = oa_client.AuthenticatedClient(
            polarion_api_endpoint, polarion_access_token
        )

    def _check_response(self, response: oa_types.Response):
        def unexpected_error():
            return errors.PolarionApiUnexpectedException(
                response.status_code, response.content
            )

        if response.status_code in range(400, 600):
            try:
                error = api_models.Errors.from_dict(
                    json.loads(response.content.decode())
                )
                if error.errors:
                    raise errors.PolarionApiException(
                        *[(e.status, e.detail) for e in error.errors]
                    )
                else:
                    raise unexpected_error()
            except json.JSONDecodeError as error:
                raise unexpected_error() from error

    def _build_work_item_post_request(
        self, work_item: base_client.WIT
    ) -> api_models.WorkitemsListPostRequestDataItem:
        assert work_item.type is not None
        assert work_item.title is not None
        assert work_item.description is not None
        assert work_item.status is not None

        attrs = api_models.WorkitemsListPostRequestDataItemAttributes(
            work_item.type,
            api_models.WorkitemsListPostRequestDataItemAttributesDescription(
                api_models.WorkitemsListPostRequestDataItemAttributesDescriptionType(  # pylint: disable=line-too-long
                    work_item.description_type
                ),
                work_item.description,
            ),
            status=work_item.status,
            title=work_item.title,
        )

        attrs.additional_properties.update(work_item.additional_attributes)

        return api_models.WorkitemsListPostRequestDataItem(
            api_models.WorkitemsListPostRequestDataItemType.WORKITEMS, attrs
        )

    def _build_work_item_patch_request(
        self, work_item: base_client.WIT
    ) -> api_models.WorkitemsSinglePatchRequest:
        attrs = api_models.WorkitemsSinglePatchRequestDataAttributes()

        if work_item.title is not None:
            attrs.title = work_item.title

        if work_item.description is not None:
            attrs.description = api_models.WorkitemsSinglePatchRequestDataAttributesDescription(
                # pylint: disable=line-too-long
                api_models.WorkitemsSinglePatchRequestDataAttributesDescriptionType(  # pylint: disable=line-too-long
                    work_item.description_type
                ),
                work_item.description,
            )

        if work_item.status is not None:
            attrs.status = work_item.status

        if work_item.additional_attributes is not None:
            attrs.additional_properties.update(work_item.additional_attributes)

        return api_models.WorkitemsSinglePatchRequest(
            api_models.WorkitemsSinglePatchRequestData(
                api_models.WorkitemsSinglePatchRequestDataType.WORKITEMS,
                f"{self.project_id}/{work_item.id}",
                attrs,
            )
        )

    def project_exists(self) -> bool:
        """Return True if self.project_id exists and False if not."""
        response = get_project.sync_detailed(
            self.project_id, client=self.client
        )
        if not response.status_code == 200:
            logger.error("Polarion request: %s", response.content)
            return False
        return True

    def get_work_items(
        self,
        query: str,
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
    ) -> tuple[list[base_client.WIT], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        sparse_fields = _build_sparse_fields(fields)
        response = get_work_items.sync_detailed(
            self.project_id,
            client=self.client,
            fields=sparse_fields,
            query=query,
            pagesize=page_size,
            pagenumber=page_number,
        )

        self._check_response(response)

        work_items_response = response.parsed

        work_items: list[base_client.WIT] = []

        next_page = False
        if (
            isinstance(
                work_items_response, api_models.WorkitemsListGetResponse
            )
            and work_items_response.data
        ):
            for work_item in work_items_response.data:
                if not getattr(work_item.meta, "errors", []):
                    assert work_item.attributes
                    assert isinstance(work_item.id, str)
                    work_items.append(
                        self._work_item(
                            work_item.id.split("/")[-1],
                            unset_str_builder(work_item.attributes.title),
                            unset_str_builder(
                                work_item.attributes.description.type
                            )
                            if work_item.attributes.description
                            else None,
                            unset_str_builder(
                                work_item.attributes.description.value
                            )
                            if work_item.attributes.description
                            else None,
                            unset_str_builder(work_item.attributes.type),
                            unset_str_builder(work_item.attributes.status),
                            work_item.attributes.additional_properties,
                        )
                    )
            next_page = isinstance(
                work_items_response.links,
                api_models.WorkitemsListGetResponseLinks,
            ) and bool(work_items_response.links.next_)

        return work_items, next_page

    def _create_work_items(self, work_items: list[base_client.WIT]):
        """Create the given list of work items."""
        response = post_work_items.sync_detailed(
            self.project_id,
            client=self.client,
            json_body=api_models.WorkitemsListPostRequest(
                [
                    self._build_work_item_post_request(work_item)
                    for work_item in work_items
                ]
            ),
        )

        self._check_response(response)

    def _delete_work_items(self, work_item_ids: list[str]):
        response = delete_work_items.sync_detailed(
            self.project_id,
            client=self.client,
            json_body=api_models.WorkitemsListDeleteRequest(
                [
                    api_models.WorkitemsListDeleteRequestDataItem(
                        api_models.WorkitemsListDeleteRequestDataItemType.WORKITEMS,  # pylint: disable=line-too-long
                        f"{self.project_id}/{work_item_id}",
                    )
                    for work_item_id in work_item_ids
                ]
            ),
        )

        self._check_response(response)

    def update_work_item(self, work_item: base_client.WIT):
        """Update the given work item in Polarion.

        Only fields not set to None will be updated in Polarion. None
        fields will stay untouched.
        """
        assert work_item.id is not None

        response = patch_work_item.sync_detailed(
            self.project_id,
            work_item.id,
            client=self.client,
            json_body=self._build_work_item_patch_request(work_item),
        )

        self._check_response(response)

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
        if fields is None:
            fields = {"linkedworkitems": "id,role,suspect"}

        sparse_fields = _build_sparse_fields(fields)
        response = get_linked_work_items.sync_detailed(
            self.project_id,
            work_item_id,
            client=self.client,
            fields=sparse_fields,
            include=include,
            pagesize=page_size,
            pagenumber=page_number,
        )

        self._check_response(response)

        linked_work_item_response = response.parsed

        work_item_links: list[dm.WorkItemLink] = []
        next_page = False
        if (
            isinstance(
                linked_work_item_response,
                api_models.LinkedworkitemsListGetResponse,
            )
            and linked_work_item_response.data
        ):
            for link in linked_work_item_response.data:
                assert isinstance(link.id, str)
                assert isinstance(
                    link.attributes,
                    api_models.LinkedworkitemsListGetResponseDataItemAttributes,  # pylint: disable=line-too-long
                )
                info = link.id.split("/")
                assert len(info) == 5
                role_id, target_project_id, linked_work_item_id = info[2:]
                suspect = link.attributes.suspect
                if isinstance(suspect, oa_types.Unset):
                    suspect = False

                work_item_links.append(
                    dm.WorkItemLink(
                        work_item_id,
                        linked_work_item_id,
                        role_id,
                        suspect,
                        target_project_id,
                    )
                )

            next_page = isinstance(
                linked_work_item_response.links,
                api_models.LinkedworkitemsListGetResponseLinks,
            ) and bool(linked_work_item_response.links.next_)

        return work_item_links, next_page

    def _create_work_item_links(self, work_item_links: list[dm.WorkItemLink]):
        response = post_linked_work_items.sync_detailed(
            self.project_id,
            work_item_links[0].primary_work_item_id,
            client=self.client,
            # pylint: disable=line-too-long
            json_body=api_models.LinkedworkitemsListPostRequest(
                [
                    api_models.LinkedworkitemsListPostRequestDataItem(
                        api_models.LinkedworkitemsListPostRequestDataItemType.LINKEDWORKITEMS,
                        api_models.LinkedworkitemsListPostRequestDataItemAttributes(
                            role=work_item_link.role,
                            suspect=work_item_link.suspect or False,
                        ),
                        api_models.LinkedworkitemsListPostRequestDataItemRelationships(
                            api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItem(
                                api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemData(
                                    api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemDataType.WORKITEMS,
                                    f"{work_item_link.secondary_work_item_project}/{work_item_link.secondary_work_item_id}",
                                )
                            )
                        ),
                    )
                    for work_item_link in work_item_links
                ]
            ),
            # pylint: enable=line-too-long
        )

        self._check_response(response)

    def _delete_work_item_links(self, work_item_links: list[dm.WorkItemLink]):
        response = delete_linked_work_items.sync_detailed(
            self.project_id,
            work_item_links[0].primary_work_item_id,
            client=self.client,
            # pylint: disable=line-too-long
            json_body=api_models.LinkedworkitemsListDeleteRequest(
                [
                    api_models.LinkedworkitemsListDeleteRequestDataItem(
                        api_models.LinkedworkitemsListDeleteRequestDataItemType.LINKEDWORKITEMS,
                        f"{self.project_id}/{work_item_link.primary_work_item_id}/{work_item_link.role}/{work_item_link.secondary_work_item_project}/{work_item_link.secondary_work_item_id}",
                    )
                    for work_item_link in work_item_links
                ]
            ),
            # pylint: enable=line-too-long
        )

        self._check_response(response)
