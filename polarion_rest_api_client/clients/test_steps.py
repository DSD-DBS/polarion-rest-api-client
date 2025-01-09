# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_steps import (
    delete_test_steps,
    get_test_steps,
    patch_test_steps,
    post_test_steps,
)

from . import base_classes as bc


class TestSteps(
    bc.UpdatableItemsClient[dm.TestStep],
):
    def get(self, *args, **kwargs) -> dm.TestStep:
        raise NotImplementedError

    def _update(self, to_update: list[dm.TestStep] | dm.TestStep):
        if not isinstance(to_update, list):
            to_update = [to_update]
        response = patch_test_steps.sync_detailed(
            self._project_id,
            to_update[0].work_item_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=api_models.TeststepsListPatchRequest(
                data=[
                    api_models.TeststepsListPatchRequestDataItem(
                        type=api_models.TeststepsListPatchRequestDataItemType.TESTSTEPS,
                        id=(
                            f"{self._project_id}/{item.work_item_id}/{item.step_index}"
                            if item.step_index
                            else oa_types.UNSET
                        ),
                        attributes=self._fill_test_step_attributes(
                            api_models.TeststepsListPatchRequestDataItemAttributes,
                            item,
                        ),
                    )
                    for item in to_update
                ]
            ),
            # pylint: enable=line-too-long
        )
        self._raise_on_error(response)

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestStep], bool]:
        if fields is None:
            fields = self._client.default_fields.teststeps

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_steps.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)

        parsed_response = response.parsed
        assert isinstance(parsed_response, api_models.TeststepsListGetResponse)

        test_steps = []

        for data in parsed_response.data or []:
            assert isinstance(data.id, str)
            assert isinstance(
                data.attributes,
                api_models.TeststepsListGetResponseDataItemAttributes,
            )
            _, work_item, index = data.id.split("/")
            attribute_values = (
                dm.TextContent(
                    val.type.value if val.type else "text/plain",
                    val.value or None,
                )
                for val in data.attributes.values or []
            )
            test_steps.append(
                dm.TestStep(
                    work_item_id=work_item,
                    step_index=int(index),
                    revision=data.revision if data.revision else None,
                    step_columns=dict(
                        zip(data.attributes.keys or [], attribute_values)
                    ),
                )
            )
        next_page = isinstance(
            parsed_response.links,
            api_models.TeststepsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)

        return test_steps, next_page

    def _split_into_batches(
        self, items: list[dm.TestStep]
    ) -> t.Generator[list[dm.TestStep], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.work_item_id):
            yield from super()._split_into_batches(list(group))

    def _create(
        self,
        items: list[dm.TestStep],
    ):
        """Create the given list of test records."""
        response = post_test_steps.sync_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=api_models.TeststepsListPostRequest(
                [
                    api_models.TeststepsListPostRequestDataItem(
                        type=api_models.TeststepsListPostRequestDataItemType.TESTSTEPS,
                        attributes=self._fill_test_step_attributes(
                            api_models.TeststepsListPostRequestDataItemAttributes,
                            test_step,
                        ),
                    )
                    for test_step in items
                ]
            ),
            # pylint: enable=line-too-long
        )

        self._raise_on_error(response)

        assert (
            isinstance(response.parsed, api_models.TeststepsListPostResponse)
            and response.parsed.data
        )
        counter = 0
        for response_item in response.parsed.data:
            if response_item.id:
                items[counter].step_index = int(
                    response_item.id.split("/")[-1]
                )
                counter += 1

    def _delete(self, items: dm.TestStep | list[dm.TestStep]):
        if not isinstance(items, list):
            items = [items]
        response = delete_test_steps.sync_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=api_models.TeststepsListDeleteRequest(
                data=[
                    api_models.TeststepsListDeleteRequestDataItem(
                        type=api_models.TeststepsListDeleteRequestDataItemType.TESTSTEPS,
                        id=f"{self._project_id}/{step.work_item_id}/{step.step_index}",
                    )
                    for step in items
                ]
            ),
        )
        self._raise_on_error(response)

    def _fill_test_step_attributes(
        self,
        attributes_type: type[
            api_models.TeststepsListPostRequestDataItemAttributes
            | api_models.TeststepsListPatchRequestDataItemAttributes
        ],
        test_step: dm.TestStep,
    ):
        value_item_name = attributes_type.__name__ + "ValuesItem"
        value_item_cls = getattr(api_models, value_item_name)
        value_item_type = getattr(api_models, value_item_name + "Type")

        return attributes_type(
            keys=list(test_step.step_columns.keys()),
            values=[
                value_item_cls(
                    type=(
                        value_item_type.TEXTHTML
                        if column.type == "text/html"
                        else value_item_type.TEXTPLAIN
                    ),
                    value=column.value,
                )
                for column in test_step.step_columns.values()
            ],
        )
