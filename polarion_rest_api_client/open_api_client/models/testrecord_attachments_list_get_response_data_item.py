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

from ..models.testrecord_attachments_list_get_response_data_item_type import (
    TestrecordAttachmentsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrecord_attachments_list_get_response_data_item_attributes import (
        TestrecordAttachmentsListGetResponseDataItemAttributes,
    )
    from ..models.testrecord_attachments_list_get_response_data_item_links import (
        TestrecordAttachmentsListGetResponseDataItemLinks,
    )
    from ..models.testrecord_attachments_list_get_response_data_item_meta import (
        TestrecordAttachmentsListGetResponseDataItemMeta,
    )
    from ..models.testrecord_attachments_list_get_response_data_item_relationships import (
        TestrecordAttachmentsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="TestrecordAttachmentsListGetResponseDataItem")


@_attrs_define
class TestrecordAttachmentsListGetResponseDataItem:
    """
    Attributes:
        type_ (Union[Unset, TestrecordAttachmentsListGetResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId/MyProjectId/MyTestcaseId/0/MyAttachmentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, TestrecordAttachmentsListGetResponseDataItemAttributes]):
        relationships (Union[Unset, TestrecordAttachmentsListGetResponseDataItemRelationships]):
        links (Union[Unset, TestrecordAttachmentsListGetResponseDataItemLinks]):
        meta (Union[Unset, TestrecordAttachmentsListGetResponseDataItemMeta]):
    """

    type_: Union[Unset, TestrecordAttachmentsListGetResponseDataItemType] = (
        UNSET
    )
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "TestrecordAttachmentsListGetResponseDataItemAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "TestrecordAttachmentsListGetResponseDataItemRelationships"
    ] = UNSET
    links: Union[
        Unset, "TestrecordAttachmentsListGetResponseDataItemLinks"
    ] = UNSET
    meta: Union[Unset, "TestrecordAttachmentsListGetResponseDataItemMeta"] = (
        UNSET
    )
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
        from ..models.testrecord_attachments_list_get_response_data_item_attributes import (
            TestrecordAttachmentsListGetResponseDataItemAttributes,
        )
        from ..models.testrecord_attachments_list_get_response_data_item_links import (
            TestrecordAttachmentsListGetResponseDataItemLinks,
        )
        from ..models.testrecord_attachments_list_get_response_data_item_meta import (
            TestrecordAttachmentsListGetResponseDataItemMeta,
        )
        from ..models.testrecord_attachments_list_get_response_data_item_relationships import (
            TestrecordAttachmentsListGetResponseDataItemRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TestrecordAttachmentsListGetResponseDataItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TestrecordAttachmentsListGetResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, TestrecordAttachmentsListGetResponseDataItemAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TestrecordAttachmentsListGetResponseDataItemAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, TestrecordAttachmentsListGetResponseDataItemRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = TestrecordAttachmentsListGetResponseDataItemRelationships.from_dict(
                _relationships
            )

        _links = d.pop("links", UNSET)
        links: Union[Unset, TestrecordAttachmentsListGetResponseDataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = (
                TestrecordAttachmentsListGetResponseDataItemLinks.from_dict(
                    _links
                )
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, TestrecordAttachmentsListGetResponseDataItemMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = TestrecordAttachmentsListGetResponseDataItemMeta.from_dict(
                _meta
            )

        testrecord_attachments_list_get_response_data_item_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        testrecord_attachments_list_get_response_data_item_obj.additional_properties = d
        return testrecord_attachments_list_get_response_data_item_obj

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
