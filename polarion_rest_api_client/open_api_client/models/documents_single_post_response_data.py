# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.documents_single_post_response_data_type import (
    DocumentsSinglePostResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_single_post_response_data_attributes import (
        DocumentsSinglePostResponseDataAttributes,
    )
    from ..models.documents_single_post_response_data_links import (
        DocumentsSinglePostResponseDataLinks,
    )
    from ..models.documents_single_post_response_data_relationships import (
        DocumentsSinglePostResponseDataRelationships,
    )


T = TypeVar("T", bound="DocumentsSinglePostResponseData")


@_attrs_define
class DocumentsSinglePostResponseData:
    """
    Attributes:
        type (Union[Unset, DocumentsSinglePostResponseDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MySpaceId/MyDocumentId.
        attributes (Union[Unset, DocumentsSinglePostResponseDataAttributes]):
        relationships (Union[Unset, DocumentsSinglePostResponseDataRelationships]):
        links (Union[Unset, DocumentsSinglePostResponseDataLinks]):
    """

    type: Union[Unset, DocumentsSinglePostResponseDataType] = UNSET
    id: Union[Unset, str] = UNSET
    attributes: Union[Unset, "DocumentsSinglePostResponseDataAttributes"] = (
        UNSET
    )
    relationships: Union[
        Unset, "DocumentsSinglePostResponseDataRelationships"
    ] = UNSET
    links: Union[Unset, "DocumentsSinglePostResponseDataLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

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
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.documents_single_post_response_data_attributes import (
            DocumentsSinglePostResponseDataAttributes,
        )
        from ..models.documents_single_post_response_data_links import (
            DocumentsSinglePostResponseDataLinks,
        )
        from ..models.documents_single_post_response_data_relationships import (
            DocumentsSinglePostResponseDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DocumentsSinglePostResponseDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DocumentsSinglePostResponseDataType(_type)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, DocumentsSinglePostResponseDataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = DocumentsSinglePostResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, DocumentsSinglePostResponseDataRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                DocumentsSinglePostResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: Union[Unset, DocumentsSinglePostResponseDataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentsSinglePostResponseDataLinks.from_dict(_links)

        documents_single_post_response_data_obj = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
        )

        documents_single_post_response_data_obj.additional_properties = d
        return documents_single_post_response_data_obj

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
