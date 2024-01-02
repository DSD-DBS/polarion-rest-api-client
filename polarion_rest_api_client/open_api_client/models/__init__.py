# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Contains all the data models used in inputs/outputs."""

from .branch_document_request_body import BranchDocumentRequestBody
from .copy_document_request_body import CopyDocumentRequestBody
from .document_attachments_list_get_response import (
    DocumentAttachmentsListGetResponse,
)
from .document_attachments_list_get_response_data_item import (
    DocumentAttachmentsListGetResponseDataItem,
)
from .document_attachments_list_get_response_data_item_attributes import (
    DocumentAttachmentsListGetResponseDataItemAttributes,
)
from .document_attachments_list_get_response_data_item_links import (
    DocumentAttachmentsListGetResponseDataItemLinks,
)
from .document_attachments_list_get_response_data_item_meta import (
    DocumentAttachmentsListGetResponseDataItemMeta,
)
from .document_attachments_list_get_response_data_item_meta_errors_item import (
    DocumentAttachmentsListGetResponseDataItemMetaErrorsItem,
)
from .document_attachments_list_get_response_data_item_meta_errors_item_source import (
    DocumentAttachmentsListGetResponseDataItemMetaErrorsItemSource,
)
from .document_attachments_list_get_response_data_item_relationships import (
    DocumentAttachmentsListGetResponseDataItemRelationships,
)
from .document_attachments_list_get_response_data_item_relationships_author import (
    DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor,
)
from .document_attachments_list_get_response_data_item_relationships_author_data import (
    DocumentAttachmentsListGetResponseDataItemRelationshipsAuthorData,
)
from .document_attachments_list_get_response_data_item_relationships_author_data_type import (
    DocumentAttachmentsListGetResponseDataItemRelationshipsAuthorDataType,
)
from .document_attachments_list_get_response_data_item_relationships_project import (
    DocumentAttachmentsListGetResponseDataItemRelationshipsProject,
)
from .document_attachments_list_get_response_data_item_relationships_project_data import (
    DocumentAttachmentsListGetResponseDataItemRelationshipsProjectData,
)
from .document_attachments_list_get_response_data_item_relationships_project_data_type import (
    DocumentAttachmentsListGetResponseDataItemRelationshipsProjectDataType,
)
from .document_attachments_list_get_response_data_item_type import (
    DocumentAttachmentsListGetResponseDataItemType,
)
from .document_attachments_list_get_response_included_item import (
    DocumentAttachmentsListGetResponseIncludedItem,
)
from .document_attachments_list_get_response_links import (
    DocumentAttachmentsListGetResponseLinks,
)
from .document_attachments_list_get_response_meta import (
    DocumentAttachmentsListGetResponseMeta,
)
from .document_attachments_list_post_request import (
    DocumentAttachmentsListPostRequest,
)
from .document_attachments_list_post_request_data_item import (
    DocumentAttachmentsListPostRequestDataItem,
)
from .document_attachments_list_post_request_data_item_attributes import (
    DocumentAttachmentsListPostRequestDataItemAttributes,
)
from .document_attachments_list_post_request_data_item_type import (
    DocumentAttachmentsListPostRequestDataItemType,
)
from .document_attachments_list_post_response import (
    DocumentAttachmentsListPostResponse,
)
from .document_attachments_list_post_response_data_item import (
    DocumentAttachmentsListPostResponseDataItem,
)
from .document_attachments_list_post_response_data_item_links import (
    DocumentAttachmentsListPostResponseDataItemLinks,
)
from .document_attachments_list_post_response_data_item_type import (
    DocumentAttachmentsListPostResponseDataItemType,
)
from .document_attachments_single_get_response import (
    DocumentAttachmentsSingleGetResponse,
)
from .document_attachments_single_get_response_data import (
    DocumentAttachmentsSingleGetResponseData,
)
from .document_attachments_single_get_response_data_attributes import (
    DocumentAttachmentsSingleGetResponseDataAttributes,
)
from .document_attachments_single_get_response_data_links import (
    DocumentAttachmentsSingleGetResponseDataLinks,
)
from .document_attachments_single_get_response_data_meta import (
    DocumentAttachmentsSingleGetResponseDataMeta,
)
from .document_attachments_single_get_response_data_meta_errors_item import (
    DocumentAttachmentsSingleGetResponseDataMetaErrorsItem,
)
from .document_attachments_single_get_response_data_meta_errors_item_source import (
    DocumentAttachmentsSingleGetResponseDataMetaErrorsItemSource,
)
from .document_attachments_single_get_response_data_relationships import (
    DocumentAttachmentsSingleGetResponseDataRelationships,
)
from .document_attachments_single_get_response_data_relationships_author import (
    DocumentAttachmentsSingleGetResponseDataRelationshipsAuthor,
)
from .document_attachments_single_get_response_data_relationships_author_data import (
    DocumentAttachmentsSingleGetResponseDataRelationshipsAuthorData,
)
from .document_attachments_single_get_response_data_relationships_author_data_type import (
    DocumentAttachmentsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .document_attachments_single_get_response_data_relationships_project import (
    DocumentAttachmentsSingleGetResponseDataRelationshipsProject,
)
from .document_attachments_single_get_response_data_relationships_project_data import (
    DocumentAttachmentsSingleGetResponseDataRelationshipsProjectData,
)
from .document_attachments_single_get_response_data_relationships_project_data_type import (
    DocumentAttachmentsSingleGetResponseDataRelationshipsProjectDataType,
)
from .document_attachments_single_get_response_data_type import (
    DocumentAttachmentsSingleGetResponseDataType,
)
from .document_attachments_single_get_response_included_item import (
    DocumentAttachmentsSingleGetResponseIncludedItem,
)
from .document_attachments_single_get_response_links import (
    DocumentAttachmentsSingleGetResponseLinks,
)
from .document_attachments_single_patch_request import (
    DocumentAttachmentsSinglePatchRequest,
)
from .document_attachments_single_patch_request_data import (
    DocumentAttachmentsSinglePatchRequestData,
)
from .document_attachments_single_patch_request_data_attributes import (
    DocumentAttachmentsSinglePatchRequestDataAttributes,
)
from .document_attachments_single_patch_request_data_type import (
    DocumentAttachmentsSinglePatchRequestDataType,
)
from .document_comments_list_get_response import (
    DocumentCommentsListGetResponse,
)
from .document_comments_list_get_response_data_item import (
    DocumentCommentsListGetResponseDataItem,
)
from .document_comments_list_get_response_data_item_attributes import (
    DocumentCommentsListGetResponseDataItemAttributes,
)
from .document_comments_list_get_response_data_item_attributes_text import (
    DocumentCommentsListGetResponseDataItemAttributesText,
)
from .document_comments_list_get_response_data_item_attributes_text_type import (
    DocumentCommentsListGetResponseDataItemAttributesTextType,
)
from .document_comments_list_get_response_data_item_links import (
    DocumentCommentsListGetResponseDataItemLinks,
)
from .document_comments_list_get_response_data_item_meta import (
    DocumentCommentsListGetResponseDataItemMeta,
)
from .document_comments_list_get_response_data_item_meta_errors_item import (
    DocumentCommentsListGetResponseDataItemMetaErrorsItem,
)
from .document_comments_list_get_response_data_item_meta_errors_item_source import (
    DocumentCommentsListGetResponseDataItemMetaErrorsItemSource,
)
from .document_comments_list_get_response_data_item_relationships import (
    DocumentCommentsListGetResponseDataItemRelationships,
)
from .document_comments_list_get_response_data_item_relationships_author import (
    DocumentCommentsListGetResponseDataItemRelationshipsAuthor,
)
from .document_comments_list_get_response_data_item_relationships_author_data import (
    DocumentCommentsListGetResponseDataItemRelationshipsAuthorData,
)
from .document_comments_list_get_response_data_item_relationships_author_data_type import (
    DocumentCommentsListGetResponseDataItemRelationshipsAuthorDataType,
)
from .document_comments_list_get_response_data_item_relationships_child_comments import (
    DocumentCommentsListGetResponseDataItemRelationshipsChildComments,
)
from .document_comments_list_get_response_data_item_relationships_child_comments_data_item import (
    DocumentCommentsListGetResponseDataItemRelationshipsChildCommentsDataItem,
)
from .document_comments_list_get_response_data_item_relationships_child_comments_data_item_type import (
    DocumentCommentsListGetResponseDataItemRelationshipsChildCommentsDataItemType,
)
from .document_comments_list_get_response_data_item_relationships_child_comments_meta import (
    DocumentCommentsListGetResponseDataItemRelationshipsChildCommentsMeta,
)
from .document_comments_list_get_response_data_item_relationships_parent_comment import (
    DocumentCommentsListGetResponseDataItemRelationshipsParentComment,
)
from .document_comments_list_get_response_data_item_relationships_parent_comment_data import (
    DocumentCommentsListGetResponseDataItemRelationshipsParentCommentData,
)
from .document_comments_list_get_response_data_item_relationships_parent_comment_data_type import (
    DocumentCommentsListGetResponseDataItemRelationshipsParentCommentDataType,
)
from .document_comments_list_get_response_data_item_relationships_project import (
    DocumentCommentsListGetResponseDataItemRelationshipsProject,
)
from .document_comments_list_get_response_data_item_relationships_project_data import (
    DocumentCommentsListGetResponseDataItemRelationshipsProjectData,
)
from .document_comments_list_get_response_data_item_relationships_project_data_type import (
    DocumentCommentsListGetResponseDataItemRelationshipsProjectDataType,
)
from .document_comments_list_get_response_data_item_type import (
    DocumentCommentsListGetResponseDataItemType,
)
from .document_comments_list_get_response_included_item import (
    DocumentCommentsListGetResponseIncludedItem,
)
from .document_comments_list_get_response_links import (
    DocumentCommentsListGetResponseLinks,
)
from .document_comments_list_get_response_meta import (
    DocumentCommentsListGetResponseMeta,
)
from .document_comments_list_post_request import (
    DocumentCommentsListPostRequest,
)
from .document_comments_list_post_request_data_item import (
    DocumentCommentsListPostRequestDataItem,
)
from .document_comments_list_post_request_data_item_attributes import (
    DocumentCommentsListPostRequestDataItemAttributes,
)
from .document_comments_list_post_request_data_item_attributes_text import (
    DocumentCommentsListPostRequestDataItemAttributesText,
)
from .document_comments_list_post_request_data_item_attributes_text_type import (
    DocumentCommentsListPostRequestDataItemAttributesTextType,
)
from .document_comments_list_post_request_data_item_relationships import (
    DocumentCommentsListPostRequestDataItemRelationships,
)
from .document_comments_list_post_request_data_item_relationships_author import (
    DocumentCommentsListPostRequestDataItemRelationshipsAuthor,
)
from .document_comments_list_post_request_data_item_relationships_author_data import (
    DocumentCommentsListPostRequestDataItemRelationshipsAuthorData,
)
from .document_comments_list_post_request_data_item_relationships_author_data_type import (
    DocumentCommentsListPostRequestDataItemRelationshipsAuthorDataType,
)
from .document_comments_list_post_request_data_item_relationships_parent_comment import (
    DocumentCommentsListPostRequestDataItemRelationshipsParentComment,
)
from .document_comments_list_post_request_data_item_relationships_parent_comment_data import (
    DocumentCommentsListPostRequestDataItemRelationshipsParentCommentData,
)
from .document_comments_list_post_request_data_item_relationships_parent_comment_data_type import (
    DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
)
from .document_comments_list_post_request_data_item_type import (
    DocumentCommentsListPostRequestDataItemType,
)
from .document_comments_list_post_response import (
    DocumentCommentsListPostResponse,
)
from .document_comments_list_post_response_data_item import (
    DocumentCommentsListPostResponseDataItem,
)
from .document_comments_list_post_response_data_item_links import (
    DocumentCommentsListPostResponseDataItemLinks,
)
from .document_comments_list_post_response_data_item_type import (
    DocumentCommentsListPostResponseDataItemType,
)
from .document_comments_single_get_response import (
    DocumentCommentsSingleGetResponse,
)
from .document_comments_single_get_response_data import (
    DocumentCommentsSingleGetResponseData,
)
from .document_comments_single_get_response_data_attributes import (
    DocumentCommentsSingleGetResponseDataAttributes,
)
from .document_comments_single_get_response_data_attributes_text import (
    DocumentCommentsSingleGetResponseDataAttributesText,
)
from .document_comments_single_get_response_data_attributes_text_type import (
    DocumentCommentsSingleGetResponseDataAttributesTextType,
)
from .document_comments_single_get_response_data_links import (
    DocumentCommentsSingleGetResponseDataLinks,
)
from .document_comments_single_get_response_data_meta import (
    DocumentCommentsSingleGetResponseDataMeta,
)
from .document_comments_single_get_response_data_meta_errors_item import (
    DocumentCommentsSingleGetResponseDataMetaErrorsItem,
)
from .document_comments_single_get_response_data_meta_errors_item_source import (
    DocumentCommentsSingleGetResponseDataMetaErrorsItemSource,
)
from .document_comments_single_get_response_data_relationships import (
    DocumentCommentsSingleGetResponseDataRelationships,
)
from .document_comments_single_get_response_data_relationships_author import (
    DocumentCommentsSingleGetResponseDataRelationshipsAuthor,
)
from .document_comments_single_get_response_data_relationships_author_data import (
    DocumentCommentsSingleGetResponseDataRelationshipsAuthorData,
)
from .document_comments_single_get_response_data_relationships_author_data_type import (
    DocumentCommentsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .document_comments_single_get_response_data_relationships_child_comments import (
    DocumentCommentsSingleGetResponseDataRelationshipsChildComments,
)
from .document_comments_single_get_response_data_relationships_child_comments_data_item import (
    DocumentCommentsSingleGetResponseDataRelationshipsChildCommentsDataItem,
)
from .document_comments_single_get_response_data_relationships_child_comments_data_item_type import (
    DocumentCommentsSingleGetResponseDataRelationshipsChildCommentsDataItemType,
)
from .document_comments_single_get_response_data_relationships_child_comments_meta import (
    DocumentCommentsSingleGetResponseDataRelationshipsChildCommentsMeta,
)
from .document_comments_single_get_response_data_relationships_parent_comment import (
    DocumentCommentsSingleGetResponseDataRelationshipsParentComment,
)
from .document_comments_single_get_response_data_relationships_parent_comment_data import (
    DocumentCommentsSingleGetResponseDataRelationshipsParentCommentData,
)
from .document_comments_single_get_response_data_relationships_parent_comment_data_type import (
    DocumentCommentsSingleGetResponseDataRelationshipsParentCommentDataType,
)
from .document_comments_single_get_response_data_relationships_project import (
    DocumentCommentsSingleGetResponseDataRelationshipsProject,
)
from .document_comments_single_get_response_data_relationships_project_data import (
    DocumentCommentsSingleGetResponseDataRelationshipsProjectData,
)
from .document_comments_single_get_response_data_relationships_project_data_type import (
    DocumentCommentsSingleGetResponseDataRelationshipsProjectDataType,
)
from .document_comments_single_get_response_data_type import (
    DocumentCommentsSingleGetResponseDataType,
)
from .document_comments_single_get_response_included_item import (
    DocumentCommentsSingleGetResponseIncludedItem,
)
from .document_comments_single_get_response_links import (
    DocumentCommentsSingleGetResponseLinks,
)
from .document_comments_single_patch_request import (
    DocumentCommentsSinglePatchRequest,
)
from .document_comments_single_patch_request_data import (
    DocumentCommentsSinglePatchRequestData,
)
from .document_comments_single_patch_request_data_attributes import (
    DocumentCommentsSinglePatchRequestDataAttributes,
)
from .document_comments_single_patch_request_data_type import (
    DocumentCommentsSinglePatchRequestDataType,
)
from .document_parts_list_get_response import DocumentPartsListGetResponse
from .document_parts_list_get_response_data_item import (
    DocumentPartsListGetResponseDataItem,
)
from .document_parts_list_get_response_data_item_attributes import (
    DocumentPartsListGetResponseDataItemAttributes,
)
from .document_parts_list_get_response_data_item_links import (
    DocumentPartsListGetResponseDataItemLinks,
)
from .document_parts_list_get_response_data_item_meta import (
    DocumentPartsListGetResponseDataItemMeta,
)
from .document_parts_list_get_response_data_item_meta_errors_item import (
    DocumentPartsListGetResponseDataItemMetaErrorsItem,
)
from .document_parts_list_get_response_data_item_meta_errors_item_source import (
    DocumentPartsListGetResponseDataItemMetaErrorsItemSource,
)
from .document_parts_list_get_response_data_item_relationships import (
    DocumentPartsListGetResponseDataItemRelationships,
)
from .document_parts_list_get_response_data_item_relationships_next_part import (
    DocumentPartsListGetResponseDataItemRelationshipsNextPart,
)
from .document_parts_list_get_response_data_item_relationships_next_part_data import (
    DocumentPartsListGetResponseDataItemRelationshipsNextPartData,
)
from .document_parts_list_get_response_data_item_relationships_next_part_data_type import (
    DocumentPartsListGetResponseDataItemRelationshipsNextPartDataType,
)
from .document_parts_list_get_response_data_item_relationships_previous_part import (
    DocumentPartsListGetResponseDataItemRelationshipsPreviousPart,
)
from .document_parts_list_get_response_data_item_relationships_previous_part_data import (
    DocumentPartsListGetResponseDataItemRelationshipsPreviousPartData,
)
from .document_parts_list_get_response_data_item_relationships_previous_part_data_type import (
    DocumentPartsListGetResponseDataItemRelationshipsPreviousPartDataType,
)
from .document_parts_list_get_response_data_item_relationships_work_item import (
    DocumentPartsListGetResponseDataItemRelationshipsWorkItem,
)
from .document_parts_list_get_response_data_item_relationships_work_item_data import (
    DocumentPartsListGetResponseDataItemRelationshipsWorkItemData,
)
from .document_parts_list_get_response_data_item_relationships_work_item_data_type import (
    DocumentPartsListGetResponseDataItemRelationshipsWorkItemDataType,
)
from .document_parts_list_get_response_data_item_type import (
    DocumentPartsListGetResponseDataItemType,
)
from .document_parts_list_get_response_included_item import (
    DocumentPartsListGetResponseIncludedItem,
)
from .document_parts_list_get_response_links import (
    DocumentPartsListGetResponseLinks,
)
from .document_parts_list_get_response_meta import (
    DocumentPartsListGetResponseMeta,
)
from .document_parts_list_post_request import DocumentPartsListPostRequest
from .document_parts_list_post_request_data_item import (
    DocumentPartsListPostRequestDataItem,
)
from .document_parts_list_post_request_data_item_attributes import (
    DocumentPartsListPostRequestDataItemAttributes,
)
from .document_parts_list_post_request_data_item_relationships import (
    DocumentPartsListPostRequestDataItemRelationships,
)
from .document_parts_list_post_request_data_item_relationships_next_part import (
    DocumentPartsListPostRequestDataItemRelationshipsNextPart,
)
from .document_parts_list_post_request_data_item_relationships_next_part_data import (
    DocumentPartsListPostRequestDataItemRelationshipsNextPartData,
)
from .document_parts_list_post_request_data_item_relationships_next_part_data_type import (
    DocumentPartsListPostRequestDataItemRelationshipsNextPartDataType,
)
from .document_parts_list_post_request_data_item_relationships_previous_part import (
    DocumentPartsListPostRequestDataItemRelationshipsPreviousPart,
)
from .document_parts_list_post_request_data_item_relationships_previous_part_data import (
    DocumentPartsListPostRequestDataItemRelationshipsPreviousPartData,
)
from .document_parts_list_post_request_data_item_relationships_previous_part_data_type import (
    DocumentPartsListPostRequestDataItemRelationshipsPreviousPartDataType,
)
from .document_parts_list_post_request_data_item_relationships_work_item import (
    DocumentPartsListPostRequestDataItemRelationshipsWorkItem,
)
from .document_parts_list_post_request_data_item_relationships_work_item_data import (
    DocumentPartsListPostRequestDataItemRelationshipsWorkItemData,
)
from .document_parts_list_post_request_data_item_relationships_work_item_data_type import (
    DocumentPartsListPostRequestDataItemRelationshipsWorkItemDataType,
)
from .document_parts_list_post_request_data_item_type import (
    DocumentPartsListPostRequestDataItemType,
)
from .document_parts_list_post_response import DocumentPartsListPostResponse
from .document_parts_list_post_response_data_item import (
    DocumentPartsListPostResponseDataItem,
)
from .document_parts_list_post_response_data_item_links import (
    DocumentPartsListPostResponseDataItemLinks,
)
from .document_parts_list_post_response_data_item_type import (
    DocumentPartsListPostResponseDataItemType,
)
from .document_parts_single_get_response import DocumentPartsSingleGetResponse
from .document_parts_single_get_response_data import (
    DocumentPartsSingleGetResponseData,
)
from .document_parts_single_get_response_data_attributes import (
    DocumentPartsSingleGetResponseDataAttributes,
)
from .document_parts_single_get_response_data_links import (
    DocumentPartsSingleGetResponseDataLinks,
)
from .document_parts_single_get_response_data_meta import (
    DocumentPartsSingleGetResponseDataMeta,
)
from .document_parts_single_get_response_data_meta_errors_item import (
    DocumentPartsSingleGetResponseDataMetaErrorsItem,
)
from .document_parts_single_get_response_data_meta_errors_item_source import (
    DocumentPartsSingleGetResponseDataMetaErrorsItemSource,
)
from .document_parts_single_get_response_data_relationships import (
    DocumentPartsSingleGetResponseDataRelationships,
)
from .document_parts_single_get_response_data_relationships_next_part import (
    DocumentPartsSingleGetResponseDataRelationshipsNextPart,
)
from .document_parts_single_get_response_data_relationships_next_part_data import (
    DocumentPartsSingleGetResponseDataRelationshipsNextPartData,
)
from .document_parts_single_get_response_data_relationships_next_part_data_type import (
    DocumentPartsSingleGetResponseDataRelationshipsNextPartDataType,
)
from .document_parts_single_get_response_data_relationships_previous_part import (
    DocumentPartsSingleGetResponseDataRelationshipsPreviousPart,
)
from .document_parts_single_get_response_data_relationships_previous_part_data import (
    DocumentPartsSingleGetResponseDataRelationshipsPreviousPartData,
)
from .document_parts_single_get_response_data_relationships_previous_part_data_type import (
    DocumentPartsSingleGetResponseDataRelationshipsPreviousPartDataType,
)
from .document_parts_single_get_response_data_relationships_work_item import (
    DocumentPartsSingleGetResponseDataRelationshipsWorkItem,
)
from .document_parts_single_get_response_data_relationships_work_item_data import (
    DocumentPartsSingleGetResponseDataRelationshipsWorkItemData,
)
from .document_parts_single_get_response_data_relationships_work_item_data_type import (
    DocumentPartsSingleGetResponseDataRelationshipsWorkItemDataType,
)
from .document_parts_single_get_response_data_type import (
    DocumentPartsSingleGetResponseDataType,
)
from .document_parts_single_get_response_included_item import (
    DocumentPartsSingleGetResponseIncludedItem,
)
from .document_parts_single_get_response_links import (
    DocumentPartsSingleGetResponseLinks,
)
from .documents_list_post_request import DocumentsListPostRequest
from .documents_list_post_request_data_item import (
    DocumentsListPostRequestDataItem,
)
from .documents_list_post_request_data_item_attributes import (
    DocumentsListPostRequestDataItemAttributes,
)
from .documents_list_post_request_data_item_attributes_home_page_content import (
    DocumentsListPostRequestDataItemAttributesHomePageContent,
)
from .documents_list_post_request_data_item_attributes_home_page_content_type import (
    DocumentsListPostRequestDataItemAttributesHomePageContentType,
)
from .documents_list_post_request_data_item_attributes_outline_numbering import (
    DocumentsListPostRequestDataItemAttributesOutlineNumbering,
)
from .documents_list_post_request_data_item_attributes_rendering_layouts_item import (
    DocumentsListPostRequestDataItemAttributesRenderingLayoutsItem,
)
from .documents_list_post_request_data_item_attributes_rendering_layouts_item_properties_item import (
    DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem,
)
from .documents_list_post_request_data_item_type import (
    DocumentsListPostRequestDataItemType,
)
from .documents_list_post_response import DocumentsListPostResponse
from .documents_list_post_response_data_item import (
    DocumentsListPostResponseDataItem,
)
from .documents_list_post_response_data_item_links import (
    DocumentsListPostResponseDataItemLinks,
)
from .documents_list_post_response_data_item_type import (
    DocumentsListPostResponseDataItemType,
)
from .documents_single_get_response import DocumentsSingleGetResponse
from .documents_single_get_response_data import DocumentsSingleGetResponseData
from .documents_single_get_response_data_attributes import (
    DocumentsSingleGetResponseDataAttributes,
)
from .documents_single_get_response_data_attributes_home_page_content import (
    DocumentsSingleGetResponseDataAttributesHomePageContent,
)
from .documents_single_get_response_data_attributes_home_page_content_type import (
    DocumentsSingleGetResponseDataAttributesHomePageContentType,
)
from .documents_single_get_response_data_attributes_outline_numbering import (
    DocumentsSingleGetResponseDataAttributesOutlineNumbering,
)
from .documents_single_get_response_data_attributes_rendering_layouts_item import (
    DocumentsSingleGetResponseDataAttributesRenderingLayoutsItem,
)
from .documents_single_get_response_data_attributes_rendering_layouts_item_properties_item import (
    DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem,
)
from .documents_single_get_response_data_links import (
    DocumentsSingleGetResponseDataLinks,
)
from .documents_single_get_response_data_meta import (
    DocumentsSingleGetResponseDataMeta,
)
from .documents_single_get_response_data_meta_errors_item import (
    DocumentsSingleGetResponseDataMetaErrorsItem,
)
from .documents_single_get_response_data_meta_errors_item_source import (
    DocumentsSingleGetResponseDataMetaErrorsItemSource,
)
from .documents_single_get_response_data_relationships import (
    DocumentsSingleGetResponseDataRelationships,
)
from .documents_single_get_response_data_relationships_attachments import (
    DocumentsSingleGetResponseDataRelationshipsAttachments,
)
from .documents_single_get_response_data_relationships_attachments_data_item import (
    DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem,
)
from .documents_single_get_response_data_relationships_attachments_data_item_type import (
    DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItemType,
)
from .documents_single_get_response_data_relationships_attachments_links import (
    DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks,
)
from .documents_single_get_response_data_relationships_attachments_meta import (
    DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta,
)
from .documents_single_get_response_data_relationships_author import (
    DocumentsSingleGetResponseDataRelationshipsAuthor,
)
from .documents_single_get_response_data_relationships_author_data import (
    DocumentsSingleGetResponseDataRelationshipsAuthorData,
)
from .documents_single_get_response_data_relationships_author_data_type import (
    DocumentsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .documents_single_get_response_data_relationships_branched_from import (
    DocumentsSingleGetResponseDataRelationshipsBranchedFrom,
)
from .documents_single_get_response_data_relationships_branched_from_data import (
    DocumentsSingleGetResponseDataRelationshipsBranchedFromData,
)
from .documents_single_get_response_data_relationships_branched_from_data_type import (
    DocumentsSingleGetResponseDataRelationshipsBranchedFromDataType,
)
from .documents_single_get_response_data_relationships_comments import (
    DocumentsSingleGetResponseDataRelationshipsComments,
)
from .documents_single_get_response_data_relationships_comments_data_item import (
    DocumentsSingleGetResponseDataRelationshipsCommentsDataItem,
)
from .documents_single_get_response_data_relationships_comments_data_item_type import (
    DocumentsSingleGetResponseDataRelationshipsCommentsDataItemType,
)
from .documents_single_get_response_data_relationships_comments_links import (
    DocumentsSingleGetResponseDataRelationshipsCommentsLinks,
)
from .documents_single_get_response_data_relationships_comments_meta import (
    DocumentsSingleGetResponseDataRelationshipsCommentsMeta,
)
from .documents_single_get_response_data_relationships_derived_from import (
    DocumentsSingleGetResponseDataRelationshipsDerivedFrom,
)
from .documents_single_get_response_data_relationships_derived_from_data import (
    DocumentsSingleGetResponseDataRelationshipsDerivedFromData,
)
from .documents_single_get_response_data_relationships_derived_from_data_type import (
    DocumentsSingleGetResponseDataRelationshipsDerivedFromDataType,
)
from .documents_single_get_response_data_relationships_project import (
    DocumentsSingleGetResponseDataRelationshipsProject,
)
from .documents_single_get_response_data_relationships_project_data import (
    DocumentsSingleGetResponseDataRelationshipsProjectData,
)
from .documents_single_get_response_data_relationships_project_data_type import (
    DocumentsSingleGetResponseDataRelationshipsProjectDataType,
)
from .documents_single_get_response_data_relationships_updated_by import (
    DocumentsSingleGetResponseDataRelationshipsUpdatedBy,
)
from .documents_single_get_response_data_relationships_updated_by_data import (
    DocumentsSingleGetResponseDataRelationshipsUpdatedByData,
)
from .documents_single_get_response_data_relationships_updated_by_data_type import (
    DocumentsSingleGetResponseDataRelationshipsUpdatedByDataType,
)
from .documents_single_get_response_data_relationships_variant import (
    DocumentsSingleGetResponseDataRelationshipsVariant,
)
from .documents_single_get_response_data_relationships_variant_data import (
    DocumentsSingleGetResponseDataRelationshipsVariantData,
)
from .documents_single_get_response_data_relationships_variant_data_type import (
    DocumentsSingleGetResponseDataRelationshipsVariantDataType,
)
from .documents_single_get_response_data_type import (
    DocumentsSingleGetResponseDataType,
)
from .documents_single_get_response_included_item import (
    DocumentsSingleGetResponseIncludedItem,
)
from .documents_single_get_response_links import (
    DocumentsSingleGetResponseLinks,
)
from .documents_single_patch_request import DocumentsSinglePatchRequest
from .documents_single_patch_request_data import (
    DocumentsSinglePatchRequestData,
)
from .documents_single_patch_request_data_attributes import (
    DocumentsSinglePatchRequestDataAttributes,
)
from .documents_single_patch_request_data_attributes_home_page_content import (
    DocumentsSinglePatchRequestDataAttributesHomePageContent,
)
from .documents_single_patch_request_data_attributes_home_page_content_type import (
    DocumentsSinglePatchRequestDataAttributesHomePageContentType,
)
from .documents_single_patch_request_data_attributes_outline_numbering import (
    DocumentsSinglePatchRequestDataAttributesOutlineNumbering,
)
from .documents_single_patch_request_data_attributes_rendering_layouts_item import (
    DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem,
)
from .documents_single_patch_request_data_attributes_rendering_layouts_item_properties_item import (
    DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItemPropertiesItem,
)
from .documents_single_patch_request_data_type import (
    DocumentsSinglePatchRequestDataType,
)
from .documents_single_post_response import DocumentsSinglePostResponse
from .documents_single_post_response_data import (
    DocumentsSinglePostResponseData,
)
from .documents_single_post_response_data_attributes import (
    DocumentsSinglePostResponseDataAttributes,
)
from .documents_single_post_response_data_attributes_home_page_content import (
    DocumentsSinglePostResponseDataAttributesHomePageContent,
)
from .documents_single_post_response_data_attributes_home_page_content_type import (
    DocumentsSinglePostResponseDataAttributesHomePageContentType,
)
from .documents_single_post_response_data_attributes_outline_numbering import (
    DocumentsSinglePostResponseDataAttributesOutlineNumbering,
)
from .documents_single_post_response_data_attributes_rendering_layouts_item import (
    DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem,
)
from .documents_single_post_response_data_attributes_rendering_layouts_item_properties_item import (
    DocumentsSinglePostResponseDataAttributesRenderingLayoutsItemPropertiesItem,
)
from .documents_single_post_response_data_type import (
    DocumentsSinglePostResponseDataType,
)
from .enum_options_action_response_body import EnumOptionsActionResponseBody
from .enum_options_action_response_body_data_item import (
    EnumOptionsActionResponseBodyDataItem,
)
from .enum_options_action_response_body_links import (
    EnumOptionsActionResponseBodyLinks,
)
from .enum_options_action_response_body_meta import (
    EnumOptionsActionResponseBodyMeta,
)
from .enumerations_list_post_request import EnumerationsListPostRequest
from .enumerations_list_post_request_data_item import (
    EnumerationsListPostRequestDataItem,
)
from .enumerations_list_post_request_data_item_attributes import (
    EnumerationsListPostRequestDataItemAttributes,
)
from .enumerations_list_post_request_data_item_attributes_options_item import (
    EnumerationsListPostRequestDataItemAttributesOptionsItem,
)
from .enumerations_list_post_request_data_item_type import (
    EnumerationsListPostRequestDataItemType,
)
from .enumerations_list_post_response import EnumerationsListPostResponse
from .enumerations_list_post_response_data_item import (
    EnumerationsListPostResponseDataItem,
)
from .enumerations_list_post_response_data_item_links import (
    EnumerationsListPostResponseDataItemLinks,
)
from .enumerations_list_post_response_data_item_type import (
    EnumerationsListPostResponseDataItemType,
)
from .enumerations_single_get_response import EnumerationsSingleGetResponse
from .enumerations_single_get_response_data import (
    EnumerationsSingleGetResponseData,
)
from .enumerations_single_get_response_data_attributes import (
    EnumerationsSingleGetResponseDataAttributes,
)
from .enumerations_single_get_response_data_attributes_options_item import (
    EnumerationsSingleGetResponseDataAttributesOptionsItem,
)
from .enumerations_single_get_response_data_links import (
    EnumerationsSingleGetResponseDataLinks,
)
from .enumerations_single_get_response_data_meta import (
    EnumerationsSingleGetResponseDataMeta,
)
from .enumerations_single_get_response_data_meta_errors_item import (
    EnumerationsSingleGetResponseDataMetaErrorsItem,
)
from .enumerations_single_get_response_data_meta_errors_item_source import (
    EnumerationsSingleGetResponseDataMetaErrorsItemSource,
)
from .enumerations_single_get_response_data_type import (
    EnumerationsSingleGetResponseDataType,
)
from .enumerations_single_get_response_included_item import (
    EnumerationsSingleGetResponseIncludedItem,
)
from .enumerations_single_get_response_links import (
    EnumerationsSingleGetResponseLinks,
)
from .enumerations_single_patch_request import EnumerationsSinglePatchRequest
from .enumerations_single_patch_request_data import (
    EnumerationsSinglePatchRequestData,
)
from .enumerations_single_patch_request_data_attributes import (
    EnumerationsSinglePatchRequestDataAttributes,
)
from .enumerations_single_patch_request_data_attributes_options_item import (
    EnumerationsSinglePatchRequestDataAttributesOptionsItem,
)
from .enumerations_single_patch_request_data_type import (
    EnumerationsSinglePatchRequestDataType,
)
from .errors import Errors
from .errors_errors_item import ErrorsErrorsItem
from .errors_errors_item_source import ErrorsErrorsItemSource
from .globalroles_single_get_response import GlobalrolesSingleGetResponse
from .globalroles_single_get_response_data import (
    GlobalrolesSingleGetResponseData,
)
from .globalroles_single_get_response_data_links import (
    GlobalrolesSingleGetResponseDataLinks,
)
from .globalroles_single_get_response_data_meta import (
    GlobalrolesSingleGetResponseDataMeta,
)
from .globalroles_single_get_response_data_meta_errors_item import (
    GlobalrolesSingleGetResponseDataMetaErrorsItem,
)
from .globalroles_single_get_response_data_meta_errors_item_source import (
    GlobalrolesSingleGetResponseDataMetaErrorsItemSource,
)
from .globalroles_single_get_response_data_relationships import (
    GlobalrolesSingleGetResponseDataRelationships,
)
from .globalroles_single_get_response_data_relationships_users import (
    GlobalrolesSingleGetResponseDataRelationshipsUsers,
)
from .globalroles_single_get_response_data_relationships_users_data_item import (
    GlobalrolesSingleGetResponseDataRelationshipsUsersDataItem,
)
from .globalroles_single_get_response_data_relationships_users_data_item_type import (
    GlobalrolesSingleGetResponseDataRelationshipsUsersDataItemType,
)
from .globalroles_single_get_response_data_relationships_users_meta import (
    GlobalrolesSingleGetResponseDataRelationshipsUsersMeta,
)
from .globalroles_single_get_response_data_type import (
    GlobalrolesSingleGetResponseDataType,
)
from .globalroles_single_get_response_included_item import (
    GlobalrolesSingleGetResponseIncludedItem,
)
from .globalroles_single_get_response_links import (
    GlobalrolesSingleGetResponseLinks,
)
from .icons_list_get_response import IconsListGetResponse
from .icons_list_get_response_data_item import IconsListGetResponseDataItem
from .icons_list_get_response_data_item_attributes import (
    IconsListGetResponseDataItemAttributes,
)
from .icons_list_get_response_data_item_links import (
    IconsListGetResponseDataItemLinks,
)
from .icons_list_get_response_data_item_meta import (
    IconsListGetResponseDataItemMeta,
)
from .icons_list_get_response_data_item_meta_errors_item import (
    IconsListGetResponseDataItemMetaErrorsItem,
)
from .icons_list_get_response_data_item_meta_errors_item_source import (
    IconsListGetResponseDataItemMetaErrorsItemSource,
)
from .icons_list_get_response_data_item_type import (
    IconsListGetResponseDataItemType,
)
from .icons_list_get_response_included_item import (
    IconsListGetResponseIncludedItem,
)
from .icons_list_get_response_links import IconsListGetResponseLinks
from .icons_list_get_response_meta import IconsListGetResponseMeta
from .icons_single_get_response import IconsSingleGetResponse
from .icons_single_get_response_data import IconsSingleGetResponseData
from .icons_single_get_response_data_attributes import (
    IconsSingleGetResponseDataAttributes,
)
from .icons_single_get_response_data_links import (
    IconsSingleGetResponseDataLinks,
)
from .icons_single_get_response_data_meta import IconsSingleGetResponseDataMeta
from .icons_single_get_response_data_meta_errors_item import (
    IconsSingleGetResponseDataMetaErrorsItem,
)
from .icons_single_get_response_data_meta_errors_item_source import (
    IconsSingleGetResponseDataMetaErrorsItemSource,
)
from .icons_single_get_response_data_type import IconsSingleGetResponseDataType
from .icons_single_get_response_included_item import (
    IconsSingleGetResponseIncludedItem,
)
from .icons_single_get_response_links import IconsSingleGetResponseLinks
from .linkedworkitems_list_delete_request import (
    LinkedworkitemsListDeleteRequest,
)
from .linkedworkitems_list_delete_request_data_item import (
    LinkedworkitemsListDeleteRequestDataItem,
)
from .linkedworkitems_list_delete_request_data_item_type import (
    LinkedworkitemsListDeleteRequestDataItemType,
)
from .linkedworkitems_list_get_response import LinkedworkitemsListGetResponse
from .linkedworkitems_list_get_response_data_item import (
    LinkedworkitemsListGetResponseDataItem,
)
from .linkedworkitems_list_get_response_data_item_attributes import (
    LinkedworkitemsListGetResponseDataItemAttributes,
)
from .linkedworkitems_list_get_response_data_item_links import (
    LinkedworkitemsListGetResponseDataItemLinks,
)
from .linkedworkitems_list_get_response_data_item_meta import (
    LinkedworkitemsListGetResponseDataItemMeta,
)
from .linkedworkitems_list_get_response_data_item_meta_errors_item import (
    LinkedworkitemsListGetResponseDataItemMetaErrorsItem,
)
from .linkedworkitems_list_get_response_data_item_meta_errors_item_source import (
    LinkedworkitemsListGetResponseDataItemMetaErrorsItemSource,
)
from .linkedworkitems_list_get_response_data_item_relationships import (
    LinkedworkitemsListGetResponseDataItemRelationships,
)
from .linkedworkitems_list_get_response_data_item_relationships_work_item import (
    LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem,
)
from .linkedworkitems_list_get_response_data_item_relationships_work_item_data import (
    LinkedworkitemsListGetResponseDataItemRelationshipsWorkItemData,
)
from .linkedworkitems_list_get_response_data_item_relationships_work_item_data_type import (
    LinkedworkitemsListGetResponseDataItemRelationshipsWorkItemDataType,
)
from .linkedworkitems_list_get_response_data_item_type import (
    LinkedworkitemsListGetResponseDataItemType,
)
from .linkedworkitems_list_get_response_included_item import (
    LinkedworkitemsListGetResponseIncludedItem,
)
from .linkedworkitems_list_get_response_links import (
    LinkedworkitemsListGetResponseLinks,
)
from .linkedworkitems_list_get_response_meta import (
    LinkedworkitemsListGetResponseMeta,
)
from .linkedworkitems_list_post_request import LinkedworkitemsListPostRequest
from .linkedworkitems_list_post_request_data_item import (
    LinkedworkitemsListPostRequestDataItem,
)
from .linkedworkitems_list_post_request_data_item_attributes import (
    LinkedworkitemsListPostRequestDataItemAttributes,
)
from .linkedworkitems_list_post_request_data_item_relationships import (
    LinkedworkitemsListPostRequestDataItemRelationships,
)
from .linkedworkitems_list_post_request_data_item_relationships_work_item import (
    LinkedworkitemsListPostRequestDataItemRelationshipsWorkItem,
)
from .linkedworkitems_list_post_request_data_item_relationships_work_item_data import (
    LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemData,
)
from .linkedworkitems_list_post_request_data_item_relationships_work_item_data_type import (
    LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemDataType,
)
from .linkedworkitems_list_post_request_data_item_type import (
    LinkedworkitemsListPostRequestDataItemType,
)
from .linkedworkitems_list_post_response import LinkedworkitemsListPostResponse
from .linkedworkitems_list_post_response_data_item import (
    LinkedworkitemsListPostResponseDataItem,
)
from .linkedworkitems_list_post_response_data_item_links import (
    LinkedworkitemsListPostResponseDataItemLinks,
)
from .linkedworkitems_list_post_response_data_item_type import (
    LinkedworkitemsListPostResponseDataItemType,
)
from .linkedworkitems_single_get_response import (
    LinkedworkitemsSingleGetResponse,
)
from .linkedworkitems_single_get_response_data import (
    LinkedworkitemsSingleGetResponseData,
)
from .linkedworkitems_single_get_response_data_attributes import (
    LinkedworkitemsSingleGetResponseDataAttributes,
)
from .linkedworkitems_single_get_response_data_links import (
    LinkedworkitemsSingleGetResponseDataLinks,
)
from .linkedworkitems_single_get_response_data_meta import (
    LinkedworkitemsSingleGetResponseDataMeta,
)
from .linkedworkitems_single_get_response_data_meta_errors_item import (
    LinkedworkitemsSingleGetResponseDataMetaErrorsItem,
)
from .linkedworkitems_single_get_response_data_meta_errors_item_source import (
    LinkedworkitemsSingleGetResponseDataMetaErrorsItemSource,
)
from .linkedworkitems_single_get_response_data_relationships import (
    LinkedworkitemsSingleGetResponseDataRelationships,
)
from .linkedworkitems_single_get_response_data_relationships_work_item import (
    LinkedworkitemsSingleGetResponseDataRelationshipsWorkItem,
)
from .linkedworkitems_single_get_response_data_relationships_work_item_data import (
    LinkedworkitemsSingleGetResponseDataRelationshipsWorkItemData,
)
from .linkedworkitems_single_get_response_data_relationships_work_item_data_type import (
    LinkedworkitemsSingleGetResponseDataRelationshipsWorkItemDataType,
)
from .linkedworkitems_single_get_response_data_type import (
    LinkedworkitemsSingleGetResponseDataType,
)
from .linkedworkitems_single_get_response_included_item import (
    LinkedworkitemsSingleGetResponseIncludedItem,
)
from .linkedworkitems_single_get_response_links import (
    LinkedworkitemsSingleGetResponseLinks,
)
from .linkedworkitems_single_patch_request import (
    LinkedworkitemsSinglePatchRequest,
)
from .linkedworkitems_single_patch_request_data import (
    LinkedworkitemsSinglePatchRequestData,
)
from .linkedworkitems_single_patch_request_data_attributes import (
    LinkedworkitemsSinglePatchRequestDataAttributes,
)
from .linkedworkitems_single_patch_request_data_type import (
    LinkedworkitemsSinglePatchRequestDataType,
)
from .move_work_item_to_document_request_body import (
    MoveWorkItemToDocumentRequestBody,
)
from .page_attachments_list_post_request import PageAttachmentsListPostRequest
from .page_attachments_list_post_request_data_item import (
    PageAttachmentsListPostRequestDataItem,
)
from .page_attachments_list_post_request_data_item_attributes import (
    PageAttachmentsListPostRequestDataItemAttributes,
)
from .page_attachments_list_post_request_data_item_type import (
    PageAttachmentsListPostRequestDataItemType,
)
from .page_attachments_list_post_response import (
    PageAttachmentsListPostResponse,
)
from .page_attachments_list_post_response_data_item import (
    PageAttachmentsListPostResponseDataItem,
)
from .page_attachments_list_post_response_data_item_links import (
    PageAttachmentsListPostResponseDataItemLinks,
)
from .page_attachments_list_post_response_data_item_type import (
    PageAttachmentsListPostResponseDataItemType,
)
from .page_attachments_single_get_response import (
    PageAttachmentsSingleGetResponse,
)
from .page_attachments_single_get_response_data import (
    PageAttachmentsSingleGetResponseData,
)
from .page_attachments_single_get_response_data_attributes import (
    PageAttachmentsSingleGetResponseDataAttributes,
)
from .page_attachments_single_get_response_data_links import (
    PageAttachmentsSingleGetResponseDataLinks,
)
from .page_attachments_single_get_response_data_meta import (
    PageAttachmentsSingleGetResponseDataMeta,
)
from .page_attachments_single_get_response_data_meta_errors_item import (
    PageAttachmentsSingleGetResponseDataMetaErrorsItem,
)
from .page_attachments_single_get_response_data_meta_errors_item_source import (
    PageAttachmentsSingleGetResponseDataMetaErrorsItemSource,
)
from .page_attachments_single_get_response_data_relationships import (
    PageAttachmentsSingleGetResponseDataRelationships,
)
from .page_attachments_single_get_response_data_relationships_author import (
    PageAttachmentsSingleGetResponseDataRelationshipsAuthor,
)
from .page_attachments_single_get_response_data_relationships_author_data import (
    PageAttachmentsSingleGetResponseDataRelationshipsAuthorData,
)
from .page_attachments_single_get_response_data_relationships_author_data_type import (
    PageAttachmentsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .page_attachments_single_get_response_data_relationships_project import (
    PageAttachmentsSingleGetResponseDataRelationshipsProject,
)
from .page_attachments_single_get_response_data_relationships_project_data import (
    PageAttachmentsSingleGetResponseDataRelationshipsProjectData,
)
from .page_attachments_single_get_response_data_relationships_project_data_type import (
    PageAttachmentsSingleGetResponseDataRelationshipsProjectDataType,
)
from .page_attachments_single_get_response_data_type import (
    PageAttachmentsSingleGetResponseDataType,
)
from .page_attachments_single_get_response_included_item import (
    PageAttachmentsSingleGetResponseIncludedItem,
)
from .page_attachments_single_get_response_links import (
    PageAttachmentsSingleGetResponseLinks,
)
from .pages_single_get_response import PagesSingleGetResponse
from .pages_single_get_response_data import PagesSingleGetResponseData
from .pages_single_get_response_data_attributes import (
    PagesSingleGetResponseDataAttributes,
)
from .pages_single_get_response_data_links import (
    PagesSingleGetResponseDataLinks,
)
from .pages_single_get_response_data_meta import PagesSingleGetResponseDataMeta
from .pages_single_get_response_data_meta_errors_item import (
    PagesSingleGetResponseDataMetaErrorsItem,
)
from .pages_single_get_response_data_meta_errors_item_source import (
    PagesSingleGetResponseDataMetaErrorsItemSource,
)
from .pages_single_get_response_data_relationships import (
    PagesSingleGetResponseDataRelationships,
)
from .pages_single_get_response_data_relationships_attachments import (
    PagesSingleGetResponseDataRelationshipsAttachments,
)
from .pages_single_get_response_data_relationships_attachments_data_item import (
    PagesSingleGetResponseDataRelationshipsAttachmentsDataItem,
)
from .pages_single_get_response_data_relationships_attachments_data_item_type import (
    PagesSingleGetResponseDataRelationshipsAttachmentsDataItemType,
)
from .pages_single_get_response_data_relationships_attachments_meta import (
    PagesSingleGetResponseDataRelationshipsAttachmentsMeta,
)
from .pages_single_get_response_data_relationships_author import (
    PagesSingleGetResponseDataRelationshipsAuthor,
)
from .pages_single_get_response_data_relationships_author_data import (
    PagesSingleGetResponseDataRelationshipsAuthorData,
)
from .pages_single_get_response_data_relationships_author_data_type import (
    PagesSingleGetResponseDataRelationshipsAuthorDataType,
)
from .pages_single_get_response_data_relationships_project import (
    PagesSingleGetResponseDataRelationshipsProject,
)
from .pages_single_get_response_data_relationships_project_data import (
    PagesSingleGetResponseDataRelationshipsProjectData,
)
from .pages_single_get_response_data_relationships_project_data_type import (
    PagesSingleGetResponseDataRelationshipsProjectDataType,
)
from .pages_single_get_response_data_relationships_updated_by import (
    PagesSingleGetResponseDataRelationshipsUpdatedBy,
)
from .pages_single_get_response_data_relationships_updated_by_data import (
    PagesSingleGetResponseDataRelationshipsUpdatedByData,
)
from .pages_single_get_response_data_relationships_updated_by_data_type import (
    PagesSingleGetResponseDataRelationshipsUpdatedByDataType,
)
from .pages_single_get_response_data_type import PagesSingleGetResponseDataType
from .pages_single_get_response_included_item import (
    PagesSingleGetResponseIncludedItem,
)
from .pages_single_get_response_links import PagesSingleGetResponseLinks
from .pages_single_patch_request import PagesSinglePatchRequest
from .pages_single_patch_request_data import PagesSinglePatchRequestData
from .pages_single_patch_request_data_attributes import (
    PagesSinglePatchRequestDataAttributes,
)
from .pages_single_patch_request_data_type import (
    PagesSinglePatchRequestDataType,
)
from .pagination import Pagination
from .patch_document_attachments_request_body import (
    PatchDocumentAttachmentsRequestBody,
)
from .patch_work_item_attachments_request_body import (
    PatchWorkItemAttachmentsRequestBody,
)
from .post_document_attachments_request_body import (
    PostDocumentAttachmentsRequestBody,
)
from .post_page_attachments_request_body import PostPageAttachmentsRequestBody
from .post_work_item_attachments_request_body import (
    PostWorkItemAttachmentsRequestBody,
)
from .projects_list_get_response import ProjectsListGetResponse
from .projects_list_get_response_data_item import (
    ProjectsListGetResponseDataItem,
)
from .projects_list_get_response_data_item_attributes import (
    ProjectsListGetResponseDataItemAttributes,
)
from .projects_list_get_response_data_item_attributes_description import (
    ProjectsListGetResponseDataItemAttributesDescription,
)
from .projects_list_get_response_data_item_attributes_description_type import (
    ProjectsListGetResponseDataItemAttributesDescriptionType,
)
from .projects_list_get_response_data_item_links import (
    ProjectsListGetResponseDataItemLinks,
)
from .projects_list_get_response_data_item_meta import (
    ProjectsListGetResponseDataItemMeta,
)
from .projects_list_get_response_data_item_meta_errors_item import (
    ProjectsListGetResponseDataItemMetaErrorsItem,
)
from .projects_list_get_response_data_item_meta_errors_item_source import (
    ProjectsListGetResponseDataItemMetaErrorsItemSource,
)
from .projects_list_get_response_data_item_relationships import (
    ProjectsListGetResponseDataItemRelationships,
)
from .projects_list_get_response_data_item_relationships_lead import (
    ProjectsListGetResponseDataItemRelationshipsLead,
)
from .projects_list_get_response_data_item_relationships_lead_data import (
    ProjectsListGetResponseDataItemRelationshipsLeadData,
)
from .projects_list_get_response_data_item_relationships_lead_data_type import (
    ProjectsListGetResponseDataItemRelationshipsLeadDataType,
)
from .projects_list_get_response_data_item_type import (
    ProjectsListGetResponseDataItemType,
)
from .projects_list_get_response_included_item import (
    ProjectsListGetResponseIncludedItem,
)
from .projects_list_get_response_links import ProjectsListGetResponseLinks
from .projects_list_get_response_meta import ProjectsListGetResponseMeta
from .projects_single_get_response import ProjectsSingleGetResponse
from .projects_single_get_response_data import ProjectsSingleGetResponseData
from .projects_single_get_response_data_attributes import (
    ProjectsSingleGetResponseDataAttributes,
)
from .projects_single_get_response_data_attributes_description import (
    ProjectsSingleGetResponseDataAttributesDescription,
)
from .projects_single_get_response_data_attributes_description_type import (
    ProjectsSingleGetResponseDataAttributesDescriptionType,
)
from .projects_single_get_response_data_links import (
    ProjectsSingleGetResponseDataLinks,
)
from .projects_single_get_response_data_meta import (
    ProjectsSingleGetResponseDataMeta,
)
from .projects_single_get_response_data_meta_errors_item import (
    ProjectsSingleGetResponseDataMetaErrorsItem,
)
from .projects_single_get_response_data_meta_errors_item_source import (
    ProjectsSingleGetResponseDataMetaErrorsItemSource,
)
from .projects_single_get_response_data_relationships import (
    ProjectsSingleGetResponseDataRelationships,
)
from .projects_single_get_response_data_relationships_lead import (
    ProjectsSingleGetResponseDataRelationshipsLead,
)
from .projects_single_get_response_data_relationships_lead_data import (
    ProjectsSingleGetResponseDataRelationshipsLeadData,
)
from .projects_single_get_response_data_relationships_lead_data_type import (
    ProjectsSingleGetResponseDataRelationshipsLeadDataType,
)
from .projects_single_get_response_data_type import (
    ProjectsSingleGetResponseDataType,
)
from .projects_single_get_response_included_item import (
    ProjectsSingleGetResponseIncludedItem,
)
from .projects_single_get_response_links import ProjectsSingleGetResponseLinks
from .resource_reference import ResourceReference
from .set_license_request_body import SetLicenseRequestBody
from .set_license_request_body_license import SetLicenseRequestBodyLicense
from .sparse_fields import SparseFields
from .usergroups_single_get_response import UsergroupsSingleGetResponse
from .usergroups_single_get_response_data import (
    UsergroupsSingleGetResponseData,
)
from .usergroups_single_get_response_data_attributes import (
    UsergroupsSingleGetResponseDataAttributes,
)
from .usergroups_single_get_response_data_attributes_description import (
    UsergroupsSingleGetResponseDataAttributesDescription,
)
from .usergroups_single_get_response_data_attributes_description_type import (
    UsergroupsSingleGetResponseDataAttributesDescriptionType,
)
from .usergroups_single_get_response_data_links import (
    UsergroupsSingleGetResponseDataLinks,
)
from .usergroups_single_get_response_data_meta import (
    UsergroupsSingleGetResponseDataMeta,
)
from .usergroups_single_get_response_data_meta_errors_item import (
    UsergroupsSingleGetResponseDataMetaErrorsItem,
)
from .usergroups_single_get_response_data_meta_errors_item_source import (
    UsergroupsSingleGetResponseDataMetaErrorsItemSource,
)
from .usergroups_single_get_response_data_relationships import (
    UsergroupsSingleGetResponseDataRelationships,
)
from .usergroups_single_get_response_data_relationships_global_roles import (
    UsergroupsSingleGetResponseDataRelationshipsGlobalRoles,
)
from .usergroups_single_get_response_data_relationships_global_roles_data_item import (
    UsergroupsSingleGetResponseDataRelationshipsGlobalRolesDataItem,
)
from .usergroups_single_get_response_data_relationships_global_roles_data_item_type import (
    UsergroupsSingleGetResponseDataRelationshipsGlobalRolesDataItemType,
)
from .usergroups_single_get_response_data_relationships_global_roles_meta import (
    UsergroupsSingleGetResponseDataRelationshipsGlobalRolesMeta,
)
from .usergroups_single_get_response_data_relationships_project_roles import (
    UsergroupsSingleGetResponseDataRelationshipsProjectRoles,
)
from .usergroups_single_get_response_data_relationships_project_roles_data_item import (
    UsergroupsSingleGetResponseDataRelationshipsProjectRolesDataItem,
)
from .usergroups_single_get_response_data_relationships_project_roles_data_item_type import (
    UsergroupsSingleGetResponseDataRelationshipsProjectRolesDataItemType,
)
from .usergroups_single_get_response_data_relationships_project_roles_meta import (
    UsergroupsSingleGetResponseDataRelationshipsProjectRolesMeta,
)
from .usergroups_single_get_response_data_relationships_users import (
    UsergroupsSingleGetResponseDataRelationshipsUsers,
)
from .usergroups_single_get_response_data_relationships_users_data_item import (
    UsergroupsSingleGetResponseDataRelationshipsUsersDataItem,
)
from .usergroups_single_get_response_data_relationships_users_data_item_type import (
    UsergroupsSingleGetResponseDataRelationshipsUsersDataItemType,
)
from .usergroups_single_get_response_data_relationships_users_meta import (
    UsergroupsSingleGetResponseDataRelationshipsUsersMeta,
)
from .usergroups_single_get_response_data_type import (
    UsergroupsSingleGetResponseDataType,
)
from .usergroups_single_get_response_included_item import (
    UsergroupsSingleGetResponseIncludedItem,
)
from .usergroups_single_get_response_links import (
    UsergroupsSingleGetResponseLinks,
)
from .users_list_get_response import UsersListGetResponse
from .users_list_get_response_data_item import UsersListGetResponseDataItem
from .users_list_get_response_data_item_attributes import (
    UsersListGetResponseDataItemAttributes,
)
from .users_list_get_response_data_item_attributes_description import (
    UsersListGetResponseDataItemAttributesDescription,
)
from .users_list_get_response_data_item_attributes_description_type import (
    UsersListGetResponseDataItemAttributesDescriptionType,
)
from .users_list_get_response_data_item_links import (
    UsersListGetResponseDataItemLinks,
)
from .users_list_get_response_data_item_meta import (
    UsersListGetResponseDataItemMeta,
)
from .users_list_get_response_data_item_meta_errors_item import (
    UsersListGetResponseDataItemMetaErrorsItem,
)
from .users_list_get_response_data_item_meta_errors_item_source import (
    UsersListGetResponseDataItemMetaErrorsItemSource,
)
from .users_list_get_response_data_item_relationships import (
    UsersListGetResponseDataItemRelationships,
)
from .users_list_get_response_data_item_relationships_global_roles import (
    UsersListGetResponseDataItemRelationshipsGlobalRoles,
)
from .users_list_get_response_data_item_relationships_global_roles_data_item import (
    UsersListGetResponseDataItemRelationshipsGlobalRolesDataItem,
)
from .users_list_get_response_data_item_relationships_global_roles_data_item_type import (
    UsersListGetResponseDataItemRelationshipsGlobalRolesDataItemType,
)
from .users_list_get_response_data_item_relationships_global_roles_meta import (
    UsersListGetResponseDataItemRelationshipsGlobalRolesMeta,
)
from .users_list_get_response_data_item_relationships_project_roles import (
    UsersListGetResponseDataItemRelationshipsProjectRoles,
)
from .users_list_get_response_data_item_relationships_project_roles_data_item import (
    UsersListGetResponseDataItemRelationshipsProjectRolesDataItem,
)
from .users_list_get_response_data_item_relationships_project_roles_data_item_type import (
    UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType,
)
from .users_list_get_response_data_item_relationships_project_roles_meta import (
    UsersListGetResponseDataItemRelationshipsProjectRolesMeta,
)
from .users_list_get_response_data_item_relationships_user_groups import (
    UsersListGetResponseDataItemRelationshipsUserGroups,
)
from .users_list_get_response_data_item_relationships_user_groups_data_item import (
    UsersListGetResponseDataItemRelationshipsUserGroupsDataItem,
)
from .users_list_get_response_data_item_relationships_user_groups_data_item_type import (
    UsersListGetResponseDataItemRelationshipsUserGroupsDataItemType,
)
from .users_list_get_response_data_item_relationships_user_groups_meta import (
    UsersListGetResponseDataItemRelationshipsUserGroupsMeta,
)
from .users_list_get_response_data_item_type import (
    UsersListGetResponseDataItemType,
)
from .users_list_get_response_included_item import (
    UsersListGetResponseIncludedItem,
)
from .users_list_get_response_links import UsersListGetResponseLinks
from .users_list_get_response_meta import UsersListGetResponseMeta
from .users_list_post_request import UsersListPostRequest
from .users_list_post_request_data_item import UsersListPostRequestDataItem
from .users_list_post_request_data_item_attributes import (
    UsersListPostRequestDataItemAttributes,
)
from .users_list_post_request_data_item_attributes_description import (
    UsersListPostRequestDataItemAttributesDescription,
)
from .users_list_post_request_data_item_attributes_description_type import (
    UsersListPostRequestDataItemAttributesDescriptionType,
)
from .users_list_post_request_data_item_relationships import (
    UsersListPostRequestDataItemRelationships,
)
from .users_list_post_request_data_item_relationships_global_roles import (
    UsersListPostRequestDataItemRelationshipsGlobalRoles,
)
from .users_list_post_request_data_item_relationships_global_roles_data_item import (
    UsersListPostRequestDataItemRelationshipsGlobalRolesDataItem,
)
from .users_list_post_request_data_item_relationships_global_roles_data_item_type import (
    UsersListPostRequestDataItemRelationshipsGlobalRolesDataItemType,
)
from .users_list_post_request_data_item_relationships_project_roles import (
    UsersListPostRequestDataItemRelationshipsProjectRoles,
)
from .users_list_post_request_data_item_relationships_project_roles_data_item import (
    UsersListPostRequestDataItemRelationshipsProjectRolesDataItem,
)
from .users_list_post_request_data_item_relationships_project_roles_data_item_type import (
    UsersListPostRequestDataItemRelationshipsProjectRolesDataItemType,
)
from .users_list_post_request_data_item_relationships_user_groups import (
    UsersListPostRequestDataItemRelationshipsUserGroups,
)
from .users_list_post_request_data_item_relationships_user_groups_data_item import (
    UsersListPostRequestDataItemRelationshipsUserGroupsDataItem,
)
from .users_list_post_request_data_item_relationships_user_groups_data_item_type import (
    UsersListPostRequestDataItemRelationshipsUserGroupsDataItemType,
)
from .users_list_post_request_data_item_type import (
    UsersListPostRequestDataItemType,
)
from .users_list_post_response import UsersListPostResponse
from .users_list_post_response_data_item import UsersListPostResponseDataItem
from .users_list_post_response_data_item_links import (
    UsersListPostResponseDataItemLinks,
)
from .users_list_post_response_data_item_type import (
    UsersListPostResponseDataItemType,
)
from .users_single_get_response import UsersSingleGetResponse
from .users_single_get_response_data import UsersSingleGetResponseData
from .users_single_get_response_data_attributes import (
    UsersSingleGetResponseDataAttributes,
)
from .users_single_get_response_data_attributes_description import (
    UsersSingleGetResponseDataAttributesDescription,
)
from .users_single_get_response_data_attributes_description_type import (
    UsersSingleGetResponseDataAttributesDescriptionType,
)
from .users_single_get_response_data_links import (
    UsersSingleGetResponseDataLinks,
)
from .users_single_get_response_data_meta import UsersSingleGetResponseDataMeta
from .users_single_get_response_data_meta_errors_item import (
    UsersSingleGetResponseDataMetaErrorsItem,
)
from .users_single_get_response_data_meta_errors_item_source import (
    UsersSingleGetResponseDataMetaErrorsItemSource,
)
from .users_single_get_response_data_relationships import (
    UsersSingleGetResponseDataRelationships,
)
from .users_single_get_response_data_relationships_global_roles import (
    UsersSingleGetResponseDataRelationshipsGlobalRoles,
)
from .users_single_get_response_data_relationships_global_roles_data_item import (
    UsersSingleGetResponseDataRelationshipsGlobalRolesDataItem,
)
from .users_single_get_response_data_relationships_global_roles_data_item_type import (
    UsersSingleGetResponseDataRelationshipsGlobalRolesDataItemType,
)
from .users_single_get_response_data_relationships_global_roles_meta import (
    UsersSingleGetResponseDataRelationshipsGlobalRolesMeta,
)
from .users_single_get_response_data_relationships_project_roles import (
    UsersSingleGetResponseDataRelationshipsProjectRoles,
)
from .users_single_get_response_data_relationships_project_roles_data_item import (
    UsersSingleGetResponseDataRelationshipsProjectRolesDataItem,
)
from .users_single_get_response_data_relationships_project_roles_data_item_type import (
    UsersSingleGetResponseDataRelationshipsProjectRolesDataItemType,
)
from .users_single_get_response_data_relationships_project_roles_meta import (
    UsersSingleGetResponseDataRelationshipsProjectRolesMeta,
)
from .users_single_get_response_data_relationships_user_groups import (
    UsersSingleGetResponseDataRelationshipsUserGroups,
)
from .users_single_get_response_data_relationships_user_groups_data_item import (
    UsersSingleGetResponseDataRelationshipsUserGroupsDataItem,
)
from .users_single_get_response_data_relationships_user_groups_data_item_type import (
    UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType,
)
from .users_single_get_response_data_relationships_user_groups_meta import (
    UsersSingleGetResponseDataRelationshipsUserGroupsMeta,
)
from .users_single_get_response_data_type import UsersSingleGetResponseDataType
from .users_single_get_response_included_item import (
    UsersSingleGetResponseIncludedItem,
)
from .users_single_get_response_links import UsersSingleGetResponseLinks
from .users_single_patch_request import UsersSinglePatchRequest
from .users_single_patch_request_data import UsersSinglePatchRequestData
from .users_single_patch_request_data_attributes import (
    UsersSinglePatchRequestDataAttributes,
)
from .users_single_patch_request_data_attributes_description import (
    UsersSinglePatchRequestDataAttributesDescription,
)
from .users_single_patch_request_data_attributes_description_type import (
    UsersSinglePatchRequestDataAttributesDescriptionType,
)
from .users_single_patch_request_data_relationships import (
    UsersSinglePatchRequestDataRelationships,
)
from .users_single_patch_request_data_relationships_global_roles import (
    UsersSinglePatchRequestDataRelationshipsGlobalRoles,
)
from .users_single_patch_request_data_relationships_global_roles_data_item import (
    UsersSinglePatchRequestDataRelationshipsGlobalRolesDataItem,
)
from .users_single_patch_request_data_relationships_global_roles_data_item_type import (
    UsersSinglePatchRequestDataRelationshipsGlobalRolesDataItemType,
)
from .users_single_patch_request_data_relationships_project_roles import (
    UsersSinglePatchRequestDataRelationshipsProjectRoles,
)
from .users_single_patch_request_data_relationships_project_roles_data_item import (
    UsersSinglePatchRequestDataRelationshipsProjectRolesDataItem,
)
from .users_single_patch_request_data_relationships_project_roles_data_item_type import (
    UsersSinglePatchRequestDataRelationshipsProjectRolesDataItemType,
)
from .users_single_patch_request_data_relationships_user_groups import (
    UsersSinglePatchRequestDataRelationshipsUserGroups,
)
from .users_single_patch_request_data_relationships_user_groups_data_item import (
    UsersSinglePatchRequestDataRelationshipsUserGroupsDataItem,
)
from .users_single_patch_request_data_relationships_user_groups_data_item_type import (
    UsersSinglePatchRequestDataRelationshipsUserGroupsDataItemType,
)
from .users_single_patch_request_data_type import (
    UsersSinglePatchRequestDataType,
)
from .workitem_attachments_list_get_response import (
    WorkitemAttachmentsListGetResponse,
)
from .workitem_attachments_list_get_response_data_item import (
    WorkitemAttachmentsListGetResponseDataItem,
)
from .workitem_attachments_list_get_response_data_item_attributes import (
    WorkitemAttachmentsListGetResponseDataItemAttributes,
)
from .workitem_attachments_list_get_response_data_item_links import (
    WorkitemAttachmentsListGetResponseDataItemLinks,
)
from .workitem_attachments_list_get_response_data_item_meta import (
    WorkitemAttachmentsListGetResponseDataItemMeta,
)
from .workitem_attachments_list_get_response_data_item_meta_errors_item import (
    WorkitemAttachmentsListGetResponseDataItemMetaErrorsItem,
)
from .workitem_attachments_list_get_response_data_item_meta_errors_item_source import (
    WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource,
)
from .workitem_attachments_list_get_response_data_item_relationships import (
    WorkitemAttachmentsListGetResponseDataItemRelationships,
)
from .workitem_attachments_list_get_response_data_item_relationships_author import (
    WorkitemAttachmentsListGetResponseDataItemRelationshipsAuthor,
)
from .workitem_attachments_list_get_response_data_item_relationships_author_data import (
    WorkitemAttachmentsListGetResponseDataItemRelationshipsAuthorData,
)
from .workitem_attachments_list_get_response_data_item_relationships_author_data_type import (
    WorkitemAttachmentsListGetResponseDataItemRelationshipsAuthorDataType,
)
from .workitem_attachments_list_get_response_data_item_relationships_project import (
    WorkitemAttachmentsListGetResponseDataItemRelationshipsProject,
)
from .workitem_attachments_list_get_response_data_item_relationships_project_data import (
    WorkitemAttachmentsListGetResponseDataItemRelationshipsProjectData,
)
from .workitem_attachments_list_get_response_data_item_relationships_project_data_type import (
    WorkitemAttachmentsListGetResponseDataItemRelationshipsProjectDataType,
)
from .workitem_attachments_list_get_response_data_item_type import (
    WorkitemAttachmentsListGetResponseDataItemType,
)
from .workitem_attachments_list_get_response_included_item import (
    WorkitemAttachmentsListGetResponseIncludedItem,
)
from .workitem_attachments_list_get_response_links import (
    WorkitemAttachmentsListGetResponseLinks,
)
from .workitem_attachments_list_get_response_meta import (
    WorkitemAttachmentsListGetResponseMeta,
)
from .workitem_attachments_list_post_request import (
    WorkitemAttachmentsListPostRequest,
)
from .workitem_attachments_list_post_request_data_item import (
    WorkitemAttachmentsListPostRequestDataItem,
)
from .workitem_attachments_list_post_request_data_item_attributes import (
    WorkitemAttachmentsListPostRequestDataItemAttributes,
)
from .workitem_attachments_list_post_request_data_item_type import (
    WorkitemAttachmentsListPostRequestDataItemType,
)
from .workitem_attachments_list_post_response import (
    WorkitemAttachmentsListPostResponse,
)
from .workitem_attachments_list_post_response_data_item import (
    WorkitemAttachmentsListPostResponseDataItem,
)
from .workitem_attachments_list_post_response_data_item_links import (
    WorkitemAttachmentsListPostResponseDataItemLinks,
)
from .workitem_attachments_list_post_response_data_item_type import (
    WorkitemAttachmentsListPostResponseDataItemType,
)
from .workitem_attachments_single_get_response import (
    WorkitemAttachmentsSingleGetResponse,
)
from .workitem_attachments_single_get_response_data import (
    WorkitemAttachmentsSingleGetResponseData,
)
from .workitem_attachments_single_get_response_data_attributes import (
    WorkitemAttachmentsSingleGetResponseDataAttributes,
)
from .workitem_attachments_single_get_response_data_links import (
    WorkitemAttachmentsSingleGetResponseDataLinks,
)
from .workitem_attachments_single_get_response_data_meta import (
    WorkitemAttachmentsSingleGetResponseDataMeta,
)
from .workitem_attachments_single_get_response_data_meta_errors_item import (
    WorkitemAttachmentsSingleGetResponseDataMetaErrorsItem,
)
from .workitem_attachments_single_get_response_data_meta_errors_item_source import (
    WorkitemAttachmentsSingleGetResponseDataMetaErrorsItemSource,
)
from .workitem_attachments_single_get_response_data_relationships import (
    WorkitemAttachmentsSingleGetResponseDataRelationships,
)
from .workitem_attachments_single_get_response_data_relationships_author import (
    WorkitemAttachmentsSingleGetResponseDataRelationshipsAuthor,
)
from .workitem_attachments_single_get_response_data_relationships_author_data import (
    WorkitemAttachmentsSingleGetResponseDataRelationshipsAuthorData,
)
from .workitem_attachments_single_get_response_data_relationships_author_data_type import (
    WorkitemAttachmentsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .workitem_attachments_single_get_response_data_relationships_project import (
    WorkitemAttachmentsSingleGetResponseDataRelationshipsProject,
)
from .workitem_attachments_single_get_response_data_relationships_project_data import (
    WorkitemAttachmentsSingleGetResponseDataRelationshipsProjectData,
)
from .workitem_attachments_single_get_response_data_relationships_project_data_type import (
    WorkitemAttachmentsSingleGetResponseDataRelationshipsProjectDataType,
)
from .workitem_attachments_single_get_response_data_type import (
    WorkitemAttachmentsSingleGetResponseDataType,
)
from .workitem_attachments_single_get_response_included_item import (
    WorkitemAttachmentsSingleGetResponseIncludedItem,
)
from .workitem_attachments_single_get_response_links import (
    WorkitemAttachmentsSingleGetResponseLinks,
)
from .workitem_attachments_single_patch_request import (
    WorkitemAttachmentsSinglePatchRequest,
)
from .workitem_attachments_single_patch_request_data import (
    WorkitemAttachmentsSinglePatchRequestData,
)
from .workitem_attachments_single_patch_request_data_attributes import (
    WorkitemAttachmentsSinglePatchRequestDataAttributes,
)
from .workitem_attachments_single_patch_request_data_type import (
    WorkitemAttachmentsSinglePatchRequestDataType,
)
from .workitem_comments_list_get_response import (
    WorkitemCommentsListGetResponse,
)
from .workitem_comments_list_get_response_data_item import (
    WorkitemCommentsListGetResponseDataItem,
)
from .workitem_comments_list_get_response_data_item_attributes import (
    WorkitemCommentsListGetResponseDataItemAttributes,
)
from .workitem_comments_list_get_response_data_item_attributes_text import (
    WorkitemCommentsListGetResponseDataItemAttributesText,
)
from .workitem_comments_list_get_response_data_item_attributes_text_type import (
    WorkitemCommentsListGetResponseDataItemAttributesTextType,
)
from .workitem_comments_list_get_response_data_item_links import (
    WorkitemCommentsListGetResponseDataItemLinks,
)
from .workitem_comments_list_get_response_data_item_meta import (
    WorkitemCommentsListGetResponseDataItemMeta,
)
from .workitem_comments_list_get_response_data_item_meta_errors_item import (
    WorkitemCommentsListGetResponseDataItemMetaErrorsItem,
)
from .workitem_comments_list_get_response_data_item_meta_errors_item_source import (
    WorkitemCommentsListGetResponseDataItemMetaErrorsItemSource,
)
from .workitem_comments_list_get_response_data_item_relationships import (
    WorkitemCommentsListGetResponseDataItemRelationships,
)
from .workitem_comments_list_get_response_data_item_relationships_author import (
    WorkitemCommentsListGetResponseDataItemRelationshipsAuthor,
)
from .workitem_comments_list_get_response_data_item_relationships_author_data import (
    WorkitemCommentsListGetResponseDataItemRelationshipsAuthorData,
)
from .workitem_comments_list_get_response_data_item_relationships_author_data_type import (
    WorkitemCommentsListGetResponseDataItemRelationshipsAuthorDataType,
)
from .workitem_comments_list_get_response_data_item_relationships_child_comments import (
    WorkitemCommentsListGetResponseDataItemRelationshipsChildComments,
)
from .workitem_comments_list_get_response_data_item_relationships_child_comments_data_item import (
    WorkitemCommentsListGetResponseDataItemRelationshipsChildCommentsDataItem,
)
from .workitem_comments_list_get_response_data_item_relationships_child_comments_data_item_type import (
    WorkitemCommentsListGetResponseDataItemRelationshipsChildCommentsDataItemType,
)
from .workitem_comments_list_get_response_data_item_relationships_child_comments_meta import (
    WorkitemCommentsListGetResponseDataItemRelationshipsChildCommentsMeta,
)
from .workitem_comments_list_get_response_data_item_relationships_parent_comment import (
    WorkitemCommentsListGetResponseDataItemRelationshipsParentComment,
)
from .workitem_comments_list_get_response_data_item_relationships_parent_comment_data import (
    WorkitemCommentsListGetResponseDataItemRelationshipsParentCommentData,
)
from .workitem_comments_list_get_response_data_item_relationships_parent_comment_data_type import (
    WorkitemCommentsListGetResponseDataItemRelationshipsParentCommentDataType,
)
from .workitem_comments_list_get_response_data_item_relationships_project import (
    WorkitemCommentsListGetResponseDataItemRelationshipsProject,
)
from .workitem_comments_list_get_response_data_item_relationships_project_data import (
    WorkitemCommentsListGetResponseDataItemRelationshipsProjectData,
)
from .workitem_comments_list_get_response_data_item_relationships_project_data_type import (
    WorkitemCommentsListGetResponseDataItemRelationshipsProjectDataType,
)
from .workitem_comments_list_get_response_data_item_type import (
    WorkitemCommentsListGetResponseDataItemType,
)
from .workitem_comments_list_get_response_included_item import (
    WorkitemCommentsListGetResponseIncludedItem,
)
from .workitem_comments_list_get_response_links import (
    WorkitemCommentsListGetResponseLinks,
)
from .workitem_comments_list_get_response_meta import (
    WorkitemCommentsListGetResponseMeta,
)
from .workitem_comments_list_post_request import (
    WorkitemCommentsListPostRequest,
)
from .workitem_comments_list_post_request_data_item import (
    WorkitemCommentsListPostRequestDataItem,
)
from .workitem_comments_list_post_request_data_item_attributes import (
    WorkitemCommentsListPostRequestDataItemAttributes,
)
from .workitem_comments_list_post_request_data_item_attributes_text import (
    WorkitemCommentsListPostRequestDataItemAttributesText,
)
from .workitem_comments_list_post_request_data_item_attributes_text_type import (
    WorkitemCommentsListPostRequestDataItemAttributesTextType,
)
from .workitem_comments_list_post_request_data_item_relationships import (
    WorkitemCommentsListPostRequestDataItemRelationships,
)
from .workitem_comments_list_post_request_data_item_relationships_author import (
    WorkitemCommentsListPostRequestDataItemRelationshipsAuthor,
)
from .workitem_comments_list_post_request_data_item_relationships_author_data import (
    WorkitemCommentsListPostRequestDataItemRelationshipsAuthorData,
)
from .workitem_comments_list_post_request_data_item_relationships_author_data_type import (
    WorkitemCommentsListPostRequestDataItemRelationshipsAuthorDataType,
)
from .workitem_comments_list_post_request_data_item_relationships_parent_comment import (
    WorkitemCommentsListPostRequestDataItemRelationshipsParentComment,
)
from .workitem_comments_list_post_request_data_item_relationships_parent_comment_data import (
    WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentData,
)
from .workitem_comments_list_post_request_data_item_relationships_parent_comment_data_type import (
    WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType,
)
from .workitem_comments_list_post_request_data_item_type import (
    WorkitemCommentsListPostRequestDataItemType,
)
from .workitem_comments_list_post_response import (
    WorkitemCommentsListPostResponse,
)
from .workitem_comments_list_post_response_data_item import (
    WorkitemCommentsListPostResponseDataItem,
)
from .workitem_comments_list_post_response_data_item_links import (
    WorkitemCommentsListPostResponseDataItemLinks,
)
from .workitem_comments_list_post_response_data_item_type import (
    WorkitemCommentsListPostResponseDataItemType,
)
from .workitem_comments_single_get_response import (
    WorkitemCommentsSingleGetResponse,
)
from .workitem_comments_single_get_response_data import (
    WorkitemCommentsSingleGetResponseData,
)
from .workitem_comments_single_get_response_data_attributes import (
    WorkitemCommentsSingleGetResponseDataAttributes,
)
from .workitem_comments_single_get_response_data_attributes_text import (
    WorkitemCommentsSingleGetResponseDataAttributesText,
)
from .workitem_comments_single_get_response_data_attributes_text_type import (
    WorkitemCommentsSingleGetResponseDataAttributesTextType,
)
from .workitem_comments_single_get_response_data_links import (
    WorkitemCommentsSingleGetResponseDataLinks,
)
from .workitem_comments_single_get_response_data_meta import (
    WorkitemCommentsSingleGetResponseDataMeta,
)
from .workitem_comments_single_get_response_data_meta_errors_item import (
    WorkitemCommentsSingleGetResponseDataMetaErrorsItem,
)
from .workitem_comments_single_get_response_data_meta_errors_item_source import (
    WorkitemCommentsSingleGetResponseDataMetaErrorsItemSource,
)
from .workitem_comments_single_get_response_data_relationships import (
    WorkitemCommentsSingleGetResponseDataRelationships,
)
from .workitem_comments_single_get_response_data_relationships_author import (
    WorkitemCommentsSingleGetResponseDataRelationshipsAuthor,
)
from .workitem_comments_single_get_response_data_relationships_author_data import (
    WorkitemCommentsSingleGetResponseDataRelationshipsAuthorData,
)
from .workitem_comments_single_get_response_data_relationships_author_data_type import (
    WorkitemCommentsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .workitem_comments_single_get_response_data_relationships_child_comments import (
    WorkitemCommentsSingleGetResponseDataRelationshipsChildComments,
)
from .workitem_comments_single_get_response_data_relationships_child_comments_data_item import (
    WorkitemCommentsSingleGetResponseDataRelationshipsChildCommentsDataItem,
)
from .workitem_comments_single_get_response_data_relationships_child_comments_data_item_type import (
    WorkitemCommentsSingleGetResponseDataRelationshipsChildCommentsDataItemType,
)
from .workitem_comments_single_get_response_data_relationships_child_comments_meta import (
    WorkitemCommentsSingleGetResponseDataRelationshipsChildCommentsMeta,
)
from .workitem_comments_single_get_response_data_relationships_parent_comment import (
    WorkitemCommentsSingleGetResponseDataRelationshipsParentComment,
)
from .workitem_comments_single_get_response_data_relationships_parent_comment_data import (
    WorkitemCommentsSingleGetResponseDataRelationshipsParentCommentData,
)
from .workitem_comments_single_get_response_data_relationships_parent_comment_data_type import (
    WorkitemCommentsSingleGetResponseDataRelationshipsParentCommentDataType,
)
from .workitem_comments_single_get_response_data_relationships_project import (
    WorkitemCommentsSingleGetResponseDataRelationshipsProject,
)
from .workitem_comments_single_get_response_data_relationships_project_data import (
    WorkitemCommentsSingleGetResponseDataRelationshipsProjectData,
)
from .workitem_comments_single_get_response_data_relationships_project_data_type import (
    WorkitemCommentsSingleGetResponseDataRelationshipsProjectDataType,
)
from .workitem_comments_single_get_response_data_type import (
    WorkitemCommentsSingleGetResponseDataType,
)
from .workitem_comments_single_get_response_included_item import (
    WorkitemCommentsSingleGetResponseIncludedItem,
)
from .workitem_comments_single_get_response_links import (
    WorkitemCommentsSingleGetResponseLinks,
)
from .workitem_comments_single_patch_request import (
    WorkitemCommentsSinglePatchRequest,
)
from .workitem_comments_single_patch_request_data import (
    WorkitemCommentsSinglePatchRequestData,
)
from .workitem_comments_single_patch_request_data_attributes import (
    WorkitemCommentsSinglePatchRequestDataAttributes,
)
from .workitem_comments_single_patch_request_data_type import (
    WorkitemCommentsSinglePatchRequestDataType,
)
from .workitems_list_delete_request import WorkitemsListDeleteRequest
from .workitems_list_delete_request_data_item import (
    WorkitemsListDeleteRequestDataItem,
)
from .workitems_list_delete_request_data_item_type import (
    WorkitemsListDeleteRequestDataItemType,
)
from .workitems_list_get_response import WorkitemsListGetResponse
from .workitems_list_get_response_data_item import (
    WorkitemsListGetResponseDataItem,
)
from .workitems_list_get_response_data_item_attributes import (
    WorkitemsListGetResponseDataItemAttributes,
)
from .workitems_list_get_response_data_item_attributes_description import (
    WorkitemsListGetResponseDataItemAttributesDescription,
)
from .workitems_list_get_response_data_item_attributes_description_type import (
    WorkitemsListGetResponseDataItemAttributesDescriptionType,
)
from .workitems_list_get_response_data_item_attributes_hyperlinks_item import (
    WorkitemsListGetResponseDataItemAttributesHyperlinksItem,
)
from .workitems_list_get_response_data_item_links import (
    WorkitemsListGetResponseDataItemLinks,
)
from .workitems_list_get_response_data_item_meta import (
    WorkitemsListGetResponseDataItemMeta,
)
from .workitems_list_get_response_data_item_meta_errors_item import (
    WorkitemsListGetResponseDataItemMetaErrorsItem,
)
from .workitems_list_get_response_data_item_meta_errors_item_source import (
    WorkitemsListGetResponseDataItemMetaErrorsItemSource,
)
from .workitems_list_get_response_data_item_relationships import (
    WorkitemsListGetResponseDataItemRelationships,
)
from .workitems_list_get_response_data_item_relationships_assignee import (
    WorkitemsListGetResponseDataItemRelationshipsAssignee,
)
from .workitems_list_get_response_data_item_relationships_assignee_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsAssigneeDataItem,
)
from .workitems_list_get_response_data_item_relationships_assignee_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsAssigneeDataItemType,
)
from .workitems_list_get_response_data_item_relationships_assignee_meta import (
    WorkitemsListGetResponseDataItemRelationshipsAssigneeMeta,
)
from .workitems_list_get_response_data_item_relationships_attachments import (
    WorkitemsListGetResponseDataItemRelationshipsAttachments,
)
from .workitems_list_get_response_data_item_relationships_attachments_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsAttachmentsDataItem,
)
from .workitems_list_get_response_data_item_relationships_attachments_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsAttachmentsDataItemType,
)
from .workitems_list_get_response_data_item_relationships_attachments_links import (
    WorkitemsListGetResponseDataItemRelationshipsAttachmentsLinks,
)
from .workitems_list_get_response_data_item_relationships_attachments_meta import (
    WorkitemsListGetResponseDataItemRelationshipsAttachmentsMeta,
)
from .workitems_list_get_response_data_item_relationships_author import (
    WorkitemsListGetResponseDataItemRelationshipsAuthor,
)
from .workitems_list_get_response_data_item_relationships_author_data import (
    WorkitemsListGetResponseDataItemRelationshipsAuthorData,
)
from .workitems_list_get_response_data_item_relationships_author_data_type import (
    WorkitemsListGetResponseDataItemRelationshipsAuthorDataType,
)
from .workitems_list_get_response_data_item_relationships_categories import (
    WorkitemsListGetResponseDataItemRelationshipsCategories,
)
from .workitems_list_get_response_data_item_relationships_categories_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsCategoriesDataItem,
)
from .workitems_list_get_response_data_item_relationships_categories_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsCategoriesDataItemType,
)
from .workitems_list_get_response_data_item_relationships_categories_meta import (
    WorkitemsListGetResponseDataItemRelationshipsCategoriesMeta,
)
from .workitems_list_get_response_data_item_relationships_comments import (
    WorkitemsListGetResponseDataItemRelationshipsComments,
)
from .workitems_list_get_response_data_item_relationships_comments_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsCommentsDataItem,
)
from .workitems_list_get_response_data_item_relationships_comments_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsCommentsDataItemType,
)
from .workitems_list_get_response_data_item_relationships_comments_links import (
    WorkitemsListGetResponseDataItemRelationshipsCommentsLinks,
)
from .workitems_list_get_response_data_item_relationships_comments_meta import (
    WorkitemsListGetResponseDataItemRelationshipsCommentsMeta,
)
from .workitems_list_get_response_data_item_relationships_linked_work_items import (
    WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems,
)
from .workitems_list_get_response_data_item_relationships_linked_work_items_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsDataItem,
)
from .workitems_list_get_response_data_item_relationships_linked_work_items_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsDataItemType,
)
from .workitems_list_get_response_data_item_relationships_linked_work_items_links import (
    WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsLinks,
)
from .workitems_list_get_response_data_item_relationships_linked_work_items_meta import (
    WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsMeta,
)
from .workitems_list_get_response_data_item_relationships_module import (
    WorkitemsListGetResponseDataItemRelationshipsModule,
)
from .workitems_list_get_response_data_item_relationships_module_data import (
    WorkitemsListGetResponseDataItemRelationshipsModuleData,
)
from .workitems_list_get_response_data_item_relationships_module_data_type import (
    WorkitemsListGetResponseDataItemRelationshipsModuleDataType,
)
from .workitems_list_get_response_data_item_relationships_planned_in import (
    WorkitemsListGetResponseDataItemRelationshipsPlannedIn,
)
from .workitems_list_get_response_data_item_relationships_planned_in_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsPlannedInDataItem,
)
from .workitems_list_get_response_data_item_relationships_planned_in_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsPlannedInDataItemType,
)
from .workitems_list_get_response_data_item_relationships_planned_in_meta import (
    WorkitemsListGetResponseDataItemRelationshipsPlannedInMeta,
)
from .workitems_list_get_response_data_item_relationships_project import (
    WorkitemsListGetResponseDataItemRelationshipsProject,
)
from .workitems_list_get_response_data_item_relationships_project_data import (
    WorkitemsListGetResponseDataItemRelationshipsProjectData,
)
from .workitems_list_get_response_data_item_relationships_project_data_type import (
    WorkitemsListGetResponseDataItemRelationshipsProjectDataType,
)
from .workitems_list_get_response_data_item_relationships_watches import (
    WorkitemsListGetResponseDataItemRelationshipsWatches,
)
from .workitems_list_get_response_data_item_relationships_watches_data_item import (
    WorkitemsListGetResponseDataItemRelationshipsWatchesDataItem,
)
from .workitems_list_get_response_data_item_relationships_watches_data_item_type import (
    WorkitemsListGetResponseDataItemRelationshipsWatchesDataItemType,
)
from .workitems_list_get_response_data_item_relationships_watches_meta import (
    WorkitemsListGetResponseDataItemRelationshipsWatchesMeta,
)
from .workitems_list_get_response_data_item_type import (
    WorkitemsListGetResponseDataItemType,
)
from .workitems_list_get_response_included_item import (
    WorkitemsListGetResponseIncludedItem,
)
from .workitems_list_get_response_links import WorkitemsListGetResponseLinks
from .workitems_list_get_response_meta import WorkitemsListGetResponseMeta
from .workitems_list_post_request import WorkitemsListPostRequest
from .workitems_list_post_request_data_item import (
    WorkitemsListPostRequestDataItem,
)
from .workitems_list_post_request_data_item_attributes import (
    WorkitemsListPostRequestDataItemAttributes,
)
from .workitems_list_post_request_data_item_attributes_description import (
    WorkitemsListPostRequestDataItemAttributesDescription,
)
from .workitems_list_post_request_data_item_attributes_description_type import (
    WorkitemsListPostRequestDataItemAttributesDescriptionType,
)
from .workitems_list_post_request_data_item_attributes_hyperlinks_item import (
    WorkitemsListPostRequestDataItemAttributesHyperlinksItem,
)
from .workitems_list_post_request_data_item_relationships import (
    WorkitemsListPostRequestDataItemRelationships,
)
from .workitems_list_post_request_data_item_relationships_assignee import (
    WorkitemsListPostRequestDataItemRelationshipsAssignee,
)
from .workitems_list_post_request_data_item_relationships_assignee_data_item import (
    WorkitemsListPostRequestDataItemRelationshipsAssigneeDataItem,
)
from .workitems_list_post_request_data_item_relationships_assignee_data_item_type import (
    WorkitemsListPostRequestDataItemRelationshipsAssigneeDataItemType,
)
from .workitems_list_post_request_data_item_relationships_author import (
    WorkitemsListPostRequestDataItemRelationshipsAuthor,
)
from .workitems_list_post_request_data_item_relationships_author_data import (
    WorkitemsListPostRequestDataItemRelationshipsAuthorData,
)
from .workitems_list_post_request_data_item_relationships_author_data_type import (
    WorkitemsListPostRequestDataItemRelationshipsAuthorDataType,
)
from .workitems_list_post_request_data_item_relationships_categories import (
    WorkitemsListPostRequestDataItemRelationshipsCategories,
)
from .workitems_list_post_request_data_item_relationships_categories_data_item import (
    WorkitemsListPostRequestDataItemRelationshipsCategoriesDataItem,
)
from .workitems_list_post_request_data_item_relationships_categories_data_item_type import (
    WorkitemsListPostRequestDataItemRelationshipsCategoriesDataItemType,
)
from .workitems_list_post_request_data_item_relationships_module import (
    WorkitemsListPostRequestDataItemRelationshipsModule,
)
from .workitems_list_post_request_data_item_relationships_module_data import (
    WorkitemsListPostRequestDataItemRelationshipsModuleData,
)
from .workitems_list_post_request_data_item_relationships_module_data_type import (
    WorkitemsListPostRequestDataItemRelationshipsModuleDataType,
)
from .workitems_list_post_request_data_item_type import (
    WorkitemsListPostRequestDataItemType,
)
from .workitems_list_post_response import WorkitemsListPostResponse
from .workitems_list_post_response_data_item import (
    WorkitemsListPostResponseDataItem,
)
from .workitems_list_post_response_data_item_links import (
    WorkitemsListPostResponseDataItemLinks,
)
from .workitems_list_post_response_data_item_type import (
    WorkitemsListPostResponseDataItemType,
)
from .workitems_single_get_response import WorkitemsSingleGetResponse
from .workitems_single_get_response_data import WorkitemsSingleGetResponseData
from .workitems_single_get_response_data_attributes import (
    WorkitemsSingleGetResponseDataAttributes,
)
from .workitems_single_get_response_data_attributes_description import (
    WorkitemsSingleGetResponseDataAttributesDescription,
)
from .workitems_single_get_response_data_attributes_description_type import (
    WorkitemsSingleGetResponseDataAttributesDescriptionType,
)
from .workitems_single_get_response_data_attributes_hyperlinks_item import (
    WorkitemsSingleGetResponseDataAttributesHyperlinksItem,
)
from .workitems_single_get_response_data_links import (
    WorkitemsSingleGetResponseDataLinks,
)
from .workitems_single_get_response_data_meta import (
    WorkitemsSingleGetResponseDataMeta,
)
from .workitems_single_get_response_data_meta_errors_item import (
    WorkitemsSingleGetResponseDataMetaErrorsItem,
)
from .workitems_single_get_response_data_meta_errors_item_source import (
    WorkitemsSingleGetResponseDataMetaErrorsItemSource,
)
from .workitems_single_get_response_data_relationships import (
    WorkitemsSingleGetResponseDataRelationships,
)
from .workitems_single_get_response_data_relationships_assignee import (
    WorkitemsSingleGetResponseDataRelationshipsAssignee,
)
from .workitems_single_get_response_data_relationships_assignee_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsAssigneeDataItem,
)
from .workitems_single_get_response_data_relationships_assignee_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsAssigneeDataItemType,
)
from .workitems_single_get_response_data_relationships_assignee_meta import (
    WorkitemsSingleGetResponseDataRelationshipsAssigneeMeta,
)
from .workitems_single_get_response_data_relationships_attachments import (
    WorkitemsSingleGetResponseDataRelationshipsAttachments,
)
from .workitems_single_get_response_data_relationships_attachments_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsAttachmentsDataItem,
)
from .workitems_single_get_response_data_relationships_attachments_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsAttachmentsDataItemType,
)
from .workitems_single_get_response_data_relationships_attachments_links import (
    WorkitemsSingleGetResponseDataRelationshipsAttachmentsLinks,
)
from .workitems_single_get_response_data_relationships_attachments_meta import (
    WorkitemsSingleGetResponseDataRelationshipsAttachmentsMeta,
)
from .workitems_single_get_response_data_relationships_author import (
    WorkitemsSingleGetResponseDataRelationshipsAuthor,
)
from .workitems_single_get_response_data_relationships_author_data import (
    WorkitemsSingleGetResponseDataRelationshipsAuthorData,
)
from .workitems_single_get_response_data_relationships_author_data_type import (
    WorkitemsSingleGetResponseDataRelationshipsAuthorDataType,
)
from .workitems_single_get_response_data_relationships_categories import (
    WorkitemsSingleGetResponseDataRelationshipsCategories,
)
from .workitems_single_get_response_data_relationships_categories_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsCategoriesDataItem,
)
from .workitems_single_get_response_data_relationships_categories_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsCategoriesDataItemType,
)
from .workitems_single_get_response_data_relationships_categories_meta import (
    WorkitemsSingleGetResponseDataRelationshipsCategoriesMeta,
)
from .workitems_single_get_response_data_relationships_comments import (
    WorkitemsSingleGetResponseDataRelationshipsComments,
)
from .workitems_single_get_response_data_relationships_comments_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsCommentsDataItem,
)
from .workitems_single_get_response_data_relationships_comments_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsCommentsDataItemType,
)
from .workitems_single_get_response_data_relationships_comments_links import (
    WorkitemsSingleGetResponseDataRelationshipsCommentsLinks,
)
from .workitems_single_get_response_data_relationships_comments_meta import (
    WorkitemsSingleGetResponseDataRelationshipsCommentsMeta,
)
from .workitems_single_get_response_data_relationships_linked_work_items import (
    WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems,
)
from .workitems_single_get_response_data_relationships_linked_work_items_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsDataItem,
)
from .workitems_single_get_response_data_relationships_linked_work_items_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsDataItemType,
)
from .workitems_single_get_response_data_relationships_linked_work_items_links import (
    WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsLinks,
)
from .workitems_single_get_response_data_relationships_linked_work_items_meta import (
    WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsMeta,
)
from .workitems_single_get_response_data_relationships_module import (
    WorkitemsSingleGetResponseDataRelationshipsModule,
)
from .workitems_single_get_response_data_relationships_module_data import (
    WorkitemsSingleGetResponseDataRelationshipsModuleData,
)
from .workitems_single_get_response_data_relationships_module_data_type import (
    WorkitemsSingleGetResponseDataRelationshipsModuleDataType,
)
from .workitems_single_get_response_data_relationships_planned_in import (
    WorkitemsSingleGetResponseDataRelationshipsPlannedIn,
)
from .workitems_single_get_response_data_relationships_planned_in_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsPlannedInDataItem,
)
from .workitems_single_get_response_data_relationships_planned_in_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsPlannedInDataItemType,
)
from .workitems_single_get_response_data_relationships_planned_in_meta import (
    WorkitemsSingleGetResponseDataRelationshipsPlannedInMeta,
)
from .workitems_single_get_response_data_relationships_project import (
    WorkitemsSingleGetResponseDataRelationshipsProject,
)
from .workitems_single_get_response_data_relationships_project_data import (
    WorkitemsSingleGetResponseDataRelationshipsProjectData,
)
from .workitems_single_get_response_data_relationships_project_data_type import (
    WorkitemsSingleGetResponseDataRelationshipsProjectDataType,
)
from .workitems_single_get_response_data_relationships_watches import (
    WorkitemsSingleGetResponseDataRelationshipsWatches,
)
from .workitems_single_get_response_data_relationships_watches_data_item import (
    WorkitemsSingleGetResponseDataRelationshipsWatchesDataItem,
)
from .workitems_single_get_response_data_relationships_watches_data_item_type import (
    WorkitemsSingleGetResponseDataRelationshipsWatchesDataItemType,
)
from .workitems_single_get_response_data_relationships_watches_meta import (
    WorkitemsSingleGetResponseDataRelationshipsWatchesMeta,
)
from .workitems_single_get_response_data_type import (
    WorkitemsSingleGetResponseDataType,
)
from .workitems_single_get_response_included_item import (
    WorkitemsSingleGetResponseIncludedItem,
)
from .workitems_single_get_response_links import (
    WorkitemsSingleGetResponseLinks,
)
from .workitems_single_patch_request import WorkitemsSinglePatchRequest
from .workitems_single_patch_request_data import (
    WorkitemsSinglePatchRequestData,
)
from .workitems_single_patch_request_data_attributes import (
    WorkitemsSinglePatchRequestDataAttributes,
)
from .workitems_single_patch_request_data_attributes_description import (
    WorkitemsSinglePatchRequestDataAttributesDescription,
)
from .workitems_single_patch_request_data_attributes_description_type import (
    WorkitemsSinglePatchRequestDataAttributesDescriptionType,
)
from .workitems_single_patch_request_data_attributes_hyperlinks_item import (
    WorkitemsSinglePatchRequestDataAttributesHyperlinksItem,
)
from .workitems_single_patch_request_data_relationships import (
    WorkitemsSinglePatchRequestDataRelationships,
)
from .workitems_single_patch_request_data_relationships_assignee import (
    WorkitemsSinglePatchRequestDataRelationshipsAssignee,
)
from .workitems_single_patch_request_data_relationships_assignee_data_item import (
    WorkitemsSinglePatchRequestDataRelationshipsAssigneeDataItem,
)
from .workitems_single_patch_request_data_relationships_assignee_data_item_type import (
    WorkitemsSinglePatchRequestDataRelationshipsAssigneeDataItemType,
)
from .workitems_single_patch_request_data_relationships_categories import (
    WorkitemsSinglePatchRequestDataRelationshipsCategories,
)
from .workitems_single_patch_request_data_relationships_categories_data_item import (
    WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItem,
)
from .workitems_single_patch_request_data_relationships_categories_data_item_type import (
    WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType,
)
from .workitems_single_patch_request_data_relationships_watches import (
    WorkitemsSinglePatchRequestDataRelationshipsWatches,
)
from .workitems_single_patch_request_data_relationships_watches_data_item import (
    WorkitemsSinglePatchRequestDataRelationshipsWatchesDataItem,
)
from .workitems_single_patch_request_data_relationships_watches_data_item_type import (
    WorkitemsSinglePatchRequestDataRelationshipsWatchesDataItemType,
)
from .workitems_single_patch_request_data_type import (
    WorkitemsSinglePatchRequestDataType,
)

__all__ = (
    "BranchDocumentRequestBody",
    "CopyDocumentRequestBody",
    "DocumentAttachmentsListGetResponse",
    "DocumentAttachmentsListGetResponseDataItem",
    "DocumentAttachmentsListGetResponseDataItemAttributes",
    "DocumentAttachmentsListGetResponseDataItemLinks",
    "DocumentAttachmentsListGetResponseDataItemMeta",
    "DocumentAttachmentsListGetResponseDataItemMetaErrorsItem",
    "DocumentAttachmentsListGetResponseDataItemMetaErrorsItemSource",
    "DocumentAttachmentsListGetResponseDataItemRelationships",
    "DocumentAttachmentsListGetResponseDataItemRelationshipsAuthor",
    "DocumentAttachmentsListGetResponseDataItemRelationshipsAuthorData",
    "DocumentAttachmentsListGetResponseDataItemRelationshipsAuthorDataType",
    "DocumentAttachmentsListGetResponseDataItemRelationshipsProject",
    "DocumentAttachmentsListGetResponseDataItemRelationshipsProjectData",
    "DocumentAttachmentsListGetResponseDataItemRelationshipsProjectDataType",
    "DocumentAttachmentsListGetResponseDataItemType",
    "DocumentAttachmentsListGetResponseIncludedItem",
    "DocumentAttachmentsListGetResponseLinks",
    "DocumentAttachmentsListGetResponseMeta",
    "DocumentAttachmentsListPostRequest",
    "DocumentAttachmentsListPostRequestDataItem",
    "DocumentAttachmentsListPostRequestDataItemAttributes",
    "DocumentAttachmentsListPostRequestDataItemType",
    "DocumentAttachmentsListPostResponse",
    "DocumentAttachmentsListPostResponseDataItem",
    "DocumentAttachmentsListPostResponseDataItemLinks",
    "DocumentAttachmentsListPostResponseDataItemType",
    "DocumentAttachmentsSingleGetResponse",
    "DocumentAttachmentsSingleGetResponseData",
    "DocumentAttachmentsSingleGetResponseDataAttributes",
    "DocumentAttachmentsSingleGetResponseDataLinks",
    "DocumentAttachmentsSingleGetResponseDataMeta",
    "DocumentAttachmentsSingleGetResponseDataMetaErrorsItem",
    "DocumentAttachmentsSingleGetResponseDataMetaErrorsItemSource",
    "DocumentAttachmentsSingleGetResponseDataRelationships",
    "DocumentAttachmentsSingleGetResponseDataRelationshipsAuthor",
    "DocumentAttachmentsSingleGetResponseDataRelationshipsAuthorData",
    "DocumentAttachmentsSingleGetResponseDataRelationshipsAuthorDataType",
    "DocumentAttachmentsSingleGetResponseDataRelationshipsProject",
    "DocumentAttachmentsSingleGetResponseDataRelationshipsProjectData",
    "DocumentAttachmentsSingleGetResponseDataRelationshipsProjectDataType",
    "DocumentAttachmentsSingleGetResponseDataType",
    "DocumentAttachmentsSingleGetResponseIncludedItem",
    "DocumentAttachmentsSingleGetResponseLinks",
    "DocumentAttachmentsSinglePatchRequest",
    "DocumentAttachmentsSinglePatchRequestData",
    "DocumentAttachmentsSinglePatchRequestDataAttributes",
    "DocumentAttachmentsSinglePatchRequestDataType",
    "DocumentCommentsListGetResponse",
    "DocumentCommentsListGetResponseDataItem",
    "DocumentCommentsListGetResponseDataItemAttributes",
    "DocumentCommentsListGetResponseDataItemAttributesText",
    "DocumentCommentsListGetResponseDataItemAttributesTextType",
    "DocumentCommentsListGetResponseDataItemLinks",
    "DocumentCommentsListGetResponseDataItemMeta",
    "DocumentCommentsListGetResponseDataItemMetaErrorsItem",
    "DocumentCommentsListGetResponseDataItemMetaErrorsItemSource",
    "DocumentCommentsListGetResponseDataItemRelationships",
    "DocumentCommentsListGetResponseDataItemRelationshipsAuthor",
    "DocumentCommentsListGetResponseDataItemRelationshipsAuthorData",
    "DocumentCommentsListGetResponseDataItemRelationshipsAuthorDataType",
    "DocumentCommentsListGetResponseDataItemRelationshipsChildComments",
    "DocumentCommentsListGetResponseDataItemRelationshipsChildCommentsDataItem",
    "DocumentCommentsListGetResponseDataItemRelationshipsChildCommentsDataItemType",
    "DocumentCommentsListGetResponseDataItemRelationshipsChildCommentsMeta",
    "DocumentCommentsListGetResponseDataItemRelationshipsParentComment",
    "DocumentCommentsListGetResponseDataItemRelationshipsParentCommentData",
    "DocumentCommentsListGetResponseDataItemRelationshipsParentCommentDataType",
    "DocumentCommentsListGetResponseDataItemRelationshipsProject",
    "DocumentCommentsListGetResponseDataItemRelationshipsProjectData",
    "DocumentCommentsListGetResponseDataItemRelationshipsProjectDataType",
    "DocumentCommentsListGetResponseDataItemType",
    "DocumentCommentsListGetResponseIncludedItem",
    "DocumentCommentsListGetResponseLinks",
    "DocumentCommentsListGetResponseMeta",
    "DocumentCommentsListPostRequest",
    "DocumentCommentsListPostRequestDataItem",
    "DocumentCommentsListPostRequestDataItemAttributes",
    "DocumentCommentsListPostRequestDataItemAttributesText",
    "DocumentCommentsListPostRequestDataItemAttributesTextType",
    "DocumentCommentsListPostRequestDataItemRelationships",
    "DocumentCommentsListPostRequestDataItemRelationshipsAuthor",
    "DocumentCommentsListPostRequestDataItemRelationshipsAuthorData",
    "DocumentCommentsListPostRequestDataItemRelationshipsAuthorDataType",
    "DocumentCommentsListPostRequestDataItemRelationshipsParentComment",
    "DocumentCommentsListPostRequestDataItemRelationshipsParentCommentData",
    "DocumentCommentsListPostRequestDataItemRelationshipsParentCommentDataType",
    "DocumentCommentsListPostRequestDataItemType",
    "DocumentCommentsListPostResponse",
    "DocumentCommentsListPostResponseDataItem",
    "DocumentCommentsListPostResponseDataItemLinks",
    "DocumentCommentsListPostResponseDataItemType",
    "DocumentCommentsSingleGetResponse",
    "DocumentCommentsSingleGetResponseData",
    "DocumentCommentsSingleGetResponseDataAttributes",
    "DocumentCommentsSingleGetResponseDataAttributesText",
    "DocumentCommentsSingleGetResponseDataAttributesTextType",
    "DocumentCommentsSingleGetResponseDataLinks",
    "DocumentCommentsSingleGetResponseDataMeta",
    "DocumentCommentsSingleGetResponseDataMetaErrorsItem",
    "DocumentCommentsSingleGetResponseDataMetaErrorsItemSource",
    "DocumentCommentsSingleGetResponseDataRelationships",
    "DocumentCommentsSingleGetResponseDataRelationshipsAuthor",
    "DocumentCommentsSingleGetResponseDataRelationshipsAuthorData",
    "DocumentCommentsSingleGetResponseDataRelationshipsAuthorDataType",
    "DocumentCommentsSingleGetResponseDataRelationshipsChildComments",
    "DocumentCommentsSingleGetResponseDataRelationshipsChildCommentsDataItem",
    "DocumentCommentsSingleGetResponseDataRelationshipsChildCommentsDataItemType",
    "DocumentCommentsSingleGetResponseDataRelationshipsChildCommentsMeta",
    "DocumentCommentsSingleGetResponseDataRelationshipsParentComment",
    "DocumentCommentsSingleGetResponseDataRelationshipsParentCommentData",
    "DocumentCommentsSingleGetResponseDataRelationshipsParentCommentDataType",
    "DocumentCommentsSingleGetResponseDataRelationshipsProject",
    "DocumentCommentsSingleGetResponseDataRelationshipsProjectData",
    "DocumentCommentsSingleGetResponseDataRelationshipsProjectDataType",
    "DocumentCommentsSingleGetResponseDataType",
    "DocumentCommentsSingleGetResponseIncludedItem",
    "DocumentCommentsSingleGetResponseLinks",
    "DocumentCommentsSinglePatchRequest",
    "DocumentCommentsSinglePatchRequestData",
    "DocumentCommentsSinglePatchRequestDataAttributes",
    "DocumentCommentsSinglePatchRequestDataType",
    "DocumentPartsListGetResponse",
    "DocumentPartsListGetResponseDataItem",
    "DocumentPartsListGetResponseDataItemAttributes",
    "DocumentPartsListGetResponseDataItemLinks",
    "DocumentPartsListGetResponseDataItemMeta",
    "DocumentPartsListGetResponseDataItemMetaErrorsItem",
    "DocumentPartsListGetResponseDataItemMetaErrorsItemSource",
    "DocumentPartsListGetResponseDataItemRelationships",
    "DocumentPartsListGetResponseDataItemRelationshipsNextPart",
    "DocumentPartsListGetResponseDataItemRelationshipsNextPartData",
    "DocumentPartsListGetResponseDataItemRelationshipsNextPartDataType",
    "DocumentPartsListGetResponseDataItemRelationshipsPreviousPart",
    "DocumentPartsListGetResponseDataItemRelationshipsPreviousPartData",
    "DocumentPartsListGetResponseDataItemRelationshipsPreviousPartDataType",
    "DocumentPartsListGetResponseDataItemRelationshipsWorkItem",
    "DocumentPartsListGetResponseDataItemRelationshipsWorkItemData",
    "DocumentPartsListGetResponseDataItemRelationshipsWorkItemDataType",
    "DocumentPartsListGetResponseDataItemType",
    "DocumentPartsListGetResponseIncludedItem",
    "DocumentPartsListGetResponseLinks",
    "DocumentPartsListGetResponseMeta",
    "DocumentPartsListPostRequest",
    "DocumentPartsListPostRequestDataItem",
    "DocumentPartsListPostRequestDataItemAttributes",
    "DocumentPartsListPostRequestDataItemRelationships",
    "DocumentPartsListPostRequestDataItemRelationshipsNextPart",
    "DocumentPartsListPostRequestDataItemRelationshipsNextPartData",
    "DocumentPartsListPostRequestDataItemRelationshipsNextPartDataType",
    "DocumentPartsListPostRequestDataItemRelationshipsPreviousPart",
    "DocumentPartsListPostRequestDataItemRelationshipsPreviousPartData",
    "DocumentPartsListPostRequestDataItemRelationshipsPreviousPartDataType",
    "DocumentPartsListPostRequestDataItemRelationshipsWorkItem",
    "DocumentPartsListPostRequestDataItemRelationshipsWorkItemData",
    "DocumentPartsListPostRequestDataItemRelationshipsWorkItemDataType",
    "DocumentPartsListPostRequestDataItemType",
    "DocumentPartsListPostResponse",
    "DocumentPartsListPostResponseDataItem",
    "DocumentPartsListPostResponseDataItemLinks",
    "DocumentPartsListPostResponseDataItemType",
    "DocumentPartsSingleGetResponse",
    "DocumentPartsSingleGetResponseData",
    "DocumentPartsSingleGetResponseDataAttributes",
    "DocumentPartsSingleGetResponseDataLinks",
    "DocumentPartsSingleGetResponseDataMeta",
    "DocumentPartsSingleGetResponseDataMetaErrorsItem",
    "DocumentPartsSingleGetResponseDataMetaErrorsItemSource",
    "DocumentPartsSingleGetResponseDataRelationships",
    "DocumentPartsSingleGetResponseDataRelationshipsNextPart",
    "DocumentPartsSingleGetResponseDataRelationshipsNextPartData",
    "DocumentPartsSingleGetResponseDataRelationshipsNextPartDataType",
    "DocumentPartsSingleGetResponseDataRelationshipsPreviousPart",
    "DocumentPartsSingleGetResponseDataRelationshipsPreviousPartData",
    "DocumentPartsSingleGetResponseDataRelationshipsPreviousPartDataType",
    "DocumentPartsSingleGetResponseDataRelationshipsWorkItem",
    "DocumentPartsSingleGetResponseDataRelationshipsWorkItemData",
    "DocumentPartsSingleGetResponseDataRelationshipsWorkItemDataType",
    "DocumentPartsSingleGetResponseDataType",
    "DocumentPartsSingleGetResponseIncludedItem",
    "DocumentPartsSingleGetResponseLinks",
    "DocumentsListPostRequest",
    "DocumentsListPostRequestDataItem",
    "DocumentsListPostRequestDataItemAttributes",
    "DocumentsListPostRequestDataItemAttributesHomePageContent",
    "DocumentsListPostRequestDataItemAttributesHomePageContentType",
    "DocumentsListPostRequestDataItemAttributesOutlineNumbering",
    "DocumentsListPostRequestDataItemAttributesRenderingLayoutsItem",
    "DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem",
    "DocumentsListPostRequestDataItemType",
    "DocumentsListPostResponse",
    "DocumentsListPostResponseDataItem",
    "DocumentsListPostResponseDataItemLinks",
    "DocumentsListPostResponseDataItemType",
    "DocumentsSingleGetResponse",
    "DocumentsSingleGetResponseData",
    "DocumentsSingleGetResponseDataAttributes",
    "DocumentsSingleGetResponseDataAttributesHomePageContent",
    "DocumentsSingleGetResponseDataAttributesHomePageContentType",
    "DocumentsSingleGetResponseDataAttributesOutlineNumbering",
    "DocumentsSingleGetResponseDataAttributesRenderingLayoutsItem",
    "DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem",
    "DocumentsSingleGetResponseDataLinks",
    "DocumentsSingleGetResponseDataMeta",
    "DocumentsSingleGetResponseDataMetaErrorsItem",
    "DocumentsSingleGetResponseDataMetaErrorsItemSource",
    "DocumentsSingleGetResponseDataRelationships",
    "DocumentsSingleGetResponseDataRelationshipsAttachments",
    "DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem",
    "DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItemType",
    "DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks",
    "DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta",
    "DocumentsSingleGetResponseDataRelationshipsAuthor",
    "DocumentsSingleGetResponseDataRelationshipsAuthorData",
    "DocumentsSingleGetResponseDataRelationshipsAuthorDataType",
    "DocumentsSingleGetResponseDataRelationshipsBranchedFrom",
    "DocumentsSingleGetResponseDataRelationshipsBranchedFromData",
    "DocumentsSingleGetResponseDataRelationshipsBranchedFromDataType",
    "DocumentsSingleGetResponseDataRelationshipsComments",
    "DocumentsSingleGetResponseDataRelationshipsCommentsDataItem",
    "DocumentsSingleGetResponseDataRelationshipsCommentsDataItemType",
    "DocumentsSingleGetResponseDataRelationshipsCommentsLinks",
    "DocumentsSingleGetResponseDataRelationshipsCommentsMeta",
    "DocumentsSingleGetResponseDataRelationshipsDerivedFrom",
    "DocumentsSingleGetResponseDataRelationshipsDerivedFromData",
    "DocumentsSingleGetResponseDataRelationshipsDerivedFromDataType",
    "DocumentsSingleGetResponseDataRelationshipsProject",
    "DocumentsSingleGetResponseDataRelationshipsProjectData",
    "DocumentsSingleGetResponseDataRelationshipsProjectDataType",
    "DocumentsSingleGetResponseDataRelationshipsUpdatedBy",
    "DocumentsSingleGetResponseDataRelationshipsUpdatedByData",
    "DocumentsSingleGetResponseDataRelationshipsUpdatedByDataType",
    "DocumentsSingleGetResponseDataRelationshipsVariant",
    "DocumentsSingleGetResponseDataRelationshipsVariantData",
    "DocumentsSingleGetResponseDataRelationshipsVariantDataType",
    "DocumentsSingleGetResponseDataType",
    "DocumentsSingleGetResponseIncludedItem",
    "DocumentsSingleGetResponseLinks",
    "DocumentsSinglePatchRequest",
    "DocumentsSinglePatchRequestData",
    "DocumentsSinglePatchRequestDataAttributes",
    "DocumentsSinglePatchRequestDataAttributesHomePageContent",
    "DocumentsSinglePatchRequestDataAttributesHomePageContentType",
    "DocumentsSinglePatchRequestDataAttributesOutlineNumbering",
    "DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem",
    "DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItemPropertiesItem",
    "DocumentsSinglePatchRequestDataType",
    "DocumentsSinglePostResponse",
    "DocumentsSinglePostResponseData",
    "DocumentsSinglePostResponseDataAttributes",
    "DocumentsSinglePostResponseDataAttributesHomePageContent",
    "DocumentsSinglePostResponseDataAttributesHomePageContentType",
    "DocumentsSinglePostResponseDataAttributesOutlineNumbering",
    "DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem",
    "DocumentsSinglePostResponseDataAttributesRenderingLayoutsItemPropertiesItem",
    "DocumentsSinglePostResponseDataType",
    "EnumerationsListPostRequest",
    "EnumerationsListPostRequestDataItem",
    "EnumerationsListPostRequestDataItemAttributes",
    "EnumerationsListPostRequestDataItemAttributesOptionsItem",
    "EnumerationsListPostRequestDataItemType",
    "EnumerationsListPostResponse",
    "EnumerationsListPostResponseDataItem",
    "EnumerationsListPostResponseDataItemLinks",
    "EnumerationsListPostResponseDataItemType",
    "EnumerationsSingleGetResponse",
    "EnumerationsSingleGetResponseData",
    "EnumerationsSingleGetResponseDataAttributes",
    "EnumerationsSingleGetResponseDataAttributesOptionsItem",
    "EnumerationsSingleGetResponseDataLinks",
    "EnumerationsSingleGetResponseDataMeta",
    "EnumerationsSingleGetResponseDataMetaErrorsItem",
    "EnumerationsSingleGetResponseDataMetaErrorsItemSource",
    "EnumerationsSingleGetResponseDataType",
    "EnumerationsSingleGetResponseIncludedItem",
    "EnumerationsSingleGetResponseLinks",
    "EnumerationsSinglePatchRequest",
    "EnumerationsSinglePatchRequestData",
    "EnumerationsSinglePatchRequestDataAttributes",
    "EnumerationsSinglePatchRequestDataAttributesOptionsItem",
    "EnumerationsSinglePatchRequestDataType",
    "EnumOptionsActionResponseBody",
    "EnumOptionsActionResponseBodyDataItem",
    "EnumOptionsActionResponseBodyLinks",
    "EnumOptionsActionResponseBodyMeta",
    "Errors",
    "ErrorsErrorsItem",
    "ErrorsErrorsItemSource",
    "GlobalrolesSingleGetResponse",
    "GlobalrolesSingleGetResponseData",
    "GlobalrolesSingleGetResponseDataLinks",
    "GlobalrolesSingleGetResponseDataMeta",
    "GlobalrolesSingleGetResponseDataMetaErrorsItem",
    "GlobalrolesSingleGetResponseDataMetaErrorsItemSource",
    "GlobalrolesSingleGetResponseDataRelationships",
    "GlobalrolesSingleGetResponseDataRelationshipsUsers",
    "GlobalrolesSingleGetResponseDataRelationshipsUsersDataItem",
    "GlobalrolesSingleGetResponseDataRelationshipsUsersDataItemType",
    "GlobalrolesSingleGetResponseDataRelationshipsUsersMeta",
    "GlobalrolesSingleGetResponseDataType",
    "GlobalrolesSingleGetResponseIncludedItem",
    "GlobalrolesSingleGetResponseLinks",
    "IconsListGetResponse",
    "IconsListGetResponseDataItem",
    "IconsListGetResponseDataItemAttributes",
    "IconsListGetResponseDataItemLinks",
    "IconsListGetResponseDataItemMeta",
    "IconsListGetResponseDataItemMetaErrorsItem",
    "IconsListGetResponseDataItemMetaErrorsItemSource",
    "IconsListGetResponseDataItemType",
    "IconsListGetResponseIncludedItem",
    "IconsListGetResponseLinks",
    "IconsListGetResponseMeta",
    "IconsSingleGetResponse",
    "IconsSingleGetResponseData",
    "IconsSingleGetResponseDataAttributes",
    "IconsSingleGetResponseDataLinks",
    "IconsSingleGetResponseDataMeta",
    "IconsSingleGetResponseDataMetaErrorsItem",
    "IconsSingleGetResponseDataMetaErrorsItemSource",
    "IconsSingleGetResponseDataType",
    "IconsSingleGetResponseIncludedItem",
    "IconsSingleGetResponseLinks",
    "LinkedworkitemsListDeleteRequest",
    "LinkedworkitemsListDeleteRequestDataItem",
    "LinkedworkitemsListDeleteRequestDataItemType",
    "LinkedworkitemsListGetResponse",
    "LinkedworkitemsListGetResponseDataItem",
    "LinkedworkitemsListGetResponseDataItemAttributes",
    "LinkedworkitemsListGetResponseDataItemLinks",
    "LinkedworkitemsListGetResponseDataItemMeta",
    "LinkedworkitemsListGetResponseDataItemMetaErrorsItem",
    "LinkedworkitemsListGetResponseDataItemMetaErrorsItemSource",
    "LinkedworkitemsListGetResponseDataItemRelationships",
    "LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem",
    "LinkedworkitemsListGetResponseDataItemRelationshipsWorkItemData",
    "LinkedworkitemsListGetResponseDataItemRelationshipsWorkItemDataType",
    "LinkedworkitemsListGetResponseDataItemType",
    "LinkedworkitemsListGetResponseIncludedItem",
    "LinkedworkitemsListGetResponseLinks",
    "LinkedworkitemsListGetResponseMeta",
    "LinkedworkitemsListPostRequest",
    "LinkedworkitemsListPostRequestDataItem",
    "LinkedworkitemsListPostRequestDataItemAttributes",
    "LinkedworkitemsListPostRequestDataItemRelationships",
    "LinkedworkitemsListPostRequestDataItemRelationshipsWorkItem",
    "LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemData",
    "LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemDataType",
    "LinkedworkitemsListPostRequestDataItemType",
    "LinkedworkitemsListPostResponse",
    "LinkedworkitemsListPostResponseDataItem",
    "LinkedworkitemsListPostResponseDataItemLinks",
    "LinkedworkitemsListPostResponseDataItemType",
    "LinkedworkitemsSingleGetResponse",
    "LinkedworkitemsSingleGetResponseData",
    "LinkedworkitemsSingleGetResponseDataAttributes",
    "LinkedworkitemsSingleGetResponseDataLinks",
    "LinkedworkitemsSingleGetResponseDataMeta",
    "LinkedworkitemsSingleGetResponseDataMetaErrorsItem",
    "LinkedworkitemsSingleGetResponseDataMetaErrorsItemSource",
    "LinkedworkitemsSingleGetResponseDataRelationships",
    "LinkedworkitemsSingleGetResponseDataRelationshipsWorkItem",
    "LinkedworkitemsSingleGetResponseDataRelationshipsWorkItemData",
    "LinkedworkitemsSingleGetResponseDataRelationshipsWorkItemDataType",
    "LinkedworkitemsSingleGetResponseDataType",
    "LinkedworkitemsSingleGetResponseIncludedItem",
    "LinkedworkitemsSingleGetResponseLinks",
    "LinkedworkitemsSinglePatchRequest",
    "LinkedworkitemsSinglePatchRequestData",
    "LinkedworkitemsSinglePatchRequestDataAttributes",
    "LinkedworkitemsSinglePatchRequestDataType",
    "MoveWorkItemToDocumentRequestBody",
    "PageAttachmentsListPostRequest",
    "PageAttachmentsListPostRequestDataItem",
    "PageAttachmentsListPostRequestDataItemAttributes",
    "PageAttachmentsListPostRequestDataItemType",
    "PageAttachmentsListPostResponse",
    "PageAttachmentsListPostResponseDataItem",
    "PageAttachmentsListPostResponseDataItemLinks",
    "PageAttachmentsListPostResponseDataItemType",
    "PageAttachmentsSingleGetResponse",
    "PageAttachmentsSingleGetResponseData",
    "PageAttachmentsSingleGetResponseDataAttributes",
    "PageAttachmentsSingleGetResponseDataLinks",
    "PageAttachmentsSingleGetResponseDataMeta",
    "PageAttachmentsSingleGetResponseDataMetaErrorsItem",
    "PageAttachmentsSingleGetResponseDataMetaErrorsItemSource",
    "PageAttachmentsSingleGetResponseDataRelationships",
    "PageAttachmentsSingleGetResponseDataRelationshipsAuthor",
    "PageAttachmentsSingleGetResponseDataRelationshipsAuthorData",
    "PageAttachmentsSingleGetResponseDataRelationshipsAuthorDataType",
    "PageAttachmentsSingleGetResponseDataRelationshipsProject",
    "PageAttachmentsSingleGetResponseDataRelationshipsProjectData",
    "PageAttachmentsSingleGetResponseDataRelationshipsProjectDataType",
    "PageAttachmentsSingleGetResponseDataType",
    "PageAttachmentsSingleGetResponseIncludedItem",
    "PageAttachmentsSingleGetResponseLinks",
    "PagesSingleGetResponse",
    "PagesSingleGetResponseData",
    "PagesSingleGetResponseDataAttributes",
    "PagesSingleGetResponseDataLinks",
    "PagesSingleGetResponseDataMeta",
    "PagesSingleGetResponseDataMetaErrorsItem",
    "PagesSingleGetResponseDataMetaErrorsItemSource",
    "PagesSingleGetResponseDataRelationships",
    "PagesSingleGetResponseDataRelationshipsAttachments",
    "PagesSingleGetResponseDataRelationshipsAttachmentsDataItem",
    "PagesSingleGetResponseDataRelationshipsAttachmentsDataItemType",
    "PagesSingleGetResponseDataRelationshipsAttachmentsMeta",
    "PagesSingleGetResponseDataRelationshipsAuthor",
    "PagesSingleGetResponseDataRelationshipsAuthorData",
    "PagesSingleGetResponseDataRelationshipsAuthorDataType",
    "PagesSingleGetResponseDataRelationshipsProject",
    "PagesSingleGetResponseDataRelationshipsProjectData",
    "PagesSingleGetResponseDataRelationshipsProjectDataType",
    "PagesSingleGetResponseDataRelationshipsUpdatedBy",
    "PagesSingleGetResponseDataRelationshipsUpdatedByData",
    "PagesSingleGetResponseDataRelationshipsUpdatedByDataType",
    "PagesSingleGetResponseDataType",
    "PagesSingleGetResponseIncludedItem",
    "PagesSingleGetResponseLinks",
    "PagesSinglePatchRequest",
    "PagesSinglePatchRequestData",
    "PagesSinglePatchRequestDataAttributes",
    "PagesSinglePatchRequestDataType",
    "Pagination",
    "PatchDocumentAttachmentsRequestBody",
    "PatchWorkItemAttachmentsRequestBody",
    "PostDocumentAttachmentsRequestBody",
    "PostPageAttachmentsRequestBody",
    "PostWorkItemAttachmentsRequestBody",
    "ProjectsListGetResponse",
    "ProjectsListGetResponseDataItem",
    "ProjectsListGetResponseDataItemAttributes",
    "ProjectsListGetResponseDataItemAttributesDescription",
    "ProjectsListGetResponseDataItemAttributesDescriptionType",
    "ProjectsListGetResponseDataItemLinks",
    "ProjectsListGetResponseDataItemMeta",
    "ProjectsListGetResponseDataItemMetaErrorsItem",
    "ProjectsListGetResponseDataItemMetaErrorsItemSource",
    "ProjectsListGetResponseDataItemRelationships",
    "ProjectsListGetResponseDataItemRelationshipsLead",
    "ProjectsListGetResponseDataItemRelationshipsLeadData",
    "ProjectsListGetResponseDataItemRelationshipsLeadDataType",
    "ProjectsListGetResponseDataItemType",
    "ProjectsListGetResponseIncludedItem",
    "ProjectsListGetResponseLinks",
    "ProjectsListGetResponseMeta",
    "ProjectsSingleGetResponse",
    "ProjectsSingleGetResponseData",
    "ProjectsSingleGetResponseDataAttributes",
    "ProjectsSingleGetResponseDataAttributesDescription",
    "ProjectsSingleGetResponseDataAttributesDescriptionType",
    "ProjectsSingleGetResponseDataLinks",
    "ProjectsSingleGetResponseDataMeta",
    "ProjectsSingleGetResponseDataMetaErrorsItem",
    "ProjectsSingleGetResponseDataMetaErrorsItemSource",
    "ProjectsSingleGetResponseDataRelationships",
    "ProjectsSingleGetResponseDataRelationshipsLead",
    "ProjectsSingleGetResponseDataRelationshipsLeadData",
    "ProjectsSingleGetResponseDataRelationshipsLeadDataType",
    "ProjectsSingleGetResponseDataType",
    "ProjectsSingleGetResponseIncludedItem",
    "ProjectsSingleGetResponseLinks",
    "ResourceReference",
    "SetLicenseRequestBody",
    "SetLicenseRequestBodyLicense",
    "SparseFields",
    "UsergroupsSingleGetResponse",
    "UsergroupsSingleGetResponseData",
    "UsergroupsSingleGetResponseDataAttributes",
    "UsergroupsSingleGetResponseDataAttributesDescription",
    "UsergroupsSingleGetResponseDataAttributesDescriptionType",
    "UsergroupsSingleGetResponseDataLinks",
    "UsergroupsSingleGetResponseDataMeta",
    "UsergroupsSingleGetResponseDataMetaErrorsItem",
    "UsergroupsSingleGetResponseDataMetaErrorsItemSource",
    "UsergroupsSingleGetResponseDataRelationships",
    "UsergroupsSingleGetResponseDataRelationshipsGlobalRoles",
    "UsergroupsSingleGetResponseDataRelationshipsGlobalRolesDataItem",
    "UsergroupsSingleGetResponseDataRelationshipsGlobalRolesDataItemType",
    "UsergroupsSingleGetResponseDataRelationshipsGlobalRolesMeta",
    "UsergroupsSingleGetResponseDataRelationshipsProjectRoles",
    "UsergroupsSingleGetResponseDataRelationshipsProjectRolesDataItem",
    "UsergroupsSingleGetResponseDataRelationshipsProjectRolesDataItemType",
    "UsergroupsSingleGetResponseDataRelationshipsProjectRolesMeta",
    "UsergroupsSingleGetResponseDataRelationshipsUsers",
    "UsergroupsSingleGetResponseDataRelationshipsUsersDataItem",
    "UsergroupsSingleGetResponseDataRelationshipsUsersDataItemType",
    "UsergroupsSingleGetResponseDataRelationshipsUsersMeta",
    "UsergroupsSingleGetResponseDataType",
    "UsergroupsSingleGetResponseIncludedItem",
    "UsergroupsSingleGetResponseLinks",
    "UsersListGetResponse",
    "UsersListGetResponseDataItem",
    "UsersListGetResponseDataItemAttributes",
    "UsersListGetResponseDataItemAttributesDescription",
    "UsersListGetResponseDataItemAttributesDescriptionType",
    "UsersListGetResponseDataItemLinks",
    "UsersListGetResponseDataItemMeta",
    "UsersListGetResponseDataItemMetaErrorsItem",
    "UsersListGetResponseDataItemMetaErrorsItemSource",
    "UsersListGetResponseDataItemRelationships",
    "UsersListGetResponseDataItemRelationshipsGlobalRoles",
    "UsersListGetResponseDataItemRelationshipsGlobalRolesDataItem",
    "UsersListGetResponseDataItemRelationshipsGlobalRolesDataItemType",
    "UsersListGetResponseDataItemRelationshipsGlobalRolesMeta",
    "UsersListGetResponseDataItemRelationshipsProjectRoles",
    "UsersListGetResponseDataItemRelationshipsProjectRolesDataItem",
    "UsersListGetResponseDataItemRelationshipsProjectRolesDataItemType",
    "UsersListGetResponseDataItemRelationshipsProjectRolesMeta",
    "UsersListGetResponseDataItemRelationshipsUserGroups",
    "UsersListGetResponseDataItemRelationshipsUserGroupsDataItem",
    "UsersListGetResponseDataItemRelationshipsUserGroupsDataItemType",
    "UsersListGetResponseDataItemRelationshipsUserGroupsMeta",
    "UsersListGetResponseDataItemType",
    "UsersListGetResponseIncludedItem",
    "UsersListGetResponseLinks",
    "UsersListGetResponseMeta",
    "UsersListPostRequest",
    "UsersListPostRequestDataItem",
    "UsersListPostRequestDataItemAttributes",
    "UsersListPostRequestDataItemAttributesDescription",
    "UsersListPostRequestDataItemAttributesDescriptionType",
    "UsersListPostRequestDataItemRelationships",
    "UsersListPostRequestDataItemRelationshipsGlobalRoles",
    "UsersListPostRequestDataItemRelationshipsGlobalRolesDataItem",
    "UsersListPostRequestDataItemRelationshipsGlobalRolesDataItemType",
    "UsersListPostRequestDataItemRelationshipsProjectRoles",
    "UsersListPostRequestDataItemRelationshipsProjectRolesDataItem",
    "UsersListPostRequestDataItemRelationshipsProjectRolesDataItemType",
    "UsersListPostRequestDataItemRelationshipsUserGroups",
    "UsersListPostRequestDataItemRelationshipsUserGroupsDataItem",
    "UsersListPostRequestDataItemRelationshipsUserGroupsDataItemType",
    "UsersListPostRequestDataItemType",
    "UsersListPostResponse",
    "UsersListPostResponseDataItem",
    "UsersListPostResponseDataItemLinks",
    "UsersListPostResponseDataItemType",
    "UsersSingleGetResponse",
    "UsersSingleGetResponseData",
    "UsersSingleGetResponseDataAttributes",
    "UsersSingleGetResponseDataAttributesDescription",
    "UsersSingleGetResponseDataAttributesDescriptionType",
    "UsersSingleGetResponseDataLinks",
    "UsersSingleGetResponseDataMeta",
    "UsersSingleGetResponseDataMetaErrorsItem",
    "UsersSingleGetResponseDataMetaErrorsItemSource",
    "UsersSingleGetResponseDataRelationships",
    "UsersSingleGetResponseDataRelationshipsGlobalRoles",
    "UsersSingleGetResponseDataRelationshipsGlobalRolesDataItem",
    "UsersSingleGetResponseDataRelationshipsGlobalRolesDataItemType",
    "UsersSingleGetResponseDataRelationshipsGlobalRolesMeta",
    "UsersSingleGetResponseDataRelationshipsProjectRoles",
    "UsersSingleGetResponseDataRelationshipsProjectRolesDataItem",
    "UsersSingleGetResponseDataRelationshipsProjectRolesDataItemType",
    "UsersSingleGetResponseDataRelationshipsProjectRolesMeta",
    "UsersSingleGetResponseDataRelationshipsUserGroups",
    "UsersSingleGetResponseDataRelationshipsUserGroupsDataItem",
    "UsersSingleGetResponseDataRelationshipsUserGroupsDataItemType",
    "UsersSingleGetResponseDataRelationshipsUserGroupsMeta",
    "UsersSingleGetResponseDataType",
    "UsersSingleGetResponseIncludedItem",
    "UsersSingleGetResponseLinks",
    "UsersSinglePatchRequest",
    "UsersSinglePatchRequestData",
    "UsersSinglePatchRequestDataAttributes",
    "UsersSinglePatchRequestDataAttributesDescription",
    "UsersSinglePatchRequestDataAttributesDescriptionType",
    "UsersSinglePatchRequestDataRelationships",
    "UsersSinglePatchRequestDataRelationshipsGlobalRoles",
    "UsersSinglePatchRequestDataRelationshipsGlobalRolesDataItem",
    "UsersSinglePatchRequestDataRelationshipsGlobalRolesDataItemType",
    "UsersSinglePatchRequestDataRelationshipsProjectRoles",
    "UsersSinglePatchRequestDataRelationshipsProjectRolesDataItem",
    "UsersSinglePatchRequestDataRelationshipsProjectRolesDataItemType",
    "UsersSinglePatchRequestDataRelationshipsUserGroups",
    "UsersSinglePatchRequestDataRelationshipsUserGroupsDataItem",
    "UsersSinglePatchRequestDataRelationshipsUserGroupsDataItemType",
    "UsersSinglePatchRequestDataType",
    "WorkitemAttachmentsListGetResponse",
    "WorkitemAttachmentsListGetResponseDataItem",
    "WorkitemAttachmentsListGetResponseDataItemAttributes",
    "WorkitemAttachmentsListGetResponseDataItemLinks",
    "WorkitemAttachmentsListGetResponseDataItemMeta",
    "WorkitemAttachmentsListGetResponseDataItemMetaErrorsItem",
    "WorkitemAttachmentsListGetResponseDataItemMetaErrorsItemSource",
    "WorkitemAttachmentsListGetResponseDataItemRelationships",
    "WorkitemAttachmentsListGetResponseDataItemRelationshipsAuthor",
    "WorkitemAttachmentsListGetResponseDataItemRelationshipsAuthorData",
    "WorkitemAttachmentsListGetResponseDataItemRelationshipsAuthorDataType",
    "WorkitemAttachmentsListGetResponseDataItemRelationshipsProject",
    "WorkitemAttachmentsListGetResponseDataItemRelationshipsProjectData",
    "WorkitemAttachmentsListGetResponseDataItemRelationshipsProjectDataType",
    "WorkitemAttachmentsListGetResponseDataItemType",
    "WorkitemAttachmentsListGetResponseIncludedItem",
    "WorkitemAttachmentsListGetResponseLinks",
    "WorkitemAttachmentsListGetResponseMeta",
    "WorkitemAttachmentsListPostRequest",
    "WorkitemAttachmentsListPostRequestDataItem",
    "WorkitemAttachmentsListPostRequestDataItemAttributes",
    "WorkitemAttachmentsListPostRequestDataItemType",
    "WorkitemAttachmentsListPostResponse",
    "WorkitemAttachmentsListPostResponseDataItem",
    "WorkitemAttachmentsListPostResponseDataItemLinks",
    "WorkitemAttachmentsListPostResponseDataItemType",
    "WorkitemAttachmentsSingleGetResponse",
    "WorkitemAttachmentsSingleGetResponseData",
    "WorkitemAttachmentsSingleGetResponseDataAttributes",
    "WorkitemAttachmentsSingleGetResponseDataLinks",
    "WorkitemAttachmentsSingleGetResponseDataMeta",
    "WorkitemAttachmentsSingleGetResponseDataMetaErrorsItem",
    "WorkitemAttachmentsSingleGetResponseDataMetaErrorsItemSource",
    "WorkitemAttachmentsSingleGetResponseDataRelationships",
    "WorkitemAttachmentsSingleGetResponseDataRelationshipsAuthor",
    "WorkitemAttachmentsSingleGetResponseDataRelationshipsAuthorData",
    "WorkitemAttachmentsSingleGetResponseDataRelationshipsAuthorDataType",
    "WorkitemAttachmentsSingleGetResponseDataRelationshipsProject",
    "WorkitemAttachmentsSingleGetResponseDataRelationshipsProjectData",
    "WorkitemAttachmentsSingleGetResponseDataRelationshipsProjectDataType",
    "WorkitemAttachmentsSingleGetResponseDataType",
    "WorkitemAttachmentsSingleGetResponseIncludedItem",
    "WorkitemAttachmentsSingleGetResponseLinks",
    "WorkitemAttachmentsSinglePatchRequest",
    "WorkitemAttachmentsSinglePatchRequestData",
    "WorkitemAttachmentsSinglePatchRequestDataAttributes",
    "WorkitemAttachmentsSinglePatchRequestDataType",
    "WorkitemCommentsListGetResponse",
    "WorkitemCommentsListGetResponseDataItem",
    "WorkitemCommentsListGetResponseDataItemAttributes",
    "WorkitemCommentsListGetResponseDataItemAttributesText",
    "WorkitemCommentsListGetResponseDataItemAttributesTextType",
    "WorkitemCommentsListGetResponseDataItemLinks",
    "WorkitemCommentsListGetResponseDataItemMeta",
    "WorkitemCommentsListGetResponseDataItemMetaErrorsItem",
    "WorkitemCommentsListGetResponseDataItemMetaErrorsItemSource",
    "WorkitemCommentsListGetResponseDataItemRelationships",
    "WorkitemCommentsListGetResponseDataItemRelationshipsAuthor",
    "WorkitemCommentsListGetResponseDataItemRelationshipsAuthorData",
    "WorkitemCommentsListGetResponseDataItemRelationshipsAuthorDataType",
    "WorkitemCommentsListGetResponseDataItemRelationshipsChildComments",
    "WorkitemCommentsListGetResponseDataItemRelationshipsChildCommentsDataItem",
    "WorkitemCommentsListGetResponseDataItemRelationshipsChildCommentsDataItemType",
    "WorkitemCommentsListGetResponseDataItemRelationshipsChildCommentsMeta",
    "WorkitemCommentsListGetResponseDataItemRelationshipsParentComment",
    "WorkitemCommentsListGetResponseDataItemRelationshipsParentCommentData",
    "WorkitemCommentsListGetResponseDataItemRelationshipsParentCommentDataType",
    "WorkitemCommentsListGetResponseDataItemRelationshipsProject",
    "WorkitemCommentsListGetResponseDataItemRelationshipsProjectData",
    "WorkitemCommentsListGetResponseDataItemRelationshipsProjectDataType",
    "WorkitemCommentsListGetResponseDataItemType",
    "WorkitemCommentsListGetResponseIncludedItem",
    "WorkitemCommentsListGetResponseLinks",
    "WorkitemCommentsListGetResponseMeta",
    "WorkitemCommentsListPostRequest",
    "WorkitemCommentsListPostRequestDataItem",
    "WorkitemCommentsListPostRequestDataItemAttributes",
    "WorkitemCommentsListPostRequestDataItemAttributesText",
    "WorkitemCommentsListPostRequestDataItemAttributesTextType",
    "WorkitemCommentsListPostRequestDataItemRelationships",
    "WorkitemCommentsListPostRequestDataItemRelationshipsAuthor",
    "WorkitemCommentsListPostRequestDataItemRelationshipsAuthorData",
    "WorkitemCommentsListPostRequestDataItemRelationshipsAuthorDataType",
    "WorkitemCommentsListPostRequestDataItemRelationshipsParentComment",
    "WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentData",
    "WorkitemCommentsListPostRequestDataItemRelationshipsParentCommentDataType",
    "WorkitemCommentsListPostRequestDataItemType",
    "WorkitemCommentsListPostResponse",
    "WorkitemCommentsListPostResponseDataItem",
    "WorkitemCommentsListPostResponseDataItemLinks",
    "WorkitemCommentsListPostResponseDataItemType",
    "WorkitemCommentsSingleGetResponse",
    "WorkitemCommentsSingleGetResponseData",
    "WorkitemCommentsSingleGetResponseDataAttributes",
    "WorkitemCommentsSingleGetResponseDataAttributesText",
    "WorkitemCommentsSingleGetResponseDataAttributesTextType",
    "WorkitemCommentsSingleGetResponseDataLinks",
    "WorkitemCommentsSingleGetResponseDataMeta",
    "WorkitemCommentsSingleGetResponseDataMetaErrorsItem",
    "WorkitemCommentsSingleGetResponseDataMetaErrorsItemSource",
    "WorkitemCommentsSingleGetResponseDataRelationships",
    "WorkitemCommentsSingleGetResponseDataRelationshipsAuthor",
    "WorkitemCommentsSingleGetResponseDataRelationshipsAuthorData",
    "WorkitemCommentsSingleGetResponseDataRelationshipsAuthorDataType",
    "WorkitemCommentsSingleGetResponseDataRelationshipsChildComments",
    "WorkitemCommentsSingleGetResponseDataRelationshipsChildCommentsDataItem",
    "WorkitemCommentsSingleGetResponseDataRelationshipsChildCommentsDataItemType",
    "WorkitemCommentsSingleGetResponseDataRelationshipsChildCommentsMeta",
    "WorkitemCommentsSingleGetResponseDataRelationshipsParentComment",
    "WorkitemCommentsSingleGetResponseDataRelationshipsParentCommentData",
    "WorkitemCommentsSingleGetResponseDataRelationshipsParentCommentDataType",
    "WorkitemCommentsSingleGetResponseDataRelationshipsProject",
    "WorkitemCommentsSingleGetResponseDataRelationshipsProjectData",
    "WorkitemCommentsSingleGetResponseDataRelationshipsProjectDataType",
    "WorkitemCommentsSingleGetResponseDataType",
    "WorkitemCommentsSingleGetResponseIncludedItem",
    "WorkitemCommentsSingleGetResponseLinks",
    "WorkitemCommentsSinglePatchRequest",
    "WorkitemCommentsSinglePatchRequestData",
    "WorkitemCommentsSinglePatchRequestDataAttributes",
    "WorkitemCommentsSinglePatchRequestDataType",
    "WorkitemsListDeleteRequest",
    "WorkitemsListDeleteRequestDataItem",
    "WorkitemsListDeleteRequestDataItemType",
    "WorkitemsListGetResponse",
    "WorkitemsListGetResponseDataItem",
    "WorkitemsListGetResponseDataItemAttributes",
    "WorkitemsListGetResponseDataItemAttributesDescription",
    "WorkitemsListGetResponseDataItemAttributesDescriptionType",
    "WorkitemsListGetResponseDataItemAttributesHyperlinksItem",
    "WorkitemsListGetResponseDataItemLinks",
    "WorkitemsListGetResponseDataItemMeta",
    "WorkitemsListGetResponseDataItemMetaErrorsItem",
    "WorkitemsListGetResponseDataItemMetaErrorsItemSource",
    "WorkitemsListGetResponseDataItemRelationships",
    "WorkitemsListGetResponseDataItemRelationshipsAssignee",
    "WorkitemsListGetResponseDataItemRelationshipsAssigneeDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsAssigneeDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsAssigneeMeta",
    "WorkitemsListGetResponseDataItemRelationshipsAttachments",
    "WorkitemsListGetResponseDataItemRelationshipsAttachmentsDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsAttachmentsDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsAttachmentsLinks",
    "WorkitemsListGetResponseDataItemRelationshipsAttachmentsMeta",
    "WorkitemsListGetResponseDataItemRelationshipsAuthor",
    "WorkitemsListGetResponseDataItemRelationshipsAuthorData",
    "WorkitemsListGetResponseDataItemRelationshipsAuthorDataType",
    "WorkitemsListGetResponseDataItemRelationshipsCategories",
    "WorkitemsListGetResponseDataItemRelationshipsCategoriesDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsCategoriesDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsCategoriesMeta",
    "WorkitemsListGetResponseDataItemRelationshipsComments",
    "WorkitemsListGetResponseDataItemRelationshipsCommentsDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsCommentsDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsCommentsLinks",
    "WorkitemsListGetResponseDataItemRelationshipsCommentsMeta",
    "WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItems",
    "WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsLinks",
    "WorkitemsListGetResponseDataItemRelationshipsLinkedWorkItemsMeta",
    "WorkitemsListGetResponseDataItemRelationshipsModule",
    "WorkitemsListGetResponseDataItemRelationshipsModuleData",
    "WorkitemsListGetResponseDataItemRelationshipsModuleDataType",
    "WorkitemsListGetResponseDataItemRelationshipsPlannedIn",
    "WorkitemsListGetResponseDataItemRelationshipsPlannedInDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsPlannedInDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsPlannedInMeta",
    "WorkitemsListGetResponseDataItemRelationshipsProject",
    "WorkitemsListGetResponseDataItemRelationshipsProjectData",
    "WorkitemsListGetResponseDataItemRelationshipsProjectDataType",
    "WorkitemsListGetResponseDataItemRelationshipsWatches",
    "WorkitemsListGetResponseDataItemRelationshipsWatchesDataItem",
    "WorkitemsListGetResponseDataItemRelationshipsWatchesDataItemType",
    "WorkitemsListGetResponseDataItemRelationshipsWatchesMeta",
    "WorkitemsListGetResponseDataItemType",
    "WorkitemsListGetResponseIncludedItem",
    "WorkitemsListGetResponseLinks",
    "WorkitemsListGetResponseMeta",
    "WorkitemsListPostRequest",
    "WorkitemsListPostRequestDataItem",
    "WorkitemsListPostRequestDataItemAttributes",
    "WorkitemsListPostRequestDataItemAttributesDescription",
    "WorkitemsListPostRequestDataItemAttributesDescriptionType",
    "WorkitemsListPostRequestDataItemAttributesHyperlinksItem",
    "WorkitemsListPostRequestDataItemRelationships",
    "WorkitemsListPostRequestDataItemRelationshipsAssignee",
    "WorkitemsListPostRequestDataItemRelationshipsAssigneeDataItem",
    "WorkitemsListPostRequestDataItemRelationshipsAssigneeDataItemType",
    "WorkitemsListPostRequestDataItemRelationshipsAuthor",
    "WorkitemsListPostRequestDataItemRelationshipsAuthorData",
    "WorkitemsListPostRequestDataItemRelationshipsAuthorDataType",
    "WorkitemsListPostRequestDataItemRelationshipsCategories",
    "WorkitemsListPostRequestDataItemRelationshipsCategoriesDataItem",
    "WorkitemsListPostRequestDataItemRelationshipsCategoriesDataItemType",
    "WorkitemsListPostRequestDataItemRelationshipsModule",
    "WorkitemsListPostRequestDataItemRelationshipsModuleData",
    "WorkitemsListPostRequestDataItemRelationshipsModuleDataType",
    "WorkitemsListPostRequestDataItemType",
    "WorkitemsListPostResponse",
    "WorkitemsListPostResponseDataItem",
    "WorkitemsListPostResponseDataItemLinks",
    "WorkitemsListPostResponseDataItemType",
    "WorkitemsSingleGetResponse",
    "WorkitemsSingleGetResponseData",
    "WorkitemsSingleGetResponseDataAttributes",
    "WorkitemsSingleGetResponseDataAttributesDescription",
    "WorkitemsSingleGetResponseDataAttributesDescriptionType",
    "WorkitemsSingleGetResponseDataAttributesHyperlinksItem",
    "WorkitemsSingleGetResponseDataLinks",
    "WorkitemsSingleGetResponseDataMeta",
    "WorkitemsSingleGetResponseDataMetaErrorsItem",
    "WorkitemsSingleGetResponseDataMetaErrorsItemSource",
    "WorkitemsSingleGetResponseDataRelationships",
    "WorkitemsSingleGetResponseDataRelationshipsAssignee",
    "WorkitemsSingleGetResponseDataRelationshipsAssigneeDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsAssigneeDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsAssigneeMeta",
    "WorkitemsSingleGetResponseDataRelationshipsAttachments",
    "WorkitemsSingleGetResponseDataRelationshipsAttachmentsDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsAttachmentsDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsAttachmentsLinks",
    "WorkitemsSingleGetResponseDataRelationshipsAttachmentsMeta",
    "WorkitemsSingleGetResponseDataRelationshipsAuthor",
    "WorkitemsSingleGetResponseDataRelationshipsAuthorData",
    "WorkitemsSingleGetResponseDataRelationshipsAuthorDataType",
    "WorkitemsSingleGetResponseDataRelationshipsCategories",
    "WorkitemsSingleGetResponseDataRelationshipsCategoriesDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsCategoriesDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsCategoriesMeta",
    "WorkitemsSingleGetResponseDataRelationshipsComments",
    "WorkitemsSingleGetResponseDataRelationshipsCommentsDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsCommentsDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsCommentsLinks",
    "WorkitemsSingleGetResponseDataRelationshipsCommentsMeta",
    "WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItems",
    "WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsLinks",
    "WorkitemsSingleGetResponseDataRelationshipsLinkedWorkItemsMeta",
    "WorkitemsSingleGetResponseDataRelationshipsModule",
    "WorkitemsSingleGetResponseDataRelationshipsModuleData",
    "WorkitemsSingleGetResponseDataRelationshipsModuleDataType",
    "WorkitemsSingleGetResponseDataRelationshipsPlannedIn",
    "WorkitemsSingleGetResponseDataRelationshipsPlannedInDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsPlannedInDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsPlannedInMeta",
    "WorkitemsSingleGetResponseDataRelationshipsProject",
    "WorkitemsSingleGetResponseDataRelationshipsProjectData",
    "WorkitemsSingleGetResponseDataRelationshipsProjectDataType",
    "WorkitemsSingleGetResponseDataRelationshipsWatches",
    "WorkitemsSingleGetResponseDataRelationshipsWatchesDataItem",
    "WorkitemsSingleGetResponseDataRelationshipsWatchesDataItemType",
    "WorkitemsSingleGetResponseDataRelationshipsWatchesMeta",
    "WorkitemsSingleGetResponseDataType",
    "WorkitemsSingleGetResponseIncludedItem",
    "WorkitemsSingleGetResponseLinks",
    "WorkitemsSinglePatchRequest",
    "WorkitemsSinglePatchRequestData",
    "WorkitemsSinglePatchRequestDataAttributes",
    "WorkitemsSinglePatchRequestDataAttributesDescription",
    "WorkitemsSinglePatchRequestDataAttributesDescriptionType",
    "WorkitemsSinglePatchRequestDataAttributesHyperlinksItem",
    "WorkitemsSinglePatchRequestDataRelationships",
    "WorkitemsSinglePatchRequestDataRelationshipsAssignee",
    "WorkitemsSinglePatchRequestDataRelationshipsAssigneeDataItem",
    "WorkitemsSinglePatchRequestDataRelationshipsAssigneeDataItemType",
    "WorkitemsSinglePatchRequestDataRelationshipsCategories",
    "WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItem",
    "WorkitemsSinglePatchRequestDataRelationshipsCategoriesDataItemType",
    "WorkitemsSinglePatchRequestDataRelationshipsWatches",
    "WorkitemsSinglePatchRequestDataRelationshipsWatchesDataItem",
    "WorkitemsSinglePatchRequestDataRelationshipsWatchesDataItemType",
    "WorkitemsSinglePatchRequestDataType",
)
