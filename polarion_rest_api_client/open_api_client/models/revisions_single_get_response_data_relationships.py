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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revisions_single_get_response_data_relationships_author import (
        RevisionsSingleGetResponseDataRelationshipsAuthor,
    )


T = TypeVar("T", bound="RevisionsSingleGetResponseDataRelationships")


@_attrs_define
class RevisionsSingleGetResponseDataRelationships:
    """
    Attributes:
        author (Union[Unset, RevisionsSingleGetResponseDataRelationshipsAuthor]):
    """

    author: Union[
        Unset, "RevisionsSingleGetResponseDataRelationshipsAuthor"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revisions_single_get_response_data_relationships_author import (
            RevisionsSingleGetResponseDataRelationshipsAuthor,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: Union[Unset, RevisionsSingleGetResponseDataRelationshipsAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                RevisionsSingleGetResponseDataRelationshipsAuthor.from_dict(
                    _author
                )
            )

        revisions_single_get_response_data_relationships_obj = cls(
            author=author,
        )

        revisions_single_get_response_data_relationships_obj.additional_properties = d
        return revisions_single_get_response_data_relationships_obj

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
