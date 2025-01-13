# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PagesSingleGetResponseDataAttributes")


@_attrs_define
class PagesSingleGetResponseDataAttributes:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        page_name (Union[Unset, str]):  Example: MyRichPageId.
        space_id (Union[Unset, str]):  Example: MySpaceId.
        title (Union[Unset, str]):  Example: Title.
        updated (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
    """

    created: Union[Unset, datetime.datetime] = UNSET
    page_name: Union[Unset, str] = UNSET
    space_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        page_name = self.page_name

        space_id = self.space_id

        title = self.title

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if page_name is not UNSET:
            field_dict["pageName"] = page_name
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        page_name = d.pop("pageName", UNSET)

        space_id = d.pop("spaceId", UNSET)

        title = d.pop("title", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        pages_single_get_response_data_attributes_obj = cls(
            created=created,
            page_name=page_name,
            space_id=space_id,
            title=title,
            updated=updated,
        )

        pages_single_get_response_data_attributes_obj.additional_properties = d
        return pages_single_get_response_data_attributes_obj

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
