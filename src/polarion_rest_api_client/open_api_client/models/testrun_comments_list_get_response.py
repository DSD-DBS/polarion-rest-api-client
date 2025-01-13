# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrun_comments_list_get_response_data_item import (
        TestrunCommentsListGetResponseDataItem,
    )
    from ..models.testrun_comments_list_get_response_included_item import (
        TestrunCommentsListGetResponseIncludedItem,
    )
    from ..models.testrun_comments_list_get_response_links import (
        TestrunCommentsListGetResponseLinks,
    )
    from ..models.testrun_comments_list_get_response_meta import (
        TestrunCommentsListGetResponseMeta,
    )


T = TypeVar("T", bound="TestrunCommentsListGetResponse")


@_attrs_define
class TestrunCommentsListGetResponse:
    """
    Attributes:
        data (Union[Unset, List['TestrunCommentsListGetResponseDataItem']]):
        included (Union[Unset, List['TestrunCommentsListGetResponseIncludedItem']]): Related entities might be returned,
            see <a href="https://docs.sw.siemens.com/en-
            US/doc/230235217/PL20231017526942799.polarion_help_sc.xid2134849/xid2134871" target="_blank">REST API User
            Guide</a>.
        links (Union[Unset, TestrunCommentsListGetResponseLinks]):
        meta (Union[Unset, TestrunCommentsListGetResponseMeta]):
    """

    data: Union[Unset, List["TestrunCommentsListGetResponseDataItem"]] = UNSET
    included: Union[
        Unset, List["TestrunCommentsListGetResponseIncludedItem"]
    ] = UNSET
    links: Union[Unset, "TestrunCommentsListGetResponseLinks"] = UNSET
    meta: Union[Unset, "TestrunCommentsListGetResponseMeta"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        included: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrun_comments_list_get_response_data_item import (
            TestrunCommentsListGetResponseDataItem,
        )
        from ..models.testrun_comments_list_get_response_included_item import (
            TestrunCommentsListGetResponseIncludedItem,
        )
        from ..models.testrun_comments_list_get_response_links import (
            TestrunCommentsListGetResponseLinks,
        )
        from ..models.testrun_comments_list_get_response_meta import (
            TestrunCommentsListGetResponseMeta,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = TestrunCommentsListGetResponseDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = (
                TestrunCommentsListGetResponseIncludedItem.from_dict(
                    included_item_data
                )
            )

            included.append(included_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, TestrunCommentsListGetResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TestrunCommentsListGetResponseLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, TestrunCommentsListGetResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = TestrunCommentsListGetResponseMeta.from_dict(_meta)

        testrun_comments_list_get_response_obj = cls(
            data=data,
            included=included,
            links=links,
            meta=meta,
        )

        testrun_comments_list_get_response_obj.additional_properties = d
        return testrun_comments_list_get_response_obj

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
