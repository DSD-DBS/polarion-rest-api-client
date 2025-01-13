# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.testruns_list_post_request_data_item_attributes_select_test_cases_by import (
    TestrunsListPostRequestDataItemAttributesSelectTestCasesBy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_list_post_request_data_item_attributes_home_page_content import (
        TestrunsListPostRequestDataItemAttributesHomePageContent,
    )


T = TypeVar("T", bound="TestrunsListPostRequestDataItemAttributes")


@_attrs_define
class TestrunsListPostRequestDataItemAttributes:
    """
    Attributes:
        finished_on (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        group_id (Union[Unset, str]):  Example: Group ID.
        home_page_content (Union[Unset, TestrunsListPostRequestDataItemAttributesHomePageContent]):
        id (Union[Unset, str]):  Example: ID.
        id_prefix (Union[Unset, str]):  Example: MyTestRunIdPrefix.
        is_template (Union[Unset, bool]):
        keep_in_history (Union[Unset, bool]):
        query (Union[Unset, str]):  Example: Query.
        select_test_cases_by (Union[Unset, TestrunsListPostRequestDataItemAttributesSelectTestCasesBy]):  Example:
            manualSelection.
        status (Union[Unset, str]):  Example: open.
        title (Union[Unset, str]):  Example: Title.
        type (Union[Unset, str]):  Example: manual.
        use_report_from_template (Union[Unset, bool]):
    """

    finished_on: Union[Unset, datetime.datetime] = UNSET
    group_id: Union[Unset, str] = UNSET
    home_page_content: Union[
        Unset, "TestrunsListPostRequestDataItemAttributesHomePageContent"
    ] = UNSET
    id: Union[Unset, str] = UNSET
    id_prefix: Union[Unset, str] = UNSET
    is_template: Union[Unset, bool] = UNSET
    keep_in_history: Union[Unset, bool] = UNSET
    query: Union[Unset, str] = UNSET
    select_test_cases_by: Union[
        Unset, TestrunsListPostRequestDataItemAttributesSelectTestCasesBy
    ] = UNSET
    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    use_report_from_template: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        finished_on: Union[Unset, str] = UNSET
        if not isinstance(self.finished_on, Unset):
            finished_on = self.finished_on.isoformat()

        group_id = self.group_id

        home_page_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        id = self.id

        id_prefix = self.id_prefix

        is_template = self.is_template

        keep_in_history = self.keep_in_history

        query = self.query

        select_test_cases_by: Union[Unset, str] = UNSET
        if not isinstance(self.select_test_cases_by, Unset):
            select_test_cases_by = self.select_test_cases_by.value

        status = self.status

        title = self.title

        type = self.type

        use_report_from_template = self.use_report_from_template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finished_on is not UNSET:
            field_dict["finishedOn"] = finished_on
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if id is not UNSET:
            field_dict["id"] = id
        if id_prefix is not UNSET:
            field_dict["idPrefix"] = id_prefix
        if is_template is not UNSET:
            field_dict["isTemplate"] = is_template
        if keep_in_history is not UNSET:
            field_dict["keepInHistory"] = keep_in_history
        if query is not UNSET:
            field_dict["query"] = query
        if select_test_cases_by is not UNSET:
            field_dict["selectTestCasesBy"] = select_test_cases_by
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if use_report_from_template is not UNSET:
            field_dict["useReportFromTemplate"] = use_report_from_template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testruns_list_post_request_data_item_attributes_home_page_content import (
            TestrunsListPostRequestDataItemAttributesHomePageContent,
        )

        d = src_dict.copy()
        _finished_on = d.pop("finishedOn", UNSET)
        finished_on: Union[Unset, datetime.datetime]
        if isinstance(_finished_on, Unset):
            finished_on = UNSET
        else:
            finished_on = isoparse(_finished_on)

        group_id = d.pop("groupId", UNSET)

        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: Union[
            Unset, TestrunsListPostRequestDataItemAttributesHomePageContent
        ]
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = TestrunsListPostRequestDataItemAttributesHomePageContent.from_dict(
                _home_page_content
            )

        id = d.pop("id", UNSET)

        id_prefix = d.pop("idPrefix", UNSET)

        is_template = d.pop("isTemplate", UNSET)

        keep_in_history = d.pop("keepInHistory", UNSET)

        query = d.pop("query", UNSET)

        _select_test_cases_by = d.pop("selectTestCasesBy", UNSET)
        select_test_cases_by: Union[
            Unset, TestrunsListPostRequestDataItemAttributesSelectTestCasesBy
        ]
        if isinstance(_select_test_cases_by, Unset):
            select_test_cases_by = UNSET
        else:
            select_test_cases_by = (
                TestrunsListPostRequestDataItemAttributesSelectTestCasesBy(
                    _select_test_cases_by
                )
            )

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        use_report_from_template = d.pop("useReportFromTemplate", UNSET)

        testruns_list_post_request_data_item_attributes_obj = cls(
            finished_on=finished_on,
            group_id=group_id,
            home_page_content=home_page_content,
            id=id,
            id_prefix=id_prefix,
            is_template=is_template,
            keep_in_history=keep_in_history,
            query=query,
            select_test_cases_by=select_test_cases_by,
            status=status,
            title=title,
            type=type,
            use_report_from_template=use_report_from_template,
        )

        testruns_list_post_request_data_item_attributes_obj.additional_properties = (
            d
        )
        return testruns_list_post_request_data_item_attributes_obj

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
