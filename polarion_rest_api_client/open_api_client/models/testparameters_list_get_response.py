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
    from ..models.testparameters_list_get_response_data_item import (
        TestparametersListGetResponseDataItem,
    )
    from ..models.testparameters_list_get_response_included_item import (
        TestparametersListGetResponseIncludedItem,
    )
    from ..models.testparameters_list_get_response_links import (
        TestparametersListGetResponseLinks,
    )
    from ..models.testparameters_list_get_response_meta import (
        TestparametersListGetResponseMeta,
    )


T = TypeVar("T", bound="TestparametersListGetResponse")


@_attrs_define
class TestparametersListGetResponse:
    """
    Attributes:
        data (Union[Unset, list['TestparametersListGetResponseDataItem']]):
        included (Union[Unset, list['TestparametersListGetResponseIncludedItem']]): Related entities might be returned,
            see <a href="https://docs.sw.siemens.com/en-
            US/doc/230235217/PL20241023686685479.polarion_help_sc.xid2134849/xid2134871" target="_blank">REST API User
            Guide</a>.
        links (Union[Unset, TestparametersListGetResponseLinks]):
        meta (Union[Unset, TestparametersListGetResponseMeta]):
    """

    data: Union[Unset, list["TestparametersListGetResponseDataItem"]] = UNSET
    included: Union[
        Unset, list["TestparametersListGetResponseIncludedItem"]
    ] = UNSET
    links: Union[Unset, "TestparametersListGetResponseLinks"] = UNSET
    meta: Union[Unset, "TestparametersListGetResponseMeta"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        included: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testparameters_list_get_response_data_item import (
            TestparametersListGetResponseDataItem,
        )
        from ..models.testparameters_list_get_response_included_item import (
            TestparametersListGetResponseIncludedItem,
        )
        from ..models.testparameters_list_get_response_links import (
            TestparametersListGetResponseLinks,
        )
        from ..models.testparameters_list_get_response_meta import (
            TestparametersListGetResponseMeta,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = TestparametersListGetResponseDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = (
                TestparametersListGetResponseIncludedItem.from_dict(
                    included_item_data
                )
            )

            included.append(included_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, TestparametersListGetResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TestparametersListGetResponseLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, TestparametersListGetResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = TestparametersListGetResponseMeta.from_dict(_meta)

        testparameters_list_get_response_obj = cls(
            data=data,
            included=included,
            links=links,
            meta=meta,
        )

        testparameters_list_get_response_obj.additional_properties = d
        return testparameters_list_get_response_obj

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
