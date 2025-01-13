# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_records import (
    get_test_records,
    patch_test_record,
    post_test_records,
)

from . import base_classes as bc


class TestRecords(
    bc.SingleUpdatableItemsMixin[dm.TestRecord],
    bc.UpdatableItemsClient[dm.TestRecord],
):
    def get(self, *args, **kwargs) -> dm.TestRecord:
        raise NotImplementedError

    def _update(self, to_update: list[dm.TestRecord] | dm.TestRecord):
        assert not isinstance(to_update, list), "Expected only one item"
        response = patch_test_record.sync_detailed(
            self._project_id,
            to_update.test_run_id,
            to_update.work_item_project_id,
            to_update.work_item_id,
            str(to_update.iteration),
            client=self._client.client,
            # pylint: disable=line-too-long
            body=api_models.TestrecordsSinglePatchRequest(
                data=api_models.TestrecordsSinglePatchRequestData(
                    type=api_models.TestrecordsSinglePatchRequestDataType.TESTRECORDS,
                    id=f"{self._project_id}/{to_update.test_run_id}/{to_update.work_item_project_id}/{to_update.work_item_id}/{to_update.iteration}",
                    attributes=self._fill_test_record_attributes(
                        api_models.TestrecordsSinglePatchRequestDataAttributes,
                        to_update,
                    ),
                )
            ),
            # pylint: enable=line-too-long
        )
        self._raise_on_error(response)

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

    def _split_into_batches(
        self, items: list[dm.TestRecord]
    ) -> t.Generator[list[dm.TestRecord], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.test_run_id):
            yield from super()._split_into_batches(list(group))

    def _create(
        self,
        items: list[dm.TestRecord],
    ):
        """Create the given list of test records."""
        response = post_test_records.sync_detailed(
            self._project_id,
            items[0].test_run_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=api_models.TestrecordsListPostRequest(
                [
                    api_models.TestrecordsListPostRequestDataItem(
                        type=api_models.TestrecordsListPostRequestDataItemType.TESTRECORDS,
                        attributes=self._fill_test_record_attributes(
                            api_models.TestrecordsListPostRequestDataItemAttributes,
                            test_record,
                        ),
                        relationships=api_models.TestrecordsListPostRequestDataItemRelationships(
                            test_case=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCase(
                                data=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseData(
                                    type=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseDataType.WORKITEMS,
                                    id=f"{test_record.work_item_project_id}/{test_record.work_item_id}",
                                )
                            )
                        ),
                    )
                    for test_record in items
                ]
            ),
            # pylint: enable=line-too-long
        )

        self._raise_on_error(response)

        assert (
            isinstance(response.parsed, api_models.TestrecordsListPostResponse)
            and response.parsed.data
        )
        counter = 0
        for response_item in response.parsed.data:
            if response_item.id:
                items[counter].iteration = int(response_item.id.split("/")[-1])
                counter += 1

    def _delete(self, items: dm.TestRecord | list[dm.TestRecord]):
        raise NotImplementedError

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
        return attributes
