# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.document_comments_single_get_response_data_type import (
    DocumentCommentsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_single_get_response_data_attributes import (
        DocumentCommentsSingleGetResponseDataAttributes,
    )
    from ..models.document_comments_single_get_response_data_links import (
        DocumentCommentsSingleGetResponseDataLinks,
    )
    from ..models.document_comments_single_get_response_data_meta import (
        DocumentCommentsSingleGetResponseDataMeta,
    )
    from ..models.document_comments_single_get_response_data_relationships import (
        DocumentCommentsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="DocumentCommentsSingleGetResponseData")


@define
class DocumentCommentsSingleGetResponseData:
    """
    Attributes
    ----------
    type : Union[Unset, DocumentCommentsSingleGetResponseDataType]
    id : Union[Unset, str]
    revision : Union[Unset, str]
    attributes : Union[Unset, DocumentCommentsSingleGetResponseDataAttributes]
    relationships : Union[Unset, DocumentCommentsSingleGetResponseDataRelationships]
    meta : Union[Unset, DocumentCommentsSingleGetResponseDataMeta]
    links : Union[Unset, DocumentCommentsSingleGetResponseDataLinks]
    """

    type: Union[Unset, DocumentCommentsSingleGetResponseDataType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "DocumentCommentsSingleGetResponseDataAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "DocumentCommentsSingleGetResponseDataRelationships"
    ] = UNSET
    meta: Union[Unset, "DocumentCommentsSingleGetResponseDataMeta"] = UNSET
    links: Union[Unset, "DocumentCommentsSingleGetResponseDataLinks"] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id
        revision = self.revision
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

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
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if meta is not UNSET:
            field_dict["meta"] = meta
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_comments_single_get_response_data_attributes import (
            DocumentCommentsSingleGetResponseDataAttributes,
        )
        from ..models.document_comments_single_get_response_data_links import (
            DocumentCommentsSingleGetResponseDataLinks,
        )
        from ..models.document_comments_single_get_response_data_meta import (
            DocumentCommentsSingleGetResponseDataMeta,
        )
        from ..models.document_comments_single_get_response_data_relationships import (
            DocumentCommentsSingleGetResponseDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DocumentCommentsSingleGetResponseDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DocumentCommentsSingleGetResponseDataType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, DocumentCommentsSingleGetResponseDataAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                DocumentCommentsSingleGetResponseDataAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, DocumentCommentsSingleGetResponseDataRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                DocumentCommentsSingleGetResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, DocumentCommentsSingleGetResponseDataMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DocumentCommentsSingleGetResponseDataMeta.from_dict(_meta)

        _links = d.pop("links", UNSET)
        links: Union[Unset, DocumentCommentsSingleGetResponseDataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentCommentsSingleGetResponseDataLinks.from_dict(
                _links
            )

        document_comments_single_get_response_data_obj = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            meta=meta,
            links=links,
        )

        document_comments_single_get_response_data_obj.additional_properties = (
            d
        )
        return document_comments_single_get_response_data_obj

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
