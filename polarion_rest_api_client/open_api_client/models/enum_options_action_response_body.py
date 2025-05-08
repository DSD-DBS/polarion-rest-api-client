# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enum_options_action_response_body_data_item import (
        EnumOptionsActionResponseBodyDataItem,
    )
    from ..models.enum_options_action_response_body_links import (
        EnumOptionsActionResponseBodyLinks,
    )
    from ..models.enum_options_action_response_body_meta import (
        EnumOptionsActionResponseBodyMeta,
    )


T = TypeVar("T", bound="EnumOptionsActionResponseBody")


@_attrs_define
class EnumOptionsActionResponseBody:
    """
    Attributes:
        data (Union[Unset, list['EnumOptionsActionResponseBodyDataItem']]):
        links (Union[Unset, EnumOptionsActionResponseBodyLinks]):
        meta (Union[Unset, EnumOptionsActionResponseBodyMeta]):
    """

    data: Union[Unset, list["EnumOptionsActionResponseBodyDataItem"]] = UNSET
    links: Union[Unset, "EnumOptionsActionResponseBodyLinks"] = UNSET
    meta: Union[Unset, "EnumOptionsActionResponseBodyMeta"] = UNSET
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
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enum_options_action_response_body_data_item import (
            EnumOptionsActionResponseBodyDataItem,
        )
        from ..models.enum_options_action_response_body_links import (
            EnumOptionsActionResponseBodyLinks,
        )
        from ..models.enum_options_action_response_body_meta import (
            EnumOptionsActionResponseBodyMeta,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = EnumOptionsActionResponseBodyDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, EnumOptionsActionResponseBodyLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = EnumOptionsActionResponseBodyLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, EnumOptionsActionResponseBodyMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = EnumOptionsActionResponseBodyMeta.from_dict(_meta)

        enum_options_action_response_body_obj = cls(
            data=data,
            links=links,
            meta=meta,
        )

        enum_options_action_response_body_obj.additional_properties = d
        return enum_options_action_response_body_obj

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
