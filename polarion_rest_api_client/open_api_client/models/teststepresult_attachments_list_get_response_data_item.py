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

from ..models.teststepresult_attachments_list_get_response_data_item_type import (
    TeststepresultAttachmentsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststepresult_attachments_list_get_response_data_item_attributes import (
        TeststepresultAttachmentsListGetResponseDataItemAttributes,
    )
    from ..models.teststepresult_attachments_list_get_response_data_item_links import (
        TeststepresultAttachmentsListGetResponseDataItemLinks,
    )
    from ..models.teststepresult_attachments_list_get_response_data_item_meta import (
        TeststepresultAttachmentsListGetResponseDataItemMeta,
    )
    from ..models.teststepresult_attachments_list_get_response_data_item_relationships import (
        TeststepresultAttachmentsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="TeststepresultAttachmentsListGetResponseDataItem")


@_attrs_define
class TeststepresultAttachmentsListGetResponseDataItem:
    """
    Attributes:
        type_ (Union[Unset, TeststepresultAttachmentsListGetResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId/MyProjectId/MyTestcaseId/0/1/MyAttachmentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, TeststepresultAttachmentsListGetResponseDataItemAttributes]):
        relationships (Union[Unset, TeststepresultAttachmentsListGetResponseDataItemRelationships]):
        links (Union[Unset, TeststepresultAttachmentsListGetResponseDataItemLinks]):
        meta (Union[Unset, TeststepresultAttachmentsListGetResponseDataItemMeta]):
    """

    type_: Union[
        Unset, TeststepresultAttachmentsListGetResponseDataItemType
    ] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "TeststepresultAttachmentsListGetResponseDataItemAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "TeststepresultAttachmentsListGetResponseDataItemRelationships"
    ] = UNSET
    links: Union[
        Unset, "TeststepresultAttachmentsListGetResponseDataItemLinks"
    ] = UNSET
    meta: Union[
        Unset, "TeststepresultAttachmentsListGetResponseDataItemMeta"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        revision = self.revision

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststepresult_attachments_list_get_response_data_item_attributes import (
            TeststepresultAttachmentsListGetResponseDataItemAttributes,
        )
        from ..models.teststepresult_attachments_list_get_response_data_item_links import (
            TeststepresultAttachmentsListGetResponseDataItemLinks,
        )
        from ..models.teststepresult_attachments_list_get_response_data_item_meta import (
            TeststepresultAttachmentsListGetResponseDataItemMeta,
        )
        from ..models.teststepresult_attachments_list_get_response_data_item_relationships import (
            TeststepresultAttachmentsListGetResponseDataItemRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[
            Unset, TeststepresultAttachmentsListGetResponseDataItemType
        ]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TeststepresultAttachmentsListGetResponseDataItemType(
                _type_
            )

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, TeststepresultAttachmentsListGetResponseDataItemAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TeststepresultAttachmentsListGetResponseDataItemAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset,
            TeststepresultAttachmentsListGetResponseDataItemRelationships,
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = TeststepresultAttachmentsListGetResponseDataItemRelationships.from_dict(
                _relationships
            )

        _links = d.pop("links", UNSET)
        links: Union[
            Unset, TeststepresultAttachmentsListGetResponseDataItemLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TeststepresultAttachmentsListGetResponseDataItemLinks.from_dict(
                _links
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[
            Unset, TeststepresultAttachmentsListGetResponseDataItemMeta
        ]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = (
                TeststepresultAttachmentsListGetResponseDataItemMeta.from_dict(
                    _meta
                )
            )

        teststepresult_attachments_list_get_response_data_item_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        teststepresult_attachments_list_get_response_data_item_obj.additional_properties = d
        return teststepresult_attachments_list_get_response_data_item_obj

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
