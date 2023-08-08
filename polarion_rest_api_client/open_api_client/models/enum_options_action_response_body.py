# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

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


@define
class EnumOptionsActionResponseBody:
    """
    Attributes
    ----------
    meta : Union[Unset, EnumOptionsActionResponseBodyMeta]
    data : Union[Unset, List['EnumOptionsActionResponseBodyDataItem']]
    links : Union[Unset, EnumOptionsActionResponseBodyLinks]
    """

    meta: Union[Unset, "EnumOptionsActionResponseBodyMeta"] = UNSET
    data: Union[Unset, List["EnumOptionsActionResponseBodyDataItem"]] = UNSET
    links: Union[Unset, "EnumOptionsActionResponseBodyLinks"] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enum_options_action_response_body_data_item import (
            EnumOptionsActionResponseBodyDataItem,
        )
        from ..models.enum_options_action_response_body_links import (
            EnumOptionsActionResponseBodyLinks,
        )
        from ..models.enum_options_action_response_body_meta import (
            EnumOptionsActionResponseBodyMeta,
        )

        d = src_dict.copy()
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, EnumOptionsActionResponseBodyMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = EnumOptionsActionResponseBodyMeta.from_dict(_meta)

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

        enum_options_action_response_body_obj = cls(
            meta=meta,
            data=data,
            links=links,
        )

        enum_options_action_response_body_obj.additional_properties = d
        return enum_options_action_response_body_obj

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
