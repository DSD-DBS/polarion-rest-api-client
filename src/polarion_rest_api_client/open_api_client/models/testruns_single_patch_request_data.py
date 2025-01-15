# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testruns_single_patch_request_data_type import (
    TestrunsSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_single_patch_request_data_attributes import (
        TestrunsSinglePatchRequestDataAttributes,
    )
    from ..models.testruns_single_patch_request_data_relationships import (
        TestrunsSinglePatchRequestDataRelationships,
    )


T = TypeVar("T", bound="TestrunsSinglePatchRequestData")


@_attrs_define
class TestrunsSinglePatchRequestData:
    """Attributes type (Union[Unset, TestrunsSinglePatchRequestDataType]):

    id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId.
    attributes (Union[Unset, TestrunsSinglePatchRequestDataAttributes]):
    relationships (Union[Unset,
    TestrunsSinglePatchRequestDataRelationships]):
    """

    type: Unset | TestrunsSinglePatchRequestDataType = UNSET
    id: Unset | str = UNSET
    attributes: Union[Unset, "TestrunsSinglePatchRequestDataAttributes"] = (
        UNSET
    )
    relationships: Union[
        Unset, "TestrunsSinglePatchRequestDataRelationships"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Unset | dict[str, Any] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        from ..models.testruns_single_patch_request_data_attributes import (
            TestrunsSinglePatchRequestDataAttributes,
        )
        from ..models.testruns_single_patch_request_data_relationships import (
            TestrunsSinglePatchRequestDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Unset | TestrunsSinglePatchRequestDataType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunsSinglePatchRequestDataType(_type)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | TestrunsSinglePatchRequestDataAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TestrunsSinglePatchRequestDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Unset | TestrunsSinglePatchRequestDataRelationships
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                TestrunsSinglePatchRequestDataRelationships.from_dict(
                    _relationships
                )
            )

        testruns_single_patch_request_data_obj = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        testruns_single_patch_request_data_obj.additional_properties = d
        return testruns_single_patch_request_data_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
