# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""The actual implementation of the API client using an OpenAPIClient."""
from __future__ import annotations

import io
import json
import logging
import os
import random
import time
import typing as t
import urllib.parse

from polarion_rest_api_client import base_client
from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client import errors
from polarion_rest_api_client.open_api_client import client as oa_client
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.documents import get_document
from polarion_rest_api_client.open_api_client.api.linked_work_items import (
    delete_linked_work_items,
    get_linked_work_items,
    post_linked_work_items,
)
from polarion_rest_api_client.open_api_client.api.projects import get_project
from polarion_rest_api_client.open_api_client.api.test_records import (
    get_test_records,
    patch_test_record,
    post_test_records,
)
from polarion_rest_api_client.open_api_client.api.test_runs import (
    get_test_runs,
    patch_test_run,
    post_test_runs,
)
from polarion_rest_api_client.open_api_client.api.work_item_attachments import (  # pylint: disable=line-too-long
    delete_work_item_attachment,
    get_work_item_attachments,
    patch_work_item_attachment,
    post_work_item_attachments,
)
from polarion_rest_api_client.open_api_client.api.work_items import (
    delete_work_items,
    get_work_item,
    get_work_items,
    patch_work_item,
    post_work_items,
)

logger = logging.getLogger(__name__)


def _get_json_content_size(data: dict):
    return len(json.dumps(data).encode("utf-8"))


min_wi_request_size = _get_json_content_size(
    api_models.WorkitemsListPostRequest([]).to_dict()
)


def _build_sparse_fields(
    fields_dict: dict[str, str]
) -> api_models.SparseFields | oa_types.Unset:
    """Build the SparseFields object based on a dict.

    Ensure that every key follow the pattern 'fields[XXX]'.
    """
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


def sleep_random_time(_min: int = 5, _max: int = 15):
    """Sleep for _min-_max seconds with defaults of 5-15 seconds."""
    time.sleep(random.uniform(_min, _max))


class OpenAPIPolarionProjectClient(
    base_client.AbstractPolarionProjectApi[base_client.WorkItemType]
):
    """A Polarion Project Client using an auto generated OpenAPI-Client."""

    client: oa_client.AuthenticatedClient

    @t.overload
    def __init__(
        self: "OpenAPIPolarionProjectClient[base_client.WorkItemType]",
        project_id: str,
        delete_polarion_work_items: bool,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        *,
        custom_work_item: type[base_client.WorkItemType],
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
        super().__init__(
            project_id,
            delete_polarion_work_items,
            custom_work_item,
            batch_size,
            page_size,
            add_work_item_checksum,
        )

        if httpx_args is None:
            httpx_args = {}

        if "proxies" not in httpx_args:
            httpx_args["proxies"] = os.getenv("PROXIES")

        self.client = oa_client.AuthenticatedClient(
            polarion_api_endpoint, polarion_access_token, httpx_args=httpx_args
        )
        self._batch_size = batch_size
        self._page_size = page_size
        self._max_content_size = max_content_size

    def _check_response(
        self, response: oa_types.Response, _raise: bool
    ) -> bool:
        def unexpected_error():
            return errors.PolarionApiUnexpectedException(
                response.status_code, response.content
            )

        if response.status_code not in range(400, 600):
            return True

        if not _raise:
            logger.warning(
                "Received error response code %d with content %s.",
                response.status_code,
                response.content,
            )
            return False

        if (
            isinstance(response.parsed, api_models.Errors)
            and response.parsed.errors
        ):
            raise errors.PolarionApiException(
                *[
                    (
                        e.status,
                        e.detail,
                        (
                            e.source.pointer
                            if not (
                                isinstance(e.source, oa_types.Unset)
                                or e.source is None
                            )
                            else "No error pointer"
                        ),
                    )
                    for e in response.parsed.errors
                ]
            )
        raise unexpected_error()

    def _build_work_item_post_request(
        self, work_item: base_client.WorkItemType
    ) -> api_models.WorkitemsListPostRequestDataItem:
        assert work_item.type is not None
        assert work_item.title is not None
        assert work_item.description is not None
        assert work_item.status is not None

        attrs = api_models.WorkitemsListPostRequestDataItemAttributes(
            type=work_item.type,
            description=api_models.WorkitemsListPostRequestDataItemAttributesDescription(
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
        self, work_item: base_client.WorkItemType
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
                id=f"{self.project_id}/{work_item.id}",
                attributes=attrs,
            )
        )

    def _post_work_item_batch(
        self,
        work_item_batch: api_models.WorkitemsListPostRequest,
        work_item_objs: list[base_client.WorkItemType],
        retry: bool = True,
    ):
        response = post_work_items.sync_detailed(
            self.project_id, client=self.client, body=work_item_batch
        )
        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self._post_work_item_batch(work_item_batch, work_item_objs, False)
            return

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
            (work_item_size + min_wi_request_size) > self._max_content_size,
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
        if fields is None:
            fields = self.default_fields.workitem_attachments

        sparse_fields = _build_sparse_fields(fields)
        response = get_work_item_attachments.sync_detailed(
            self.project_id,
            work_item_id=work_item_id,
            client=self.client,
            fields=sparse_fields,
            pagesize=page_size,
            pagenumber=page_number,
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_work_item_attachments(
                work_item_id, fields, page_size, page_number, False
            )

        parsed_response = response.parsed

        work_item_attachments: list[dm.WorkItemAttachment] = []

        next_page = False

        if (
            isinstance(
                parsed_response, api_models.WorkitemAttachmentsListGetResponse
            )
            and parsed_response.data
        ):
            for attachment in parsed_response.data:
                assert attachment.attributes
                assert isinstance(attachment.attributes.id, str)

                work_item_attachments.append(
                    dm.WorkItemAttachment(
                        work_item_id,
                        attachment.attributes.id,
                        unset_str_builder(attachment.attributes.title),
                        file_name=unset_str_builder(
                            attachment.attributes.file_name
                        ),
                    )
                )

            next_page = isinstance(
                parsed_response.links,
                api_models.WorkitemAttachmentsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)

        return work_item_attachments, next_page

    def delete_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment, retry: bool = True
    ):
        """Delete the given work item attachment."""
        response = delete_work_item_attachment.sync_detailed(
            self.project_id,
            work_item_attachment.work_item_id,
            work_item_attachment.id,
            client=self.client,
        )
        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.delete_work_item_attachment(work_item_attachment, False)

    def update_work_item_attachment(
        self, work_item_attachment: dm.WorkItemAttachment, retry: bool = True
    ):
        """Update the given work item attachment in Polarion."""
        attributes = (
            api_models.WorkitemAttachmentsSinglePatchRequestDataAttributes()
        )
        if work_item_attachment.title:
            attributes.title = work_item_attachment.title

        multipart = api_models.PatchWorkItemAttachmentsRequestBody(
            resource=api_models.WorkitemAttachmentsSinglePatchRequest(
                data=api_models.WorkitemAttachmentsSinglePatchRequestData(
                    type=api_models.WorkitemAttachmentsSinglePatchRequestDataType.WORKITEM_ATTACHMENTS,  # pylint: disable=line-too-long
                    id=f"{self.project_id}/{work_item_attachment.work_item_id}/{work_item_attachment.id}",  # pylint: disable=line-too-long
                    attributes=attributes,
                )
            )
        )

        if work_item_attachment.content_bytes:
            multipart.content = oa_types.File(
                io.BytesIO(work_item_attachment.content_bytes),
                work_item_attachment.file_name,
                work_item_attachment.mime_type,
            )

        response = patch_work_item_attachment.sync_detailed(
            self.project_id,
            work_item_attachment.work_item_id,
            work_item_attachment.id,
            client=self.client,
            body=multipart,
        )
        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.update_work_item_attachment(work_item_attachment, False)

    def create_work_item_attachments(
        self,
        work_item_attachments: list[dm.WorkItemAttachment],
        retry: bool = True,
    ):
        """Create the given work item attachment in Polarion."""
        attachment_attributes = []
        attachment_files = []
        assert len(work_item_attachments), "No attachments were provided."
        assert all(
            [wia.work_item_id == work_item_attachments[0].work_item_id]
            for wia in work_item_attachments
        ), "All attachments must belong to the same WorkItem."

        for work_item_attachment in work_item_attachments:
            assert (
                work_item_attachment.file_name
            ), "You have to define a FileName."
            assert (
                work_item_attachment.content_bytes
            ), "You have to provide content bytes."
            assert (
                work_item_attachment.mime_type
            ), "You have to provide a mime_type."

            attributes = api_models.WorkitemAttachmentsListPostRequestDataItemAttributes(  # pylint: disable=line-too-long
                file_name=work_item_attachment.file_name
            )
            if work_item_attachment.title:
                attributes.title = work_item_attachment.title

            attachment_attributes.append(
                api_models.WorkitemAttachmentsListPostRequestDataItem(
                    type=api_models.WorkitemAttachmentsListPostRequestDataItemType.WORKITEM_ATTACHMENTS,  # pylint: disable=line-too-long
                    attributes=attributes,
                )
            )

            attachment_files.append(
                oa_types.File(
                    io.BytesIO(work_item_attachment.content_bytes),
                    work_item_attachment.file_name,
                    work_item_attachment.mime_type,
                )
            )

        multipart = api_models.PostWorkItemAttachmentsRequestBody(
            resource=api_models.WorkitemAttachmentsListPostRequest(
                attachment_attributes
            ),
            files=attachment_files,
        )

        response = post_work_item_attachments.sync_detailed(
            self.project_id,
            work_item_attachments[0].work_item_id,
            client=self.client,
            body=multipart,
        )
        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.create_work_item_attachments(work_item_attachments, False)
            return

        assert (
            isinstance(
                response.parsed, api_models.WorkitemAttachmentsListPostResponse
            )
            and response.parsed.data
        )
        counter = 0
        for work_item_attachment_res in response.parsed.data:
            assert work_item_attachment_res.id
            work_item_attachments[counter].id = (
                work_item_attachment_res.id.split("/")[-1]
            )
            counter += 1

    def get_work_items(
        self,
        query: str = "",
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[base_client.WorkItemType], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self.default_fields.workitems

        sparse_fields = _build_sparse_fields(fields)
        response = get_work_items.sync_detailed(
            self.project_id,
            client=self.client,
            fields=sparse_fields,
            query=query,
            pagesize=page_size,
            pagenumber=page_number,
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_work_items(
                query, fields, page_size, page_number, False
            )

        work_items_response = response.parsed

        work_items: list[base_client.WorkItemType] = []

        next_page = False
        if (
            isinstance(
                work_items_response, api_models.WorkitemsListGetResponse
            )
            and work_items_response.data
        ):
            work_items = [
                self._generate_work_item(work_item)
                for work_item in work_items_response.data
                if not getattr(work_item.meta, "errors", [])
            ]

            next_page = isinstance(
                work_items_response.links,
                api_models.WorkitemsListGetResponseLinks,
            ) and bool(work_items_response.links.next_)

        return work_items, next_page

    def get_work_item(
        self,
        work_item_id: str,
        retry: bool = True,
    ) -> base_client.WorkItemType | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True.
        """
        response = get_work_item.sync_detailed(
            self.project_id,
            work_item_id,
            client=self.client,
            fields=_build_sparse_fields(
                {
                    "workitems": "@all",
                    "workitem_attachments": "@all",
                    "linkedworkitems": "@all",
                }
            ),
        )
        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_work_item(work_item_id, False)

        if isinstance(
            response.parsed, api_models.WorkitemsSingleGetResponse
        ) and isinstance(
            response.parsed.data, api_models.WorkitemsSingleGetResponseData
        ):
            return self._generate_work_item(response.parsed.data)

        return None

    def _generate_work_item(
        self,
        work_item: (
            api_models.WorkitemsListGetResponseDataItem
            | api_models.WorkitemsSingleGetResponseData
        ),
    ) -> base_client.WorkItemType:
        assert work_item.attributes
        assert isinstance(work_item.id, str)
        work_item_id = work_item.id.split("/")[-1]
        work_item_links = []
        work_item_attachments = []

        # We set both truncated flags to True and will only set them to False,
        # if the corresponding fields were requested and returned completely
        links_truncated = True
        attachments_truncated = True
        if work_item.relationships:
            if links := work_item.relationships.linked_work_items:
                if not links.meta or links.meta.total_count is oa_types.UNSET:
                    links_truncated = False

                work_item_links = [
                    self._parse_work_item_link(
                        link.id,
                        link.additional_properties.get("suspect", False),
                        work_item_id,
                    )
                    for link in links.data or []
                ]

            if attachments := work_item.relationships.attachments:
                if (
                    not attachments.meta
                    or attachments.meta.total_count is oa_types.UNSET
                ):
                    attachments_truncated = False

                work_item_attachments = [
                    dm.WorkItemAttachment(
                        work_item_id,
                        attachment.id.split("/")[-1],
                        None,  # title isn't provided
                    )
                    for attachment in attachments.data or []
                    if attachment.id
                ]

        desctype = None
        desc = None
        if work_item.attributes.description:
            desctype = unset_str_builder(work_item.attributes.description.type)
            desc = unset_str_builder(work_item.attributes.description.value)

        work_item_obj = self._work_item(
            work_item_id,
            unset_str_builder(work_item.attributes.title),
            desctype,
            desc,
            unset_str_builder(work_item.attributes.type),
            unset_str_builder(work_item.attributes.status),
            work_item.attributes.additional_properties,
            work_item_links,
            work_item_attachments,
            links_truncated,
            attachments_truncated,
        )
        return work_item_obj

    def get_document(
        self,
        space_id: str,
        document_name: str,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
        retry: bool = True,
    ) -> dm.Document | None:
        """Return the document with the given document_name and space_id."""
        if include is None:
            include = oa_types.UNSET

        if revision is None:
            revision = oa_types.UNSET

        if " " in space_id or " " in document_name:
            space_id = urllib.parse.quote(
                space_id, safe="/", encoding=None, errors=None
            )
            document_name = urllib.parse.quote(
                document_name, safe="/", encoding=None, errors=None
            )
        if fields is None:
            fields = self.default_fields.documents

        sparse_fields = _build_sparse_fields(fields)
        response = get_document.sync_detailed(
            self.project_id,
            space_id,
            document_name,
            client=self.client,
            fields=sparse_fields,
            include=include,
            revision=revision,
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_document(
                space_id, document_name, fields, include, revision, False
            )

        document_response = response.parsed

        if isinstance(
            document_response, api_models.DocumentsSingleGetResponse
        ) and (data := document_response.data):
            if not getattr(data.meta, "errors", []):
                assert (attributes := data.attributes)
                assert isinstance(data.id, str)
                home_page_content = self._handle_text_content(
                    attributes.home_page_content
                )

                return dm.Document(
                    id=data.id,
                    module_folder=unset_str_builder(attributes.module_folder),
                    module_name=unset_str_builder(attributes.module_name),
                    type=unset_str_builder(attributes.type),
                    status=unset_str_builder(attributes.status),
                    home_page_content=home_page_content,
                )
        return None

    def _handle_text_content(
        self,
        polarion_content: api_models.DocumentsSingleGetResponseDataAttributesHomePageContent  # pylint: disable=line-too-long
        | api_models.TestrecordsListGetResponseDataItemAttributesComment
        | api_models.TestrunsListGetResponseDataItemAttributesHomePageContent
        | oa_types.Unset,
    ) -> dm.TextContent | None:
        if not polarion_content:
            return None

        return dm.TextContent(
            type=str(polarion_content.type) if polarion_content.type else None,
            value=polarion_content.value or None,
        )

    def create_work_items(self, work_items: list[base_client.WorkItemType]):
        """Create the given list of work items."""
        current_batch = api_models.WorkitemsListPostRequest(data=[])
        content_size = min_wi_request_size
        batch_start_index = 0
        batch_end_index = 0

        for work_item in work_items:
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
                proj_content_size >= self._max_content_size
                or len(current_batch.data) >= self._batch_size
            ):
                self._post_work_item_batch(
                    current_batch,
                    work_items[batch_start_index:batch_end_index],
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
            self._post_work_item_batch(
                current_batch, work_items[batch_start_index:]
            )

    def _delete_work_items(self, work_item_ids: list[str], retry: bool = True):
        response = delete_work_items.sync_detailed(
            self.project_id,
            client=self.client,
            body=api_models.WorkitemsListDeleteRequest(
                data=[
                    api_models.WorkitemsListDeleteRequestDataItem(
                        type=api_models.WorkitemsListDeleteRequestDataItemType.WORKITEMS,  # pylint: disable=line-too-long
                        id=f"{self.project_id}/{work_item_id}",
                    )
                    for work_item_id in work_item_ids
                ]
            ),
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self._delete_work_items(work_item_ids, False)

    def update_work_item(
        self, work_item: base_client.WorkItemType, retry: bool = True
    ):
        """Update the given work item in Polarion.

        Only fields not set to None will be updated in Polarion. None
        fields will stay untouched.
        """
        assert work_item.id is not None
        if work_item.type:
            logger.warning(
                "Attempting to change the type of Work Item %s to %s.",
                work_item.id,
                work_item.type,
            )

        response = patch_work_item.sync_detailed(
            self.project_id,
            work_item.id,
            client=self.client,
            change_type_to=work_item.type or oa_types.UNSET,
            body=self._build_work_item_patch_request(work_item),
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.update_work_item(work_item, False)

    def get_work_item_links(
        self,
        work_item_id: str,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self.default_fields.linkedworkitems

        if include is None:
            include = oa_types.UNSET

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

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_work_item_links(
                work_item_id, fields, include, page_size, page_number, False
            )

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

    def _create_work_item_links(
        self, work_item_links: list[dm.WorkItemLink], retry: bool = True
    ):
        response = post_linked_work_items.sync_detailed(
            self.project_id,
            work_item_links[0].primary_work_item_id,
            client=self.client,
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
                                    id=f"{work_item_link.secondary_work_item_project}/{work_item_link.secondary_work_item_id}",
                                )
                            )
                        ),
                    )
                    for work_item_link in work_item_links
                ]
            ),
            # pylint: enable=line-too-long
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self._create_work_item_links(work_item_links, False)

    def _delete_work_item_links(
        self, work_item_links: list[dm.WorkItemLink], retry: bool = True
    ):
        response = delete_linked_work_items.sync_detailed(
            self.project_id,
            work_item_links[0].primary_work_item_id,
            client=self.client,
            # pylint: disable=line-too-long
            body=api_models.LinkedworkitemsListDeleteRequest(
                data=[
                    api_models.LinkedworkitemsListDeleteRequestDataItem(
                        type=api_models.LinkedworkitemsListDeleteRequestDataItemType.LINKEDWORKITEMS,
                        id=f"{self.project_id}/{work_item_link.primary_work_item_id}/{work_item_link.role}/{work_item_link.secondary_work_item_project}/{work_item_link.secondary_work_item_id}",
                    )
                    for work_item_link in work_item_links
                ]
            ),
            # pylint: enable=line-too-long
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self._delete_work_item_links(work_item_links, False)

    def get_test_records(
        self,
        test_run_id: str,
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[dm.TestRecord], bool]:
        """Return the test records on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self.default_fields.testrecords

        sparse_fields = _build_sparse_fields(fields)
        response = get_test_records.sync_detailed(
            self.project_id,
            test_run_id,
            client=self.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_test_records(
                test_run_id, fields, page_size, page_number, False
            )

        parsed_response = response.parsed
        assert parsed_response

        test_records = []
        for data in parsed_response.data or []:
            assert isinstance(data.id, str)
            assert isinstance(
                data.attributes,
                api_models.TestrecordsListGetResponseDataItemAttributes,
            )
            _, _, project_id, work_item, iteration = data.id.split("/")
            test_records.append(
                dm.TestRecord(
                    project_id,
                    work_item,
                    data.attributes.test_case_revision or None,
                    int(iteration),
                    data.attributes.duration or -1,
                    data.attributes.result or None,
                    self._handle_text_content(data.attributes.comment),
                    data.additional_properties or {},
                )
            )
        next_page = isinstance(
            parsed_response.links,
            api_models.TestrecordsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)

        return test_records, next_page

    def get_test_runs(
        self,
        query: str,
        fields: dict[str, str] | None = None,
        page_size: int = 100,
        page_number: int = 1,
        retry: bool = True,
    ) -> tuple[list[dm.TestRun], bool]:
        """Return the test runs on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self.default_fields.testruns

        sparse_fields = _build_sparse_fields(fields)
        response = get_test_runs.sync_detailed(
            self.project_id,
            client=self.client,
            query=query,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            return self.get_test_runs(
                query, fields, page_size, page_number, False
            )

        parsed_response = response.parsed
        assert parsed_response

        test_runs = []
        for data in parsed_response.data or []:
            assert isinstance(data.id, str)
            assert isinstance(
                data.attributes,
                api_models.TestrunsListGetResponseDataItemAttributes,
            )
            test_runs.append(
                dm.TestRun(
                    data.id.split("/")[-1],
                    data.attributes.type or None,
                    data.attributes.status or None,
                    data.attributes.title or None,
                    self._handle_text_content(
                        data.attributes.home_page_content
                    ),
                    dm.SelectTestCasesBy(
                        str(data.attributes.select_test_cases_by)
                    )
                    if data.attributes.select_test_cases_by
                    else None,
                    data.attributes.additional_properties or {},
                )
            )
        next_page = isinstance(
            parsed_response.links,
            api_models.TestrunsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)

        return test_runs, next_page

    def create_test_runs(
        self, test_runs: list[dm.TestRun], retry: bool = True
    ):
        """Create the given list of test runs."""
        polarion_test_runs = [
            api_models.TestrunsListPostRequestDataItem(
                api_models.TestrunsListPostRequestDataItemType.TESTRUNS,
                self._fill_test_run_attributes(
                    api_models.TestrunsListPostRequestDataItemAttributes,
                    test_run,
                ),
            )
            for test_run in test_runs
        ]

        response = post_test_runs.sync_detailed(
            self.project_id,
            client=self.client,
            body=api_models.TestrunsListPostRequest(polarion_test_runs),
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.create_test_runs(test_runs, False)

    def update_test_run(self, test_run: dm.TestRun, retry: bool = True):
        """Create the given list of test runs."""
        assert test_run.id
        response = patch_test_run.sync_detailed(
            self.project_id,
            test_run.id,
            client=self.client,
            body=api_models.TestrunsSinglePatchRequest(
                api_models.TestrunsSinglePatchRequestData(
                    api_models.TestrunsSinglePatchRequestDataType.TESTRUNS,
                    f"{self.project_id}/{test_run.id}",
                    self._fill_test_run_attributes(
                        api_models.TestrunsSinglePatchRequestDataAttributes,
                        test_run,
                    ),
                )
            ),
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.update_test_run(test_run, False)

    def _fill_test_run_attributes(
        self,
        attributes_type: type[
            api_models.TestrunsListPostRequestDataItemAttributes
            | api_models.TestrunsSinglePatchRequestDataAttributes
        ],
        test_run: dm.TestRun,
    ):
        type_prefix = attributes_type.__name__
        attributes = attributes_type()
        if test_run.type:
            attributes.type = test_run.type
        if test_run.id and hasattr(attributes, "id"):
            attributes.id = test_run.id
        if test_run.status:
            attributes.status = test_run.status
        if test_run.title:
            attributes.title = test_run.title
        if test_run.additional_attributes:
            attributes.additional_properties = test_run.additional_attributes
        if test_run.select_test_cases_by:
            attributes.select_test_cases_by = getattr(
                api_models, f"{type_prefix}SelectTestCasesBy"
            )(str(test_run.select_test_cases_by))
        if test_run.home_page_content:
            attributes.home_page_content = getattr(
                api_models, f"{type_prefix}HomePageContent"
            )()
            assert attributes.home_page_content
            if test_run.home_page_content.type:
                attributes.home_page_content.type = getattr(
                    api_models, f"{type_prefix}HomePageContentType"
                )(test_run.home_page_content.type)
            if test_run.home_page_content.value:
                attributes.home_page_content.value = (
                    test_run.home_page_content.value
                )

        return attributes

    def _fill_test_record_attributes(
        self,
        attributes_type: type[
            api_models.TestrecordsListPostRequestDataItemAttributes
            | api_models.TestrecordsSinglePatchRequestDataAttributes
        ],
        test_record: dm.TestRecord,
    ):
        type_prefix = attributes_type.__name__
        attributes = attributes_type()
        if test_record.result:
            attributes.result = test_record.result
        if test_record.comment:
            attributes.comment = getattr(api_models, f"{type_prefix}Comment")()
            assert attributes.comment
            if test_record.comment.type:
                attributes.comment.type = getattr(
                    api_models, f"{type_prefix}CommentType"
                )(test_record.comment.type)
            if test_record.comment.value:
                attributes.comment.value = test_record.comment.value
        if test_record.duration:
            attributes.duration = test_record.duration
        if test_record.work_item_revision:
            attributes.test_case_revision = test_record.work_item_revision
        if test_record.additional_attributes:
            attributes.additional_properties = (
                test_record.additional_attributes
            )
        return attributes

    def create_test_records(
        self,
        test_run_id: str,
        test_records: list[dm.TestRecord],
        retry: bool = True,
    ):
        """Create the given list of test records."""
        response = post_test_records.sync_detailed(
            self.project_id,
            test_run_id,
            client=self.client,
            body=api_models.TestrecordsListPostRequest(
                [
                    api_models.TestrecordsListPostRequestDataItem(
                        api_models.TestrecordsListPostRequestDataItemType.TESTRECORDS,
                        self._fill_test_record_attributes(
                            api_models.TestrecordsListPostRequestDataItemAttributes,
                            test_record,
                        ),
                        api_models.TestrecordsListPostRequestDataItemRelationships(
                            test_case=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCase(
                                api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseData(
                                    api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseDataType.WORKITEMS,
                                    f"{test_record.work_item_project_id}/{test_record.work_item_id}",
                                )
                            )
                        ),
                    )
                    for test_record in test_records
                ]
            ),
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.create_test_records(test_run_id, test_records, False)

    def update_test_record(
        self, test_run_id: str, test_record: dm.TestRecord, retry: bool = True
    ):
        """Create the given list of test records."""
        response = patch_test_record.sync_detailed(
            self.project_id,
            test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            client=self.client,
            body=api_models.TestrecordsSinglePatchRequest(
                api_models.TestrecordsSinglePatchRequestData(
                    api_models.TestrecordsSinglePatchRequestDataType.TESTRECORDS,
                    f"{self.project_id}/{test_run_id}/{test_record.work_item_project_id}/{test_record.work_item_id}/{test_record.iteration}",
                    self._fill_test_record_attributes(
                        api_models.TestrecordsSinglePatchRequestDataAttributes,
                        test_record,
                    ),
                )
            ),
        )

        if not self._check_response(response, not retry) and retry:
            sleep_random_time()
            self.update_test_record(test_run_id, test_record, False)
