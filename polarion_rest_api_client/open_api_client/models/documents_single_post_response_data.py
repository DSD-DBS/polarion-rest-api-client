# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

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
        type_ (Union[Unset, DocumentsSinglePostResponseDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MySpaceId/MyDocumentId.
        attributes (Union[Unset, DocumentsSinglePostResponseDataAttributes]):
        relationships (Union[Unset, DocumentsSinglePostResponseDataRelationships]):
        links (Union[Unset, DocumentsSinglePostResponseDataLinks]):
    """

    type_: Union[Unset, DocumentsSinglePostResponseDataType] = UNSET
    id: Union[Unset, str] = UNSET
    attributes: Union[Unset, "DocumentsSinglePostResponseDataAttributes"] = (
        UNSET
    )
    relationships: Union[
        Unset, "DocumentsSinglePostResponseDataRelationships"
    ] = UNSET
    links: Union[Unset, "DocumentsSinglePostResponseDataLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents_single_post_response_data_attributes import (
            DocumentsSinglePostResponseDataAttributes,
        )
        from ..models.documents_single_post_response_data_links import (
            DocumentsSinglePostResponseDataLinks,
        )
        from ..models.documents_single_post_response_data_relationships import (
            DocumentsSinglePostResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DocumentsSinglePostResponseDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentsSinglePostResponseDataType(_type_)

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
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
        )

        documents_single_post_response_data_obj.additional_properties = d
        return documents_single_post_response_data_obj

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
