# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.teststepresult_attachments_single_get_response_data_type import (
    TeststepresultAttachmentsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststepresult_attachments_single_get_response_data_attributes import (
        TeststepresultAttachmentsSingleGetResponseDataAttributes,
    )
    from ..models.teststepresult_attachments_single_get_response_data_links import (
        TeststepresultAttachmentsSingleGetResponseDataLinks,
    )
    from ..models.teststepresult_attachments_single_get_response_data_meta import (
        TeststepresultAttachmentsSingleGetResponseDataMeta,
    )
    from ..models.teststepresult_attachments_single_get_response_data_relationships import (
        TeststepresultAttachmentsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="TeststepresultAttachmentsSingleGetResponseData")


@_attrs_define
class TeststepresultAttachmentsSingleGetResponseData:
    """
    Attributes:
        type (Union[Unset, TeststepresultAttachmentsSingleGetResponseDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId/1234/MyProjectId/MyTestcaseId/0/1/MyAttachmentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, TeststepresultAttachmentsSingleGetResponseDataAttributes]):
        relationships (Union[Unset, TeststepresultAttachmentsSingleGetResponseDataRelationships]):
        meta (Union[Unset, TeststepresultAttachmentsSingleGetResponseDataMeta]):
        links (Union[Unset, TeststepresultAttachmentsSingleGetResponseDataLinks]):
    """

    type: Union[Unset, TeststepresultAttachmentsSingleGetResponseDataType] = (
        UNSET
    )
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "TeststepresultAttachmentsSingleGetResponseDataAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "TeststepresultAttachmentsSingleGetResponseDataRelationships"
    ] = UNSET
    meta: Union[
        Unset, "TeststepresultAttachmentsSingleGetResponseDataMeta"
    ] = UNSET
    links: Union[
        Unset, "TeststepresultAttachmentsSingleGetResponseDataLinks"
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
        from ..models.teststepresult_attachments_single_get_response_data_attributes import (
            TeststepresultAttachmentsSingleGetResponseDataAttributes,
        )
        from ..models.teststepresult_attachments_single_get_response_data_links import (
            TeststepresultAttachmentsSingleGetResponseDataLinks,
        )
        from ..models.teststepresult_attachments_single_get_response_data_meta import (
            TeststepresultAttachmentsSingleGetResponseDataMeta,
        )
        from ..models.teststepresult_attachments_single_get_response_data_relationships import (
            TeststepresultAttachmentsSingleGetResponseDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, TeststepresultAttachmentsSingleGetResponseDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TeststepresultAttachmentsSingleGetResponseDataType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, TeststepresultAttachmentsSingleGetResponseDataAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TeststepresultAttachmentsSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, TeststepresultAttachmentsSingleGetResponseDataRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = TeststepresultAttachmentsSingleGetResponseDataRelationships.from_dict(
                _relationships
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, TeststepresultAttachmentsSingleGetResponseDataMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = (
                TeststepresultAttachmentsSingleGetResponseDataMeta.from_dict(
                    _meta
                )
            )

        _links = d.pop("links", UNSET)
        links: Union[
            Unset, TeststepresultAttachmentsSingleGetResponseDataLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = (
                TeststepresultAttachmentsSingleGetResponseDataLinks.from_dict(
                    _links
                )
            )

        teststepresult_attachments_single_get_response_data_obj = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            meta=meta,
            links=links,
        )

        teststepresult_attachments_single_get_response_data_obj.additional_properties = (
            d
        )
        return teststepresult_attachments_single_get_response_data_obj

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
