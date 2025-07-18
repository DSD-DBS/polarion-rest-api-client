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

from ..models.workitem_comments_list_get_response_data_item_type import (
    WorkitemCommentsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_comments_list_get_response_data_item_attributes import (
        WorkitemCommentsListGetResponseDataItemAttributes,
    )
    from ..models.workitem_comments_list_get_response_data_item_links import (
        WorkitemCommentsListGetResponseDataItemLinks,
    )
    from ..models.workitem_comments_list_get_response_data_item_meta import (
        WorkitemCommentsListGetResponseDataItemMeta,
    )
    from ..models.workitem_comments_list_get_response_data_item_relationships import (
        WorkitemCommentsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="WorkitemCommentsListGetResponseDataItem")


@_attrs_define
class WorkitemCommentsListGetResponseDataItem:
    """
    Attributes:
        type_ (Union[Unset, WorkitemCommentsListGetResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyWorkItemId/MyCommentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, WorkitemCommentsListGetResponseDataItemAttributes]):
        relationships (Union[Unset, WorkitemCommentsListGetResponseDataItemRelationships]):
        links (Union[Unset, WorkitemCommentsListGetResponseDataItemLinks]):
        meta (Union[Unset, WorkitemCommentsListGetResponseDataItemMeta]):
    """

    type_: Union[Unset, WorkitemCommentsListGetResponseDataItemType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "WorkitemCommentsListGetResponseDataItemAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "WorkitemCommentsListGetResponseDataItemRelationships"
    ] = UNSET
    links: Union[Unset, "WorkitemCommentsListGetResponseDataItemLinks"] = UNSET
    meta: Union[Unset, "WorkitemCommentsListGetResponseDataItemMeta"] = UNSET
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
        from ..models.workitem_comments_list_get_response_data_item_attributes import (
            WorkitemCommentsListGetResponseDataItemAttributes,
        )
        from ..models.workitem_comments_list_get_response_data_item_links import (
            WorkitemCommentsListGetResponseDataItemLinks,
        )
        from ..models.workitem_comments_list_get_response_data_item_meta import (
            WorkitemCommentsListGetResponseDataItemMeta,
        )
        from ..models.workitem_comments_list_get_response_data_item_relationships import (
            WorkitemCommentsListGetResponseDataItemRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, WorkitemCommentsListGetResponseDataItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WorkitemCommentsListGetResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, WorkitemCommentsListGetResponseDataItemAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                WorkitemCommentsListGetResponseDataItemAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, WorkitemCommentsListGetResponseDataItemRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                WorkitemCommentsListGetResponseDataItemRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: Union[Unset, WorkitemCommentsListGetResponseDataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkitemCommentsListGetResponseDataItemLinks.from_dict(
                _links
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, WorkitemCommentsListGetResponseDataItemMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = WorkitemCommentsListGetResponseDataItemMeta.from_dict(_meta)

        workitem_comments_list_get_response_data_item_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        workitem_comments_list_get_response_data_item_obj.additional_properties = d
        return workitem_comments_list_get_response_data_item_obj

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
