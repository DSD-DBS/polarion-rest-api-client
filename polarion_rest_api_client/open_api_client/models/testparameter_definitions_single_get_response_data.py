# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testparameter_definitions_single_get_response_data_type import (
    TestparameterDefinitionsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testparameter_definitions_single_get_response_data_attributes import (
        TestparameterDefinitionsSingleGetResponseDataAttributes,
    )
    from ..models.testparameter_definitions_single_get_response_data_links import (
        TestparameterDefinitionsSingleGetResponseDataLinks,
    )
    from ..models.testparameter_definitions_single_get_response_data_meta import (
        TestparameterDefinitionsSingleGetResponseDataMeta,
    )


T = TypeVar("T", bound="TestparameterDefinitionsSingleGetResponseData")


@_attrs_define
class TestparameterDefinitionsSingleGetResponseData:
    """
    Attributes:
        type (Union[Unset, TestparameterDefinitionsSingleGetResponseDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestParamDefinition.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, TestparameterDefinitionsSingleGetResponseDataAttributes]):
        meta (Union[Unset, TestparameterDefinitionsSingleGetResponseDataMeta]):
        links (Union[Unset, TestparameterDefinitionsSingleGetResponseDataLinks]):
    """

    type: Union[
        Unset, TestparameterDefinitionsSingleGetResponseDataType
    ] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "TestparameterDefinitionsSingleGetResponseDataAttributes"
    ] = UNSET
    meta: Union[
        Unset, "TestparameterDefinitionsSingleGetResponseDataMeta"
    ] = UNSET
    links: Union[
        Unset, "TestparameterDefinitionsSingleGetResponseDataLinks"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        revision = self.revision

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if meta is not UNSET:
            field_dict["meta"] = meta
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testparameter_definitions_single_get_response_data_attributes import (
            TestparameterDefinitionsSingleGetResponseDataAttributes,
        )
        from ..models.testparameter_definitions_single_get_response_data_links import (
            TestparameterDefinitionsSingleGetResponseDataLinks,
        )
        from ..models.testparameter_definitions_single_get_response_data_meta import (
            TestparameterDefinitionsSingleGetResponseDataMeta,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, TestparameterDefinitionsSingleGetResponseDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestparameterDefinitionsSingleGetResponseDataType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, TestparameterDefinitionsSingleGetResponseDataAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TestparameterDefinitionsSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, TestparameterDefinitionsSingleGetResponseDataMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = TestparameterDefinitionsSingleGetResponseDataMeta.from_dict(
                _meta
            )

        _links = d.pop("links", UNSET)
        links: Union[Unset, TestparameterDefinitionsSingleGetResponseDataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = (
                TestparameterDefinitionsSingleGetResponseDataLinks.from_dict(
                    _links
                )
            )

        testparameter_definitions_single_get_response_data_obj = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            meta=meta,
            links=links,
        )

        testparameter_definitions_single_get_response_data_obj.additional_properties = (
            d
        )
        return testparameter_definitions_single_get_response_data_obj

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