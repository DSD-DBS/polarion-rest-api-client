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
    from ..models.collections_single_patch_request_data_relationships_documents import (
        CollectionsSinglePatchRequestDataRelationshipsDocuments,
    )
    from ..models.collections_single_patch_request_data_relationships_rich_pages import (
        CollectionsSinglePatchRequestDataRelationshipsRichPages,
    )
    from ..models.collections_single_patch_request_data_relationships_upstream_collections import (
        CollectionsSinglePatchRequestDataRelationshipsUpstreamCollections,
    )


T = TypeVar("T", bound="CollectionsSinglePatchRequestDataRelationships")


@_attrs_define
class CollectionsSinglePatchRequestDataRelationships:
    """
    Attributes:
        documents (Union[Unset, CollectionsSinglePatchRequestDataRelationshipsDocuments]):
        rich_pages (Union[Unset, CollectionsSinglePatchRequestDataRelationshipsRichPages]):
        upstream_collections (Union[Unset, CollectionsSinglePatchRequestDataRelationshipsUpstreamCollections]):
    """

    documents: Union[
        Unset, "CollectionsSinglePatchRequestDataRelationshipsDocuments"
    ] = UNSET
    rich_pages: Union[
        Unset, "CollectionsSinglePatchRequestDataRelationshipsRichPages"
    ] = UNSET
    upstream_collections: Union[
        Unset,
        "CollectionsSinglePatchRequestDataRelationshipsUpstreamCollections",
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        documents: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        rich_pages: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rich_pages, Unset):
            rich_pages = self.rich_pages.to_dict()

        upstream_collections: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.upstream_collections, Unset):
            upstream_collections = self.upstream_collections.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documents is not UNSET:
            field_dict["documents"] = documents
        if rich_pages is not UNSET:
            field_dict["richPages"] = rich_pages
        if upstream_collections is not UNSET:
            field_dict["upstreamCollections"] = upstream_collections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_single_patch_request_data_relationships_documents import (
            CollectionsSinglePatchRequestDataRelationshipsDocuments,
        )
        from ..models.collections_single_patch_request_data_relationships_rich_pages import (
            CollectionsSinglePatchRequestDataRelationshipsRichPages,
        )
        from ..models.collections_single_patch_request_data_relationships_upstream_collections import (
            CollectionsSinglePatchRequestDataRelationshipsUpstreamCollections,
        )

        d = dict(src_dict)
        _documents = d.pop("documents", UNSET)
        documents: Union[
            Unset, CollectionsSinglePatchRequestDataRelationshipsDocuments
        ]
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = CollectionsSinglePatchRequestDataRelationshipsDocuments.from_dict(
                _documents
            )

        _rich_pages = d.pop("richPages", UNSET)
        rich_pages: Union[
            Unset, CollectionsSinglePatchRequestDataRelationshipsRichPages
        ]
        if isinstance(_rich_pages, Unset):
            rich_pages = UNSET
        else:
            rich_pages = CollectionsSinglePatchRequestDataRelationshipsRichPages.from_dict(
                _rich_pages
            )

        _upstream_collections = d.pop("upstreamCollections", UNSET)
        upstream_collections: Union[
            Unset,
            CollectionsSinglePatchRequestDataRelationshipsUpstreamCollections,
        ]
        if isinstance(_upstream_collections, Unset):
            upstream_collections = UNSET
        else:
            upstream_collections = CollectionsSinglePatchRequestDataRelationshipsUpstreamCollections.from_dict(
                _upstream_collections
            )

        collections_single_patch_request_data_relationships_obj = cls(
            documents=documents,
            rich_pages=rich_pages,
            upstream_collections=upstream_collections,
        )

        collections_single_patch_request_data_relationships_obj.additional_properties = d
        return collections_single_patch_request_data_relationships_obj

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
