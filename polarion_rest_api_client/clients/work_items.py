# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json
import logging
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client import errors
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.work_items import (
    delete_work_items,
    get_work_item,
    get_work_items,
    patch_work_item,
    post_work_items,
)

from . import base_classes as bc
from . import work_item_attachments, work_item_links

WorkItemType = t.TypeVar("WorkItemType", bound=dm.WorkItem)
logger = logging.getLogger(__name__)


def _get_json_content_size(data: dict):
    return len(json.dumps(data).encode("utf-8"))


min_wi_request_size = _get_json_content_size(
    api_models.WorkitemsListPostRequest(data=[]).to_dict()
)


class WorkItems(bc.StatusItemClient, t.Generic[WorkItemType]):
    def __init__(
        self,
        project_id: str,
        client: "polarion_client.PolarionClient",
        delete_status: str | None = None,
        add_work_item_checksum: bool = False,
    ):
        super().__init__(project_id, client, delete_status)
        self.attachments = work_item_attachments.WorkItemAttachments(
            project_id, client
        )
        self.links = work_item_links.WorkItemLinks(project_id, client)
        self.add_work_item_checksum = add_work_item_checksum

    def _update_single(self, work_item: WorkItemType):
        assert work_item.id is not None
        if work_item.type:
            logger.warning(
                "Attempting to change the type of Work Item %s to %s.",
                work_item.id,
                work_item.type,
            )

        response = patch_work_item.sync_detailed(
            self._project_id,
            work_item.id,
            client=self._client.client,
            change_type_to=work_item.type or oa_types.UNSET,
            body=self._build_work_item_patch_request(work_item),
        )
        self._raise_on_error(response)

    def _update(self, items: list[WorkItemType]):
        for work_item in items:
            self._retry_on_error(self._update_single, work_item)

    def _get_multi(
        self,
        query: str = "",
        fields: dict[str, str] | None = None,
        work_item_cls: type[WorkItemType] = dm.WorkItem,
        page_size: int = 100,
        page_number: int = 1,
    ) -> tuple[list[WorkItemType], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.workitems

        sparse_fields = self._build_sparse_fields(fields)
        response = get_work_items.sync_detailed(
            self._project_id,
            client=self._client.client,
            fields=sparse_fields,
            query=query,
            pagesize=page_size,
            pagenumber=page_number,
        )

        self._raise_on_error(response)

        work_items_response = response.parsed

        work_items: list[WorkItemType] = []

        next_page = False
        if (
            isinstance(
                work_items_response, api_models.WorkitemsListGetResponse
            )
            and work_items_response.data
        ):
            work_items = [
                self._generate_work_item(work_item, work_item_cls)
                for work_item in work_items_response.data
                if not getattr(work_item.meta, "errors", [])
            ]

            next_page = isinstance(
                work_items_response.links,
                api_models.WorkitemsListGetResponseLinks,
            ) and bool(work_items_response.links.next_)

        return work_items, next_page

    def _get(
        self,
        work_item_id: str,
        work_item_cls: type[WorkItemType] = dm.WorkItem,
    ) -> WorkItemType | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True.
        """
        response = get_work_item.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(
                {
                    "workitems": "@all",
                    "workitem_attachments": "@all",
                    "linkedworkitems": "@all",
                }
            ),
        )
        self._raise_on_error(response)

        if isinstance(
            response.parsed, api_models.WorkitemsSingleGetResponse
        ) and isinstance(
            response.parsed.data, api_models.WorkitemsSingleGetResponseData
        ):
            return self._generate_work_item(
                response.parsed.data, work_item_cls
            )

        return None

    def _create(self, items: list[WorkItemType]):
        raise NotImplementedError("We have a custom create instead.")

    def create(self, items: WorkItemType | list[WorkItemType]):
        current_batch = api_models.WorkitemsListPostRequest(data=[])
        content_size = min_wi_request_size
        batch_start_index = 0
        batch_end_index = 0

        for work_item in items:
            work_item_data = self._build_work_item_post_request(work_item)

            (
                proj_content_size,
                too_big,
            ) = self._calculate_post_work_item_request_sizes(
                work_item_data, content_size
            )

            if too_big:
                raise errors.PolarionWorkItemException(
                    "A WorkItem is too large to create.", work_item
                )

            assert isinstance(current_batch.data, list)
            if (
                proj_content_size >= self._client.max_content_size
                or len(current_batch.data) >= self._client.batch_size
            ):
                self._retry_on_error(
                    self._post_work_item_batch,
                    current_batch,
                    items[batch_start_index:batch_end_index],
                )

                current_batch = api_models.WorkitemsListPostRequest(
                    data=[work_item_data]
                )
                content_size = _get_json_content_size(current_batch.to_dict())
                batch_start_index = batch_end_index
            else:
                assert isinstance(current_batch.data, list)
                current_batch.data.append(work_item_data)
                content_size = proj_content_size

            batch_end_index += 1

        if current_batch.data:
            self._retry_on_error(
                self._post_work_item_batch,
                current_batch,
                items[batch_start_index:],
            )

    def _delete(self, items: WorkItemType | list[WorkItemType]):
        work_item_ids = [work_item.id for work_item in items]
        response = delete_work_items.sync_detailed(
            self._project_id,
            client=self._client.client,
            body=api_models.WorkitemsListDeleteRequest(
                data=[
                    api_models.WorkitemsListDeleteRequestDataItem(
                        type=api_models.WorkitemsListDeleteRequestDataItemType.WORKITEMS,  # pylint: disable=line-too-long
                        id=f"{self._project_id}/{work_item_id}",
                    )
                    for work_item_id in work_item_ids
                ]
            ),
        )
        self._raise_on_error(response)

    def _build_work_item_post_request(
        self, work_item: WorkItemType
    ) -> api_models.WorkitemsListPostRequestDataItem:
        assert work_item.type is not None
        assert work_item.title is not None
        assert work_item.description is not None
        assert work_item.status is not None

        attrs = api_models.WorkitemsListPostRequestDataItemAttributes(
            type=work_item.type,
            description=api_models.WorkitemsListPostRequestDataItemAttributesDescription(  # pylint: disable=line-too-long
                type=api_models.WorkitemsListPostRequestDataItemAttributesDescriptionType(  # pylint: disable=line-too-long
                    work_item.description_type
                ),
                value=work_item.description,
            ),
            status=work_item.status,
            title=work_item.title,
        )

        attrs.additional_properties.update(work_item.additional_attributes)

        if self.add_work_item_checksum:
            attrs.additional_properties["checksum"] = (
                work_item.calculate_checksum()
            )

        return api_models.WorkitemsListPostRequestDataItem(
            type=api_models.WorkitemsListPostRequestDataItemType.WORKITEMS,
            attributes=attrs,
        )

    def _build_work_item_patch_request(
        self, work_item: WorkItemType
    ) -> api_models.WorkitemsSinglePatchRequest:
        attrs = api_models.WorkitemsSinglePatchRequestDataAttributes()

        if work_item.title is not None:
            attrs.title = work_item.title

        if work_item.description is not None:
            attrs.description = api_models.WorkitemsSinglePatchRequestDataAttributesDescription(  # pylint: disable=line-too-long
                type=api_models.WorkitemsSinglePatchRequestDataAttributesDescriptionType(  # pylint: disable=line-too-long
                    work_item.description_type
                ),
                value=work_item.description,
            )

        if work_item.status is not None:
            attrs.status = work_item.status

        attrs.additional_properties.update(work_item.additional_attributes)

        if self.add_work_item_checksum:
            attrs.additional_properties["checksum"] = (
                work_item.get_current_checksum()
            )

        return api_models.WorkitemsSinglePatchRequest(
            data=api_models.WorkitemsSinglePatchRequestData(
                type=api_models.WorkitemsSinglePatchRequestDataType.WORKITEMS,
                id=f"{self._project_id}/{work_item.id}",
                attributes=attrs,
            )
        )

    def _post_work_item_batch(
        self,
        work_item_batch: api_models.WorkitemsListPostRequest,
        work_item_objs: list[WorkItemType],
    ):
        response = post_work_items.sync_detailed(
            self._project_id, client=self._client.client, body=work_item_batch
        )

        self._raise_on_error(response)

        assert (
            isinstance(response.parsed, api_models.WorkitemsListPostResponse)
            and response.parsed.data
        )
        counter = 0
        for work_item_res in response.parsed.data:
            assert work_item_res.id
            work_item_objs[counter].id = work_item_res.id.split("/")[-1]
            counter += 1

    def _calculate_post_work_item_request_sizes(
        self,
        work_item_data: api_models.WorkitemsListPostRequestDataItem,
        current_content_size: int = min_wi_request_size,
    ) -> t.Tuple[int, bool]:
        work_item_size = _get_json_content_size(work_item_data.to_dict())

        proj_content_size = current_content_size + work_item_size
        if current_content_size != min_wi_request_size:
            proj_content_size += len(b", ")

        return (
            proj_content_size,
            (work_item_size + min_wi_request_size)
            > self._client.max_content_size,
        )

    def _generate_work_item(
        self,
        work_item: (
            api_models.WorkitemsListGetResponseDataItem
            | api_models.WorkitemsSingleGetResponseData
        ),
        work_item_cls: t.Type[WorkItemType] = dm.WorkItem,
    ) -> WorkItemType:
        assert work_item.attributes
        assert isinstance(work_item.id, str)
        work_item_id = work_item.id.split("/")[-1]
        links = []
        attachments = []

        # We set both truncated flags to True and will only set them to False,
        # if the corresponding fields were requested and returned completely
        links_truncated = True
        attachments_truncated = True
        if work_item.relationships:
            if links := work_item.relationships.linked_work_items:
                if not links.meta or links.meta.total_count is oa_types.UNSET:
                    links_truncated = False

                links = [
                    self.links._parse_work_item_link(
                        link.id,
                        link.additional_properties.get("suspect", False),
                        work_item_id,
                    )
                    for link in links.data or []
                ]

            if attachment_data := work_item.relationships.attachments:
                if (
                    not attachment_data.meta
                    or attachment_data.meta.total_count is oa_types.UNSET
                ):
                    attachments_truncated = False

                attachments = [
                    dm.WorkItemAttachment(
                        work_item_id,
                        attachment.id.split("/")[-1],
                        None,  # title isn't provided
                    )
                    for attachment in attachment_data.data or []
                    if attachment.id
                ]

        desctype = None
        desc = None
        if work_item.attributes.description:
            desctype = self.unset_to_none(
                work_item.attributes.description.type
            )
            desc = self.unset_to_none(work_item.attributes.description.value)

        work_item_obj = work_item_cls(
            work_item_id,
            self.unset_to_none(work_item.attributes.title),
            desctype,
            desc,
            self.unset_to_none(work_item.attributes.type),
            self.unset_to_none(work_item.attributes.status),
            work_item.attributes.additional_properties,
            links,
            attachments,
            links_truncated,
            attachments_truncated,
        )
        return work_item_obj
