# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_parts_list_get_response_data_item_relationships_next_part import (
        DocumentPartsListGetResponseDataItemRelationshipsNextPart,
    )
    from ..models.document_parts_list_get_response_data_item_relationships_previous_part import (
        DocumentPartsListGetResponseDataItemRelationshipsPreviousPart,
    )
    from ..models.document_parts_list_get_response_data_item_relationships_work_item import (
        DocumentPartsListGetResponseDataItemRelationshipsWorkItem,
    )


T = TypeVar("T", bound="DocumentPartsListGetResponseDataItemRelationships")


@_attrs_define
class DocumentPartsListGetResponseDataItemRelationships:
    """
    Attributes:
        next_part (Union[Unset, DocumentPartsListGetResponseDataItemRelationshipsNextPart]):
        previous_part (Union[Unset, DocumentPartsListGetResponseDataItemRelationshipsPreviousPart]):
        work_item (Union[Unset, DocumentPartsListGetResponseDataItemRelationshipsWorkItem]):
    """

    next_part: Union[
        Unset, "DocumentPartsListGetResponseDataItemRelationshipsNextPart"
    ] = UNSET
    previous_part: Union[
        Unset, "DocumentPartsListGetResponseDataItemRelationshipsPreviousPart"
    ] = UNSET
    work_item: Union[
        Unset, "DocumentPartsListGetResponseDataItemRelationshipsWorkItem"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        next_part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.next_part, Unset):
            next_part = self.next_part.to_dict()

        previous_part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous_part, Unset):
            previous_part = self.previous_part.to_dict()

        work_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_item, Unset):
            work_item = self.work_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_part is not UNSET:
            field_dict["nextPart"] = next_part
        if previous_part is not UNSET:
            field_dict["previousPart"] = previous_part
        if work_item is not UNSET:
            field_dict["workItem"] = work_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_parts_list_get_response_data_item_relationships_next_part import (
            DocumentPartsListGetResponseDataItemRelationshipsNextPart,
        )
        from ..models.document_parts_list_get_response_data_item_relationships_previous_part import (
            DocumentPartsListGetResponseDataItemRelationshipsPreviousPart,
        )
        from ..models.document_parts_list_get_response_data_item_relationships_work_item import (
            DocumentPartsListGetResponseDataItemRelationshipsWorkItem,
        )

        d = src_dict.copy()
        _next_part = d.pop("nextPart", UNSET)
        next_part: Union[
            Unset, DocumentPartsListGetResponseDataItemRelationshipsNextPart
        ]
        if isinstance(_next_part, Unset):
            next_part = UNSET
        else:
            next_part = DocumentPartsListGetResponseDataItemRelationshipsNextPart.from_dict(
                _next_part
            )

        _previous_part = d.pop("previousPart", UNSET)
        previous_part: Union[
            Unset,
            DocumentPartsListGetResponseDataItemRelationshipsPreviousPart,
        ]
        if isinstance(_previous_part, Unset):
            previous_part = UNSET
        else:
            previous_part = DocumentPartsListGetResponseDataItemRelationshipsPreviousPart.from_dict(
                _previous_part
            )

        _work_item = d.pop("workItem", UNSET)
        work_item: Union[
            Unset, DocumentPartsListGetResponseDataItemRelationshipsWorkItem
        ]
        if isinstance(_work_item, Unset):
            work_item = UNSET
        else:
            work_item = DocumentPartsListGetResponseDataItemRelationshipsWorkItem.from_dict(
                _work_item
            )

        document_parts_list_get_response_data_item_relationships_obj = cls(
            next_part=next_part,
            previous_part=previous_part,
            work_item=work_item,
        )

        document_parts_list_get_response_data_item_relationships_obj.additional_properties = (
            d
        )
        return document_parts_list_get_response_data_item_relationships_obj

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
