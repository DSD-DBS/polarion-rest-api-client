# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrun_attachments_list_post_response_data_item_type import (
    TestrunAttachmentsListPostResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrun_attachments_list_post_response_data_item_links import (
        TestrunAttachmentsListPostResponseDataItemLinks,
    )


T = TypeVar("T", bound="TestrunAttachmentsListPostResponseDataItem")


@_attrs_define
class TestrunAttachmentsListPostResponseDataItem:
    """
    Attributes:
        type (Union[Unset, TestrunAttachmentsListPostResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId/MyAttachmentId.
        links (Union[Unset, TestrunAttachmentsListPostResponseDataItemLinks]):
    """

    type: Union[Unset, TestrunAttachmentsListPostResponseDataItemType] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[
        Unset, "TestrunAttachmentsListPostResponseDataItemLinks"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrun_attachments_list_post_response_data_item_links import (
            TestrunAttachmentsListPostResponseDataItemLinks,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, TestrunAttachmentsListPostResponseDataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunAttachmentsListPostResponseDataItemType(_type)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, TestrunAttachmentsListPostResponseDataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TestrunAttachmentsListPostResponseDataItemLinks.from_dict(
                _links
            )

        testrun_attachments_list_post_response_data_item_obj = cls(
            type=type,
            id=id,
            links=links,
        )

        testrun_attachments_list_post_response_data_item_obj.additional_properties = (
            d
        )
        return testrun_attachments_list_post_response_data_item_obj

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