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
    from ..models.collections_single_get_response_data_relationships_author import (
        CollectionsSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.collections_single_get_response_data_relationships_documents import (
        CollectionsSingleGetResponseDataRelationshipsDocuments,
    )
    from ..models.collections_single_get_response_data_relationships_downstream_collections import (
        CollectionsSingleGetResponseDataRelationshipsDownstreamCollections,
    )
    from ..models.collections_single_get_response_data_relationships_project import (
        CollectionsSingleGetResponseDataRelationshipsProject,
    )
    from ..models.collections_single_get_response_data_relationships_reused_from import (
        CollectionsSingleGetResponseDataRelationshipsReusedFrom,
    )
    from ..models.collections_single_get_response_data_relationships_rich_pages import (
        CollectionsSingleGetResponseDataRelationshipsRichPages,
    )
    from ..models.collections_single_get_response_data_relationships_upstream_collections import (
        CollectionsSingleGetResponseDataRelationshipsUpstreamCollections,
    )


T = TypeVar("T", bound="CollectionsSingleGetResponseDataRelationships")


@_attrs_define
class CollectionsSingleGetResponseDataRelationships:
    """
    Attributes:
        author (Union[Unset, CollectionsSingleGetResponseDataRelationshipsAuthor]):
        documents (Union[Unset, CollectionsSingleGetResponseDataRelationshipsDocuments]):
        downstream_collections (Union[Unset, CollectionsSingleGetResponseDataRelationshipsDownstreamCollections]):
        project (Union[Unset, CollectionsSingleGetResponseDataRelationshipsProject]):
        reused_from (Union[Unset, CollectionsSingleGetResponseDataRelationshipsReusedFrom]):
        rich_pages (Union[Unset, CollectionsSingleGetResponseDataRelationshipsRichPages]):
        upstream_collections (Union[Unset, CollectionsSingleGetResponseDataRelationshipsUpstreamCollections]):
    """

    author: Union[
        Unset, "CollectionsSingleGetResponseDataRelationshipsAuthor"
    ] = UNSET
    documents: Union[
        Unset, "CollectionsSingleGetResponseDataRelationshipsDocuments"
    ] = UNSET
    downstream_collections: Union[
        Unset,
        "CollectionsSingleGetResponseDataRelationshipsDownstreamCollections",
    ] = UNSET
    project: Union[
        Unset, "CollectionsSingleGetResponseDataRelationshipsProject"
    ] = UNSET
    reused_from: Union[
        Unset, "CollectionsSingleGetResponseDataRelationshipsReusedFrom"
    ] = UNSET
    rich_pages: Union[
        Unset, "CollectionsSingleGetResponseDataRelationshipsRichPages"
    ] = UNSET
    upstream_collections: Union[
        Unset,
        "CollectionsSingleGetResponseDataRelationshipsUpstreamCollections",
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        documents: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        downstream_collections: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.downstream_collections, Unset):
            downstream_collections = self.downstream_collections.to_dict()

        project: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        reused_from: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reused_from, Unset):
            reused_from = self.reused_from.to_dict()

        rich_pages: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rich_pages, Unset):
            rich_pages = self.rich_pages.to_dict()

        upstream_collections: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.upstream_collections, Unset):
            upstream_collections = self.upstream_collections.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if documents is not UNSET:
            field_dict["documents"] = documents
        if downstream_collections is not UNSET:
            field_dict["downstreamCollections"] = downstream_collections
        if project is not UNSET:
            field_dict["project"] = project
        if reused_from is not UNSET:
            field_dict["reusedFrom"] = reused_from
        if rich_pages is not UNSET:
            field_dict["richPages"] = rich_pages
        if upstream_collections is not UNSET:
            field_dict["upstreamCollections"] = upstream_collections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_single_get_response_data_relationships_author import (
            CollectionsSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.collections_single_get_response_data_relationships_documents import (
            CollectionsSingleGetResponseDataRelationshipsDocuments,
        )
        from ..models.collections_single_get_response_data_relationships_downstream_collections import (
            CollectionsSingleGetResponseDataRelationshipsDownstreamCollections,
        )
        from ..models.collections_single_get_response_data_relationships_project import (
            CollectionsSingleGetResponseDataRelationshipsProject,
        )
        from ..models.collections_single_get_response_data_relationships_reused_from import (
            CollectionsSingleGetResponseDataRelationshipsReusedFrom,
        )
        from ..models.collections_single_get_response_data_relationships_rich_pages import (
            CollectionsSingleGetResponseDataRelationshipsRichPages,
        )
        from ..models.collections_single_get_response_data_relationships_upstream_collections import (
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollections,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: Union[
            Unset, CollectionsSingleGetResponseDataRelationshipsAuthor
        ]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                CollectionsSingleGetResponseDataRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _documents = d.pop("documents", UNSET)
        documents: Union[
            Unset, CollectionsSingleGetResponseDataRelationshipsDocuments
        ]
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = CollectionsSingleGetResponseDataRelationshipsDocuments.from_dict(
                _documents
            )

        _downstream_collections = d.pop("downstreamCollections", UNSET)
        downstream_collections: Union[
            Unset,
            CollectionsSingleGetResponseDataRelationshipsDownstreamCollections,
        ]
        if isinstance(_downstream_collections, Unset):
            downstream_collections = UNSET
        else:
            downstream_collections = CollectionsSingleGetResponseDataRelationshipsDownstreamCollections.from_dict(
                _downstream_collections
            )

        _project = d.pop("project", UNSET)
        project: Union[
            Unset, CollectionsSingleGetResponseDataRelationshipsProject
        ]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                CollectionsSingleGetResponseDataRelationshipsProject.from_dict(
                    _project
                )
            )

        _reused_from = d.pop("reusedFrom", UNSET)
        reused_from: Union[
            Unset, CollectionsSingleGetResponseDataRelationshipsReusedFrom
        ]
        if isinstance(_reused_from, Unset):
            reused_from = UNSET
        else:
            reused_from = CollectionsSingleGetResponseDataRelationshipsReusedFrom.from_dict(
                _reused_from
            )

        _rich_pages = d.pop("richPages", UNSET)
        rich_pages: Union[
            Unset, CollectionsSingleGetResponseDataRelationshipsRichPages
        ]
        if isinstance(_rich_pages, Unset):
            rich_pages = UNSET
        else:
            rich_pages = CollectionsSingleGetResponseDataRelationshipsRichPages.from_dict(
                _rich_pages
            )

        _upstream_collections = d.pop("upstreamCollections", UNSET)
        upstream_collections: Union[
            Unset,
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollections,
        ]
        if isinstance(_upstream_collections, Unset):
            upstream_collections = UNSET
        else:
            upstream_collections = CollectionsSingleGetResponseDataRelationshipsUpstreamCollections.from_dict(
                _upstream_collections
            )

        collections_single_get_response_data_relationships_obj = cls(
            author=author,
            documents=documents,
            downstream_collections=downstream_collections,
            project=project,
            reused_from=reused_from,
            rich_pages=rich_pages,
            upstream_collections=upstream_collections,
        )

        collections_single_get_response_data_relationships_obj.additional_properties = d
        return collections_single_get_response_data_relationships_obj

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
