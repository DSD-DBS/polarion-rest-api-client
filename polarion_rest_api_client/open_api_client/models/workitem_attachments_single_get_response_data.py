# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workitem_attachments_single_get_response_data_type import (
    WorkitemAttachmentsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_attachments_single_get_response_data_attributes import (
        WorkitemAttachmentsSingleGetResponseDataAttributes,
    )
    from ..models.workitem_attachments_single_get_response_data_links import (
        WorkitemAttachmentsSingleGetResponseDataLinks,
    )
    from ..models.workitem_attachments_single_get_response_data_meta import (
        WorkitemAttachmentsSingleGetResponseDataMeta,
    )
    from ..models.workitem_attachments_single_get_response_data_relationships import (
        WorkitemAttachmentsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="WorkitemAttachmentsSingleGetResponseData")


@_attrs_define
class WorkitemAttachmentsSingleGetResponseData:
    """
    Attributes:
        type (Union[Unset, WorkitemAttachmentsSingleGetResponseDataType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyWorkItemId/MyAttachmentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, WorkitemAttachmentsSingleGetResponseDataAttributes]):
        relationships (Union[Unset, WorkitemAttachmentsSingleGetResponseDataRelationships]):
        links (Union[Unset, WorkitemAttachmentsSingleGetResponseDataLinks]):
        meta (Union[Unset, WorkitemAttachmentsSingleGetResponseDataMeta]):
    """

    type: Union[Unset, WorkitemAttachmentsSingleGetResponseDataType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "WorkitemAttachmentsSingleGetResponseDataAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "WorkitemAttachmentsSingleGetResponseDataRelationships"
    ] = UNSET
    links: Union[Unset, "WorkitemAttachmentsSingleGetResponseDataLinks"] = (
        UNSET
    )
    meta: Union[Unset, "WorkitemAttachmentsSingleGetResponseDataMeta"] = UNSET
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

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

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
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitem_attachments_single_get_response_data_attributes import (
            WorkitemAttachmentsSingleGetResponseDataAttributes,
        )
        from ..models.workitem_attachments_single_get_response_data_links import (
            WorkitemAttachmentsSingleGetResponseDataLinks,
        )
        from ..models.workitem_attachments_single_get_response_data_meta import (
            WorkitemAttachmentsSingleGetResponseDataMeta,
        )
        from ..models.workitem_attachments_single_get_response_data_relationships import (
            WorkitemAttachmentsSingleGetResponseDataRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, WorkitemAttachmentsSingleGetResponseDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WorkitemAttachmentsSingleGetResponseDataType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, WorkitemAttachmentsSingleGetResponseDataAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                WorkitemAttachmentsSingleGetResponseDataAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, WorkitemAttachmentsSingleGetResponseDataRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = WorkitemAttachmentsSingleGetResponseDataRelationships.from_dict(
                _relationships
            )

        _links = d.pop("links", UNSET)
        links: Union[Unset, WorkitemAttachmentsSingleGetResponseDataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkitemAttachmentsSingleGetResponseDataLinks.from_dict(
                _links
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, WorkitemAttachmentsSingleGetResponseDataMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = WorkitemAttachmentsSingleGetResponseDataMeta.from_dict(
                _meta
            )

        workitem_attachments_single_get_response_data_obj = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        workitem_attachments_single_get_response_data_obj.additional_properties = (
            d
        )
        return workitem_attachments_single_get_response_data_obj

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
