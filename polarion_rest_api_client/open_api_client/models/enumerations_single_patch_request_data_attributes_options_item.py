# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="EnumerationsSinglePatchRequestDataAttributesOptionsItem"
)


@_attrs_define
class EnumerationsSinglePatchRequestDataAttributesOptionsItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: open.
        name (Union[Unset, str]):  Example: Open.
        color (Union[Unset, str]):  Example: #F9FF4D.
        description (Union[Unset, str]):  Example: Description.
        hidden (Union[Unset, bool]):
        default (Union[Unset, bool]):  Example: True.
        parent (Union[Unset, bool]):  Example: True.
        opposite_name (Union[Unset, str]):  Example: Opposite Name.
        column_width (Union[Unset, str]):  Example: 90%.
        icon_url (Union[Unset, str]):  Example: /polarion/icons/default/enums/status_open.gif.
        create_defect (Union[Unset, bool]):  Example: True.
        template_work_item (Union[Unset, str]):  Example: exampleTemplate.
        min_value (Union[Unset, float]):  Example: 30.0.
        requires_signature_for_test_case_execution (Union[Unset, bool]):  Example: True.
        terminal (Union[Unset, bool]):  Example: True.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    default: Union[Unset, bool] = UNSET
    parent: Union[Unset, bool] = UNSET
    opposite_name: Union[Unset, str] = UNSET
    column_width: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    create_defect: Union[Unset, bool] = UNSET
    template_work_item: Union[Unset, str] = UNSET
    min_value: Union[Unset, float] = UNSET
    requires_signature_for_test_case_execution: Union[Unset, bool] = UNSET
    terminal: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        color = self.color

        description = self.description

        hidden = self.hidden

        default = self.default

        parent = self.parent

        opposite_name = self.opposite_name

        column_width = self.column_width

        icon_url = self.icon_url

        create_defect = self.create_defect

        template_work_item = self.template_work_item

        min_value = self.min_value

        requires_signature_for_test_case_execution = (
            self.requires_signature_for_test_case_execution
        )

        terminal = self.terminal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if default is not UNSET:
            field_dict["default"] = default
        if parent is not UNSET:
            field_dict["parent"] = parent
        if opposite_name is not UNSET:
            field_dict["oppositeName"] = opposite_name
        if column_width is not UNSET:
            field_dict["columnWidth"] = column_width
        if icon_url is not UNSET:
            field_dict["iconURL"] = icon_url
        if create_defect is not UNSET:
            field_dict["createDefect"] = create_defect
        if template_work_item is not UNSET:
            field_dict["templateWorkItem"] = template_work_item
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if requires_signature_for_test_case_execution is not UNSET:
            field_dict["requiresSignatureForTestCaseExecution"] = (
                requires_signature_for_test_case_execution
            )
        if terminal is not UNSET:
            field_dict["terminal"] = terminal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        default = d.pop("default", UNSET)

        parent = d.pop("parent", UNSET)

        opposite_name = d.pop("oppositeName", UNSET)

        column_width = d.pop("columnWidth", UNSET)

        icon_url = d.pop("iconURL", UNSET)

        create_defect = d.pop("createDefect", UNSET)

        template_work_item = d.pop("templateWorkItem", UNSET)

        min_value = d.pop("minValue", UNSET)

        requires_signature_for_test_case_execution = d.pop(
            "requiresSignatureForTestCaseExecution", UNSET
        )

        terminal = d.pop("terminal", UNSET)

        enumerations_single_patch_request_data_attributes_options_item_obj = cls(
            id=id,
            name=name,
            color=color,
            description=description,
            hidden=hidden,
            default=default,
            parent=parent,
            opposite_name=opposite_name,
            column_width=column_width,
            icon_url=icon_url,
            create_defect=create_defect,
            template_work_item=template_work_item,
            min_value=min_value,
            requires_signature_for_test_case_execution=requires_signature_for_test_case_execution,
            terminal=terminal,
        )

        enumerations_single_patch_request_data_attributes_options_item_obj.additional_properties = (
            d
        )
        return (
            enumerations_single_patch_request_data_attributes_options_item_obj
        )

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
