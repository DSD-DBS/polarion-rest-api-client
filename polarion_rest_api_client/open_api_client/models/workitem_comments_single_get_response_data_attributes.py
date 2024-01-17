# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_comments_single_get_response_data_attributes_text import (
        WorkitemCommentsSingleGetResponseDataAttributesText,
    )


T = TypeVar("T", bound="WorkitemCommentsSingleGetResponseDataAttributes")


@_attrs_define
class WorkitemCommentsSingleGetResponseDataAttributes:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        id (Union[Unset, str]):  Example: MyCommentId.
        resolved (Union[Unset, bool]):
        text (Union[Unset, WorkitemCommentsSingleGetResponseDataAttributesText]):
        title (Union[Unset, str]):  Example: Title.
    """

    created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    resolved: Union[Unset, bool] = UNSET
    text: Union[
        Unset, "WorkitemCommentsSingleGetResponseDataAttributesText"
    ] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        resolved = self.resolved

        text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workitem_comments_single_get_response_data_attributes_text import (
            WorkitemCommentsSingleGetResponseDataAttributesText,
        )

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        id = d.pop("id", UNSET)

        resolved = d.pop("resolved", UNSET)

        _text = d.pop("text", UNSET)
        text: Union[Unset, WorkitemCommentsSingleGetResponseDataAttributesText]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = (
                WorkitemCommentsSingleGetResponseDataAttributesText.from_dict(
                    _text
                )
            )

        title = d.pop("title", UNSET)

        workitem_comments_single_get_response_data_attributes_obj = cls(
            created=created,
            id=id,
            resolved=resolved,
            text=text,
            title=title,
        )

        workitem_comments_single_get_response_data_attributes_obj.additional_properties = (
            d
        )
        return workitem_comments_single_get_response_data_attributes_obj

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
