# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_records import (
    delete_test_record,
    get_test_records,
    patch_test_record,
    post_test_records,
)

from . import base_classes as bc
from . import test_parameters

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client

AttributesType = t.TypeVar(
    "AttributesType",
    bound=api_models.TestrecordsListPostRequestDataItemAttributes
    | api_models.TestrecordsSinglePatchRequestDataAttributes,
)


class TestRecords(
    bc.CreateClient[dm.TestRecord],
    bc.MultiGetClient[dm.TestRecord],
    bc.DeleteClient[dm.TestRecord],
    bc.UpdateClient[dm.TestRecord],
):
    _update_batch_size = 1

    def __init__(
        self, project_id: str, client: polarion_client.PolarionClient
    ):
        super().__init__(project_id, client)
        self.parameters = test_parameters.TestRecordParameters(
            project_id, client
        )

    def _update(self, to_update: list[dm.TestRecord]) -> None:
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        response = patch_test_record.sync_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
            body=self._build_patch_body(item),
        )
        self._raise_on_error(response)

    async def _a_update(self, to_update: list[dm.TestRecord]) -> None:
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        response = await patch_test_record.asyncio_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
            body=self._build_patch_body(item),
        )
        self._raise_on_error(response)

    def _build_patch_body(
        self, to_update: dm.TestRecord
    ) -> api_models.TestrecordsSinglePatchRequest:
        # pylint: disable=line-too-long
        return api_models.TestrecordsSinglePatchRequest(
            data=api_models.TestrecordsSinglePatchRequestData(
                type_=api_models.TestrecordsSinglePatchRequestDataType.TESTRECORDS,
                id=f"{self._project_id}/{to_update.test_run_id}/{to_update.work_item_project_id}/{to_update.work_item_id}/{to_update.iteration}",
                attributes=self._fill_test_record_attributes(
                    api_models.TestrecordsSinglePatchRequestDataAttributes,
                    to_update,
                ),
            )
        )
        # pylint: enable=line-too-long

    def get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestRecord], bool]:
        if fields is None:
            fields = self._client.default_fields.testrecords

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_records.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )
        return self._parse_get_response(response, test_run_id)

    async def a_get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestRecord], bool]:
        if fields is None:
            fields = self._client.default_fields.testrecords

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_records.asyncio_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )
        return self._parse_get_response(response, test_run_id)

    def _parse_get_response(
        self, response: oa_types.Response, test_run_id: str
    ) -> tuple[list[dm.TestRecord], bool]:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(
            parsed_response, api_models.TestrecordsListGetResponse
        )
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
                    test_run_id,
                    project_id,
                    work_item,
                    self.unset_to_none(data.attributes.test_case_revision),
                    int(iteration),
                    (
                        data.attributes.duration
                        if not isinstance(
                            data.attributes.duration, oa_types.Unset
                        )
                        else -1
                    ),
                    self.unset_to_none(data.attributes.result),
                    self._handle_text_content(data.attributes.comment),
                    self.unset_to_none(data.attributes.executed),
                    data.additional_properties or {},
                )
            )
        next_page = isinstance(
            parsed_response.links,
            api_models.TestrecordsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)
        return test_records, next_page

    def _pre_batching_grouping(
        self, items: list[dm.TestRecord]
    ) -> t.Generator[list[dm.TestRecord], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.test_run_id):
            yield list(group)

    def _create(
        self,
        items: list[dm.TestRecord],
    ) -> None:
        """Create the given list of test records."""
        response = post_test_records.sync_detailed(
            self._project_id,
            items[0].test_run_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=self._build_post_body(items),
            # pylint: enable=line-too-long
        )

        self._parse_post_response(items, response)

    async def _a_create(
        self,
        items: list[dm.TestRecord],
    ) -> None:
        """Create the given list of test records."""
        response = await post_test_records.asyncio_detailed(
            self._project_id,
            items[0].test_run_id,
            client=self._client.client,
            body=self._build_post_body(items),
        )
        self._parse_post_response(items, response)

    def _parse_post_response(
        self, items: list[dm.TestRecord], response: oa_types.Response
    ) -> None:
        self._raise_on_error(response)
        assert isinstance(
            response.parsed, api_models.TestrecordsListPostResponse
        )
        assert response.parsed.data
        counter = 0
        for response_item in response.parsed.data:
            if response_item.id:
                items[counter].iteration = int(response_item.id.split("/")[-1])
                counter += 1

    def _build_post_body(
        self, items: list[dm.TestRecord]
    ) -> api_models.TestrecordsListPostRequest:
        # pylint: disable=line-too-long
        return api_models.TestrecordsListPostRequest(
            [
                api_models.TestrecordsListPostRequestDataItem(
                    type_=api_models.TestrecordsListPostRequestDataItemType.TESTRECORDS,
                    attributes=self._fill_test_record_attributes(
                        api_models.TestrecordsListPostRequestDataItemAttributes,
                        test_record,
                    ),
                    relationships=api_models.TestrecordsListPostRequestDataItemRelationships(
                        test_case=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCase(
                            data=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseData(
                                type_=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseDataType.WORKITEMS,
                                id=f"{test_record.work_item_project_id}/{test_record.work_item_id}",
                            )
                        )
                    ),
                )
                for test_record in items
            ]
        )
        # pylint: enable=line-too-long

    def _delete(self, items: list[dm.TestRecord]) -> None:
        assert len(items) == 1, "Expected only one item"
        item = items[0]
        response = delete_test_record.sync_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
        )
        self._raise_on_error(response)

    async def _a_delete(self, items: list[dm.TestRecord]) -> None:
        assert len(items) == 1, "Expected only one item"
        item = items[0]
        response = await delete_test_record.asyncio_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
        )
        self._raise_on_error(response)

    def _fill_test_record_attributes(
        self,
        attributes_type: type[AttributesType],
        test_record: dm.TestRecord,
    ) -> AttributesType:
        type_prefix = attributes_type.__name__
        attributes = attributes_type()
        if test_record.result:
            attributes.result = test_record.result
        if test_record.comment:
            attributes.comment = getattr(api_models, f"{type_prefix}Comment")()
            assert attributes.comment
            if test_record.comment.type:
                attributes.comment.type_ = getattr(
                    api_models, f"{type_prefix}CommentType"
                )(test_record.comment.type)
            if test_record.comment.value:
                attributes.comment.value = test_record.comment.value
        if test_record.duration != -1:
            attributes.duration = test_record.duration
        if test_record.work_item_revision:
            attributes.test_case_revision = test_record.work_item_revision
        if test_record.executed:
            attributes.executed = test_record.executed
        if test_record.additional_attributes:
            attributes.additional_properties = (
                test_record.additional_attributes
            )
        return t.cast(AttributesType, attributes)
