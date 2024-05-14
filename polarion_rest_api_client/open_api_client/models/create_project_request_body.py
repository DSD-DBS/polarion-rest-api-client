# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_project_request_body_params_type_0 import (
        CreateProjectRequestBodyParamsType0,
    )


T = TypeVar("T", bound="CreateProjectRequestBody")


@_attrs_define
class CreateProjectRequestBody:
    """
    Attributes:
        location (Union[Unset, str]): Location of the new Project to be created. Example: MyLocation.
        params (Union['CreateProjectRequestBodyParamsType0', None, Unset]): params of new Project to be created.
        project_id (Union[Unset, str]): Id of the new Project to be created. Example: MyProjectId.
        template_id (Union[None, Unset, str]): Id of the template to create the new Project from. Example:
            MyProjectTemplateId.
        tracker_prefix (Union[Unset, str]): Tracker prefix of the new Project to be created. Example: MyTrackerPrefix.
    """

    location: Union[Unset, str] = UNSET
    params: Union["CreateProjectRequestBodyParamsType0", None, Unset] = UNSET
    project_id: Union[Unset, str] = UNSET
    template_id: Union[None, Unset, str] = UNSET
    tracker_prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_project_request_body_params_type_0 import (
            CreateProjectRequestBodyParamsType0,
        )

        location = self.location

        params: Union[Dict[str, Any], None, Unset]
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, CreateProjectRequestBodyParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        project_id = self.project_id

        template_id: Union[None, Unset, str]
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        tracker_prefix = self.tracker_prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if params is not UNSET:
            field_dict["params"] = params
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if tracker_prefix is not UNSET:
            field_dict["trackerPrefix"] = tracker_prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_project_request_body_params_type_0 import (
            CreateProjectRequestBodyParamsType0,
        )

        d = src_dict.copy()
        location = d.pop("location", UNSET)

        def _parse_params(
            data: object,
        ) -> Union["CreateProjectRequestBodyParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = CreateProjectRequestBodyParamsType0.from_dict(
                    data
                )

                return params_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["CreateProjectRequestBodyParamsType0", None, Unset], data
            )

        params = _parse_params(d.pop("params", UNSET))

        project_id = d.pop("projectId", UNSET)

        def _parse_template_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        template_id = _parse_template_id(d.pop("templateId", UNSET))

        tracker_prefix = d.pop("trackerPrefix", UNSET)

        create_project_request_body_obj = cls(
            location=location,
            params=params,
            project_id=project_id,
            template_id=template_id,
            tracker_prefix=tracker_prefix,
        )

        create_project_request_body_obj.additional_properties = d
        return create_project_request_body_obj

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
