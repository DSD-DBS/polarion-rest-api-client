# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.projecttemplates_list_get_response_data_item_attributes_parameters import (
        ProjecttemplatesListGetResponseDataItemAttributesParameters,
    )


T = TypeVar("T", bound="ProjecttemplatesListGetResponseDataItemAttributes")


@_attrs_define
class ProjecttemplatesListGetResponseDataItemAttributes:
    """
    Attributes:
        custom_icon (Union[Unset, str]):
        description (Union[Unset, str]):
        distributions (Union[Unset, List[str]]):
        id (Union[Unset, str]):
        is_default (Union[Unset, bool]):
        name (Union[Unset, str]):
        parameters (Union[Unset, ProjecttemplatesListGetResponseDataItemAttributesParameters]):
    """

    custom_icon: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    distributions: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    parameters: Union[
        Unset, "ProjecttemplatesListGetResponseDataItemAttributesParameters"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        custom_icon = self.custom_icon

        description = self.description

        distributions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.distributions, Unset):
            distributions = self.distributions

        id = self.id

        is_default = self.is_default

        name = self.name

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_icon is not UNSET:
            field_dict["customIcon"] = custom_icon
        if description is not UNSET:
            field_dict["description"] = description
        if distributions is not UNSET:
            field_dict["distributions"] = distributions
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.projecttemplates_list_get_response_data_item_attributes_parameters import (
            ProjecttemplatesListGetResponseDataItemAttributesParameters,
        )

        d = src_dict.copy()
        custom_icon = d.pop("customIcon", UNSET)

        description = d.pop("description", UNSET)

        distributions = cast(List[str], d.pop("distributions", UNSET))

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        name = d.pop("name", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[
            Unset, ProjecttemplatesListGetResponseDataItemAttributesParameters
        ]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ProjecttemplatesListGetResponseDataItemAttributesParameters.from_dict(
                _parameters
            )

        projecttemplates_list_get_response_data_item_attributes_obj = cls(
            custom_icon=custom_icon,
            description=description,
            distributions=distributions,
            id=id,
            is_default=is_default,
            name=name,
            parameters=parameters,
        )

        projecttemplates_list_get_response_data_item_attributes_obj.additional_properties = (
            d
        )
        return projecttemplates_list_get_response_data_item_attributes_obj

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
