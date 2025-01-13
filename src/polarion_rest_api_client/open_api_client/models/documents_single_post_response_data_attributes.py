# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_single_post_response_data_attributes_home_page_content import (
        DocumentsSinglePostResponseDataAttributesHomePageContent,
    )
    from ..models.documents_single_post_response_data_attributes_outline_numbering import (
        DocumentsSinglePostResponseDataAttributesOutlineNumbering,
    )
    from ..models.documents_single_post_response_data_attributes_rendering_layouts_item import (
        DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem,
    )


T = TypeVar("T", bound="DocumentsSinglePostResponseDataAttributes")


@_attrs_define
class DocumentsSinglePostResponseDataAttributes:
    """
    Attributes:
        auto_suspect (Union[Unset, bool]):
        branched_with_initialized_fields (Union[Unset, List[str]]):
        branched_with_query (Union[Unset, str]):  Example: Branched with Query.
        created (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        derived_fields (Union[Unset, List[str]]):
        derived_from_link_role (Union[Unset, str]):  Example: relates_to.
        home_page_content (Union[Unset, DocumentsSinglePostResponseDataAttributesHomePageContent]):
        module_folder (Union[Unset, str]):  Example: MySpaceId.
        outline_numbering (Union[Unset, DocumentsSinglePostResponseDataAttributesOutlineNumbering]):
        rendering_layouts (Union[Unset, List['DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem']]):
        status (Union[Unset, str]):  Example: draft.
        title (Union[Unset, str]):  Example: Title.
        type (Union[Unset, str]):  Example: req_specification.
        updated (Union[Unset, datetime.datetime]):  Example: 1970-01-01T00:00:00Z.
        uses_outline_numbering (Union[Unset, bool]):
    """

    auto_suspect: Union[Unset, bool] = UNSET
    branched_with_initialized_fields: Union[Unset, List[str]] = UNSET
    branched_with_query: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    derived_fields: Union[Unset, List[str]] = UNSET
    derived_from_link_role: Union[Unset, str] = UNSET
    home_page_content: Union[
        Unset, "DocumentsSinglePostResponseDataAttributesHomePageContent"
    ] = UNSET
    module_folder: Union[Unset, str] = UNSET
    outline_numbering: Union[
        Unset, "DocumentsSinglePostResponseDataAttributesOutlineNumbering"
    ] = UNSET
    rendering_layouts: Union[
        Unset,
        List["DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem"],
    ] = UNSET
    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    uses_outline_numbering: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        auto_suspect = self.auto_suspect

        branched_with_initialized_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.branched_with_initialized_fields, Unset):
            branched_with_initialized_fields = (
                self.branched_with_initialized_fields
            )

        branched_with_query = self.branched_with_query

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        derived_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.derived_fields, Unset):
            derived_fields = self.derived_fields

        derived_from_link_role = self.derived_from_link_role

        home_page_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        module_folder = self.module_folder

        outline_numbering: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outline_numbering, Unset):
            outline_numbering = self.outline_numbering.to_dict()

        rendering_layouts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rendering_layouts, Unset):
            rendering_layouts = []
            for rendering_layouts_item_data in self.rendering_layouts:
                rendering_layouts_item = rendering_layouts_item_data.to_dict()
                rendering_layouts.append(rendering_layouts_item)

        status = self.status

        title = self.title

        type = self.type

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        uses_outline_numbering = self.uses_outline_numbering

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_suspect is not UNSET:
            field_dict["autoSuspect"] = auto_suspect
        if branched_with_initialized_fields is not UNSET:
            field_dict["branchedWithInitializedFields"] = (
                branched_with_initialized_fields
            )
        if branched_with_query is not UNSET:
            field_dict["branchedWithQuery"] = branched_with_query
        if created is not UNSET:
            field_dict["created"] = created
        if derived_fields is not UNSET:
            field_dict["derivedFields"] = derived_fields
        if derived_from_link_role is not UNSET:
            field_dict["derivedFromLinkRole"] = derived_from_link_role
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if module_folder is not UNSET:
            field_dict["moduleFolder"] = module_folder
        if outline_numbering is not UNSET:
            field_dict["outlineNumbering"] = outline_numbering
        if rendering_layouts is not UNSET:
            field_dict["renderingLayouts"] = rendering_layouts
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if updated is not UNSET:
            field_dict["updated"] = updated
        if uses_outline_numbering is not UNSET:
            field_dict["usesOutlineNumbering"] = uses_outline_numbering

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.documents_single_post_response_data_attributes_home_page_content import (
            DocumentsSinglePostResponseDataAttributesHomePageContent,
        )
        from ..models.documents_single_post_response_data_attributes_outline_numbering import (
            DocumentsSinglePostResponseDataAttributesOutlineNumbering,
        )
        from ..models.documents_single_post_response_data_attributes_rendering_layouts_item import (
            DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem,
        )

        d = src_dict.copy()
        auto_suspect = d.pop("autoSuspect", UNSET)

        branched_with_initialized_fields = cast(
            List[str], d.pop("branchedWithInitializedFields", UNSET)
        )

        branched_with_query = d.pop("branchedWithQuery", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        derived_fields = cast(List[str], d.pop("derivedFields", UNSET))

        derived_from_link_role = d.pop("derivedFromLinkRole", UNSET)

        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: Union[
            Unset, DocumentsSinglePostResponseDataAttributesHomePageContent
        ]
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = DocumentsSinglePostResponseDataAttributesHomePageContent.from_dict(
                _home_page_content
            )

        module_folder = d.pop("moduleFolder", UNSET)

        _outline_numbering = d.pop("outlineNumbering", UNSET)
        outline_numbering: Union[
            Unset, DocumentsSinglePostResponseDataAttributesOutlineNumbering
        ]
        if isinstance(_outline_numbering, Unset):
            outline_numbering = UNSET
        else:
            outline_numbering = DocumentsSinglePostResponseDataAttributesOutlineNumbering.from_dict(
                _outline_numbering
            )

        rendering_layouts = []
        _rendering_layouts = d.pop("renderingLayouts", UNSET)
        for rendering_layouts_item_data in _rendering_layouts or []:
            rendering_layouts_item = DocumentsSinglePostResponseDataAttributesRenderingLayoutsItem.from_dict(
                rendering_layouts_item_data
            )

            rendering_layouts.append(rendering_layouts_item)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        uses_outline_numbering = d.pop("usesOutlineNumbering", UNSET)

        documents_single_post_response_data_attributes_obj = cls(
            auto_suspect=auto_suspect,
            branched_with_initialized_fields=branched_with_initialized_fields,
            branched_with_query=branched_with_query,
            created=created,
            derived_fields=derived_fields,
            derived_from_link_role=derived_from_link_role,
            home_page_content=home_page_content,
            module_folder=module_folder,
            outline_numbering=outline_numbering,
            rendering_layouts=rendering_layouts,
            status=status,
            title=title,
            type=type,
            updated=updated,
            uses_outline_numbering=uses_outline_numbering,
        )

        documents_single_post_response_data_attributes_obj.additional_properties = (
            d
        )
        return documents_single_post_response_data_attributes_obj

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
