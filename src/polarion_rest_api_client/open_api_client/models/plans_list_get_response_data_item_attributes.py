# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.plans_list_get_response_data_item_attributes_calculation_type import (
    PlansListGetResponseDataItemAttributesCalculationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plans_list_get_response_data_item_attributes_description import (
        PlansListGetResponseDataItemAttributesDescription,
    )
    from ..models.plans_list_get_response_data_item_attributes_home_page_content import (
        PlansListGetResponseDataItemAttributesHomePageContent,
    )


T = TypeVar("T", bound="PlansListGetResponseDataItemAttributes")


@_attrs_define
class PlansListGetResponseDataItemAttributes:
    """
    Attributes:
        allowed_types (Union[Unset, List[str]]):
        calculation_type (Union[Unset, PlansListGetResponseDataItemAttributesCalculationType]):  Example: timeBased.
        capacity (Union[Unset, float]):
        color (Union[Unset, str]):  Example: Color.
        created (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        default_estimate (Union[Unset, float]):
        description (Union[Unset, PlansListGetResponseDataItemAttributesDescription]):
        due_date (Union[Unset, datetime.date]):  Example: 1970-01-01.
        estimation_field (Union[Unset, str]):  Example: Estimation Field.
        finished_on (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        home_page_content (Union[Unset, PlansListGetResponseDataItemAttributesHomePageContent]):
        id (Union[Unset, str]):  Example: ID.
        is_template (Union[Unset, bool]):
        name (Union[Unset, str]):  Example: Name.
        previous_time_spent (Union[Unset, str]):  Example: 5 1/2d.
        prioritization_field (Union[Unset, str]):  Example: Prioritization Field.
        sort_order (Union[Unset, int]):
        start_date (Union[Unset, datetime.date]):  Example: 1970-01-01.
        started_on (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        status (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        use_report_from_template (Union[Unset, bool]):
    """

    allowed_types: Union[Unset, List[str]] = UNSET
    calculation_type: Union[
        Unset, PlansListGetResponseDataItemAttributesCalculationType
    ] = UNSET
    capacity: Union[Unset, float] = UNSET
    color: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    default_estimate: Union[Unset, float] = UNSET
    description: Union[
        Unset, "PlansListGetResponseDataItemAttributesDescription"
    ] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    estimation_field: Union[Unset, str] = UNSET
    finished_on: Union[Unset, datetime.datetime] = UNSET
    home_page_content: Union[
        Unset, "PlansListGetResponseDataItemAttributesHomePageContent"
    ] = UNSET
    id: Union[Unset, str] = UNSET
    is_template: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    previous_time_spent: Union[Unset, str] = UNSET
    prioritization_field: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    started_on: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    use_report_from_template: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        allowed_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_types, Unset):
            allowed_types = self.allowed_types

        calculation_type: Union[Unset, str] = UNSET
        if not isinstance(self.calculation_type, Unset):
            calculation_type = self.calculation_type.value

        capacity = self.capacity

        color = self.color

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        default_estimate = self.default_estimate

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        estimation_field = self.estimation_field

        finished_on: Union[Unset, str] = UNSET
        if not isinstance(self.finished_on, Unset):
            finished_on = self.finished_on.isoformat()

        home_page_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        id = self.id

        is_template = self.is_template

        name = self.name

        previous_time_spent = self.previous_time_spent

        prioritization_field = self.prioritization_field

        sort_order = self.sort_order

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        started_on: Union[Unset, str] = UNSET
        if not isinstance(self.started_on, Unset):
            started_on = self.started_on.isoformat()

        status = self.status

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        use_report_from_template = self.use_report_from_template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_types is not UNSET:
            field_dict["allowedTypes"] = allowed_types
        if calculation_type is not UNSET:
            field_dict["calculationType"] = calculation_type
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if color is not UNSET:
            field_dict["color"] = color
        if created is not UNSET:
            field_dict["created"] = created
        if default_estimate is not UNSET:
            field_dict["defaultEstimate"] = default_estimate
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if estimation_field is not UNSET:
            field_dict["estimationField"] = estimation_field
        if finished_on is not UNSET:
            field_dict["finishedOn"] = finished_on
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if id is not UNSET:
            field_dict["id"] = id
        if is_template is not UNSET:
            field_dict["isTemplate"] = is_template
        if name is not UNSET:
            field_dict["name"] = name
        if previous_time_spent is not UNSET:
            field_dict["previousTimeSpent"] = previous_time_spent
        if prioritization_field is not UNSET:
            field_dict["prioritizationField"] = prioritization_field
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if started_on is not UNSET:
            field_dict["startedOn"] = started_on
        if status is not UNSET:
            field_dict["status"] = status
        if updated is not UNSET:
            field_dict["updated"] = updated
        if use_report_from_template is not UNSET:
            field_dict["useReportFromTemplate"] = use_report_from_template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plans_list_get_response_data_item_attributes_description import (
            PlansListGetResponseDataItemAttributesDescription,
        )
        from ..models.plans_list_get_response_data_item_attributes_home_page_content import (
            PlansListGetResponseDataItemAttributesHomePageContent,
        )

        d = src_dict.copy()
        allowed_types = cast(List[str], d.pop("allowedTypes", UNSET))

        _calculation_type = d.pop("calculationType", UNSET)
        calculation_type: Union[
            Unset, PlansListGetResponseDataItemAttributesCalculationType
        ]
        if isinstance(_calculation_type, Unset):
            calculation_type = UNSET
        else:
            calculation_type = (
                PlansListGetResponseDataItemAttributesCalculationType(
                    _calculation_type
                )
            )

        capacity = d.pop("capacity", UNSET)

        color = d.pop("color", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        default_estimate = d.pop("defaultEstimate", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[
            Unset, PlansListGetResponseDataItemAttributesDescription
        ]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                PlansListGetResponseDataItemAttributesDescription.from_dict(
                    _description
                )
            )

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        estimation_field = d.pop("estimationField", UNSET)

        _finished_on = d.pop("finishedOn", UNSET)
        finished_on: Union[Unset, datetime.datetime]
        if isinstance(_finished_on, Unset):
            finished_on = UNSET
        else:
            finished_on = isoparse(_finished_on)

        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: Union[
            Unset, PlansListGetResponseDataItemAttributesHomePageContent
        ]
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = PlansListGetResponseDataItemAttributesHomePageContent.from_dict(
                _home_page_content
            )

        id = d.pop("id", UNSET)

        is_template = d.pop("isTemplate", UNSET)

        name = d.pop("name", UNSET)

        previous_time_spent = d.pop("previousTimeSpent", UNSET)

        prioritization_field = d.pop("prioritizationField", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _started_on = d.pop("startedOn", UNSET)
        started_on: Union[Unset, datetime.datetime]
        if isinstance(_started_on, Unset):
            started_on = UNSET
        else:
            started_on = isoparse(_started_on)

        status = d.pop("status", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        use_report_from_template = d.pop("useReportFromTemplate", UNSET)

        plans_list_get_response_data_item_attributes_obj = cls(
            allowed_types=allowed_types,
            calculation_type=calculation_type,
            capacity=capacity,
            color=color,
            created=created,
            default_estimate=default_estimate,
            description=description,
            due_date=due_date,
            estimation_field=estimation_field,
            finished_on=finished_on,
            home_page_content=home_page_content,
            id=id,
            is_template=is_template,
            name=name,
            previous_time_spent=previous_time_spent,
            prioritization_field=prioritization_field,
            sort_order=sort_order,
            start_date=start_date,
            started_on=started_on,
            status=status,
            updated=updated,
            use_report_from_template=use_report_from_template,
        )

        plans_list_get_response_data_item_attributes_obj.additional_properties = (
            d
        )
        return plans_list_get_response_data_item_attributes_obj

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
