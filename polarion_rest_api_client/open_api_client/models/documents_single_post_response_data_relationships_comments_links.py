# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="DocumentsSinglePostResponseDataRelationshipsCommentsLinks"
)


@_attrs_define
class DocumentsSinglePostResponseDataRelationshipsCommentsLinks:
    """
    Attributes:
        related (Union[Unset, str]):  Example: server-host-name/application-
            path/projects/MyProjectId/spaces/MySpaceId/documents/MyDocumentId/comments?revision=1234.
    """

    related: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        related = self.related

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if related is not UNSET:
            field_dict["related"] = related

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        related = d.pop("related", UNSET)

        documents_single_post_response_data_relationships_comments_links_obj = cls(
            related=related,
        )

        documents_single_post_response_data_relationships_comments_links_obj.additional_properties = d
        return documents_single_post_response_data_relationships_comments_links_obj

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
