# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client.api.test_runs import (
    get_test_runs,
    patch_test_run,
    post_test_runs,
)

from . import base_classes as bc
from . import test_records

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client


class TestRuns(
    bc.SingleUpdatableItemsMixin[dm.TestRun],
    bc.UpdatableItemsClient[dm.TestRun],
):
    def get(self, *args, **kwargs) -> dm.TestRun:
        raise NotImplementedError

    def __init__(
        self, project_id: str, client: "polarion_client.PolarionClient"
    ):
        super().__init__(project_id, client)
        self.records = test_records.TestRecords(project_id, client)

    def _update(self, to_update: list[dm.TestRun] | dm.TestRun):
        """Create the given list of test runs."""
        assert not isinstance(to_update, list), "Expected only one item"
        assert to_update.id
        response = patch_test_run.sync_detailed(
            self._project_id,
            to_update.id,
            client=self._client.client,
            body=api_models.TestrunsSinglePatchRequest(
                data=api_models.TestrunsSinglePatchRequestData(
                    type=api_models.TestrunsSinglePatchRequestDataType.TESTRUNS,  # pylint: disable=line-too-long
                    id=f"{self._project_id}/{to_update.id}",
                    attributes=self._fill_test_run_attributes(
                        api_models.TestrunsSinglePatchRequestDataAttributes,
                        to_update,
                    ),
                )
            ),
        )

        self._raise_on_error(response)

    def get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: t.Optional[dict[str, str]] = None,
    ) -> tuple[list[dm.TestRun], bool]:
        """Return the test runs on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.testruns

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_runs.sync_detailed(
            self._project_id,
            client=self._client.client,
            query=query,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)

        parsed_response = response.parsed
        assert isinstance(parsed_response, api_models.TestrunsListGetResponse)

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
                    self.unset_to_none(data.attributes.type),
                    self.unset_to_none(data.attributes.status),
                    self.unset_to_none(data.attributes.title),
                    self._handle_text_content(
                        data.attributes.home_page_content
                    ),
                    self.unset_to_none(data.attributes.finished_on),
                    self.unset_to_none(data.attributes.group_id),
                    self.unset_to_none(data.attributes.id_prefix),
                    self.unset_to_none(data.attributes.is_template),
                    self.unset_to_none(data.attributes.keep_in_history),
                    self.unset_to_none(data.attributes.query),
                    self.unset_to_none(data.attributes.keep_in_history),
                    (
                        dm.SelectTestCasesBy(
                            str(data.attributes.select_test_cases_by)
                        )
                        if data.attributes.select_test_cases_by
                        else None
                    ),
                    data.attributes.additional_properties or {},
                )
            )
        next_page = isinstance(
            parsed_response.links,
            api_models.TestrunsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)

        return test_runs, next_page

    def _create(self, items: list[dm.TestRun]):
        """Create the given list of test runs."""
        polarion_test_runs = [
            api_models.TestrunsListPostRequestDataItem(
                type=api_models.TestrunsListPostRequestDataItemType.TESTRUNS,
                attributes=self._fill_test_run_attributes(
                    api_models.TestrunsListPostRequestDataItemAttributes,
                    test_run,
                ),
            )
            for test_run in items
        ]

        response = post_test_runs.sync_detailed(
            self._project_id,
            client=self._client.client,
            body=api_models.TestrunsListPostRequest(polarion_test_runs),
        )

        self._raise_on_error(response)

    def _delete(self, items: dm.TestRun | list[dm.TestRun]):
        raise NotImplementedError

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
        if test_run.type is not None:
            attributes.type = test_run.type
        if test_run.id and hasattr(attributes, "id"):
            attributes.id = test_run.id
        if test_run.status is not None:
            attributes.status = test_run.status
        if test_run.title is not None:
            attributes.title = test_run.title
        if test_run.finished_on is not None:
            attributes.finished_on = test_run.finished_on
        if test_run.group_id is not None:
            attributes.group_id = test_run.group_id
        if test_run.id_prefix is not None:
            attributes.id_prefix = test_run.id_prefix
        if test_run.is_template is not None and hasattr(
            attributes, "is_template"
        ):
            attributes.is_template = test_run.is_template
        if test_run.keep_in_history is not None:
            attributes.keep_in_history = test_run.keep_in_history
        if test_run.query is not None:
            attributes.query = test_run.query
        if test_run.use_report_from_template is not None:
            attributes.use_report_from_template = (
                test_run.use_report_from_template
            )
        if test_run.additional_attributes:
            attributes.additional_properties = test_run.additional_attributes
        if test_run.select_test_cases_by:
            attributes.select_test_cases_by = getattr(
                api_models, f"{type_prefix}SelectTestCasesBy"
            )(test_run.select_test_cases_by.value)
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
