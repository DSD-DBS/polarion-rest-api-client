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
    from ..models.document_comments_single_get_response_data import (
        DocumentCommentsSingleGetResponseData,
    )
    from ..models.document_comments_single_get_response_included_item import (
        DocumentCommentsSingleGetResponseIncludedItem,
    )
    from ..models.document_comments_single_get_response_links import (
        DocumentCommentsSingleGetResponseLinks,
    )


T = TypeVar("T", bound="DocumentCommentsSingleGetResponse")


@_attrs_define
class DocumentCommentsSingleGetResponse:
    """
    Attributes:
        data (Union[Unset, DocumentCommentsSingleGetResponseData]):
        included (Union[Unset, list['DocumentCommentsSingleGetResponseIncludedItem']]): Related entities might be
            returned, see <a href="https://docs.sw.siemens.com/en-
            US/doc/230235217/PL20241023686685479.polarion_help_sc.xid2134849/xid2134871" target="_blank">REST API User
            Guide</a>.
        links (Union[Unset, DocumentCommentsSingleGetResponseLinks]):
    """

    data: Union[Unset, "DocumentCommentsSingleGetResponseData"] = UNSET
    included: Union[
        Unset, list["DocumentCommentsSingleGetResponseIncludedItem"]
    ] = UNSET
    links: Union[Unset, "DocumentCommentsSingleGetResponseLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        included: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_comments_single_get_response_data import (
            DocumentCommentsSingleGetResponseData,
        )
        from ..models.document_comments_single_get_response_included_item import (
            DocumentCommentsSingleGetResponseIncludedItem,
        )
        from ..models.document_comments_single_get_response_links import (
            DocumentCommentsSingleGetResponseLinks,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, DocumentCommentsSingleGetResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DocumentCommentsSingleGetResponseData.from_dict(_data)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = (
                DocumentCommentsSingleGetResponseIncludedItem.from_dict(
                    included_item_data
                )
            )

            included.append(included_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, DocumentCommentsSingleGetResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentCommentsSingleGetResponseLinks.from_dict(_links)

        document_comments_single_get_response_obj = cls(
            data=data,
            included=included,
            links=links,
        )

        document_comments_single_get_response_obj.additional_properties = d
        return document_comments_single_get_response_obj

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
