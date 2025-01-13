# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementation of LinkedWorkItems operations."""
import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.linked_work_items import (
    delete_linked_work_items,
    get_linked_work_items,
    post_linked_work_items,
)

from . import base_classes as bc


class WorkItemLinks(bc.ItemsClient[dm.WorkItemLink]):
    """A client providing LinkedWorkItems functions."""

    def get(self, *args, **kwargs) -> dm.WorkItemLink:
        """Return a specific link - not implemented yet."""
        raise NotImplementedError

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.linkedworkitems

        if include is None:
            include = oa_types.UNSET

        sparse_fields = self._build_sparse_fields(fields)
        response = get_linked_work_items.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            include=include,
            pagesize=page_size,
            pagenumber=page_number,
        )

        self._raise_on_error(response)

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

                work_item_links.append(
                    self._parse_work_item_link(
                        link.id, link.attributes.suspect, work_item_id
                    )
                )

            next_page = isinstance(
                linked_work_item_response.links,
                api_models.LinkedworkitemsListGetResponseLinks,
            ) and bool(linked_work_item_response.links.next_)

        return work_item_links, next_page

    def _parse_work_item_link(self, link_id, suspect, work_item_id):
        info = link_id.split("/")
        assert len(info) == 5
        role_id, target_project_id, linked_work_item_id = info[2:]
        if isinstance(suspect, oa_types.Unset):
            suspect = False
        work_item_link = dm.WorkItemLink(
            work_item_id,
            linked_work_item_id,
            role_id,
            suspect,
            target_project_id,
        )
        return work_item_link

    def _split_into_batches(
        self, items: list[dm.WorkItemLink]
    ) -> t.Generator[list[dm.WorkItemLink], None, None]:
        for _, group in itertools.groupby(
            items, lambda x: x.primary_work_item_id
        ):
            yield from super()._split_into_batches(list(group))

    def _create(self, items: list[dm.WorkItemLink]):
        response = post_linked_work_items.sync_detailed(
            self._project_id,
            items[0].primary_work_item_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=api_models.LinkedworkitemsListPostRequest(
                data=[
                    api_models.LinkedworkitemsListPostRequestDataItem(
                        type=api_models.LinkedworkitemsListPostRequestDataItemType.LINKEDWORKITEMS,
                        attributes=api_models.LinkedworkitemsListPostRequestDataItemAttributes(
                            role=work_item_link.role,
                            suspect=work_item_link.suspect or False,
                        ),
                        relationships=api_models.LinkedworkitemsListPostRequestDataItemRelationships(
                            work_item=api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItem(
                                data=api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemData(
                                    type=api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemDataType.WORKITEMS,
                                    id=f"{work_item_link.secondary_work_item_project or self._project_id}/{work_item_link.secondary_work_item_id}",
                                )
                            )
                        ),
                    )
                    for work_item_link in items
                ]
            ),
            # pylint: enable=line-too-long
        )

        self._raise_on_error(response)

    def _delete(self, items: list[dm.WorkItemLink]):
        response = delete_linked_work_items.sync_detailed(
            self._project_id,
            items[0].primary_work_item_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=api_models.LinkedworkitemsListDeleteRequest(
                data=[
                    api_models.LinkedworkitemsListDeleteRequestDataItem(
                        type=api_models.LinkedworkitemsListDeleteRequestDataItemType.LINKEDWORKITEMS,
                        id=f"{self._project_id}/{work_item_link.primary_work_item_id}/{work_item_link.role}/{work_item_link.secondary_work_item_project or self._project_id}/{work_item_link.secondary_work_item_id}",
                    )
                    for work_item_link in items
                ]
            ),
            # pylint: enable=line-too-long
        )
        self._raise_on_error(response)
