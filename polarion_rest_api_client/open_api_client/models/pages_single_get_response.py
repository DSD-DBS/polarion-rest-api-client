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
    from ..models.pages_single_get_response_data import (
        PagesSingleGetResponseData,
    )
    from ..models.pages_single_get_response_included_item import (
        PagesSingleGetResponseIncludedItem,
    )
    from ..models.pages_single_get_response_links import (
        PagesSingleGetResponseLinks,
    )


T = TypeVar("T", bound="PagesSingleGetResponse")


@_attrs_define
class PagesSingleGetResponse:
    """
    Attributes:
        data (Union[Unset, PagesSingleGetResponseData]):
        included (Union[Unset, list['PagesSingleGetResponseIncludedItem']]): Related entities might be returned, see <a
            href="https://docs.sw.siemens.com/en-
            US/doc/230235217/PL20241023686685479.polarion_help_sc.xid2134849/xid2134871" target="_blank">REST API User
            Guide</a>.
        links (Union[Unset, PagesSingleGetResponseLinks]):
    """

    data: Union[Unset, "PagesSingleGetResponseData"] = UNSET
    included: Union[Unset, list["PagesSingleGetResponseIncludedItem"]] = UNSET
    links: Union[Unset, "PagesSingleGetResponseLinks"] = UNSET
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
        from ..models.pages_single_get_response_data import (
            PagesSingleGetResponseData,
        )
        from ..models.pages_single_get_response_included_item import (
            PagesSingleGetResponseIncludedItem,
        )
        from ..models.pages_single_get_response_links import (
            PagesSingleGetResponseLinks,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, PagesSingleGetResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PagesSingleGetResponseData.from_dict(_data)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = PagesSingleGetResponseIncludedItem.from_dict(
                included_item_data
            )

            included.append(included_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, PagesSingleGetResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PagesSingleGetResponseLinks.from_dict(_links)

        pages_single_get_response_obj = cls(
            data=data,
            included=included,
            links=links,
        )

        pages_single_get_response_obj.additional_properties = d
        return pages_single_get_response_obj

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
