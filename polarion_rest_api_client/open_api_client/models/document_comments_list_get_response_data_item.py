# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.document_comments_list_get_response_data_item_type import (
    DocumentCommentsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_list_get_response_data_item_attributes import (
        DocumentCommentsListGetResponseDataItemAttributes,
    )
    from ..models.document_comments_list_get_response_data_item_links import (
        DocumentCommentsListGetResponseDataItemLinks,
    )
    from ..models.document_comments_list_get_response_data_item_meta import (
        DocumentCommentsListGetResponseDataItemMeta,
    )
    from ..models.document_comments_list_get_response_data_item_relationships import (
        DocumentCommentsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="DocumentCommentsListGetResponseDataItem")


@attr.s(auto_attribs=True)
class DocumentCommentsListGetResponseDataItem:
    """
    Attributes:
        type (Union[Unset, DocumentCommentsListGetResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MySpaceId/MyDocumentId/MyCommentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, DocumentCommentsListGetResponseDataItemAttributes]):
        relationships (Union[Unset, DocumentCommentsListGetResponseDataItemRelationships]):
        meta (Union[Unset, DocumentCommentsListGetResponseDataItemMeta]):
        links (Union[Unset, DocumentCommentsListGetResponseDataItemLinks]):
    """

    type: Union[Unset, DocumentCommentsListGetResponseDataItemType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "DocumentCommentsListGetResponseDataItemAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "DocumentCommentsListGetResponseDataItemRelationships"
    ] = UNSET
    meta: Union[Unset, "DocumentCommentsListGetResponseDataItemMeta"] = UNSET
    links: Union[Unset, "DocumentCommentsListGetResponseDataItemLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.document_comments_list_get_response_data_item_attributes import (
            DocumentCommentsListGetResponseDataItemAttributes,
        )
        from ..models.document_comments_list_get_response_data_item_links import (
            DocumentCommentsListGetResponseDataItemLinks,
        )
        from ..models.document_comments_list_get_response_data_item_meta import (
            DocumentCommentsListGetResponseDataItemMeta,
        )
        from ..models.document_comments_list_get_response_data_item_relationships import (
            DocumentCommentsListGetResponseDataItemRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DocumentCommentsListGetResponseDataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DocumentCommentsListGetResponseDataItemType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, DocumentCommentsListGetResponseDataItemAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                DocumentCommentsListGetResponseDataItemAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, DocumentCommentsListGetResponseDataItemRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                DocumentCommentsListGetResponseDataItemRelationships.from_dict(
                    _relationships
                )
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, DocumentCommentsListGetResponseDataItemMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DocumentCommentsListGetResponseDataItemMeta.from_dict(_meta)

        _links = d.pop("links", UNSET)
        links: Union[Unset, DocumentCommentsListGetResponseDataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentCommentsListGetResponseDataItemLinks.from_dict(
                _links
            )

        document_comments_list_get_response_data_item = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            meta=meta,
            links=links,
        )

        document_comments_list_get_response_data_item.additional_properties = d
        return document_comments_list_get_response_data_item

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
