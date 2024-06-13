# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementations of WorkItemAttachment relates functions."""
import io
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.work_item_attachments import (  # pylint: disable=line-too-long
    delete_work_item_attachment,
    get_work_item_attachments,
    patch_work_item_attachment,
    post_work_item_attachments,
)

from . import base_classes as bc


class WorkItemAttachments(bc.UpdatableItemsClient[dm.WorkItemAttachment]):
    """A class to handle WorkItemAttachments."""

    def _get(self, *args, **kwargs) -> dm.WorkItemAttachment:
        raise NotImplementedError

    def _update(self, items: list[dm.WorkItemAttachment]):
        for work_item_attachment in items:
            self._retry_on_error(self._update_single, work_item_attachment)

    def _update_single(self, work_item_attachment: dm.WorkItemAttachment):
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
                    id=f"{self._project_id}/{work_item_attachment.work_item_id}/{work_item_attachment.id}",  # pylint: disable=line-too-long
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
            self._project_id,
            work_item_attachment.work_item_id,
            work_item_attachment.id,
            client=self._client.client,
            body=multipart,
        )
        self._raise_on_error(response)

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: t.Optional[dict[str, str]] = None,
    ) -> tuple[list[dm.WorkItemAttachment], bool]:
        """Return the attachments for a given work item on a defined page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        return super().get_multi(
            work_item_id,
            page_size=page_size,
            page_number=page_number,
            fields=fields,
        )

    def _get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: t.Optional[dict[str, str]] = None,
    ) -> tuple[list[dm.WorkItemAttachment], bool]:
        if fields is None:
            fields = self._client.default_fields.workitem_attachments

        sparse_fields = self._build_sparse_fields(fields)
        response = get_work_item_attachments.sync_detailed(
            self._project_id,
            work_item_id=work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            pagesize=page_size,
            pagenumber=page_number,
        )

        self._raise_on_error(response)

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
                        self.unset_to_none(attachment.attributes.title),
                        file_name=self.unset_to_none(
                            attachment.attributes.file_name
                        ),
                    )
                )

            next_page = isinstance(
                parsed_response.links,
                api_models.WorkitemAttachmentsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)

        return work_item_attachments, next_page

    def _create(self, work_item_attachments: list[dm.WorkItemAttachment]):
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

            attributes = api_models.WorkitemAttachmentsListPostRequestDataItemAttributes(
                # pylint: disable=line-too-long
                file_name=work_item_attachment.file_name
            )
            if work_item_attachment.title:
                attributes.title = work_item_attachment.title

            attachment_attributes.append(
                api_models.WorkitemAttachmentsListPostRequestDataItem(
                    type=api_models.WorkitemAttachmentsListPostRequestDataItemType.WORKITEM_ATTACHMENTS,
                    # pylint: disable=line-too-long
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
            self._project_id,
            work_item_attachments[0].work_item_id,
            client=self._client.client,
            body=multipart,
        )

        self._raise_on_error(response)
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

    def _delete(self, items: list[dm.WorkItemAttachment]):
        for item in items:
            self._retry_on_error(self._single_delete, item)

    def _single_delete(self, work_item_attachment: dm.WorkItemAttachment):
        """Delete the given work item attachment."""
        response = delete_work_item_attachment.sync_detailed(
            self._project_id,
            work_item_attachment.work_item_id,
            work_item_attachment.id,
            client=self._client.client,
        )
        self._raise_on_error(response)
