# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linkedoslcresources_list_post_response_data_item_type import (
    LinkedoslcresourcesListPostResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linkedoslcresources_list_post_response_data_item_links import (
        LinkedoslcresourcesListPostResponseDataItemLinks,
    )


T = TypeVar("T", bound="LinkedoslcresourcesListPostResponseDataItem")


@_attrs_define
class LinkedoslcresourcesListPostResponseDataItem:
    """
    Attributes:
        type (Union[Unset, LinkedoslcresourcesListPostResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyWorkItemId/http://server-host-
            name/ns/cm#relatedChangeRequest/http://server-host-name/application-
            path/oslc/services/projects/MyProjectId/workitems/MyWorkItemId.
        links (Union[Unset, LinkedoslcresourcesListPostResponseDataItemLinks]):
    """

    type: Union[Unset, LinkedoslcresourcesListPostResponseDataItemType] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "LinkedoslcresourcesListPostResponseDataItemLinks"] = (
        UNSET
    )
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
        from ..models.linkedoslcresources_list_post_response_data_item_links import (
            LinkedoslcresourcesListPostResponseDataItemLinks,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, LinkedoslcresourcesListPostResponseDataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = LinkedoslcresourcesListPostResponseDataItemType(_type)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, LinkedoslcresourcesListPostResponseDataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = LinkedoslcresourcesListPostResponseDataItemLinks.from_dict(
                _links
            )

        linkedoslcresources_list_post_response_data_item_obj = cls(
            type=type,
            id=id,
            links=links,
        )

        linkedoslcresources_list_post_response_data_item_obj.additional_properties = (
            d
        )
        return linkedoslcresources_list_post_response_data_item_obj

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
