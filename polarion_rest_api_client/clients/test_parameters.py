# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Clients to handle test parameters."""

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client.api.test_records import (
    delete_test_record_test_parameter,
    get_test_record_test_parameters,
    post_test_record_test_parameters,
)
from polarion_rest_api_client.open_api_client.api.test_runs import (
    delete_test_run_test_parameters,
    get_test_run_test_parameters,
    post_test_run_test_parameters,
)

from . import base_classes as bc


class TestRunParameters(bc.ItemsClient[dm.TestParameter]):
    """Client to handle TestParameters of a TestRun."""

    def get(self, *args, **kwargs) -> dm.TestParameter:
        raise NotImplementedError

    def get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestParameter], bool]:
        if fields is None:
            fields = self._client.default_fields.testparameters

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_run_test_parameters.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)
        return _parse_get_response(response.parsed, test_run_id)

    def _split_into_batches(
        self, items: list[dm.TestParameter]
    ) -> t.Generator[list[dm.TestParameter], None, None]:
        assert all(isinstance(item.scope, str) for item in items)
        for _, group in itertools.groupby(
            sorted(
                items,
                key=lambda x: x.scope if isinstance(x.scope, str) else "",
            ),
            lambda x: x.scope,
        ):
            yield list(group)

    def _create(self, items: list[dm.TestParameter]):
        body = api_models.TestparametersListPostRequest(
            data=[
                api_models.TestparametersListPostRequestDataItem(
                    type_=api_models.TestparametersListPostRequestDataItemType.TESTPARAMETERS,
                    attributes=api_models.TestparametersListPostRequestDataItemAttributes(
                        name=item.name, value=item.value
                    ),
                )
                for item in items
            ]
        )

        assert isinstance(
            items[0].scope, str
        ), "For parameters of TestRuns the scope must be a string"

        response = post_test_run_test_parameters.sync_detailed(
            self._project_id,
            items[0].scope,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

        assert (
            isinstance(
                response.parsed, api_models.TestparametersListPostResponse
            )
            and response.parsed.data
        )

    def _delete(self, items: list[dm.TestParameter]):
        body = api_models.TestparametersListDeleteRequest(
            data=[
                api_models.TestparametersListDeleteRequestDataItem(
                    type_=api_models.TestparametersListDeleteRequestDataItemType.TESTPARAMETERS,
                    id=f"{self._project_id}/{item.scope}/{item.name}",
                )
                for item in items
            ]
        )

        assert isinstance(
            items[0].scope, str
        ), "For parameters of TestRuns the scope must be a string"

        response = delete_test_run_test_parameters.sync_detailed(
            self._project_id,
            items[0].scope,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)


class TestRecordParameters(bc.ItemsClient[dm.TestParameter]):
    """Clients to handle TestParameters of a TestRecord."""

    def get(self, *args, **kwargs) -> dm.TestParameter:
        raise NotImplementedError

    def get_multi(  # type: ignore[override]
        self,
        test_record: dm.TestRecord,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestParameter], bool]:
        if fields is None:
            fields = self._client.default_fields.testparameters

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_record_test_parameters.sync_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)

        return _parse_get_response(response.parsed, test_record)

    def _split_into_batches(
        self, items: list[dm.TestParameter]
    ) -> t.Generator[list[dm.TestParameter], None, None]:
        assert all(isinstance(item.scope, dm.TestRecord) for item in items)
        for _, group in itertools.groupby(
            sorted(
                items,
                key=lambda x: (
                    f"{x.scope.test_run_id}/{x.scope.work_item_project_id}/{x.scope.work_item_id}/{x.scope.iteration}"
                    if isinstance(x.scope, dm.TestRecord)
                    else ""
                ),
            ),
            lambda x: x.scope,
        ):
            yield list(group)

    def _create(self, items: list[dm.TestParameter]):
        body = _build_post_body(items)

        assert isinstance(
            items[0].scope, dm.TestRecord
        ), "For parameters of TestRecords the scope must be a TestRecord"

        response = post_test_record_test_parameters.sync_detailed(
            self._project_id,
            items[0].scope.test_run_id,
            items[0].scope.work_item_project_id,
            items[0].scope.work_item_id,
            str(items[0].scope.iteration),
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    def _delete(self, items: list[dm.TestParameter]):
        assert len(items) == 1
        assert isinstance(
            items[0].scope, dm.TestRecord
        ), "For parameters of TestRecords the scope must be a TestRecord"
        response = delete_test_record_test_parameter.sync_detailed(
            self._project_id,
            items[0].scope.test_run_id,
            items[0].scope.work_item_project_id,
            items[0].scope.work_item_id,
            str(items[0].scope.iteration),
            items[0].name,
            client=self._client.client,
        )
        self._raise_on_error(response)

    def delete(self, items: dm.TestParameter | list[dm.TestParameter]):
        if not isinstance(items, list):
            items = [items]

        for item in items:
            self._delete([item])


def _parse_get_response(
    parsed_response: (
        api_models.TestparametersListGetResponse | api_models.Errors | None
    ),
    scope: str | dm.TestRecord,
) -> tuple[list[dm.TestParameter], bool]:
    assert isinstance(
        parsed_response, api_models.TestparametersListGetResponse
    )
    parameters = [
        dm.TestParameter(
            scope=scope,
            name=data.attributes.name or "",
            value=data.attributes.value or "",
        )
        for data in parsed_response.data or []
        if data.attributes
    ]
    next_page = isinstance(
        parsed_response.links, api_models.TestparametersListGetResponseLinks
    ) and bool(parsed_response.links.next_)
    return parameters, next_page


def _build_post_body(
    items: list[dm.TestParameter],
) -> api_models.TestparametersListPostRequest:
    body = api_models.TestparametersListPostRequest(
        data=[
            api_models.TestparametersListPostRequestDataItem(
                type_=api_models.TestparametersListPostRequestDataItemType.TESTPARAMETERS,
                attributes=api_models.TestparametersListPostRequestDataItemAttributes(
                    name=item.name, value=item.value
                ),
            )
            for item in items
        ]
    )
    return body
