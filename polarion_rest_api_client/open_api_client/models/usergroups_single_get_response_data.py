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

from ..models.usergroups_single_get_response_data_type import (
    UsergroupsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usergroups_single_get_response_data_attributes import (
        UsergroupsSingleGetResponseDataAttributes,
    )
    from ..models.usergroups_single_get_response_data_links import (
        UsergroupsSingleGetResponseDataLinks,
    )
    from ..models.usergroups_single_get_response_data_meta import (
        UsergroupsSingleGetResponseDataMeta,
    )
    from ..models.usergroups_single_get_response_data_relationships import (
        UsergroupsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="UsergroupsSingleGetResponseData")


@_attrs_define
class UsergroupsSingleGetResponseData:
    """
    Attributes:
        type_ (Union[Unset, UsergroupsSingleGetResponseDataType]):
        id (Union[Unset, str]):  Example: MyUserGroupId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, UsergroupsSingleGetResponseDataAttributes]):
        relationships (Union[Unset, UsergroupsSingleGetResponseDataRelationships]):
        links (Union[Unset, UsergroupsSingleGetResponseDataLinks]):
        meta (Union[Unset, UsergroupsSingleGetResponseDataMeta]):
    """

    type_: Union[Unset, UsergroupsSingleGetResponseDataType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[Unset, "UsergroupsSingleGetResponseDataAttributes"] = (
        UNSET
    )
    relationships: Union[
        Unset, "UsergroupsSingleGetResponseDataRelationships"
    ] = UNSET
    links: Union[Unset, "UsergroupsSingleGetResponseDataLinks"] = UNSET
    meta: Union[Unset, "UsergroupsSingleGetResponseDataMeta"] = UNSET
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
        from ..models.usergroups_single_get_response_data_attributes import (
            UsergroupsSingleGetResponseDataAttributes,
        )
        from ..models.usergroups_single_get_response_data_links import (
            UsergroupsSingleGetResponseDataLinks,
        )
        from ..models.usergroups_single_get_response_data_meta import (
            UsergroupsSingleGetResponseDataMeta,
        )
        from ..models.usergroups_single_get_response_data_relationships import (
            UsergroupsSingleGetResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, UsergroupsSingleGetResponseDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UsergroupsSingleGetResponseDataType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, UsergroupsSingleGetResponseDataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UsergroupsSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, UsergroupsSingleGetResponseDataRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                UsergroupsSingleGetResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: Union[Unset, UsergroupsSingleGetResponseDataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UsergroupsSingleGetResponseDataLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, UsergroupsSingleGetResponseDataMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = UsergroupsSingleGetResponseDataMeta.from_dict(_meta)

        usergroups_single_get_response_data_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        usergroups_single_get_response_data_obj.additional_properties = d
        return usergroups_single_get_response_data_obj

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
