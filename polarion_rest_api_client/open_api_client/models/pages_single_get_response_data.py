# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.pages_single_get_response_data_type import (
    PagesSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pages_single_get_response_data_attributes import (
        PagesSingleGetResponseDataAttributes,
    )
    from ..models.pages_single_get_response_data_links import (
        PagesSingleGetResponseDataLinks,
    )
    from ..models.pages_single_get_response_data_meta import (
        PagesSingleGetResponseDataMeta,
    )
    from ..models.pages_single_get_response_data_relationships import (
        PagesSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="PagesSingleGetResponseData")


@define
class PagesSingleGetResponseData:
    """
    Attributes
    ----------
    type : Union[Unset, PagesSingleGetResponseDataType]
    id : Union[Unset, str]
    revision : Union[Unset, str]
    attributes : Union[Unset, PagesSingleGetResponseDataAttributes]
    relationships : Union[Unset, PagesSingleGetResponseDataRelationships]
    meta : Union[Unset, PagesSingleGetResponseDataMeta]
    links : Union[Unset, PagesSingleGetResponseDataLinks]
    """

    type: Union[Unset, PagesSingleGetResponseDataType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[Unset, "PagesSingleGetResponseDataAttributes"] = UNSET
    relationships: Union[
        Unset, "PagesSingleGetResponseDataRelationships"
    ] = UNSET
    meta: Union[Unset, "PagesSingleGetResponseDataMeta"] = UNSET
    links: Union[Unset, "PagesSingleGetResponseDataLinks"] = UNSET
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
        from ..models.pages_single_get_response_data_attributes import (
            PagesSingleGetResponseDataAttributes,
        )
        from ..models.pages_single_get_response_data_links import (
            PagesSingleGetResponseDataLinks,
        )
        from ..models.pages_single_get_response_data_meta import (
            PagesSingleGetResponseDataMeta,
        )
        from ..models.pages_single_get_response_data_relationships import (
            PagesSingleGetResponseDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, PagesSingleGetResponseDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PagesSingleGetResponseDataType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, PagesSingleGetResponseDataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PagesSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, PagesSingleGetResponseDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = PagesSingleGetResponseDataRelationships.from_dict(
                _relationships
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, PagesSingleGetResponseDataMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PagesSingleGetResponseDataMeta.from_dict(_meta)

        _links = d.pop("links", UNSET)
        links: Union[Unset, PagesSingleGetResponseDataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PagesSingleGetResponseDataLinks.from_dict(_links)

        pages_single_get_response_data_obj = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            meta=meta,
            links=links,
        )

        pages_single_get_response_data_obj.additional_properties = d
        return pages_single_get_response_data_obj

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
