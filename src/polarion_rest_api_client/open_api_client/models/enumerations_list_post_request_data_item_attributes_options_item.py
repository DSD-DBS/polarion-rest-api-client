# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="EnumerationsListPostRequestDataItemAttributesOptionsItem"
)


@_attrs_define
class EnumerationsListPostRequestDataItemAttributesOptionsItem:
    """
    Attributes:
        color (Union[Unset, str]):  Example: #F9FF4D.
        column_width (Union[Unset, str]):  Example: 90%.
        create_defect (Union[Unset, bool]):  Example: True.
        default (Union[Unset, bool]):  Example: True.
        description (Union[Unset, str]):  Example: Description.
        hidden (Union[Unset, bool]):
        icon_url (Union[Unset, str]):  Example: /polarion/icons/default/enums/status_open.gif.
        id (Union[Unset, str]):  Example: open.
        min_value (Union[Unset, float]):  Example: 30.0.
        name (Union[Unset, str]):  Example: Open.
        opposite_name (Union[Unset, str]):  Example: Opposite Name.
        parent (Union[Unset, bool]):  Example: True.
        requires_signature_for_test_case_execution (Union[Unset, bool]):  Example: True.
        template_work_item (Union[Unset, str]):  Example: exampleTemplate.
        terminal (Union[Unset, bool]):  Example: True.
    """

    color: Union[Unset, str] = UNSET
    column_width: Union[Unset, str] = UNSET
    create_defect: Union[Unset, bool] = UNSET
    default: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    icon_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    min_value: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    opposite_name: Union[Unset, str] = UNSET
    parent: Union[Unset, bool] = UNSET
    requires_signature_for_test_case_execution: Union[Unset, bool] = UNSET
    template_work_item: Union[Unset, str] = UNSET
    terminal: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        color = self.color

        column_width = self.column_width

        create_defect = self.create_defect

        default = self.default

        description = self.description

        hidden = self.hidden

        icon_url = self.icon_url

        id = self.id

        min_value = self.min_value

        name = self.name

        opposite_name = self.opposite_name

        parent = self.parent

        requires_signature_for_test_case_execution = (
            self.requires_signature_for_test_case_execution
        )

        template_work_item = self.template_work_item

        terminal = self.terminal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if column_width is not UNSET:
            field_dict["columnWidth"] = column_width
        if create_defect is not UNSET:
            field_dict["createDefect"] = create_defect
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if icon_url is not UNSET:
            field_dict["iconURL"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if name is not UNSET:
            field_dict["name"] = name
        if opposite_name is not UNSET:
            field_dict["oppositeName"] = opposite_name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if requires_signature_for_test_case_execution is not UNSET:
            field_dict["requiresSignatureForTestCaseExecution"] = (
                requires_signature_for_test_case_execution
            )
        if template_work_item is not UNSET:
            field_dict["templateWorkItem"] = template_work_item
        if terminal is not UNSET:
            field_dict["terminal"] = terminal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        color = d.pop("color", UNSET)

        column_width = d.pop("columnWidth", UNSET)

        create_defect = d.pop("createDefect", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        icon_url = d.pop("iconURL", UNSET)

        id = d.pop("id", UNSET)

        min_value = d.pop("minValue", UNSET)

        name = d.pop("name", UNSET)

        opposite_name = d.pop("oppositeName", UNSET)

        parent = d.pop("parent", UNSET)

        requires_signature_for_test_case_execution = d.pop(
            "requiresSignatureForTestCaseExecution", UNSET
        )

        template_work_item = d.pop("templateWorkItem", UNSET)

        terminal = d.pop("terminal", UNSET)

        enumerations_list_post_request_data_item_attributes_options_item_obj = cls(
            color=color,
            column_width=column_width,
            create_defect=create_defect,
            default=default,
            description=description,
            hidden=hidden,
            icon_url=icon_url,
            id=id,
            min_value=min_value,
            name=name,
            opposite_name=opposite_name,
            parent=parent,
            requires_signature_for_test_case_execution=requires_signature_for_test_case_execution,
            template_work_item=template_work_item,
            terminal=terminal,
        )

        enumerations_list_post_request_data_item_attributes_options_item_obj.additional_properties = (
            d
        )
        return enumerations_list_post_request_data_item_attributes_options_item_obj

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
